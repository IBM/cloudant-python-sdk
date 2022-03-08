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

from ibmcloudant.cloudant_v1 import CloudantV1

# 1. Create a Cloudant client with "EXAMPLES" service name ============
client = CloudantV1.new_instance(service_name="EXAMPLES")

# 2. Get server information ===========================================
server_information = client.get_server_information(
).get_result()

print(f'Server Version: {server_information["version"]}')

# 3. Get database information for "animaldb" ==========================
db_name = "animaldb"

db_information = client.get_database_information(
    db=db_name
).get_result()

# 4. Show document count in database ==================================
document_count = db_information["doc_count"]

print(f'Document count in \"{db_information["db_name"]}\" '
      f'database is {document_count}.')

# 5. Get zebra document out of the database by document id ============
document_about_zebra = client.get_document(
    db=db_name,
    doc_id="zebra"
).get_result()

print(f'Document retrieved from database:\n'
      f'{json.dumps(document_about_zebra, indent=2)}')
