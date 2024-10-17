# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_document(
  db='orders',
  doc_id='order00058',
  rev='1-99b02e08da151943c2dcb40090160bb8'
).get_result()

print(response)
