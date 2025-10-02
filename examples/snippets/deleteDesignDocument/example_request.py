# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_design_document(
  db='products',
  ddoc='appliances',
  rev='1-00000000000000000000000000000000'
).get_result()

print(response)
