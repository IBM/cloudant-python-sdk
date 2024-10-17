# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_partition_explain(
  db='events',
  execution_stats=True,
  limit=10,
  partition_key='ns1HJS13AMkK',
  selector={'userId': {'$eq': 'abc123'}}
).get_result()

print(response)
