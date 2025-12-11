# coding: utf-8

# © Copyright IBM Corporation 2020, 2023.
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
              f'"{example_db_name}" database or "{example_doc_id}" ' +
              'document was not found.')
