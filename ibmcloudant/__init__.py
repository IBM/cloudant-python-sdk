# coding: utf-8
# © Copyright IBM Corporation 2020, 2021.
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

"""Python client library for the IBM Cloudant"""

# Ignore warnings about unaccesed imports in this block, they are needed for the core patches
from ibm_cloud_sdk_core import IAMTokenManager, DetailedResponse, BaseService, ApiException, get_authenticator
from .couchdb_session_authenticator import CouchDbSessionAuthenticator
from .couchdb_session_get_authenticator_patch import new_construct_authenticator
from .cloudant_base_service import new_init, new_prepare_request, new_set_service_url, new_set_default_headers
from .couchdb_session_token_manager import CouchDbSessionTokenManager
from .cloudant_v1 import CloudantV1

# sdk-core's __construct_authenticator works with a long switch-case so monkey-patching is required
get_authenticator.__construct_authenticator = new_construct_authenticator

CloudantV1.__init__ = new_init

CloudantV1.set_service_url = new_set_service_url

CloudantV1.set_default_headers = new_set_default_headers

CloudantV1.prepare_request = new_prepare_request
