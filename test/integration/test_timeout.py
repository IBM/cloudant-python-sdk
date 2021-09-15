#  © Copyright IBM Corporation 2020.
#  #
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  #
#       http://www.apache.org/licenses/LICENSE-2.0
#  #
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import time
import unittest

import requests
from unittest.mock import Mock
from requests import Response
from urllib3 import Timeout

from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator, IAMAuthenticator, NoAuthAuthenticator
from ibmcloudant.couchdb_session_authenticator import CouchDbSessionAuthenticator

class TestTimeout(unittest.TestCase):

# ** Helpers
# *************

    _timeout_mock_response = Response()
    _timeout_mock_response.status_code=200
    _timeout_mock_response._content = '{"foo":"bar"}'.encode()
    _timeout_mock_response.cookies.set("AuthSession", "bar", expires=time.time()+120)

    def _mock_out_cloudant_request(self, _mock_response=_timeout_mock_response):
        self.cloudant.http_client.request = Mock(return_value=_mock_response)

    def _get_authenticate_arguments(self):
        requests.request.assert_called_once()
        first_call = requests.request.mock_calls[0]
        return first_call

    def _get_request_arguments(self):
        self.cloudant.http_client.request.assert_called_once()
        return self.cloudant.http_client.request.mock_calls[0]

    def _assert_default_timeout_setting(self, call_args):
        _, _, kwargs = call_args
        self.assertTrue(isinstance(kwargs['timeout'], Timeout))
        self.assertEqual(kwargs['timeout'].read_timeout, 150)

    def _assert_custom_timeout_setting(self, call_args):
        _, _, kwargs = call_args
        self.assertEqual(kwargs['timeout'], 10)


# ** CloudantV1
# *************

    def test_timeout_cloudantV1_NoAuth(self):
        authenticator = NoAuthAuthenticator()
        self.cloudant = CloudantV1(
            authenticator=authenticator
        )

        self._mock_out_cloudant_request()

        self.cloudant.get_server_information()

        # Assert request arguments, here the timeout should be included
        req_args=self._get_request_arguments()
        self._assert_default_timeout_setting(req_args)

    def test_timeout_cloudantV1_IAMAuth(self, timeout_mock_response=_timeout_mock_response):
        authenticator = IAMAuthenticator('apikey')
        self.cloudant = CloudantV1(
            authenticator=authenticator
        )

        # Mock out authentication
        orig_request = requests.request
        requests.request = Mock(return_value=timeout_mock_response)
        self.cloudant.authenticator.token_manager._save_token_info=Mock()
        self.cloudant.authenticator.token_manager.refresh_time = int(time.time()) + 60

        # Mock out request response
        self._mock_out_cloudant_request()

        # Call the server
        self.cloudant.get_server_information()

        # Assert timeout is set to the authenticator
        auth_args = self._get_authenticate_arguments()
        self._assert_default_timeout_setting(auth_args)
        # Set back requests.request
        requests.request = orig_request

        # Assert timeout is set in the server request
        req_args=self._get_request_arguments()
        self._assert_default_timeout_setting(req_args)

    # Check Basic - no authentication request case like `NoAuth`
    def test_timeout_cloudantV1_BasicAuth(self):
        authenticator = BasicAuthenticator('name', 'psw')
        self.cloudant = CloudantV1(
            authenticator=authenticator
        )

        # Mock out request response
        self._mock_out_cloudant_request()

        # Call the server
        self.cloudant.get_server_information()

        # Assert timeout is set in the server request
        req_args=self._get_request_arguments()
        self._assert_default_timeout_setting(req_args)

    def test_timeout_cloudantV1_SessionAuth(self, timeout_mock_response=_timeout_mock_response):
        authenticator = CouchDbSessionAuthenticator('name', 'psw')
        self.cloudant = CloudantV1(
            authenticator=authenticator,
        )
        self.cloudant.set_service_url("http://cloudant.example")

        # Mock out authentication
        orig_request = requests.request
        requests.request = Mock(return_value=timeout_mock_response)

        # Mock out request response
        self._mock_out_cloudant_request()

        # Call the server
        self.cloudant.get_server_information()

        # Assert timeout is set to the authenticator
        auth_args = self._get_authenticate_arguments()
        self._assert_default_timeout_setting(auth_args)
        # Set back requests.request
        requests.request = orig_request

        # Assert timeout is set in the server request
        req_args=self._get_request_arguments()
        self._assert_default_timeout_setting(req_args)

# ** new_instance
# ***************

    def test_timeout_new_instance(self):
        self.cloudant = CloudantV1.new_instance(service_name='SERVER')

        # Mock out request response
        self._mock_out_cloudant_request()

        # Call the server
        self.cloudant.get_server_information()

        # Assert timeout is set in the server request
        req_args=self._get_request_arguments()
        self._assert_default_timeout_setting(req_args)

# ** Allow timeout overwrite
# ***************

    def test_timeout_new_instance_overwrite(self):
        self.cloudant = CloudantV1.new_instance(service_name='SERVER')

        # Overwrite timeout
        self.cloudant.set_http_config({'timeout':10})

        # Mock out request response
        self._mock_out_cloudant_request()

        # Call the server
        self.cloudant.get_server_information()

        # Assert timeout is set in the server request
        req_args=self._get_request_arguments()
        self._assert_custom_timeout_setting(req_args)

    def test_timeout_cloudantV1_IAMAuth_overwrite(self, timeout_mock_response=_timeout_mock_response):
        authenticator = IAMAuthenticator('apikey')
        self.cloudant = CloudantV1(
            authenticator=authenticator
        )

        # Overwrite timeout
        self.cloudant.set_http_config({'timeout':10})

        # Mock out authentication
        orig_request = requests.request
        requests.request = Mock(return_value=timeout_mock_response)
        self.cloudant.authenticator.token_manager._save_token_info=Mock()
        self.cloudant.authenticator.token_manager.refresh_time = int(time.time()) + 60

        # Mock out request response
        self._mock_out_cloudant_request()

        # Call the server
        self.cloudant.get_server_information()

        # Assert timeout is set to the authenticator
        auth_args = self._get_authenticate_arguments()
        self._assert_custom_timeout_setting(auth_args)

        # Set back requests.request
        requests.request = orig_request

        # Assert timeout is set in the server request
        req_args=self._get_request_arguments()
        self._assert_custom_timeout_setting(req_args)


