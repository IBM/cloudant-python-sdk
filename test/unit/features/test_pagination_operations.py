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

from unittest.mock import patch
from conftest import MockClientBaseCase, PaginationMockSupport, PaginationMockResponse
from ibmcloudant.features.pagination import Pager, PagerType, Pagination

class TestPaginationOperations(MockClientBaseCase):

  test_page_size = 10
  # tuples of test parameters
  # total items, page size
  page_sets = (
    (0, test_page_size),
    (1, test_page_size),
    (test_page_size - 1, test_page_size),
    (test_page_size, test_page_size),
    (test_page_size + 1, test_page_size),
    (3 * test_page_size, test_page_size),
    (3 * test_page_size + 1, test_page_size),
    (4 * test_page_size - 1, test_page_size),
  )

  def get_expected_pages(self, total: int, page_size: int, pager_type: PagerType) -> int:
    full_pages = total // page_size
    partial_pages = 0 if (total % page_size == 0) else 1
    expected_pages = full_pages + partial_pages
    # Need at least 1 empty page to know there are no more results
    # if not ending on a partial page, except if the first page or
    # using n+1 paging (because an exact user page is a partial real page).
    if partial_pages == 0 and (expected_pages == 0 or pager_type not in PaginationMockSupport.key_pagers):
      expected_pages += 1; # Will get at least 1 empty page
    return expected_pages

  def test_pager(self):
    for pager_type in PagerType:
      with self.subTest(pager_type):
        for page_set in self.page_sets:
          with self.subTest(page_set):
            actual_items: set = set()
            actual_item_count: int = 0
            actual_page_count: int = 0
            expected_items_count: int = page_set[0]
            page_size: int = page_set[1]
            expected_page_count: int = self.get_expected_pages(expected_items_count, page_size, pager_type)
            with patch(PaginationMockSupport.operation_map[pager_type], PaginationMockResponse(expected_items_count, page_size, pager_type).get_next_page):
              pager: Pager = Pagination.new_pagination(self.client, pager_type, limit=page_size).pager()
              while(pager.has_next()):
                page = pager.get_next()
                actual_page_count += 1
                actual_item_count += len(page)
                for row in page:
                  if pager_type in (PagerType.POST_FIND, PagerType.POST_PARTITION_FIND):
                    id = row._id
                  else:
                    id = row.id
                  actual_items.add(id)
              self.assertEqual(actual_page_count, expected_page_count, 'There should be the expected number of pages.')
              self.assertEqual(actual_item_count, expected_items_count, 'There should be the expected number of items.')
              self.assertEqual(len(actual_items), expected_items_count, 'The items should be unique.')

  def test_pages(self):
    for pager_type in PagerType:
      with self.subTest(pager_type):
        for page_set in self.page_sets:
          with self.subTest(page_set):
            actual_items: set = set()
            actual_item_count: int = 0
            actual_page_count: int = 0
            expected_items_count: int = page_set[0]
            page_size: int = page_set[1]
            expected_page_count: int = self.get_expected_pages(expected_items_count, page_size, pager_type)
            with patch(PaginationMockSupport.operation_map[pager_type], PaginationMockResponse(expected_items_count, page_size, pager_type).get_next_page):
              for page in Pagination.new_pagination(self.client, pager_type, limit=page_size).pages():
                actual_page_count += 1
                actual_item_count += len(page)
                for row in page:
                  if pager_type in (PagerType.POST_FIND, PagerType.POST_PARTITION_FIND):
                    id = row._id
                  else:
                    id = row.id
                  actual_items.add(id)
              self.assertEqual(actual_page_count, expected_page_count, 'There should be the expected number of pages.')
              self.assertEqual(actual_item_count, expected_items_count, 'There should be the expected number of items.')
              self.assertEqual(len(actual_items), expected_items_count, 'The items should be unique.')

  def test_rows(self):
    for pager_type in PagerType:
      with self.subTest(pager_type):
        for page_set in self.page_sets:
          with self.subTest(page_set):
            actual_items: set = set()
            actual_item_count: int = 0
            expected_items_count: int = page_set[0]
            page_size: int = page_set[1]
            with patch(PaginationMockSupport.operation_map[pager_type], PaginationMockResponse(expected_items_count, page_size, pager_type).get_next_page):
              for row in Pagination.new_pagination(self.client, pager_type, limit=page_size).rows():
                actual_item_count += 1
                if pager_type in (PagerType.POST_FIND, PagerType.POST_PARTITION_FIND):
                  id = row._id
                else:
                  id = row.id
                actual_items.add(id)
              self.assertEqual(actual_item_count, expected_items_count, 'There should be the expected number of items.')
              self.assertEqual(len(actual_items), expected_items_count, 'The items should be unique.')
