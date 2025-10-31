# section: code
from ibmcloudant.cloudant_v1 import Document, CloudantV1

service = CloudantV1.new_instance()

with open("products_doc.json", "rb") as products_doc:
  response = service.post_document(
      db='products',
      document=products_doc_binary,
      content_type="application/json"
  ).get_result()

print(response)
