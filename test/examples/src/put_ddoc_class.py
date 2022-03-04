from ibmcloudant.cloudant_v1 import DesignDocument, CloudantV1, DesignDocumentOptions, SearchIndexDefinition

service = CloudantV1.new_instance()

price_index = SearchIndexDefinition(
    index='function (doc) { index("price", doc.price); }',
)

design_document_options = DesignDocumentOptions(
    partitioned=True
)

partitioned_design_doc = DesignDocument(
    indexes={'findByPrice': price_index},
    options=design_document_options
)

response = service.put_design_document(
    db='products',
    design_document=partitioned_design_doc,
    ddoc='appliances'
).get_result()

print(response)
