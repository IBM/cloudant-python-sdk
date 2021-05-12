import json
import logging

from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1

# Set logging level to show only critical logs
logging.basicConfig(level=logging.CRITICAL)

# 1. Create a client with `CLOUDANT` default service name ============
client = CloudantV1.new_instance()

# 2. Update the document =============================================
example_db_name = "orders"
example_doc_id = "example"

# Try to get the document if it previously existed in the database
try:
    document = client.get_document(
        db=example_db_name,
        doc_id=example_doc_id
    ).get_result()

    # Note: for response byte stream use:
    # document_as_stream = client.get_document_as_stream(
    #     db=example_db_name,
    #     doc_id=example_doc_id
    # ).get_result()

    #  Add Bob Smith's address to the document
    document["address"] = "19 Front Street, Darlington, DL5 1TY"

    #  Remove the joined property from document object
    if "joined" in document:
        document.pop("joined")

    # Update the document in the database
    update_document_response = client.post_document(
        db=example_db_name,
        document=document
    ).get_result()

    # Note: for request byte stream use:
    # update_document_response = client.post_document(
    #     db=example_db_name,
    #     document=document_as_binaryio
    # ).get_result()

    # Keep track with the revision number of the document object:
    document["_rev"] = update_document_response["rev"]
    print(f'You have updated the document:\n' +
          json.dumps(document, indent=2))

except ApiException as ae:
    if ae.code == 404:
        print('Cannot delete document because either ' +
              f'"{example_db_name}" database or "{example_doc_id}" ' +
              'document was not found.')
