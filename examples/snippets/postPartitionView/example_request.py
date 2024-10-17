# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_partition_view(
  db='events',
  ddoc='checkout',
  include_docs=True,
  limit=10,
  partition_key='ns1HJS13AMkK',
  view='byProductId'
).get_result()

print(response)
# section: markdown
# This example requires the `byProductId` partitioned view to exist. To create the design document with this view, see [Create or modify a design document.](#putdesigndocument)
