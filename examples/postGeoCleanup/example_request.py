# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_geo_cleanup(
  db='stores'
).get_result()

print(response)
