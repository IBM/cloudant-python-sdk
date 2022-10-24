# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_document_shards_info(
  db='products',
  doc_id='small-appliances:1000042'
).get_result()

print(response)
