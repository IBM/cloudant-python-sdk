# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_index(
  db='users',
  ddoc='json-index',
  index='getUserByName',
  type='json'
).get_result()

print(response)
# section: markdown
# This example will fail if `getUserByName` index doesn't exist. To create the index, see [Create a new index on a database.](#postindex)
