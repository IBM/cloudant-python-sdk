# coding: utf-8

# © Copyright IBM Corporation 2020, 2022.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1, Document

# Set logging level to show only critical logs
logging.basicConfig(level=logging.CRITICAL)

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
    if ae.code == 412:
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
