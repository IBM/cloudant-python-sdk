# Limitations, Restrictions, and Known Issues

## All Cloudant SDKs

### Cloudant (Gen 2) Compatibility

Cloudant Gen 2 is compatible with IAM authentication only.
The SDK authentication types `BASIC` and `COUCHDB_SESSION` do not work with Cloudant Gen 2 instances.

Instances of Cloudant Gen 2 do not provide some configuration and monitoring APIs that were available in Gen 1.

Migrating an application using this SDK from Cloudant Gen 1 to Cloudant Gen 2 requires either removing calls to these operations
or replacing them with alternatives.

This table summarizes the SDK operations that are incompatible with Cloudant Gen 2 instances and the recommended replacement operations.

| Gen 1 operation | Summary | Gen 1 Endpoint | API docs link | Replacement operation for Gen 2 |
|---|---|---|---|---|
| **Authentication and authorization** | | | | |
| `post_api_keys` | Generates API keys for apps or persons to enable database access | `POST /_api/v2/api_keys` | [API docs link](https://cloud.ibm.com/apidocs/cloudant/cloudant-gen1?code=python#postapikeys) | Use IAM authentication |
| `put_cloudant_security_configuration` | Modify only Cloudant related database permissions | `PUT /_api/v2/db/{db}/_security` | [API docs link](https://cloud.ibm.com/apidocs/cloudant/cloudant-gen1?code=python#putcloudantsecurity) | Use [database level IAM policies](https://cloud.ibm.com/docs/cloudant-gen2?topic=cloudant-gen2-managing-access-for-cloudant#database-level-iam-policies) |
| **Audit events configuration** | | | | |
`get_activity_tracker_events` | Retrieve activity tracking events information | `GET /_api/v2/user/activity_tracker/events` | [API docs link](https://cloud.ibm.com/apidocs/cloudant/cloudant-gen1?code=python#getactivitytrackerevents) | `management` events are always enabled, `data` events are not currently available in Gen 2 |
`post_activity_tracker_events` | Modify activity tracking events configuration | `POST /_api/v2/user/activity_tracker/events` | [API docs link](https://cloud.ibm.com/apidocs/cloudant/cloudant-gen1?code=python#postactivitytrackerevents) | `management` events are always enabled, `data` events are not currently available in Gen 2 |
| **CORS configuration** | | | | |
| `get_cors_information` | Retrieve CORS configuration information | `GET /_api/v2/user/config/cors` | [API docs link](https://cloud.ibm.com/apidocs/cloudant/cloudant-gen1?code=python#getcorsinformation) | Use the [Platform Services SDK](#using-the-platform-services-sdk)
| `put_cors_configuration` | Modify CORS configuration | `PUT /_api/v2/user/config/cors` | [API docs link](https://cloud.ibm.com/apidocs/cloudant/cloudant-gen1?code=python#putcorsconfiguration) | Use the [Platform Services SDK](#using-the-platform-services-sdk)
| **Capacity configuration** | | | | |
| `get_capacity_databases_information` | Retrieve maximum allowed database count | `GET /_api/v2/user/capacity/databases` | [API docs link](https://cloud.ibm.com/apidocs/cloudant/cloudant-gen1?code=python#getcapacitydatabasesinformation) | Use the [Platform Services SDK](#using-the-platform-services-sdk)
| `get_capacity_throughput_information` | Retrieve provisioned throughput capacity information | `GET /_api/v2/user/capacity/throughput` | [API docs link](https://cloud.ibm.com/apidocs/cloudant/cloudant-gen1?code=python#getcapacitythroughputinformation) | Use the [Platform Services SDK](#using-the-platform-services-sdk)
| `put_capacity_throughput_configuration` | Update the target provisioned throughput capacity | `PUT /_api/v2/user/capacity/throughput` | [API docs link](https://cloud.ibm.com/apidocs/cloudant/cloudant-gen1?code=python#putcapacitythroughputconfiguration) | Use the [Platform Services SDK](#using-the-platform-services-sdk)
| **Capacity monitoring** | | | | |
| `get_current_databases_information` | Retrieve current database count | `GET /_api/v2/user/current/databases` | [API docs link](https://cloud.ibm.com/apidocs/cloudant/cloudant-gen1?code=python#getcurrentdatabasesinformation) | Use the length of the list returned from the `get_all_dbs` operation.
| `get_current_throughput_information` | Retrieve the current provisioned throughput capacity consumption | `GET /_api/v2/user/current/throughput` | [API docs link](https://cloud.ibm.com/apidocs/cloudant/cloudant-gen1?code=python#getcurrentthroughputinformation) | Use a Prometheus instant query with IBM Cloud Monitoring APIs. For example to get the capacity consumption rate over the last minute use a query like `rate(ibm_cloudant_permitted_operations_total[1m])`. See the [IBM Cloud Monitoring docs for an example](https://cloud.ibm.com/docs/monitoring?topic=monitoring-metrics_api#metrics-api-sample-prom).

#### Using the Platform Services SDK

Use the [IBM Cloud Platform Services Python SDK](https://github.com/IBM/platform-services-python-sdk) Resource Controller APIs to programmatically configure your Cloudant Gen 2 instance.

Update the configuration values in the `parameters` mapping of key-value pairs.
Read the current values from the `extensions` mapping of key-value pairs.

| Key path in `parameters` or `extensions` | Value description |
| --- | --- |
`dataservices.cloudant.capacity_units` | The provisioned throughput capacity of the instance in [units](https://cloud.ibm.com/docs/cloudant-gen2?topic=cloudant-gen2-usage-and-charges#provisioned-throughput-capacity-units)
`dataservices.cloudant.configuration.cors` | The CORS configuration object of the instance with booleans for `enabled` and `allowCredentials` and a string array of `origins`
`dataservices.cloudant.configuration.db_count_limit` | Read only value of the maximum number of databases allowed on the instance

##### Viewing configuration

Use [Get a resource instance](https://cloud.ibm.com/apidocs/resource-controller/resource-controller?code=python#get-resource-instance) to retrieve the resource instance configuration.

##### Modifying configuration

For a new instance use [Create (provision) a new resource instance](https://cloud.ibm.com/apidocs/resource-controller/resource-controller?code=python#create-resource-instance).
For a pre-existing instance use [Update a resource instance](https://cloud.ibm.com/apidocs/resource-controller/resource-controller?code=python#update-resource-instance).


### Path elements containing the `+` character

Path elements containing the `+` character in the SDKs are not interoperable with:
* Cloudant 
* Apache CouchDB versions older than 3.2.0
* Apache CouchDB versions 3.2.0 or newer with the setting `decode_plus_to_space = true`

This is because standard URL encoding libraries following the [RFC3986 URI specification](https://tools.ietf.org/html/rfc3986#section-3.3) do not encode the `+` character in path elements.
* It is possible to workaround for document names with a `+` in the ID (e.g. `docidwith+char`) by using:
    * For reading: use the `post` all docs operation and the `key` or `keys` parameter with a value of the document ID including the `+`.
    * For writing: use the `post` document operation or `post` bulk docs operation with the value of the document ID including the `+`.
* There is no pre-encoding workaround because the result is a double encoding e.g. using `%2b` in the path element ends up being double encoded as `%252b`.

### Views

#### Objects as keys

Using JSON objects as keys (e.g. `start_key`, `end_key`, `key`, `keys`)
can cause inconsistent results because the ordering of the members of the JSON
object after serialization is not guaranteed.

### Documents

#### Attachments

The `atts_since` parameter is not supported when retrieving a document.
The workaround is to call `POST /{db}/_bulk_get` using the `atts_since` field under the `docs` request body. See the [alternative example request for `atts_since` using the `/_bulk_get` endpoint](https://cloud.ibm.com/apidocs/cloudant#postbulkget) in our API Docs.
Example JSON request body:
```json
{
  "docs": [{"id": "order00058", "atts_since": "1-99b02e08da151943c2dcb40090160bb8"}]
}
```

#### Open revisions

The `open_revs` parameter is not supported when retrieving a document.
If you want to retrieve documents with all leaf revisions (`open_revs=all`), the workaround is to call `POST /{db}/_bulk_get` using the `id` field within the `docs` array request body.
See the [alternative example request for `open_revs=all` using the `/_bulk_get` endpoint](https://cloud.ibm.com/apidocs/cloudant#postbulkget) in our API Docs.
Example JSON request body:
```json
{
  "docs": [{"id": "order00067"}]
}
```

If you want to retrieve documents of specified leaf revisions (e.g. `open_revs=["3-917fa2381192822767f010b95b45325b", "4-a5be949eeb7296747cc271766e9a498b"]`), the workaround is to call `POST /{db}/_bulk_get` using the same `id` value for each unique `rev` value within of the `docs` array request body.
See the [default example request using the `/_bulk_get` endpoint](https://cloud.ibm.com/apidocs/cloudant#postbulkget) in our API Docs.
Example JSON request body:
```json
{
  "docs": [
    {
      "id": "order00067",
      "rev": "3-917fa2381192822767f010b95b45325b"
    },
    {
      "id": "order00067",
      "rev": "4-a5be949eeb7296747cc271766e9a498b"
    }
  ]
}
```

### Compression

* Manually setting an `Accept-Encoding` header on requests will disable the transparent gzip decompression of response bodies from the server.
* Manually setting a `Content-Encoding` header on requests will disable the transparent gzip compression of request bodies to the server.

### Changes feed

#### Filter functions

The SDK does not support passing user-defined query or body parameters in `_changes` requests for dynamic filter functions in design documents. 
The workaround and recommended option is to use a `selector` type filter.
For example, if you are using a `_changes` request like `/{db}/_changes?filter=myDdoc/byName&name=Jane` with a filter function like:
```javascript
function(doc, req) {
    if (doc.name !== req.query.name) {
        return false;
    }
    return true; 
}
```
It can be replaced with a request using a selector filter:
```python
service = CloudantV1.new_instance()

response = service.post_changes(
  db='orders',
  filter='_selector',
  selector={'name': 'Jane'}
).get_result()
```


## Cloudant SDK for Python
<!-- KNOWN_ISSUES specific to Python -->
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

### Disabling request body compression

Some issues with older server versions can be worked around by disabling
compression of request bodies. This is an example of how to do that.

```python
from ibmcloudant.cloudant_v1 import CloudantV1
client = CloudantV1.new_instance(service_name="YOUR_SERVICE_NAME")
client.set_enable_gzip_compression(False)
...
```

### Attachments with `content-type: application/json`

Calling [`get_attachment`](https://ibm.github.io/cloudant-python-sdk/docs/latest/apidocs/ibmcloudant/ibmcloudant.cloudant_v1.html#ibmcloudant.cloudant_v1.CloudantV1.get_attachment)
typically returns a `DetailedResponse` with `BinaryIO` result.
For attachments uploaded with a `content-type: application/json`
header or as a `.json` file in the dashboard then calls to `get_attachment`
return a `DetailedResponse` with, for example, a `dict` result for a JSON
object.
The JSON is automatically loaded by the underlying SDK core
and client to the default Python object types.

To get a `BinaryIO` result with an `application/json` attachment
pass `stream=True` on the `get_attachment` request.

```python
json_attachment: bytes = service.get_attachment(
  db='products',
  doc_id='1000042',
  attachment_name='product_details.json',
  stream=True
).get_result().content # content bytes that can be decoded
```
