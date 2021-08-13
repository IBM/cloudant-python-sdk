# coding: utf-8

# © Copyright IBM Corporation 2021.
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

import unittest
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibmcloudant.cloudant_v1 import *

class TestValidation(unittest.TestCase):

    def test_validates_doc_id(self):
        service = CloudantV1(
            authenticator=NoAuthAuthenticator()
        )
        service.set_service_url('https://cloudant.example')
        with self.assertRaisesRegex(ValueError, '.+_testDocument.+') as cm:
            service.get_document('testDatabase', '_testDocument')

    def test_validates_doc_id_at_long_service_path(self):
        service = CloudantV1(
            authenticator=NoAuthAuthenticator()
        )
        service.set_service_url('https://cloudant.example/some/proxy/path')
        with self.assertRaisesRegex(ValueError, '.+_testDocument.+') as cm:
            service.get_document('testDatabase', '_testDocument')

    def test_validates_doc_id_at_long_service_path_after_change(self):
        service = CloudantV1(
            authenticator=NoAuthAuthenticator()
        )
        service.set_service_url('https://cloudant.example')
        with self.assertRaisesRegex(ValueError, '.+_testDocument.+') as cm:
            service.get_document('testDatabase', '_testDocument')
        service.set_service_url('https://cloudant.example/some/proxy/path')
        with self.assertRaisesRegex(ValueError, '.+_testDocument.+') as cm:
            service.get_document('testDatabase', '_testDocument')
