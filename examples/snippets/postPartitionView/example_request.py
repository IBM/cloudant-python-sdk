# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_partition_view(
  db='products',
  ddoc='appliances',
  limit=10,
  partition_key='small-appliances',
  view='byApplianceProdId'
).get_result()

print(response)
# section: markdown
# This example requires the `byApplianceProdId` partitioned view to exist. To create the design document with this view, see [Create or modify a design document.](#putdesigndocument)
