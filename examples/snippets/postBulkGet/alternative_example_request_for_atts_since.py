# section: code
from ibmcloudant.cloudant_v1 import BulkGetQueryDocument, CloudantV1

service = CloudantV1.new_instance()

bulk_get_doc = BulkGetQueryDocument(
    id='order00058',
    atts_since=['1-00000000000000000000000000000000'])
response = service.post_bulk_get(
    db='orders',
    docs=[bulk_get_doc]
).get_result()

print(response)
