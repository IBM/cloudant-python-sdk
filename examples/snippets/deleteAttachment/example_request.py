# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_attachment(
  db='products',
  doc_id='1000042',
  attachment_name='product_details.txt',
  rev='4-33333333333333333333333333333333'
).get_result()

print(response)
# section: markdown
# This example requires the `product_details.txt` attachment in `1000042` document to exist. To create the attachment, see [Create or modify an attachment.](#putattachment)
