# section: code
from ibmcloudant.cloudant_v1 import BulkGetQueryDocument, CloudantV1

service = CloudantV1.new_instance()

bulk_get_doc = BulkGetQueryDocument(
    id='order00058',
    atts_since=['1-99b02e08da151943c2dcb40090160bb8'])
response = service.post_bulk_get(
    db='orders',
    docs=[bulk_get_doc]
).get_result()

print(response)
