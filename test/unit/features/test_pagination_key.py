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
from ibmcloudant.cloudant_v1 import ViewResult, ViewResultRow
from ibmcloudant.features.pagination import _KeyPager, Pager
from conftest import MockClientBaseCase

class KeyTestPager(_KeyPager):
  """
  A test subclass of the _KeyPager under test.
  """
  operation: Callable = None
  boundary_func: Callable = lambda p,l: None

  def __init__(self, client, opts):
    super().__init__(client, KeyTestPager.operation or client.post_view, opts)

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
    return KeyTestPager.boundary_func(penultimate_item, last_item)

class MockPageResponses:
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
      # Add an n+1 row for key based paging if more pages
      if (n_plus_one := page[-1] + 1) < self.total_items:
        rows.append({'id':str(n_plus_one), 'key':n_plus_one, 'value':n_plus_one})
      yield DetailedResponse(response={'rows': rows})
    yield DetailedResponse(response={'rows': []})

  def get_next_page(self, **kwargs):
    # ignore kwargs
    # get next page
    page = next(self.pages)
    # convert to an expected page, removing the n+1 row if needed
    result = ViewResult.from_dict(page.get_result())
    if len(result.rows) > self.page_size:
      self.expected_pages.append(result.rows[:-1])
    else:
      self.expected_pages.append(result.rows)
    return page

  def get_expected_page(self, page: int) -> list[ViewResultRow]:
    return self.expected_pages[page - 1]
  
  def all_expected_items(self) -> list[ViewResultRow]:
    all_items: list[ViewResultRow] = []
    for page in self.expected_pages:
      all_items.extend(page)
    return all_items

class TestKeyPager(MockClientBaseCase):

  # Test page size default (+1)
  def test_default_page_size(self):
    pager: Pager = KeyTestPager(self.client, {})
    # Assert the limit default as page size
    self.assertEqual(pager._page_size, 201, 'The page size should be one more than the default limit.')

  # Test page size limit (+1)
  def test_limit_page_size(self):
    pager: Pager = KeyTestPager(self.client, {'limit': 42})
    # Assert the limit provided as page size
    self.assertEqual(pager._page_size, 43, 'The page size should be one more than the default limit.')

  # Test all items on page when no more pages
  def test_get_next_page_less_than_limit(self):
    page_size = 21
    mock = MockPageResponses(page_size, page_size)
    with patch('test_pagination_key.KeyTestPager.operation', mock.get_next_page):
      pager = KeyTestPager(self.client, {'limit': page_size})
      # Get and assert first page
      actual_page = pager.get_next()
      self.assertSequenceEqual(actual_page, mock.get_expected_page(1), 'The actual page should match the expected page')
      # Assert page size
      self.assertEqual(len(actual_page), page_size, 'The actual page size should match the expected page size.')
      # Assert has_next False because n+1 limit is 1 more than user page size
      self.assertFalse(pager.has_next(), 'has_next() should return False.')

  # Test correct items on page when n+1
  def test_get_next_page_equal_to_limit(self):
    page_size = 14
    mock = MockPageResponses(page_size+1, page_size)
    with patch('test_pagination_key.KeyTestPager.operation', mock.get_next_page):
      pager = KeyTestPager(self.client, {'limit': page_size})
      # Get and assert first page
      actual_page = pager.get_next()
      self.assertSequenceEqual(actual_page, mock.get_expected_page(1), 'The actual page should match the expected page.')
      # Assert page size
      self.assertEqual(len(actual_page), page_size, 'The actual page size should match the expected page size.')
      # Assert has_next True
      self.assertTrue(pager.has_next(), 'has_next() should return True.')
      # Get and assert second page
      second_page = pager.get_next()
      self.assertEqual(len(second_page), 1 , 'The second page should have one item.')
      # Note row keys are zero indexed so n+1 element that is first item on second page matches page size
      self.assertEqual(second_page[0].key, page_size, 'The first item key on the second page should match the page size number.')
      self.assertSequenceEqual(second_page, mock.get_expected_page(2), "The actual page should match the expected page")
      self.assertFalse(pager.has_next(), 'has_next() should return False.')

  # Test correct items on page when n+more  
  def test_get_next_page_greater_than_limit(self):
    page_size = 7
    mock = MockPageResponses(page_size+2, page_size)
    with patch('test_pagination_key.KeyTestPager.operation', mock.get_next_page):
      pager = KeyTestPager(self.client, {'limit': page_size})
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
      self.assertEqual(second_page[0].key, page_size, 'The first item key on the second page should match the page size number.')
      self.assertSequenceEqual(second_page, mock.get_expected_page(2), "The actual page should match the expected page")
      self.assertFalse(pager.has_next(), 'has_next() should return False.')

  # Test getting all items
  def test_get_all(self):
    page_size = 3
    mock = MockPageResponses(page_size*12, page_size)
    with patch('test_pagination_key.KeyTestPager.operation', mock.get_next_page):
      pager = KeyTestPager(self.client, {'limit': page_size})
      # Get and assert all items
      self.assertSequenceEqual(pager.get_all(), mock.all_expected_items(), 'The results should match all the pages.')

  def test_no_boundary_check_by_default(self):
      mock_rows = [
          {'id': '1', 'key': 1, 'value': 1},
          {'id': '1', 'key': 1, 'value': 1}
      ]
      expected_rows = ViewResult.from_dict({'rows': mock_rows}).rows
      mockmock = Mock(return_value=DetailedResponse(response={'rows': mock_rows}))
      with patch('test_pagination_key.KeyTestPager.operation', mockmock):
        pager = KeyTestPager(self.client, {'limit': 1})
        # Get and assert page
        self.assertSequenceEqual(pager.get_next(), (expected_rows[0],))

  def test_boundary_failure_throws_on_get_next(self):
      mock_rows = [
          {'id': '1', 'key': 1, 'value': 1},
          {'id': '1', 'key': 1, 'value': 1}
      ]
      expected_rows = ViewResult.from_dict({'rows': mock_rows}).rows
      mockmock = Mock(return_value=DetailedResponse(response={'rows': mock_rows}))
      with patch('test_pagination_key.KeyTestPager.operation', mockmock):
        pager = KeyTestPager(self.client, {'limit': 1})
      with patch(
        'test_pagination_key.KeyTestPager.boundary_func',
        lambda p,l: 'test error' if p.id == l.id and p.key == l.key else None):
        # Get and assert page
        self.assertSequenceEqual(pager.get_next(), (expected_rows[0],))
        # Assert has_next True
        self.assertTrue(pager.has_next(), 'has_next() should return True.')
        with self.assertRaises(Exception):
          pager.get_next()

  def test_no_boundary_check_when_no_items_left(self):
      mock_rows = [
          {'id': '1', 'key': 1, 'value': 1}
      ]
      expected_rows = ViewResult.from_dict({'rows': mock_rows}).rows
      mockmock = Mock(return_value=DetailedResponse(response={'rows': mock_rows}))
      with patch('test_pagination_key.KeyTestPager.operation', mockmock):
        pager = KeyTestPager(self.client, {'limit': 1})
      with patch(
        'test_pagination_key.KeyTestPager.boundary_func',
        Exception('Check boundary should not be called.')):
        # Get and assert page if boundary is checked, will raise exception
        self.assertSequenceEqual(pager.get_next(), (expected_rows[0],))
        # Assert has_next False
        self.assertFalse(pager.has_next(), 'has_next() should return True.')
