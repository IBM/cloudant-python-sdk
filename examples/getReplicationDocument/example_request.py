# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_replication_document(
  doc_id='repldoc-example'
).get_result()

print(response)
