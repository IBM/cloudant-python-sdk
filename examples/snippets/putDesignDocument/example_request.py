# section: code
from ibmcloudant.cloudant_v1 import Analyzer, AnalyzerConfiguration, CloudantV1, DesignDocument, DesignDocumentOptions, DesignDocumentViewsMapReduce, SearchIndexDefinition

service = CloudantV1.new_instance()

email_view_map_reduce = DesignDocumentViewsMapReduce(
  map='function(doc) { if(doc.email_verified === true) { emit(doc.email, [doc.name, doc.email_verified, doc.joined]); }}'
)

user_index = SearchIndexDefinition(
  index='function(doc) { index("name", doc.name); index("active", doc.active); }',
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
  map='function(doc) { emit(doc.productId, [doc.date, doc.eventType, doc.userId]); }'
)

date_index = SearchIndexDefinition(
  index='function(doc) { index("date", doc.date); }',
  analyzer=AnalyzerConfiguration(name="classic", fields={"description": Analyzer(name="english")})
)

design_document_options = DesignDocumentOptions(
  partitioned=True
)

partitioned_design_doc = DesignDocument(
  views={'byProductId': product_map},
  indexes={'findByDate': date_index},
  options=design_document_options
)

response = service.put_design_document(
  db='events',
  design_document=partitioned_design_doc,
  ddoc='checkout'
).get_result()

print(response)
# section: markdown
# This example creates `allusers` design document in the `users` database and `checkout` design document in the partitioned `events` database.
