# section: code
from ibmcloudant.cloudant_v1 import AllDocsQuery, CloudantV1

service = CloudantV1.new_instance()

doc1 = AllDocsQuery(
  descending=True,
  include_docs=True,
  limit=10
)
doc2 = AllDocsQuery(
  inclusive_end=True,
  key='_design/allusers',
  skip=1
)

response = service.post_design_docs_queries(
  db='users',
  queries=[doc1, doc2]
).get_result()

print(response)
