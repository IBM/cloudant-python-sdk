# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.head_document(
  db='events',
  doc_id='0007241142412418284'
)
print(response.get_status_code())
print(response.get_headers()['ETag'])
