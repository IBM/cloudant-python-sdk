# section: code
from ibmcloudant.cloudant_v1 import Document, CloudantV1

service = CloudantV1.new_instance()

local_document = Document(
   type='order',
   user='Bob Smith',
   orderId='0007741142412418284',
   userId='abc123',
   total=214.98,
   deliveryAddress='19 Front Street, Darlington, DL5 1TY',
   delivered='true',
   courier='UPS',
   courierId='15125425151261289',
   date='2019-01-28T10:44:22.000Z'
)

response = service.put_local_document(
  db='orders',
  doc_id='local-0007741142412418284',
  document=local_document,
).get_result()

print(response)
