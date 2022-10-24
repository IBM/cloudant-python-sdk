# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_design_document(
  db='products',
  ddoc='appliances',
  latest=True
).get_result()

print(response)
