# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_partition_search(
  db='products',
  partition_key='small-appliances',
  ddoc='appliances',
  index='findByPrice',
  query='price:[14 TO 20]'
).get_result()

print(response)
# section: markdown
# This example requires the `findByPrice` Cloudant Search partitioned index to exist. To create the design document with this index, see [Create or modify a design document.](#putdesigndocument)
