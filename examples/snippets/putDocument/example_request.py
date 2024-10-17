# section: code
from ibmcloudant.cloudant_v1 import Document, CloudantV1

service = CloudantV1.new_instance()

event_doc = Document(
  type='event',
  userId='abc123',
  eventType='addedToBasket',
  productId='1000042',
  date='2019-01-28T10:44:22.000Z'
)
response = service.put_document(
  db='events',
  doc_id='ns1HJS13AMkK:0007241142412418284',
  document=event_doc
).get_result()

print(response)
