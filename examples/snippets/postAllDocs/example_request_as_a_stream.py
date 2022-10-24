# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

result = service.post_all_docs_as_stream(
  db='orders',
  include_docs=True,
  start_key='abc',
  limit=10
).get_result()

with open('result.json', 'wb') as f:
  for chunk in result.iter_content():
    f.write(chunk)
