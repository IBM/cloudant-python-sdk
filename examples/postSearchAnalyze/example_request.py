# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_search_analyze(
  analyzer='english',
  text='running is fun'
).get_result()

print(response)
