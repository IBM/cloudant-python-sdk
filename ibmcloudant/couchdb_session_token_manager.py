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
Module for managing session authentication token
"""
from ibm_cloud_sdk_core.token_manager import TokenManager


class CouchDbSessionTokenManager(TokenManager):
    """The SessionTokenManager takes a username and password and performs the necessary interactions with
    the CouchDB service to obtain and store a session token.

    If the current stored session token has expired a new session token will be retrieved.

    This class is used by CouchDbSessionAuthenticator and is internal.

    Attributes:
        url (str): The CouchDB service URL for token requests.
        username (str): The CouchDB username to obtain the session token for
        password (str): The CouchDB password to obtain the session token for
        http_config (dict): A dictionary containing values that control the timeout, proxies, and etc of HTTP requests.
        headers (dict): A dictionary containing values that specify custom headers used for HTTP requests.

    Args:
        username: The CouchDB username to obtain the session token for
        password: The CouchDB password to obtain the session token for
    """

    def __init__(self, username: str, password: str,
                 url: str = None,
                 ):
        super().__init__(url)
        self.username = username
        self.password = password

        self.token = None

        self.http_config = {}
        self.headers = None

    def request_token(self):
        """Request a CouchDB session token given an username and password.


        Returns:
             A CookieJar of Cookies the server sent back.
        """

        response = self._request(
            method='POST',
            url=self.url + "/_session",
            headers=self.headers,
            data={
                'name': self.username,
                'password': self.password,
            }
        )

        return response

    def _save_token_info(self, token_response) -> None:
        """
        Decode the access token and save the response from the service to the object's state

        Refresh time is set to approximately 80% of the token's TTL to ensure that
        the token refresh completes before the current token expires.

        Parameters
        ----------
        token_response : dict
            Response from token service
        """
        self.access_token = token_response.cookies
        cookie = next(x for x in self.access_token if x.name == 'AuthSession')
        exp = cookie.expires
        iat = self._get_current_time()
        self.expire_time = exp
        ttl = exp - iat
        buffer = ttl * 0.2
        self.refresh_time = self.expire_time - buffer

    def set_service_url(self, service_url):
        self.url = service_url
        self.expire_time = 0

    def set_default_headers(self, headers):
        self.headers = headers
