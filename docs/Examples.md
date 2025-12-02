# Code examples

<details open>
<summary>Table of Contents</summary>

<!-- toc -->
- [1. Create a database and add a document](#1-create-a-database-and-add-a-document)
- [2. Retrieve information from an existing database](#2-retrieve-information-from-an-existing-database)
- [3. Update your previously created document](#3-update-your-previously-created-document)
- [4. Delete your previously created document](#4-delete-your-previously-created-document)
- [Further code examples](#further-code-examples)
</details>

The following code examples
[authenticate with the environment variables](Authentication.md#authentication-with-environment-variables).

## 1. Create a database and add a document

**Note:** This example code assumes that `orders` database does not exist in your account.

This example code creates `orders` database and adds a new document "example"
into it. To connect, you must set your environment variables with
the *service url*, *authentication type* and *authentication credentials*
of your Cloudant service.

Cloudant environment variable naming starts with a *service name* prefix that identifies your service.
By default, this is `CLOUDANT`, see the settings in the
[authentication with environment variables section](Authentication.md#authentication-with-environment-variables).

If you would like to rename your Cloudant service from `CLOUDANT`,
you must use your defined service name as the prefix for all Cloudant related environment variables.

Once the environment variables are set, you can try out the code examples.

```py
from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1, Document

# 1. Create a client with `CLOUDANT` default service name =============
client = CloudantV1.new_instance()

# 2. Create a database ================================================
example_db_name = "orders"

# Try to create database if it doesn't exist
try:
    put_database_result = client.put_database(
        db=example_db_name
    ).get_result()
    if put_database_result["ok"]:
        print(f'"{example_db_name}" database created.')
except ApiException as ae:
    if ae.status_code == 412:
        print(f'Cannot create "{example_db_name}" database, ' +
              'it already exists.')

# 3. Create a document ================================================
# Create a document object with "example" id
example_doc_id = "example"
# Setting `id` for the document is optional when "post_document"
# function is used for CREATE. When `id` is not provided the server
# will generate one for your document.
example_document: Document = Document(id=example_doc_id)

# Add "name" and "joined" fields to the document
example_document.name = "Bob Smith"
example_document.joined = "2019-01-24T10:42:59.000Z"

# Save the document in the database with "post_document" function
create_document_response = client.post_document(
    db=example_db_name,
    document=example_document
).get_result()

# =====================================================================
# Note: saving the document can also be done with the "put_document"
# function. In this case `doc_id` is required for a CREATE operation:
"""
create_document_response = client.put_document(
    db=example_db_name,
    doc_id=example_doc_id,
    document=example_document
).get_result()
"""
# =====================================================================

# Keeping track of the revision number of the document object
# is necessary for further UPDATE/DELETE operations:
example_document.rev = create_document_response["rev"]
print(f'You have created the document:\n{example_document}')
```

When you run the code, you see a result similar to the following output.

```text
"orders" database created.
You have created the document:
{
  "_id": "example",
  "_rev": "1-1b403633540686aa32d013fda9041a5d",
  "name": "Bob Smith",
  "joined": "2019-01-24T10:42:99.000Z"
}
```

## 2. Retrieve information from an existing database

**Note**: This example code assumes that you have created both the `orders`
database and the `example` document by
[running the previous example code](#1-create-a-database-and-add-a-document)
successfully. Otherwise, the following error message occurs, "Cannot delete document because either 'orders'
database or 'example' document was not found."

<details open>
<summary>Gather database information example</summary>

```py
import json

from ibmcloudant.cloudant_v1 import CloudantV1

# 1. Create a client with `CLOUDANT` default service name ============
client = CloudantV1.new_instance()

# 2. Get server information ===========================================
server_information = client.get_server_information(
).get_result()

print(f'Server Version: {server_information["version"]}')

# 3. Get database information for "orders" ==========================
db_name = "orders"

db_information = client.get_database_information(
    db=db_name
).get_result()

# 4. Show document count in database ==================================
document_count = db_information["doc_count"]

print(f'Document count in \"{db_information["db_name"]}\" '
      f'database is {document_count}.')

# 5. Get "example" document out of the database by document id ============
document_example = client.get_document(
    db=db_name,
    doc_id="example"
).get_result()

print(f'Document retrieved from database:\n'
      f'{json.dumps(document_example, indent=2)}')
```

</details>
When you run the code, you see a result similar to the following output.

```text
Server Version: 2.1.1
Document count in "orders" database is 1.
Document retrieved from database:
{
  "_id": "example",
  "_rev": "1-1b403633540686aa32d013fda9041a5d",
  "name": "Bob Smith",
  "joined": "2019-01-24T10:42:99.000Z"
}
```

## 3. Update your previously created document

**Note**: This example code assumes that you have created both the `orders`
database and the `example` document by
[running the previous example code](#1-create-a-database-and-add-a-document)
successfully. Otherwise, the following error message occurs, "Cannot update document because either 'orders'
database or 'example' document was not found."

<details open>
<summary>Update code example</summary>

```py
import json

from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1

# 1. Create a client with `CLOUDANT` default service name =============
client = CloudantV1.new_instance()

# 2. Update the document ==============================================
example_db_name = "orders"
example_doc_id = "example"

# Try to get the document if it previously existed in the database
try:
    document = client.get_document(
        db=example_db_name,
        doc_id=example_doc_id
    ).get_result()

    # =================================================================
    # Note: for response byte stream use:
    """
    document_as_byte_stream = client.get_document_as_stream(
        db=example_db_name,
        doc_id=example_doc_id
    ).get_result()
    """
    # =================================================================

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

    # =================================================================
    # Note 1: for request byte stream use:
    """
    update_document_response = client.post_document(
        db=example_db_name,
        document=document_as_byte_stream
    ).get_result()
    """
    # =================================================================

    # =================================================================
    # Note 2: updating the document can also be done with the
    # "put_document" function. `doc_id` and `rev` are required for an
    # UPDATE operation, but `rev` can be provided in the document
    # object as `_rev` too:
    """
    update_document_response = client.put_document(
        db=example_db_name,
        doc_id=example_doc_id,  # doc_id is a required parameter
        rev=document["_rev"],
        document=document  # _rev in the document object CAN replace above `rev` parameter
    ).get_result()
    """
    # =================================================================

    # Keeping track of the latest revision number of the document
    # object is necessary for further UPDATE/DELETE operations:
    document["_rev"] = update_document_response["rev"]
    print(f'You have updated the document:\n' +
          json.dumps(document, indent=2))

except ApiException as ae:
    if ae.status_code == 404:
        print('Cannot delete document because either ' +
              f'"{example_db_name}" database or "{example_doc_id}" ' +
              'document was not found.')
```

</details>
When you run the code, you see a result similar to the following output.

```text
{
  "_id": "example",
  "_rev": "2-4e2178e85cffb32d38ba4e451f6ca376",
  "name": "Bob Smith",
  "address": "19 Front Street, Darlington, DL5 1TY"
}
```

## 4. Delete your previously created document

**Note**: This example code assumes that you have created both the `orders`
database and the `example` document by
[running the previous example code](#1-create-a-database-and-add-a-document)
successfully. Otherwise, the following error message occurs, "Cannot delete document because either 'orders'
database or 'example' document was not found."

<details open>
<summary>Delete code example</summary>

```py
from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1

# 1. Create a client with `CLOUDANT` default service name =============
client = CloudantV1.new_instance()

# 2. Delete the document ==============================================
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
        doc_id=example_doc_id,  # `doc_id` is required for DELETE
        rev=document["_rev"]    # `rev` is required for DELETE
    ).get_result()

    if delete_document_response["ok"]:
        print('You have deleted the document.')

except ApiException as ae:
    if ae.status_code == 404:
        print('Cannot delete document because either ' +
              f'"{example_db_name}" database or "{example_doc_id}"' +
              'document was not found.')
```

</details>
When you run the code, you see the following output.

```text
You have deleted the document.
```

## Further code examples

For a complete list of code examples, see the [examples directory](https://github.com/IBM/cloudant-python-sdk/tree/v0.11.2/examples#examples-for-python).
