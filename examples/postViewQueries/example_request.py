# section: code
from ibmcloudant.cloudant_v1 import CloudantV1, ViewQuery

service = CloudantV1.new_instance()

query1 = ViewQuery(
  include_docs=True,
  limit=5
)
query2 = ViewQuery(
  descending=True,
  skip=1
)

response = service.post_view_queries(
  db='users',
  ddoc='allusers',
  queries=[query1, query2],
  view='getVerifiedEmails'
).get_result()

print(response)
# section: markdown
# This example requires the `getVerifiedEmails` view to exist. To create the design document with this view, see [Create or modify a design document.](#putdesigndocument)
