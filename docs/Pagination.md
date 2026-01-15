# Pagination

<details open>
<summary>Table of Contents</summary>

<!-- toc -->
- [Introduction](#introduction)
- [Limitations](#limitations)
- [Capacity considerations](#capacity-considerations)
- [Available operations](#available-operations)
- [Creating a pagination](#creating-a-pagination)
  * [Initialize the service](#initialize-the-service)
  * [Set the options](#set-the-options)
  * [Create the pagination](#create-the-pagination)
- [Using pagination](#using-pagination)
  * [Iterate pages](#iterate-pages)
  * [Iterate rows](#iterate-rows)
  * [Pager](#pager)
    + [Get each page from a pager](#get-each-page-from-a-pager)
    + [Get all results from a pager](#get-all-results-from-a-pager)
</details>

## Introduction

The pagination feature (currently beta) accepts options for a single operation and automatically
creates the multiple requests to the server necessary to page through the results a fixed number at a time.

Pagination is a best-practice to break apart large queries into multiple server requests.
This has a number of advantages:
* Keeping requests within server imposed limits, for example
  * `200` max results for text search
  * `2000` max results for partitioned queries
* Fetching only the necessary data, for example
  * User finds required result on first page, no need to continue fetching results
* Reducing the duration of any individual query
  * Reduce risk of query timing out on the server
  * Reduce risk of network request timeouts

## Limitations

Limitations of pagination:
* Forward only, no backwards paging
* Limitations on `_all_docs` and `_design_docs` operations
  * No pagination for `key` option.
    There is no need to paginate as IDs are unique and this returns only a single row.
    This is better achieved with a single document get request.
  * No pagination for `keys` option.
* Limitations on `_view` operations
  * No pagination for `key` option. Pass the same `key` as a start and end key instead.
  * No pagination for `keys` option.
  * Views that emit multiple identical keys (with the same or different values)
    from the same document cannot paginate if those key rows with the same ID
    span a page boundary.
    The pagination feature detects this condition and an error occurs.
    It may be possible to workaround using a different page size.
* Limitations on `_search` operations
  * No pagination of grouped results.
  * No pagination of faceted `counts` or `ranges` results.

## Capacity considerations

Pagination can make many requests rapidly from a single program call.

For IBM Cloudant take care to ensure you have appropriate plan capacity
in place to avoid consuming all the permitted requests.
If there is no remaining plan allowance and retries are not enabled or insufficient
then a `429 Too Many Requests` error occurs.

## Available operations

Pagination is available for these operations:
* Query all documents [global](https://cloud.ibm.com/apidocs/cloudant?code=python#postalldocs)
  and [partitioned](https://cloud.ibm.com/apidocs/cloudant?code=python#postpartitionalldocs)
  * [Global all documents examples](https://github.com/IBM/cloudant-python-sdk/tree/v0.11.3/test/examples/src/features/pagination/all_docs_pagination.py)
  * [Partitioned all documents examples](https://github.com/IBM/cloudant-python-sdk/tree/v0.11.3/test/examples/src/features/pagination/partition_all_docs_pagination.py)
* Query all [design documents](https://cloud.ibm.com/apidocs/cloudant?code=python#postdesigndocs)
  * [Design documents examples](https://github.com/IBM/cloudant-python-sdk/tree/v0.11.3/test/examples/src/features/pagination/design_docs_pagination.py)
* Query with selector syntax [global](https://cloud.ibm.com/apidocs/cloudant?code=python#postfind)
  and [partitioned](https://cloud.ibm.com/apidocs/cloudant?code=python#postpartitionfind)
  * [Global find selector query examples](https://github.com/IBM/cloudant-python-sdk/tree/v0.11.3/test/examples/src/features/pagination/find_pagination.py)
  * [Partitioned find selector query examples](https://github.com/IBM/cloudant-python-sdk/tree/v0.11.3/test/examples/src/features/pagination/partition_find_pagination.py)
* Query a search index [global](https://cloud.ibm.com/apidocs/cloudant?code=python#postsearch)
  and [partitioned](https://cloud.ibm.com/apidocs/cloudant?code=python#postpartitionsearch)
  * [Global search examples](https://github.com/IBM/cloudant-python-sdk/tree/v0.11.3/test/examples/src/features/pagination/search_pagination.py)
  * [Partitioned search examples](https://github.com/IBM/cloudant-python-sdk/tree/v0.11.3/test/examples/src/features/pagination/partition_search_pagination.py)
* Query a MapReduce view [global](https://cloud.ibm.com/apidocs/cloudant?code=python#postview)
  and [partitioned](https://cloud.ibm.com/apidocs/cloudant?code=python#postpartitionview)
  * [Global view examples](https://github.com/IBM/cloudant-python-sdk/tree/v0.11.3/test/examples/src/features/pagination/view_pagination.py)
  * [Partitioned view examples](https://github.com/IBM/cloudant-python-sdk/tree/v0.11.3/test/examples/src/features/pagination/partition_view_pagination.py)

The examples presented in this `README` are for all documents in a partition.
The links in the list are to equivalent examples for each of the other available operations.

## Creating a pagination

Make a new pagination from a client, `PagerType` for the operation
and the options for the chosen operation.
Use the `limit` option to configure the page size (default and maximum `200`).

Imports required for these examples:

<details open>
<summary>Python:</summary>

```py
from ibmcloudant import Pager, Pagination, PagerType
from ibmcloudant.cloudant_v1 import CloudantV1
```

</details>

### Initialize the service

<details open>
<summary>Python:</summary>

```py
# Initialize service
service = CloudantV1.new_instance()
```

</details>

### Set the options

<details open>
<summary>Python:</summary>

```py
# Setup options
opts = {
    'db': 'events',  # example database name
    'limit': 50,  # limit option sets the page size
    'partition_key': 'ns1HJS13AMkK',  # query only this partition
}
```

</details>

### Create the pagination

<details open>
<summary>Python:</summary>

```py
# Create pagination
pagination = Pagination.new_pagination(
    service, PagerType.POST_PARTITION_ALL_DOCS, **opts)
# pagination can be reused without side-effects as a factory for iterables or pagers
# options are fixed at pagination creation time
```

</details>

## Using pagination

Once you have a pagination factory there are multiple options available.

* Iterate pages
* Iterate rows
* Get each page from a pager
* Get all results from a pager

All the paging styles produce equivalent results and make identical page requests.
The style of paging to choose depends on the use case requirements
in particular whether to process a page at a time or a row at a time.

The pagination factory is reusable and can repeatedly produce new instances
of the same or different pagination styles for the same operation options.

Here are examples for each paging style.

### Iterate pages

Iterating pages is ideal for using an iterable for loop to process a page at a time.

<details open>
<summary>Python:</summary>

```py
# Option: iterate pages
# Ideal for using a for loop with each page.
# Each call to pages() returns a fresh iterator that can be traversed once.
for page in pagination.pages():
    # Do something with page
    pass
```

</details>

### Iterate rows

Iterating rows is ideal for using an iterable for loop to process a result row at a time.

<details open>
<summary>Python:</summary>

```py
# Option: iterate rows
# Ideal for using a for loop with each row.
# Each call to rows() returns a fresh iterator that can be traversed once.
for row in pagination.rows():
    # Do something with row
    pass
```

</details>

### Pager

The pager style is similar to other [IBM Cloud SDKs](https://github.com/IBM/ibm-cloud-sdk-common?tab=readme-ov-file#pagination).
Users familiar with that style of pagination may find using them preferable
to the native language style iterators.

In the Cloudant SDKs these pagers are single use and traverse the complete set of pages once and only once.
After exhaustion they cannot be re-used, simply create a new one from the pagination factory if needed.

Pagers are only valid for one of either page at a time or getting all results.
For example, calling for the next page then calling for all results causes an error.

#### Get each page from a pager

This is useful for calling to retrieve one page at a time, for example,
in a user interface with a "next page" interaction.

If calling for the next page errors, it is valid to call for the next page again
to continue paging.

<details open>
<summary>Python:</summary>

```py
# Option: use pager next page
# For retrieving one page at a time with a method call.
pager: Pager = pagination.pager()
if pager.has_next():
    page = pager.get_next()
    # Do something with page
```

</details>

#### Get all results from a pager

This is useful to retrieve all results in a single call.
However, this approach requires sufficient memory for the entire collection of results.
So although it may be convenient for small result sets generally prefer iterating pages
or rows with the other paging styles, especially for large result sets.

If calling for all the results errors, then calling for all the results again restarts the pagination.

<details open>
<summary>Python:</summary>

```py
# Option: use pager all results
# For retrieving all result rows in a single list
# Note: all result rows may be very large!
# Preferably use iterables instead of get_all for memory efficiency with large result sets.
all_pager: Pager = pagination.pager()
all_rows = all_pager.get_all()
for page in all_rows:
    # Do something with row
    pass
```

</details>
