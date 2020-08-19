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
"""
Module to patch sdk core base service for session authentication
"""
from typing import Dict

from requests.cookies import RequestsCookieJar

from ibm_cloud_sdk_core.authenticators import Authenticator
from .common import get_sdk_headers
from .cloudant_v1 import CloudantV1
from .couchdb_session_authenticator import CouchDbSessionAuthenticator

old_init = CloudantV1.__init__

# pylint: disable=missing-function-docstring
def new_init(self, authenticator: Authenticator = None):
    old_init(self, authenticator)
    if isinstance(authenticator, CouchDbSessionAuthenticator):
        # Replacing BaseService's http.cookiejar.CookieJar as RequestsCookieJar supports update(CookieJar)
        self.jar = RequestsCookieJar(self.jar)
        self.authenticator.set_jar(self.jar)  # Authenticators don't have access to cookie jars by default


old_set_service_url = CloudantV1.set_service_url

# pylint: disable=missing-function-docstring
def new_set_service_url(self, service_url: str):
    old_set_service_url(self, service_url)
    try:
        if isinstance(self.authenticator, CouchDbSessionAuthenticator):
            self.authenticator.token_manager.set_service_url(service_url)
    except AttributeError:
        pass  # in case no authenticator is configured yet, pass


old_set_default_headers = CloudantV1.set_default_headers

# pylint: disable=missing-function-docstring
def new_set_default_headers(self, headers: Dict[str, str]):
    old_set_default_headers(self, headers)
    if isinstance(self.authenticator, CouchDbSessionAuthenticator):
        combined_headers = {}
        combined_headers.update(headers)
        combined_headers.update(get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='authenticator_post_session')
        )
        self.authenticator.token_manager.set_default_headers(combined_headers)


old_set_disable_ssl_verification = CloudantV1.set_disable_ssl_verification

# pylint: disable=missing-function-docstring
def new_set_disable_ssl_verification(self, status: bool = False) -> None:
    old_set_disable_ssl_verification(self, status)
    if isinstance(self.authenticator, CouchDbSessionAuthenticator):
        self.authenticator.token_manager.set_disable_ssl_verification(status)
