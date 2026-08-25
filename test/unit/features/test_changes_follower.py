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

import sys
import timeit
import unittest

import pytest
import responses
from conftest import ChangesFollowerBaseCase
from ibm_cloud_sdk_core import ApiException
from requests.exceptions import ConnectionError

from ibmcloudant.cloudant_v1 import PostChangesEnums
from ibmcloudant.features.changes_follower import (
    _BATCH_SIZE,
    _FOREVER,
    _LONGPOLL_TIMEOUT,
    _SEQ_MARKERS_CAPACITY,
    _SEQ_MARKERS_EVICTION_COUNT,
    ChangesFollower,
    _Mode,
)

# the largest positive integer supported by the platform
MAX_BATCHES = sys.maxsize / _BATCH_SIZE


@pytest.mark.usefixtures("timeouts")
class TestChangesFollowerInitialization(ChangesFollowerBaseCase):
    def test_minimal_initialization(self):
        try:
            ChangesFollower(self.client, db="db")
        except BaseException:
            self.fail("There should be no exception.")

    def test_validate_missing_database_name(self):
        regx = "The option db must be provided when using ChangesFollower."
        with self.assertRaisesRegex(ValueError, regx):
            ChangesFollower(self.client)

    def test_validate_overflow_tolerance(self):
        regx = "Error tolerance duration must not be larger than"
        with self.assertRaisesRegex(ValueError, regx):
            ChangesFollower(self.client, db="db", error_tolerance=_FOREVER + 1)

    def test_validate_negative_tolerance(self):
        regx = "Error tolerance duration must not be negative."
        with self.assertRaisesRegex(ValueError, regx):
            ChangesFollower(self.client, db="db", error_tolerance=-1)

    def test_initialization_with_valid_client_timeout(self):
        for timeout in self.timeouts_valid:
            try:
                self.client.set_http_config({"timeout": timeout})
                ChangesFollower(self.client, db="db")
            except BaseException:
                self.fail("There should be no exception.")

    def test_initialization_with_invalid_client_timeout(self):
        for timeout in self.timeouts_invalid:
            self.client.set_http_config({"timeout": timeout})
            regx = "timeouts must be at least"
            with self.assertRaisesRegex(ValueError, regx):
                ChangesFollower(self.client, db="db")


@pytest.mark.usefixtures("kwargs")
class TestChangesFollowerOptions(ChangesFollowerBaseCase):
    def test_validate_options_valid_cases(self):
        try:
            ChangesFollower(self.client, db="db", **self.kwarg_valid)
        except BaseException:
            self.fail("There should be no illegal argument exception.")

    def test_validate_options_invalid_cases(self):
        for opt, val in self.kwarg_invalid.items():
            if opt == "filter":
                error_opt = f"filter={val}"
            else:
                error_opt = opt
            regx = f"The option '{error_opt}' is invalid when using ChangesFollower."
            with self.assertRaisesRegex(ValueError, regx):
                ChangesFollower(self.client, db="db", **{opt: val})

    def test_validate_options_multiple_invalid_cases(self):
        error_opts = ""
        for opt, val in self.kwarg_invalid.items():
            if opt == "filter":
                error_opts += f"filter={val}, "
            else:
                error_opts += f"{opt}, "
        if error_opts.endswith(", "):
            error_opts = error_opts[: -len(", ")]
        regx = f"The options {error_opts} are invalid when using ChangesFollower."
        with self.assertRaisesRegex(ValueError, regx):
            ChangesFollower(self.client, db="db", **self.kwarg_invalid)

    def test_set_defaults(self):
        follower = ChangesFollower(self.client, db="db", **self.kwarg_valid)
        expected = {
            "feed": PostChangesEnums.Feed.NORMAL,
            "timeout": None,
        }
        for opt, val in expected.items():
            self.assertEqual(follower.options.get(opt), val)

    def test_set_defaults_listen(self):
        follower = ChangesFollower(self.client, db="db", **self.kwarg_valid)
        follower._set_defaults(_Mode.LISTEN)
        expected = {
            "feed": PostChangesEnums.Feed.LONGPOLL,
            "timeout": _LONGPOLL_TIMEOUT,
        }
        for opt, val in expected.items():
            self.assertEqual(follower.options.get(opt), val)

    def test_set_defaults_with_limit(self):
        follower = ChangesFollower(self.client, db="db", **self.kwarg_valid)
        follower._set_defaults(_Mode.FINITE, limit=12)
        expected = {
            "feed": PostChangesEnums.Feed.NORMAL,
            "timeout": None,
            "limit": 12,
        }
        for opt, val in expected.items():
            self.assertEqual(follower.options.get(opt), val)

    def test_set_defaults_listen_with_limit(self):
        follower = ChangesFollower(self.client, db="db", **self.kwarg_valid)
        follower._set_defaults(_Mode.LISTEN, limit=12)
        expected = {
            "feed": PostChangesEnums.Feed.LONGPOLL,
            "timeout": _LONGPOLL_TIMEOUT,
            "limit": 12,
        }
        for opt, val in expected.items():
            self.assertEqual(follower.options.get(opt), val)

    def test_set_defaults_with_kwarg_limit(self):
        kwarg = {**self.kwarg_valid, **{"limit": 24}}
        follower = ChangesFollower(self.client, db="db", **kwarg)
        follower._set_defaults(_Mode.LISTEN, limit=12)
        self.assertEqual(follower.options.get("limit"), 12)


@pytest.mark.usefixtures("limits", "errors")
class TestChangesFollowerFinite(ChangesFollowerBaseCase):
    @responses.activate
    def test_start_one_off(self):
        """
        Checks that a FINITE mode completes successfully
        for a fixed number of batches.
        """
        batches = 6
        self.prepare_mock_changes(batches=batches)
        follower = ChangesFollower(self.client, db="db")
        changes = follower.start_one_off()
        count = sum(1 for _ in changes)
        self.assertEqual(
            count,
            batches * _BATCH_SIZE,
            "There should be the expected number of changes.",
        )

    @responses.activate
    def test_start_one_off_terminal_errors(self):
        """
        Checks that a FINITE mode errors for all terminal errors.
        """
        for error in self.terminal_errors:
            self.prepare_mock_with_error(error)
            follower = ChangesFollower(self.client, db="db")
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
            follower = ChangesFollower(self.client, db="db", error_tolerance=0)
            start = timeit.default_timer()
            changes = follower.start_one_off()
            if error == "bad_io":
                with self.assertRaises(ConnectionError):
                    next(changes)
            else:
                if error == "bad_json":
                    error = "Error processing the HTTP response"
                with self.assertRaisesRegex(ApiException, error):
                    next(changes)
            stop = timeit.default_timer() - start
            self.assertLess(
                stop,
                0.300,
                "There should be no exception delay.",
            )

    @responses.activate
    def test_start_one_off_transient_errors_with_suppression_duration(self):
        """
        Checks that a FINITE mode repeatedly encountering transient errors
        will terminate with an exception after a duration.
        """
        for error in self.transient_errors:
            self.prepare_mock_with_error(error)
            follower = ChangesFollower(self.client, db="db", error_tolerance=100)
            start = timeit.default_timer()
            changes = follower.start_one_off()
            if error == "bad_io":
                with self.assertRaises(ConnectionError):
                    next(changes)
            else:
                if error == "bad_json":
                    error = "Error processing the HTTP response"
                with self.assertRaisesRegex(ApiException, error):
                    next(changes)
            stop = timeit.default_timer() - start
            self.assertGreaterEqual(
                stop,
                0.100,
                "The exception delay should be longer error_tolerance.",
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
        follower = ChangesFollower(self.client, db="db", error_tolerance=300)
        changes = follower.start_one_off()
        count = sum(1 for _ in changes)
        self.assertEqual(
            count,
            batches * _BATCH_SIZE,
            "There should be the expected number of changes.",
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
                follower = ChangesFollower(self.client, db="db")
                count = self.runner(follower, _Mode.FINITE, timeout=0.5)
            except BaseException:
                self.fail("There should be no exception.")
            self.assertEqual(count, 0, "There should be no changes.")

    @responses.activate
    def test_start_one_off_transient_errors_with_max_suppression_does_complete(
        self,
    ):
        """
        Checks that a FINITE mode encountering transient errors
        will complete successfully with max suppression.
        """
        batches = 4
        self.prepare_mock_changes(batches=batches, errors=self.transient_errors)
        follower = ChangesFollower(self.client, db="db")
        changes = follower.start_one_off()
        count = sum(1 for _ in changes)
        self.assertEqual(
            count,
            batches * _BATCH_SIZE,
            "There should be the expected number of changes.",
        )

    @responses.activate
    def test_stop(self):
        """
        Checks calling stop for the FINITE case.
        """
        try:
            self.prepare_mock_changes(batches=MAX_BATCHES)
            follower = ChangesFollower(self.client, db="db")
            start = timeit.default_timer()
            count = self.runner(follower, _Mode.FINITE, timeout=2, stop_after=1000)
            stop = timeit.default_timer() - start
        except BaseException:
            self.fail("There should be no exception.")
        self.assertGreaterEqual(count, 1000, "There should be some changes.")
        self.assertLess(stop, 2, "The thread should have stopped before the wait time.")

    @responses.activate
    def test_state_error(self):
        """
        Checks that a FINITE follower can only be started once.
        """
        try:
            self.prepare_mock_changes(batches=MAX_BATCHES)
            follower = ChangesFollower(self.client, db="db")
            self.runner(follower, _Mode.FINITE, timeout=1, stop_after=1000)
            with self.assertRaisesRegex(
                RuntimeError, "Cannot start a feed that has already started."
            ):
                follower.start_one_off()
            with self.assertRaisesRegex(
                RuntimeError, "Cannot start a feed that has already started."
            ):
                follower.start()
        except BaseException:
            self.fail("There should be no exception.")

    @responses.activate
    def test_limit(self):
        """
        Checks that setting a limit terminates iterations early for FINITE mode
        and limits smaller, the same and larger than the default batch size.
        """
        for limit in self.limits:
            try:
                self.prepare_mock_changes(batches=MAX_BATCHES)
                follower = ChangesFollower(self.client, db="db", limit=limit)
                count = self.runner(follower, _Mode.FINITE, timeout=180)
            except BaseException:
                self.fail("There should be no exception.")
            self.assertEqual(
                count,
                limit,
                "There should be the correct number of changes.",
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
            follower = ChangesFollower(self.client, db="db")
            count = self.runner(follower, _Mode.FINITE, timeout=0.6)
        except BaseException:
            self.fail("There should be no exception.")
        self.assertEqual(count, 0, "There should be no changes.")
        self.assertLessEqual(resp.call_count, 15, "Call count should not exceed limit.")

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
            self.client, db="db", error_tolerance=0, include_docs=True
        )
        changes = follower.start_one_off()
        next(changes)
        params = responses.calls[1].request.params
        self.assertEqual(
            params["limit"],
            "5125",
            "Limit should be set to the expected value.",
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
        self.prepare_mock_changes(
            batches=1, db_info_doc_count=1, db_info_doc_size=(5 * 1024 * 1024 - 1)
        )
        follower = ChangesFollower(
            self.client, db="db", error_tolerance=0, include_docs=True
        )
        changes = follower.start_one_off()
        next(changes)
        params = responses.calls[1].request.params
        self.assertEqual(
            params["limit"],
            "1",
            "Limit should be set to the expected value.",
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
            db="db",
            error_tolerance=0,
            limit=1000,
            include_docs=True,
        )
        changes = follower.start_one_off()
        next(changes)
        params = responses.calls[1].request.params
        self.assertEqual(
            params["limit"],
            "1000",
            "Limit should be set to the expected value.",
        )


@pytest.mark.usefixtures("limits", "errors")
class TestChangesFollowerListen(ChangesFollowerBaseCase):
    @responses.activate
    def test_start(self):
        """
        Checks that a LISTEN mode completes successfully (after stopping)
        with some batches.
        """
        try:
            self.prepare_mock_changes(batches=3)
            follower = ChangesFollower(self.client, db="db")
            count = self.runner(follower, _Mode.LISTEN, timeout=2)
        except BaseException:
            self.fail("There should be no exception.")
        self.assertGreater(count, 2 * _BATCH_SIZE + 1, "There should be some changes.")

    @responses.activate
    def test_start_terminal_errors(self):
        """
        Checks that a LISTEN mode errors for all terminal errors.
        """
        for error in self.terminal_errors:
            self.prepare_mock_with_error(error)
            follower = ChangesFollower(self.client, db="db")
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
            follower = ChangesFollower(self.client, db="db", error_tolerance=0)
            if error == "bad_io":
                with self.assertRaises(ConnectionError):
                    self.runner(follower, _Mode.LISTEN, timeout=1)
            else:
                if error == "bad_json":
                    error = "Error processing the HTTP response"
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
            follower = ChangesFollower(self.client, db="db", error_tolerance=100)
            if error == "bad_io":
                with self.assertRaises(ConnectionError):
                    self.runner(follower, _Mode.LISTEN, timeout=1)
            else:
                if error == "bad_json":
                    error = "Error processing the HTTP response"
                with self.assertRaisesRegex(ApiException, error):
                    self.runner(follower, _Mode.LISTEN, timeout=1)
            self.assertGreater(resp.call_count, 1, "Mock server should receive calls.")

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
            follower = ChangesFollower(self.client, db="db", error_tolerance=300)
            count = self.runner(follower, _Mode.LISTEN, timeout=1)
        except BaseException:
            self.fail("There should be no exception.")
        self.assertEqual(
            count,
            batches * _BATCH_SIZE,
            "There should be the correct number of changes.",
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
                follower = ChangesFollower(self.client, db="db")
                count = self.runner(follower, _Mode.LISTEN, timeout=1)
            except BaseException:
                self.fail("There should be no exception.")
            self.assertEqual(count, 0, "There should be no changes.")
            self.assertGreater(resp.call_count, 1, "Mock server should receive calls.")

    @responses.activate
    def test_start_transient_errors_with_max_suppression_all_changes(self):
        """
        Checks that a LISTEN mode runs through transient errors
        with max suppression to receive changes until stopped.
        """
        batches = 2
        self.prepare_mock_changes(
            batches=batches,
            errors=self.transient_errors,
        )
        try:
            follower = ChangesFollower(self.client, db="db")
            count = self.runner(follower, _Mode.LISTEN, timeout=1)
        except BaseException:
            self.fail("There should be no exception.")
        self.assertEqual(
            count,
            batches * _BATCH_SIZE,
            "There should be the correct number of changes.",
        )

    @responses.activate
    def test_stop(self):
        """
        Checks calling stop for the LISTEN case.
        """
        try:
            self.prepare_mock_changes(batches=MAX_BATCHES)
            follower = ChangesFollower(self.client, db="db")
            start = timeit.default_timer()
            count = self.runner(follower, _Mode.LISTEN, timeout=2, stop_after=1000)
            stop = timeit.default_timer() - start
        except BaseException:
            self.fail("There should be no exception.")
        self.assertGreaterEqual(count, 1000, "There should be some changes.")
        self.assertLess(stop, 2, "The thread should have stopped before the wait time.")

    @responses.activate
    def test_state_error(self):
        """
        Checks that a LISTEN follower can only be started once.
        """
        try:
            self.prepare_mock_changes(batches=MAX_BATCHES)
            follower = ChangesFollower(self.client, db="db")
            self.runner(follower, _Mode.LISTEN, timeout=1, stop_after=1000)
            with self.assertRaisesRegex(
                RuntimeError, "Cannot start a feed that has already started."
            ):
                follower.start_one_off()
            with self.assertRaisesRegex(
                RuntimeError, "Cannot start a feed that has already started."
            ):
                follower.start()
        except BaseException:
            self.fail("There should be no exception.")

    @responses.activate
    def test_limit(self):
        """
        Checks that setting a limit terminates iterations early for LISTEN mode
        and limits smaller, the same and larger than the default batch size.
        """
        for limit in self.limits:
            try:
                self.prepare_mock_changes(batches=MAX_BATCHES)
                follower = ChangesFollower(self.client, db="db", limit=limit)
                count = self.runner(follower, _Mode.LISTEN, timeout=180)
            except BaseException:
                self.fail("There should be no exception.")
            self.assertEqual(
                count,
                limit,
                "There should be the correct number of changes.",
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
            follower = ChangesFollower(self.client, db="db")
            count = self.runner(follower, _Mode.LISTEN, timeout=0.6)
        except BaseException:
            self.fail("There should be no exception.")
        self.assertEqual(count, 0, "There should be no changes.")
        self.assertLessEqual(resp.call_count, 15, "Call count should not exceed limit.")

def _seq(n):
    """Build a seq string from an integer, e.g. _seq(11) -> '11-aa'."""
    return f'{n}-aa'


def _make_row(seq):
    """Build a raw changes result item dict."""
    return {'id': 'doc', 'seq': seq, 'changes': []}


def _page_type(page_type, base):
    """
    Factory for the 9 page types.

    Type 1: rows=[b, b+1],     last_seq=b+1  (last row == last_seq, no nulls)
    Type 2: rows=[b, b+1],     last_seq=b+2  (last row != last_seq, no nulls)
    Type 3: rows=[null, b+1],  last_seq=b+1  (leading null, last row == last_seq)
    Type 4: rows=[null, b+1],  last_seq=b+2  (leading null, last row != last_seq)
    Type 5: rows=[b, null],    last_seq=b+1  (trailing null last row)
    Type 6: rows=[b, null],    last_seq=b+2  (trailing null last row, last_seq beyond)
    Type 7: rows=[null, null], last_seq=b+1  (all nulls)
    Type 8: rows=[null, null], last_seq=b+2  (all nulls, last_seq beyond)
    Type 9: rows=[],           last_seq=b    (empty page)
    """
    if page_type == 1:
        return {'results': [_make_row(_seq(base)), _make_row(_seq(base + 1))],
                'last_seq': _seq(base + 1), 'pending': 0}
    elif page_type == 2:
        return {'results': [_make_row(_seq(base)), _make_row(_seq(base + 1))],
                'last_seq': _seq(base + 2), 'pending': 0}
    elif page_type == 3:
        return {'results': [_make_row(None), _make_row(_seq(base + 1))],
                'last_seq': _seq(base + 1), 'pending': 0}
    elif page_type == 4:
        return {'results': [_make_row(None), _make_row(_seq(base + 1))],
                'last_seq': _seq(base + 2), 'pending': 0}
    elif page_type == 5:
        return {'results': [_make_row(_seq(base)), _make_row(None)],
                'last_seq': _seq(base + 1), 'pending': 0}
    elif page_type == 6:
        return {'results': [_make_row(_seq(base)), _make_row(None)],
                'last_seq': _seq(base + 2), 'pending': 0}
    elif page_type == 7:
        return {'results': [_make_row(None), _make_row(None)],
                'last_seq': _seq(base + 1), 'pending': 0}
    elif page_type == 8:
        return {'results': [_make_row(None), _make_row(None)],
                'last_seq': _seq(base + 2), 'pending': 0}
    elif page_type == 9:
        return {'results': [], 'last_seq': _seq(base), 'pending': 0}
    else:
        raise ValueError(f'Unknown page type: {page_type}')


def _populate_iterator(pages):
    """
    Build a _ChangesFollowerIterator and populate its _seq_markers by calling
    _update_seq_markers for each page.
    """
    from ibmcloudant.features.changes_follower import _ChangesFollowerIterator
    from threading import Lock

    iterator = _ChangesFollowerIterator.__new__(_ChangesFollowerIterator)
    iterator._seq_markers = []
    iterator._seq_markers_lock = Lock()

    for page in pages:
        iterator._update_seq_markers(page['results'], page['last_seq'])

    return iterator


def _last_seq_since(pages, query_seq):
    """Populate an iterator with pages and call last_seq_since directly."""
    return _populate_iterator(pages).last_seq_since(query_seq)


# ---------------------------------------------------------------------------
# TestSeqMarkers — unit tests for _ChangesFollowerIterator.last_seq_since
# ---------------------------------------------------------------------------

class TestSeqMarkers(unittest.TestCase):

    # -----------------------------------------------------------------------
    # Not-found / empty edge cases
    # -----------------------------------------------------------------------

    def test_last_seq_since_not_found(self):
        """Returns the input seq unchanged when not found in markers."""
        result = _last_seq_since([_page_type(1, 10)], '999-ff')
        self.assertEqual(result, '999-ff')

    def test_last_seq_since_empty_seq_markers(self):
        """Returns the input seq unchanged when markers are empty."""
        result = _last_seq_since([], '1-aa')
        self.assertEqual(result, '1-aa')

    # -----------------------------------------------------------------------
    # Per-page-type: single page
    # -----------------------------------------------------------------------

    def test_last_seq_since_single_page(self):
        cases = [
            ('Type 1: last row seq (== last_seq)',     1, 10, _seq(11), _seq(11)),
            ('Type 3: last row seq (== last_seq)',     3, 10, _seq(11), _seq(11)),
            ('Type 2: last row seq -> last_seq',       2, 10, _seq(11), _seq(12)),
            ('Type 2: last_seq key -> itself',         2, 10, _seq(12), _seq(12)),
            ('Type 4: last row seq -> last_seq',       4, 10, _seq(11), _seq(12)),
            ('Type 4: last_seq key -> itself',         4, 10, _seq(12), _seq(12)),
            ('Type 5: non-stored row seq unchanged',   5, 10, _seq(10), _seq(10)),
            ('Type 5: last_seq key -> itself',         5, 10, _seq(11), _seq(11)),
            ('Type 6: non-stored row seq unchanged',   6, 10, _seq(10), _seq(10)),
            ('Type 6: last_seq key -> itself',         6, 10, _seq(12), _seq(12)),
            ('Type 7: last_seq key -> itself',         7, 10, _seq(11), _seq(11)),
            ('Type 8: last_seq key -> itself',         8, 10, _seq(12), _seq(12)),
            ('Type 9: last_seq key -> itself',         9, 10, _seq(10), _seq(10)),
        ]
        for name, page_type, base, query_seq, expected in cases:
            with self.subTest(name):
                result = _last_seq_since([_page_type(page_type, base)], query_seq)
                self.assertEqual(result, expected)

    # -----------------------------------------------------------------------
    # Per-page-type: followed by a non-empty page (type 1 at base 20)
    # Page 2 inserts ROW('21-aa') which blocks advancement.
    # -----------------------------------------------------------------------

    def test_last_seq_since_followed_by_non_empty(self):
        cases = [
            ('Type 1 + non-empty: blocked by p2 ROW',           1, 10, _seq(11), _seq(11)),
            ('Type 2 + non-empty: last row seq -> p1 last_seq', 2, 10, _seq(11), _seq(12)),
            ('Type 2 + non-empty: last_seq key -> p1 last_seq', 2, 10, _seq(12), _seq(12)),
            ('Type 3 + non-empty: blocked by p2 ROW',           3, 10, _seq(11), _seq(11)),
            ('Type 4 + non-empty: last row seq -> p1 last_seq', 4, 10, _seq(11), _seq(12)),
            ('Type 4 + non-empty: last_seq key -> p1 last_seq', 4, 10, _seq(12), _seq(12)),
            ('Type 5 + non-empty: blocked by p2 ROW',           5, 10, _seq(11), _seq(11)),
            ('Type 6 + non-empty: blocked by p2 ROW',           6, 10, _seq(12), _seq(12)),
            ('Type 7 + non-empty: blocked by p2 ROW',           7, 10, _seq(11), _seq(11)),
            ('Type 8 + non-empty: blocked by p2 ROW',           8, 10, _seq(12), _seq(12)),
            ('Type 9 + non-empty: blocked by p2 ROW',           9, 10, _seq(10), _seq(10)),
        ]
        for name, page_type, base, query_seq, expected in cases:
            with self.subTest(name):
                result = _last_seq_since([_page_type(page_type, base), _page_type(1, 20)], query_seq)
                self.assertEqual(result, expected)

    # -----------------------------------------------------------------------
    # Per-page-type: followed by an empty page (type 9 at base 20)
    # Page 2 inserts only PAGE('20-aa') — no ROW to block, advances to '20-aa'.
    # -----------------------------------------------------------------------

    def test_last_seq_since_followed_by_empty(self):
        cases = [
            ('Type 1 + empty: advances to p2 last_seq',     1, 10, _seq(11), _seq(20)),
            ('Type 2 + empty: last row seq advances to p2', 2, 10, _seq(11), _seq(20)),
            ('Type 2 + empty: last_seq key advances to p2', 2, 10, _seq(12), _seq(20)),
            ('Type 3 + empty: advances to p2 last_seq',     3, 10, _seq(11), _seq(20)),
            ('Type 4 + empty: last row seq advances to p2', 4, 10, _seq(11), _seq(20)),
            ('Type 4 + empty: last_seq key advances to p2', 4, 10, _seq(12), _seq(20)),
            ('Type 5 + empty: last_seq advances to p2',     5, 10, _seq(11), _seq(20)),
            ('Type 6 + empty: last_seq advances to p2',     6, 10, _seq(12), _seq(20)),
            ('Type 7 + empty: last_seq advances to p2',     7, 10, _seq(11), _seq(20)),
            ('Type 8 + empty: last_seq advances to p2',     8, 10, _seq(12), _seq(20)),
            ('Type 9 + empty: advances to p2 last_seq',     9, 10, _seq(10), _seq(20)),
        ]
        for name, page_type, base, query_seq, expected in cases:
            with self.subTest(name):
                result = _last_seq_since([_page_type(page_type, base), _page_type(9, 20)], query_seq)
                self.assertEqual(result, expected)

    # -----------------------------------------------------------------------
    # All 8 three-page sequences of empty (E=type 9) and non-empty (N=type 1).
    # Query from page 1's last_seq key. E adds only PAGE; N adds ROW+PAGE.
    # -----------------------------------------------------------------------

    def test_last_seq_since_3_page_sequence(self):
        cases = [
            ('NNN: blocked by p2 ROW -> p1 last_seq',
             [1, 1, 1], [10, 20, 30], _seq(11), _seq(11)),
            ('NNE: blocked by p2 ROW -> p1 last_seq',
             [1, 1, 9], [10, 20, 30], _seq(11), _seq(11)),
            ('NEE: advances through both empty pages',
             [1, 9, 9], [10, 20, 30], _seq(11), _seq(30)),
            ('NEN: advances through p2 empty, stops at p3 ROW',
             [1, 9, 1], [10, 20, 30], _seq(11), _seq(20)),
            ('ENN: blocked by p2 ROW -> p1 last_seq',
             [9, 1, 1], [10, 20, 30], _seq(10), _seq(10)),
            ('ENE: blocked by p2 ROW -> p1 last_seq',
             [9, 1, 9], [10, 20, 30], _seq(10), _seq(10)),
            ('EEN: advances through p2, stops at p3 ROW',
             [9, 9, 1], [10, 20, 30], _seq(10), _seq(20)),
            ('EEE: advances through all three empty pages',
             [9, 9, 9], [10, 20, 30], _seq(10), _seq(30)),
        ]
        for name, types, bases, query_seq, expected in cases:
            with self.subTest(name):
                pages = [_page_type(t, b) for t, b in zip(types, bases)]
                result = _last_seq_since(pages, query_seq)
                self.assertEqual(result, expected)

    # -----------------------------------------------------------------------
    # Eviction
    # Each non-empty page (type 2) adds 2 entries (ROW + PAGE).
    # With CAPACITY=200 and EVICTION_COUNT=20, adding 101 pages triggers one
    # eviction of the oldest 20 entries (first 10 pages).
    # Entries for page 0 (base=0) should be gone; most recent should remain.
    # -----------------------------------------------------------------------

    def test_last_seq_since_eviction(self):
        pages = [_page_type(2, i * 10) for i in range(101)]
        iterator = _populate_iterator(pages)

        # Page 0 (base=0): row=_seq(1), page=_seq(2) — evicted
        self.assertEqual(iterator.last_seq_since(_seq(1)), _seq(1))
        self.assertEqual(iterator.last_seq_since(_seq(2)), _seq(2))

        # Most recent page (base=1000): row=_seq(1001), page=_seq(1002) — still present
        self.assertEqual(iterator.last_seq_since(_seq(1001)), _seq(1002))
        self.assertEqual(iterator.last_seq_since(_seq(1002)), _seq(1002))


# ---------------------------------------------------------------------------
# TestGetLastSeqNewerThan — unit tests for ChangesFollower.get_last_seq_newer_than
# ---------------------------------------------------------------------------

class TestGetLastSeqNewerThan(ChangesFollowerBaseCase):

    def test_get_last_seq_newer_than_with_none(self):
        """Raises ValueError when passed None."""
        follower = ChangesFollower(self.client, db='db')
        with self.assertRaisesRegex(ValueError, 'The provided sequence ID cannot be null or empty'):
            follower.get_last_seq_newer_than(None)

    def test_get_last_seq_newer_than_with_empty_string(self):
        """Raises ValueError when passed an empty string."""
        follower = ChangesFollower(self.client, db='db')
        with self.assertRaisesRegex(ValueError, 'The provided sequence ID cannot be null or empty'):
            follower.get_last_seq_newer_than('')

    def test_get_last_seq_newer_than_before_feed_starts(self):
        """Returns the input seq unchanged when the feed has not started yet."""
        follower = ChangesFollower(self.client, db='db')
        self.assertEqual(follower.get_last_seq_newer_than('seq-a'), 'seq-a')

    @responses.activate
    def test_get_last_seq_newer_than_unknown_seq(self):
        """Returns the input seq unchanged when it was never seen by this follower."""
        self.prepare_mock_changes(batches=1)
        follower = ChangesFollower(self.client, db='db')
        changes = follower.start_one_off()
        for _ in changes:
            pass
        self.assertEqual(follower.get_last_seq_newer_than('seq-unknown'), 'seq-unknown')

    @responses.activate
    def test_get_last_seq_newer_than_middle_of_batch(self):
        """
        Returns the input seq unchanged when querying with a seq from the
        middle of a batch — only the last item's seq is stored in seq_markers.
        """
        self.prepare_mock_changes(batches=1)
        follower = ChangesFollower(self.client, db='db')
        changes = follower.start_one_off()
        items = list(changes)
        # seq-a and seq-b are middle items — not stored in seq_markers
        seq_a = items[0].seq
        seq_b = items[1].seq
        self.assertEqual(follower.get_last_seq_newer_than(seq_a), seq_a)
        self.assertEqual(follower.get_last_seq_newer_than(seq_b), seq_b)

    @responses.activate
    def test_get_last_seq_newer_than_end_to_end(self):
        """Returns the correct last_seq through a completed stream."""
        self.prepare_mock_changes(batches=1)
        follower = ChangesFollower(self.client, db='db')
        changes = follower.start_one_off()
        items = list(changes)
        # Last item's seq should map to the page's last_seq
        last_item_seq = items[-1].seq
        result = follower.get_last_seq_newer_than(last_item_seq)
        # The last item seq IS the last_seq for a normal page (type 1 equivalent)
        self.assertEqual(result, last_item_seq)
