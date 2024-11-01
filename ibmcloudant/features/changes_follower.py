# coding: utf-8

# © Copyright IBM Corporation 2022, 2024.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
A helper for using the changes feed.
"""
import logging
import time
import random
import math
from datetime import datetime, timezone, timedelta
import functools
from queue import Queue
from threading import Thread, Event

from enum import Enum, auto
from typing import Dict, Iterator

from ibm_cloud_sdk_core import ApiException

from ibmcloudant.cloudant_v1 import (
    CloudantV1,
    PostChangesEnums,
    ChangesResultItem,
)

# max timedelta in milliseconds
_FOREVER = round(timedelta.max.total_seconds() * 1000) - 1
# 1 minute in millisec
_MIN_CLIENT_TIMEOUT = 60000
# To give the changes request a chance to be answered
# before the client timeout it is set to 3 seconds less.
_LONGPOLL_TIMEOUT = _MIN_CLIENT_TIMEOUT - 3000
_BATCH_SIZE = 10000

# Base delay in milliseconds between unsuccessful attempts to pull changes feed
# in presence of transient errors
_BASE_DELAY = 100
# Once we reach this number of retries we'll be capping the backoff
_EXP_RETRY_GATE = int(math.log(_LONGPOLL_TIMEOUT / _BASE_DELAY) / math.log(2))


class _Mode(Enum):
    """
    Enums for changes follower's operation mode.
    """
    FINITE = auto()
    LISTEN = auto()


class _TransientErrorSuppression(Enum):
    """
    Enums for changes follower's transient errors suppression mode.
    """
    ALWAYS = auto()
    NEVER = auto()
    TIMER = auto()


class _ChangesFollowerIterator:
    """
    The ChangesFollowerIterator implements iterator interface.

    This class is for internal use by ChangesFollower, which provides
    the user facing API.

    Args:
        changes_caller: A partial function that pulls changes feed from CouchDB
        for a given "since" parameter.
        mode: Enum representing either one-off consumption of changes feed (FINITE)
        or constant following the changes feed (LISTEN)
        error_tolerance: The duration to suppress errors,
        measured from the previous successful request.
    """

    def __init__(
        self, changes_caller, mode: _Mode, error_tolerance: int
    ) -> None:
        self.changes_caller = changes_caller
        self._changes_iter = iter([])
        self.mode = mode
        self._transient_suppression = _TransientErrorSuppression.TIMER
        if error_tolerance == 0:
            self._transient_suppression = _TransientErrorSuppression.NEVER
        elif error_tolerance == _FOREVER:
            self._transient_suppression = _TransientErrorSuppression.ALWAYS
        self.error_tolerance = timedelta(milliseconds=error_tolerance)
        self.since = 'now' if mode is _Mode.LISTEN else '0'
        self._success_timestamp = datetime.now(timezone.utc)
        self._request_thread = Thread(target=self._request_callback)
        self._buffer = Queue()
        self._pending = None
        self._has_next = True
        self._retry = 0
        self._limit = None
        self._stop = Event()
        self.logger = logging.getLogger(__name__)

    @property
    def limit(self) -> int:
        return self._limit

    @limit.setter
    def limit(self, value: int) -> None:
        if value < 0:
            raise ValueError('Limit must not be negative.')
        self._limit = value

    @property
    def since(self) -> str:
        return self._since

    @since.setter
    def since(self, value: str) -> None:
        self._since = value

    def _start(self) -> None:
        self._request_thread.start()

    def stop(self) -> None:
        # shortcut limit and cancel in-flight
        self.limit = 0
        self._stop.set()
        try:
            self._buffer.task_done()
        except Exception:
            pass
        self._request_thread.join()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.limit is not None and self.limit == 0:
                if not self._stop.is_set():
                    self.stop()
                raise StopIteration
            try:
                item = next(self._changes_iter)
                if self.limit is not None and self.limit > 0:
                    self.limit -= 1
                return item
            except StopIteration as exc:
                data = self._buffer.get()
                if self._stop.is_set():
                    raise StopIteration from exc
                if isinstance(data, Exception):
                    raise data from None
                self._changes_iter = iter(
                    (ChangesResultItem.from_dict(item) for item in data)
                )
                self._buffer.task_done()

    def _request_callback(self):
        while True:
            try:
                if not self._has_next or self._stop.is_set():
                    raise StopIteration
                result = self.changes_caller(since=self.since).get_result()
                self.since = result.get('last_seq')
                self._pending = result.get('pending')
                self._retry = 0
                if self._transient_suppression == _TransientErrorSuppression.TIMER:
                    self._success_timestamp = datetime.now(timezone.utc)
                if self.mode == _Mode.FINITE and self._pending == 0:
                    self._has_next = False
                results = result['results']
                self.logger.debug(f'_request_callback results {results}')
                self._buffer.join()
                if self._stop.is_set():
                    raise StopIteration
                self._buffer.put(results)
            except StopIteration as e:
                self.logger.debug('Iterator stopped.')
                self._buffer.join()
                self._buffer.put(e)
                break
            except Exception as e:
                self.logger.debug(f'Exception getting changes {e}')
                if (
                    self._transient_suppression == _TransientErrorSuppression.NEVER
                    or (
                        self._transient_suppression
                        == _TransientErrorSuppression.TIMER
                        and self._success_timestamp + self.error_tolerance
                        < datetime.now(timezone.utc)
                    )
                ):
                    self.logger.debug('Error tolerance deadline exceeded.')
                    self._buffer.join()
                    self._buffer.put(e)
                    break
                if type(e) is ApiException and e.status_code in [400, 401, 403, 404]:
                    self.logger.debug('Terminal error.')
                    self._buffer.join()
                    self._buffer.put(e)
                    break
                self.retry_delay()

    def retry_delay(self):
        """
        Method retry_delay implements full jitter delay algorithm.
        This is an exponential capped backoff with added jitter
        to spread retry calls in case of multiple followers
        started simultaneously for different feeds on the same account.

        The base delay is set to 100 ms and cap is set to the changes
        feed pull's timeout.

        Algorithm reference: https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/
        """
        if (self._retry >= _EXP_RETRY_GATE):
            exp_delay = _LONGPOLL_TIMEOUT
        else:
            exp_delay = pow(2, self._retry) * _BASE_DELAY
        jitter_delay = random.uniform(0, exp_delay)
        time.sleep(round(jitter_delay / 1000, 3))
        self._retry += 1


class ChangesFollower:
    """
    ChangesFollower is a helper for using the changes feed.

    There are two modes of operation:
        start_one_off() to fetch the changes from the supplied since sequence
        until there are no further pending changes.
        start() to fetch the changes from the supplied since sequence
        and then continuing to listen indefinitely for further new changes.

    The starting sequence ID can be changed for either mode by using "since".

    By default when using:
        start_one_off() the feed will start from the beginning.
        start() the feed will start from "now".

    In either mode the iterator can be terminated early by calling stop().

    By default ChangesFollower will suppress transient errors indefinitely
    and endeavour to run to completion or listen forever. For applications
    where that behaviour is not desirable an alternate options is
    available where a duration may be specified to limit the time since the
    last successful response that transient errors will be suppressed.

    It should be noted that errors considered terminal, for example, the
    database not existing or invalid credentials are never suppressed and will
    throw an exception immediately.

    The named arguments for "post_changes" are used to configure the behaviour
    of the ChangesFollower. However, a subset of the options are invalid as
    they are configured internally by the implementation and will cause an
    ValueError exception to be thrown if supplied.

    These invalid options are:
        - descending
        - feed
        - heartbeat
        - last_event_id
        - timeout

    Only the value of "_selector" is permitted for the post_changes's "filter" option.
    Selector based filters perform better than JS based filters and using one
    of the alternative JS based filter types will cause ChangesFollower
    to throw a ValueError exception.

    It should also be noted that the "limit" parameter will truncate the
    iterator at the given number of changes in either operating mode.

    The ChangesFollower requires the Cloudant client to have HTTP call and
    read timeouts of at least 1 minute. The default client configuration has
    sufficiently long timeouts.

    :param CloudantV1 service: A client for the Cloudant service.
    :param int error_tolerance: A duration to suppress transient errors for set in milliseconds.
    :return: None
    """

    def __init__(
        self, service: CloudantV1, *, error_tolerance: int = _FOREVER, **kwargs
    ) -> None:
        self.options = kwargs
        self.limit = self.options.get('limit')
        self._set_defaults()
        self.service = service
        self.error_tolerance = error_tolerance
        self._iter = None
        self.logger = logging.getLogger(__name__)
        # Check the timeouts are suitable
        timeouts = self.service.http_config.get('timeout', 0)
        if isinstance(timeouts, int):
            call_timeout, read_timeout = timeouts, timeouts
        else:
            call_timeout, read_timeout = timeouts
        call_timeout, read_timeout = call_timeout * 1000, read_timeout * 1000
        if (
            call_timeout > 0
            and call_timeout < _MIN_CLIENT_TIMEOUT
            or read_timeout > 0
            and read_timeout < _MIN_CLIENT_TIMEOUT
        ):
            raise ValueError(
                'To use {} the client read and call timeouts must be at least'
                ' {:d} ms. The client read timeout is {:d}'
                ' ms and the call timeout is {:d} ms.'.format(
                    type(self).__name__,
                    _MIN_CLIENT_TIMEOUT,
                    read_timeout,
                    call_timeout,
                )
            )

    @property
    def error_tolerance(self) -> int:
        return self._error_tolerance

    @error_tolerance.setter
    def error_tolerance(self, value: int) -> None:
        if value > _FOREVER:
            raise ValueError(
                f'Error tolerance duration must not be larger than {_FOREVER}.'
            )
        if value < 0:
            raise ValueError('Error tolerance duration must not be negative.')
        self._error_tolerance = value

    @property
    def options(self) -> Dict:
        return self._options

    @options.setter
    def options(self, value: Dict):
        class_name = type(self).__name__
        if value.get('db') is None:
            error_fmt = 'The option db must be provided when using {}.'
            raise ValueError(error_fmt.format(class_name))
        opts = ['descending', 'feed', 'heartbeat', 'last_event_id', 'timeout']
        invalid_options = [o for o in opts if value.get(o) is not None]
        if value.get('filter') and value.get('filter') != '_selector':
            invalid_options.append(f"filter={value.get('filter')}")
        if len(invalid_options) > 0:
            invalid_opts_list = ', '.join(invalid_options)
            error_fmt = 'The options {} are invalid when using {}.'
            if len(invalid_options) == 1:
                error_fmt = "The option '{}' is invalid when using {}."
            raise ValueError(error_fmt.format(invalid_opts_list, class_name))
        self._options = value

    def _set_defaults(self, limit: int = None):
        defaults = {
            'feed': PostChangesEnums.Feed.LONGPOLL,
            'timeout': _LONGPOLL_TIMEOUT,
        }
        if limit is not None:
            self.logger.debug(f'Applying changes limit {limit}')
            defaults['limit'] = limit
        self._options = {**self._options, **defaults}

    def start(self) -> Iterator[ChangesResultItem]:
        """
        Return all available changes and keep listening for new changes
        until reaching an end condition.

        The end conditions are:
            - a terminal error (e.g. unauthorized client).
            - transient errors occur for longer than the error
              suppression duration.
            - the number of changes received reaches the limit specified
              in the "post_changes" args used to instantiate
              this ChangesFollower.
            - ChangesFollower's stop() is called.

        The same change may be received more than once.

        Returns an iterator of ChangesResultItem per change.

        Throws ValueError if ChangesFollower's start() or start_one_off()
        was already called or ApiException if a terminal error
        or unsupressed transient error is recevied from the service
        when fetching changes
        """
        return self._run(_Mode.LISTEN)

    def start_one_off(self) -> Iterator[ChangesResultItem]:
        """
        Return all available changes until there are no further changes
        pending or reaching an end condition.

        The end conditions are:
            - a terminal error (e.g. unauthorized client).
            - transient errors occur for longer than the error
              suppression duration.
            - the number of changes received reaches the limit specified
              in the "post_changes" args used to instantiate
              this ChangesFollower.
            - ChangesFollower's stop() is called.

        The same change may be received more than once.

        Returns an iterator of ChangesResultItem per change.

        Throws ValueError if ChangesFollower's start() or start_one_off()
        was already called or ApiException if a terminal error
        or unsupressed transient error is recevied from the service
        when fetching changes
        """
        return self._run(_Mode.FINITE)

    def stop(self) -> None:
        """
        Stop this ChangesFollower.

        Note that synchronous iterator blocks so this stop method
        needs to be called from a different thread to have any effect.
        """
        self._iter.stop()

    def _run(self, mode: _Mode):
        if self._iter is not None:
            raise RuntimeError('Cannot start a feed that has already started.')

        batch_size = _BATCH_SIZE
        if self.options.get('include_docs', False):
            resp = self.service.get_database_information(
                db=self.options.get('db')
            ).get_result()
            docs = resp.get('doc_count', 0)
            sizes = resp.get('sizes', {})
            external_size = sizes.get('external', 0)
            if external_size > 0 and docs > 0:
                batch_size = max(int(5 * 1024 * 1024 / (external_size / docs + 500)), 1)

        if self.limit is not None:
            batch_size = self.limit if self.limit < batch_size else batch_size

        self._set_defaults(batch_size)
        changes_caller = functools.partial(
            self.service.post_changes, **self.options
        )
        self._iter = _ChangesFollowerIterator(
            changes_caller, mode, self.error_tolerance
        )
        if self.limit is not None:
            self._iter.limit = self.limit
        if self.options.get('since') is not None:
            self._iter.since = self.options.get('since')
        self._iter._start()
        return self._iter
