# section: code
from ibmcloudant.cloudant_v1 import DocumentRevisions, CloudantV1

service = CloudantV1.new_instance()

revs_diff = DocumentRevisions(
  order00077=[
      "1-00000000000000000000000000000000", # missing revision
      "2-11111111111111111111111111111111", # missing revision
      "3-22222222222222222222222222222222"  # possible ancestor revision
]
)

response = service.post_revs_diff(
  db='orders',
  revs_diff_request=revs_diff.to_dict()
).get_result()

print(response)
// section: markdown
// This example requires the example revisions in the POST body to be replaced with valid revisions.
