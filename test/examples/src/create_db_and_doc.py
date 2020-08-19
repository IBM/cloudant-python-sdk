import logging

from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1, Document

# Set logging level to show only critical logs
logging.basicConfig(level=logging.CRITICAL)

# 1. Create a client with `CLOUDANT` default service name ============
client = CloudantV1.new_instance()

# 2. Create a database ===============================================
example_db_name = "orders"

# Try to create database if it doesn't exist
try:
    put_database_result = client.put_database(
        db=example_db_name
    ).get_result()
    if put_database_result["ok"]:
        print(f'"{example_db_name}" database created.')
except ApiException as ae:
    if ae.code == 412:
        print(f'Cannot create "{example_db_name}" database, ' +
              'it already exists.')

# 3. Create a document ===============================================
# Create a document object with "example" id
example_doc_id = "example"
example_document: Document = Document(id=example_doc_id)

# Add "name" and "joined" fields to the document
example_document.name = "Bob Smith"
example_document.joined = "2019-01-24T10:42:99.000Z"

'''
Try to get the document and set revision of example_document to the
latest one if it previously existed in the database
'''
try:
    document_info = client.get_document(
        db=example_db_name, doc_id=example_doc_id
    ).get_result()
    example_document.rev = document_info["_rev"]
    print(f'The document revision for {example_doc_id} document' +
          f'is set to {example_document.rev}.')
except ApiException as ae:
    if ae.code == 404:
        pass

# Save the document in the database
create_document_response = client.post_document(
    db=example_db_name,
    document=example_document
).get_result()

# Keep track of the revision number from the `example` document object
example_document.rev = create_document_response["rev"]
print(f'You have created the document:\n{example_document}')
