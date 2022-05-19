# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_document(
  db='events',
  doc_id='0007241142412418284',
  rev='2-9a0d1cd9f40472509e9aac6461837367'
).get_result()

print(response)
