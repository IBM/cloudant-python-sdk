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
 
 Import :class:`~ibmcloudant.Pagination` and :class:`~ibmcloudant.PagerType`
 from :mod:`ibmcloudant`.
 Use :meth:`Pagination.new_pagination` to create a :class:`Pagination`
 for the specific :class:`PagerType` operation and options.
"""

from abc import abstractmethod
from collections.abc import Callable, Iterable, Iterator
from enum import auto, Enum
from functools import partial
from types import MappingProxyType
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

class Pager(Protocol[I]):
  """
  Protocol for pagination of Cloudant operations.

  Use Pager.new_pager to create a new pager for one of
  the operation types in PagerType.
  """

  @abstractmethod
  def has_next(self) -> bool:
    """
    returns False if there are no more pages
    """

    raise NotImplementedError()

  @abstractmethod
  def get_next(self) -> tuple[I]:
    """
    returns the next page of results
    """

    raise NotImplementedError()

  @abstractmethod
  def get_all(self) -> tuple[I]:
    """
    returns all the pages of results in single list
    """

    raise NotImplementedError()

class Pagination:
  """
  Entry point for the pagination features.

  Use :meth:`Pagination.new_pagination` to create a :class:`Pagination`
  instance for the specific :class:`PagerType` operation and options.

  Then create a Pager or Iterable using one of the functions:
   * :meth:`pager` - for an IBM Cloud SDK style Pager
   * :meth:`pages` - for a page Iterable
   * :meth:`rows` - for a row Iterable
  """

  def __init__(self, client: CloudantV1, type, opts: dict):
    self._client = client
    self._operation_type = type
    self._initial_opts = dict(opts)

  def pager(self) -> Pager[I]:
    """
    Create a new IBM Cloud SDK style Pager.
    This type is useful for retrieving one page at a time from a function call.
    """

    return _IteratorPager(self.pages)

  def pages(self) -> Iterable[tuple[I]]:
    """
    Create a new Iterable for all the pages.
    This type is useful for handling pages in a for loop.

    for page in Pagination.new_pagination(client, **opts).pages():
      ...
    """

    return self._operation_type(self._client, self._initial_opts)

  def rows(self) -> Iterable[I]:
    """
    Create a new Iterable for all the rows from all the pages.
    This type is useful for handling rows in a for loop.

    for row in Pagination.new_pagination(client, **opts).rows():
      ...
    """

    for page in self.pages():
      yield from page

  @classmethod
  def new_pagination(cls, client:CloudantV1, type: PagerType, **kwargs):
    """
    Create a new Pagination.
    client: CloudantV1 - the Cloudant service client
    type: PagerType - the operation type to paginate
    kwargs: dict - the options for the operation
    """

    if type == PagerType.POST_ALL_DOCS:
      return Pagination(client, _AllDocsPager, kwargs)
    if type == PagerType.POST_DESIGN_DOCS:
      return Pagination(client, _DesignDocsPager, kwargs)
    if type == PagerType.POST_FIND:
      return Pagination(client, _FindPager, kwargs)
    if type == PagerType.POST_PARTITION_ALL_DOCS:
      return Pagination(client, _AllDocsPartitionPager, kwargs)
    if type == PagerType.POST_PARTITION_FIND:
      return Pagination(client, _FindPartitionPager, kwargs)
    if type == PagerType.POST_PARTITION_SEARCH:
      return Pagination(client, _SearchPartitionPager, kwargs)
    if type == PagerType.POST_PARTITION_VIEW:
      return Pagination(client, _ViewPartitionPager, kwargs)
    if type == PagerType.POST_SEARCH:
      return Pagination(client, _SearchPager, kwargs)
    if type == PagerType.POST_VIEW:
      return Pagination(client, _ViewPager, kwargs)

# TODO state checks
class _IteratorPagerState(Enum):
  NEW = auto()
  GET_NEXT = auto()
  GET_ALL = auto()
  CONSUMED = auto()

class _IteratorPager(Pager[I]):

  _state_mixed_msg = 'This pager has been consumed, use a new Pager.'
  _state_consumed_msg = 'Cannot mix get_all() and get_next() use only one method or make a new Pager.'

  def __init__(self, iterable_func: Callable[[], Iterator[tuple[I]]]):
    self._iterable_func: Callable[[], Iterator[tuple[I]]] = iterable_func
    self._iterator: Iterator[tuple[I]] = iter(self._iterable_func())
    self._state: _IteratorPagerState = _IteratorPagerState.NEW

  def has_next(self) -> bool:
    """
    returns False if there are no more pages
    """

    return self._iterator._has_next

  def get_next(self) -> tuple[I]:
    """
    returns the next page of results
    """
    self._check_state(mode=_IteratorPagerState.GET_NEXT)
    page: tuple[I] = next(self._iterator)
    if not self._iterator._has_next:
      self._state = _IteratorPagerState.CONSUMED
    return page

  def get_all(self) -> tuple[I]:
    """
    returns all the pages of results in single list
    """

    self._check_state(mode=_IteratorPagerState.GET_ALL)
    all_items: list[I] = []
    for page in self._iterable_func():
      all_items.extend(page)
    self._state = _IteratorPagerState.CONSUMED
    return (*all_items,)

  def _check_state(self, mode: _IteratorPagerState):
    if self._state == mode:
      return
    if self._state == _IteratorPagerState.NEW:
      self._state = mode
      return
    if self._state == _IteratorPagerState.CONSUMED:
      raise Exception(_IteratorPager._state_consumed_msg)
    raise Exception(_IteratorPager._state_mixed_msg)

class _BasePager(Iterator[tuple[I]]):

  def __init__(self,
               client: CloudantV1,
               operation: Callable[..., DetailedResponse],
               page_opts: list[str],
               opts: dict):
    self._client: CloudantV1 = client
    self._has_next: bool = True
    # split the opts into fixed and page parts based on page_opts
    self._next_page_opts: dict = {}
    fixed_opts: dict = dict(opts)
    # Get the page size and set the limit acoordingly
    self._page_size: int = self._page_size_from_opts_limit(fixed_opts)
    fixed_opts['limit'] = self._page_size
    # Remove the options that change per page
    for k in page_opts:
      if v := fixed_opts.pop(k, None):
        self._next_page_opts[k] = v
    fixed_opts = MappingProxyType(fixed_opts)
    # Partial method with the fixed ops
    self._next_request_function: Callable[..., DetailedResponse] = partial(operation, **fixed_opts)

  def __iter__(self) -> Iterator[tuple[I]]:
    return self

  def __next__(self) -> tuple[I]:
    if self._has_next:
      return (*self._next_request(),)
    raise StopIteration()

  def _next_request(self) -> list[I]:
    response: DetailedResponse = self._next_request_function(**self._next_page_opts)
    result: dict = response.get_result()
    typed_result: R = self._result_converter()(result)
    items: list[I] = self._items(typed_result)
    if len(items) < self._page_size:
      self._has_next = False
    else:
      self._next_page_opts = self._get_next_page_options(typed_result)
    return items

  def _page_size_from_opts_limit(self, opts:dict) -> int:
    return opts.get('limit', 200)

  @abstractmethod
  def _result_converter(self) -> Callable[[dict], R]:
    raise NotImplementedError()

  @abstractmethod
  def _items(self, result: R) -> list[I]:
    raise NotImplementedError()

  @abstractmethod
  def _get_next_page_options(self, result: R) -> dict:
    raise NotImplementedError()

class _KeyPager(_BasePager, Generic[K]):

  def __init__(self, client: CloudantV1, operation: Callable[..., DetailedResponse], opts: dict):
    super().__init__(client, operation, ['start_key', 'start_key_doc_id'], opts)
    self._boundary_failure: str | None = None

  def _next_request(self) -> list[I]:
    if self._boundary_failure is not None:
      raise Exception(self._boundary_failure)
    items: list[I] = super()._next_request()
    if self._has_next:
      last_item: I = items.pop()
      if len(items) > 0:
        # Get, but don't remove the last item from the list
        penultimate_item: I = items[-1]
        self._boundary_failure: str | None = self.check_boundary(penultimate_item, last_item)
    return items

  def _get_next_page_options(self, result: R) -> dict:
    # last item is used for next page options
    last_item = self._items(result)[-1]
    return {
      'start_key': last_item.key,
      'start_key_doc_id': last_item.id,
    }

  def _items(self, result: R) -> list[I]:
    return result.rows

  def _page_size_from_opts_limit(self, opts:dict) -> int:
    return super()._page_size_from_opts_limit(opts) + 1

  @abstractmethod
  def check_boundary(self, penultimate_item: I, last_item: I) -> str | None:
    raise NotImplementedError()

class _BookmarkPager(_BasePager):

  def __init__(self, client: CloudantV1, operation: Callable[..., DetailedResponse], opts: dict):
    super().__init__(client, operation, ['bookmark'], opts)

  def _get_next_page_options(self, result: R) -> dict:
    return {'bookmark': result.bookmark}

class _AllDocsBasePager(_KeyPager[str]):

  def _result_converter(self) -> Callable[[dict], AllDocsResult]:
    return AllDocsResult.from_dict

  def _get_next_page_options(self, result: R) -> dict:
    # Remove start_key_doc_id for all_docs paging
    opts: dict = super()._get_next_page_options(result)
    del opts.start_key_doc_id

  def check_boundary(self, penultimate_item: I, last_item: I) -> str | None:
    # IDs are always unique in _all_docs pagers so return None
    return None

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
    return ViewResult.from_dict

  def check_boundary(self, penultimate_item: I, last_item: I) -> str | None:
    if penultimate_item.id == (boundary_id := last_item.id) \
      and penultimate_item.key == (boundary_key := last_item.key):
      return f'Cannot paginate on a boundary containing identical keys {boundary_key} and document IDs {boundary_id}'
    return None

class _ViewPager(_ViewBasePager):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_view, opts)

class _ViewPartitionPager(_ViewBasePager):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_partition_view, opts)
