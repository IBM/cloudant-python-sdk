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
import subprocess
import sys
import os
import requests
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent


class TestReadmeExamples(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up test environment before all tests"""
        # Get WireMock URL from environment
        wiremock_url = os.environ.get('WIREMOCK_URL')

        # Reset WireMock scenarios
        requests.post(f"{wiremock_url}/__admin/scenarios/reset")

        # Set authentication environment variables
        os.environ['CLOUDANT_URL'] = wiremock_url
        os.environ['CLOUDANT_AUTH_TYPE'] = 'noauth'

    def run_example_and_check_output(self, script_path, expected_output_path):
        env = os.environ.copy()

        # Ensure the subprocess uses the same site-packages
        python_path = sys.path.copy()
        if 'PYTHONPATH' in env:
            python_path.append(env['PYTHONPATH'])
        env['PYTHONPATH'] = os.pathsep.join(python_path)

        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            timeout=5,
            env=env,
        )
        if result.returncode != 0:
            self.fail(f"Script failed with return code {result.returncode}\n"
                      f"STDOUT:\n{result.stdout}\n"
                      f"STDERR:\n{result.stderr}")

        with open(expected_output_path, 'r') as f:
            expected_output = f.read().strip()

        actual_output = result.stdout.strip()

        self.assertEqual(actual_output, expected_output,
                         f"Output mismatch.\nExpected:\n{expected_output}\n\nGot:\n{actual_output}")

    def test_1_create_db_and_doc_example(self):
        """Creates db and doc for the first time"""
        script = parent_dir / "src" / "create_db_and_doc.py"
        output = parent_dir / "output" / "create_db_and_doc.txt"
        self.run_example_and_check_output(script, output)

    def test_2_get_info_from_existing_database_example(self):
        """Gets document from orders database"""
        script = parent_dir / "src" / "get_info_from_existing_database.py"
        output = parent_dir / "output" / "get_info_from_existing_database.txt"
        self.run_example_and_check_output(script, output)

    def test_3_update_doc_example_first_time(self):
        """Updates doc for the first time"""
        script = parent_dir / "src" / "update_doc.py"
        output = parent_dir / "output" / "update_doc.txt"
        self.run_example_and_check_output(script, output)

    def test_4_update_doc_example_second_time(self):
        """Updates doc for the second time"""
        script = parent_dir / "src" / "update_doc.py"
        output = parent_dir / "output" / "update_doc2.txt"
        self.run_example_and_check_output(script, output)

    def test_5_delete_doc_example_existing(self):
        """Deletes existing doc"""
        script = parent_dir / "src" / "delete_doc.py"
        output = parent_dir / "output" / "delete_doc.txt"
        self.run_example_and_check_output(script, output)

    def test_6_delete_doc_example_non_existing(self):
        """Deletes non-existing doc"""
        script = parent_dir / "src" / "delete_doc.py"
        output = parent_dir / "output" / "delete_doc2.txt"
        self.run_example_and_check_output(script, output)


if __name__ == '__main__':
    unittest.main()
