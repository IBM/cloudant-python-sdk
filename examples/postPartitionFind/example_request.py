# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_partition_find(
  db='products',
  partition_key='small-appliances',
  fields=['productid', 'name', 'description'],
  selector={'type': {'$eq': 'product'}}
).get_result()

print(response)
