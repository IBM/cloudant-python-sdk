# coding: utf-8

# © Copyright IBM Corporation 2021, 2022.
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
import os
import unittest
from unittest import mock
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibmcloudant.cloudant_base_service import CLOUDANT_SDK_GEN1_ERRORS, gen1_only_rule
from ibmcloudant.cloudant_v1 import *

class TestValidation(unittest.TestCase):

    def test_validates_doc_id(self):
        service = CloudantV1(
            authenticator=NoAuthAuthenticator()
        )
        service.set_service_url('https://cloudant.example')
        with self.assertRaisesRegex(ValueError, '.+_testDocument.+') as cm:
            service.get_document('testDatabase', '_testDocument')

    def test_validates_doc_id_with_as_stream_operation(self):
        service = CloudantV1(
            authenticator=NoAuthAuthenticator()
        )
        service.set_service_url('https://cloudant.example')
        with self.assertRaisesRegex(ValueError, '.+_testDocument.+') as cm:
            service.get_document_as_stream('testDatabase', '_testDocument')

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

    def test_validates_strip_trailing_slash(self):
        service = CloudantV1(
            authenticator=NoAuthAuthenticator()
        )
        service.set_service_url('https://cloudant.example/')
        self.assertEqual(service.service_url, 'https://cloudant.example')


def _operation_headers(operation_id):
    return {
        'X-IBMCloud-SDK-Analytics': 'service_name=cloudant;service_version=V1;operation_id={0}'.format(operation_id)
    }


class TestGen1OnlyOperations(unittest.TestCase):

    def setUp(self):
        self.service = CloudantV1(authenticator=NoAuthAuthenticator())
        self.service.set_service_url('https://cloudant.example')

    def _set_env(self, value):
        """Patch the environment for the test, unsetting the variable when value is None."""
        patcher = mock.patch.dict(os.environ)
        patcher.start()
        self.addCleanup(patcher.stop)
        if value is None:
            os.environ.pop(CLOUDANT_SDK_GEN1_ERRORS, None)
        else:
            os.environ[CLOUDANT_SDK_GEN1_ERRORS] = value

    def test_raises_for_every_gen1_only_operation_when_enabled(self):
        self._set_env('true')
        for operation_id in gen1_only_rule.operation_ids:
            with self.subTest(operation_id=operation_id):
                with self.assertRaisesRegex(TypeError, operation_id + '.+unavailable for Gen 2'):
                    self.service.prepare_request('GET', '/', headers=_operation_headers(operation_id))

    def test_raises_from_public_operation_when_enabled(self):
        self._set_env('true')
        with self.assertRaisesRegex(TypeError, 'get_cors_information.+unavailable for Gen 2'):
            self.service.get_cors_information()

    def test_enabled_value_is_case_insensitive(self):
        for value in ('TRUE', 'True', 'tRuE'):
            with self.subTest(value=value):
                self._set_env(value)
                with self.assertRaises(TypeError):
                    self.service.prepare_request('GET', '/', headers=_operation_headers('get_cors_information'))

    def test_does_not_raise_when_not_enabled(self):
        for value in (None, '', 'false', '1', 'yes'):
            with self.subTest(value=value):
                self._set_env(value)
                for operation_id in gen1_only_rule.operation_ids:
                    request = self.service.prepare_request('GET', '/', headers=_operation_headers(operation_id))
                    self.assertIsNotNone(request)

    def test_warning_logged_even_when_root_logger_level_is_error(self):
        self._set_env(None)
        records = []

        class ListHandler(logging.Handler):
            def emit(self, record):
                records.append(record)

        root = logging.getLogger()
        handler = ListHandler()
        original_level = root.level
        root.addHandler(handler)
        root.setLevel(logging.ERROR)
        self.addCleanup(root.removeHandler, handler)
        self.addCleanup(root.setLevel, original_level)

        self.service.prepare_request('GET', '/', headers=_operation_headers('get_cors_information'))

        self.assertEqual(1, len(records))
        self.assertEqual(logging.WARNING, records[0].levelno)
        self.assertIn('get_cors_information', records[0].getMessage())

    def test_other_operations_unaffected_when_enabled(self):
        self._set_env('true')
        request = self.service.prepare_request('GET', '/', headers=_operation_headers('get_server_information'))
        self.assertIsNotNone(request)

    def test_doc_id_validation_still_applies_when_enabled(self):
        self._set_env('true')
        with self.assertRaisesRegex(ValueError, '.+_testDocument.+'):
            self.service.get_document('testDatabase', '_testDocument')
