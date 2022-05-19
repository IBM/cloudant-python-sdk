# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_design_document(
  db='products',
  ddoc='appliances',
  rev='1-98e6a25b3b45df62e7d47095ac15b16a'
).get_result()

print(response)
