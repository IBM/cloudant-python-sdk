# section: code
from ibmcloudant.cloudant_v1 import CloudantV1, IndexDefinition, IndexField

service = CloudantV1.new_instance()

# Type "text" index fields require an object with a name and type properties for the field.
index_field = IndexField(
  name="address",
  type=IndexField.TypeEnum.STRING
)
index = IndexDefinition(
  fields=[index_field]
)

response = service.post_index(
  db='users',
  ddoc='text-index',
  name='getUserByAddress',
  index=index,
  type='text'
).get_result()

print(response)
