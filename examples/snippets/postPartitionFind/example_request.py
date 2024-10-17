# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_partition_find(
  db='events',
  partition_key='ns1HJS13AMkK',
  fields=['productId', 'eventType', 'date'],
  selector={'userId': {'$eq': 'abc123'}}
).get_result()

print(response)
