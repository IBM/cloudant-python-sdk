# coding: utf-8

# © Copyright IBM Corporation 2020.
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

import datetime
import json
import unittest
from unittest import mock

import requests
import responses
import time

from ibmcloudant import CouchDbSessionAuthenticator
from ibmcloudant.cloudant_v1 import CloudantV1

request = requests.request
request_args = None
request_kwargs = None


class MockSession(requests.sessions.Session):
    def __init__(self):
        super().__init__()
        self.last_verify = None

    def request(self, *args, **kwargs):
        if 'verify' in kwargs:
            self.last_verify = kwargs['verify']
        return super().request(*args, **kwargs)


class TestCouchDbSessionAuth(unittest.TestCase):

    def setUp(self) -> None:
        self.cookie_value = "foobar"
        self.cookie_expire_time = "Tue, 26-May-2020 14:37:56 GMT"

        self.authenticator = CouchDbSessionAuthenticator("adm", "pass")
        self.client = CloudantV1(self.authenticator)
        self.prepare_for_url('http://cloudant.example')

    def prepare_for_url(self, url):
        def post_session(request):
            return (200, {
                "Set-Cookie": "AuthSession=" + self.cookie_value + ";  Version=1; Expires=" +
                              self.cookie_expire_time + "; Max-Age=600; Path=/; HttpOnly"},
                    json.dumps({"ok": True, "name": "adm", "roles": ["_admin"]}))

        responses.add_callback(responses.POST, url + '/_session', post_session)
        responses.add(responses.GET, url + '/_session',
                      json={"ok": True, "userCtx": {"name": "adm", "roles": ["_admin"]},
                            "info": {"authentication_db": "_users", "authentication_handlers": ["cookie", "default"],
                                     "authenticated": "cookie"}}
                      , status=200)
        self.client.set_service_url(url)

    @responses.activate
    def test_header_passing(self):
        self.client.set_default_headers({"yes": "works"})
        response = self.client.get_session_information(headers={"foo": "bar"})
        self.assertIsNotNone(response)
        result = response.get_result()
        self.assertIsNotNone(result)
        self.assertEqual(responses.calls[0].request.headers["yes"], "works")
        self.assertEqual(responses.calls[0].request.method, "POST")
        self.assertEqual("service_name=cloudant;service_version=V1;operation_id=authenticator_post_session",
                         responses.calls[0].request.headers['X-IBMCloud-SDK-Analytics'],
                         )  # POST /_session agent headers
        self.assertEqual(responses.calls[1].request.headers["foo"], "bar")
        self.assertEqual(responses.calls[1].request.method, "GET")
        self.assertEqual(responses.calls[1].request.headers["yes"], "works")

    @responses.activate
    def test_disable_ssl_verification_on(self):
        original_http_client = self.client.get_http_client()
        mock_session = MockSession()
        try:
            self.client.set_http_client(mock_session)
            self.client.set_disable_ssl_verification(True)
            self.client.get_session_information()
            assert mock_session.last_verify is False
        finally:
            self.client.set_http_client(original_http_client)

    @responses.activate
    def test_disable_ssl_verification_off(self):
        original_http_client = self.client.get_http_client()
        mock_session = MockSession()
        try:
            self.client.set_http_client(mock_session)
            self.client.set_disable_ssl_verification(False)
            self.client.get_session_information()
            assert mock_session.last_verify is None
        finally:
            self.client.set_http_client(original_http_client)

    @responses.activate
    def test_cookie_refresh(self):
        self.client.get_session_information()
        self.assertEqual(responses.calls[-1].request.headers["Cookie"], "AuthSession=foobar")
        self.cookie_value = "bar"
        self.authenticator.token_manager.refresh_time = 0
        self.client.get_session_information()
        self.assertEqual(responses.calls[-1].request.headers["Cookie"], "AuthSession=bar")

        self.assertNotEqual(self.authenticator.token_manager.refresh_time, 0)
        self.cookie_value = "bar2"
        self.authenticator.token_manager.refresh_time = 0
        self.client.get_session_information()
        self.assertEqual(responses.calls[-1].request.headers["Cookie"], "AuthSession=bar2")

    @responses.activate
    def test_cookie_expired(self):
        self.client.get_session_information()
        self.assertEqual(responses.calls[-1].request.headers["Cookie"], "AuthSession=foobar")
        self.cookie_value = "bar"
        self.authenticator.token_manager.expire_time = 0
        self.assertTrue(self.authenticator.token_manager._is_token_expired())
        self.client.get_session_information()
        self.assertEqual(responses.calls[-1].request.headers["Cookie"], "AuthSession=bar")

    @responses.activate
    def test_cookie_not_yet_expired(self):
        self.client.get_session_information()
        self.assertEqual(responses.calls[-1].request.headers["Cookie"], "AuthSession=foobar")
        self.cookie_value = "bar"
        self.authenticator.token_manager.expire_time = float("inf")
        self.assertFalse(self.authenticator.token_manager._is_token_expired())
        self.client.get_session_information()
        self.assertEqual(responses.calls[-1].request.headers["Cookie"], "AuthSession=foobar")

    @responses.activate
    def test_refresh_time_calculation(self):
        self.cookie_expire_time = datetime.datetime.fromtimestamp(time.time() + 10 * 60).strftime(
            "%a, %d-%b-%Y %H:%M:%S %Z")
        self.client.get_session_information()
        self.assertAlmostEqual(self.authenticator.token_manager.refresh_time,
                               self.authenticator.token_manager._get_current_time() + 8 * 60, delta=3)

    @responses.activate
    def test_set_service_url(self):
        self.client.get_session_information()
        self.assertEqual(responses.calls[-2].request.url, "http://cloudant.example/_session")
        self.assertEqual(responses.calls[-2].request.method, "POST")
        self.assertEqual(responses.calls[-1].request.url, "http://cloudant.example/_session")
        self.assertEqual(responses.calls[-1].request.method, "GET")
        self.prepare_for_url('http://cloudant2.example')
        self.client.get_session_information()
        self.assertEqual(responses.calls[-2].request.url, "http://cloudant2.example/_session")
        self.assertEqual(responses.calls[-2].request.method, "POST")
        self.assertEqual(responses.calls[-1].request.url, "http://cloudant2.example/_session")
        self.assertEqual(responses.calls[-1].request.method, "GET")
