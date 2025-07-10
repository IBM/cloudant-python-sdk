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

from unittest import TestCase
from ibmcloudant.features.pagination import _DOCS_KEY_ERROR, _MIN_LIMIT, _MAX_LIMIT, _VIEW_KEY_ERROR, PagerType, Pagination

class TestPaginationOptionValidation(TestCase):

  all_doc_paginations = (PagerType.POST_ALL_DOCS, PagerType.POST_PARTITION_ALL_DOCS, PagerType.POST_DESIGN_DOCS)
  find_paginations = (PagerType.POST_PARTITION_FIND, PagerType.POST_FIND)
  search_paginations = (PagerType.POST_SEARCH, PagerType.POST_PARTITION_SEARCH)
  view_paginations = (PagerType.POST_PARTITION_VIEW, PagerType.POST_VIEW)
  view_like_paginations = (*all_doc_paginations, *view_paginations)
  all_paginations = (*find_paginations, *search_paginations, *view_like_paginations)

  def test_valid_limits(self):
      test_limits = (_MIN_LIMIT, _MAX_LIMIT - 1, _MAX_LIMIT, None)
      for limit in test_limits:
        for pager_type in self.all_paginations:
          with self.subTest(pager_type):
            try:
              Pagination.new_pagination(None, pager_type, limit=limit)
            except ValueError:
              self.fail('There should be no ValueError for valid limits.')

  def test_invalid_limits(self):
      test_limits = (_MIN_LIMIT - 1, _MAX_LIMIT + 1)
      for limit in test_limits:
        if (limit == _MIN_LIMIT -1):
          msg_regex = f'The provided limit {limit} is lower than the minimum page size value of 1.'
        elif (limit == _MAX_LIMIT + 1):
          msg_regex= f'The provided limit {limit} exceeds the maximum page size value of 200.'
        for pager_type in self.all_paginations:
          with self.subTest(pager_type):
            with self.assertRaisesRegex(ValueError, msg_regex):
              Pagination.new_pagination(None, pager_type, limit=limit)

  def test_keys_value_error_for_view_like(self):
      for pager_type in self.view_like_paginations:
        with self.subTest(pager_type):
          with self.assertRaisesRegex(ValueError, 'The option \'keys\' is invalid when using pagination.'):
            Pagination.new_pagination(None, pager_type, keys=['a','b','c'])

  def test_facet_value_errors_for_search(self):
    for invalid_opt in ('counts', 'group_field', 'group_limit', 'group_sort', 'ranges',):
      with self.subTest(invalid_opt):
        with self.assertRaisesRegex(ValueError, f'The option \'{invalid_opt}\' is invalid when using pagination.'):
          Pagination.new_pagination(None, PagerType.POST_SEARCH, **{invalid_opt: 'test value'})

  def test_key_value_error_for_docs(self):
      for pager_type in self.all_doc_paginations:
        with self.subTest(pager_type):
          with self.assertRaisesRegex(ValueError, f'The option \'key\' is invalid when using pagination. {_DOCS_KEY_ERROR}'):
            Pagination.new_pagination(None, pager_type, key='a')

  def test_key_value_error_for_views(self):
      for pager_type in self.view_paginations:
        with self.subTest(pager_type):
          with self.assertRaisesRegex(ValueError, f'The option \'key\' is invalid when using pagination. {_VIEW_KEY_ERROR}'):
            Pagination.new_pagination(None, pager_type, key={})
