# coding: utf-8

# © Copyright IBM Corporation 2020, 2025.
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
Module for handling session authentication
"""
from requests import Request, Session
from requests.cookies import RequestsCookieJar


from ibm_cloud_sdk_core.authenticators import Authenticator
from .couchdb_session_token_manager import CouchDbSessionTokenManager


class CouchDbSessionAuthenticator(Authenticator):
    """The CouchDbSessionAuthenticator utilizes a server url and a username and password pair to
    obtain a session token, and adds it to requests.

    Args:
        username: The CouchDB username
        password: The CouchDB password

    Attributes: token_manager (ibmcloudantsdk.couchdb_session_token_manager.CouchDbSessionTokenManager): Retrieves
    and manages CouchDB session tokens.

    Raises:
        ValueError: The supplied username, and/or password are not valid.
    """

    AUTHTYPE_COUCHDB_SESSION = 'COUCHDB_SESSION'

    def __init__(self,
                 username: str,
                 password: str,
                 disable_ssl_verification: bool = False) -> None:
        if not isinstance(disable_ssl_verification, bool):
            raise TypeError('disable_ssl_verification must be a bool')

        self.token_manager = CouchDbSessionTokenManager(
            username,
            password,
            disable_ssl_verification=disable_ssl_verification
        )
        self.validate()

    def _set_http_client(self, http_client: Session, jar: RequestsCookieJar) -> None:
        """Sets base serivice's http client for the authenticator.
        This is an internal method called by BaseService. Not to be called directly.
        """
        if isinstance(http_client, Session):
            self.token_manager.http_client = http_client
            self.token_manager.jar = jar
        else:
            raise TypeError("http_client parameter must be a requests.sessions.Session")

    def validate(self):
        """Validates the username, and password for session token requests.

        Ensure both the username and password are set.

        Raises:
            ValueError: The supplied username, and/or password are not valid.
        """
        if self.token_manager.username is None or self.token_manager.username == '':
            raise ValueError('The username shouldn\'t be None or empty.')
        if self.token_manager.password is None:
            raise ValueError('The password shouldn\'t be None.')

    def authenticate(self, req: Request):
        """Adds session authentication information to the request.

        The session token will be added as an update to the BaseService cookie jar.

        Args:
            req: Ignored. BaseService uses the cookie jar for every request
        """
        self.token_manager.get_token()

    def authentication_type(self) -> str:
        """Returns this authenticator's type ('COUCHDB_SESSION')."""
        return CouchDbSessionAuthenticator.AUTHTYPE_COUCHDB_SESSION
