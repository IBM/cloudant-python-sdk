# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.delete_attachment(
  db='products',
  doc_id='small-appliances:100001',
  attachment_name='product_details.txt',
  rev='4-1a0d1cd6f40472509e9aac646183736a'
).get_result()

print(response)
# section: markdown
# This example requires the `product_details.txt` attachment in `small-appliances:100001` document to exist. To create the attachment, see [Create or modify an attachment.](#putattachment)
