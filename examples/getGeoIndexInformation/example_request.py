# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_geo_index_information(
  db='stores',
  ddoc='places',
  index='pointsInEngland'
).get_result()

print(response)
