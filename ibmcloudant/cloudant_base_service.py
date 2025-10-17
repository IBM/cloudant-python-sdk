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
Module to patch sdk core base service for session authentication
and other helpful features.
"""
from collections import namedtuple
from typing import Dict, Optional, Union, Tuple, List
from urllib.parse import urlsplit, unquote
from json import dumps
from json.decoder import JSONDecodeError
from io import BytesIO

from ibm_cloud_sdk_core import BaseService
from ibm_cloud_sdk_core.authenticators import Authenticator
from requests import Response, Session
from requests.cookies import RequestsCookieJar

from .common import get_sdk_headers
from .couchdb_session_authenticator import CouchDbSessionAuthenticator

# pylint: disable=missing-docstring

# Define timeout values
CONNECT_TIMEOUT=60
READ_TIMEOUT=150

# Define validations
class ValidationRule(namedtuple('ValidationRule', ['path_segment_index', 'error_parameter_name', 'operation_ids'])):
    __slots__ = ()
    # Use the error_parameter_name as the hash to allow it to be a dict key
    def __hash__(self):
        return self.error_parameter_name.__hash__()

doc_id_rule = ValidationRule(path_segment_index=1, error_parameter_name='Document ID', operation_ids= [
    'delete_document',
    'get_document',
    'get_document_as_mixed',
    'get_document_as_related',
    'get_document_as_stream',
    'head_document',
    'put_document',
    'delete_attachment',
    'get_attachment',
    'head_attachment',
    'put_attachment'
])
att_name_rule = ValidationRule(path_segment_index=2, error_parameter_name='Attachment name', operation_ids= [
    'delete_attachment',
    'get_attachment',
    'head_attachment',
    'put_attachment'
])
rules_by_operation = {}
# Build the rules_by_operation dict of validation rules
for rule in [doc_id_rule, att_name_rule]:
    for operation_id in rule.operation_ids:
        # Use a mapping of operation_id to an ordered set of rules
        # Since Py3.6 dict is ordered so use a key only dict for our set
        rules_by_operation.setdefault(operation_id, dict()).setdefault(rule)

class CloudantBaseService(BaseService):
    """
    The base class for service classes.
    """
    def __init__(
        self,
        service_url: str = None,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the Cloudant service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=service_url, authenticator=authenticator)
        # Overwrite default read timeout to 2.5 minutes
        if not ('timeout' in self.http_config):
            new_http_config = self.http_config.copy()
            new_http_config['timeout'] = (CONNECT_TIMEOUT, READ_TIMEOUT)
            self.set_http_config(new_http_config)
        # Custom actions for CouchDbSessionAuthenticator
        if isinstance(authenticator, CouchDbSessionAuthenticator):
            # Replacing BaseService's http.cookiejar.CookieJar as RequestsCookieJar supports update(CookieJar)
            self.jar = RequestsCookieJar(self.jar)
            self.authenticator.set_jar(self.jar)  # Authenticators don't have access to cookie jars by default
        add_hooks(self)

    def set_service_url(self, service_url: str):
        super().set_service_url(service_url)
        try:
            if isinstance(self.authenticator, CouchDbSessionAuthenticator):
                self.authenticator.token_manager.set_service_url(service_url)
        except AttributeError:
            pass  # in case no authenticator is configured yet, pass

    def set_default_headers(self, headers: Dict[str, str]):
        super().set_default_headers(headers)
        if isinstance(self.authenticator, CouchDbSessionAuthenticator):
            combined_headers = {}
            combined_headers.update(headers)
            combined_headers.update(get_sdk_headers(
                service_name=self.DEFAULT_SERVICE_NAME,
                service_version='V1',
                operation_id='authenticator_post_session')
            )
            self.authenticator.token_manager.set_default_headers(combined_headers)

    def set_disable_ssl_verification(self, status: bool = False) -> None:
        super().set_disable_ssl_verification(status)
        if isinstance(self.authenticator, CouchDbSessionAuthenticator):
            self.authenticator.token_manager.set_disable_ssl_verification(status)

    def set_http_client(self, http_client: Session) -> None:
        super().set_http_client(http_client)
        add_hooks(self)

    def prepare_request(self,
                            method: str,
                            url: str,
                            *args,
                            headers: Optional[dict] = None,
                            params: Optional[dict] = None,
                            data: Optional[Union[str, dict]] = None,
                            files: Optional[Union[Dict[str, Tuple[str]],
                                                List[Tuple[str,
                                                            Tuple[str,
                                                                ...]]]]] = None,
                            **kwargs) -> dict:
        # Extract the operation ID from the request headers.
        operation_id = None
        header = headers.get('X-IBMCloud-SDK-Analytics')
        if header is not None:
            for element in header.split(';'):
                if element.startswith('operation_id'):
                    operation_id = element.split('=')[1]
                    break
        if operation_id is not None:
            # Check each validation rule that applies to the operation.
            # Until the request URL is passed to old_prepare_request it does not include the
            # service URL and is relative to it
            request_url_path_segments = urlsplit(url).path.strip('/').split('/')
            if len(request_url_path_segments) == 1 and request_url_path_segments[0] == '':
                request_url_path_segments = []
            # Note the get returns a value-less dict, we are iterating only the keys
            for rule in rules_by_operation.get(operation_id, {}):
                if len(request_url_path_segments) > rule.path_segment_index:
                    segment_to_validate = request_url_path_segments[rule.path_segment_index]
                    if segment_to_validate.startswith('_'):
                        raise ValueError('{0} {1} starts with the invalid _ character.'.format(rule.error_parameter_name,
                            unquote(segment_to_validate)))
        return super().prepare_request(method, url, *args, headers=headers, params=params, data=data, files=files, **kwargs)

def _error_response_hook(response:Response, *args, **kwargs) -> Optional[Response]:
    # pylint: disable=W0613
    # unused args and kwargs required by requests event hook interface
    """Function for augmenting error responses.
    Converts the Cloudant response to better match the
    standard error response formats including adding a
    trace ID and appending the Cloudant/CouchDB error
    reason to the message.

    Follows the requests event hook pattern.

    :param response: the requests Response object
    :type response: Response

    :return: A new response object, defaults to the existing response
    :rtype: Response,optional
    """
    # Only hook into error responses
    # Ignore HEAD request responses because there is no body to read
    if not response.ok and response.request.method != 'HEAD':
        content_type = response.headers.get('content-type')
        # If it isn't JSON don't mess with it!
        if content_type is not None and content_type.startswith('application/json'):
            try:
                error_json: dict = response.json()
                # Only augment if there isn't a trace or errors already
                send_augmented_response = False
                if 'trace' not in error_json:
                    if 'errors' not in error_json:
                        error = error_json.get('error')
                        reason = error_json.get('reason')
                        if error is not None:
                            error_model: dict = {'code': error, 'message': f'{error}'}
                            if reason:
                                error_model['message'] += f': {reason}'
                            error_json['errors'] = [error_model]
                            send_augmented_response = True
                    if 'errors' in error_json:
                        # Get the x-request-id header if available
                        # otherwise try the x-couch-request-id header
                        trace = response.headers.get('x-request-id',
                                    response.headers.get('x-couch-request-id'))
                        if trace is not None:
                            # Augment trace if there was a value
                            error_json['trace'] = trace
                            send_augmented_response = True
                    if send_augmented_response:
                        # It'd be nice to just change content on response, but it's internal.
                        # Instead copy the named attributes to a new Response and then set
                        # the encoding and bytes of the modified error body.
                        error_response = Response()
                        error_response.status_code = response.status_code
                        error_response.headers = response.headers
                        error_response.url = response.url
                        error_response.history = response.history
                        error_response.reason = response.reason
                        error_response.cookies = response.cookies
                        error_response.elapsed = response.elapsed
                        error_response.request = response.request
                        error_response.encoding = 'utf-8'
                        error_response.raw = BytesIO(dumps(error_json).encode('utf-8'))
                        return error_response
            except JSONDecodeError:
                # If we couldn't read the JSON we just return the response as-is
                # so the exception can surface elsewhere.
                pass
    return response
def add_hooks(self):
    response_hooks = self.get_http_client().hooks['response']
    if _error_response_hook not in response_hooks:
        response_hooks.append(_error_response_hook)
