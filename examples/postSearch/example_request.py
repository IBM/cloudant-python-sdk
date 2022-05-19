# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_search(
  db='users',
  ddoc='allusers',
  index='activeUsers',
  query='name:Jane* AND active:True'
).get_result()

print(response)
# section: markdown
# This example requires the `activeUsers` Cloudant Search index to exist. To create the design document with this index, see [Create or modify a design document.](#putdesigndocument)
