# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_find(
  db='users',
  selector={'address': {'$exists': True}},
  fields=["_id", "type", "name", "email", "address"],
  limit=3
).get_result()
print(response)
# section: markdown
# This example requires the `getUserByAddress` Cloudant Query "text" index to exist. To create the index, see [Create a new index on a database.](#postindex)
