# section: code
from ibmcloudant.cloudant_v1 import Document, CloudantV1

service = CloudantV1.new_instance()

products_doc = Document(
  _id="1000042",
  type="product",
  productId="1000042",
  brand="Salter",
  name="Digital Kitchen Scales",
  description="Slim Colourful Design Electronic Cooking Appliance for Home / Kitchen, Weigh up to 5kg + Aquatronic for Liquids ml + fl. oz. 15Yr Guarantee - Green",
  price=14.99,
  image="assets/img/0gmsnghhew.jpg")

response = service.post_document(db='products', document=products_doc).get_result()

print(response)
