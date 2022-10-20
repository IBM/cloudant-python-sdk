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
Module to patch sdk core authenticator for session authentication
"""
from .couchdb_session_authenticator import CouchDbSessionAuthenticator
from ibm_cloud_sdk_core import get_authenticator

old_construct_authenticator = get_authenticator.__construct_authenticator


def new_construct_authenticator(config):  # pylint: disable=missing-docstring
    if config.get('AUTH_TYPE'):
        auth_type = config.get('AUTH_TYPE').upper()
    elif config.get('AUTHTYPE'):
        auth_type = config.get('AUTHTYPE').upper()
    else:
        auth_type = ''

    if auth_type == 'COUCHDB_SESSION':
        return CouchDbSessionAuthenticator(
            username=config.get('USERNAME'),
            password=config.get('PASSWORD'),
            disable_ssl_verification=config.get(
                'AUTH_DISABLE_SSL',
                config.get('DISABLE_SSL', 'false')).lower() == 'true'
        )
    return old_construct_authenticator(config)
