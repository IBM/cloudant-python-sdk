# section: code
from ibmcloudant.cloudant_v1 import CloudantV1, IndexDefinition, IndexField

service = CloudantV1.new_instance()

# Type "json" index fields require an object that maps the name of a field to a sort direction.
index_field = IndexField(
  email="asc"
)
index = IndexDefinition(
  fields=[index_field]
)

response = service.post_index(
  db='users',
  ddoc='json-index',
  name='getUserByEmail',
  index=index,
  type='json'
).get_result()

print(response)
