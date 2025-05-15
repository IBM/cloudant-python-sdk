# coding: utf-8

# © Copyright IBM Corporation 2025.
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

from collections.abc import Callable
from typing import Iterable
from unittest.mock import Mock, patch
from ibmcloudant.cloudant_v1 import ViewResult, ViewResultRow
from ibmcloudant.features.pagination import _BasePageIterator, _IteratorPager, Pager, PagerType, Pagination
from conftest import MockClientBaseCase, PaginationMockResponse

class BasePageMockResponses(PaginationMockResponse):
  """
  Test class for mocking page responses.
  """
  def __init__(self, total_items: int, page_size: int):
    super().__init__(total_items, page_size, PagerType.POST_VIEW)
    # This test uses View structures, but doesn't do n+1 like a view/key pager
    # Override plus_one_paging to accommodate this weird hybrid
    self.plus_one_paging = False

class TestPageIterator(_BasePageIterator):
  """
  A test subclass of the _BasePager under test.
  """
  operation: Callable = None
  page_keys: list[str] = []

  def __init__(self, client, opts):
    super().__init__(client, TestPageIterator.operation or client.post_view, TestPageIterator.page_keys, opts)

  def _result_converter(self) -> Callable[[dict], ViewResult]:
    return lambda d: ViewResult.from_dict(d)

  def _items(self, result: ViewResult) -> tuple[ViewResultRow]:
    return result.rows

  def _get_next_page_options(self, result: ViewResult) -> dict:
    if len(result.rows ) == 0:
      self.assertFail("Test failure: tried to setNextPageOptions on empty page.")
    else:
      return {'start_key': result.rows[-1].key}

class TestBasePageIterator(MockClientBaseCase):
  def test_init(self):
    operation = self.client.post_view
    opts = {'db': 'test', 'limit': 20}
    page_iterator: Iterable[ViewResultRow] = TestPageIterator(self.client, opts)
    # Assert client is set
    self.assertEqual(page_iterator._client, self.client, 'The supplied client should be set.')
    # Assert operation is set
    self.assertIsNotNone(page_iterator._next_request_function, 'The operation function should be set.')
    # Assert partial function parts are as expected
    self.assertEqual(page_iterator._next_request_function.func, operation, 'The partial function should be the operation.')
    self.assertEqual(page_iterator._next_request_function.keywords, opts, 'The partial function kwargs should be the options.')

  def test_partial_options(self):
    static_opts = {'db': 'test', 'limit': 20, 'baz': 'faz'}
    page_opts = {'foo': 'boo', 'bar': 'far'}
    opts = {**static_opts, **page_opts}
    # Use page_opts.keys() to pass the list of names for page options
    with patch('test_pagination_base.TestPageIterator.page_keys', page_opts.keys()):
      page_iterator: Iterable[ViewResultRow] = TestPageIterator(self.client, opts)
    # Assert partial function has only static opts
    self.assertEqual(page_iterator._next_request_function.keywords, static_opts, 'The partial function kwargs should be only the static options.')
    # Assert next page options
    self.assertEqual(page_iterator._next_page_opts, page_opts, 'The next page options should match the expected.')

  def test_default_page_size(self):
    opts = {'db': 'test'}
    page_iterator: Iterable[ViewResultRow] = TestPageIterator(self.client, opts)
    # Assert the default page size
    expected_page_size = 200
    self.assertEqual(page_iterator._page_size, expected_page_size, 'The default page size should be set.')
    self.assertEqual(page_iterator._next_request_function.keywords, opts | {'limit': expected_page_size}, 'The default page size should be present in the options.')

  def test_limit_page_size(self):
    opts = {'db': 'test', 'limit': 42}
    page_iterator: Iterable[ViewResultRow] = TestPageIterator(self.client, opts)
    # Assert the provided page size
    expected_page_size = 42
    self.assertEqual(page_iterator._page_size, expected_page_size, 'The default page size should be set.')
    self.assertEqual(page_iterator._next_request_function.keywords, opts | {'limit': expected_page_size}, 'The default page size should be present in the options.')

  def test_has_next_initially_true(self):
    opts = {'limit': 1}
    page_iterator: Iterable[ViewResultRow] = TestPageIterator(self.client, opts)
    # Assert _has_next
    self.assertTrue(page_iterator._has_next, '_has_next should initially return True.')

  def test_has_next_true_for_result_equal_to_limit(self):
    page_size = 1
    # Init with mock that returns only a single row
    with patch('test_pagination_base.TestPageIterator.operation', BasePageMockResponses(1, page_size).get_next_page):
      page_iterator: Iterable[ViewResultRow] = TestPageIterator(
          self.client,
          {'limit': page_size})
      # Get first page with 1 result
      next(page_iterator)
      # Assert _has_next
      self.assertTrue(page_iterator._has_next, '_has_next should return True.')

  def test_has_next_false_for_result_less_than_limit(self):
    page_size = 1
    # Init with mock that returns zero rows
    with patch('test_pagination_base.TestPageIterator.operation', BasePageMockResponses(0, page_size).get_next_page):
      page_iterator: Iterable[ViewResultRow] = TestPageIterator(
          self.client,
          {'limit': page_size})
      # Get first page with 0 result
      next(page_iterator)
      # Assert _has_next
      self.assertFalse(page_iterator._has_next, '_has_next should return False.')

  def test_next_first_page(self):
    page_size = 25
    # Mock that returns one page of 25 items
    mock = BasePageMockResponses(page_size, page_size)
    with patch('test_pagination_base.TestPageIterator.operation', mock.get_next_page):
      page_iterator: Iterable[ViewResultRow] = TestPageIterator(
          self.client,
          {'limit': page_size})
      # Get first page
      actual_page: list[ViewResultRow] = next(page_iterator)
      # Assert first page
      self.assertSequenceEqual(actual_page, mock.get_expected_page(1), "The actual page should match the expected page")

  def test_next_two_pages(self):
    page_size = 3
    # Mock that returns two pages of 3 items
    mock = BasePageMockResponses(2*page_size, page_size)
    with patch('test_pagination_base.TestPageIterator.operation', mock.get_next_page):
      page_iterator: Iterable[ViewResultRow] = TestPageIterator(
          self.client,
          {'limit': page_size})
      # Get first page
      actual_page_1: list[ViewResultRow] = next(page_iterator)
      # Assert first page
      self.assertSequenceEqual(actual_page_1, mock.get_expected_page(1), "The actual page should match the expected page")
      # Assert has_next
      self.assertTrue(page_iterator._has_next, '_has_next should return True.')
      # Get second page
      actual_page_2: list[ViewResultRow] = next(page_iterator)
      # Assert first page
      self.assertSequenceEqual(actual_page_2, mock.get_expected_page(2), "The actual page should match the expected page")
      # Assert has_next, True since page is not smaller than limit
      self.assertTrue(page_iterator._has_next, '_has_next should return True.')

  def test_next_until_empty(self):
    page_size = 3
    # Mock that returns 3 pages of 3 items
    mock = BasePageMockResponses(3*page_size, page_size)
    with patch('test_pagination_base.TestPageIterator.operation', mock.get_next_page):
      page_iterator: Iterable[ViewResultRow] = TestPageIterator(
          self.client,
          {'limit': page_size})
      page_count = 0
      actual_items = []
      while page_iterator._has_next:
        page_count += 1
        page = next(page_iterator)
        # Assert each page is the same or smaller than the limit to confirm all results not in one page
        self.assertTrue(len(page) <= page_size, "The actual page size should be the expected page size.")
        actual_items.extend(page)
      self.assertSequenceEqual(actual_items, mock.all_expected_items(), "The results should match all the pages.")
      self.assertEqual(page_count, len(mock.expected_pages), "There should be the correct number of pages.")

  def test_next_until_smaller(self):
    page_size = 3
    # Mock that returns 3 pages of 3 items, then 1 more page with 1 item
    mock = BasePageMockResponses(3*page_size + 1, page_size)
    with patch('test_pagination_base.TestPageIterator.operation', mock.get_next_page):
      page_iterator: Iterable[ViewResultRow] = TestPageIterator(
          self.client,
          {'limit': page_size})
      page_count = 0
      actual_items = []
      while page_iterator._has_next:
        page_count += 1
        page = next(page_iterator)
        # Assert each page is the same or smaller than the limit to confirm all results not in one page
        self.assertTrue(len(page) <= page_size, "The actual page size should be the expected page size.")
        actual_items.extend(page)
      self.assertSequenceEqual(actual_items, mock.all_expected_items(), "The results should match all the pages.")
      self.assertEqual(page_count, len(mock.expected_pages), "There should be the correct number of pages.")

  def test_next_exception(self):
    page_size = 2
    # Mock that returns one page of one item
    mock = BasePageMockResponses(page_size - 1, page_size)
    with patch('test_pagination_base.TestPageIterator.operation', mock.get_next_page):
      page_iterator: Iterable[ViewResultRow] = TestPageIterator(
          self.client,
          {'limit': page_size})
      # Get first and only page
      actual_page: list[ViewResultRow] = next(page_iterator)
      # Assert page
      self.assertSequenceEqual(actual_page, mock.get_expected_page(1), "The actual page should match the expected page")
      # Assert _has_next now False
      self.assertFalse(page_iterator._has_next, '_has_next should return False.')
      # Assert StopIteraton on get_next()
      with self.assertRaises(StopIteration):
        next(page_iterator)

  def test_pages_immutable(self):
    page_size = 1
    mock = BasePageMockResponses(page_size, page_size)
    with patch('test_pagination_base.TestPageIterator.operation', mock.get_next_page):
      page_iterator: Iterable[ViewResultRow] = TestPageIterator(
          self.client,
          {'limit': page_size})
      # Get page
      actual_page: list[ViewResultRow] = next(page_iterator)
      # Assert immutable tuple type
      self.assertIsInstance(actual_page, tuple)

  def test_set_next_page_options(self):
    page_size = 1
    mock = BasePageMockResponses(5*page_size, page_size)
    with patch('test_pagination_base.TestPageIterator.operation', mock.get_next_page):
      page_iterator: Iterable[ViewResultRow] = TestPageIterator(
          self.client,
          {'limit': page_size})
      self.assertIsNone(page_iterator._next_page_opts.get('start_key'), "The start key should intially be None.")
      # Since we use a page size of 1, each next page options key, is the same as the element from the page and the page count
      page_count = 0
      while page_iterator._has_next:
        page = next(page_iterator)
        if page_iterator._has_next:
          self.assertEqual(page_count, page_iterator._next_page_opts.get('start_key'), "The key should increment per page.")
        else:
          self.assertEqual(page_count - 1, page_iterator._next_page_opts.get('start_key'), "The options should not be set for the final page.")
        page_count += 1

  def test_next_resumes_after_error(self):
    page_size = 1
    mock = BasePageMockResponses(3*page_size, page_size)
    with patch('test_pagination_base.TestPageIterator.operation', mock.get_next_page):
      page_iterator: Iterable[ViewResultRow] = TestPageIterator(
          self.client,
          {'limit': page_size})
      self.assertIsNone(page_iterator._next_page_opts.get('start_key'), "The start key should intially be None.")
      actual_page = next(page_iterator)
      self.assertSequenceEqual(actual_page, mock.get_expected_page(1), "The actual page should match the expected page")
      self.assertEqual(0, page_iterator._next_page_opts.get('start_key'), "The start_key should be 0 for the second page.")
      with patch('ibmcloudant.features.pagination._BasePageIterator._next_request', Exception('test exception')):
        with self.assertRaises(Exception):
          next(page_iterator)
      self.assertTrue(page_iterator._has_next, '_has_next should return True.')
      self.assertEqual(0, page_iterator._next_page_opts.get('start_key'), "The start_key should still be 0 for the second page.")
      second_page = next(page_iterator)
      self.assertSequenceEqual(second_page, mock.get_expected_page(2), "The actual page should match the expected page")
      self.assertTrue(page_iterator._has_next, '_has_next should return False.')


  def test_pages_iterable(self):
    page_size = 23
    mock = BasePageMockResponses(3*page_size-1, page_size)
    pagination = Pagination(self.client, TestPageIterator, {'limit': page_size})
    with patch('test_pagination_base.TestPageIterator.operation', mock.get_next_page):
      # Check pages are iterable
      page_number = 0
      for page in pagination.pages():
        page_number += 1
        self.assertSequenceEqual(page, mock.get_expected_page(page_number), "The actual page should match the expected page")
      # Asser the correct number of pages
      self.assertEqual(page_number, 3, 'There should have been 3 pages.')

  def test_rows_iterable(self):
    page_size = 23
    mock = BasePageMockResponses(3*page_size-1, page_size)
    pagination = Pagination(self.client, TestPageIterator, {'limit': page_size})
    with patch('test_pagination_base.TestPageIterator.operation', mock.get_next_page):
      actual_items = []
      # Check rows are iterable
      for row in pagination.rows():
        actual_items.append(row)
    self.assertSequenceEqual(actual_items, mock.all_expected_items(), "The actual rows should match the expected rows.")

  def test_as_pager_get_next_first_page(self):
    page_size = 7
    # Mock that returns two pages of 7 items
    mock = BasePageMockResponses(2*page_size, page_size)
    pagination = Pagination(self.client, TestPageIterator, {'limit': page_size})
    with patch('test_pagination_base.TestPageIterator.operation', mock.get_next_page):
      pager = pagination.pager()
      # Get first page
      actual_page: list[ViewResultRow] = pager.get_next()
      self.assertSequenceEqual(actual_page, mock.get_expected_page(1), "The actual page should match the expected page")

  def test_as_pager_get_all(self):
    page_size = 11
    # Mock that returns 6 pages of 11 items, then 1 more page with 5 items
    mock = BasePageMockResponses(71, page_size)
    pagination = Pagination(self.client, TestPageIterator, {'limit': page_size})
    with patch('test_pagination_base.TestPageIterator.operation', mock.get_next_page):
      pager: Pager[ViewResultRow] = pagination.pager()
      actual_items = pager.get_all()
      self.assertSequenceEqual(actual_items, mock.all_expected_items(), "The results should match all the pages.")
    # Assert consumed state prevents calling again
    with self.assertRaises(Exception, msg=_IteratorPager._state_consumed_msg):
      pager.get_all()

  def test_as_pager_get_all_restarts_after_error(self):
    page_size = 1
    mock = BasePageMockResponses(2*page_size, page_size)
    first_page = mock.get_next_page()
    # mock response order
    # first page, error, first page replay, second page
    mockmock = Mock(side_effect=[
      first_page,
      Exception('test exception'),
      first_page,
      mock.get_next_page()
    ])
    pagination = Pagination(self.client, TestPageIterator, {'limit': page_size})
    with patch('test_pagination_base.TestPageIterator.operation', mockmock):
      pager = pagination.pager()
      with self.assertRaises(Exception):
        pager.get_all()
      self.assertSequenceEqual(pager.get_all(), mock.all_expected_items(), "The results should match all the pages.")

  def test_as_pager_get_next_get_all_throws(self):
    page_size = 11
    # Mock that returns 6 pages of 11 items, then 1 more page with 5 items
    mock = BasePageMockResponses(71, page_size)
    pagination = Pagination(self.client, TestPageIterator, {'limit': page_size})
    with patch('test_pagination_base.TestPageIterator.operation', mock.get_next_page):
      pager: Pager[ViewResultRow] = pagination.pager()
      first_page = pager.get_next()
      self.assertSequenceEqual(first_page, mock.get_expected_page(1), "The actual page should match the expected page")
      # Assert throws
      with self.assertRaises(Exception, msg=_IteratorPager._state_mixed_msg):
        pager.get_all()
      # Assert second page ok
      self.assertSequenceEqual(pager.get_next(), mock.get_expected_page(2), "The actual page should match the expected page")

  def test_as_pager_get_all_get_next_throws(self):
    page_size = 1
    mock = BasePageMockResponses(2*page_size, page_size)
    first_page = mock.get_next_page()
    # mock response order
    # first page, error, first page replay, second page
    mockmock = Mock(side_effect=[
      first_page,
      Exception('test exception')
    ])
    pagination = Pagination(self.client, TestPageIterator, {'limit': page_size})
    with patch('test_pagination_base.TestPageIterator.operation', mockmock):
      pager = pagination.pager()
      # Stop get all part way through so it isn't consumed when we call get Next
      with self.assertRaises(Exception):
        pager.get_all()
      # Assert calling get_next() throws
      with self.assertRaises(Exception, msg=_IteratorPager._state_mixed_msg):
        pager.get_next()

  def test_as_pager_get_next_resumes_after_error(self):
    page_size = 1
    mock = BasePageMockResponses(2*page_size, page_size)
    # mock response order
    # first page, error, second page
    mockmock = Mock(side_effect=[
      mock.get_next_page(),
      Exception('test exception'),
      mock.get_next_page()
    ])
    pagination = Pagination(self.client, TestPageIterator, {'limit': page_size})
    with patch('test_pagination_base.TestPageIterator.operation', mockmock):
      pager = pagination.pager()
      # Assert first page
      self.assertSequenceEqual(pager.get_next(), mock.get_expected_page(1), "The actual page should match the expected page")
      with self.assertRaises(Exception):
        pager.get_next()
      # Assert second page after error
      self.assertSequenceEqual(pager.get_next(), mock.get_expected_page(2), "The actual page should match the expected page")

  def test_as_pager_get_next_until_consumed(self):
    page_size = 7
    # Mock that returns two pages of 7 items
    mock = BasePageMockResponses(2*page_size, page_size)
    pagination = Pagination(self.client, TestPageIterator, {'limit': page_size})
    with patch('test_pagination_base.TestPageIterator.operation', mock.get_next_page):
      pager = pagination.pager()
      page_count = 0
      while pager.has_next():
        page_count += 1
        self.assertSequenceEqual(pager.get_next(), mock.get_expected_page(page_count), "The actual page should match the expected page")
      # Note 3 because third page is empty
      self.assertEqual(page_count, 3, 'There should be the expected number of pages.')
    # Assert consumed state prevents calling again
    with self.assertRaises(Exception, msg=_IteratorPager._state_consumed_msg):
      pager.get_next()
