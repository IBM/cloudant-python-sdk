# coding: utf-8

# © Copyright IBM Corporation 2024.
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

from typing import Any, Literal, TypedDict
import responses
import unittest
from json.decoder import JSONDecodeError
from ibm_cloud_sdk_core import ApiException
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibmcloudant.cloudant_v1 import *
from ibmcloudant.cloudant_base_service import _error_response_hook

class MockResponse(TypedDict):
    body: Union[dict[str,Any], str, bytes, None]
    headers: dict[str, str]
    status: int
    stream: bool

class ExpectedResponse(TypedDict, total=False):
    body: Union[dict[str,Any], str, bytes, None]
    message: str # not required (but can't be marked that way until 3.11)

class TestErrorAugment(unittest.TestCase):

    _base_url = 'https://~replace-with-cloudant-host~.cloudantnosqldb.appdomain.cloud'
    _db_name = 'testdb'
    _doc_id = 'testdoc'
    _req_id = 'testreqid'
    _error_name = 'test_value'
    _error_reason = 'A valid test reason'
    _content_type_header = {'content-type': 'application/json'}
    _request_id_header = {'x-couch-request-id': _req_id}
    _default_mock_headers = _content_type_header | _request_id_header
    _error_only_body = {'error': _error_name}
    _error_reason_body = {'error': _error_name, 'reason': _error_reason}
    _errors_error_only = {'errors': [{'code': _error_name, 'message': _error_name}]}
    _errors_error_reason = {'errors': [{'code': _error_name, 'message': f'{_error_name}: {_error_reason}'}]}
    _trace = {'trace': _req_id}

    @classmethod
    def setUpClass(cls):
        cls._service = CloudantV1(
            authenticator=NoAuthAuthenticator()
        )
        cls._service.set_service_url(cls._base_url)

    def _make_request(self, method: Literal['GET','HEAD'], stream: bool):
        if method == responses.GET:
            if stream:
                return self._service.get_document_as_stream(self._db_name, self._doc_id)
            else:
                return self._service.get_document(self._db_name, self._doc_id)
        elif method == responses.HEAD:
            return self._service.head_document(self._db_name, self._doc_id)
        else:
            raise Exception('Only GET and HEAD requests expected.')

    def _expected_message_from_mock_response(self, mock_response: MockResponse):
        body = mock_response['body']
        status_code = mock_response['status']
        err = body['error']
        msg: str = f'Error: {err}'
        if 'reason' in body:
            reason = body['reason']
            msg += f': {reason}'
        msg += f', Status code: {status_code}'
        return msg

    def _run_test(
              self,
              method: Literal['GET', 'HEAD'] = responses.GET,
              mock_response: MockResponse = {
                  'body': _error_reason_body,
                  'headers': _default_mock_headers,
                  'status': 444,
                  'stream': False
                  },
              expected_response: ExpectedResponse = None
        ) -> Union[Exception, None]:

            if expected_response is None:
                # Default to a no-augment body pass-through
                expected_response = {
                    'body': mock_response['body']
                }

            if mock_response['status'] == 200:
                expect_raises = False
            else:
                expect_raises = True
                if 'message' not in expected_response:
                    expected_response['message'] = self._expected_message_from_mock_response(mock_response)

            if isinstance(mock_response['body'], dict):
                # stringify dict responses
                mock_response['body'] = json.dumps(mock_response['body'])

            caught_exception = None
            with responses.RequestsMock(response_callback=self._response_callback) as mock_ctx:
                # Add the mock response
                # Copy the headers so we can remove content-type for responses preferred format
                mock_response['headers'] = dict(mock_response['headers'])
                mock_content_type = mock_response['headers'].pop('content-type', None)
                mock_ctx.add(
                    method,
                    url=self._base_url + f'/{self._db_name}/{self._doc_id}',
                    content_type=mock_content_type,
                    **mock_response
                )
                if expect_raises:
                    with self.assertRaisesRegex(ApiException, expected_response['message']) as e_ctx:
                        self._make_request(method, mock_response['stream'])
                    caught_exception = e_ctx.exception
                    actual_status_code = caught_exception.status_code
                    actual_headers = caught_exception.http_response.headers
                    # Default to raw body
                    actual_body = caught_exception.http_response.content
                    if method != 'HEAD' and mock_content_type:
                        if mock_content_type.startswith('application/json'):
                            try:
                                actual_body = caught_exception.http_response.json()
                            except JSONDecodeError:
                                # Catch the malformed JSON case
                                actual_body = caught_exception.http_response.text
                        elif mock_content_type == 'text/plain':
                            actual_body = caught_exception.http_response.text
                else:
                    try:
                        service_response = self._make_request(method, mock_response['stream'])
                        actual_status_code = service_response.get_status_code()
                        actual_headers = service_response.get_headers()
                        actual_body = service_response.get_result()
                    except Exception as e:
                        raise Exception('There should be no exception raised in this case.') from e
                # Assert expected status_code
                self.assertEqual(mock_response['status'], actual_status_code)
                # Assert headers unchanged, re-adding the content-type we had to pop for responses mock
                if mock_content_type:
                    expected_headers = mock_response['headers'] | {'content-type': mock_content_type}
                else:
                    expected_headers = mock_response['headers']
                self.assertEqual(expected_headers, actual_headers)
                # Assert expected body
                self.assertEqual(expected_response['body'], actual_body)
                return caught_exception

    # Responses mocking doesn't actually go through requests it presents
    # a requests like API. This means the requests event hooks aren't called
    # when mocking with responses. However, the response_callback behaves like
    # requests response event hook so we use it to invoke our _error_response_hook
    # during testing.
    @classmethod
    def _response_callback(cls, resp):
        return _error_response_hook(resp)

    def test_response_hook_added(self):
        self.assertEqual(_error_response_hook, self._service.get_http_client().hooks['response'][0])

    def test_response_hook_not_double_added_via_set_http_client(self):
        client = self._service.get_http_client()
        self._service.set_http_client(client)
        response_hooks =  self._service.get_http_client().hooks['response']
        self.assertEqual(1, len(response_hooks))
        self.assertEqual(_error_response_hook, response_hooks[0])

    def test_response_hook_added_via_set_http_client(self):
        client = self._service.get_http_client()
        client.hooks['response'].clear()
        self._service.set_http_client(client)
        response_hooks =  self._service.get_http_client().hooks['response']
        self.assertEqual(1, len(response_hooks))
        self.assertEqual(_error_response_hook, response_hooks[0])

    def test_augment_error(self):
        self._run_test(
            mock_response={
                'body': self._error_only_body,
                'headers': self._content_type_header,
                'status': 444,
                'stream': False
            },
            expected_response={
                'body': self._error_only_body | self._errors_error_only
            }
        )

    def test_augment_error_with_trace(self):
        self._run_test(
            mock_response={
                'body': self._error_only_body,
                'headers': self._default_mock_headers,
                'status': 444,
                'stream': False
            },
            expected_response={
                'body': self._error_only_body | self._errors_error_only | self._trace
            }
        )

    def test_augment_error_reason(self):
        self._run_test(
            mock_response={
                'body': self._error_reason_body,
                'headers': self._content_type_header,
                'status': 444,
                'stream': False
            },
            expected_response={
                'body': self._error_reason_body | self._errors_error_reason
            }
        )

    def test_augment_error_reason_with_trace(self):
        self._run_test(
            mock_response={
                'body': self._error_reason_body,
                'headers': self._default_mock_headers,
                'status': 444,
                'stream': False
            },
            expected_response={
                'body': self._error_reason_body | self._errors_error_reason | self._trace
            }
        )

    def test_augment_error_reason_stream(self):
        self._run_test(
            mock_response={
                'body': self._error_reason_body,
                'headers': self._default_mock_headers,
                'status': 444,
                'stream': True
            },
            expected_response={
                'body': self._error_reason_body | self._errors_error_reason | self._trace
            }
        )

    def test_augment_json_charset(self):
        self._run_test(
            mock_response={
                'body': self._error_reason_body,
                'headers': self._request_id_header | {'content-type': 'application/json; charset=utf-8'},
                'status': 444,
                'stream': False
            },
            expected_response={
                'body': self._error_reason_body | self._errors_error_reason | self._trace
            }
        )

    def test_augment_no_header(self):
        self._run_test(
            mock_response={
                'body': self._error_reason_body,
                'headers': self._content_type_header,
                'status': 444,
                'stream': False
            },
            expected_response={
                'body': self._error_reason_body | self._errors_error_reason
            }
        )

    def test_no_augment_success(self):
        self._run_test(
            mock_response={
                'body': {'_id': self._doc_id, '_rev': '1-abc', 'foo': 'bar'},
                'headers': self._default_mock_headers,
                'status': 200,
                'stream': False
            }
        )

    def test_no_augment_head(self):
        self._run_test(
            method=responses.HEAD,
            mock_response={
                'body': None,
                'headers': self._default_mock_headers,
                'status': 444,
                'stream': False
            },
            expected_response={
                'body': b'', # no body content for HEAD
                'message': 'Error: Unknown error, Status code: 444'
            }
        )

    def test_no_augment_id_only(self):
        self._run_test(
            mock_response={
                'body': {},
                'headers': self._default_mock_headers,
                'status': 444,
                'stream': False
            },
            expected_response={
                'body': {},
                'message': 'Error: {}, Status code: 444'
            }
        )

    def test_no_augment_existing_trace(self):
        test_body = {
            'trace': 'testanotherreqid',
            'error': 'too_many_requests',
            'reason': 'Buy a bigger plan.'
        }
        self._run_test(
            mock_response={
                'body': test_body,
                'headers': self._default_mock_headers,
                'status': 429,
                'stream': False
            },
            expected_response={
                'body': test_body,
                'message': 'Error: too_many_requests, Status code: 429'
            }
        )

    def test_no_augment_existing_errors_no_id(self):
        test_body = {
            'errors': [
                {
                    'code': 'forbidden',
                    'message':'forbidden: You must have _reader to access this resource.'
                }],
            'error': 'forbidden', # error for use by assertion
            'reason': 'You must have _reader to access this resource.' # reason for use by assertion
        }
        self._run_test(
            mock_response={
                'body': test_body,
                'headers': self._content_type_header,
                'status': 403,
                'stream': False
            },
            expected_response={
                'body': test_body,
            }
        )

    def test_augment_trace_existing_errors(self):
        test_body = {
            'errors': [
                {
                    'code': 'forbidden',
                    'message':'forbidden: You must have _reader to access this resource.'
                }],
            'error': 'forbidden', # error for use by assertion
            'reason': 'You must have _reader to access this resource.' # reason for use by assertion
        }
        self._run_test(
            mock_response={
                'body': test_body,
                'headers': self._default_mock_headers,
                'status': 403,
                'stream': False
            },
            expected_response={
                'body': test_body | self._trace
            }
        )

    def test_no_augment_non_json(self):
        test_body = 'foo'
        self._run_test(
            mock_response={
                'body': test_body,
                'headers': self._request_id_header | {'content-type': 'text/plain'},
                'status': 400,
                'stream': False
            },
            expected_response={
                'body': test_body,
                'message': f'Error: {test_body}, Status code: 400'
            }
        )

    def test_no_augment_no_content_type(self):
        test_body = b'000'
        self._run_test(
            mock_response={
                'body': test_body,
                'headers': self._request_id_header,
                'status': 444,
                'stream': False
            },
            expected_response={
                'body': test_body,
                'message': 'Error: 000, Status code: 444'
            }
        )

    def test_no_augment_no_error(self):
        test_body = {'foo':'bar', 'reason': 'testing'}
        self._run_test(
            mock_response={
                'body': test_body,
                'headers': self._default_mock_headers,
                'status': 400,
                'stream': False
            },
            expected_response={
                'body': test_body,
                'message': 'Error: Bad Request, Status code: 400'
            }
        )

    def test_no_augment_no_error_no_header(self):
        test_body = {'foo':'bar', 'reason': 'testing'}
        self._run_test(
            mock_response={
                'body': test_body,
                'headers': self._content_type_header,
                'status': 400,
                'stream': False
            },
            expected_response={
                'body': test_body,
                'message': 'Error: Bad Request, Status code: 400'
            }
        )

    def test_no_augment_invalid_json(self):
        test_body = '{"err'
        e = self._run_test(
            mock_response={
                'body': test_body,
                'headers': self._content_type_header,
                'status': 400,
                'stream': False
            },
            expected_response={
                'body': test_body,
                'message': 'Error: {"err, Status code: 400'
            }
        )
        with self.assertRaises(JSONDecodeError):
            e.http_response.json()

    def test_augment_error_empty_reason_with_trace(self):
        test_body = self._error_only_body | {"reason": ''}
        self._run_test(
            mock_response={
                'body': test_body,
                'headers': self._default_mock_headers,
                'status': 444,
                'stream': False
            },
            expected_response={
                'body': test_body | self._errors_error_only | self._trace,
                "message": f'Error: {self._error_name}, Status code: 444'
            }
        )
