# `0.8.0`

For versions earlier than `0.8.0` the model classes for document types:
* `Document`
* `DesignDocument`
* `ReplicationDocument`

were generated with standard Python convention names for all fields.
By convention a leading `_` in Python implies internal use so leading `_` were
not used for the reserved CouchDB names in the Python model classes and
were added during serialization.

This representation of the `Document` model did not allow for members with the
same names as the reserved (`_` prefixed) document metadata members.

This meant that members named any of the following were removed by the `Document`
`from_dict` and `to_dict` functions:
* `attachments`
* `conflicts`
* `deleted`
* `deleted_conflicts`
* `id`
* `local_seq`
* `rev`
* `revisions`
* `revs_info`

as described in [issue #490](https://github.com/IBM/cloudant-python-sdk/issues/490).

To resolve this problem, starting from version `0.8.0` model classes that accept
user defined properties use the leading `_` CouchDB convention for
CouchDB metadata property names instead of using the Python convention.
This introduces breaking changes that require code updates for usages
of the model types `Document`, `DesignDocument` and `ReplicationDocument`.

## Breaking changes

The kwarg or attribute names that changed are:
| kwarg/attribute name (<`0.8.0`) | kwarg/attribute name (>=`0.8.0`) |
| --- | --- |
| `attachments`| `_attachments` |
| `conflicts`| `_conflicts` |
| `deleted`| `_deleted` |
| `deleted_conflicts`| `_deleted_conflicts` |
| `id`| `_id` |
| `local_seq`| `_local_seq` |
| `rev`| `_rev` |
| `revisions`| `_revisions` |
| `revs_info`| `_revs_info` |

_Note:_ Dictionary literals always used the `_` prefixed form of the
name so there are no code changes in those cases.

### Writing

In the case of writing to the server the names are
kwarg parameters used to initialize these classes:
* `Document`
* `DesignDocument`
* `ReplicationDocument`

The functions that impacted by these changes are:
1. Functions that accept `Document` in the `document` kwarg:
    * `post_document`
    * `put_document`
    * `put_local_document` 
1. Functions that accept `DesignDocument` in the `design_document` kwarg:
    * `put_design_document`
1. Functions that accept `ReplicationDocument` in the `replication_document` kwarg:
    * `put_replication_document`
1. Functions that accept `BulkDocs` in the `bulk_docs` kwarg. In this case the
changes are in the elements of the `List[Document]` in the `docs` kwarg:
    * `post_bulk_docs`

#### Example class initialization

Before:
```python
# id is used in Document initializer
my_doc = Document(
  id="small-appliances:1000042",
  type="product",
  productid="1000042",
  name="Fidget toy")

result = service.post_document(db='products', document=my_doc).get_result()
```

After:
```python
# Now _id is used in Document initializer
my_doc = Document(
  _id="small-appliances:1000042",
  type="product",
  productid="1000042",
  name="Fidget toy")

result = service.post_document(db='products', document=my_doc).get_result()
```

#### Example dict literal

Before & After (no changes):
```python
# _id is used in dict literal
my_doc = {
  '_id': 'small-appliances:1000042',
  'type': 'product',
  'productid': '1000042',
  'name': 'Fidget toy'
}

result = service.post_document(db='products', document=my_doc).get_result()
```

### Reading

In the case of reading from the server the `_` prefixed names were always used in the raw
dictionaries returned from the `get_result` function. As such **no changes** are necessary
to the key names to read the values from these result dicts. However, renames are necessary
if the calling code uses the `from_dict` function to convert the result dict to a model class.

The functions impacted in that case are:
1. Functions returning a `dict` that represents a `Document`:
    * `get_document`
    * `get_local_document`
1. Functions returning a `dict` that represents a `DesignDocument`:
    * `get_design_document`
1. Functions returning a `dict` that represents a `ReplicationDocument`:
    * `get_replication_document`
1. Functions returning a `dict` containing a `Document` representation:
    * `post_bulk_get` (via `BulkGetResult` `results` > `BulkGetResultItem` `docs` >`BulkGetResultDocument` `ok`)
1. Functions returning a `dict` potentially containing a `Document` representation (for example if using `include_docs`):
    * `post_all_docs` (via `AllDocsResult` `rows` > `DocsResultRow` `doc`)
    * `post_changes` (via `ChangesResult` `results` > `ChangesResultItem` `doc`)
    * `post_find` (via `FindResult` `docs`)
    * `post_partition_find`(via `FindResult` `docs`)
    * `post_search` (via `SearchResult` `rows` > `SearchResultRow` `doc` or `SearchResult` `groups` > `SearchResultProperties` `rows` > `SearchResultRow` `doc`)
    * `post_partition_search` (via `SearchResult` `rows` > `SearchResultRow` `doc` or `SearchResult` `groups` > `SearchResultProperties` `rows` > `SearchResultRow` `doc`)
    * `post_view` (via `ViewResult` `rows` > `ViewResultRow` `doc`)
    * `post_partition_view` (via `ViewResult` `rows` > `ViewResultRow` `doc`)

#### Example result

Before & after (no changes):
```python
result = service.get_document(
  db='products',
  doc_id='small-appliances:1000042'
).get_result()

# _id is used to access document id in result dict
print(result._id)
# prints:
# small-appliances:1000042
```

#### Example `from_dict`

Before:
```python
result = service.get_document(
  db='products',
  doc_id='small-appliances:1000042'
).get_result()

doc = Document.from_dict(result)
# id is used to access document id in Document class
print(doc.id)
# prints:
# small-appliances:1000042
```

After:
```python
result = service.get_document(
  db='products',
  doc_id='small-appliances:1000042'
).get_result()

doc = Document.from_dict(result)
# Now _id is used to access document id in Document class
print(doc._id)
# prints:
# small-appliances:1000042
```
