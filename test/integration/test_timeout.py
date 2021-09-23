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

DEFAULT_TIMEOUT = 150  # 2.5m (=150s)
CUSTOM_TIMEOUT = 10    # 10s
CUSTOM_TIMEOUT_CONFIG = {'timeout': CUSTOM_TIMEOUT}


def get_current_time_plus_two_minute() -> int:
    return int(time.time()) + 120

MOCK_RESPONSE = Response()
MOCK_RESPONSE.status_code = 200
MOCK_RESPONSE._content = '{"foo":"bar"}'.encode()
MOCK_RESPONSE.cookies.set("AuthSession", "bar", expires=get_current_time_plus_two_minute())

class TestTimeout(unittest.TestCase):
    # ** Helpers
    # *************
    def _set_no_timeout(self, new_value: dict):
        new_value['timeout']

    # Every test case tests an authenticator and its default timeout value at first,
    # in the second iteration a custom overwrite possibility is checked.
    def _defineTestCases(self):
        return [
            {
                'assert_func': self._assert_default_timeout_setting,
                'set_timeout': self._set_no_timeout
            },
            {
                'assert_func': self._assert_custom_timeout_setting,
                'set_timeout': self.cloudant.set_http_config
            }
        ]

    def _mock_out_cloudant_request(self, _mock_response=MOCK_RESPONSE):
        self.cloudant.http_client.request = Mock(return_value=_mock_response)

    def _get_authenticate_arguments(self):
        requests.request.assert_called_once()
        return requests.request.mock_calls[0]

    def _get_request_arguments(self, counter):
        self.assertEqual(self.cloudant.http_client.request.call_count, counter + 1)
        return self.cloudant.http_client.request.mock_calls[counter]

    def _assert_default_timeout_setting(self, call_args):
        _, _, kwargs = call_args
        self.assertTrue(isinstance(kwargs['timeout'], Timeout))
        self.assertEqual(kwargs['timeout'].read_timeout, DEFAULT_TIMEOUT)

    def _assert_custom_timeout_setting(self, call_args):
        _, _, kwargs = call_args
        self.assertEqual(kwargs['timeout'], CUSTOM_TIMEOUT)

    # ** CloudantV1
    # *************
    # Check every authenticator type
    def test_timeout_cloudantv1_noauth(self):
        no_auth = NoAuthAuthenticator()
        self.cloudant = CloudantV1(
            authenticator=no_auth
        )

        self._mock_out_cloudant_request()

        testcases = self._defineTestCases()

        for idx, tc in enumerate(testcases):
            tc['set_timeout'](CUSTOM_TIMEOUT_CONFIG)

            # Call the server
            self.cloudant.get_server_information()

            # Assert timeout is set in the server request
            req_args = self._get_request_arguments(idx)
            tc['assert_func'](req_args)

    def test_timeout_cloudantv1_basicauth(self):
        basic_auth = BasicAuthenticator('name', 'psw')
        self.cloudant = CloudantV1(
            authenticator=basic_auth
        )

        # Mock out request response
        self._mock_out_cloudant_request()

        testcases = self._defineTestCases()

        for idx, tc in enumerate(testcases):
            tc['set_timeout'](CUSTOM_TIMEOUT_CONFIG)

            # Call the server
            self.cloudant.get_server_information()

            # Assert timeout is set in the server request
            req_args = self._get_request_arguments(idx)
            tc['assert_func'](req_args)

    def test_timeout_cloudantv1_sessionauth(self, timeout_mock_response=MOCK_RESPONSE):
        session_auth = CouchDbSessionAuthenticator('name', 'psw')
        self.cloudant = CloudantV1(
            authenticator=session_auth,
        )
        self.cloudant.set_service_url("http://cloudant.example")

        # Mock out authentication
        orig_request = requests.request
        requests.request = Mock(return_value=timeout_mock_response)

        # Mock out request response
        self._mock_out_cloudant_request()

        testcases = self._defineTestCases()

        for idx, tc in enumerate(testcases):
            tc['set_timeout'](CUSTOM_TIMEOUT_CONFIG)

            # Call the server
            self.cloudant.get_server_information()

            # Assert timeout is set to the authenticator
            auth_args = self._get_authenticate_arguments()
            self._assert_default_timeout_setting(auth_args)

            # Assert timeout is set in the server request
            req_args = self._get_request_arguments(idx)
            tc['assert_func'](req_args)

        # Set back requests.request
        requests.request = orig_request

    def test_timeout_cloudantv1_iamauth(self, timeout_mock_response=MOCK_RESPONSE):
        authenticator = IAMAuthenticator('apikey')
        self.cloudant = CloudantV1(
            authenticator=authenticator
        )

        # Mock out authentication
        orig_request = requests.request
        requests.request = Mock(return_value=timeout_mock_response)
        self.cloudant.authenticator.token_manager._save_token_info = Mock()
        self.cloudant.authenticator.token_manager.refresh_time = get_current_time_plus_two_minute()

        # Mock out request response
        self._mock_out_cloudant_request()

        testcases = self._defineTestCases()

        for idx, tc in enumerate(testcases):
            tc['set_timeout'](CUSTOM_TIMEOUT_CONFIG)

            # Call the server
            self.cloudant.get_server_information()

            # Assert timeout is set to the authenticator
            auth_args = self._get_authenticate_arguments()
            self._assert_default_timeout_setting(auth_args)

            # Assert timeout is set in the server request
            req_args = self._get_request_arguments(idx)
            tc['assert_func'](req_args)

            # Set expire time to not authenticate again
            self.cloudant.authenticator.token_manager.expire_time = get_current_time_plus_two_minute()

        # Set back requests.request
        requests.request = orig_request

    # ** new_instance
    # ***************
    # For this function no authenticator can be defined programmatically,
    # this way the `SERVER` service is used to check the timeout values.
    def test_timeout_new_instance(self):
        self.cloudant = CloudantV1.new_instance(service_name='SERVER')

        # Mock out request response
        self._mock_out_cloudant_request()

        testcases = self._defineTestCases()

        for idx, tc in enumerate(testcases):
            tc['set_timeout'](CUSTOM_TIMEOUT_CONFIG)

            # Call the server
            self.cloudant.get_server_information()

            # Assert timeout is set in the server request
            req_args = self._get_request_arguments(idx)
            tc['assert_func'](req_args)
