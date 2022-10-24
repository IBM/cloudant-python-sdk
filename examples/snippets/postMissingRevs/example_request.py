# section: code
from ibmcloudant.cloudant_v1 import DocumentRevisions, CloudantV1

service = CloudantV1.new_instance()

revs = DocumentRevisions(order00077=['<order00077-existing-revision>', '<2-missing-revision>'])
response = service.post_missing_revs(
  db='orders',
  missing_revs=revs.to_dict()
).get_result()

print(response)
