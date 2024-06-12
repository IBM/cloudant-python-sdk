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
Shared tests' fixtures
"""

import unittest
import pytest
import os
import json
import responses

import threading
import queue

import itertools

from requests import codes
from requests.exceptions import ConnectionError

from ibmcloudant.cloudant_v1 import (
    CloudantV1,
    PostChangesEnums,
    ChangesResult,
    ChangesResultItem,
)

from ibmcloudant.features.changes_follower import (
    _LONGPOLL_TIMEOUT,
    _BATCH_SIZE,
    _Mode,
)


@pytest.fixture(scope='class')
def kwargs(request):
    request.cls.kwarg_valid = {
        'include_docs': True,
        'doc_ids': ['foo', 'bar', 'baz'],
        'att_encoding_info': True,
        'attachments': True,
        'conflicts': True,
        'filter': '_selector',
        'selector': {'selector': {'foo': 'bar'}},
    }

    request.cls.kwarg_invalid = {
        'descending': True,
        'feed': PostChangesEnums.Feed.CONTINUOUS,
        'heartbeat': 150,
        'last_event_id': '9876-alotofcharactersthatarenotreallyrandom',
        'timeout': 3600000,
        'filter': '_view',
    }


@pytest.fixture(scope='class')
def timeouts(request):
    longpoll_timeout = int(_LONGPOLL_TIMEOUT / 1000)
    request.cls.timeouts_valid = [60, (60, 60), 120, 300, (120, 300)]
    request.cls.timeouts_invalid = [
        15,
        30,
        (30, 15),
        longpoll_timeout,
        (longpoll_timeout, longpoll_timeout),
    ]


@pytest.fixture(scope='class')
def errors(request):
    request.cls.terminal_errors = [
        'bad_request',
        'unauthorized',
        'forbidden',
        'not_found',
    ]
    request.cls.transient_errors = [
        'too_many_requests',
        'internal_server_error',
        'bad_gateway',
        'gateway_timeout',
        'bad_json',
        'bad_io',
    ]


@pytest.fixture(scope='class')
def limits(request):
    request.cls.limits = [
        100,
        _BATCH_SIZE,
        _BATCH_SIZE + 123,
    ]


class ChangesFollowerBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup client env config
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'
        os.environ['TEST_SERVICE_URL'] = 'http://localhost:5984'
        cls.client = CloudantV1.new_instance(
            service_name='TEST_SERVICE',
        )

    def prepare_mock_changes(
        self,
        batches=0,
        errors=[],
        db_info_doc_count=500_000,
        db_info_doc_size=523,
    ):
        class changes_callback:
            def __init__(self):
                self._batch_num = 1
                self._errors = itertools.cycle(errors)
                self._return_error = False

            def __call__(self, request):
                if self._return_error:
                    self._return_error = False
                    error = next(self._errors)
                    if error == 'bad_io':
                        return (200, {}, ConnectionError('peer reset'))
                    elif error == 'bad_json':
                        return (200, {}, '{')
                    else:
                        return (
                            codes[error],
                            {},
                            json.dumps({'error': error}),
                        )
                # this stands for "large" seq in empty result case
                last_seq = f'{batches * _BATCH_SIZE}-abcdef'
                pending = 0
                items = []
                if self._batch_num <= batches:
                    # we start from doc idx 000001
                    start = (self._batch_num - 1) * _BATCH_SIZE + 1
                    stop = start + _BATCH_SIZE
                    last_seq = f'{stop-1}-abcdef'
                    pending = (
                        batches * _BATCH_SIZE - (self._batch_num) * _BATCH_SIZE
                    )
                    for idx in range(start, stop, 1):
                        items.append(
                            ChangesResultItem(
                                id=f'{idx:06}',
                                changes=[],
                                seq=f'{idx}-abcdef',
                            )
                        )
                resp = ChangesResult(
                    last_seq=last_seq, pending=pending, results=items
                ).to_dict()
                self._batch_num += 1
                if len(errors) > 0:
                    self._return_error = True
                return (
                    200,
                    {},
                    json.dumps(resp),
                )

        _base_url = os.environ.get('TEST_SERVER_URL', 'http://localhost:5984')
        url = _base_url + '/db'
        responses.get(
            url,
            status=200,
            content_type='application/json',
            json={
                'doc_count': db_info_doc_count,
                'sizes': {'external': db_info_doc_count * db_info_doc_size},
            },
        )

        url = _base_url + '/db/_changes'
        return responses.add_callback(
            responses.POST,
            url,
            content_type='application/json',
            callback=changes_callback(),
        )

    def prepare_mock_with_error(self, error: str):
        _base_url = os.environ.get('TEST_SERVER_URL', 'http://localhost:5984')
        url = _base_url + '/db/_changes'
        if error == 'bad_io':
            return responses.post(url, body=ConnectionError('peer reset'))
        elif error == 'bad_json':
            return responses.post(
                url,
                status=200,
                content_type='application/json',
                body='{',
            )
        else:
            return responses.post(
                url,
                status=codes[error],
                content_type='application/json',
                json={'error': error},
            )

    def runner(self, follower, mode, timeout=0, stop_after=0):
        """
        blocking runner with timeout
        """

        class TimeoutError(Exception):
            pass

        def looper(changes, buf):
            counter = 0
            buf.put(counter)
            try:
                for _ in changes:
                    counter += 1
                    buf.put(counter)
                    if stop_after > 0 and stop_after == counter:
                        follower.stop()
            except Exception as e:
                buf.put(e)

        def main():
            if mode == _Mode.LISTEN:
                changes = follower.start()
            elif mode == _Mode.FINITE:
                changes = follower.start_one_off()
            buf = queue.Queue()
            thread = threading.Thread(target=looper, args=(changes, buf))
            thread.start()
            thread.join(timeout)
            while not buf.empty():
                data = buf.get()
                if isinstance(data, Exception):
                    raise data
            while True:
                if thread.is_alive():
                    follower.stop()
                else:
                    break
            return data

        return main()
