# section: code
from ibmcloudant.cloudant_v1 import Analyzer, AnalyzerConfiguration, CloudantV1, DesignDocument, DesignDocumentOptions, DesignDocumentViewsMapReduce, SearchIndexDefinition

service = CloudantV1.new_instance()

email_view_map_reduce = DesignDocumentViewsMapReduce(
  map='function(doc) { if(doc.email_verified  === true){\n  emit(doc.email, [doc.name, doc.email_verified, doc.joined]) }}'
)

user_index = SearchIndexDefinition(
  index='function (doc) { index("name", doc.name); index("active", doc.active); }',
  analyzer=AnalyzerConfiguration(name="standard", fields={"email": Analyzer(name="email")}))

design_document = DesignDocument(
  views={'getVerifiedEmails': email_view_map_reduce},
  indexes={'activeUsers': user_index}
)

response = service.put_design_document(
  db='users',
  design_document=design_document,
  ddoc='allusers'
).get_result()

print(response)

# Partitioned DesignDocument Example

product_map = DesignDocumentViewsMapReduce(
  map='function(doc) { emit(doc.productId, [doc.brand, doc.name, doc.description]) }'
)

price_index = SearchIndexDefinition(
  index='function (doc) { index("price", doc.price);}',
  analyzer=AnalyzerConfiguration(name="classic", fields={"description": Analyzer(name="english")})
)

design_document_options = DesignDocumentOptions(
  partitioned=True
)

partitioned_design_doc = DesignDocument(
  views={'byApplianceProdId': product_map},
  indexes={'findByPrice': price_index},
  options=design_document_options
)

response = service.put_design_document(
  db='products',
  design_document=partitioned_design_doc,
  ddoc='appliances'
).get_result()

print(response)
# section: markdown
# This example creates `allusers` design document in the `users` database and `appliances` design document in the partitioned `products` database.
