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
Test methods in the changes follower module
"""

import pytest
import responses
import sys
import timeit

from requests.exceptions import ConnectionError

from ibm_cloud_sdk_core import ApiException

from ibmcloudant.cloudant_v1 import PostChangesEnums

from ibmcloudant.features.changes_follower import (
    ChangesFollower,
    _FOREVER,
    _LONGPOLL_TIMEOUT,
    _BATCH_SIZE,
    _Mode,
)


from conftest import ChangesFollowerBaseCase

# the largest positive integer supported by the platform
MAX_BATCHES = sys.maxsize / _BATCH_SIZE


@pytest.mark.usefixtures('timeouts')
class TestChangesFollowerInitialization(ChangesFollowerBaseCase):
    def test_minimal_initialization(self):
        try:
            ChangesFollower(self.client, db='db')
        except BaseException:
            self.fail('There should be no exception.')

    def test_validate_missing_database_name(self):
        regx = 'The option db must be provided when using ChangesFollower.'
        with self.assertRaisesRegex(ValueError, regx):
            ChangesFollower(self.client)

    def test_validate_overflow_tolerance(self):
        regx = 'Error tolerance duration must not be larger than'
        with self.assertRaisesRegex(ValueError, regx):
            ChangesFollower(self.client, db='db', error_tolerance=_FOREVER + 1)

    def test_validate_negative_tolerance(self):
        regx = 'Error tolerance duration must not be negative.'
        with self.assertRaisesRegex(ValueError, regx):
            ChangesFollower(self.client, db='db', error_tolerance=-1)

    def test_initialization_with_valid_client_timeout(self):
        for timeout in self.timeouts_valid:
            try:
                self.client.set_http_config({'timeout': timeout})
                ChangesFollower(self.client, db='db')
            except BaseException:
                self.fail('There should be no exception.')

    def test_initialization_with_invalid_client_timeout(self):
        for timeout in self.timeouts_invalid:
            self.client.set_http_config({'timeout': timeout})
            regx = 'timeouts must be at least'
            with self.assertRaisesRegex(ValueError, regx):
                ChangesFollower(self.client, db='db')


@pytest.mark.usefixtures('kwargs')
class TestChangesFollowerOptions(ChangesFollowerBaseCase):
    def test_validate_options_valid_cases(self):
        try:
            ChangesFollower(self.client, db='db', **self.kwarg_valid)
        except BaseException:
            self.fail('There should be no illegal argument exception.')

    def test_validate_options_invalid_cases(self):
        for opt, val in self.kwarg_invalid.items():
            if opt == 'filter':
                error_opt = f"filter={val}"
            else:
                error_opt = opt
            regx = f"The option '{error_opt}' is invalid when using ChangesFollower."
            with self.assertRaisesRegex(ValueError, regx):
                ChangesFollower(self.client, db='db', **{opt: val})

    def test_validate_options_multiple_invalid_cases(self):
        error_opts = ''
        for opt, val in self.kwarg_invalid.items():
            if opt == 'filter':
                error_opts += f'filter={val}, '
            else:
                error_opts += f'{opt}, '
        if error_opts.endswith(', '):
          error_opts = error_opts[:-len(', ')]
        regx = (
            f'The options {error_opts} are invalid when using ChangesFollower.'
        )
        with self.assertRaisesRegex(ValueError, regx):
            ChangesFollower(self.client, db='db', **self.kwarg_invalid)

    def test_set_defaults(self):
        follower = ChangesFollower(self.client, db='db', **self.kwarg_valid)
        expected = {
            'feed': PostChangesEnums.Feed.LONGPOLL,
            'timeout': _LONGPOLL_TIMEOUT,
        }
        for opt, val in expected.items():
            self.assertEqual(follower.options.get(opt), val)

    def test_set_defaults_with_limit(self):
        follower = ChangesFollower(self.client, db='db', **self.kwarg_valid)
        follower._set_defaults(limit=12)
        expected = {
            'feed': PostChangesEnums.Feed.LONGPOLL,
            'timeout': _LONGPOLL_TIMEOUT,
            'limit': 12,
        }
        for opt, val in expected.items():
            self.assertEqual(follower.options.get(opt), val)

    def test_set_defaults_with_kwarg_limit(self):
        kwarg = {**self.kwarg_valid, **{'limit': 24}}
        follower = ChangesFollower(self.client, db='db', **kwarg)
        follower._set_defaults(limit=12)
        self.assertEqual(follower.options.get('limit'), 12)


@pytest.mark.usefixtures('limits', 'errors')
class TestChangesFollowerFinite(ChangesFollowerBaseCase):
    @responses.activate
    def test_start_one_off(self):
        """
        Checks that a FINITE mode completes successfully
        for a fixed number of batches.
        """
        batches = 6
        self.prepare_mock_changes(batches=batches)
        follower = ChangesFollower(self.client, db='db')
        changes = follower.start_one_off()
        count = sum(1 for _ in changes)
        self.assertEqual(
            count,
            batches * _BATCH_SIZE,
            'There should be the expected number of changes.',
        )

    @responses.activate
    def test_start_one_off_terminal_errors(self):
        """
        Checks that a FINITE mode errors for all terminal errors.
        """
        for error in self.terminal_errors:
            self.prepare_mock_with_error(error)
            follower = ChangesFollower(self.client, db='db')
            changes = follower.start_one_off()
            with self.assertRaisesRegex(ApiException, error):
                next(changes)

    @responses.activate
    def test_start_one_off_transient_errors_no_suppression(self):
        """
        Checks that a FINITE mode errors for all transient errors
        when not suppressing.
        """
        for error in self.transient_errors:
            self.prepare_mock_with_error(error)
            follower = ChangesFollower(self.client, db='db', error_tolerance=0)
            start = timeit.default_timer()
            changes = follower.start_one_off()
            if error == 'bad_io':
                with self.assertRaises(ConnectionError):
                    next(changes)
            else:
                if error == 'bad_json':
                    error = 'Error processing the HTTP response'
                with self.assertRaisesRegex(ApiException, error):
                    next(changes)
            stop = timeit.default_timer() - start
            self.assertLess(
                stop,
                0.300,
                'There should be no exception delay.',
            )

    @responses.activate
    def test_start_one_off_transient_errors_with_suppression_duration(self):
        """
        Checks that a FINITE mode repeatedly encountering transient errors
        will terminate with an exception after a duration.
        """
        for error in self.transient_errors:
            self.prepare_mock_with_error(error)
            follower = ChangesFollower(
                self.client, db='db', error_tolerance=100
            )
            start = timeit.default_timer()
            changes = follower.start_one_off()
            if error == 'bad_io':
                with self.assertRaises(ConnectionError):
                    next(changes)
            else:
                if error == 'bad_json':
                    error = 'Error processing the HTTP response'
                with self.assertRaisesRegex(ApiException, error):
                    next(changes)
            stop = timeit.default_timer() - start
            self.assertGreaterEqual(
                stop,
                0.100,
                'The exception delay should be longer error_tolerance.',
            )

    @responses.activate
    def test_start_one_off_transient_errors_with_suppression_does_complete(
        self,
    ):
        """
        Checks that a FINITE mode repeatedly encountering transient errors
        will complete successfully if not exceeding the duration.
        """
        batches = 5
        self.prepare_mock_changes(
            batches=batches,
            errors=self.transient_errors,
        )
        follower = ChangesFollower(self.client, db='db', error_tolerance=300)
        changes = follower.start_one_off()
        count = sum(1 for _ in changes)
        self.assertEqual(
            count,
            batches * _BATCH_SIZE,
            'There should be the expected number of changes.',
        )

    @responses.activate
    def test_start_one_off_transient_errors_max_suppression_does_not_complete(
        self,
    ):
        """
        Checks that a FINITE mode repeatedly encountering transient errors
        will keep trying indefinitely with max suppression.
        """
        for error in self.transient_errors:
            try:
                self.prepare_mock_with_error(error)
                follower = ChangesFollower(self.client, db='db')
                count = self.runner(follower, _Mode.FINITE, timeout=0.5)
            except BaseException:
                self.fail('There should be no exception.')
            self.assertEqual(count, 0, 'There should be no changes.')

    @responses.activate
    def test_start_one_off_transient_errors_with_max_suppression_does_complete(
        self,
    ):
        """
        Checks that a FINITE mode encountering transient errors
        will complete successfully with max suppression.
        """
        batches = 4
        self.prepare_mock_changes(
            batches=batches, errors=self.transient_errors
        )
        follower = ChangesFollower(self.client, db='db')
        changes = follower.start_one_off()
        count = sum(1 for _ in changes)
        self.assertEqual(
            count,
            batches * _BATCH_SIZE,
            'There should be the expected number of changes.',
        )

    @responses.activate
    def test_stop(self):
        """
        Checks calling stop for the FINITE case.
        """
        try:
            self.prepare_mock_changes(batches=MAX_BATCHES)
            follower = ChangesFollower(self.client, db='db')
            start = timeit.default_timer()
            count = self.runner(
                follower, _Mode.FINITE, timeout=5, stop_after=1000
            )
            stop = timeit.default_timer() - start
        except BaseException:
            self.fail('There should be no exception.')
        self.assertGreaterEqual(count, 1000, 'There should be some changes.')
        self.assertLess(
            stop, 5, 'The thread should have stopped before the wait time.'
        )

    @responses.activate
    def test_state_error(self):
        """
        Checks that a FINITE follower can only be started once.
        """
        try:
            self.prepare_mock_changes(batches=MAX_BATCHES)
            follower = ChangesFollower(self.client, db='db')
            self.runner(follower, _Mode.FINITE, timeout=1, stop_after=1000)
            with self.assertRaisesRegex(
                RuntimeError, 'Cannot start a feed that has already started.'
            ):
                follower.start_one_off()
            with self.assertRaisesRegex(
                RuntimeError, 'Cannot start a feed that has already started.'
            ):
                follower.start()
        except BaseException:
            self.fail('There should be no exception.')

    @responses.activate
    def test_limit(self):
        """
        Checks that setting a limit terminates iterations early for FINITE mode
        and limits smaller, the same and larger than the default batch size.
        """
        for limit in self.limits:
            try:
                self.prepare_mock_changes(batches=MAX_BATCHES)
                follower = ChangesFollower(self.client, db='db', limit=limit)
                count = self.runner(follower, _Mode.FINITE, timeout=3600)
            except BaseException:
                self.fail('There should be no exception.')
            self.assertEqual(
                count,
                limit,
                'There should be the correct number of changes.',
            )

    @responses.activate
    def test_retry_delay(self):
        """
        Checks that a FINITE follower delays between retries.

        For a time frame in 600ms an exponential backoff would make 3 retry
        attempts (first immideately, for duration of 100ms, second after
        that for duration of 200ms, and third after 100ms+200ms for duration
        of 400ms).

        In the same time frame a full jitter backoff would make more attempts
        because of its random delay, realistically we can expect ~4-5.

        We can safely tripple this number, check for no more for 15 calls
        and still be sure that we have delay working, because without it
        we are looking at +1000 calls in the same time frame.
        """
        try:
            error = self.transient_errors[0]
            resp = self.prepare_mock_with_error(error)
            follower = ChangesFollower(self.client, db='db')
            count = self.runner(follower, _Mode.FINITE, timeout=0.6)
        except BaseException:
            self.fail('There should be no exception.')
        self.assertEqual(count, 0, 'There should be no changes.')
        self.assertLessEqual(
            resp.call_count, 15, 'Call count should not exceed limit.'
        )

    @responses.activate
    def test_batch_size(self):
        """
        Checks that setting includeDocs forces a calculation of batch size
        and asserts the size.

        Mocks a DB of 500_000 docs of 523 bytes each to give an expected batch
        size of 5125

        523 bytes + 500 bytes of changes overhead = 1023 bytes
        5 MiB / 1023 bytes = 5125 docs per batch
        """
        self.prepare_mock_changes(batches=1)
        follower = ChangesFollower(
            self.client, db='db', error_tolerance=0, include_docs=True
        )
        changes = follower.start_one_off()
        next(changes)
        params = responses.calls[1].request.params
        self.assertEqual(
            params['limit'],
            '5125',
            'Limit should be set to the expected value.',
        )

    @responses.activate
    def test_batch_size_minimum(self):
        """
        Checks that setting includeDocs forces a calculation of batch size
        and asserts the size.

        Mocks a DB of 1 docs of less than 5 MiB size to give an expected batch
        size of 0

        Checks that the minimum batch_size of 1 is set.
        """
        self.prepare_mock_changes(batches=1, db_info_doc_count=1, db_info_doc_size=(5 * 1024 * 1024 - 1))
        follower = ChangesFollower(
            self.client, db='db', error_tolerance=0, include_docs=True
        )
        changes = follower.start_one_off()
        next(changes)
        params = responses.calls[1].request.params
        self.assertEqual(
            params['limit'],
            '1',
            'Limit should be set to the expected value.',
        )

    @responses.activate
    def test_batch_size_with_limit(self):
        """
        Checks that setting includeDocs and limit that below calculated
        batch sets batch size to limit
        """
        self.prepare_mock_changes(batches=1)
        follower = ChangesFollower(
            self.client,
            db='db',
            error_tolerance=0,
            limit=1000,
            include_docs=True,
        )
        changes = follower.start_one_off()
        next(changes)
        params = responses.calls[1].request.params
        self.assertEqual(
            params['limit'],
            '1000',
            'Limit should be set to the expected value.',
        )


@pytest.mark.usefixtures('limits', 'errors')
class TestChangesFollowerListen(ChangesFollowerBaseCase):
    @responses.activate
    def test_start(self):
        """
        Checks that a LISTEN mode completes successfully (after stopping)
        with some batches.
        """
        try:
            self.prepare_mock_changes(batches=3)
            follower = ChangesFollower(self.client, db='db')
            count = self.runner(follower, _Mode.LISTEN, timeout=5)
        except BaseException:
            self.fail('There should be no exception.')
        self.assertGreater(
            count, 2 * _BATCH_SIZE + 1, 'There should be some changes.'
        )

    @responses.activate
    def test_start_terminal_errors(self):
        """
        Checks that a LISTEN mode errors for all terminal errors.
        """
        for error in self.terminal_errors:
            self.prepare_mock_with_error(error)
            follower = ChangesFollower(self.client, db='db')
            with self.assertRaisesRegex(ApiException, error):
                self.runner(follower, _Mode.LISTEN, timeout=1)

    @responses.activate
    def test_start_transient_errors_no_suppression(self):
        """
        Checks that a LISTEN mode errors for all transient errors
        when not suppressing.
        """
        for error in self.transient_errors:
            self.prepare_mock_with_error(error)
            follower = ChangesFollower(self.client, db='db', error_tolerance=0)
            if error == 'bad_io':
                with self.assertRaises(ConnectionError):
                    self.runner(follower, _Mode.LISTEN, timeout=1)
            else:
                if error == 'bad_json':
                    error = 'Error processing the HTTP response'
                with self.assertRaisesRegex(ApiException, error):
                    self.runner(follower, _Mode.LISTEN, timeout=1)

    @responses.activate
    def test_start_transient_errors_with_suppression_error_termination(self):
        """
        Checks that a LISTEN mode errors for all transient errors
        when exceeding the suppression duration.
        """
        for error in self.transient_errors:
            resp = self.prepare_mock_with_error(error)
            follower = ChangesFollower(
                self.client, db='db', error_tolerance=100
            )
            if error == 'bad_io':
                with self.assertRaises(ConnectionError):
                    self.runner(follower, _Mode.LISTEN, timeout=1)
            else:
                if error == 'bad_json':
                    error = 'Error processing the HTTP response'
                with self.assertRaisesRegex(ApiException, error):
                    self.runner(follower, _Mode.LISTEN, timeout=1)
            self.assertGreater(
                resp.call_count, 1, 'Mock server should receive calls.'
            )

    @responses.activate
    def test_start_transient_errors_with_suppression_all_changes(self):
        """
        Checks that a LISTEN mode gets changes and can be stopped cleanly
        with transient errors when not exceeding the suppression duration.
        """
        batches = 2
        self.prepare_mock_changes(
            batches=batches,
            errors=self.transient_errors,
        )
        try:
            follower = ChangesFollower(
                self.client, db='db', error_tolerance=300
            )
            count = self.runner(follower, _Mode.LISTEN, timeout=1)
        except BaseException:
            self.fail('There should be no exception.')
        self.assertEqual(
            count,
            batches * _BATCH_SIZE,
            'There should be the correct number of changes.',
        )

    @responses.activate
    def test_start_transient_errors_with_max_suppression(self):
        """
        Checks that a LISTEN mode keeps running with transient errors
        (until stopped cleanly) with max suppression.
        """
        for error in self.transient_errors:
            try:
                resp = self.prepare_mock_with_error(error)
                follower = ChangesFollower(self.client, db='db')
                count = self.runner(follower, _Mode.LISTEN, timeout=1)
            except BaseException:
                self.fail('There should be no exception.')
            self.assertEqual(count, 0, 'There should be no changes.')
            self.assertGreater(
                resp.call_count, 1, 'Mock server should receive calls.'
            )

    @responses.activate
    def test_start_transient_errors_with_max_suppression_all_changes(self):
        """
        Checks that a LISTEN mode runs through transient errors
        with max suppression to receive changes until stopped.
        """
        batches = 3
        self.prepare_mock_changes(
            batches=batches,
            errors=self.transient_errors,
        )
        try:
            follower = ChangesFollower(self.client, db='db')
            count = self.runner(follower, _Mode.LISTEN, timeout=1)
        except BaseException:
            self.fail('There should be no exception.')
        self.assertEqual(
            count,
            batches * _BATCH_SIZE,
            'There should be the correct number of changes.',
        )

    @responses.activate
    def test_stop(self):
        """
        Checks calling stop for the LISTEN case.
        """
        try:
            self.prepare_mock_changes(batches=MAX_BATCHES)
            follower = ChangesFollower(self.client, db='db')
            start = timeit.default_timer()
            count = self.runner(
                follower, _Mode.LISTEN, timeout=5, stop_after=1000
            )
            stop = timeit.default_timer() - start
        except BaseException:
            self.fail('There should be no exception.')
        self.assertGreaterEqual(count, 1000, 'There should be some changes.')
        self.assertLess(
            stop, 5, 'The thread should have stopped before the wait time.'
        )

    @responses.activate
    def test_state_error(self):
        """
        Checks that a LISTEN follower can only be started once.
        """
        try:
            self.prepare_mock_changes(batches=MAX_BATCHES)
            follower = ChangesFollower(self.client, db='db')
            self.runner(follower, _Mode.LISTEN, timeout=1, stop_after=1000)
            with self.assertRaisesRegex(
                RuntimeError, 'Cannot start a feed that has already started.'
            ):
                follower.start_one_off()
            with self.assertRaisesRegex(
                RuntimeError, 'Cannot start a feed that has already started.'
            ):
                follower.start()
        except BaseException:
            self.fail('There should be no exception.')

    @responses.activate
    def test_limit(self):
        """
        Checks that setting a limit terminates iterations early for LISTEN mode
        and limits smaller, the same and larger than the default batch size.
        """
        for limit in self.limits:
            try:
                self.prepare_mock_changes(batches=MAX_BATCHES)
                follower = ChangesFollower(self.client, db='db', limit=limit)
                count = self.runner(follower, _Mode.LISTEN, timeout=3600)
            except BaseException:
                self.fail('There should be no exception.')
            self.assertEqual(
                count,
                limit,
                'There should be the correct number of changes.',
            )

    @responses.activate
    def test_retry_delay(self):
        """
        Checks that a LISTEN follower delays between retries.
        See the FINITE version of the test for additional comments.
        """
        try:
            error = self.transient_errors[0]
            resp = self.prepare_mock_with_error(error)
            follower = ChangesFollower(self.client, db='db')
            count = self.runner(follower, _Mode.LISTEN, timeout=0.6)
        except BaseException:
            self.fail('There should be no exception.')
        self.assertEqual(count, 0, 'There should be no changes.')
        self.assertLessEqual(
            resp.call_count, 15, 'Call count should not exceed limit.'
        )
