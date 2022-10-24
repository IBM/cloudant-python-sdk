# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_scheduler_docs(
  limit=100,
  states=['completed']
).get_result()

print(response)
