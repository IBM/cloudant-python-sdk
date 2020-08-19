import logging

from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1

# Set logging level to show only critical logs
logging.basicConfig(level=logging.CRITICAL)

# 1. Create a client with `CLOUDANT` default service name ============
client = CloudantV1.new_instance()

# 2. Delete the document =============================================
example_db_name = "orders"
example_doc_id = "example"

# Try to get the document if it previously existed in the database
try:
    document = client.get_document(
        db=example_db_name,
        doc_id=example_doc_id
    ).get_result()

    delete_document_response = client.delete_document(
        db=example_db_name,
        doc_id=example_doc_id,
        rev=document["_rev"]
    ).get_result()

    if delete_document_response["ok"]:
        print('You have deleted the document.')

except ApiException as ae:
    if ae.code == 404:
        print('Cannot delete document because either ' +
              f'"{example_db_name}" database or "{example_doc_id}"' +
              'document was not found.')