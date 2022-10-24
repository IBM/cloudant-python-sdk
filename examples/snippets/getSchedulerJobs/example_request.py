# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_scheduler_jobs(
  limit=100
).get_result()

print(response)
