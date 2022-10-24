# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_replication_document(
doc_id='repldoc-example',
rev='3-a0ccbdc6fe95b4184f9031d086034d85'
).get_result()

print(response)
