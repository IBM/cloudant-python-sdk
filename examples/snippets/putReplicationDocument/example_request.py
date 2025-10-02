# section: code
from ibmcloudant.cloudant_v1 import CloudantV1, ReplicationDocument, ReplicationDatabase, ReplicationDatabaseAuthIam, ReplicationDatabaseAuth

service = CloudantV1.new_instance()

source_db = ReplicationDatabase(
  url='https://~replace-with-source-host~.cloudantnosqldb.appdomain.cloud/animaldb'
)

target_auth_iam = ReplicationDatabaseAuthIam(
  api_key='a1b2c3d4e5f6f1g4h7j3k6l9m2p5q8s1t4v7x0z3' #use your own IAM API key
)
target_auth = ReplicationDatabaseAuth(
  iam=target_auth_iam
)
target_db = ReplicationDatabase(
  auth=target_auth,
  url='https://~replace-with-target-host~.cloudantnosqldb.appdomain.cloud/animaldb-target'
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
