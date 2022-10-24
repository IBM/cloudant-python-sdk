# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response_attachment = service.get_attachment(
  db='products',
  doc_id='small-appliances:100001',
  attachment_name='product_details.txt'
).get_result().content

print(response_attachment)
# section: markdown
# This example requires the `product_details.txt` attachment in `small-appliances:100001` document to exist. To create the attachment, see [Create or modify an attachment.](#putattachment)
