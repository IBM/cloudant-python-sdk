# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_design_document_information(
  db='products',
  ddoc='appliances'
).get_result()

print(response)
