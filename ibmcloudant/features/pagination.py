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
"""
 Feature for paginating requests.
 
 Import :class:`~ibmcloudant.Pager` and :class:`~ibmcloudant.PagerType`
 from :mod:`ibmcloudant`.
 Use :meth:`Pager.new_pager` to create a :class:`Pager` for different
 :class:`PagerType` operations.
"""
from abc import abstractmethod
from collections.abc import Callable
from enum import auto, Enum
from functools import partial
from typing import Generic, Protocol, TypeVar

from ibm_cloud_sdk_core import DetailedResponse
from ibmcloudant.cloudant_v1 import CloudantV1,\
  AllDocsResult, DocsResultRow, Document, FindResult, SearchResult, SearchResultRow, ViewResult, ViewResultRow

# Type variable for the result
R = TypeVar('R', AllDocsResult, FindResult, SearchResult, ViewResult)
# Type variable for the items
I = TypeVar('I', DocsResultRow, Document, SearchResultRow, ViewResultRow)
# Type variable for the key in key based paging
K = TypeVar('K')

class PagerType(Enum):
  """
  Enumeration of the available Pager types
  """
  POST_ALL_DOCS = auto()
  POST_DESIGN_DOCS = auto()
  POST_FIND = auto()
  POST_PARTITION_ALL_DOCS = auto()
  POST_PARTITION_FIND = auto()
  POST_PARTITION_SEARCH = auto()
  POST_PARTITION_VIEW = auto()
  POST_SEARCH = auto()
  POST_VIEW = auto()

class Pager(Protocol[R, I]):
  """
  Protocol for pagination of Cloudant operations.
  Use Pager.new_pager to create a new pager for one of
  the operation types in PagerType.
  """

  def has_next(self) -> bool:
    """
    returns True if there may be another page of results, False otherwise
    """
    pass

  @abstractmethod
  def get_next(self) -> list[I]:
    """
    returns the next page of results
    """
    pass

  def get_all(self) -> list[I]:
    """
    returns all the pages of results in single list
    """
    pass

  @classmethod
  def new_pager(cls, client:CloudantV1, type: PagerType, **kwargs,):
    """
    Create a new Pager.
    client: CloudantV1 - the Cloudant service client
    type: PagerType - the operation type to paginate
    kwargs: dict - the options for the operation
    """
    pass

class _BasePager(Pager):

  def __init__(self,
               client: CloudantV1,
               operation: Callable[..., DetailedResponse],
               page_opts: list[str],
               opts:dict):
    self._client = client
    # TODO split the opts into fixed and page parts based on page_opts
    self._next_page_opts = {}
    fixed_opts = {}
    # Partial method with the fixed ops
    self._next_request_function = partial(operation, **fixed_opts)

  def _next_request(self) -> R:
    response: DetailedResponse = self._next_request_function(**self._next_page_opts)
    result: dict = response.get_result()
    return self._result_converter()(result)

  @abstractmethod
  def _result_converter(self) -> Callable[[dict], R]:
    ...

  @abstractmethod
  def _items(self, result: R) -> list[I]:
    ...

  @abstractmethod
  def _get_next_page_options(self, result: R) -> dict:
    ...

class _KeyPager(_BasePager, Generic[K]):

  def __init__(self, client: CloudantV1, operation: Callable[..., DetailedResponse], opts: dict):
    super().__init__(client, operation, ['start_key', 'start_key_doc_id'], opts)

  def get_next(self) -> list[I]:
    pass

  def _get_next_page_options(self, result: R):
    pass

  def _items(self, result: R) -> list[I]:
    return result.rows

  def _get_key(self, item: I) -> K:
    return item.key

  def _get_id(self, item: I) -> str:
    return item.id

  def _set_id(self, opts: dict, next_id: str):
    opts['start_key_doc_id'] = next_id

class _BookmarkPager(_BasePager):

  def __init__(self, client: CloudantV1, operation: Callable[..., DetailedResponse], opts: dict):
    super().__init__(client, operation, ['bookmark'], opts)

  def _get_next_page_options(self, result: R) -> dict:
    pass

  def _get_bookmark(self, result: R):
    return result.bookmark

  def _set_bookmark(self, opts:dict, bookmark:str) -> str:
    opts['bookmark'] = bookmark

class _AllDocsBasePager(_KeyPager[str]):

  def _result_converter(self):
    return AllDocsResult.from_dict

  def _set_id(self, opts: dict, next_id: str):
    # no-op for AllDocs paging
    pass

class _AllDocsPager(_AllDocsBasePager):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_all_docs, opts)

class _AllDocsPartitionPager(_AllDocsBasePager):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_partition_all_docs, opts)

class _DesignDocsPager(_AllDocsBasePager):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_design_docs, opts)

class _FindBasePager(_BookmarkPager):

  def _items(self, result: FindResult):
    return result.docs

  def _result_converter(self):
    return FindResult.from_dict

class _FindPager(_FindBasePager):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_find, opts)

class _FindPartitionPager(_FindBasePager):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_partition_find, opts)

class _SearchBasePager(_BookmarkPager):

  def _items(self, result: SearchResult):
    return result.rows

  def _result_converter(self):
    return SearchResult.from_dict

class _SearchPager(_SearchBasePager):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_search, opts)

class _SearchPartitionPager(_SearchBasePager):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_partition_search, opts)

class _ViewBasePager(_KeyPager[any]):

  def _result_converter(self):
    return AllDocsResult.from_dict

class _ViewPager(_ViewBasePager):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_view, opts)

class _ViewPartitionPager(_ViewBasePager):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_partition_view, opts)
