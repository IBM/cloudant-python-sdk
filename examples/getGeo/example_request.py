# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_geo(
  db='stores',
  ddoc='places',
  index='pointsInEngland',
  bbox='-50.52,-4.46,54.59,1.45',
  include_docs=True,
  nearest=True
).get_result()

print(response)
