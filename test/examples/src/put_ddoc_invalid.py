from ibmcloudant.cloudant_v1 import CloudantV1, DesignDocument

service = CloudantV1.new_instance()

price_index = {
    'index': 'function (doc) { index("price", doc.price); }',
}

partitioned_design_doc = DesignDocument(
    indexes={'findByPrice': price_index},
    options={'partitioned': True}
)

response = service.put_design_document(
    db='products',
    design_document=partitioned_design_doc,
    ddoc='appliances'
).get_result()

print(response)
