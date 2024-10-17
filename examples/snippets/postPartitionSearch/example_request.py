# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_partition_search(
  db='events',
  partition_key='ns1HJS13AMkK',
  ddoc='checkout',
  index='findByDate',
  query='date:[2019-01-01T12:00:00.000Z TO 2019-01-31T12:00:00.000Z]'
).get_result()

print(response)
# section: markdown
# This example requires the `findByDate` Cloudant Search partitioned index to exist. To create the design document with this index, see [Create or modify a design document.](#putdesigndocument)
