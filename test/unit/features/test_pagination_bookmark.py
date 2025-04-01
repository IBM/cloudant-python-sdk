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
from unittest.mock import Mock, patch
from ibm_cloud_sdk_core import DetailedResponse
from ibmcloudant.cloudant_v1 import SearchResult, SearchResultRow
from ibmcloudant.features.pagination import _BookmarkPageIterator, Pager
from conftest import MockClientBaseCase

class BookmarkTestPageIterator(_BookmarkPageIterator):
  """
  A test subclass of the _BookmarkPager under test.
  """
  operation: Callable = None
  boundary_func: Callable = lambda p,l: None

  def __init__(self, client, opts):
    super().__init__(client, BookmarkTestPageIterator.operation or client.post_view, opts)

  def _result_converter(self) -> Callable[[dict], SearchResult]:
    return lambda d: SearchResult.from_dict(d)

  def _items(self, result: SearchResult) -> tuple[SearchResultRow]:
    return result.rows

class MockPageResponses:
  """
  Test class for mocking page responses.
  """
  def __init__(self, total_items: int, page_size: int):
    self.total_items: int = total_items
    self.page_size: int = page_size
    self.pages = self.generator()
    self.expected_pages: list[list[SearchResultRow]] = []

  def generator(self):
    for page in batched(range(0, self.total_items), self.page_size):
      rows = [{'id':str(i), 'fields': {'value': i}} for i in page]
      yield DetailedResponse(response={'total_rows': self.total_items, 'bookmark': rows[-1]['id'], 'rows': rows})
    yield DetailedResponse(response={'total_rows': self.total_items, 'bookmark': 'last', 'rows': []})

  def get_next_page(self, **kwargs):
    # ignore kwargs
    # get next page
    page = next(self.pages)
    # convert to an expected page
    self.expected_pages.append(SearchResult.from_dict(page.get_result()).rows)
    return page

  def get_expected_page(self, page: int) -> list[SearchResultRow]:
    return self.expected_pages[page - 1]

  def all_expected_items(self) -> list[SearchResultRow]:
    all_items: list[SearchResultRow] = []
    for page in self.expected_pages:
      all_items.extend(page)
    return all_items

class TestBookmarkPageIterator(MockClientBaseCase):

  # Test page size default
  def test_default_page_size(self):
    pager: Pager = BookmarkTestPageIterator(self.client, {})
    # Assert the limit default as page size
    self.assertEqual(pager._page_size, 200, 'The page size should be one more than the default limit.')

  # Test page size limit
  def test_limit_page_size(self):
    pager: Pager = BookmarkTestPageIterator(self.client, {'limit': 42})
    # Assert the limit provided as page size
    self.assertEqual(pager._page_size, 42, 'The page size should be one more than the default limit.')

  # Test all items on page when no more pages
  def test_get_next_page_less_than_limit(self):
    page_size = 21
    mock = MockPageResponses(page_size - 1, page_size)
    with patch('test_pagination_bookmark.BookmarkTestPager.operation', mock.get_next_page):
      pager = BookmarkTestPageIterator(self.client, {'limit': page_size})
      # Get and assert first page
      actual_page = pager.get_next()
      self.assertSequenceEqual(actual_page, mock.get_expected_page(1), 'The actual page should match the expected page')
      # Assert page size
      self.assertEqual(len(actual_page), page_size - 1, 'The actual page size should match the expected page size.')
      # Assert has_next False because n+1 limit is 1 more than user page size
      self.assertFalse(pager.has_next(), 'has_next() should return False.')

  # Test correct items on page when limit
  def test_get_next_page_equal_to_limit(self):
    page_size = 14
    mock = MockPageResponses(page_size, page_size)
    with patch('test_pagination_bookmark.BookmarkTestPager.operation', mock.get_next_page):
      pager = BookmarkTestPageIterator(self.client, {'limit': page_size})
      # Get and assert first page
      actual_page = pager.get_next()
      self.assertSequenceEqual(actual_page, mock.get_expected_page(1), 'The actual page should match the expected page.')
      # Assert page size
      self.assertEqual(len(actual_page), page_size, 'The actual page size should match the expected page size.')
      # Assert has_next True
      self.assertTrue(pager.has_next(), 'has_next() should return True.')
      # Assert bookmark
      self.assertEqual(pager._next_page_opts['bookmark'], str(page_size - 1), 'The bookmark should be one less than the page size.')
      # Get and assert second page
      second_page = pager.get_next()
      # Note row keys are zero indexed so page size - 1
      self.assertEqual(len(second_page), 0, "The second page should be empty.")
      self.assertFalse(pager.has_next(), 'has_next() should return False.')

  # Test correct items on page when n+more  
  def test_get_next_page_greater_than_limit(self):
    page_size = 7
    mock = MockPageResponses(page_size+2, page_size)
    with patch('test_pagination_bookmark.BookmarkTestPager.operation', mock.get_next_page):
      pager = BookmarkTestPageIterator(self.client, {'limit': page_size})
      # Get and assert first page
      actual_page = pager.get_next()
      self.assertSequenceEqual(actual_page, mock.get_expected_page(1), 'The actual page should match the expected page.')
      # Assert page size
      self.assertEqual(len(actual_page), page_size, 'The actual page size should match the expected page size.')
      # Assert has_next True
      self.assertTrue(pager.has_next(), 'has_next() should return True.')
      # Get and assert second page
      second_page = pager.get_next()
      self.assertEqual(len(second_page), 2 , 'The second page should have two items.')
      # Note row keys are zero indexed so n+1 element that is first item on second page matches page size
      self.assertEqual(second_page[0].id, str(page_size), 'The first item key on the second page should match the page size number.')
      self.assertSequenceEqual(second_page, mock.get_expected_page(2), "The actual page should match the expected page")
      self.assertFalse(pager.has_next(), 'has_next() should return False.')

  # Test getting all items
  def test_get_all(self):
    page_size = 3
    mock = MockPageResponses(page_size*12, page_size)
    with patch('test_pagination_bookmark.BookmarkTestPager.operation', mock.get_next_page):
      pager = BookmarkTestPageIterator(self.client, {'limit': page_size})
      # Get and assert all items
      self.assertSequenceEqual(pager.get_all(), mock.all_expected_items(), 'The results should match all the pages.')
