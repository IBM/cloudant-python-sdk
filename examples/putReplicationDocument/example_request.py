# section: code
from ibmcloudant.cloudant_v1 import CloudantV1, ReplicationDocument, ReplicationDatabase, ReplicationDatabaseAuthIam, ReplicationDatabaseAuth

service = CloudantV1.new_instance()

source_db = ReplicationDatabase(
  url='https://examples.cloudant.com/animaldb'
)

target_auth_iam = ReplicationDatabaseAuthIam(
  api_key='<your-iam-api-key>'
)
target_auth = ReplicationDatabaseAuth(
  iam=target_auth_iam
)
target_db = ReplicationDatabase(
  auth=target_auth,
  url='<your-service-url>/animaldb-target'
)

replication_document = ReplicationDocument(
  id='repldoc-example',
  create_target=True,
  source=source_db,
  target=target_db
)

response = service.put_replication_document(
  doc_id='repldoc-example',
  replication_document=replication_document
).get_result()

print(response)
