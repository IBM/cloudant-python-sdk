# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.head_design_document(
  db='events',
  ddoc='checkout'
)
print(response.get_status_code())
print(response.get_headers()['ETag'])
