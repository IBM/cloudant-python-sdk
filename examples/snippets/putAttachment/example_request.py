# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

detailed_description = "This appliance includes..."
response = service.put_attachment(
  db='products',
  doc_id='1000042',
  attachment_name='product_details.txt',
  attachment=detailed_description,
  content_type='text/plain'
).get_result()

print(response)
