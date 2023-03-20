# coding: utf-8

#  © Copyright IBM Corporation 2021.
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
from unittest.mock import Mock

from ibm_cloud_sdk_core.authenticators import BasicAuthenticator, IAMAuthenticator, NoAuthAuthenticator
import requests
from requests import Response

from ibmcloudant.cloudant_v1 import CloudantV1
from ibmcloudant.couchdb_session_authenticator import CouchDbSessionAuthenticator

DEFAULT_TIMEOUT = (60, 150)  # 2.5m (=150s)
CUSTOM_TIMEOUT = 10    # 10s
CUSTOM_TIMEOUT_CONFIG = {'timeout': CUSTOM_TIMEOUT}

class Helpers():

    @staticmethod
    def get_current_time_plus_two_minute() -> int:
        return int(time.time()) + 120

    # This mocked response has content that suitable for functionally test
    # both authentication and service requests
    @staticmethod
    def get_mocked_response():
        mock_response = Response()
        mock_response.status_code = 200
        mock_response._content = '{"foo":"bar"}'.encode()
        mock_response.cookies.set("AuthSession", "bar", expires=Helpers.get_current_time_plus_two_minute())
        mock_response.headers.setdefault("Content-Type", "application/json")
        return mock_response

    @staticmethod
    def mock_out_cloudant_request(srv):
        srv.http_client.request = Mock(return_value=Helpers.get_mocked_response())

    # Every test case tests a timeout settings.
    @staticmethod
    def defineTestCases(srv):
        return [
            # 1. case: check default timeout value
            {
                'assert_func': Helpers.assert_default_timeout_setting,
                'set_timeout': Helpers.set_no_timeout
            },
            # 2. case: check custom timeout overwrite
            {
                'assert_func': Helpers.assert_custom_timeout_setting,
                'set_timeout': srv.set_http_config
            }
        ]

    @staticmethod
    def set_no_timeout(new_value: dict):
        new_value['timeout']

    @staticmethod
    def assert_default_timeout_setting(tci, call_args):
        _, _, kwargs = call_args
        tci.assertTrue(isinstance(kwargs['timeout'], tuple))
        tci.assertEqual(kwargs['timeout'], DEFAULT_TIMEOUT)

    @staticmethod
    def assert_custom_timeout_setting(tci, call_args):
        _, _, kwargs = call_args
        tci.assertEqual(kwargs['timeout'], CUSTOM_TIMEOUT)

    @staticmethod
    def get_authenticate_arguments(req):
        req.assert_called_once()
        return req.mock_calls[0]

    @staticmethod
    def get_request_arguments(tci, srv, idx):
        tci.assertEqual(srv.http_client.request.call_count, idx + 1)
        return srv.http_client.request.mock_calls[idx]

# Every method tests an authenticator.
class TestTimeout(unittest.TestCase):
    # ** CloudantV1
    # *************
    def test_timeout_cloudantv1_noauth(self):
        no_auth = NoAuthAuthenticator()
        my_service = CloudantV1(
            authenticator=no_auth
        )

        Helpers.mock_out_cloudant_request(my_service)

        testcases = Helpers.defineTestCases(my_service)

        for tc_num, tc in enumerate(testcases):
            tc['set_timeout'](CUSTOM_TIMEOUT_CONFIG)

            # Call the server
            my_service.get_server_information()

            # Assert timeout is set in the server request
            req_args = Helpers.get_request_arguments(self, my_service, tc_num)
            tc['assert_func'](self, req_args)

    def test_timeout_cloudantv1_basicauth(self):
        basic_auth = BasicAuthenticator('name', 'psw')
        my_service = CloudantV1(
            authenticator=basic_auth
        )

        # Mock out request response
        Helpers.mock_out_cloudant_request(my_service)

        testcases = Helpers.defineTestCases(my_service)

        for tc_num, tc in enumerate(testcases):
            tc['set_timeout'](CUSTOM_TIMEOUT_CONFIG)

            # Call the server
            my_service.get_server_information()

            # Assert timeout is set in the server request
            req_args = Helpers.get_request_arguments(self, my_service, tc_num)
            tc['assert_func'](self, req_args)

    def test_timeout_cloudantv1_sessionauth(self):
        session_auth = CouchDbSessionAuthenticator('name', 'psw')
        my_service = CloudantV1(
            authenticator=session_auth,
        )
        my_service.set_service_url("http://cloudant.example")

        # Mock out authentication
        orig_request = requests.request
        requests.request = Mock(return_value=Helpers.get_mocked_response())

        # Mock out request response
        Helpers.mock_out_cloudant_request(my_service)

        testcases = Helpers.defineTestCases(my_service)

        for tc_num, tc in enumerate(testcases):
            tc['set_timeout'](CUSTOM_TIMEOUT_CONFIG)

            # Call the server
            my_service.get_server_information()

            # Assert timeout is set to the authenticator
            auth_args = Helpers.get_authenticate_arguments(requests.request)
            Helpers.assert_default_timeout_setting(self, auth_args)

            # Assert timeout is set in the server request
            req_args = Helpers.get_request_arguments(self, my_service, tc_num)
            tc['assert_func'](self, req_args)

        # Set back requests.request
        requests.request = orig_request

    def test_timeout_cloudantv1_iamauth(self):
        authenticator = IAMAuthenticator('apikey')
        my_service = CloudantV1(
            authenticator=authenticator
        )

        # Mock out authentication
        orig_request = requests.request
        requests.request = Mock(return_value=Helpers.get_mocked_response())
        my_service.authenticator.token_manager._save_token_info = Mock()
        my_service.authenticator.token_manager.refresh_time = Helpers.get_current_time_plus_two_minute()

        # Mock out request response
        Helpers.mock_out_cloudant_request(my_service)

        testcases = Helpers.defineTestCases(my_service)

        for tc_num, tc in enumerate(testcases):
            tc['set_timeout'](CUSTOM_TIMEOUT_CONFIG)

            # Call the server
            my_service.get_server_information()

            # Assert timeout is set to the authenticator
            auth_args = Helpers.get_authenticate_arguments(requests.request)
            Helpers.assert_default_timeout_setting(self, auth_args)

            # Assert timeout is set in the server request
            req_args = Helpers.get_request_arguments(self, my_service, tc_num)
            tc['assert_func'](self, req_args)

            # Set expire time to not authenticate again
            my_service.authenticator.token_manager.expire_time = Helpers.get_current_time_plus_two_minute()

        # Set back requests.request
        requests.request = orig_request

    # ** new_instance
    # ***************
    # For this function no authenticator can be defined programmatically,
    # this way the `SERVER` service is used to check the timeout values.
    def test_timeout_new_instance(self):
        my_service = CloudantV1.new_instance(service_name='SERVER')

        # Mock out request response
        Helpers.mock_out_cloudant_request(my_service)

        testcases = Helpers.defineTestCases(my_service)

        for tc_num, tc in enumerate(testcases):
            tc['set_timeout'](CUSTOM_TIMEOUT_CONFIG)

            # Call the server
            my_service.get_server_information()

            # Assert timeout is set in the server request
            req_args = Helpers.get_request_arguments(self, my_service, tc_num)
            tc['assert_func'](self, req_args)
