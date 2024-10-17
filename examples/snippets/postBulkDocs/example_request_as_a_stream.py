# section: code
from ibmcloudant.cloudant_v1 import Document, CloudantV1

service = CloudantV1.new_instance()

with open('upload.json', 'rb') as f:
  response = service.post_bulk_docs(
    db='events',
    bulk_docs=f
  ).get_result()

print(response)
# section: markdown
# Content of upload.json
# section: code
{
  "docs": [
    {
      "_id": "ns1HJS13AMkK:0007241142412418284",
      "type": "event",
      "userId": "abc123",
      "eventType": "addedToBasket",
      "productId": "1000042",
      "date": "2019-01-28T10:44:22.000Z"
    },
    {
      "_id": "H8tDIwfadxp9:0007241142412418285",
      "type": "event",
      "userId": "abc234",
      "eventType": "addedToBasket",
      "productId": "1000050",
      "date": "2019-01-25T20:00:00.000Z"
    }
  ]
}
