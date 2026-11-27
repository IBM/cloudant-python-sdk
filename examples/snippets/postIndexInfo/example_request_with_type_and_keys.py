# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_index_info(
  db='recipes',
  keys=['_design/cookbook'],
  type=['search']
).get_result()

print(response)
# section: markdown
# This example requires the `cookbook` design document to exist with a Cloudant Search index. To create the design document, see [Create or modify a design document.](#putdesigndocument)
