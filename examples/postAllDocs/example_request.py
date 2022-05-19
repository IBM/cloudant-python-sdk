# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_all_docs(
  db='orders',
  include_docs=True,
  start_key='abc',
  limit=10
).get_result()

print(response)
