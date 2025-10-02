# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_document(
  db='orders',
  doc_id='order00058',
  rev='1-00000000000000000000000000000000'
).get_result()

print(response)
