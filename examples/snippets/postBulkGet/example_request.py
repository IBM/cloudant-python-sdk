# section: code
from ibmcloudant.cloudant_v1 import BulkGetQueryDocument, CloudantV1

service = CloudantV1.new_instance()

doc_id = 'order00067'
bulk_get_doc_1 = BulkGetQueryDocument(
    id=doc_id,
    rev='3-22222222222222222222222222222222')
bulk_get_doc_2 = BulkGetQueryDocument(
    id=doc_id,
    rev='4-33333333333333333333333333333333')

response = service.post_bulk_get(
    db='orders',
    docs=[bulk_get_doc_1, bulk_get_doc_2],
).get_result()

print(response)
