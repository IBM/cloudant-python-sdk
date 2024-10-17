# section: code
from ibmcloudant.cloudant_v1 import Document, CloudantV1, BulkDocs

service = CloudantV1.new_instance()

event_doc_1 = Document(
  _id="ns1HJS13AMkK:0007241142412418284",
  type="event",
  userId="abc123",
  eventType="addedToBasket",
  productId="1000042",
  date="2019-01-28T10:44:22.000Z"
)
event_doc_2 = Document(
  _id="H8tDIwfadxp9:0007241142412418285",
  type="event",
  userId="abc234",
  eventType="addedToBasket",
  productId="1000050",
  date="2019-01-25T20:00:00.000Z"
)

bulk_docs = BulkDocs(docs=[event_doc_1, event_doc_2])

response = service.post_bulk_docs(
  db='events',
  bulk_docs=bulk_docs
).get_result()

print(response)
