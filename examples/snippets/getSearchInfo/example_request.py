# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_search_info(
  db='events',
  ddoc='checkout',
  index='findByDate'
).get_result()

print(response)
# section: markdown
# This example requires the `findByDate` Cloudant Search partitioned index to exist. To create the design document with this index, see [Create or modify a design document.](#putdesigndocument)
