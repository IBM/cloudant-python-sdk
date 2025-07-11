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
from collections.abc import Callable, Iterable, Iterator, Sequence
from enum import auto, Enum
from functools import partial
from types import MappingProxyType
from typing import Generic, Optional, Protocol, TypeVar

from ibm_cloud_sdk_core import DetailedResponse
from ibmcloudant.cloudant_v1 import CloudantV1,\
  AllDocsResult, DocsResultRow, Document, FindResult, SearchResult, SearchResultRow, ViewResult, ViewResultRow

# Type variable for the result
R = TypeVar('R', AllDocsResult, FindResult, SearchResult, ViewResult)
# Type variable for the items
I = TypeVar('I', DocsResultRow, Document, SearchResultRow, ViewResultRow)
# Type variable for the key in key based paging
K = TypeVar('K')

_MAX_LIMIT = 200
_MIN_LIMIT = 1
_DOCS_KEY_ERROR = "No need to paginate as 'key' returns a single result for an ID."
_VIEW_KEY_ERROR = "Use 'start_key' and 'end_key' instead."

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
  def get_next(self) -> Sequence[I]:
    """
    returns the next page of results
    """

    raise NotImplementedError()

  @abstractmethod
  def get_all(self) -> Sequence[I]:
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

  def __init__(self, client: CloudantV1, type: PagerType, opts: dict):
    self._client = client
    self._operation_type = type
    self._initial_opts = dict(opts)

  def pager(self) -> Pager[I]:
    """
    Create a new IBM Cloud SDK style Pager.
    This type is useful for retrieving one page at a time from a function call.
    """

    return _IteratorPager(self.pages)

  def pages(self) -> Iterable[Sequence[I]]:
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
  def _validate_limit(cls, opts: dict):
    limit: int | None = opts.get('limit')
    # For None case the valid default limit of _MAX_LIMIT will be applied later
    if limit is not None:
      if limit > _MAX_LIMIT:
        raise ValueError(f'The provided limit {limit} exceeds the maximum page size value of {_MAX_LIMIT}.')
      if limit < _MIN_LIMIT:
        raise ValueError(f'The provided limit {limit} is lower than the minimum page size value of {_MIN_LIMIT}.')

  @classmethod
  def _validate_option_absent(cls, invalid_opt: str, opts: dict, message_suffix: Optional[str]=None):
    # check if the invalid_opt is present in opts dict
    if invalid_opt in opts:
      raise ValueError(f"The option '{invalid_opt}' is invalid when using pagination.{' ' + message_suffix if message_suffix else ''}")

  @classmethod
  def _validate_options_absent(cls, invalid_opts: Sequence[str], opts: dict):
    # for each invalid_opts entry check if it is present in opts dict
    for invalid_opt in invalid_opts:
      cls._validate_option_absent(invalid_opt, opts)

  @classmethod
  def new_pagination(cls, client:CloudantV1, type: PagerType, **kwargs):
    """
    Create a new Pagination.
    client: CloudantV1 - the Cloudant service client
    type: PagerType - the operation type to paginate
    kwargs: dict - the options for the operation
    """

    # Validate the limit
    cls._validate_limit(kwargs)
    if type == PagerType.POST_ALL_DOCS:
      cls._validate_option_absent('key', kwargs, _DOCS_KEY_ERROR)
      cls._validate_options_absent(('keys',), kwargs)
      return Pagination(client, _AllDocsPageIterator, kwargs)
    if type == PagerType.POST_DESIGN_DOCS:
      cls._validate_option_absent('key', kwargs, _DOCS_KEY_ERROR)
      cls._validate_options_absent(('keys',), kwargs)
      return Pagination(client, _DesignDocsPageIterator, kwargs)
    if type == PagerType.POST_FIND:
      return Pagination(client, _FindPageIterator, kwargs)
    if type == PagerType.POST_PARTITION_ALL_DOCS:
      cls._validate_option_absent('key', kwargs, _DOCS_KEY_ERROR)
      cls._validate_options_absent(('keys',), kwargs)
      return Pagination(client, _AllDocsPartitionPageIterator, kwargs)
    if type == PagerType.POST_PARTITION_FIND:
      return Pagination(client, _FindPartitionPageIterator, kwargs)
    if type == PagerType.POST_PARTITION_SEARCH:
      return Pagination(client, _SearchPartitionPageIterator, kwargs)
    if type == PagerType.POST_PARTITION_VIEW:
      cls._validate_option_absent('key', kwargs, _VIEW_KEY_ERROR)
      cls._validate_options_absent(('keys',), kwargs)
      return Pagination(client, _ViewPartitionPageIterator, kwargs)
    if type == PagerType.POST_SEARCH:
      cls._validate_options_absent(('counts', 'group_field', 'group_limit', 'group_sort', 'ranges',), kwargs)
      return Pagination(client, _SearchPageIterator, kwargs)
    if type == PagerType.POST_VIEW:
      cls._validate_option_absent('key', kwargs, _VIEW_KEY_ERROR)
      cls._validate_options_absent(('keys',), kwargs)
      return Pagination(client, _ViewPageIterator, kwargs)

class _IteratorPagerState(Enum):
  NEW = auto()
  GET_NEXT = auto()
  GET_ALL = auto()
  CONSUMED = auto()

class _IteratorPager(Pager[I]):

  _state_consumed_msg = 'This pager has been consumed, use a new Pager.'
  _state_mixed_msg = 'Cannot mix get_all() and get_next() use only one method or make a new Pager.'

  def __init__(self, iterable_func: Callable[[], Iterator[Sequence[I]]]):
    self._iterable_func: Callable[[], Iterator[Sequence[I]]] = iterable_func
    self._iterator: Iterator[Sequence[I]] = iter(self._iterable_func())
    self._state: _IteratorPagerState = _IteratorPagerState.NEW

  def has_next(self) -> bool:
    """
    returns False if there are no more pages
    """

    return self._iterator._has_next

  def get_next(self) -> Sequence[I]:
    """
    returns the next page of results
    """
    self._check_state(mode=_IteratorPagerState.GET_NEXT)
    page: Sequence[I] = next(self._iterator)
    if not self._iterator._has_next:
      self._state = _IteratorPagerState.CONSUMED
    return page

  def get_all(self) -> Sequence[I]:
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

class _BasePageIterator(Iterator[Sequence[I]]):

  def __init__(self,
               client: CloudantV1,
               operation: Callable[..., DetailedResponse],
               page_opts: Sequence[str],
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

  def __iter__(self) -> Iterator[Sequence[I]]:
    return self

  def __next__(self) -> Sequence[I]:
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
    return opts.get('limit', _MAX_LIMIT)

  @abstractmethod
  def _result_converter(self) -> Callable[[dict], R]:
    raise NotImplementedError()

  @abstractmethod
  def _items(self, result: R) -> list[I]:
    raise NotImplementedError()

  @abstractmethod
  def _get_next_page_options(self, result: R) -> dict:
    raise NotImplementedError()

class _KeyPageIterator(_BasePageIterator, Generic[K]):

  def __init__(self, client: CloudantV1, operation: Callable[..., DetailedResponse], opts: dict):
    super().__init__(client, operation, ('skip', 'start_key', 'start_key_doc_id',), opts)
    self._boundary_failure: Optional[str] = None

  def _next_request(self) -> list[I]:
    if self._boundary_failure is not None:
      raise Exception(self._boundary_failure)
    items: list[I] = super()._next_request()
    if self._has_next:
      last_item: I = items.pop()
      if len(items) > 0:
        # Get, but don't remove the last item from the list
        penultimate_item: I = items[-1]
        self._boundary_failure: Optional[str] = self.check_boundary(penultimate_item, last_item)
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
  def check_boundary(self, penultimate_item: I, last_item: I) -> Optional[str]:
    raise NotImplementedError()

class _BookmarkPageIterator(_BasePageIterator):

  def __init__(self, client: CloudantV1, operation: Callable[..., DetailedResponse], opts: dict, extra_page_opts:Sequence[str]=()):
    super().__init__(client, operation, ('bookmark',) + extra_page_opts, opts)

  def _get_next_page_options(self, result: R) -> dict:
    return {'bookmark': result.bookmark}

class _AllDocsBasePageIterator(_KeyPageIterator[str]):

  def _result_converter(self) -> Callable[[dict], AllDocsResult]:
    return AllDocsResult.from_dict

  def _get_next_page_options(self, result: R) -> dict:
    # Remove start_key_doc_id for all_docs paging
    opts: dict = super()._get_next_page_options(result)
    del opts['start_key_doc_id']
    return opts

  def check_boundary(self, penultimate_item: I, last_item: I) -> Optional[str]:
    # IDs are always unique in _all_docs pagers so return None
    return None

class _AllDocsPageIterator(_AllDocsBasePageIterator):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_all_docs, opts)

class _AllDocsPartitionPageIterator(_AllDocsBasePageIterator):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_partition_all_docs, opts)

class _DesignDocsPageIterator(_AllDocsBasePageIterator):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_design_docs, opts)

class _FindBasePageIterator(_BookmarkPageIterator):

  def __init__(self, client: CloudantV1, operation: Callable[..., DetailedResponse], opts: dict):
    # Find requests allow skip, but it should only be used on the first request.
    # Since we don't want it on subsequent page requests we need to exclude it from
    # fixed opts used for the partial function.
    super().__init__(client, operation, opts, extra_page_opts=('skip',))

  def _items(self, result: FindResult):
    return result.docs

  def _result_converter(self):
    return FindResult.from_dict

class _FindPageIterator(_FindBasePageIterator):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_find, opts)

class _FindPartitionPageIterator(_FindBasePageIterator):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_partition_find, opts)

class _SearchBasePageIterator(_BookmarkPageIterator):

  def _items(self, result: SearchResult):
    return result.rows

  def _result_converter(self):
    return SearchResult.from_dict

class _SearchPageIterator(_SearchBasePageIterator):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_search, opts)

class _SearchPartitionPageIterator(_SearchBasePageIterator):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_partition_search, opts)

class _ViewBasePageIterator(_KeyPageIterator[any]):

  def _result_converter(self):
    return ViewResult.from_dict

  def check_boundary(self, penultimate_item: I, last_item: I) -> Optional[str]:
    if penultimate_item.id == (boundary_id := last_item.id) \
      and penultimate_item.key == (boundary_key := last_item.key):
      return f'Cannot paginate on a boundary containing identical keys {boundary_key} and document IDs {boundary_id}'
    return None

class _ViewPageIterator(_ViewBasePageIterator):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_view, opts)

class _ViewPartitionPageIterator(_ViewBasePageIterator):

  def __init__(self, client: CloudantV1, opts: dict):
    super().__init__(client, client.post_partition_view, opts)
