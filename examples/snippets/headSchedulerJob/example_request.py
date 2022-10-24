# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.head_scheduler_job(
  job_id='7b94915cd8c4a0173c77c55cd0443939+continuous'
).get_result()

print(response.get_status_code())
