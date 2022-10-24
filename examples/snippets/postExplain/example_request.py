# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_explain(
  db='users',
  execution_stats=True,
  limit=10,
  selector={'type': {"$eq": "user"}}
).get_result()

print(response)
