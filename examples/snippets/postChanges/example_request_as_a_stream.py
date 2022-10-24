# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

result = service.post_changes_as_stream(
  db='orders'
).get_result()

with open('result.json', 'wb') as f:
  for chunk in result.iter_content():
    f.write(chunk)
