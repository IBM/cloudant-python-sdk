<!-- This section applied from common template, do not edit in language specific repository KNOWN_ISSUES file -->
# Limitations, Restrictions, and Known Issues

## All Cloudant SDKs

### Path elements containing the `+` character

Path elements containing the `+` character in the SDKs are not interoperable with Apache CouchDB and Cloudant.
* This is because standard URL encoding libraries following the [RFC3986 URI specification](https://tools.ietf.org/html/rfc3986#section-3.3) do not encode this character in path elements.
* Apache CouchDB violates the specification by treating the `+` in path elements as a space character (see https://github.com/apache/couchdb/issues/2235).
* Path elements include database names, all document names, and index and view names.
* It is possible to workaround for document names with a `+` in the ID (e.g. `docidwith+char`) by using:
    * For reading: use the `post` all docs operation and the `key` or `keys` parameter with a value of the document ID including the `+`.
    * For writing: use the `post` document operation or `post` bulk docs operation with the value of the document ID including the `+`.
* There is no pre-encoding workaround because the result is a double encoding e.g. using `%2b` in the path element ends up being double encoded as `%252b`.

### Views

#### Objects as keys

Using JSON objects as keys (e.g. `start_key`, `end_key`, `key`, `keys`)
can cause inconsistent results because the ordering of the members of the JSON
object after serialization is not guaranteed.

### Search

#### Cannot use `drilldown` parameters

Drilldown parameters cannot be used for search queries with server versions:
* CouchDB versions <= 3.1.0
* Cloudant (Classic) <= 8158

### Changes

#### Terminated connections

When using the `post` changes operation the connection may intermittently terminate with an early `EOF` when using
server versions:
* CouchDB versions <= 3.1.1
* Cloudant (Classic) <= 8169

### Cloudant on Transaction Engine

Whilst most SDK methods will work with _Cloudant on Transaction Engine_ there are some limitations.
It should be noted that not all existing API options are applicable to _Cloudant on Transaction Engine_
and new API options added in _Cloudant on Transaction Engine_ are not yet available in the SDKs. Please
consult the Cloudant documentation for further information.

### Compression

* Manually setting an `Accept-Encoding` header on requests will disable the transparent gzip decompression of response bodies from the server.
* Manually setting a `Content-Encoding` header on requests will disable the transparent gzip compression of request bodies to the server.

<!-- End common section -->

<!-- Template substitution for language specific content -->
<!-- ## SPLIT MARKER ## -->
## Cloudant SDK for Python

### Request bodies containing the `headers` parameter

The `headers` dict is always reserved for the API request headers.
In order to avoid collision between the request headers and the `headers` parameter
that is contained by the request body, use the `headers_` as
the request body `headers` parameter.

E.g. to set the `headers` parameter of your replication
target database, use the following approach:

```python
...
target_db = ReplicationDatabase(
    headers_={"Authorization": "Basic <your-base64-encoded-auth-key>"},
    url='http://localhost:5984/animaldb-target'
)
...
```
The example above represents this JSON body:
```json
{
    ...
    "target": {
        "headers": {
            "Authorization": "Basic <your-base64-encoded-auth-key>"
        },
        "url": "<your-service-url>/animaldb-target"
    },
    ...
}
```
