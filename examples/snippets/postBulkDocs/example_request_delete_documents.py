# section: code
from ibmcloudant.cloudant_v1 import Document, CloudantV1, BulkDocs

service = CloudantV1.new_instance()

event_doc_1 = Document(
  _id="0007241142412418284",
  _rev="1-5005d65514fe9e90f8eccf174af5dd64",
  _deleted=True,
)
event_doc_2 = Document(
  _id="0007241142412418285",
  _rev="1-2d7810b054babeda4812b3924428d6d6",
  _deleted=True,
)

bulk_docs = BulkDocs(docs=[event_doc_1, event_doc_2])

response = service.post_bulk_docs(
  db='events',
  bulk_docs=bulk_docs
).get_result()

print(response)
