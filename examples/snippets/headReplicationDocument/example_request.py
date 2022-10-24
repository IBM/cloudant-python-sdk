# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.head_replication_document(
 doc_id='repldoc-example'
)
print(response.get_status_code())
print(response.get_headers()['ETag'])
