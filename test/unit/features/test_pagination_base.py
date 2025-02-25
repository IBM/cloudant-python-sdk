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
from itertools import batched
from ibm_cloud_sdk_core import DetailedResponse
from ibmcloudant.cloudant_v1 import ViewResult, ViewResultRow
from ibmcloudant.features.pagination import _BasePager, Pager
from conftest import MockClientBaseCase

class TestPager(_BasePager):
  """
  A test subclass of the _BasePager under test.
  """
  def _result_converter(self) -> Callable[[dict], ViewResult]:
    return lambda d: ViewResult.from_dict(d)

  def _items(self, result: ViewResult) -> tuple[ViewResultRow]:
    return result.rows

  def _get_next_page_options(self, result: ViewResult) -> dict:
    if len(result.rows ) == 0:
      self.assertFail("Test failure: tried to setNextPageOptions on empty page.")
    else:
      return {'start_key': result.rows[-1].key}

class MockPageReponses:
  """
  Test class for mocking page responses.
  """
  def __init__(self, total_items: int, page_size: int):
    self.total_items: int = total_items
    self.page_size: int = page_size
    self.pages = self.generator()
    self.expected_pages: list[list[ViewResultRow]] = []

  def generator(self):
    for page in batched(range(0, self.total_items), self.page_size):
      rows = [{'id':str(i), 'key':i, 'value':i} for i in page]
      yield DetailedResponse(response={'rows': rows})
    yield DetailedResponse(response={'rows': []})

  def get_next_page(self, **kwargs):
    # ignore kwargs
    # get next page
    page = next(self.pages)
    # convert to an expected page
    self.expected_pages.append(ViewResult.from_dict(page.get_result()).rows)
    return page

  def get_expected_page(self, page: int) -> list[ViewResultRow]:
    return self.expected_pages[page - 1]
  
  def all_expected_items(self) -> list[ViewResultRow]:
    all_items: list[ViewResultRow] = []
    for page in self.expected_pages:
      all_items.extend(page)
    return all_items

class TestBasePager(MockClientBaseCase):
  def test_init(self):
    operation = self.client.post_view
    opts = {'db': 'test', 'limit': 20}
    pager: Pager = TestPager(self.client, operation, [], opts)
    # Assert client is set
    self.assertEqual(pager._client, self.client, 'The supplied client should be set.')
    # Assert operation is set
    self.assertIsNotNone(pager._next_request_function, 'The operation function should be set.')
    # Assert partial function parts are as expected
    self.assertEqual(pager._next_request_function.func, operation, 'The partial function should be the operation.')
    self.assertEqual(pager._next_request_function.keywords, opts, 'The partial function kwargs should be the options.')

  def test_partial_options(self):
    operation = self.client.post_view
    static_opts = {'db': 'test', 'limit': 20, 'baz': 'faz'}
    page_opts = {'foo': 'boo', 'bar': 'far'}
    opts = {**static_opts, **page_opts}
    # Use page_opts.keys() to pass the list of names for page options
    pager: Pager = TestPager(self.client, operation, page_opts.keys(), opts)
    # Assert partial function has only static opts
    self.assertEqual(pager._next_request_function.keywords, static_opts, 'The partial function kwargs should be only the static options.')
    # Assert next page options
    self.assertEqual(pager._next_page_opts, page_opts, 'The next page options should match the expected.')

  def test_default_page_size(self):
    operation = self.client.post_view
    opts = {'db': 'test'}
    pager: Pager = TestPager(self.client, operation, [], opts)
    # Assert the default page size
    expected_page_size = 20
    self.assertEqual(pager._page_size, expected_page_size, 'The default page size should be set.')
    self.assertEqual(pager._next_request_function.keywords, opts | {'limit': expected_page_size}, 'The default page size should be present in the options.')

  def test_limit_page_size(self):
    operation = self.client.post_view
    opts = {'db': 'test', 'limit': 42}
    pager: Pager = TestPager(self.client, operation, [], opts)
    # Assert the provided page size
    expected_page_size = 42
    self.assertEqual(pager._page_size, expected_page_size, 'The default page size should be set.')
    self.assertEqual(pager._next_request_function.keywords, opts | {'limit': expected_page_size}, 'The default page size should be present in the options.')

  def test_has_next_initially_true(self):
    operation = self.client.post_view
    opts = {'limit': 1}
    pager: Pager = TestPager(self.client, operation, [], opts)
    # Assert has_next()
    self.assertTrue(pager.has_next(), 'has_next() should initially return True.')

  def test_has_next_true_for_result_equal_to_limit(self):
    page_size = 1
    # Init with mock that returns only a single row
    pager: Pager = TestPager(
        self.client,
        MockPageReponses(1, page_size).get_next_page,
        [],
        {'limit': page_size})
    # Get first page with 1 result
    pager.get_next()
    # Assert has_next()
    self.assertTrue(pager.has_next(), 'has_next() should return True.')

  def test_has_next_false_for_result_less_than_limit(self):
    page_size = 1
    # Init with mock that returns zero rows
    pager: Pager = TestPager(
        self.client,
        MockPageReponses(0, page_size).get_next_page,
        [],
        {'limit': page_size})
    # Get first page with 0 result
    pager.get_next()
    # Assert has_next()
    self.assertFalse(pager.has_next(), 'has_next() should return False.')

  def test_get_next_first_page(self):
    page_size = 25
    # Mock that returns one page of 25 items
    mock = MockPageReponses(page_size, page_size)
    pager: Pager = TestPager(
        self.client,
        mock.get_next_page,
        [],
        {'limit': page_size})
    # Get first page
    actual_page: list[ViewResultRow] = pager.get_next()
    # Assert first page
    self.assertSequenceEqual(actual_page, mock.get_expected_page(1), "The actual page should match the expected page")

  def test_get_next_two_pages(self):
    page_size = 3
    # Mock that returns two pages of 3 items
    mock = MockPageReponses(2*page_size, page_size)
    pager: Pager = TestPager(
        self.client,
        mock.get_next_page,
        [],
        {'limit': page_size})
    # Get first page
    actual_page_1: list[ViewResultRow] = pager.get_next()
    # Assert first page
    self.assertSequenceEqual(actual_page_1, mock.get_expected_page(1), "The actual page should match the expected page")
    # Assert has_next
    self.assertTrue(pager.has_next(), 'has_next() should return True.')
    # Get second page
    actual_page_2: list[ViewResultRow] = pager.get_next()
    # Assert first page
    self.assertSequenceEqual(actual_page_2, mock.get_expected_page(2), "The actual page should match the expected page")
    # Assert has_next, True since page is not smaller than limit
    self.assertTrue(pager.has_next(), 'has_next() should return True.')

  def test_get_next_until_empty(self):
    page_size = 3
    # Mock that returns 3 pages of 3 items
    mock = MockPageReponses(3*page_size, page_size)
    pager: Pager = TestPager(
        self.client,
        mock.get_next_page,
        [],
        {'limit': page_size})
    page_count = 0
    actual_items = []
    while pager.has_next():
      page_count += 1
      page = pager.get_next()
      # Assert each page is the same or smaller than the limit to confirm all results not in one page
      self.assertTrue(len(page) <= page_size, "The actual page size should be the expected page size.")
      actual_items.extend(page)
    self.assertSequenceEqual(actual_items, mock.all_expected_items(), "The results should match all the pages.")
    self.assertEqual(page_count, len(mock.expected_pages), "There should be the correct number of pages.")

  def test_get_next_until_smaller(self):
    page_size = 3
    # Mock that returns 3 pages of 3 items, then 1 more page with 1 item
    mock = MockPageReponses(3*page_size + 1, page_size)
    pager: Pager = TestPager(
        self.client,
        mock.get_next_page,
        [],
        {'limit': page_size})
    page_count = 0
    actual_items = []
    while pager.has_next():
      page_count += 1
      page = pager.get_next()
      # Assert each page is the same or smaller than the limit to confirm all results not in one page
      self.assertTrue(len(page) <= page_size, "The actual page size should be the expected page size.")
      actual_items.extend(page)
    self.assertSequenceEqual(actual_items, mock.all_expected_items(), "The results should match all the pages.")
    self.assertEqual(page_count, len(mock.expected_pages), "There should be the correct number of pages.")

  def test_get_next_exception(self):
    page_size = 2
    # Mock that returns one page of one item
    mock = MockPageReponses(page_size - 1, page_size)
    pager: Pager = TestPager(
        self.client,
        mock.get_next_page,
        [],
        {'limit': page_size})
    # Get first and only page
    actual_page: list[ViewResultRow] = pager.get_next()
    # Assert page
    self.assertSequenceEqual(actual_page, mock.get_expected_page(1), "The actual page should match the expected page")
    # Assert has_next() now False
    self.assertFalse(pager.has_next(), 'has_next() should return False.')
    # Assert StopIteraton on get_next()
    with self.assertRaises(StopIteration):
      pager.get_next()

  def test_get_all(self):
    page_size = 11
    # Mock that returns 6 pages of 11 items, then 1 more page with 5 items
    mock = MockPageReponses(71, page_size)
    pager: Pager = TestPager(
        self.client,
        mock.get_next_page,
        [],
        {'limit': page_size})
    actual_items = pager.get_all()
    self.assertSequenceEqual(actual_items, mock.all_expected_items(), "The results should match all the pages.")

  def test_iter_next_first_page(self):
    page_size = 7
    # Mock that returns two pages of 7 items
    mock = MockPageReponses(2*page_size, page_size)
    pager: Pager = TestPager(
        self.client,
        mock.get_next_page,
        [],
        {'limit': page_size})
    # Get first page
    actual_page: list[ViewResultRow] = next(pager)
    self.assertSequenceEqual(actual_page, mock.get_expected_page(1), "The actual page should match the expected page")

  def test_iter(self):
    page_size = 23
    mock = MockPageReponses(3*page_size-1, page_size)
    pager: Pager = TestPager(
        self.client,
        mock.get_next_page,
        [],
        {'limit': page_size})
    # Check pager is an iterator
    page_number = 0
    for page in pager:
      page_number += 1
      self.assertSequenceEqual(page, mock.get_expected_page(page_number), "The actual page should match the expected page")
    # Asser the correct number of pages
    self.assertEqual(page_number, 3, 'There should have been 3 pages.')

  def test_pages_immutable(self):
    page_size = 1
    mock = MockPageReponses(page_size, page_size)
    pager: Pager = TestPager(
        self.client,
        mock.get_next_page,
        [],
        {'limit': page_size})
    # Get page
    actual_page: list[ViewResultRow] = pager.get_next()
    # Assert immutable tuple type
    self.assertIsInstance(actual_page, tuple)

  def test_set_next_page_options(self):
    page_size = 1
    mock = MockPageReponses(5*page_size, page_size)
    pager: Pager = TestPager(
        self.client,
        mock.get_next_page,
        [],
        {'limit': page_size})
    self.assertIsNone(pager._next_page_opts.get('start_key'), "The start key should intially be None.")
    # Since we use a page size of 1, each next page options key, is the same as the element from the page and the page count
    page_count = 0
    while pager.has_next():
      page = pager.get_next()
      if pager.has_next():
        self.assertEqual(page_count, pager._next_page_opts.get('start_key'), "The key should increment per page.")
      else:
        self.assertEqual(page_count - 1, pager._next_page_opts.get('start_key'), "The options should not be set for the final page.")
      page_count += 1
