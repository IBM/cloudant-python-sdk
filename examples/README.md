# Examples for python

## getServerInformation

_GET `/`_

### [Example request](snippets/getServerInformation/example_request.py)

[embedmd]:# (snippets/getServerInformation/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_server_information().get_result()

print(response)
```

## getActiveTasks

_GET `/_active_tasks`_

### [Example request](snippets/getActiveTasks/example_request.py)

[embedmd]:# (snippets/getActiveTasks/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_active_tasks().get_result()

print(response)
```

## getAllDbs

_GET `/_all_dbs`_

### [Example request](snippets/getAllDbs/example_request.py)

[embedmd]:# (snippets/getAllDbs/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_all_dbs().get_result()

print(response)
```

## postApiKeys

_POST `/_api/v2/api_keys`_

### [Example request](snippets/postApiKeys/example_request.py)

[embedmd]:# (snippets/postApiKeys/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_api_keys().get_result()

print(response)
```

## putCloudantSecurity

_PUT `/_api/v2/db/{db}/_security`_

### [Example request](snippets/putCloudantSecurity/example_request.py)

[embedmd]:# (snippets/putCloudantSecurity/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

security_object = {'nobody':['_reader']}
response = service.put_cloudant_security_configuration(
  db='products',
  cloudant=security_object
).get_result()

print(response)
# section: markdown
# The `nobody` username applies to all unauthenticated connection attempts. For example, if an application tries to read data from a database, but didn't identify itself, the task can continue only if the `nobody` user has the role `_reader`.
# section: markdown
# If instead of using Cloudant's security model for managing permissions you opt to use the Apache CouchDB `_users` database (that is using legacy credentials _and_ the `couchdb_auth_only:true` option) then be aware that the user must already exist in `_users` database before adding permissions. For information on the `_users` database, see <a href="https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-work-with-your-account#using-the-users-database-with-cloudant-nosql-db" target="_blank">Using the `_users` database with Cloudant</a>.
```

## getActivityTrackerEvents

_GET `/_api/v2/user/activity_tracker/events`_

### [Example request](snippets/getActivityTrackerEvents/example_request.py)

[embedmd]:# (snippets/getActivityTrackerEvents/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_activity_tracker_events().get_result()

print(response)
```

## postActivityTrackerEvents

_POST `/_api/v2/user/activity_tracker/events`_

### [Example request](snippets/postActivityTrackerEvents/example_request.py)

[embedmd]:# (snippets/postActivityTrackerEvents/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_activity_tracker_events(
  types=['management']
).get_result()

print(response)
```

## getCapacityThroughputInformation

_GET `/_api/v2/user/capacity/throughput`_

### [Example request](snippets/getCapacityThroughputInformation/example_request.py)

[embedmd]:# (snippets/getCapacityThroughputInformation/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_capacity_throughput_information().get_result()

print(response)
```

## putCapacityThroughputConfiguration

_PUT `/_api/v2/user/capacity/throughput`_

### [Example request](snippets/putCapacityThroughputConfiguration/example_request.py)

[embedmd]:# (snippets/putCapacityThroughputConfiguration/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.put_capacity_throughput_configuration(
  blocks=1
).get_result()

print(response)
```

## getCorsInformation

_GET `/_api/v2/user/config/cors`_

### [Example request](snippets/getCorsInformation/example_request.py)

[embedmd]:# (snippets/getCorsInformation/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_cors_information().get_result()

print(response)
```

## putCorsConfiguration

_PUT `/_api/v2/user/config/cors`_

### [Example request](snippets/putCorsConfiguration/example_request.py)

[embedmd]:# (snippets/putCorsConfiguration/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.put_cors_configuration(
  enable_cors=True,
  origins=['https://example.com']
).get_result()

print(response)
```

## getCurrentThroughputInformation

_GET `/_api/v2/user/current/throughput`_

### [Example request](snippets/getCurrentThroughputInformation/example_request.py)

[embedmd]:# (snippets/getCurrentThroughputInformation/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_current_throughput_information().get_result()

print(response)
```

## getDbUpdates

_GET `/_db_updates`_

### [Example request](snippets/getDbUpdates/example_request.py)

[embedmd]:# (snippets/getDbUpdates/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_db_updates(
  feed='normal',
  heartbeat=10000,
  since='now'
).get_result()

print(response)
# section: markdown
# This request requires `server_admin` access.
```

## postDbsInfo

_POST `/_dbs_info`_

### [Example request](snippets/postDbsInfo/example_request.py)

[embedmd]:# (snippets/postDbsInfo/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_dbs_info(
  keys=['products', 'users', 'orders']
).get_result()

print(response)
```

## getMembershipInformation

_GET `/_membership`_

### [Example request](snippets/getMembershipInformation/example_request.py)

[embedmd]:# (snippets/getMembershipInformation/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_membership_information().get_result()

print(response)
```

## deleteReplicationDocument

_DELETE `/_replicator/{doc_id}`_

### [Example request](snippets/deleteReplicationDocument/example_request.py)

[embedmd]:# (snippets/deleteReplicationDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_replication_document(
doc_id='repldoc-example',
rev='3-a0ccbdc6fe95b4184f9031d086034d85'
).get_result()

print(response)
```

## getReplicationDocument

_GET `/_replicator/{doc_id}`_

### [Example request](snippets/getReplicationDocument/example_request.py)

[embedmd]:# (snippets/getReplicationDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_replication_document(
  doc_id='repldoc-example'
).get_result()

print(response)
```

## headReplicationDocument

_HEAD `/_replicator/{doc_id}`_

### [Example request](snippets/headReplicationDocument/example_request.py)

[embedmd]:# (snippets/headReplicationDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.head_replication_document(
 doc_id='repldoc-example'
)
print(response.get_status_code())
print(response.get_headers()['ETag'])
```

## putReplicationDocument

_PUT `/_replicator/{doc_id}`_

### [Example request](snippets/putReplicationDocument/example_request.py)

[embedmd]:# (snippets/putReplicationDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1, ReplicationDocument, ReplicationDatabase, ReplicationDatabaseAuthIam, ReplicationDatabaseAuth

service = CloudantV1.new_instance()

source_db = ReplicationDatabase(
  url='<your-source-service-url>/animaldb'
)

target_auth_iam = ReplicationDatabaseAuthIam(
  api_key='<your-iam-api-key>'
)
target_auth = ReplicationDatabaseAuth(
  iam=target_auth_iam
)
target_db = ReplicationDatabase(
  auth=target_auth,
  url='<your-target-service-url>/animaldb-target'
)

replication_document = ReplicationDocument(
  _id='repldoc-example',
  create_target=True,
  source=source_db,
  target=target_db
)

response = service.put_replication_document(
  doc_id='repldoc-example',
  replication_document=replication_document
).get_result()

print(response)
```

## getSchedulerDocs

_GET `/_scheduler/docs`_

### [Example request](snippets/getSchedulerDocs/example_request.py)

[embedmd]:# (snippets/getSchedulerDocs/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_scheduler_docs(
  limit=100,
  states=['completed']
).get_result()

print(response)
```

## getSchedulerDocument

_GET `/_scheduler/docs/_replicator/{doc_id}`_

### [Example request](snippets/getSchedulerDocument/example_request.py)

[embedmd]:# (snippets/getSchedulerDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_scheduler_document(doc_id='repldoc-example').get_result()

print(response)
```

## getSchedulerJobs

_GET `/_scheduler/jobs`_

### [Example request](snippets/getSchedulerJobs/example_request.py)

[embedmd]:# (snippets/getSchedulerJobs/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_scheduler_jobs(
  limit=100
).get_result()

print(response)
```

## getSchedulerJob

_GET `/_scheduler/jobs/{job_id}`_

### [Example request](snippets/getSchedulerJob/example_request.py)

[embedmd]:# (snippets/getSchedulerJob/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_scheduler_job(
  job_id='7b94915cd8c4a0173c77c55cd0443939+continuous'
).get_result()

print(response)
```

## headSchedulerJob

_HEAD `/_scheduler/jobs/{job_id}`_

### [Example request](snippets/headSchedulerJob/example_request.py)

[embedmd]:# (snippets/headSchedulerJob/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.head_scheduler_job(
  job_id='7b94915cd8c4a0173c77c55cd0443939+continuous'
).get_result()

print(response.get_status_code())
```

## postSearchAnalyze

_POST `/_search_analyze`_

### [Example request](snippets/postSearchAnalyze/example_request.py)

[embedmd]:# (snippets/postSearchAnalyze/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_search_analyze(
  analyzer='english',
  text='running is fun'
).get_result()

print(response)
```

## getSessionInformation

_GET `/_session`_

### [Example request](snippets/getSessionInformation/example_request.py)

[embedmd]:# (snippets/getSessionInformation/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_session_information().get_result()

print(response)
# section: markdown
# For more details on Session Authentication, see [Authentication.](#authentication)
```

## getUpInformation

_GET `/_up`_

### [Example request](snippets/getUpInformation/example_request.py)

[embedmd]:# (snippets/getUpInformation/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_up_information().get_result()

print(response)
```

## getUuids

_GET `/_uuids`_

### [Example request](snippets/getUuids/example_request.py)

[embedmd]:# (snippets/getUuids/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_uuids(count=10).get_result()

print(response)
```

## deleteDatabase

_DELETE `/{db}`_

### [Example request](snippets/deleteDatabase/example_request.py)

[embedmd]:# (snippets/deleteDatabase/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_database(db='<db-name>').get_result()

print(response)
```

## getDatabaseInformation

_GET `/{db}`_

### [Example request](snippets/getDatabaseInformation/example_request.py)

[embedmd]:# (snippets/getDatabaseInformation/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_database_information(db='products').get_result()

print(response)
```

## headDatabase

_HEAD `/{db}`_

### [Example request](snippets/headDatabase/example_request.py)

[embedmd]:# (snippets/headDatabase/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.head_database(db='products')
print(response.get_status_code())
```

## postDocument

_POST `/{db}`_

### [Example request](snippets/postDocument/example_request.py)

[embedmd]:# (snippets/postDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import Document, CloudantV1

service = CloudantV1.new_instance()

products_doc = Document(
  _id="small-appliances:1000042",
  type="product",
  productid="1000042",
  brand="Salter",
  name="Digital Kitchen Scales",
  description="Slim Colourful Design Electronic Cooking Appliance for Home / Kitchen, Weigh up to 5kg + Aquatronic for Liquids ml + fl. oz. 15Yr Guarantee - Green",
  price=14.99,
  image="assets/img/0gmsnghhew.jpg")

response = service.post_document(db='products', document=products_doc).get_result()

print(response)
```

## putDatabase

_PUT `/{db}`_

### [Example request](snippets/putDatabase/example_request.py)

[embedmd]:# (snippets/putDatabase/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.put_database(db='products', partitioned=True).get_result()

print(response)
```

## postAllDocs

_POST `/{db}/_all_docs`_

### [Example request](snippets/postAllDocs/example_request.py)

[embedmd]:# (snippets/postAllDocs/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_all_docs(
  db='orders',
  include_docs=True,
  start_key='abc',
  limit=10
).get_result()

print(response)
```

### [Example request as a stream](snippets/postAllDocs/example_request_as_a_stream.py)

[embedmd]:# (snippets/postAllDocs/example_request_as_a_stream.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

result = service.post_all_docs_as_stream(
  db='orders',
  include_docs=True,
  start_key='abc',
  limit=10
).get_result()

with open('result.json', 'wb') as f:
  for chunk in result.iter_content():
    f.write(chunk)
```

## postAllDocsQueries

_POST `/{db}/_all_docs/queries`_

### [Example request](snippets/postAllDocsQueries/example_request.py)

[embedmd]:# (snippets/postAllDocsQueries/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import AllDocsQuery, CloudantV1

service = CloudantV1.new_instance()

all_docs_query1 = AllDocsQuery(
  keys=['small-appliances:1000042', 'small-appliances:1000043']
)

all_docs_query2 = AllDocsQuery(
  limit=3,
  skip=2
)

response = service.post_all_docs_queries(
  db='products',
  queries=[all_docs_query1, all_docs_query2]
).get_result()

print(response)
```

## postBulkDocs

_POST `/{db}/_bulk_docs`_

### [Example request: create documents](snippets/postBulkDocs/example_request_create_documents.py)

[embedmd]:# (snippets/postBulkDocs/example_request_create_documents.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import Document, CloudantV1, BulkDocs

service = CloudantV1.new_instance()

event_doc_1 = Document(
  _id="0007241142412418284",
  type="event",
  userid="abc123",
  eventType="addedToBasket",
  productId="1000042",
  date="2019-01-28T10:44:22.000Z"
)
event_doc_2 = Document(
  _id="0007241142412418285",
  type="event",
  userid="abc234",
  eventType="addedToBasket",
  productId="1000050",
  date="2019-01-25T20:00:00.000Z"
)

bulk_docs = BulkDocs(docs=[event_doc_1, event_doc_2])

response = service.post_bulk_docs(
  db='events',
  bulk_docs=bulk_docs
).get_result()

print(response)
```

### [Example request: delete documents](snippets/postBulkDocs/example_request_delete_documents.py)

[embedmd]:# (snippets/postBulkDocs/example_request_delete_documents.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import Document, CloudantV1, BulkDocs

service = CloudantV1.new_instance()

event_doc_1 = Document(
  _id="0007241142412418284",
  _rev="1-5005d65514fe9e90f8eccf174af5dd64",
  _deleted=True,
)
event_doc_2 = Document(
  _id="0007241142412418285",
  _rev="1-2d7810b054babeda4812b3924428d6d6",
  _deleted=True,
)

bulk_docs = BulkDocs(docs=[event_doc_1, event_doc_2])

response = service.post_bulk_docs(
  db='events',
  bulk_docs=bulk_docs
).get_result()

print(response)
```

### [Example request as a stream](snippets/postBulkDocs/example_request_as_a_stream.py)

[embedmd]:# (snippets/postBulkDocs/example_request_as_a_stream.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import Document, CloudantV1

service = CloudantV1.new_instance()

with open('upload.json', 'rb') as f:
  response = service.post_bulk_docs(
    db='events',
    bulk_docs=f
  ).get_result()

print(response)
# section: markdown
# Content of upload.json
# section: code
{
  "docs": [
    {
      "_id": "0007241142412418284",
      "type": "event",
      "userid": "abc123",
      "eventType": "addedToBasket",
      "productId": "1000042",
      "date": "2019-01-28T10:44:22.000Z"
    },
    {
      "_id": "0007241142412418285",
      "type": "event",
      "userid": "abc123",
      "eventType": "addedToBasket",
      "productId": "1000050",
      "date": "2019-01-25T20:00:00.000Z"
    }
  ]
}
```

## postBulkGet

_POST `/{db}/_bulk_get`_

### [Example request](snippets/postBulkGet/example_request.py)

[embedmd]:# (snippets/postBulkGet/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import BulkGetQueryDocument, CloudantV1

service = CloudantV1.new_instance()

doc_id = 'order00067'
bulk_get_doc_1 = BulkGetQueryDocument(
    id=doc_id,
    rev='3-917fa2381192822767f010b95b45325b')
bulk_get_doc_2 = BulkGetQueryDocument(
    id=doc_id,
    rev='4-a5be949eeb7296747cc271766e9a498b')

response = service.post_bulk_get(
    db='orders',
    docs=[bulk_get_doc_1, bulk_get_doc_2],
).get_result()

print(response)
```

### [Alternative example request for `open_revs=all`](snippets/postBulkGet/alternative_example_request_for_open_revs_all.py)

[embedmd]:# (snippets/postBulkGet/alternative_example_request_for_open_revs_all.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import BulkGetQueryDocument, CloudantV1

service = CloudantV1.new_instance()

bulk_get_doc = BulkGetQueryDocument(id='order00067')
response = service.post_bulk_get(
    db='orders',
    docs=[bulk_get_doc],
).get_result()

print(response)
```

### [Alternative example request for `atts_since`](snippets/postBulkGet/alternative_example_request_for_atts_since.py)

[embedmd]:# (snippets/postBulkGet/alternative_example_request_for_atts_since.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import BulkGetQueryDocument, CloudantV1

service = CloudantV1.new_instance()

bulk_get_doc = BulkGetQueryDocument(
    id='order00058',
    atts_since=['1-99b02e08da151943c2dcb40090160bb8'])
response = service.post_bulk_get(
    db='orders',
    docs=[bulk_get_doc]
).get_result()

print(response)
```

## postChanges

_POST `/{db}/_changes`_

### [Example request](snippets/postChanges/example_request.py)

[embedmd]:# (snippets/postChanges/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()
response = service.post_changes(
  db='orders'
).get_result()

print(response)
```

### [Example request as a stream](snippets/postChanges/example_request_as_a_stream.py)

[embedmd]:# (snippets/postChanges/example_request_as_a_stream.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

result = service.post_changes_as_stream(
  db='orders'
).get_result()

with open('result.json', 'wb') as f:
  for chunk in result.iter_content():
    f.write(chunk)
```

## deleteDesignDocument

_DELETE `/{db}/_design/{ddoc}`_

### [Example request](snippets/deleteDesignDocument/example_request.py)

[embedmd]:# (snippets/deleteDesignDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_design_document(
  db='products',
  ddoc='appliances',
  rev='1-98e6a25b3b45df62e7d47095ac15b16a'
).get_result()

print(response)
```

## getDesignDocument

_GET `/{db}/_design/{ddoc}`_

### [Example request](snippets/getDesignDocument/example_request.py)

[embedmd]:# (snippets/getDesignDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_design_document(
  db='products',
  ddoc='appliances',
  latest=True
).get_result()

print(response)
```

## headDesignDocument

_HEAD `/{db}/_design/{ddoc}`_

### [Example request](snippets/headDesignDocument/example_request.py)

[embedmd]:# (snippets/headDesignDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.head_design_document(
  db='products',
  ddoc='appliances'
)
print(response.get_status_code())
print(response.get_headers()['ETag'])
```

## putDesignDocument

_PUT `/{db}/_design/{ddoc}`_

### [Example request](snippets/putDesignDocument/example_request.py)

[embedmd]:# (snippets/putDesignDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import Analyzer, AnalyzerConfiguration, CloudantV1, DesignDocument, DesignDocumentOptions, DesignDocumentViewsMapReduce, SearchIndexDefinition

service = CloudantV1.new_instance()

email_view_map_reduce = DesignDocumentViewsMapReduce(
  map='function(doc) { if(doc.email_verified  === true){\n  emit(doc.email, [doc.name, doc.email_verified, doc.joined]) }}'
)

user_index = SearchIndexDefinition(
  index='function (doc) { index("name", doc.name); index("active", doc.active); }',
  analyzer=AnalyzerConfiguration(name="standard", fields={"email": Analyzer(name="email")}))

design_document = DesignDocument(
  views={'getVerifiedEmails': email_view_map_reduce},
  indexes={'activeUsers': user_index}
)

response = service.put_design_document(
  db='users',
  design_document=design_document,
  ddoc='allusers'
).get_result()

print(response)

# Partitioned DesignDocument Example

product_map = DesignDocumentViewsMapReduce(
  map='function(doc) { emit(doc.productId, [doc.brand, doc.name, doc.description]) }'
)

price_index = SearchIndexDefinition(
  index='function (doc) { index("price", doc.price);}',
  analyzer=AnalyzerConfiguration(name="classic", fields={"description": Analyzer(name="english")})
)

design_document_options = DesignDocumentOptions(
  partitioned=True
)

partitioned_design_doc = DesignDocument(
  views={'byApplianceProdId': product_map},
  indexes={'findByPrice': price_index},
  options=design_document_options
)

response = service.put_design_document(
  db='products',
  design_document=partitioned_design_doc,
  ddoc='appliances'
).get_result()

print(response)
# section: markdown
# This example creates `allusers` design document in the `users` database and `appliances` design document in the partitioned `products` database.
```

## getDesignDocumentInformation

_GET `/{db}/_design/{ddoc}/_info`_

### [Example request](snippets/getDesignDocumentInformation/example_request.py)

[embedmd]:# (snippets/getDesignDocumentInformation/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_design_document_information(
  db='products',
  ddoc='appliances'
).get_result()

print(response)
```

## postSearch

_POST `/{db}/_design/{ddoc}/_search/{index}`_

### [Example request](snippets/postSearch/example_request.py)

[embedmd]:# (snippets/postSearch/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_search(
  db='users',
  ddoc='allusers',
  index='activeUsers',
  query='name:Jane* AND active:True'
).get_result()

print(response)
# section: markdown
# This example requires the `activeUsers` Cloudant Search index to exist. To create the design document with this index, see [Create or modify a design document.](#putdesigndocument)
```

## getSearchInfo

_GET `/{db}/_design/{ddoc}/_search_info/{index}`_

### [Example request](snippets/getSearchInfo/example_request.py)

[embedmd]:# (snippets/getSearchInfo/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_search_info(
  db='products',
  ddoc='appliances',
  index='findByPrice'
).get_result()

print(response)
# section: markdown
# This example requires the `findByPrice` Cloudant Search partitioned index to exist. To create the design document with this index, see [Create or modify a design document.](#putdesigndocument)
```

## postView

_POST `/{db}/_design/{ddoc}/_view/{view}`_

### [Example request](snippets/postView/example_request.py)

[embedmd]:# (snippets/postView/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_view(
  db='users',
  ddoc='allusers',
  view='getVerifiedEmails'
).get_result()

print(response)
# section: markdown
# This example requires the `getVerifiedEmails` view to exist. To create the design document with this view, see [Create or modify a design document.](#putdesigndocument)
```

## postViewQueries

_POST `/{db}/_design/{ddoc}/_view/{view}/queries`_

### [Example request](snippets/postViewQueries/example_request.py)

[embedmd]:# (snippets/postViewQueries/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1, ViewQuery

service = CloudantV1.new_instance()

query1 = ViewQuery(
  include_docs=True,
  limit=5
)
query2 = ViewQuery(
  descending=True,
  skip=1
)

response = service.post_view_queries(
  db='users',
  ddoc='allusers',
  queries=[query1, query2],
  view='getVerifiedEmails'
).get_result()

print(response)
# section: markdown
# This example requires the `getVerifiedEmails` view to exist. To create the design document with this view, see [Create or modify a design document.](#putdesigndocument)
```

## postDesignDocs

_POST `/{db}/_design_docs`_

### [Example request](snippets/postDesignDocs/example_request.py)

[embedmd]:# (snippets/postDesignDocs/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_design_docs(
  attachments=True,
  db='users'
).get_result()

print(response)
```

## postDesignDocsQueries

_POST `/{db}/_design_docs/queries`_

### [Example request](snippets/postDesignDocsQueries/example_request.py)

[embedmd]:# (snippets/postDesignDocsQueries/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import AllDocsQuery, CloudantV1

service = CloudantV1.new_instance()

doc1 = AllDocsQuery(
  descending=True,
  include_docs=True,
  limit=10
)
doc2 = AllDocsQuery(
  inclusive_end=True,
  key='_design/allusers',
  skip=1
)

response = service.post_design_docs_queries(
  db='users',
  queries=[doc1, doc2]
).get_result()

print(response)
```

## postExplain

_POST `/{db}/_explain`_

### [Example request](snippets/postExplain/example_request.py)

[embedmd]:# (snippets/postExplain/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_explain(
  db='users',
  execution_stats=True,
  limit=10,
  selector={'type': {"$eq": "user"}}
).get_result()

print(response)
```

## postFind

_POST `/{db}/_find`_

### [Example request for "json" index type](snippets/postFind/example_request_for_json_index_type.py)

[embedmd]:# (snippets/postFind/example_request_for_json_index_type.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_find(
  db='users',
  selector={'email_verified': {'$eq': True}},
  fields=["_id", "type", "name", "email"],
  sort=[{'email': 'desc'}],
  limit=3
).get_result()
print(response)
# section: markdown
# This example requires the `getUserByAddress` Cloudant Query "json" index to exist. To create the index, see [Create a new index on a database.](#postindex)
```

### [Example request for "text" index type](snippets/postFind/example_request_for_text_index_type.py)

[embedmd]:# (snippets/postFind/example_request_for_text_index_type.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_find(
  db='users',
  selector={'address': {'$regex': 'Street'}},
  fields=["_id", "type", "name", "email", "address"],
  limit=3
).get_result()
print(response)
# section: markdown
# This example requires the `getUserByVerifiedEmail` Cloudant Query "text" index to exist. To create the index, see [Create a new index on a database.](#postindex)
```

## getIndexesInformation

_GET `/{db}/_index`_

### [Example request](snippets/getIndexesInformation/example_request.py)

[embedmd]:# (snippets/getIndexesInformation/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_indexes_information(
  db='users'
).get_result()

print(response)
```

## postIndex

_POST `/{db}/_index`_

### [Example request using "json" type index](snippets/postIndex/example_request_using_json_type_index.py)

[embedmd]:# (snippets/postIndex/example_request_using_json_type_index.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1, IndexDefinition, IndexField

service = CloudantV1.new_instance()

# Type "json" index fields require an object that maps the name of a field to a sort direction.
index_field = IndexField(
  email="asc"
)
index = IndexDefinition(
  fields=[index_field]
)

response = service.post_index(
  db='users',
  ddoc='json-index',
  name='getUserByEmail',
  index=index,
  type='json'
).get_result()

print(response)
```

### [Example request using "text" type index](snippets/postIndex/example_request_using_text_type_index.py)

[embedmd]:# (snippets/postIndex/example_request_using_text_type_index.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1, IndexDefinition, IndexField

service = CloudantV1.new_instance()

# Type "text" index fields require an object with a name and type properties for the field.
index_field = IndexField(
  name="address",
  type="string"
)
index = IndexDefinition(
  fields=[index_field]
)

response = service.post_index(
  db='users',
  ddoc='text-index',
  name='getUserByAddress',
  index=index,
  type='text'
).get_result()

print(response)
```

## deleteIndex

_DELETE `/{db}/_index/_design/{ddoc}/{type}/{index}`_

### [Example request](snippets/deleteIndex/example_request.py)

[embedmd]:# (snippets/deleteIndex/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_index(
  db='users',
  ddoc='json-index',
  index='getUserByName',
  type='json'
).get_result()

print(response)
# section: markdown
# This example will fail if `getUserByName` index doesn't exist. To create the index, see [Create a new index on a database.](#postindex)
```

## deleteLocalDocument

_DELETE `/{db}/_local/{doc_id}`_

### [Example request](snippets/deleteLocalDocument/example_request.py)

[embedmd]:# (snippets/deleteLocalDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_local_document(
  db='orders',
  doc_id='local-0007741142412418284'
).get_result()

print(response)
```

## getLocalDocument

_GET `/{db}/_local/{doc_id}`_

### [Example request](snippets/getLocalDocument/example_request.py)

[embedmd]:# (snippets/getLocalDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_local_document(
  db='orders',
  doc_id='local-0007741142412418284'
).get_result()

print(response)
```

## putLocalDocument

_PUT `/{db}/_local/{doc_id}`_

### [Example request](snippets/putLocalDocument/example_request.py)

[embedmd]:# (snippets/putLocalDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import Document, CloudantV1

service = CloudantV1.new_instance()

local_document = Document(
   type='order',
   user='Bob Smith',
   orderid='0007741142412418284',
   userid='abc123',
   total=214.98,
   deliveryAddress='19 Front Street, Darlington, DL5 1TY',
   delivered='true',
   courier='UPS',
   courierid='15125425151261289',
   date='2019-01-28T10:44:22.000Z'
)

response = service.put_local_document(
  db='orders',
  doc_id='local-0007741142412418284',
  document=local_document,
).get_result()

print(response)
```

## postMissingRevs

_POST `/{db}/_missing_revs`_

### [Example request](snippets/postMissingRevs/example_request.py)

[embedmd]:# (snippets/postMissingRevs/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import DocumentRevisions, CloudantV1

service = CloudantV1.new_instance()

revs = DocumentRevisions(order00077=['<order00077-existing-revision>', '<2-missing-revision>'])
response = service.post_missing_revs(
  db='orders',
  missing_revs=revs.to_dict()
).get_result()

print(response)
```

## getPartitionInformation

_GET `/{db}/_partition/{partition_key}`_

### [Example request](snippets/getPartitionInformation/example_request.py)

[embedmd]:# (snippets/getPartitionInformation/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_partition_information(
  db='products',
  partition_key='small-appliances'
).get_result()

print(response)
```

## postPartitionAllDocs

_POST `/{db}/_partition/{partition_key}/_all_docs`_

### [Example request](snippets/postPartitionAllDocs/example_request.py)

[embedmd]:# (snippets/postPartitionAllDocs/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_partition_all_docs(
  db='products',
  partition_key='small-appliances',
  include_docs=True
).get_result()

print(response)
```

## postPartitionSearch

_POST `/{db}/_partition/{partition_key}/_design/{ddoc}/_search/{index}`_

### [Example request](snippets/postPartitionSearch/example_request.py)

[embedmd]:# (snippets/postPartitionSearch/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_partition_search(
  db='products',
  partition_key='small-appliances',
  ddoc='appliances',
  index='findByPrice',
  query='price:[14 TO 20]'
).get_result()

print(response)
# section: markdown
# This example requires the `findByPrice` Cloudant Search partitioned index to exist. To create the design document with this index, see [Create or modify a design document.](#putdesigndocument)
```

## postPartitionView

_POST `/{db}/_partition/{partition_key}/_design/{ddoc}/_view/{view}`_

### [Example request](snippets/postPartitionView/example_request.py)

[embedmd]:# (snippets/postPartitionView/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_partition_view(
  db='products',
  ddoc='appliances',
  limit=10,
  partition_key='small-appliances',
  view='byApplianceProdId'
).get_result()

print(response)
# section: markdown
# This example requires the `byApplianceProdId` partitioned view to exist. To create the design document with this view, see [Create or modify a design document.](#putdesigndocument)
```

## postPartitionFind

_POST `/{db}/_partition/{partition_key}/_find`_

### [Example request](snippets/postPartitionFind/example_request.py)

[embedmd]:# (snippets/postPartitionFind/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_partition_find(
  db='products',
  partition_key='small-appliances',
  fields=['productid', 'name', 'description'],
  selector={'type': {'$eq': 'product'}}
).get_result()

print(response)
```

## postRevsDiff

_POST `/{db}/_revs_diff`_

### [Example request](snippets/postRevsDiff/example_request.py)

[embedmd]:# (snippets/postRevsDiff/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import DocumentRevisions, CloudantV1

service = CloudantV1.new_instance()

revs_diff = DocumentRevisions(
  order00077=[
      "<1-missing-revision>",
      "<2-missing-revision>",
      "<3-possible-ancestor-revision>"
]
)

response = service.post_revs_diff(
  db='orders',
  revs_diff_request=revs_diff.to_dict()
).get_result()

print(response)
```

## getSecurity

_GET `/{db}/_security`_

### [Example request](snippets/getSecurity/example_request.py)

[embedmd]:# (snippets/getSecurity/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_security(
  db='products'
).get_result()

print(response)
```

## putSecurity

_PUT `/{db}/_security`_

### [Example request](snippets/putSecurity/example_request.py)

[embedmd]:# (snippets/putSecurity/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1, SecurityObject

service = CloudantV1.new_instance()

members = SecurityObject(
  names=['user1', 'user2'],
  roles=['developers']
)

response = service.put_security(
  db='products',
  members=members
).get_result()

print(response)
# section: markdown
# The `nobody` username applies to all unauthenticated connection attempts. For example, if an application tries to read data from a database, but didn't identify itself, the task can continue only if the `nobody` user has the role `_reader`.
# section: markdown
# If instead of using Cloudant's security model for managing permissions you opt to use the Apache CouchDB `_users` database (that is using legacy credentials _and_ the `couchdb_auth_only:true` option) then be aware that the user must already exist in `_users` database before adding permissions. For information on the `_users` database, see <a href="https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-work-with-your-account#using-the-users-database-with-cloudant-nosql-db" target="_blank">Using the `_users` database with Cloudant</a>.
```

## getShardsInformation

_GET `/{db}/_shards`_

### [Example request](snippets/getShardsInformation/example_request.py)

[embedmd]:# (snippets/getShardsInformation/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_shards_information(
  db='products'
).get_result()

print(response)
```

## getDocumentShardsInfo

_GET `/{db}/_shards/{doc_id}`_

### [Example request](snippets/getDocumentShardsInfo/example_request.py)

[embedmd]:# (snippets/getDocumentShardsInfo/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_document_shards_info(
  db='products',
  doc_id='small-appliances:1000042'
).get_result()

print(response)
```

## deleteDocument

_DELETE `/{db}/{doc_id}`_

### [Example request](snippets/deleteDocument/example_request.py)

[embedmd]:# (snippets/deleteDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_document(
  db='events',
  doc_id='0007241142412418284',
  rev='2-9a0d1cd9f40472509e9aac6461837367'
).get_result()

print(response)
```

## getDocument

_GET `/{db}/{doc_id}`_

### [Example request](snippets/getDocument/example_request.py)

[embedmd]:# (snippets/getDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_document(
  db='products',
  doc_id='small-appliances:1000042'
).get_result()

print(response)
```

## headDocument

_HEAD `/{db}/{doc_id}`_

### [Example request](snippets/headDocument/example_request.py)

[embedmd]:# (snippets/headDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.head_document(
  db='events',
  doc_id='0007241142412418284'
)
print(response.get_status_code())
print(response.get_headers()['ETag'])
```

## putDocument

_PUT `/{db}/{doc_id}`_

### [Example request](snippets/putDocument/example_request.py)

[embedmd]:# (snippets/putDocument/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import Document, CloudantV1

service = CloudantV1.new_instance()

event_doc = Document(
  type='event',
  userid='abc123',
  eventType='addedToBasket',
  productId='1000042',
  date='2019-01-28T10:44:22.000Z'
)
response = service.put_document(
  db='events',
  doc_id='0007241142412418284',
  document=event_doc
).get_result()

print(response)
```

## deleteAttachment

_DELETE `/{db}/{doc_id}/{attachment_name}`_

### [Example request](snippets/deleteAttachment/example_request.py)

[embedmd]:# (snippets/deleteAttachment/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_attachment(
  db='products',
  doc_id='small-appliances:100001',
  attachment_name='product_details.txt',
  rev='4-1a0d1cd6f40472509e9aac646183736a'
).get_result()

print(response)
# section: markdown
# This example requires the `product_details.txt` attachment in `small-appliances:100001` document to exist. To create the attachment, see [Create or modify an attachment.](#putattachment)
```

## getAttachment

_GET `/{db}/{doc_id}/{attachment_name}`_

### [Example request](snippets/getAttachment/example_request.py)

[embedmd]:# (snippets/getAttachment/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response_attachment = service.get_attachment(
  db='products',
  doc_id='small-appliances:100001',
  attachment_name='product_details.txt'
).get_result().content

print(response_attachment)
# section: markdown
# This example requires the `product_details.txt` attachment in `small-appliances:100001` document to exist. To create the attachment, see [Create or modify an attachment.](#putattachment)
```

## headAttachment

_HEAD `/{db}/{doc_id}/{attachment_name}`_

### [Example request](snippets/headAttachment/example_request.py)

[embedmd]:# (snippets/headAttachment/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.head_attachment(
  db='products',
  doc_id='small-appliances:100001',
  attachment_name='product_details.txt'
)
print(response.get_status_code())
print(response.get_headers()['Content-Length'])
print(response.get_headers()['Content-Type'])
# section: markdown
# This example requires the `product_details.txt` attachment in `small-appliances:100001` document to exist. To create the attachment, see [Create or modify an attachment.](#putattachment)
```

## putAttachment

_PUT `/{db}/{doc_id}/{attachment_name}`_

### [Example request](snippets/putAttachment/example_request.py)

[embedmd]:# (snippets/putAttachment/example_request.py)
```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

detailed_description = "This appliance includes..."
response = service.put_attachment(
  db='products',
  doc_id='small-appliances:100001',
  attachment_name='product_details.txt',
  attachment=detailed_description,
  content_type='text/plain'
).get_result()

print(response)
```
