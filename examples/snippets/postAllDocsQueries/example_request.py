# section: code
from ibmcloudant.cloudant_v1 import AllDocsQuery, CloudantV1

service = CloudantV1.new_instance()

all_docs_query1 = AllDocsQuery(
  keys=['small-appliances:1000042', 'small-appliances:1000043']
)

all_docs_query2 = AllDocsQuery(
  limit=3,
  skip=2
)

response = service.post_all_docs_queries(
  db='products',
  queries=[all_docs_query1, all_docs_query2]
).get_result()

print(response)
