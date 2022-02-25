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

"""
Test methods in the common module
"""

import unittest
from ibmcloudant import common


class TestCommon(unittest.TestCase):
    """
    Test methods in the common module
    """

    def test_get_sdk_headers(self):
        """
        Test the get_sdk_headers method
        """
        headers = common.get_sdk_headers(service_name='ibmcloudant', service_version='V1', operation_id='operation1')
        self.assertIsNotNone(headers)
        self.assertIsNotNone(headers.get('User-Agent'))
        self.assertIn('cloudant-python-sdk', headers.get('User-Agent'))
        self.assertRegex(headers.get('User-Agent'), r'^cloudant-python-sdk/[\d\.]* \(.*\)$')

    def test_get_system_info(self):
        """
        Test the get_system_info method
        """
        system_info = common.get_system_info()
        self.assertIsNotNone(system_info)
