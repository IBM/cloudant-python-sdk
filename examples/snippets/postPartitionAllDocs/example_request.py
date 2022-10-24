# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_partition_all_docs(
  db='products',
  partition_key='small-appliances',
  include_docs=True
).get_result()

print(response)
