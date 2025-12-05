# © Copyright IBM Corporation 2025. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Testsuite for the examples in the README file.

import unittest
from ibmcloudant.cloudant_v1 import CloudantV1
import os
import time
import requests

from pathlib import Path
import sys
parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

class TestReadmeExamples(unittest.TestCase):
    wiremock_url: str = None

    def setUp(self):
        # Set Wiremock server URL from environment variable if exists
        self.wiremock_url = os.getenv('WIREMOCK_URL')

        os.environ['CLOUDANT_URL'] = self.wiremock_url
        os.environ['CLOUDANT_AUTH_TYPE'] = 'noauth'

    #  Test create_db_and_doc example

    def test_create_db_and_doc_example(self):
        from src import create_db_and_doc
        client: CloudantV1 = create_db_and_doc.client
        example_db_name: str = create_db_and_doc.example_db_name
        example_doc_id: str = create_db_and_doc.example_doc_id

        # Verify database was created
        dbs = client.get_all_dbs().get_result()
        self.assertIn(example_db_name, dbs)

        # Verify document was created
        doc = client.get_document(
            db=example_db_name,
            doc_id=example_doc_id
        ).get_result()
        self.assertEqual(doc["id"], example_doc_id)

    # Test delete_doc example
    def test_delete_doc_example(self):
        from src import delete_doc
        client: CloudantV1 = delete_doc.client
        example_db_name: str = delete_doc.example_db_name
        example_doc_id: str = delete_doc.example_doc_id

        # Verify document was deleted
        with self.assertRaises(Exception) as context:
            client.get_document(
                db=example_db_name,
                doc_id=example_doc_id
            ).get_result()
        self.assertIn('not found', str(context.exception).lower())
    
    # Test get_info_from_existing_database example
    def test_get_info_from_existing_database_example(self):
        from src import get_info_from_existing_database
        client: CloudantV1 = get_info_from_existing_database.client
        db_name: str = get_info_from_existing_database.db_name

        # Verify server information was retrieved
        server_information = client.get_server_information().get_result()
        self.assertIn("version", server_information)

        # Verify database information was retrieved
        db_information = client.get_database_information(
            db=db_name
        ).get_result()
        self.assertEqual(db_information["db_name"], db_name)

        # Verify document was retrieved
        document_example = client.get_document(
            db=db_name,
            doc_id="example"
        ).get_result()
        self.assertEqual(document_example["id"], "example")

    def tearDown(self):
        # wait 5 seconds for CI/CD resource constraints
        time.sleep(5)

        # Reset wiremock
        try:
            requests.post(self.wiremock_url + "/__admin/scenarios/reset",
                          headers={"Content-Type": "application/json"})
        except Exception as e:
            print("Error resetting wiremock:", str(e))

        return super().tearDown()


if __name__ == '__main__':
    unittest.main()
