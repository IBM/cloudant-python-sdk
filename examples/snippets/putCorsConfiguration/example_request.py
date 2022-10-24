# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.put_cors_configuration(
  enable_cors=True,
  origins=['https://example.com']
).get_result()

print(response)
