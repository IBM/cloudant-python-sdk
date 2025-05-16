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

from typing import Sequence
import unittest
import pytest
import os
import json
import responses

from threading import Timer

import itertools

from requests import codes
from requests.exceptions import ConnectionError

from ibm_cloud_sdk_core import ApiException, DetailedResponse

from ibmcloudant.cloudant_v1 import (
    AllDocsResult,
    CloudantV1,
    FindResult,
    PostChangesEnums,
    ChangesResult,
    ChangesResultItem,
    SearchResult,
    ViewResult,
)

from ibmcloudant.features.changes_follower import (
    _LONGPOLL_TIMEOUT,
    _BATCH_SIZE,
    _Mode,
)
from ibmcloudant.features.pagination import PagerType


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

class MockClientBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup client env config
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'
        os.environ['TEST_SERVICE_URL'] = 'http://localhost:5984'
        cls.client = CloudantV1.new_instance(
            service_name='TEST_SERVICE',
        )

    def make_error_tuple(self, error: str) -> tuple[any]:
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

    def make_error(self, error: str) -> dict[str:any]:
        error_tuple = self.make_error_tuple(error)
        if error == 'bad_io':
            return {'body': error_tuple[2]}
        else:
            return {
                'status': error_tuple[0],
                'content_type': 'application/json',
                'body': error_tuple[2],
            }

    def make_error_exception(self, error: str) -> Exception:
        error_dict = self.make_error(error)
        if error == 'bad_io':
            return error_dict['body']
        elif error == 'bad_json':
            return ApiException(code=error_dict['status'],
                    message='Error processing the HTTP response',)
        return ApiException(error_dict['status'])

class ChangesFollowerBaseCase(MockClientBaseCase):

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
                    return self.make_error_tuple(error)
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
        return responses.post(url, **self.make_error(error))

    def runner(self, follower, mode, timeout=1, stop_after=0):
        """
        blocking runner with timeout
        """

        def main():
            if mode == _Mode.LISTEN:
                changes = follower.start()
            elif mode == _Mode.FINITE:
                changes = follower.start_one_off()
            stop_timer = Timer(timeout, follower.stop)
            stop_timer.start()
            counter = 0
            try:
                for _ in changes:
                    counter += 1
                    if stop_after > 0 and stop_after == counter:
                        follower.stop()
                        break
            finally:
                stop_timer.cancel()
            return counter

        return main()

class PaginationMockSupport:
    all_docs_pagers: Sequence[PagerType] = (
        PagerType.POST_ALL_DOCS,
        PagerType.POST_DESIGN_DOCS,
        PagerType.POST_PARTITION_ALL_DOCS
    )
    view_pagers: Sequence[PagerType] = (
        PagerType.POST_VIEW,
        PagerType.POST_PARTITION_VIEW
    )
    # the key pager types (n+1 paging)
    key_pagers: Sequence[PagerType] = all_docs_pagers + view_pagers
    find_pagers: Sequence[PagerType] = (
        PagerType.POST_FIND,
        PagerType.POST_PARTITION_FIND)
    search_pagers: Sequence[PagerType] = (
        PagerType.POST_SEARCH,
        PagerType.POST_PARTITION_SEARCH)

    # Map of pager type to a tuple of patch function name, result wrapper lambda, result row lambda
    operation_map: dict[PagerType:str] = {
        PagerType.POST_ALL_DOCS: 'ibmcloudant.cloudant_v1.CloudantV1.post_all_docs',
        PagerType.POST_DESIGN_DOCS: 'ibmcloudant.cloudant_v1.CloudantV1.post_design_docs',
        PagerType.POST_FIND: 'ibmcloudant.cloudant_v1.CloudantV1.post_find',
        PagerType.POST_PARTITION_ALL_DOCS: 'ibmcloudant.cloudant_v1.CloudantV1.post_partition_all_docs',
        PagerType.POST_PARTITION_FIND: 'ibmcloudant.cloudant_v1.CloudantV1.post_partition_find',
        PagerType.POST_PARTITION_SEARCH: 'ibmcloudant.cloudant_v1.CloudantV1.post_partition_search',
        PagerType.POST_PARTITION_VIEW: 'ibmcloudant.cloudant_v1.CloudantV1.post_partition_view',
        PagerType.POST_SEARCH: 'ibmcloudant.cloudant_v1.CloudantV1.post_search',
        PagerType.POST_VIEW: 'ibmcloudant.cloudant_v1.CloudantV1.post_view'
    }

    def make_wrapper(pager_type: PagerType, total: int, rows: Sequence) -> dict[str:any]:
        if pager_type in PaginationMockSupport.key_pagers:
            return {'total_rows': total, 'rows': rows}
        else:
            bkmk = 'emptypagebookmark'
            last_row = rows[-1] if len(rows) > 0 else None
            if pager_type in PaginationMockSupport.find_pagers:
                return {'bookmark': last_row['_id'] if last_row else bkmk, 'docs': rows}
            elif pager_type in PaginationMockSupport.search_pagers:
                return {'bookmark': last_row['id'] if last_row else bkmk, 'total_rows': total, 'rows': rows}
            else:
                raise Exception('Unknown pager type, fail test.')

    def make_row(pager_type: PagerType, i: int) -> dict[str:any]:
        id = f'testdoc{i}'
        rev = f'1-abc{i}'
        if pager_type in PaginationMockSupport.key_pagers:
            if pager_type in (PagerType.POST_VIEW, PagerType.POST_PARTITION_VIEW):
                key = i
                value = 1
            else:
                key = id
                value = {'rev': rev}
            return {'id': id, 'key': key, 'value': value}
        elif pager_type in PaginationMockSupport.find_pagers:
            return {'_id':id, '_rev': rev, 'testfield': i}
        elif pager_type in PaginationMockSupport.search_pagers:
            return {'fields':{}, 'id': id}
        else:
            raise Exception('Unknown pager type, fail test.')

class PaginationMockResponse:
    """
    Test class for mocking page responses.
    """
    def __init__(self,
                total_items: int,
                page_size: int,
                pager_type: PagerType
                ):
        self.total_items: int = total_items
        self.page_size: int = page_size
        self.pages = self.generator()
        self.pager_type: PagerType = pager_type
        self.plus_one_paging: bool = self.pager_type in PaginationMockSupport.key_pagers
        self.expected_pages: list[list] = []

    def generator(self):
        for page in itertools.batched(range(0, self.total_items), self.page_size):
            rows = [PaginationMockSupport.make_row(self.pager_type, i) for i in page]
            if self.plus_one_paging:
                # Add an n+1 row for key based paging if more pages
                if (n_plus_one := page[-1] + 1) < self.total_items:
                    rows.append(PaginationMockSupport.make_row(self.pager_type, n_plus_one))
            yield DetailedResponse(response=PaginationMockSupport.make_wrapper(self.pager_type, self.total_items, rows))
        yield DetailedResponse(response=PaginationMockSupport.make_wrapper(self.pager_type, self.total_items, []))

    def convert_result(self, result: dict) -> Sequence:
        if self.pager_type in PaginationMockSupport.all_docs_pagers:
            return AllDocsResult.from_dict(result).rows
        elif self.pager_type in PaginationMockSupport.find_pagers:
            return FindResult.from_dict(result).docs
        elif self.pager_type in PaginationMockSupport.search_pagers:
            return SearchResult.from_dict(result).rows
        elif self.pager_type in PaginationMockSupport.view_pagers:
            return ViewResult.from_dict(result).rows

    def get_next_page(self, **kwargs):
        # return next(self.pages)
        # ignore kwargs
        # get next page
        page = next(self.pages)
        # convert to an expected page
        rows = self.convert_result(page.get_result())
        if len(rows) > self.page_size and self.plus_one_paging:
            self.expected_pages.append(rows[:-1])
        else:
            self.expected_pages.append(rows)
        return page

    def get_expected_page(self, page: int) -> list:
        return self.expected_pages[page - 1]

    def all_expected_items(self) -> list:
        all_items: list = []
        for page in self.expected_pages:
            all_items.extend(page)
        return all_items
