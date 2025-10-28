# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_db_updates(
  feed='normal',
  since='now'
).get_result()

print(response)
# section: markdown
# This request requires `server_admin` access.
