# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.post_view(
  db='users',
  ddoc='allusers',
  view='getVerifiedEmails'
).get_result()

print(response)
# section: markdown
# This example requires the `getVerifiedEmails` view to exist. To create the design document with this view, see [Create or modify a design document.](#putdesigndocument)
