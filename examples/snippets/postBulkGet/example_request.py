# section: code
from ibmcloudant.cloudant_v1 import BulkGetQueryDocument, CloudantV1

service = CloudantV1.new_instance()

doc_id = 'order00067'
bulk_get_doc_1 = BulkGetQueryDocument(
    id=doc_id,
    rev='3-917fa2381192822767f010b95b45325b')
bulk_get_doc_2 = BulkGetQueryDocument(
    id=doc_id,
    rev='4-a5be949eeb7296747cc271766e9a498b')

response = service.post_bulk_get(
    db='orders',
    docs=[bulk_get_doc_1, bulk_get_doc_2],
).get_result()

print(response)
