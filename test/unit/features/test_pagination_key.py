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
from unittest.mock import Mock, patch
from ibm_cloud_sdk_core import DetailedResponse
from ibmcloudant.cloudant_v1 import ViewResult, ViewResultRow
from ibmcloudant.features.pagination import _KeyPageIterator, PagerType, Pagination
from conftest import MockClientBaseCase, PaginationMockResponse

class KeyTestPageIterator(_KeyPageIterator):
  """
  A test subclass of the _KeyPager under test.
  """
  operation: Callable = None
  boundary_func: Callable = lambda p,l: None

  def __init__(self, client, opts):
    super().__init__(client, KeyTestPageIterator.operation or client.post_view, opts)

  def _result_converter(self) -> Callable[[dict], ViewResult]:
    return lambda d: ViewResult.from_dict(d)

  def _items(self, result: ViewResult) -> tuple[ViewResultRow]:
    return result.rows

  def _get_next_page_options(self, result: ViewResult) -> dict:
    if len(result.rows ) == 0:
      self.assertFail("Test failure: tried to setNextPageOptions on empty page.")
    else:
      return {'start_key': result.rows[-1].key}
  
  def check_boundary(self, penultimate_item, last_item):
    return KeyTestPageIterator.boundary_func(penultimate_item, last_item)

class KeyPaginationMockResponses(PaginationMockResponse):
  """
  Test class for mocking page responses.
  """
  def __init__(self, total_items: int, page_size: int):
    super().__init__(total_items, page_size, PagerType.POST_VIEW)

class TestKeyPageIterator(MockClientBaseCase):

  # Test page size default (+1)
  def test_default_page_size(self):
    page_iterator: Iterator[tuple[ViewResultRow]] = KeyTestPageIterator(self.client, {})
    # Assert the limit default as page size
    self.assertEqual(page_iterator._page_size, 201, 'The page size should be one more than the default limit.')

  # Test page size limit (+1)
  def test_limit_page_size(self):
    page_iterator: Iterator[tuple[ViewResultRow]] = KeyTestPageIterator(self.client, {'limit': 42})
    # Assert the limit provided as page size
    self.assertEqual(page_iterator._page_size, 43, 'The page size should be one more than the default limit.')

  # Test all items on page when no more pages
  def test_get_next_page_less_than_limit(self):
    page_size = 21
    mock = KeyPaginationMockResponses(page_size, page_size)
    with patch('test_pagination_key.KeyTestPageIterator.operation', mock.get_next_page):
      page_iterator = KeyTestPageIterator(self.client, {'limit': page_size})
      # Get and assert first page
      actual_page = next(page_iterator)
      self.assertSequenceEqual(actual_page, mock.get_expected_page(1), 'The actual page should match the expected page')
      # Assert page size
      self.assertEqual(len(actual_page), page_size, 'The actual page size should match the expected page size.')
      # Assert has_next False because n+1 limit is 1 more than user page size
      self.assertFalse(page_iterator._has_next, '_has_next should return False.')

  # Test correct items on page when n+1
  def test_get_next_page_equal_to_limit(self):
    page_size = 14
    mock = KeyPaginationMockResponses(page_size+1, page_size)
    with patch('test_pagination_key.KeyTestPageIterator.operation', mock.get_next_page):
      page_iterator = KeyTestPageIterator(self.client, {'limit': page_size})
      # Get and assert first page
      actual_page = next(page_iterator)
      self.assertSequenceEqual(actual_page, mock.get_expected_page(1), 'The actual page should match the expected page.')
      # Assert page size
      self.assertEqual(len(actual_page), page_size, 'The actual page size should match the expected page size.')
      # Assert has_next True
      self.assertTrue(page_iterator._has_next, '_has_next should return True.')
      # Get and assert second page
      second_page = next(page_iterator)
      self.assertEqual(len(second_page), 1 , 'The second page should have one item.')
      # Note row keys are zero indexed so n+1 element that is first item on second page matches page size
      self.assertEqual(second_page[0].key, page_size, 'The first item key on the second page should match the page size number.')
      self.assertSequenceEqual(second_page, mock.get_expected_page(2), "The actual page should match the expected page")
      self.assertFalse(page_iterator._has_next, '_has_next should return False.')

  # Test correct items on page when n+more  
  def test_get_next_page_greater_than_limit(self):
    page_size = 7
    mock = KeyPaginationMockResponses(page_size+2, page_size)
    with patch('test_pagination_key.KeyTestPageIterator.operation', mock.get_next_page):
      page_iterator = KeyTestPageIterator(self.client, {'limit': page_size})
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
      self.assertEqual(second_page[0].key, page_size, 'The first item key on the second page should match the page size number.')
      self.assertSequenceEqual(second_page, mock.get_expected_page(2), "The actual page should match the expected page")
      self.assertFalse(page_iterator._has_next, '_has_next should return False.')

  # Test getting all items
  def test_get_all(self):
    page_size = 3
    mock = KeyPaginationMockResponses(page_size*12, page_size)
    pagination = Pagination(self.client, KeyTestPageIterator, {'limit': page_size})
    with patch('test_pagination_key.KeyTestPageIterator.operation', mock.get_next_page):
      pager = pagination.pager()
      # Get and assert all items
      self.assertSequenceEqual(pager.get_all(), mock.all_expected_items(), 'The results should match all the pages.')

  def test_no_boundary_check_by_default(self):
      mock_rows = [
          {'id': '1', 'key': 1, 'value': 1},
          {'id': '1', 'key': 1, 'value': 1}
      ]
      expected_rows = ViewResult.from_dict({'rows': mock_rows}).rows
      mockmock = Mock(return_value=DetailedResponse(response={'rows': mock_rows}))
      with patch('test_pagination_key.KeyTestPageIterator.operation', mockmock):
        page_iterator = KeyTestPageIterator(self.client, {'limit': 1})
        # Get and assert page
        self.assertSequenceEqual(next(page_iterator), (expected_rows[0],))

  def test_boundary_failure_throws_on_get_next(self):
      mock_rows = [
          {'id': '1', 'key': 1, 'value': 1},
          {'id': '1', 'key': 1, 'value': 1}
      ]
      expected_rows = ViewResult.from_dict({'rows': mock_rows}).rows
      mockmock = Mock(return_value=DetailedResponse(response={'rows': mock_rows}))
      with patch('test_pagination_key.KeyTestPageIterator.operation', mockmock):
        page_iterator = KeyTestPageIterator(self.client, {'limit': 1})
      with patch(
        'test_pagination_key.KeyTestPageIterator.boundary_func',
        lambda p,l: 'test error' if p.id == l.id and p.key == l.key else None):
        # Get and assert page
        self.assertSequenceEqual(next(page_iterator), (expected_rows[0],))
        # Assert has_next True
        self.assertTrue(page_iterator._has_next, '_has_next should return True.')
        with self.assertRaises(Exception):
          next(page_iterator)

  def test_no_boundary_check_when_no_items_left(self):
      mock_rows = [
          {'id': '1', 'key': 1, 'value': 1}
      ]
      expected_rows = ViewResult.from_dict({'rows': mock_rows}).rows
      mockmock = Mock(return_value=DetailedResponse(response={'rows': mock_rows}))
      with patch('test_pagination_key.KeyTestPageIterator.operation', mockmock):
        page_iterator = KeyTestPageIterator(self.client, {'limit': 1})
      with patch(
        'test_pagination_key.KeyTestPageIterator.boundary_func',
        Exception('Check boundary should not be called.')):
        # Get and assert page if boundary is checked, will raise exception
        self.assertSequenceEqual(next(page_iterator), (expected_rows[0],))
        # Assert has_next False
        self.assertFalse(page_iterator._has_next, '_has_next should return True.')
