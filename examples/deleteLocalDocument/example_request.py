# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_local_document(
  db='orders',
  doc_id='local-0007741142412418284'
).get_result()

print(response)
