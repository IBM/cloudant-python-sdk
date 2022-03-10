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

import json
import logging

from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1

# Set logging level to show only critical logs
logging.basicConfig(level=logging.CRITICAL)

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
    if ae.code == 404:
        print('Cannot delete document because either ' +
              f'"{example_db_name}" database or "{example_doc_id}" ' +
              'document was not found.')
