# Examples for python

## getServerInformation

### get `/`

- [Example request](./getServerInformation/example_request.py)

## getActiveTasks

### get `/_active_tasks`

- [Example request](./getActiveTasks/example_request.py)

## getAllDbs

### get `/_all_dbs`

- [Example request](./getAllDbs/example_request.py)

## postApiKeys

### post `/_api/v2/api_keys`

- [Example request](./postApiKeys/example_request.py)

## putCloudantSecurity

### put `/_api/v2/db/{db}/_security`

- [Example request](./putCloudantSecurity/example_request.py)

## getActivityTrackerEvents

### get `/_api/v2/user/activity_tracker/events`

- [Example request](./getActivityTrackerEvents/example_request.py)

## postActivityTrackerEvents

### post `/_api/v2/user/activity_tracker/events`

- [Example request](./postActivityTrackerEvents/example_request.py)

## getCapacityThroughputInformation

### get `/_api/v2/user/capacity/throughput`

- [Example request](./getCapacityThroughputInformation/example_request.py)

## putCapacityThroughputConfiguration

### put `/_api/v2/user/capacity/throughput`

- [Example request](./putCapacityThroughputConfiguration/example_request.py)

## getCorsInformation

### get `/_api/v2/user/config/cors`

- [Example request](./getCorsInformation/example_request.py)

## putCorsConfiguration

### put `/_api/v2/user/config/cors`

- [Example request](./putCorsConfiguration/example_request.py)

## getCurrentThroughputInformation

### get `/_api/v2/user/current/throughput`

- [Example request](./getCurrentThroughputInformation/example_request.py)

## getDbUpdates

### get `/_db_updates`

- [Example request](./getDbUpdates/example_request.py)

## postDbsInfo

### post `/_dbs_info`

- [Example request](./postDbsInfo/example_request.py)

## getMembershipInformation

### get `/_membership`

- [Example request](./getMembershipInformation/example_request.py)

## deleteReplicationDocument

### delete `/_replicator/{doc_id}`

- [Example request](./deleteReplicationDocument/example_request.py)

## getReplicationDocument

### get `/_replicator/{doc_id}`

- [Example request](./getReplicationDocument/example_request.py)

## headReplicationDocument

### head `/_replicator/{doc_id}`

- [Example request](./headReplicationDocument/example_request.py)

## putReplicationDocument

### put `/_replicator/{doc_id}`

- [Example request](./putReplicationDocument/example_request.py)

## getSchedulerDocs

### get `/_scheduler/docs`

- [Example request](./getSchedulerDocs/example_request.py)

## getSchedulerDocument

### get `/_scheduler/docs/_replicator/{doc_id}`

- [Example request](./getSchedulerDocument/example_request.py)

## getSchedulerJobs

### get `/_scheduler/jobs`

- [Example request](./getSchedulerJobs/example_request.py)

## getSchedulerJob

### get `/_scheduler/jobs/{job_id}`

- [Example request](./getSchedulerJob/example_request.py)

## headSchedulerJob

### head `/_scheduler/jobs/{job_id}`

- [Example request](./headSchedulerJob/example_request.py)

## postSearchAnalyze

### post `/_search_analyze`

- [Example request](./postSearchAnalyze/example_request.py)

## getSessionInformation

### get `/_session`

- [Example request](./getSessionInformation/example_request.py)

## getUpInformation

### get `/_up`

- [Example request](./getUpInformation/example_request.py)

## getUuids

### get `/_uuids`

- [Example request](./getUuids/example_request.py)

## deleteDatabase

### delete `/{db}`

- [Example request](./deleteDatabase/example_request.py)

## getDatabaseInformation

### get `/{db}`

- [Example request](./getDatabaseInformation/example_request.py)

## headDatabase

### head `/{db}`

- [Example request](./headDatabase/example_request.py)

## postDocument

### post `/{db}`

- [Example request](./postDocument/example_request.py)

## putDatabase

### put `/{db}`

- [Example request](./putDatabase/example_request.py)

## postAllDocs

### post `/{db}/_all_docs`

- [Example request](./postAllDocs/example_request.py)
- [Example request as a stream](./postAllDocs/example_request_as_a_stream.py)

## postAllDocsQueries

### post `/{db}/_all_docs/queries`

- [Example request](./postAllDocsQueries/example_request.py)

## postBulkDocs

### post `/{db}/_bulk_docs`

- [Example request: create documents](./postBulkDocs/example_request_create_documents.py)
- [Example request: delete documents](./postBulkDocs/example_request_delete_documents.py)
- [Example request as a stream](./postBulkDocs/example_request_as_a_stream.py)

## postBulkGet

### post `/{db}/_bulk_get`

- [Example request](./postBulkGet/example_request.py)
- [Alternative example request for `open_revs=all`](./postBulkGet/alternative_example_request_for_open_revs_all.py)
- [Alternative example request for `atts_since`](./postBulkGet/alternative_example_request_for_atts_since.py)

## postChanges

### post `/{db}/_changes`

- [Example request](./postChanges/example_request.py)
- [Example request as a stream](./postChanges/example_request_as_a_stream.py)

## deleteDesignDocument

### delete `/{db}/_design/{ddoc}`

- [Example request](./deleteDesignDocument/example_request.py)

## getDesignDocument

### get `/{db}/_design/{ddoc}`

- [Example request](./getDesignDocument/example_request.py)

## headDesignDocument

### head `/{db}/_design/{ddoc}`

- [Example request](./headDesignDocument/example_request.py)

## putDesignDocument

### put `/{db}/_design/{ddoc}`

- [Example request](./putDesignDocument/example_request.py)

## getDesignDocumentInformation

### get `/{db}/_design/{ddoc}/_info`

- [Example request](./getDesignDocumentInformation/example_request.py)

## postSearch

### post `/{db}/_design/{ddoc}/_search/{index}`

- [Example request](./postSearch/example_request.py)

## getSearchInfo

### get `/{db}/_design/{ddoc}/_search_info/{index}`

- [Example request](./getSearchInfo/example_request.py)

## postView

### post `/{db}/_design/{ddoc}/_view/{view}`

- [Example request](./postView/example_request.py)

## postViewQueries

### post `/{db}/_design/{ddoc}/_view/{view}/queries`

- [Example request](./postViewQueries/example_request.py)

## postDesignDocs

### post `/{db}/_design_docs`

- [Example request](./postDesignDocs/example_request.py)

## postDesignDocsQueries

### post `/{db}/_design_docs/queries`

- [Example request](./postDesignDocsQueries/example_request.py)

## postExplain

### post `/{db}/_explain`

- [Example request](./postExplain/example_request.py)

## postFind

### post `/{db}/_find`

- [Example request for "json" index type](./postFind/example_request_for_json_index_type.py)
- [Example request for "text" index type](./postFind/example_request_for_text_index_type.py)

## getIndexesInformation

### get `/{db}/_index`

- [Example request](./getIndexesInformation/example_request.py)

## postIndex

### post `/{db}/_index`

- [Example request using "json" type index](./postIndex/example_request_using_json_type_index.py)
- [Example request using "text" type index](./postIndex/example_request_using_text_type_index.py)

## deleteIndex

### delete `/{db}/_index/_design/{ddoc}/{type}/{index}`

- [Example request](./deleteIndex/example_request.py)

## deleteLocalDocument

### delete `/{db}/_local/{doc_id}`

- [Example request](./deleteLocalDocument/example_request.py)

## getLocalDocument

### get `/{db}/_local/{doc_id}`

- [Example request](./getLocalDocument/example_request.py)

## putLocalDocument

### put `/{db}/_local/{doc_id}`

- [Example request](./putLocalDocument/example_request.py)

## postMissingRevs

### post `/{db}/_missing_revs`

- [Example request](./postMissingRevs/example_request.py)

## getPartitionInformation

### get `/{db}/_partition/{partition_key}`

- [Example request](./getPartitionInformation/example_request.py)

## postPartitionAllDocs

### post `/{db}/_partition/{partition_key}/_all_docs`

- [Example request](./postPartitionAllDocs/example_request.py)

## postPartitionSearch

### post `/{db}/_partition/{partition_key}/_design/{ddoc}/_search/{index}`

- [Example request](./postPartitionSearch/example_request.py)

## postPartitionView

### post `/{db}/_partition/{partition_key}/_design/{ddoc}/_view/{view}`

- [Example request](./postPartitionView/example_request.py)

## postPartitionFind

### post `/{db}/_partition/{partition_key}/_find`

- [Example request](./postPartitionFind/example_request.py)

## postRevsDiff

### post `/{db}/_revs_diff`

- [Example request](./postRevsDiff/example_request.py)

## getSecurity

### get `/{db}/_security`

- [Example request](./getSecurity/example_request.py)

## putSecurity

### put `/{db}/_security`

- [Example request](./putSecurity/example_request.py)

## getShardsInformation

### get `/{db}/_shards`

- [Example request](./getShardsInformation/example_request.py)

## getDocumentShardsInfo

### get `/{db}/_shards/{doc_id}`

- [Example request](./getDocumentShardsInfo/example_request.py)

## deleteDocument

### delete `/{db}/{doc_id}`

- [Example request](./deleteDocument/example_request.py)

## getDocument

### get `/{db}/{doc_id}`

- [Example request](./getDocument/example_request.py)

## headDocument

### head `/{db}/{doc_id}`

- [Example request](./headDocument/example_request.py)

## putDocument

### put `/{db}/{doc_id}`

- [Example request](./putDocument/example_request.py)

## deleteAttachment

### delete `/{db}/{doc_id}/{attachment_name}`

- [Example request](./deleteAttachment/example_request.py)

## getAttachment

### get `/{db}/{doc_id}/{attachment_name}`

- [Example request](./getAttachment/example_request.py)

## headAttachment

### head `/{db}/{doc_id}/{attachment_name}`

- [Example request](./headAttachment/example_request.py)

## putAttachment

### put `/{db}/{doc_id}/{attachment_name}`

- [Example request](./putAttachment/example_request.py)
