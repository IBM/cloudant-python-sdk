# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_replication_document(
doc_id='repldoc-example',
rev='1-00000000000000000000000000000000'
).get_result()

print(response)
