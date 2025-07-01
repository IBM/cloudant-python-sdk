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

from collections.abc import Callable, Iterator
from unittest.mock import patch
from ibmcloudant.cloudant_v1 import SearchResult, SearchResultRow
from ibmcloudant.features.pagination import _BookmarkPageIterator, PagerType, Pagination
from conftest import MockClientBaseCase, PaginationMockResponse

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

class BookmarkPaginationMockResponses(PaginationMockResponse):
  """
  Test class for mocking page responses.
  """
  def __init__(self, total_items: int, page_size: int):
    super().__init__(total_items, page_size, PagerType.POST_SEARCH)

class TestBookmarkPageIterator(MockClientBaseCase):

  # Test page size default
  def test_default_page_size(self):
    page_iterator: Iterator[tuple[SearchResultRow]] = BookmarkTestPageIterator(self.client, {})
    # Assert the limit default as page size
    self.assertEqual(page_iterator._page_size, 200, 'The page size should be one more than the default limit.')

  # Test page size limit
  def test_limit_page_size(self):
    page_iterator: Iterator[tuple[SearchResultRow]] = BookmarkTestPageIterator(self.client, {'limit': 42})
    # Assert the limit provided as page size
    self.assertEqual(page_iterator._page_size, 42, 'The page size should be one more than the default limit.')

  # Test all items on page when no more pages
  def test_get_next_page_less_than_limit(self):
    page_size = 21
    mock = BookmarkPaginationMockResponses(page_size - 1, page_size)
    with patch('test_pagination_bookmark.BookmarkTestPageIterator.operation', mock.get_next_page):
      page_iterator = BookmarkTestPageIterator(self.client, {'limit': page_size})
      # Get and assert first page
      actual_page = next(page_iterator)
      self.assertSequenceEqual(actual_page, mock.get_expected_page(1), 'The actual page should match the expected page')
      # Assert page size
      self.assertEqual(len(actual_page), page_size - 1, 'The actual page size should match the expected page size.')
      # Assert has_next False because n+1 limit is 1 more than user page size
      self.assertFalse(page_iterator._has_next, '_has_next should return False.')

  # Test correct items on page when limit
  def test_get_next_page_equal_to_limit(self):
    page_size = 14
    mock = BookmarkPaginationMockResponses(page_size, page_size)
    with patch('test_pagination_bookmark.BookmarkTestPageIterator.operation', mock.get_next_page):
      page_iterator = BookmarkTestPageIterator(self.client, {'limit': page_size})
      # Get and assert first page
      actual_page = next(page_iterator)
      self.assertSequenceEqual(actual_page, mock.get_expected_page(1), 'The actual page should match the expected page.')
      # Assert page size
      self.assertEqual(len(actual_page), page_size, 'The actual page size should match the expected page size.')
      # Assert has_next True
      self.assertTrue(page_iterator._has_next, '_has_next should return True.')
      # Assert bookmark
      self.assertEqual(page_iterator._next_page_opts['bookmark'], f'testdoc{page_size - 1}', 'The bookmark should be one less than the page size.')
      # Get and assert second page
      second_page = next(page_iterator)
      # Note row keys are zero indexed so page size - 1
      self.assertEqual(len(second_page), 0, "The second page should be empty.")
      self.assertFalse(page_iterator._has_next, '_has_next should return False.')

  # Test correct items on page when n+more  
  def test_get_next_page_greater_than_limit(self):
    page_size = 7
    mock = BookmarkPaginationMockResponses(page_size+2, page_size)
    with patch('test_pagination_bookmark.BookmarkTestPageIterator.operation', mock.get_next_page):
      page_iterator = BookmarkTestPageIterator(self.client, {'limit': page_size})
      # Get and assert first page
      actual_page = next(page_iterator)
      self.assertSequenceEqual(actual_page, mock.get_expected_page(1), 'The actual page should match the expected page.')
      # Assert page size
      self.assertEqual(len(actual_page), page_size, 'The actual page size should match the expected page size.')
      # Assert has_next True
      self.assertTrue(page_iterator._has_next, '_has_next should return True.')
      # Get and assert second page
      second_page = next(page_iterator)
      self.assertEqual(len(second_page), 2 , 'The second page should have two items.')
      # Note row keys are zero indexed so n+1 element that is first item on second page matches page size
      self.assertEqual(second_page[0].id, f'testdoc{page_size}', 'The first item key on the second page should match the page size number.')
      self.assertSequenceEqual(second_page, mock.get_expected_page(2), "The actual page should match the expected page")
      self.assertFalse(page_iterator._has_next, '_has_next should return False.')

  # Test getting all items
  def test_get_all(self):
    page_size = 3
    mock = BookmarkPaginationMockResponses(page_size*12, page_size)
    pagination = Pagination(self.client, BookmarkTestPageIterator, {'limit': page_size})
    with patch('test_pagination_bookmark.BookmarkTestPageIterator.operation', mock.get_next_page):
      pager = pagination.pager()
      # Get and assert all items
      self.assertSequenceEqual(pager.get_all(), mock.all_expected_items(), 'The results should match all the pages.')
