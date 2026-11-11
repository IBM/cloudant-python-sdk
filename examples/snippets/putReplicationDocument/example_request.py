# section: code
from ibmcloudant.cloudant_v1 import CloudantV1, ReplicationDocument, ReplicationDatabase, ReplicationDatabaseAuthIBMIam, ReplicationDatabaseAuthIBM, ReplicationDatabaseAuth

service = CloudantV1.new_instance()

source_db = ReplicationDatabase(
  url='https://~replace-with-source-host~.cloudantnosqldb.appdomain.cloud/animaldb'
)

target_auth_ibm_iam = ReplicationDatabaseAuthIBMIam(
  api_key='a1b2c3d4e5f6f1g4h7j3k6l9m2p5q8s1t4v7x0z3' #use your own IAM API key
)
target_auth_ibm = ReplicationDatabaseAuthIBM(
  iam=target_auth_ibm_iam
)
target_auth = ReplicationDatabaseAuth(
  ibm=target_auth_ibm
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
