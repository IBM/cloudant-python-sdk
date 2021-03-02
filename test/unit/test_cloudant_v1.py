# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
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
Unit Tests for CloudantV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import base64
import inspect
import io
import json
import pytest
import re
import requests
import requests.models
import responses
import tempfile
import urllib
import gzip
from ibmcloudant.cloudant_v1 import *


service = CloudantV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'http://localhost:5984'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Server
##############################################################################
# region

class TestGetServerInformation():
    """
    Test Class for get_server_information
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_server_information_all_params(self):
        """
        get_server_information()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/')
        mock_response = '{"couchdb": "couchdb", "features": ["features"], "vendor": {"name": "name", "variant": "variant", "version": "version"}, "version": "version", "features_flags": ["features_flags"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_server_information()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetMembershipInformation():
    """
    Test Class for get_membership_information
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_membership_information_all_params(self):
        """
        get_membership_information()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_membership')
        mock_response = '{"all_nodes": ["all_nodes"], "cluster_nodes": ["cluster_nodes"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_membership_information()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetUuids():
    """
    Test Class for get_uuids
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_uuids_all_params(self):
        """
        get_uuids()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_uuids')
        mock_response = '{"uuids": ["uuids"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        count = 1

        # Invoke method
        response = service.get_uuids(
            count=count,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'count={}'.format(count) in query_string


    @responses.activate
    def test_get_uuids_required_params(self):
        """
        test_get_uuids_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_uuids')
        mock_response = '{"uuids": ["uuids"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_uuids()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetCapacityThroughputInformation():
    """
    Test Class for get_capacity_throughput_information
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_capacity_throughput_information_all_params(self):
        """
        get_capacity_throughput_information()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_api/v2/user/capacity/throughput')
        mock_response = '{"current": {"throughput": {"blocks": 0, "query": 0, "read": 0, "write": 0}}, "target": {"throughput": {"blocks": 0, "query": 0, "read": 0, "write": 0}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_capacity_throughput_information()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestPutCapacityThroughputInformation():
    """
    Test Class for put_capacity_throughput_information
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_put_capacity_throughput_information_all_params(self):
        """
        put_capacity_throughput_information()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_api/v2/user/capacity/throughput')
        mock_response = '{"current": {"throughput": {"blocks": 0, "query": 0, "read": 0, "write": 0}}, "target": {"throughput": {"blocks": 0, "query": 0, "read": 0, "write": 0}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        blocks = 0

        # Invoke method
        response = service.put_capacity_throughput_information(
            blocks,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['blocks'] == 0


    @responses.activate
    def test_put_capacity_throughput_information_value_error(self):
        """
        test_put_capacity_throughput_information_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_api/v2/user/capacity/throughput')
        mock_response = '{"current": {"throughput": {"blocks": 0, "query": 0, "read": 0, "write": 0}}, "target": {"throughput": {"blocks": 0, "query": 0, "read": 0, "write": 0}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        blocks = 0

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "blocks": blocks,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.put_capacity_throughput_information(**req_copy)



# endregion
##############################################################################
# End of Service: Server
##############################################################################

##############################################################################
# Start of Service: Changes
##############################################################################
# region

class TestGetDbUpdates():
    """
    Test Class for get_db_updates
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_db_updates_all_params(self):
        """
        get_db_updates()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_db_updates')
        mock_response = '{"last_seq": "last_seq", "results": [{"account": "account", "db_name": "db_name", "seq": "seq", "type": "created"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        feed = 'continuous'
        heartbeat = 0
        timeout = 0
        since = 'testString'

        # Invoke method
        response = service.get_db_updates(
            feed=feed,
            heartbeat=heartbeat,
            timeout=timeout,
            since=since,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'feed={}'.format(feed) in query_string
        assert 'heartbeat={}'.format(heartbeat) in query_string
        assert 'timeout={}'.format(timeout) in query_string
        assert 'since={}'.format(since) in query_string


    @responses.activate
    def test_get_db_updates_required_params(self):
        """
        test_get_db_updates_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_db_updates')
        mock_response = '{"last_seq": "last_seq", "results": [{"account": "account", "db_name": "db_name", "seq": "seq", "type": "created"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_db_updates()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestPostChanges():
    """
    Test Class for post_changes
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_changes_all_params(self):
        """
        post_changes()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_changes')
        mock_response = '{"last_seq": "last_seq", "pending": 7, "results": [{"changes": [{"rev": "rev"}], "deleted": false, "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "seq": "seq"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_ids = ['testString']
        fields = ['testString']
        selector = {}
        last_event_id = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        feed = 'continuous'
        filter = 'testString'
        heartbeat = 0
        include_docs = True
        limit = 0
        seq_interval = 1
        since = 'testString'
        style = 'testString'
        timeout = 0
        view = 'testString'

        # Invoke method
        response = service.post_changes(
            db,
            doc_ids=doc_ids,
            fields=fields,
            selector=selector,
            last_event_id=last_event_id,
            att_encoding_info=att_encoding_info,
            attachments=attachments,
            conflicts=conflicts,
            descending=descending,
            feed=feed,
            filter=filter,
            heartbeat=heartbeat,
            include_docs=include_docs,
            limit=limit,
            seq_interval=seq_interval,
            since=since,
            style=style,
            timeout=timeout,
            view=view,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'att_encoding_info={}'.format('true' if att_encoding_info else 'false') in query_string
        assert 'attachments={}'.format('true' if attachments else 'false') in query_string
        assert 'conflicts={}'.format('true' if conflicts else 'false') in query_string
        assert 'descending={}'.format('true' if descending else 'false') in query_string
        assert 'feed={}'.format(feed) in query_string
        assert 'filter={}'.format(filter) in query_string
        assert 'heartbeat={}'.format(heartbeat) in query_string
        assert 'include_docs={}'.format('true' if include_docs else 'false') in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'seq_interval={}'.format(seq_interval) in query_string
        assert 'since={}'.format(since) in query_string
        assert 'style={}'.format(style) in query_string
        assert 'timeout={}'.format(timeout) in query_string
        assert 'view={}'.format(view) in query_string
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['doc_ids'] == ['testString']
        assert req_body['fields'] == ['testString']
        assert req_body['selector'] == {}


    @responses.activate
    def test_post_changes_required_params(self):
        """
        test_post_changes_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_changes')
        mock_response = '{"last_seq": "last_seq", "pending": 7, "results": [{"changes": [{"rev": "rev"}], "deleted": false, "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "seq": "seq"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_ids = ['testString']
        fields = ['testString']
        selector = {}

        # Invoke method
        response = service.post_changes(
            db,
            doc_ids=doc_ids,
            fields=fields,
            selector=selector,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['doc_ids'] == ['testString']
        assert req_body['fields'] == ['testString']
        assert req_body['selector'] == {}


    @responses.activate
    def test_post_changes_value_error(self):
        """
        test_post_changes_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_changes')
        mock_response = '{"last_seq": "last_seq", "pending": 7, "results": [{"changes": [{"rev": "rev"}], "deleted": false, "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "seq": "seq"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_ids = ['testString']
        fields = ['testString']
        selector = {}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_changes(**req_copy)



class TestPostChangesAsStream():
    """
    Test Class for post_changes_as_stream
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_changes_as_stream_all_params(self):
        """
        post_changes_as_stream()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_changes')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_ids = ['0007741142412418284']
        fields = ['testString']
        selector = {}
        last_event_id = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        feed = 'continuous'
        filter = 'testString'
        heartbeat = 0
        include_docs = True
        limit = 0
        seq_interval = 1
        since = 'testString'
        style = 'testString'
        timeout = 0
        view = 'testString'

        # Invoke method
        response = service.post_changes_as_stream(
            db,
            doc_ids=doc_ids,
            fields=fields,
            selector=selector,
            last_event_id=last_event_id,
            att_encoding_info=att_encoding_info,
            attachments=attachments,
            conflicts=conflicts,
            descending=descending,
            feed=feed,
            filter=filter,
            heartbeat=heartbeat,
            include_docs=include_docs,
            limit=limit,
            seq_interval=seq_interval,
            since=since,
            style=style,
            timeout=timeout,
            view=view,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'att_encoding_info={}'.format('true' if att_encoding_info else 'false') in query_string
        assert 'attachments={}'.format('true' if attachments else 'false') in query_string
        assert 'conflicts={}'.format('true' if conflicts else 'false') in query_string
        assert 'descending={}'.format('true' if descending else 'false') in query_string
        assert 'feed={}'.format(feed) in query_string
        assert 'filter={}'.format(filter) in query_string
        assert 'heartbeat={}'.format(heartbeat) in query_string
        assert 'include_docs={}'.format('true' if include_docs else 'false') in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'seq_interval={}'.format(seq_interval) in query_string
        assert 'since={}'.format(since) in query_string
        assert 'style={}'.format(style) in query_string
        assert 'timeout={}'.format(timeout) in query_string
        assert 'view={}'.format(view) in query_string
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['doc_ids'] == ['0007741142412418284']
        assert req_body['fields'] == ['testString']
        assert req_body['selector'] == {}

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_post_changes_as_stream_required_params(self):
        """
        test_post_changes_as_stream_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_changes')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_ids = ['0007741142412418284']
        fields = ['testString']
        selector = {}

        # Invoke method
        response = service.post_changes_as_stream(
            db,
            doc_ids=doc_ids,
            fields=fields,
            selector=selector,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['doc_ids'] == ['0007741142412418284']
        assert req_body['fields'] == ['testString']
        assert req_body['selector'] == {}

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_post_changes_as_stream_value_error(self):
        """
        test_post_changes_as_stream_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_changes')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_ids = ['0007741142412418284']
        fields = ['testString']
        selector = {}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_changes_as_stream(**req_copy)



# endregion
##############################################################################
# End of Service: Changes
##############################################################################

##############################################################################
# Start of Service: Databases
##############################################################################
# region

class TestHeadDatabase():
    """
    Test Class for head_database
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_head_database_all_params(self):
        """
        head_database()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        db = 'testString'

        # Invoke method
        response = service.head_database(
            db,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_head_database_value_error(self):
        """
        test_head_database_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        db = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.head_database(**req_copy)



class TestGetAllDbs():
    """
    Test Class for get_all_dbs
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_all_dbs_all_params(self):
        """
        get_all_dbs()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_all_dbs')
        mock_response = '["operation_response"]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        descending = True
        endkey = 'testString'
        limit = 0
        skip = 0
        startkey = 'testString'

        # Invoke method
        response = service.get_all_dbs(
            descending=descending,
            endkey=endkey,
            limit=limit,
            skip=skip,
            startkey=startkey,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'descending={}'.format('true' if descending else 'false') in query_string
        assert 'endkey={}'.format(endkey) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'skip={}'.format(skip) in query_string
        assert 'startkey={}'.format(startkey) in query_string


    @responses.activate
    def test_get_all_dbs_required_params(self):
        """
        test_get_all_dbs_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_all_dbs')
        mock_response = '["operation_response"]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_all_dbs()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestPostDbsInfo():
    """
    Test Class for post_dbs_info
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_dbs_info_all_params(self):
        """
        post_dbs_info()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_dbs_info')
        mock_response = '[{"info": {"cluster": {"n": 1, "q": 1, "r": 1, "w": 1}, "committed_update_seq": "committed_update_seq", "compact_running": false, "compacted_seq": "compacted_seq", "db_name": "db_name", "disk_format_version": 19, "doc_count": 0, "doc_del_count": 0, "engine": "engine", "props": {"partitioned": false}, "sizes": {"active": 6, "external": 8, "file": 4}, "update_seq": "update_seq", "uuid": "uuid"}, "key": "key"}]'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        keys = ['testString']

        # Invoke method
        response = service.post_dbs_info(
            keys,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['keys'] == ['testString']


    @responses.activate
    def test_post_dbs_info_value_error(self):
        """
        test_post_dbs_info_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_dbs_info')
        mock_response = '[{"info": {"cluster": {"n": 1, "q": 1, "r": 1, "w": 1}, "committed_update_seq": "committed_update_seq", "compact_running": false, "compacted_seq": "compacted_seq", "db_name": "db_name", "disk_format_version": 19, "doc_count": 0, "doc_del_count": 0, "engine": "engine", "props": {"partitioned": false}, "sizes": {"active": 6, "external": 8, "file": 4}, "update_seq": "update_seq", "uuid": "uuid"}, "key": "key"}]'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        keys = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "keys": keys,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_dbs_info(**req_copy)



class TestDeleteDatabase():
    """
    Test Class for delete_database
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_database_all_params(self):
        """
        delete_database()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString')
        mock_response = '{"ok": true}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'

        # Invoke method
        response = service.delete_database(
            db,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_database_value_error(self):
        """
        test_delete_database_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString')
        mock_response = '{"ok": true}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_database(**req_copy)



class TestGetDatabaseInformation():
    """
    Test Class for get_database_information
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_database_information_all_params(self):
        """
        get_database_information()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString')
        mock_response = '{"cluster": {"n": 1, "q": 1, "r": 1, "w": 1}, "committed_update_seq": "committed_update_seq", "compact_running": false, "compacted_seq": "compacted_seq", "db_name": "db_name", "disk_format_version": 19, "doc_count": 0, "doc_del_count": 0, "engine": "engine", "props": {"partitioned": false}, "sizes": {"active": 6, "external": 8, "file": 4}, "update_seq": "update_seq", "uuid": "uuid"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'

        # Invoke method
        response = service.get_database_information(
            db,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_database_information_value_error(self):
        """
        test_get_database_information_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString')
        mock_response = '{"cluster": {"n": 1, "q": 1, "r": 1, "w": 1}, "committed_update_seq": "committed_update_seq", "compact_running": false, "compacted_seq": "compacted_seq", "db_name": "db_name", "disk_format_version": 19, "doc_count": 0, "doc_del_count": 0, "engine": "engine", "props": {"partitioned": false}, "sizes": {"active": 6, "external": 8, "file": 4}, "update_seq": "update_seq", "uuid": "uuid"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_database_information(**req_copy)



class TestPutDatabase():
    """
    Test Class for put_database
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_put_database_all_params(self):
        """
        put_database()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString')
        mock_response = '{"ok": true}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        db = 'testString'
        partitioned = True
        q = 1

        # Invoke method
        response = service.put_database(
            db,
            partitioned=partitioned,
            q=q,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'partitioned={}'.format('true' if partitioned else 'false') in query_string
        assert 'q={}'.format(q) in query_string


    @responses.activate
    def test_put_database_required_params(self):
        """
        test_put_database_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString')
        mock_response = '{"ok": true}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        db = 'testString'

        # Invoke method
        response = service.put_database(
            db,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_put_database_value_error(self):
        """
        test_put_database_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString')
        mock_response = '{"ok": true}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        db = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.put_database(**req_copy)



# endregion
##############################################################################
# End of Service: Databases
##############################################################################

##############################################################################
# Start of Service: Documents
##############################################################################
# region

class TestHeadDocument():
    """
    Test Class for head_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_head_document_all_params(self):
        """
        head_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        if_none_match = 'testString'
        latest = True
        rev = 'testString'

        # Invoke method
        response = service.head_document(
            db,
            doc_id,
            if_none_match=if_none_match,
            latest=latest,
            rev=rev,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'latest={}'.format('true' if latest else 'false') in query_string
        assert 'rev={}'.format(rev) in query_string


    @responses.activate
    def test_head_document_required_params(self):
        """
        test_head_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Invoke method
        response = service.head_document(
            db,
            doc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_head_document_value_error(self):
        """
        test_head_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "doc_id": doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.head_document(**req_copy)



class TestPostDocument():
    """
    Test Class for post_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_document_all_params(self):
        """
        post_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a Document model
        document_model = {}
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        db = 'testString'
        document = document_model
        content_type = 'application/json'
        batch = 'ok'

        # Invoke method
        response = service.post_document(
            db,
            document,
            content_type=content_type,
            batch=batch,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'batch={}'.format(batch) in query_string
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params


    @responses.activate
    def test_post_document_required_params(self):
        """
        test_post_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a Document model
        document_model = {}
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        db = 'testString'
        document = document_model

        # Invoke method
        response = service.post_document(
            db,
            document,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params


    @responses.activate
    def test_post_document_value_error(self):
        """
        test_post_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a Document model
        document_model = {}
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        db = 'testString'
        document = document_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "document": document,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_document(**req_copy)



class TestPostAllDocs():
    """
    Test Class for post_all_docs
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_all_docs_all_params(self):
        """
        post_all_docs()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_all_docs')
        mock_response = '{"total_rows": 0, "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": "key", "value": {"rev": "rev"}}], "update_seq": "update_seq"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 0
        skip = 0
        update_seq = True
        endkey = 'testString'
        key = 'testString'
        keys = ['testString']
        startkey = 'testString'

        # Invoke method
        response = service.post_all_docs(
            db,
            att_encoding_info=att_encoding_info,
            attachments=attachments,
            conflicts=conflicts,
            descending=descending,
            include_docs=include_docs,
            inclusive_end=inclusive_end,
            limit=limit,
            skip=skip,
            update_seq=update_seq,
            endkey=endkey,
            key=key,
            keys=keys,
            startkey=startkey,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['att_encoding_info'] == True
        assert req_body['attachments'] == True
        assert req_body['conflicts'] == True
        assert req_body['descending'] == True
        assert req_body['include_docs'] == True
        assert req_body['inclusive_end'] == True
        assert req_body['limit'] == 0
        assert req_body['skip'] == 0
        assert req_body['update_seq'] == True
        assert req_body['endkey'] == 'testString'
        assert req_body['key'] == 'testString'
        assert req_body['keys'] == ['testString']
        assert req_body['startkey'] == 'testString'


    @responses.activate
    def test_post_all_docs_value_error(self):
        """
        test_post_all_docs_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_all_docs')
        mock_response = '{"total_rows": 0, "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": "key", "value": {"rev": "rev"}}], "update_seq": "update_seq"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 0
        skip = 0
        update_seq = True
        endkey = 'testString'
        key = 'testString'
        keys = ['testString']
        startkey = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_all_docs(**req_copy)



class TestPostAllDocsAsStream():
    """
    Test Class for post_all_docs_as_stream
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_all_docs_as_stream_all_params(self):
        """
        post_all_docs_as_stream()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_all_docs')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 10
        skip = 0
        update_seq = True
        endkey = 'testString'
        key = 'testString'
        keys = ['testString']
        startkey = '0007741142412418284'

        # Invoke method
        response = service.post_all_docs_as_stream(
            db,
            att_encoding_info=att_encoding_info,
            attachments=attachments,
            conflicts=conflicts,
            descending=descending,
            include_docs=include_docs,
            inclusive_end=inclusive_end,
            limit=limit,
            skip=skip,
            update_seq=update_seq,
            endkey=endkey,
            key=key,
            keys=keys,
            startkey=startkey,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['att_encoding_info'] == True
        assert req_body['attachments'] == True
        assert req_body['conflicts'] == True
        assert req_body['descending'] == True
        assert req_body['include_docs'] == True
        assert req_body['inclusive_end'] == True
        assert req_body['limit'] == 10
        assert req_body['skip'] == 0
        assert req_body['update_seq'] == True
        assert req_body['endkey'] == 'testString'
        assert req_body['key'] == 'testString'
        assert req_body['keys'] == ['testString']
        assert req_body['startkey'] == '0007741142412418284'

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_post_all_docs_as_stream_value_error(self):
        """
        test_post_all_docs_as_stream_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_all_docs')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 10
        skip = 0
        update_seq = True
        endkey = 'testString'
        key = 'testString'
        keys = ['testString']
        startkey = '0007741142412418284'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_all_docs_as_stream(**req_copy)



class TestPostAllDocsQueries():
    """
    Test Class for post_all_docs_queries
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_all_docs_queries_all_params(self):
        """
        post_all_docs_queries()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_all_docs/queries')
        mock_response = '{"results": [{"total_rows": 0, "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": "key", "value": {"rev": "rev"}}], "update_seq": "update_seq"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a AllDocsQuery model
        all_docs_query_model = {}
        all_docs_query_model['att_encoding_info'] = True
        all_docs_query_model['attachments'] = True
        all_docs_query_model['conflicts'] = True
        all_docs_query_model['descending'] = True
        all_docs_query_model['include_docs'] = True
        all_docs_query_model['inclusive_end'] = True
        all_docs_query_model['limit'] = 0
        all_docs_query_model['skip'] = 0
        all_docs_query_model['update_seq'] = True
        all_docs_query_model['endkey'] = 'testString'
        all_docs_query_model['key'] = 'testString'
        all_docs_query_model['keys'] = ['testString']
        all_docs_query_model['startkey'] = 'testString'

        # Set up parameter values
        db = 'testString'
        queries = [all_docs_query_model]

        # Invoke method
        response = service.post_all_docs_queries(
            db,
            queries,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['queries'] == [all_docs_query_model]


    @responses.activate
    def test_post_all_docs_queries_value_error(self):
        """
        test_post_all_docs_queries_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_all_docs/queries')
        mock_response = '{"results": [{"total_rows": 0, "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": "key", "value": {"rev": "rev"}}], "update_seq": "update_seq"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a AllDocsQuery model
        all_docs_query_model = {}
        all_docs_query_model['att_encoding_info'] = True
        all_docs_query_model['attachments'] = True
        all_docs_query_model['conflicts'] = True
        all_docs_query_model['descending'] = True
        all_docs_query_model['include_docs'] = True
        all_docs_query_model['inclusive_end'] = True
        all_docs_query_model['limit'] = 0
        all_docs_query_model['skip'] = 0
        all_docs_query_model['update_seq'] = True
        all_docs_query_model['endkey'] = 'testString'
        all_docs_query_model['key'] = 'testString'
        all_docs_query_model['keys'] = ['testString']
        all_docs_query_model['startkey'] = 'testString'

        # Set up parameter values
        db = 'testString'
        queries = [all_docs_query_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "queries": queries,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_all_docs_queries(**req_copy)



class TestPostAllDocsQueriesAsStream():
    """
    Test Class for post_all_docs_queries_as_stream
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_all_docs_queries_as_stream_all_params(self):
        """
        post_all_docs_queries_as_stream()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_all_docs/queries')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a AllDocsQuery model
        all_docs_query_model = {}
        all_docs_query_model['att_encoding_info'] = True
        all_docs_query_model['attachments'] = True
        all_docs_query_model['conflicts'] = True
        all_docs_query_model['descending'] = True
        all_docs_query_model['include_docs'] = True
        all_docs_query_model['inclusive_end'] = True
        all_docs_query_model['limit'] = 0
        all_docs_query_model['skip'] = 0
        all_docs_query_model['update_seq'] = True
        all_docs_query_model['endkey'] = 'testString'
        all_docs_query_model['key'] = 'testString'
        all_docs_query_model['keys'] = ['small-appliances:1000042', 'small-appliances:1000043']
        all_docs_query_model['startkey'] = 'testString'

        # Set up parameter values
        db = 'testString'
        queries = [all_docs_query_model]

        # Invoke method
        response = service.post_all_docs_queries_as_stream(
            db,
            queries,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['queries'] == [all_docs_query_model]

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_post_all_docs_queries_as_stream_value_error(self):
        """
        test_post_all_docs_queries_as_stream_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_all_docs/queries')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a AllDocsQuery model
        all_docs_query_model = {}
        all_docs_query_model['att_encoding_info'] = True
        all_docs_query_model['attachments'] = True
        all_docs_query_model['conflicts'] = True
        all_docs_query_model['descending'] = True
        all_docs_query_model['include_docs'] = True
        all_docs_query_model['inclusive_end'] = True
        all_docs_query_model['limit'] = 0
        all_docs_query_model['skip'] = 0
        all_docs_query_model['update_seq'] = True
        all_docs_query_model['endkey'] = 'testString'
        all_docs_query_model['key'] = 'testString'
        all_docs_query_model['keys'] = ['small-appliances:1000042', 'small-appliances:1000043']
        all_docs_query_model['startkey'] = 'testString'

        # Set up parameter values
        db = 'testString'
        queries = [all_docs_query_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "queries": queries,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_all_docs_queries_as_stream(**req_copy)



class TestPostBulkDocs():
    """
    Test Class for post_bulk_docs
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_bulk_docs_all_params(self):
        """
        post_bulk_docs()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_bulk_docs')
        mock_response = '[{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}]'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a Document model
        document_model = {}
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        # Construct a dict representation of a BulkDocs model
        bulk_docs_model = {}
        bulk_docs_model['docs'] = [document_model]
        bulk_docs_model['new_edits'] = True

        # Set up parameter values
        db = 'testString'
        bulk_docs = bulk_docs_model

        # Invoke method
        response = service.post_bulk_docs(
            db,
            bulk_docs,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == bulk_docs


    @responses.activate
    def test_post_bulk_docs_value_error(self):
        """
        test_post_bulk_docs_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_bulk_docs')
        mock_response = '[{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}]'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a Document model
        document_model = {}
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        # Construct a dict representation of a BulkDocs model
        bulk_docs_model = {}
        bulk_docs_model['docs'] = [document_model]
        bulk_docs_model['new_edits'] = True

        # Set up parameter values
        db = 'testString'
        bulk_docs = bulk_docs_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "bulk_docs": bulk_docs,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_bulk_docs(**req_copy)



class TestPostBulkGet():
    """
    Test Class for post_bulk_get
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_bulk_get_all_params(self):
        """
        post_bulk_get()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_bulk_get')
        mock_response = '{"results": [{"docs": [{"error": {"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}, "ok": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}}], "id": "id"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {}
        bulk_get_query_document_model['atts_since'] = ['testString']
        bulk_get_query_document_model['id'] = 'testString'
        bulk_get_query_document_model['open_revs'] = ['testString']
        bulk_get_query_document_model['rev'] = 'testString'

        # Set up parameter values
        db = 'testString'
        docs = [bulk_get_query_document_model]
        attachments = True
        att_encoding_info = True
        latest = True
        revs = True

        # Invoke method
        response = service.post_bulk_get(
            db,
            docs,
            attachments=attachments,
            att_encoding_info=att_encoding_info,
            latest=latest,
            revs=revs,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'attachments={}'.format('true' if attachments else 'false') in query_string
        assert 'att_encoding_info={}'.format('true' if att_encoding_info else 'false') in query_string
        assert 'latest={}'.format('true' if latest else 'false') in query_string
        assert 'revs={}'.format('true' if revs else 'false') in query_string
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['docs'] == [bulk_get_query_document_model]


    @responses.activate
    def test_post_bulk_get_required_params(self):
        """
        test_post_bulk_get_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_bulk_get')
        mock_response = '{"results": [{"docs": [{"error": {"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}, "ok": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}}], "id": "id"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {}
        bulk_get_query_document_model['atts_since'] = ['testString']
        bulk_get_query_document_model['id'] = 'testString'
        bulk_get_query_document_model['open_revs'] = ['testString']
        bulk_get_query_document_model['rev'] = 'testString'

        # Set up parameter values
        db = 'testString'
        docs = [bulk_get_query_document_model]

        # Invoke method
        response = service.post_bulk_get(
            db,
            docs,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['docs'] == [bulk_get_query_document_model]


    @responses.activate
    def test_post_bulk_get_value_error(self):
        """
        test_post_bulk_get_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_bulk_get')
        mock_response = '{"results": [{"docs": [{"error": {"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}, "ok": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}}], "id": "id"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {}
        bulk_get_query_document_model['atts_since'] = ['testString']
        bulk_get_query_document_model['id'] = 'testString'
        bulk_get_query_document_model['open_revs'] = ['testString']
        bulk_get_query_document_model['rev'] = 'testString'

        # Set up parameter values
        db = 'testString'
        docs = [bulk_get_query_document_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "docs": docs,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_bulk_get(**req_copy)



class TestPostBulkGetAsMixed():
    """
    Test Class for post_bulk_get_as_mixed
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_bulk_get_as_mixed_all_params(self):
        """
        post_bulk_get_as_mixed()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_bulk_get')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='multipart/mixed',
                      status=200)

        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {}
        bulk_get_query_document_model['atts_since'] = ['testString']
        bulk_get_query_document_model['id'] = 'small-appliances:1000042'
        bulk_get_query_document_model['open_revs'] = ['testString']
        bulk_get_query_document_model['rev'] = 'testString'

        # Set up parameter values
        db = 'testString'
        docs = [bulk_get_query_document_model]
        attachments = True
        att_encoding_info = True
        latest = True
        revs = True

        # Invoke method
        response = service.post_bulk_get_as_mixed(
            db,
            docs,
            attachments=attachments,
            att_encoding_info=att_encoding_info,
            latest=latest,
            revs=revs,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'attachments={}'.format('true' if attachments else 'false') in query_string
        assert 'att_encoding_info={}'.format('true' if att_encoding_info else 'false') in query_string
        assert 'latest={}'.format('true' if latest else 'false') in query_string
        assert 'revs={}'.format('true' if revs else 'false') in query_string
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['docs'] == [bulk_get_query_document_model]


    @responses.activate
    def test_post_bulk_get_as_mixed_required_params(self):
        """
        test_post_bulk_get_as_mixed_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_bulk_get')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='multipart/mixed',
                      status=200)

        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {}
        bulk_get_query_document_model['atts_since'] = ['testString']
        bulk_get_query_document_model['id'] = 'small-appliances:1000042'
        bulk_get_query_document_model['open_revs'] = ['testString']
        bulk_get_query_document_model['rev'] = 'testString'

        # Set up parameter values
        db = 'testString'
        docs = [bulk_get_query_document_model]

        # Invoke method
        response = service.post_bulk_get_as_mixed(
            db,
            docs,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['docs'] == [bulk_get_query_document_model]


    @responses.activate
    def test_post_bulk_get_as_mixed_value_error(self):
        """
        test_post_bulk_get_as_mixed_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_bulk_get')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='multipart/mixed',
                      status=200)

        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {}
        bulk_get_query_document_model['atts_since'] = ['testString']
        bulk_get_query_document_model['id'] = 'small-appliances:1000042'
        bulk_get_query_document_model['open_revs'] = ['testString']
        bulk_get_query_document_model['rev'] = 'testString'

        # Set up parameter values
        db = 'testString'
        docs = [bulk_get_query_document_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "docs": docs,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_bulk_get_as_mixed(**req_copy)



class TestPostBulkGetAsRelated():
    """
    Test Class for post_bulk_get_as_related
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_bulk_get_as_related_all_params(self):
        """
        post_bulk_get_as_related()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_bulk_get')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='multipart/related',
                      status=200)

        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {}
        bulk_get_query_document_model['atts_since'] = ['testString']
        bulk_get_query_document_model['id'] = 'small-appliances:1000042'
        bulk_get_query_document_model['open_revs'] = ['testString']
        bulk_get_query_document_model['rev'] = 'testString'

        # Set up parameter values
        db = 'testString'
        docs = [bulk_get_query_document_model]
        attachments = True
        att_encoding_info = True
        latest = True
        revs = True

        # Invoke method
        response = service.post_bulk_get_as_related(
            db,
            docs,
            attachments=attachments,
            att_encoding_info=att_encoding_info,
            latest=latest,
            revs=revs,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'attachments={}'.format('true' if attachments else 'false') in query_string
        assert 'att_encoding_info={}'.format('true' if att_encoding_info else 'false') in query_string
        assert 'latest={}'.format('true' if latest else 'false') in query_string
        assert 'revs={}'.format('true' if revs else 'false') in query_string
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['docs'] == [bulk_get_query_document_model]


    @responses.activate
    def test_post_bulk_get_as_related_required_params(self):
        """
        test_post_bulk_get_as_related_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_bulk_get')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='multipart/related',
                      status=200)

        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {}
        bulk_get_query_document_model['atts_since'] = ['testString']
        bulk_get_query_document_model['id'] = 'small-appliances:1000042'
        bulk_get_query_document_model['open_revs'] = ['testString']
        bulk_get_query_document_model['rev'] = 'testString'

        # Set up parameter values
        db = 'testString'
        docs = [bulk_get_query_document_model]

        # Invoke method
        response = service.post_bulk_get_as_related(
            db,
            docs,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['docs'] == [bulk_get_query_document_model]


    @responses.activate
    def test_post_bulk_get_as_related_value_error(self):
        """
        test_post_bulk_get_as_related_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_bulk_get')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='multipart/related',
                      status=200)

        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {}
        bulk_get_query_document_model['atts_since'] = ['testString']
        bulk_get_query_document_model['id'] = 'small-appliances:1000042'
        bulk_get_query_document_model['open_revs'] = ['testString']
        bulk_get_query_document_model['rev'] = 'testString'

        # Set up parameter values
        db = 'testString'
        docs = [bulk_get_query_document_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "docs": docs,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_bulk_get_as_related(**req_copy)



class TestPostBulkGetAsStream():
    """
    Test Class for post_bulk_get_as_stream
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_bulk_get_as_stream_all_params(self):
        """
        post_bulk_get_as_stream()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_bulk_get')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {}
        bulk_get_query_document_model['atts_since'] = ['testString']
        bulk_get_query_document_model['id'] = 'small-appliances:1000042'
        bulk_get_query_document_model['open_revs'] = ['testString']
        bulk_get_query_document_model['rev'] = 'testString'

        # Set up parameter values
        db = 'testString'
        docs = [bulk_get_query_document_model]
        attachments = True
        att_encoding_info = True
        latest = True
        revs = True

        # Invoke method
        response = service.post_bulk_get_as_stream(
            db,
            docs,
            attachments=attachments,
            att_encoding_info=att_encoding_info,
            latest=latest,
            revs=revs,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'attachments={}'.format('true' if attachments else 'false') in query_string
        assert 'att_encoding_info={}'.format('true' if att_encoding_info else 'false') in query_string
        assert 'latest={}'.format('true' if latest else 'false') in query_string
        assert 'revs={}'.format('true' if revs else 'false') in query_string
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['docs'] == [bulk_get_query_document_model]

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_post_bulk_get_as_stream_required_params(self):
        """
        test_post_bulk_get_as_stream_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_bulk_get')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {}
        bulk_get_query_document_model['atts_since'] = ['testString']
        bulk_get_query_document_model['id'] = 'small-appliances:1000042'
        bulk_get_query_document_model['open_revs'] = ['testString']
        bulk_get_query_document_model['rev'] = 'testString'

        # Set up parameter values
        db = 'testString'
        docs = [bulk_get_query_document_model]

        # Invoke method
        response = service.post_bulk_get_as_stream(
            db,
            docs,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['docs'] == [bulk_get_query_document_model]

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_post_bulk_get_as_stream_value_error(self):
        """
        test_post_bulk_get_as_stream_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_bulk_get')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {}
        bulk_get_query_document_model['atts_since'] = ['testString']
        bulk_get_query_document_model['id'] = 'small-appliances:1000042'
        bulk_get_query_document_model['open_revs'] = ['testString']
        bulk_get_query_document_model['rev'] = 'testString'

        # Set up parameter values
        db = 'testString'
        docs = [bulk_get_query_document_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "docs": docs,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_bulk_get_as_stream(**req_copy)



class TestDeleteDocument():
    """
    Test Class for delete_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_document_all_params(self):
        """
        delete_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        if_match = 'testString'
        batch = 'ok'
        rev = 'testString'

        # Invoke method
        response = service.delete_document(
            db,
            doc_id,
            if_match=if_match,
            batch=batch,
            rev=rev,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'batch={}'.format(batch) in query_string
        assert 'rev={}'.format(rev) in query_string


    @responses.activate
    def test_delete_document_required_params(self):
        """
        test_delete_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Invoke method
        response = service.delete_document(
            db,
            doc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_document_value_error(self):
        """
        test_delete_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "doc_id": doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_document(**req_copy)



class TestGetDocument():
    """
    Test Class for get_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_document_all_params(self):
        """
        get_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = '{"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        if_none_match = 'testString'
        attachments = True
        att_encoding_info = True
        atts_since = ['testString']
        conflicts = True
        deleted_conflicts = True
        latest = True
        local_seq = True
        meta = True
        open_revs = ['testString']
        rev = 'testString'
        revs = True
        revs_info = True

        # Invoke method
        response = service.get_document(
            db,
            doc_id,
            if_none_match=if_none_match,
            attachments=attachments,
            att_encoding_info=att_encoding_info,
            atts_since=atts_since,
            conflicts=conflicts,
            deleted_conflicts=deleted_conflicts,
            latest=latest,
            local_seq=local_seq,
            meta=meta,
            open_revs=open_revs,
            rev=rev,
            revs=revs,
            revs_info=revs_info,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'attachments={}'.format('true' if attachments else 'false') in query_string
        assert 'att_encoding_info={}'.format('true' if att_encoding_info else 'false') in query_string
        assert 'atts_since={}'.format(','.join(atts_since)) in query_string
        assert 'conflicts={}'.format('true' if conflicts else 'false') in query_string
        assert 'deleted_conflicts={}'.format('true' if deleted_conflicts else 'false') in query_string
        assert 'latest={}'.format('true' if latest else 'false') in query_string
        assert 'local_seq={}'.format('true' if local_seq else 'false') in query_string
        assert 'meta={}'.format('true' if meta else 'false') in query_string
        assert 'open_revs={}'.format(','.join(open_revs)) in query_string
        assert 'rev={}'.format(rev) in query_string
        assert 'revs={}'.format('true' if revs else 'false') in query_string
        assert 'revs_info={}'.format('true' if revs_info else 'false') in query_string


    @responses.activate
    def test_get_document_required_params(self):
        """
        test_get_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = '{"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Invoke method
        response = service.get_document(
            db,
            doc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_document_value_error(self):
        """
        test_get_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = '{"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "doc_id": doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_document(**req_copy)



class TestGetDocumentAsMixed():
    """
    Test Class for get_document_as_mixed
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_document_as_mixed_all_params(self):
        """
        get_document_as_mixed()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='multipart/mixed',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        if_none_match = 'testString'
        attachments = True
        att_encoding_info = True
        atts_since = ['testString']
        conflicts = True
        deleted_conflicts = True
        latest = True
        local_seq = True
        meta = True
        open_revs = ['testString']
        rev = 'testString'
        revs = True
        revs_info = True

        # Invoke method
        response = service.get_document_as_mixed(
            db,
            doc_id,
            if_none_match=if_none_match,
            attachments=attachments,
            att_encoding_info=att_encoding_info,
            atts_since=atts_since,
            conflicts=conflicts,
            deleted_conflicts=deleted_conflicts,
            latest=latest,
            local_seq=local_seq,
            meta=meta,
            open_revs=open_revs,
            rev=rev,
            revs=revs,
            revs_info=revs_info,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'attachments={}'.format('true' if attachments else 'false') in query_string
        assert 'att_encoding_info={}'.format('true' if att_encoding_info else 'false') in query_string
        assert 'atts_since={}'.format(','.join(atts_since)) in query_string
        assert 'conflicts={}'.format('true' if conflicts else 'false') in query_string
        assert 'deleted_conflicts={}'.format('true' if deleted_conflicts else 'false') in query_string
        assert 'latest={}'.format('true' if latest else 'false') in query_string
        assert 'local_seq={}'.format('true' if local_seq else 'false') in query_string
        assert 'meta={}'.format('true' if meta else 'false') in query_string
        assert 'open_revs={}'.format(','.join(open_revs)) in query_string
        assert 'rev={}'.format(rev) in query_string
        assert 'revs={}'.format('true' if revs else 'false') in query_string
        assert 'revs_info={}'.format('true' if revs_info else 'false') in query_string


    @responses.activate
    def test_get_document_as_mixed_required_params(self):
        """
        test_get_document_as_mixed_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='multipart/mixed',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Invoke method
        response = service.get_document_as_mixed(
            db,
            doc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_document_as_mixed_value_error(self):
        """
        test_get_document_as_mixed_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='multipart/mixed',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "doc_id": doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_document_as_mixed(**req_copy)



class TestGetDocumentAsRelated():
    """
    Test Class for get_document_as_related
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_document_as_related_all_params(self):
        """
        get_document_as_related()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='multipart/related',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        if_none_match = 'testString'
        attachments = True
        att_encoding_info = True
        atts_since = ['testString']
        conflicts = True
        deleted_conflicts = True
        latest = True
        local_seq = True
        meta = True
        open_revs = ['testString']
        rev = 'testString'
        revs = True
        revs_info = True

        # Invoke method
        response = service.get_document_as_related(
            db,
            doc_id,
            if_none_match=if_none_match,
            attachments=attachments,
            att_encoding_info=att_encoding_info,
            atts_since=atts_since,
            conflicts=conflicts,
            deleted_conflicts=deleted_conflicts,
            latest=latest,
            local_seq=local_seq,
            meta=meta,
            open_revs=open_revs,
            rev=rev,
            revs=revs,
            revs_info=revs_info,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'attachments={}'.format('true' if attachments else 'false') in query_string
        assert 'att_encoding_info={}'.format('true' if att_encoding_info else 'false') in query_string
        assert 'atts_since={}'.format(','.join(atts_since)) in query_string
        assert 'conflicts={}'.format('true' if conflicts else 'false') in query_string
        assert 'deleted_conflicts={}'.format('true' if deleted_conflicts else 'false') in query_string
        assert 'latest={}'.format('true' if latest else 'false') in query_string
        assert 'local_seq={}'.format('true' if local_seq else 'false') in query_string
        assert 'meta={}'.format('true' if meta else 'false') in query_string
        assert 'open_revs={}'.format(','.join(open_revs)) in query_string
        assert 'rev={}'.format(rev) in query_string
        assert 'revs={}'.format('true' if revs else 'false') in query_string
        assert 'revs_info={}'.format('true' if revs_info else 'false') in query_string


    @responses.activate
    def test_get_document_as_related_required_params(self):
        """
        test_get_document_as_related_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='multipart/related',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Invoke method
        response = service.get_document_as_related(
            db,
            doc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_document_as_related_value_error(self):
        """
        test_get_document_as_related_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='multipart/related',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "doc_id": doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_document_as_related(**req_copy)



class TestGetDocumentAsStream():
    """
    Test Class for get_document_as_stream
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_document_as_stream_all_params(self):
        """
        get_document_as_stream()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        if_none_match = 'testString'
        attachments = True
        att_encoding_info = True
        atts_since = ['testString']
        conflicts = True
        deleted_conflicts = True
        latest = True
        local_seq = True
        meta = True
        open_revs = ['testString']
        rev = 'testString'
        revs = True
        revs_info = True

        # Invoke method
        response = service.get_document_as_stream(
            db,
            doc_id,
            if_none_match=if_none_match,
            attachments=attachments,
            att_encoding_info=att_encoding_info,
            atts_since=atts_since,
            conflicts=conflicts,
            deleted_conflicts=deleted_conflicts,
            latest=latest,
            local_seq=local_seq,
            meta=meta,
            open_revs=open_revs,
            rev=rev,
            revs=revs,
            revs_info=revs_info,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'attachments={}'.format('true' if attachments else 'false') in query_string
        assert 'att_encoding_info={}'.format('true' if att_encoding_info else 'false') in query_string
        assert 'atts_since={}'.format(','.join(atts_since)) in query_string
        assert 'conflicts={}'.format('true' if conflicts else 'false') in query_string
        assert 'deleted_conflicts={}'.format('true' if deleted_conflicts else 'false') in query_string
        assert 'latest={}'.format('true' if latest else 'false') in query_string
        assert 'local_seq={}'.format('true' if local_seq else 'false') in query_string
        assert 'meta={}'.format('true' if meta else 'false') in query_string
        assert 'open_revs={}'.format(','.join(open_revs)) in query_string
        assert 'rev={}'.format(rev) in query_string
        assert 'revs={}'.format('true' if revs else 'false') in query_string
        assert 'revs_info={}'.format('true' if revs_info else 'false') in query_string

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_get_document_as_stream_required_params(self):
        """
        test_get_document_as_stream_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Invoke method
        response = service.get_document_as_stream(
            db,
            doc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_get_document_as_stream_value_error(self):
        """
        test_get_document_as_stream_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "doc_id": doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_document_as_stream(**req_copy)



class TestPutDocument():
    """
    Test Class for put_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_put_document_all_params(self):
        """
        put_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a Document model
        document_model = {}
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'exampleid'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        document = document_model
        content_type = 'application/json'
        if_match = 'testString'
        batch = 'ok'
        new_edits = True
        rev = 'testString'

        # Invoke method
        response = service.put_document(
            db,
            doc_id,
            document,
            content_type=content_type,
            if_match=if_match,
            batch=batch,
            new_edits=new_edits,
            rev=rev,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'batch={}'.format(batch) in query_string
        assert 'new_edits={}'.format('true' if new_edits else 'false') in query_string
        assert 'rev={}'.format(rev) in query_string
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params


    @responses.activate
    def test_put_document_required_params(self):
        """
        test_put_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a Document model
        document_model = {}
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'exampleid'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        document = document_model

        # Invoke method
        response = service.put_document(
            db,
            doc_id,
            document,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params


    @responses.activate
    def test_put_document_value_error(self):
        """
        test_put_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a Document model
        document_model = {}
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'exampleid'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        document = document_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "doc_id": doc_id,
            "document": document,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.put_document(**req_copy)



# endregion
##############################################################################
# End of Service: Documents
##############################################################################

##############################################################################
# Start of Service: DesignDocuments
##############################################################################
# region

class TestHeadDesignDocument():
    """
    Test Class for head_design_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_head_design_document_all_params(self):
        """
        head_design_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        if_none_match = 'testString'

        # Invoke method
        response = service.head_design_document(
            db,
            ddoc,
            if_none_match=if_none_match,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_head_design_document_required_params(self):
        """
        test_head_design_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'

        # Invoke method
        response = service.head_design_document(
            db,
            ddoc,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_head_design_document_value_error(self):
        """
        test_head_design_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "ddoc": ddoc,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.head_design_document(**req_copy)



class TestDeleteDesignDocument():
    """
    Test Class for delete_design_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_design_document_all_params(self):
        """
        delete_design_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        if_match = 'testString'
        batch = 'ok'
        rev = 'testString'

        # Invoke method
        response = service.delete_design_document(
            db,
            ddoc,
            if_match=if_match,
            batch=batch,
            rev=rev,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'batch={}'.format(batch) in query_string
        assert 'rev={}'.format(rev) in query_string


    @responses.activate
    def test_delete_design_document_required_params(self):
        """
        test_delete_design_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'

        # Invoke method
        response = service.delete_design_document(
            db,
            ddoc,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_design_document_value_error(self):
        """
        test_delete_design_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "ddoc": ddoc,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_design_document(**req_copy)



class TestGetDesignDocument():
    """
    Test Class for get_design_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_design_document_all_params(self):
        """
        get_design_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString')
        mock_response = '{"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}], "autoupdate": true, "filters": {"mapKey": "inner"}, "indexes": {"mapKey": {"analyzer": {"name": "classic", "stopwords": ["stopwords"], "fields": {"mapKey": {"name": "classic", "stopwords": ["stopwords"]}}}, "index": "index"}}, "language": "language", "options": {"partitioned": false}, "updates": {"mapKey": "inner"}, "validate_doc_update": {"mapKey": "inner"}, "views": {"mapKey": {"map": "map", "reduce": "reduce"}}, "st_indexes": {"mapKey": {"index": "index"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        if_none_match = 'testString'
        attachments = True
        att_encoding_info = True
        atts_since = ['testString']
        conflicts = True
        deleted_conflicts = True
        latest = True
        local_seq = True
        meta = True
        open_revs = ['testString']
        rev = 'testString'
        revs = True
        revs_info = True

        # Invoke method
        response = service.get_design_document(
            db,
            ddoc,
            if_none_match=if_none_match,
            attachments=attachments,
            att_encoding_info=att_encoding_info,
            atts_since=atts_since,
            conflicts=conflicts,
            deleted_conflicts=deleted_conflicts,
            latest=latest,
            local_seq=local_seq,
            meta=meta,
            open_revs=open_revs,
            rev=rev,
            revs=revs,
            revs_info=revs_info,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'attachments={}'.format('true' if attachments else 'false') in query_string
        assert 'att_encoding_info={}'.format('true' if att_encoding_info else 'false') in query_string
        assert 'atts_since={}'.format(','.join(atts_since)) in query_string
        assert 'conflicts={}'.format('true' if conflicts else 'false') in query_string
        assert 'deleted_conflicts={}'.format('true' if deleted_conflicts else 'false') in query_string
        assert 'latest={}'.format('true' if latest else 'false') in query_string
        assert 'local_seq={}'.format('true' if local_seq else 'false') in query_string
        assert 'meta={}'.format('true' if meta else 'false') in query_string
        assert 'open_revs={}'.format(','.join(open_revs)) in query_string
        assert 'rev={}'.format(rev) in query_string
        assert 'revs={}'.format('true' if revs else 'false') in query_string
        assert 'revs_info={}'.format('true' if revs_info else 'false') in query_string


    @responses.activate
    def test_get_design_document_required_params(self):
        """
        test_get_design_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString')
        mock_response = '{"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}], "autoupdate": true, "filters": {"mapKey": "inner"}, "indexes": {"mapKey": {"analyzer": {"name": "classic", "stopwords": ["stopwords"], "fields": {"mapKey": {"name": "classic", "stopwords": ["stopwords"]}}}, "index": "index"}}, "language": "language", "options": {"partitioned": false}, "updates": {"mapKey": "inner"}, "validate_doc_update": {"mapKey": "inner"}, "views": {"mapKey": {"map": "map", "reduce": "reduce"}}, "st_indexes": {"mapKey": {"index": "index"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'

        # Invoke method
        response = service.get_design_document(
            db,
            ddoc,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_design_document_value_error(self):
        """
        test_get_design_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString')
        mock_response = '{"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}], "autoupdate": true, "filters": {"mapKey": "inner"}, "indexes": {"mapKey": {"analyzer": {"name": "classic", "stopwords": ["stopwords"], "fields": {"mapKey": {"name": "classic", "stopwords": ["stopwords"]}}}, "index": "index"}}, "language": "language", "options": {"partitioned": false}, "updates": {"mapKey": "inner"}, "validate_doc_update": {"mapKey": "inner"}, "views": {"mapKey": {"map": "map", "reduce": "reduce"}}, "st_indexes": {"mapKey": {"index": "index"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "ddoc": ddoc,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_design_document(**req_copy)



class TestPutDesignDocument():
    """
    Test Class for put_design_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_put_design_document_all_params(self):
        """
        put_design_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a Analyzer model
        analyzer_model = {}
        analyzer_model['name'] = 'classic'
        analyzer_model['stopwords'] = ['testString']

        # Construct a dict representation of a AnalyzerConfiguration model
        analyzer_configuration_model = {}
        analyzer_configuration_model['name'] = 'classic'
        analyzer_configuration_model['stopwords'] = ['testString']
        analyzer_configuration_model['fields'] = {}

        # Construct a dict representation of a SearchIndexDefinition model
        search_index_definition_model = {}
        search_index_definition_model['analyzer'] = analyzer_configuration_model
        search_index_definition_model['index'] = 'testString'

        # Construct a dict representation of a DesignDocumentOptions model
        design_document_options_model = {}
        design_document_options_model['partitioned'] = True

        # Construct a dict representation of a DesignDocumentViewsMapReduce model
        design_document_views_map_reduce_model = {}
        design_document_views_map_reduce_model['map'] = 'testString'
        design_document_views_map_reduce_model['reduce'] = 'testString'

        # Construct a dict representation of a GeoIndexDefinition model
        geo_index_definition_model = {}
        geo_index_definition_model['index'] = 'testString'

        # Construct a dict representation of a DesignDocument model
        design_document_model = {}
        design_document_model['_attachments'] = {}
        design_document_model['_conflicts'] = ['testString']
        design_document_model['_deleted'] = True
        design_document_model['_deleted_conflicts'] = ['testString']
        design_document_model['_id'] = 'testString'
        design_document_model['_local_seq'] = 'testString'
        design_document_model['_rev'] = 'testString'
        design_document_model['_revisions'] = revisions_model
        design_document_model['_revs_info'] = [document_revision_status_model]
        design_document_model['autoupdate'] = True
        design_document_model['filters'] = {}
        design_document_model['indexes'] = {}
        design_document_model['language'] = 'testString'
        design_document_model['options'] = design_document_options_model
        design_document_model['updates'] = {}
        design_document_model['validate_doc_update'] = {}
        design_document_model['views'] = {}
        design_document_model['st_indexes'] = {}
        design_document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        design_document = design_document_model
        if_match = 'testString'
        batch = 'ok'
        new_edits = True
        rev = 'testString'

        # Invoke method
        response = service.put_design_document(
            db,
            ddoc,
            design_document,
            if_match=if_match,
            batch=batch,
            new_edits=new_edits,
            rev=rev,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'batch={}'.format(batch) in query_string
        assert 'new_edits={}'.format('true' if new_edits else 'false') in query_string
        assert 'rev={}'.format(rev) in query_string
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == design_document


    @responses.activate
    def test_put_design_document_required_params(self):
        """
        test_put_design_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a Analyzer model
        analyzer_model = {}
        analyzer_model['name'] = 'classic'
        analyzer_model['stopwords'] = ['testString']

        # Construct a dict representation of a AnalyzerConfiguration model
        analyzer_configuration_model = {}
        analyzer_configuration_model['name'] = 'classic'
        analyzer_configuration_model['stopwords'] = ['testString']
        analyzer_configuration_model['fields'] = {}

        # Construct a dict representation of a SearchIndexDefinition model
        search_index_definition_model = {}
        search_index_definition_model['analyzer'] = analyzer_configuration_model
        search_index_definition_model['index'] = 'testString'

        # Construct a dict representation of a DesignDocumentOptions model
        design_document_options_model = {}
        design_document_options_model['partitioned'] = True

        # Construct a dict representation of a DesignDocumentViewsMapReduce model
        design_document_views_map_reduce_model = {}
        design_document_views_map_reduce_model['map'] = 'testString'
        design_document_views_map_reduce_model['reduce'] = 'testString'

        # Construct a dict representation of a GeoIndexDefinition model
        geo_index_definition_model = {}
        geo_index_definition_model['index'] = 'testString'

        # Construct a dict representation of a DesignDocument model
        design_document_model = {}
        design_document_model['_attachments'] = {}
        design_document_model['_conflicts'] = ['testString']
        design_document_model['_deleted'] = True
        design_document_model['_deleted_conflicts'] = ['testString']
        design_document_model['_id'] = 'testString'
        design_document_model['_local_seq'] = 'testString'
        design_document_model['_rev'] = 'testString'
        design_document_model['_revisions'] = revisions_model
        design_document_model['_revs_info'] = [document_revision_status_model]
        design_document_model['autoupdate'] = True
        design_document_model['filters'] = {}
        design_document_model['indexes'] = {}
        design_document_model['language'] = 'testString'
        design_document_model['options'] = design_document_options_model
        design_document_model['updates'] = {}
        design_document_model['validate_doc_update'] = {}
        design_document_model['views'] = {}
        design_document_model['st_indexes'] = {}
        design_document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        design_document = design_document_model

        # Invoke method
        response = service.put_design_document(
            db,
            ddoc,
            design_document,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == design_document


    @responses.activate
    def test_put_design_document_value_error(self):
        """
        test_put_design_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a Analyzer model
        analyzer_model = {}
        analyzer_model['name'] = 'classic'
        analyzer_model['stopwords'] = ['testString']

        # Construct a dict representation of a AnalyzerConfiguration model
        analyzer_configuration_model = {}
        analyzer_configuration_model['name'] = 'classic'
        analyzer_configuration_model['stopwords'] = ['testString']
        analyzer_configuration_model['fields'] = {}

        # Construct a dict representation of a SearchIndexDefinition model
        search_index_definition_model = {}
        search_index_definition_model['analyzer'] = analyzer_configuration_model
        search_index_definition_model['index'] = 'testString'

        # Construct a dict representation of a DesignDocumentOptions model
        design_document_options_model = {}
        design_document_options_model['partitioned'] = True

        # Construct a dict representation of a DesignDocumentViewsMapReduce model
        design_document_views_map_reduce_model = {}
        design_document_views_map_reduce_model['map'] = 'testString'
        design_document_views_map_reduce_model['reduce'] = 'testString'

        # Construct a dict representation of a GeoIndexDefinition model
        geo_index_definition_model = {}
        geo_index_definition_model['index'] = 'testString'

        # Construct a dict representation of a DesignDocument model
        design_document_model = {}
        design_document_model['_attachments'] = {}
        design_document_model['_conflicts'] = ['testString']
        design_document_model['_deleted'] = True
        design_document_model['_deleted_conflicts'] = ['testString']
        design_document_model['_id'] = 'testString'
        design_document_model['_local_seq'] = 'testString'
        design_document_model['_rev'] = 'testString'
        design_document_model['_revisions'] = revisions_model
        design_document_model['_revs_info'] = [document_revision_status_model]
        design_document_model['autoupdate'] = True
        design_document_model['filters'] = {}
        design_document_model['indexes'] = {}
        design_document_model['language'] = 'testString'
        design_document_model['options'] = design_document_options_model
        design_document_model['updates'] = {}
        design_document_model['validate_doc_update'] = {}
        design_document_model['views'] = {}
        design_document_model['st_indexes'] = {}
        design_document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        design_document = design_document_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "ddoc": ddoc,
            "design_document": design_document,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.put_design_document(**req_copy)



class TestGetDesignDocumentInformation():
    """
    Test Class for get_design_document_information
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_design_document_information_all_params(self):
        """
        get_design_document_information()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_info')
        mock_response = '{"name": "name", "view_index": {"compact_running": false, "language": "language", "signature": "signature", "sizes": {"active": 6, "external": 8, "file": 4}, "update_seq": "update_seq", "updater_running": false, "waiting_clients": 0, "waiting_commit": true}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'

        # Invoke method
        response = service.get_design_document_information(
            db,
            ddoc,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_design_document_information_value_error(self):
        """
        test_get_design_document_information_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_info')
        mock_response = '{"name": "name", "view_index": {"compact_running": false, "language": "language", "signature": "signature", "sizes": {"active": 6, "external": 8, "file": 4}, "update_seq": "update_seq", "updater_running": false, "waiting_clients": 0, "waiting_commit": true}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "ddoc": ddoc,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_design_document_information(**req_copy)



class TestPostDesignDocs():
    """
    Test Class for post_design_docs
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_design_docs_all_params(self):
        """
        post_design_docs()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design_docs')
        mock_response = '{"total_rows": 0, "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": "key", "value": {"rev": "rev"}}], "update_seq": "update_seq"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 10
        skip = 0
        update_seq = True
        endkey = 'testString'
        key = 'testString'
        keys = ['testString']
        startkey = '0007741142412418284'
        accept = 'application/json'

        # Invoke method
        response = service.post_design_docs(
            db,
            att_encoding_info=att_encoding_info,
            attachments=attachments,
            conflicts=conflicts,
            descending=descending,
            include_docs=include_docs,
            inclusive_end=inclusive_end,
            limit=limit,
            skip=skip,
            update_seq=update_seq,
            endkey=endkey,
            key=key,
            keys=keys,
            startkey=startkey,
            accept=accept,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['att_encoding_info'] == True
        assert req_body['attachments'] == True
        assert req_body['conflicts'] == True
        assert req_body['descending'] == True
        assert req_body['include_docs'] == True
        assert req_body['inclusive_end'] == True
        assert req_body['limit'] == 10
        assert req_body['skip'] == 0
        assert req_body['update_seq'] == True
        assert req_body['endkey'] == 'testString'
        assert req_body['key'] == 'testString'
        assert req_body['keys'] == ['testString']
        assert req_body['startkey'] == '0007741142412418284'


    @responses.activate
    def test_post_design_docs_required_params(self):
        """
        test_post_design_docs_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design_docs')
        mock_response = '{"total_rows": 0, "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": "key", "value": {"rev": "rev"}}], "update_seq": "update_seq"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 10
        skip = 0
        update_seq = True
        endkey = 'testString'
        key = 'testString'
        keys = ['testString']
        startkey = '0007741142412418284'

        # Invoke method
        response = service.post_design_docs(
            db,
            att_encoding_info=att_encoding_info,
            attachments=attachments,
            conflicts=conflicts,
            descending=descending,
            include_docs=include_docs,
            inclusive_end=inclusive_end,
            limit=limit,
            skip=skip,
            update_seq=update_seq,
            endkey=endkey,
            key=key,
            keys=keys,
            startkey=startkey,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['att_encoding_info'] == True
        assert req_body['attachments'] == True
        assert req_body['conflicts'] == True
        assert req_body['descending'] == True
        assert req_body['include_docs'] == True
        assert req_body['inclusive_end'] == True
        assert req_body['limit'] == 10
        assert req_body['skip'] == 0
        assert req_body['update_seq'] == True
        assert req_body['endkey'] == 'testString'
        assert req_body['key'] == 'testString'
        assert req_body['keys'] == ['testString']
        assert req_body['startkey'] == '0007741142412418284'


    @responses.activate
    def test_post_design_docs_value_error(self):
        """
        test_post_design_docs_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design_docs')
        mock_response = '{"total_rows": 0, "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": "key", "value": {"rev": "rev"}}], "update_seq": "update_seq"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 10
        skip = 0
        update_seq = True
        endkey = 'testString'
        key = 'testString'
        keys = ['testString']
        startkey = '0007741142412418284'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_design_docs(**req_copy)



class TestPostDesignDocsQueries():
    """
    Test Class for post_design_docs_queries
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_design_docs_queries_all_params(self):
        """
        post_design_docs_queries()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design_docs/queries')
        mock_response = '{"results": [{"total_rows": 0, "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": "key", "value": {"rev": "rev"}}], "update_seq": "update_seq"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a AllDocsQuery model
        all_docs_query_model = {}
        all_docs_query_model['att_encoding_info'] = True
        all_docs_query_model['attachments'] = True
        all_docs_query_model['conflicts'] = True
        all_docs_query_model['descending'] = True
        all_docs_query_model['include_docs'] = True
        all_docs_query_model['inclusive_end'] = True
        all_docs_query_model['limit'] = 0
        all_docs_query_model['skip'] = 0
        all_docs_query_model['update_seq'] = True
        all_docs_query_model['endkey'] = 'testString'
        all_docs_query_model['key'] = 'testString'
        all_docs_query_model['keys'] = ['small-appliances:1000042', 'small-appliances:1000043']
        all_docs_query_model['startkey'] = 'testString'

        # Set up parameter values
        db = 'testString'
        queries = [all_docs_query_model]
        accept = 'application/json'

        # Invoke method
        response = service.post_design_docs_queries(
            db,
            queries,
            accept=accept,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['queries'] == [all_docs_query_model]


    @responses.activate
    def test_post_design_docs_queries_required_params(self):
        """
        test_post_design_docs_queries_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design_docs/queries')
        mock_response = '{"results": [{"total_rows": 0, "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": "key", "value": {"rev": "rev"}}], "update_seq": "update_seq"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a AllDocsQuery model
        all_docs_query_model = {}
        all_docs_query_model['att_encoding_info'] = True
        all_docs_query_model['attachments'] = True
        all_docs_query_model['conflicts'] = True
        all_docs_query_model['descending'] = True
        all_docs_query_model['include_docs'] = True
        all_docs_query_model['inclusive_end'] = True
        all_docs_query_model['limit'] = 0
        all_docs_query_model['skip'] = 0
        all_docs_query_model['update_seq'] = True
        all_docs_query_model['endkey'] = 'testString'
        all_docs_query_model['key'] = 'testString'
        all_docs_query_model['keys'] = ['small-appliances:1000042', 'small-appliances:1000043']
        all_docs_query_model['startkey'] = 'testString'

        # Set up parameter values
        db = 'testString'
        queries = [all_docs_query_model]

        # Invoke method
        response = service.post_design_docs_queries(
            db,
            queries,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['queries'] == [all_docs_query_model]


    @responses.activate
    def test_post_design_docs_queries_value_error(self):
        """
        test_post_design_docs_queries_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design_docs/queries')
        mock_response = '{"results": [{"total_rows": 0, "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": "key", "value": {"rev": "rev"}}], "update_seq": "update_seq"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a AllDocsQuery model
        all_docs_query_model = {}
        all_docs_query_model['att_encoding_info'] = True
        all_docs_query_model['attachments'] = True
        all_docs_query_model['conflicts'] = True
        all_docs_query_model['descending'] = True
        all_docs_query_model['include_docs'] = True
        all_docs_query_model['inclusive_end'] = True
        all_docs_query_model['limit'] = 0
        all_docs_query_model['skip'] = 0
        all_docs_query_model['update_seq'] = True
        all_docs_query_model['endkey'] = 'testString'
        all_docs_query_model['key'] = 'testString'
        all_docs_query_model['keys'] = ['small-appliances:1000042', 'small-appliances:1000043']
        all_docs_query_model['startkey'] = 'testString'

        # Set up parameter values
        db = 'testString'
        queries = [all_docs_query_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "queries": queries,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_design_docs_queries(**req_copy)



# endregion
##############################################################################
# End of Service: DesignDocuments
##############################################################################

##############################################################################
# Start of Service: Views
##############################################################################
# region

class TestPostView():
    """
    Test Class for post_view
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_view_all_params(self):
        """
        post_view()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_view/testString')
        mock_response = '{"total_rows": 0, "update_seq": "update_seq", "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": {"anyKey": "anyValue"}, "value": {"anyKey": "anyValue"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        view = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 0
        skip = 0
        update_seq = True
        endkey = { 'foo': 'bar' }
        endkey_docid = 'testString'
        group = True
        group_level = 1
        key = { 'foo': 'bar' }
        keys = [{ 'foo': 'bar' }]
        reduce = True
        stable = True
        startkey = { 'foo': 'bar' }
        startkey_docid = 'testString'
        update = 'true'

        # Invoke method
        response = service.post_view(
            db,
            ddoc,
            view,
            att_encoding_info=att_encoding_info,
            attachments=attachments,
            conflicts=conflicts,
            descending=descending,
            include_docs=include_docs,
            inclusive_end=inclusive_end,
            limit=limit,
            skip=skip,
            update_seq=update_seq,
            endkey=endkey,
            endkey_docid=endkey_docid,
            group=group,
            group_level=group_level,
            key=key,
            keys=keys,
            reduce=reduce,
            stable=stable,
            startkey=startkey,
            startkey_docid=startkey_docid,
            update=update,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['att_encoding_info'] == True
        assert req_body['attachments'] == True
        assert req_body['conflicts'] == True
        assert req_body['descending'] == True
        assert req_body['include_docs'] == True
        assert req_body['inclusive_end'] == True
        assert req_body['limit'] == 0
        assert req_body['skip'] == 0
        assert req_body['update_seq'] == True
        assert req_body['endkey'] == { 'foo': 'bar' }
        assert req_body['endkey_docid'] == 'testString'
        assert req_body['group'] == True
        assert req_body['group_level'] == 1
        assert req_body['key'] == { 'foo': 'bar' }
        assert req_body['keys'] == [{ 'foo': 'bar' }]
        assert req_body['reduce'] == True
        assert req_body['stable'] == True
        assert req_body['startkey'] == { 'foo': 'bar' }
        assert req_body['startkey_docid'] == 'testString'
        assert req_body['update'] == 'true'


    @responses.activate
    def test_post_view_value_error(self):
        """
        test_post_view_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_view/testString')
        mock_response = '{"total_rows": 0, "update_seq": "update_seq", "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": {"anyKey": "anyValue"}, "value": {"anyKey": "anyValue"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        view = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 0
        skip = 0
        update_seq = True
        endkey = { 'foo': 'bar' }
        endkey_docid = 'testString'
        group = True
        group_level = 1
        key = { 'foo': 'bar' }
        keys = [{ 'foo': 'bar' }]
        reduce = True
        stable = True
        startkey = { 'foo': 'bar' }
        startkey_docid = 'testString'
        update = 'true'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "ddoc": ddoc,
            "view": view,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_view(**req_copy)



class TestPostViewAsStream():
    """
    Test Class for post_view_as_stream
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_view_as_stream_all_params(self):
        """
        post_view_as_stream()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_view/testString')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        view = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 10
        skip = 0
        update_seq = True
        endkey = { 'foo': 'bar' }
        endkey_docid = 'testString'
        group = True
        group_level = 1
        key = { 'foo': 'bar' }
        keys = ['examplekey']
        reduce = True
        stable = True
        startkey = { 'foo': 'bar' }
        startkey_docid = 'testString'
        update = 'true'

        # Invoke method
        response = service.post_view_as_stream(
            db,
            ddoc,
            view,
            att_encoding_info=att_encoding_info,
            attachments=attachments,
            conflicts=conflicts,
            descending=descending,
            include_docs=include_docs,
            inclusive_end=inclusive_end,
            limit=limit,
            skip=skip,
            update_seq=update_seq,
            endkey=endkey,
            endkey_docid=endkey_docid,
            group=group,
            group_level=group_level,
            key=key,
            keys=keys,
            reduce=reduce,
            stable=stable,
            startkey=startkey,
            startkey_docid=startkey_docid,
            update=update,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['att_encoding_info'] == True
        assert req_body['attachments'] == True
        assert req_body['conflicts'] == True
        assert req_body['descending'] == True
        assert req_body['include_docs'] == True
        assert req_body['inclusive_end'] == True
        assert req_body['limit'] == 10
        assert req_body['skip'] == 0
        assert req_body['update_seq'] == True
        assert req_body['endkey'] == { 'foo': 'bar' }
        assert req_body['endkey_docid'] == 'testString'
        assert req_body['group'] == True
        assert req_body['group_level'] == 1
        assert req_body['key'] == { 'foo': 'bar' }
        assert req_body['keys'] == ['examplekey']
        assert req_body['reduce'] == True
        assert req_body['stable'] == True
        assert req_body['startkey'] == { 'foo': 'bar' }
        assert req_body['startkey_docid'] == 'testString'
        assert req_body['update'] == 'true'

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_post_view_as_stream_value_error(self):
        """
        test_post_view_as_stream_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_view/testString')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        view = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 10
        skip = 0
        update_seq = True
        endkey = { 'foo': 'bar' }
        endkey_docid = 'testString'
        group = True
        group_level = 1
        key = { 'foo': 'bar' }
        keys = ['examplekey']
        reduce = True
        stable = True
        startkey = { 'foo': 'bar' }
        startkey_docid = 'testString'
        update = 'true'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "ddoc": ddoc,
            "view": view,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_view_as_stream(**req_copy)



class TestPostViewQueries():
    """
    Test Class for post_view_queries
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_view_queries_all_params(self):
        """
        post_view_queries()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_view/testString/queries')
        mock_response = '{"results": [{"total_rows": 0, "update_seq": "update_seq", "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": {"anyKey": "anyValue"}, "value": {"anyKey": "anyValue"}}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ViewQuery model
        view_query_model = {}
        view_query_model['att_encoding_info'] = True
        view_query_model['attachments'] = True
        view_query_model['conflicts'] = True
        view_query_model['descending'] = True
        view_query_model['include_docs'] = True
        view_query_model['inclusive_end'] = True
        view_query_model['limit'] = 0
        view_query_model['skip'] = 0
        view_query_model['update_seq'] = True
        view_query_model['endkey'] = { 'foo': 'bar' }
        view_query_model['endkey_docid'] = 'testString'
        view_query_model['group'] = True
        view_query_model['group_level'] = 1
        view_query_model['key'] = { 'foo': 'bar' }
        view_query_model['keys'] = [{ 'foo': 'bar' }]
        view_query_model['reduce'] = True
        view_query_model['stable'] = True
        view_query_model['startkey'] = { 'foo': 'bar' }
        view_query_model['startkey_docid'] = 'testString'
        view_query_model['update'] = 'true'

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        view = 'testString'
        queries = [view_query_model]

        # Invoke method
        response = service.post_view_queries(
            db,
            ddoc,
            view,
            queries,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['queries'] == [view_query_model]


    @responses.activate
    def test_post_view_queries_value_error(self):
        """
        test_post_view_queries_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_view/testString/queries')
        mock_response = '{"results": [{"total_rows": 0, "update_seq": "update_seq", "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": {"anyKey": "anyValue"}, "value": {"anyKey": "anyValue"}}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ViewQuery model
        view_query_model = {}
        view_query_model['att_encoding_info'] = True
        view_query_model['attachments'] = True
        view_query_model['conflicts'] = True
        view_query_model['descending'] = True
        view_query_model['include_docs'] = True
        view_query_model['inclusive_end'] = True
        view_query_model['limit'] = 0
        view_query_model['skip'] = 0
        view_query_model['update_seq'] = True
        view_query_model['endkey'] = { 'foo': 'bar' }
        view_query_model['endkey_docid'] = 'testString'
        view_query_model['group'] = True
        view_query_model['group_level'] = 1
        view_query_model['key'] = { 'foo': 'bar' }
        view_query_model['keys'] = [{ 'foo': 'bar' }]
        view_query_model['reduce'] = True
        view_query_model['stable'] = True
        view_query_model['startkey'] = { 'foo': 'bar' }
        view_query_model['startkey_docid'] = 'testString'
        view_query_model['update'] = 'true'

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        view = 'testString'
        queries = [view_query_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "ddoc": ddoc,
            "view": view,
            "queries": queries,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_view_queries(**req_copy)



class TestPostViewQueriesAsStream():
    """
    Test Class for post_view_queries_as_stream
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_view_queries_as_stream_all_params(self):
        """
        post_view_queries_as_stream()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_view/testString/queries')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ViewQuery model
        view_query_model = {}
        view_query_model['att_encoding_info'] = True
        view_query_model['attachments'] = True
        view_query_model['conflicts'] = True
        view_query_model['descending'] = True
        view_query_model['include_docs'] = True
        view_query_model['inclusive_end'] = True
        view_query_model['limit'] = 5
        view_query_model['skip'] = 0
        view_query_model['update_seq'] = True
        view_query_model['endkey'] = { 'foo': 'bar' }
        view_query_model['endkey_docid'] = 'testString'
        view_query_model['group'] = True
        view_query_model['group_level'] = 1
        view_query_model['key'] = { 'foo': 'bar' }
        view_query_model['keys'] = [{ 'foo': 'bar' }]
        view_query_model['reduce'] = True
        view_query_model['stable'] = True
        view_query_model['startkey'] = { 'foo': 'bar' }
        view_query_model['startkey_docid'] = 'testString'
        view_query_model['update'] = 'true'

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        view = 'testString'
        queries = [view_query_model]

        # Invoke method
        response = service.post_view_queries_as_stream(
            db,
            ddoc,
            view,
            queries,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['queries'] == [view_query_model]

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_post_view_queries_as_stream_value_error(self):
        """
        test_post_view_queries_as_stream_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_view/testString/queries')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ViewQuery model
        view_query_model = {}
        view_query_model['att_encoding_info'] = True
        view_query_model['attachments'] = True
        view_query_model['conflicts'] = True
        view_query_model['descending'] = True
        view_query_model['include_docs'] = True
        view_query_model['inclusive_end'] = True
        view_query_model['limit'] = 5
        view_query_model['skip'] = 0
        view_query_model['update_seq'] = True
        view_query_model['endkey'] = { 'foo': 'bar' }
        view_query_model['endkey_docid'] = 'testString'
        view_query_model['group'] = True
        view_query_model['group_level'] = 1
        view_query_model['key'] = { 'foo': 'bar' }
        view_query_model['keys'] = [{ 'foo': 'bar' }]
        view_query_model['reduce'] = True
        view_query_model['stable'] = True
        view_query_model['startkey'] = { 'foo': 'bar' }
        view_query_model['startkey_docid'] = 'testString'
        view_query_model['update'] = 'true'

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        view = 'testString'
        queries = [view_query_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "ddoc": ddoc,
            "view": view,
            "queries": queries,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_view_queries_as_stream(**req_copy)



# endregion
##############################################################################
# End of Service: Views
##############################################################################

##############################################################################
# Start of Service: PartitionedDatabases
##############################################################################
# region

class TestGetPartitionInformation():
    """
    Test Class for get_partition_information
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_partition_information_all_params(self):
        """
        get_partition_information()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString')
        mock_response = '{"db_name": "db_name", "doc_count": 0, "doc_del_count": 0, "partition": "partition", "partitioned_indexes": {"count": 0, "indexes": {"search": 0, "view": 0}, "limit": 0}, "sizes": {"active": 0, "external": 0}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'

        # Invoke method
        response = service.get_partition_information(
            db,
            partition_key,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_partition_information_value_error(self):
        """
        test_get_partition_information_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString')
        mock_response = '{"db_name": "db_name", "doc_count": 0, "doc_del_count": 0, "partition": "partition", "partitioned_indexes": {"count": 0, "indexes": {"search": 0, "view": 0}, "limit": 0}, "sizes": {"active": 0, "external": 0}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "partition_key": partition_key,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_partition_information(**req_copy)



class TestPostPartitionAllDocs():
    """
    Test Class for post_partition_all_docs
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_partition_all_docs_all_params(self):
        """
        post_partition_all_docs()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString/_all_docs')
        mock_response = '{"total_rows": 0, "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": "key", "value": {"rev": "rev"}}], "update_seq": "update_seq"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 10
        skip = 0
        update_seq = True
        endkey = 'testString'
        key = 'testString'
        keys = ['testString']
        startkey = '0007741142412418284'

        # Invoke method
        response = service.post_partition_all_docs(
            db,
            partition_key,
            att_encoding_info=att_encoding_info,
            attachments=attachments,
            conflicts=conflicts,
            descending=descending,
            include_docs=include_docs,
            inclusive_end=inclusive_end,
            limit=limit,
            skip=skip,
            update_seq=update_seq,
            endkey=endkey,
            key=key,
            keys=keys,
            startkey=startkey,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['att_encoding_info'] == True
        assert req_body['attachments'] == True
        assert req_body['conflicts'] == True
        assert req_body['descending'] == True
        assert req_body['include_docs'] == True
        assert req_body['inclusive_end'] == True
        assert req_body['limit'] == 10
        assert req_body['skip'] == 0
        assert req_body['update_seq'] == True
        assert req_body['endkey'] == 'testString'
        assert req_body['key'] == 'testString'
        assert req_body['keys'] == ['testString']
        assert req_body['startkey'] == '0007741142412418284'


    @responses.activate
    def test_post_partition_all_docs_value_error(self):
        """
        test_post_partition_all_docs_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString/_all_docs')
        mock_response = '{"total_rows": 0, "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": "key", "value": {"rev": "rev"}}], "update_seq": "update_seq"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 10
        skip = 0
        update_seq = True
        endkey = 'testString'
        key = 'testString'
        keys = ['testString']
        startkey = '0007741142412418284'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "partition_key": partition_key,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_partition_all_docs(**req_copy)



class TestPostPartitionAllDocsAsStream():
    """
    Test Class for post_partition_all_docs_as_stream
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_partition_all_docs_as_stream_all_params(self):
        """
        post_partition_all_docs_as_stream()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString/_all_docs')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 10
        skip = 0
        update_seq = True
        endkey = 'testString'
        key = 'testString'
        keys = ['testString']
        startkey = '0007741142412418284'

        # Invoke method
        response = service.post_partition_all_docs_as_stream(
            db,
            partition_key,
            att_encoding_info=att_encoding_info,
            attachments=attachments,
            conflicts=conflicts,
            descending=descending,
            include_docs=include_docs,
            inclusive_end=inclusive_end,
            limit=limit,
            skip=skip,
            update_seq=update_seq,
            endkey=endkey,
            key=key,
            keys=keys,
            startkey=startkey,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['att_encoding_info'] == True
        assert req_body['attachments'] == True
        assert req_body['conflicts'] == True
        assert req_body['descending'] == True
        assert req_body['include_docs'] == True
        assert req_body['inclusive_end'] == True
        assert req_body['limit'] == 10
        assert req_body['skip'] == 0
        assert req_body['update_seq'] == True
        assert req_body['endkey'] == 'testString'
        assert req_body['key'] == 'testString'
        assert req_body['keys'] == ['testString']
        assert req_body['startkey'] == '0007741142412418284'

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_post_partition_all_docs_as_stream_value_error(self):
        """
        test_post_partition_all_docs_as_stream_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString/_all_docs')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 10
        skip = 0
        update_seq = True
        endkey = 'testString'
        key = 'testString'
        keys = ['testString']
        startkey = '0007741142412418284'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "partition_key": partition_key,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_partition_all_docs_as_stream(**req_copy)



class TestPostPartitionSearch():
    """
    Test Class for post_partition_search
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_partition_search_all_params(self):
        """
        post_partition_search()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString/_design/testString/_search/testString')
        mock_response = '{"total_rows": 0, "bookmark": "bookmark", "by": "by", "counts": {"mapKey": {"mapKey": 0}}, "ranges": {"mapKey": {"mapKey": 0}}, "rows": [{"doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "fields": {"mapKey": {"anyKey": "anyValue"}}, "highlights": {"mapKey": ["inner"]}, "id": "id"}], "groups": [{"total_rows": 0, "bookmark": "bookmark", "by": "by", "counts": {"mapKey": {"mapKey": 0}}, "ranges": {"mapKey": {"mapKey": 0}}, "rows": [{"doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "fields": {"mapKey": {"anyKey": "anyValue"}}, "highlights": {"mapKey": ["inner"]}, "id": "id"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'
        ddoc = 'testString'
        index = 'testString'
        query = 'testString'
        bookmark = 'testString'
        highlight_fields = ['testString']
        highlight_number = 1
        highlight_post_tag = 'testString'
        highlight_pre_tag = 'testString'
        highlight_size = 1
        include_docs = True
        include_fields = ['testString']
        limit = 0
        sort = ['testString']
        stale = 'ok'

        # Invoke method
        response = service.post_partition_search(
            db,
            partition_key,
            ddoc,
            index,
            query,
            bookmark=bookmark,
            highlight_fields=highlight_fields,
            highlight_number=highlight_number,
            highlight_post_tag=highlight_post_tag,
            highlight_pre_tag=highlight_pre_tag,
            highlight_size=highlight_size,
            include_docs=include_docs,
            include_fields=include_fields,
            limit=limit,
            sort=sort,
            stale=stale,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['query'] == 'testString'
        assert req_body['bookmark'] == 'testString'
        assert req_body['highlight_fields'] == ['testString']
        assert req_body['highlight_number'] == 1
        assert req_body['highlight_post_tag'] == 'testString'
        assert req_body['highlight_pre_tag'] == 'testString'
        assert req_body['highlight_size'] == 1
        assert req_body['include_docs'] == True
        assert req_body['include_fields'] == ['testString']
        assert req_body['limit'] == 0
        assert req_body['sort'] == ['testString']
        assert req_body['stale'] == 'ok'


    @responses.activate
    def test_post_partition_search_value_error(self):
        """
        test_post_partition_search_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString/_design/testString/_search/testString')
        mock_response = '{"total_rows": 0, "bookmark": "bookmark", "by": "by", "counts": {"mapKey": {"mapKey": 0}}, "ranges": {"mapKey": {"mapKey": 0}}, "rows": [{"doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "fields": {"mapKey": {"anyKey": "anyValue"}}, "highlights": {"mapKey": ["inner"]}, "id": "id"}], "groups": [{"total_rows": 0, "bookmark": "bookmark", "by": "by", "counts": {"mapKey": {"mapKey": 0}}, "ranges": {"mapKey": {"mapKey": 0}}, "rows": [{"doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "fields": {"mapKey": {"anyKey": "anyValue"}}, "highlights": {"mapKey": ["inner"]}, "id": "id"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'
        ddoc = 'testString'
        index = 'testString'
        query = 'testString'
        bookmark = 'testString'
        highlight_fields = ['testString']
        highlight_number = 1
        highlight_post_tag = 'testString'
        highlight_pre_tag = 'testString'
        highlight_size = 1
        include_docs = True
        include_fields = ['testString']
        limit = 0
        sort = ['testString']
        stale = 'ok'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "partition_key": partition_key,
            "ddoc": ddoc,
            "index": index,
            "query": query,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_partition_search(**req_copy)



class TestPostPartitionSearchAsStream():
    """
    Test Class for post_partition_search_as_stream
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_partition_search_as_stream_all_params(self):
        """
        post_partition_search_as_stream()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString/_design/testString/_search/testString')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'
        ddoc = 'testString'
        index = 'testString'
        query = 'testString'
        bookmark = 'testString'
        highlight_fields = ['testString']
        highlight_number = 1
        highlight_post_tag = 'testString'
        highlight_pre_tag = 'testString'
        highlight_size = 1
        include_docs = True
        include_fields = ['testString']
        limit = 3
        sort = ['testString']
        stale = 'ok'

        # Invoke method
        response = service.post_partition_search_as_stream(
            db,
            partition_key,
            ddoc,
            index,
            query,
            bookmark=bookmark,
            highlight_fields=highlight_fields,
            highlight_number=highlight_number,
            highlight_post_tag=highlight_post_tag,
            highlight_pre_tag=highlight_pre_tag,
            highlight_size=highlight_size,
            include_docs=include_docs,
            include_fields=include_fields,
            limit=limit,
            sort=sort,
            stale=stale,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['query'] == 'testString'
        assert req_body['bookmark'] == 'testString'
        assert req_body['highlight_fields'] == ['testString']
        assert req_body['highlight_number'] == 1
        assert req_body['highlight_post_tag'] == 'testString'
        assert req_body['highlight_pre_tag'] == 'testString'
        assert req_body['highlight_size'] == 1
        assert req_body['include_docs'] == True
        assert req_body['include_fields'] == ['testString']
        assert req_body['limit'] == 3
        assert req_body['sort'] == ['testString']
        assert req_body['stale'] == 'ok'

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_post_partition_search_as_stream_value_error(self):
        """
        test_post_partition_search_as_stream_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString/_design/testString/_search/testString')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'
        ddoc = 'testString'
        index = 'testString'
        query = 'testString'
        bookmark = 'testString'
        highlight_fields = ['testString']
        highlight_number = 1
        highlight_post_tag = 'testString'
        highlight_pre_tag = 'testString'
        highlight_size = 1
        include_docs = True
        include_fields = ['testString']
        limit = 3
        sort = ['testString']
        stale = 'ok'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "partition_key": partition_key,
            "ddoc": ddoc,
            "index": index,
            "query": query,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_partition_search_as_stream(**req_copy)



class TestPostPartitionView():
    """
    Test Class for post_partition_view
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_partition_view_all_params(self):
        """
        post_partition_view()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString/_design/testString/_view/testString')
        mock_response = '{"total_rows": 0, "update_seq": "update_seq", "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": {"anyKey": "anyValue"}, "value": {"anyKey": "anyValue"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'
        ddoc = 'testString'
        view = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 10
        skip = 0
        update_seq = True
        endkey = { 'foo': 'bar' }
        endkey_docid = 'testString'
        group = True
        group_level = 1
        key = { 'foo': 'bar' }
        keys = ['examplekey']
        reduce = True
        stable = True
        startkey = { 'foo': 'bar' }
        startkey_docid = 'testString'
        update = 'true'

        # Invoke method
        response = service.post_partition_view(
            db,
            partition_key,
            ddoc,
            view,
            att_encoding_info=att_encoding_info,
            attachments=attachments,
            conflicts=conflicts,
            descending=descending,
            include_docs=include_docs,
            inclusive_end=inclusive_end,
            limit=limit,
            skip=skip,
            update_seq=update_seq,
            endkey=endkey,
            endkey_docid=endkey_docid,
            group=group,
            group_level=group_level,
            key=key,
            keys=keys,
            reduce=reduce,
            stable=stable,
            startkey=startkey,
            startkey_docid=startkey_docid,
            update=update,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['att_encoding_info'] == True
        assert req_body['attachments'] == True
        assert req_body['conflicts'] == True
        assert req_body['descending'] == True
        assert req_body['include_docs'] == True
        assert req_body['inclusive_end'] == True
        assert req_body['limit'] == 10
        assert req_body['skip'] == 0
        assert req_body['update_seq'] == True
        assert req_body['endkey'] == { 'foo': 'bar' }
        assert req_body['endkey_docid'] == 'testString'
        assert req_body['group'] == True
        assert req_body['group_level'] == 1
        assert req_body['key'] == { 'foo': 'bar' }
        assert req_body['keys'] == ['examplekey']
        assert req_body['reduce'] == True
        assert req_body['stable'] == True
        assert req_body['startkey'] == { 'foo': 'bar' }
        assert req_body['startkey_docid'] == 'testString'
        assert req_body['update'] == 'true'


    @responses.activate
    def test_post_partition_view_value_error(self):
        """
        test_post_partition_view_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString/_design/testString/_view/testString')
        mock_response = '{"total_rows": 0, "update_seq": "update_seq", "rows": [{"caused_by": "caused_by", "error": "error", "reason": "reason", "doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "id": "id", "key": {"anyKey": "anyValue"}, "value": {"anyKey": "anyValue"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'
        ddoc = 'testString'
        view = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 10
        skip = 0
        update_seq = True
        endkey = { 'foo': 'bar' }
        endkey_docid = 'testString'
        group = True
        group_level = 1
        key = { 'foo': 'bar' }
        keys = ['examplekey']
        reduce = True
        stable = True
        startkey = { 'foo': 'bar' }
        startkey_docid = 'testString'
        update = 'true'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "partition_key": partition_key,
            "ddoc": ddoc,
            "view": view,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_partition_view(**req_copy)



class TestPostPartitionViewAsStream():
    """
    Test Class for post_partition_view_as_stream
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_partition_view_as_stream_all_params(self):
        """
        post_partition_view_as_stream()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString/_design/testString/_view/testString')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'
        ddoc = 'testString'
        view = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 10
        skip = 0
        update_seq = True
        endkey = { 'foo': 'bar' }
        endkey_docid = 'testString'
        group = True
        group_level = 1
        key = { 'foo': 'bar' }
        keys = ['examplekey']
        reduce = True
        stable = True
        startkey = { 'foo': 'bar' }
        startkey_docid = 'testString'
        update = 'true'

        # Invoke method
        response = service.post_partition_view_as_stream(
            db,
            partition_key,
            ddoc,
            view,
            att_encoding_info=att_encoding_info,
            attachments=attachments,
            conflicts=conflicts,
            descending=descending,
            include_docs=include_docs,
            inclusive_end=inclusive_end,
            limit=limit,
            skip=skip,
            update_seq=update_seq,
            endkey=endkey,
            endkey_docid=endkey_docid,
            group=group,
            group_level=group_level,
            key=key,
            keys=keys,
            reduce=reduce,
            stable=stable,
            startkey=startkey,
            startkey_docid=startkey_docid,
            update=update,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['att_encoding_info'] == True
        assert req_body['attachments'] == True
        assert req_body['conflicts'] == True
        assert req_body['descending'] == True
        assert req_body['include_docs'] == True
        assert req_body['inclusive_end'] == True
        assert req_body['limit'] == 10
        assert req_body['skip'] == 0
        assert req_body['update_seq'] == True
        assert req_body['endkey'] == { 'foo': 'bar' }
        assert req_body['endkey_docid'] == 'testString'
        assert req_body['group'] == True
        assert req_body['group_level'] == 1
        assert req_body['key'] == { 'foo': 'bar' }
        assert req_body['keys'] == ['examplekey']
        assert req_body['reduce'] == True
        assert req_body['stable'] == True
        assert req_body['startkey'] == { 'foo': 'bar' }
        assert req_body['startkey_docid'] == 'testString'
        assert req_body['update'] == 'true'

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_post_partition_view_as_stream_value_error(self):
        """
        test_post_partition_view_as_stream_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString/_design/testString/_view/testString')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'
        ddoc = 'testString'
        view = 'testString'
        att_encoding_info = True
        attachments = True
        conflicts = True
        descending = True
        include_docs = True
        inclusive_end = True
        limit = 10
        skip = 0
        update_seq = True
        endkey = { 'foo': 'bar' }
        endkey_docid = 'testString'
        group = True
        group_level = 1
        key = { 'foo': 'bar' }
        keys = ['examplekey']
        reduce = True
        stable = True
        startkey = { 'foo': 'bar' }
        startkey_docid = 'testString'
        update = 'true'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "partition_key": partition_key,
            "ddoc": ddoc,
            "view": view,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_partition_view_as_stream(**req_copy)



class TestPostPartitionFind():
    """
    Test Class for post_partition_find
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_partition_find_all_params(self):
        """
        post_partition_find()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString/_find')
        mock_response = '{"bookmark": "bookmark", "docs": [{"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}], "execution_stats": {"execution_time_ms": 17, "results_returned": 0, "total_docs_examined": 0, "total_keys_examined": 0, "total_quorum_docs_examined": 0}, "warning": "warning"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'
        selector = {}
        bookmark = 'testString'
        conflicts = True
        execution_stats = True
        fields = ['testString']
        limit = 0
        skip = 0
        sort = [{}]
        stable = True
        update = 'false'
        use_index = ['testString']

        # Invoke method
        response = service.post_partition_find(
            db,
            partition_key,
            selector,
            bookmark=bookmark,
            conflicts=conflicts,
            execution_stats=execution_stats,
            fields=fields,
            limit=limit,
            skip=skip,
            sort=sort,
            stable=stable,
            update=update,
            use_index=use_index,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['selector'] == {}
        assert req_body['bookmark'] == 'testString'
        assert req_body['conflicts'] == True
        assert req_body['execution_stats'] == True
        assert req_body['fields'] == ['testString']
        assert req_body['limit'] == 0
        assert req_body['skip'] == 0
        assert req_body['sort'] == [{}]
        assert req_body['stable'] == True
        assert req_body['update'] == 'false'
        assert req_body['use_index'] == ['testString']


    @responses.activate
    def test_post_partition_find_value_error(self):
        """
        test_post_partition_find_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString/_find')
        mock_response = '{"bookmark": "bookmark", "docs": [{"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}], "execution_stats": {"execution_time_ms": 17, "results_returned": 0, "total_docs_examined": 0, "total_keys_examined": 0, "total_quorum_docs_examined": 0}, "warning": "warning"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'
        selector = {}
        bookmark = 'testString'
        conflicts = True
        execution_stats = True
        fields = ['testString']
        limit = 0
        skip = 0
        sort = [{}]
        stable = True
        update = 'false'
        use_index = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "partition_key": partition_key,
            "selector": selector,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_partition_find(**req_copy)



class TestPostPartitionFindAsStream():
    """
    Test Class for post_partition_find_as_stream
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_partition_find_as_stream_all_params(self):
        """
        post_partition_find_as_stream()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString/_find')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'
        selector = {}
        bookmark = 'testString'
        conflicts = True
        execution_stats = True
        fields = ['productid', 'name', 'description']
        limit = 0
        skip = 0
        sort = [{}]
        stable = True
        update = 'false'
        use_index = ['testString']

        # Invoke method
        response = service.post_partition_find_as_stream(
            db,
            partition_key,
            selector,
            bookmark=bookmark,
            conflicts=conflicts,
            execution_stats=execution_stats,
            fields=fields,
            limit=limit,
            skip=skip,
            sort=sort,
            stable=stable,
            update=update,
            use_index=use_index,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['selector'] == {}
        assert req_body['bookmark'] == 'testString'
        assert req_body['conflicts'] == True
        assert req_body['execution_stats'] == True
        assert req_body['fields'] == ['productid', 'name', 'description']
        assert req_body['limit'] == 0
        assert req_body['skip'] == 0
        assert req_body['sort'] == [{}]
        assert req_body['stable'] == True
        assert req_body['update'] == 'false'
        assert req_body['use_index'] == ['testString']

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_post_partition_find_as_stream_value_error(self):
        """
        test_post_partition_find_as_stream_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_partition/testString/_find')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        partition_key = 'testString'
        selector = {}
        bookmark = 'testString'
        conflicts = True
        execution_stats = True
        fields = ['productid', 'name', 'description']
        limit = 0
        skip = 0
        sort = [{}]
        stable = True
        update = 'false'
        use_index = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "partition_key": partition_key,
            "selector": selector,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_partition_find_as_stream(**req_copy)



# endregion
##############################################################################
# End of Service: PartitionedDatabases
##############################################################################

##############################################################################
# Start of Service: Queries
##############################################################################
# region

class TestPostExplain():
    """
    Test Class for post_explain
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_explain_all_params(self):
        """
        post_explain()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_explain')
        mock_response = '{"dbname": "dbname", "fields": ["fields"], "index": {"ddoc": "ddoc", "def": {"default_analyzer": {"name": "classic", "stopwords": ["stopwords"]}, "default_field": {"analyzer": {"name": "classic", "stopwords": ["stopwords"]}, "enabled": false}, "fields": [{"name": "name", "type": "boolean"}], "index_array_lengths": false, "partial_filter_selector": {"mapKey": {"anyKey": "anyValue"}}}, "name": "name", "type": "json"}, "limit": 0, "opts": {"mapKey": {"anyKey": "anyValue"}}, "range": {"end_key": [{"anyKey": "anyValue"}], "start_key": [{"anyKey": "anyValue"}]}, "selector": {"mapKey": {"anyKey": "anyValue"}}, "skip": 0}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        selector = {}
        bookmark = 'testString'
        conflicts = True
        execution_stats = True
        fields = ['testString']
        limit = 0
        skip = 0
        sort = [{}]
        stable = True
        update = 'false'
        use_index = ['testString']
        r = 1

        # Invoke method
        response = service.post_explain(
            db,
            selector,
            bookmark=bookmark,
            conflicts=conflicts,
            execution_stats=execution_stats,
            fields=fields,
            limit=limit,
            skip=skip,
            sort=sort,
            stable=stable,
            update=update,
            use_index=use_index,
            r=r,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['selector'] == {}
        assert req_body['bookmark'] == 'testString'
        assert req_body['conflicts'] == True
        assert req_body['execution_stats'] == True
        assert req_body['fields'] == ['testString']
        assert req_body['limit'] == 0
        assert req_body['skip'] == 0
        assert req_body['sort'] == [{}]
        assert req_body['stable'] == True
        assert req_body['update'] == 'false'
        assert req_body['use_index'] == ['testString']
        assert req_body['r'] == 1


    @responses.activate
    def test_post_explain_value_error(self):
        """
        test_post_explain_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_explain')
        mock_response = '{"dbname": "dbname", "fields": ["fields"], "index": {"ddoc": "ddoc", "def": {"default_analyzer": {"name": "classic", "stopwords": ["stopwords"]}, "default_field": {"analyzer": {"name": "classic", "stopwords": ["stopwords"]}, "enabled": false}, "fields": [{"name": "name", "type": "boolean"}], "index_array_lengths": false, "partial_filter_selector": {"mapKey": {"anyKey": "anyValue"}}}, "name": "name", "type": "json"}, "limit": 0, "opts": {"mapKey": {"anyKey": "anyValue"}}, "range": {"end_key": [{"anyKey": "anyValue"}], "start_key": [{"anyKey": "anyValue"}]}, "selector": {"mapKey": {"anyKey": "anyValue"}}, "skip": 0}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        selector = {}
        bookmark = 'testString'
        conflicts = True
        execution_stats = True
        fields = ['testString']
        limit = 0
        skip = 0
        sort = [{}]
        stable = True
        update = 'false'
        use_index = ['testString']
        r = 1

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "selector": selector,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_explain(**req_copy)



class TestPostFind():
    """
    Test Class for post_find
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_find_all_params(self):
        """
        post_find()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_find')
        mock_response = '{"bookmark": "bookmark", "docs": [{"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}], "execution_stats": {"execution_time_ms": 17, "results_returned": 0, "total_docs_examined": 0, "total_keys_examined": 0, "total_quorum_docs_examined": 0}, "warning": "warning"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        selector = {}
        bookmark = 'testString'
        conflicts = True
        execution_stats = True
        fields = ['_id', 'type', 'name', 'email']
        limit = 3
        skip = 0
        sort = [{}]
        stable = True
        update = 'false'
        use_index = ['testString']
        r = 1

        # Invoke method
        response = service.post_find(
            db,
            selector,
            bookmark=bookmark,
            conflicts=conflicts,
            execution_stats=execution_stats,
            fields=fields,
            limit=limit,
            skip=skip,
            sort=sort,
            stable=stable,
            update=update,
            use_index=use_index,
            r=r,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['selector'] == {}
        assert req_body['bookmark'] == 'testString'
        assert req_body['conflicts'] == True
        assert req_body['execution_stats'] == True
        assert req_body['fields'] == ['_id', 'type', 'name', 'email']
        assert req_body['limit'] == 3
        assert req_body['skip'] == 0
        assert req_body['sort'] == [{}]
        assert req_body['stable'] == True
        assert req_body['update'] == 'false'
        assert req_body['use_index'] == ['testString']
        assert req_body['r'] == 1


    @responses.activate
    def test_post_find_value_error(self):
        """
        test_post_find_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_find')
        mock_response = '{"bookmark": "bookmark", "docs": [{"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}], "execution_stats": {"execution_time_ms": 17, "results_returned": 0, "total_docs_examined": 0, "total_keys_examined": 0, "total_quorum_docs_examined": 0}, "warning": "warning"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        selector = {}
        bookmark = 'testString'
        conflicts = True
        execution_stats = True
        fields = ['_id', 'type', 'name', 'email']
        limit = 3
        skip = 0
        sort = [{}]
        stable = True
        update = 'false'
        use_index = ['testString']
        r = 1

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "selector": selector,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_find(**req_copy)



class TestPostFindAsStream():
    """
    Test Class for post_find_as_stream
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_find_as_stream_all_params(self):
        """
        post_find_as_stream()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_find')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        selector = {}
        bookmark = 'testString'
        conflicts = True
        execution_stats = True
        fields = ['_id', 'type', 'name', 'email']
        limit = 3
        skip = 0
        sort = [{}]
        stable = True
        update = 'false'
        use_index = ['testString']
        r = 1

        # Invoke method
        response = service.post_find_as_stream(
            db,
            selector,
            bookmark=bookmark,
            conflicts=conflicts,
            execution_stats=execution_stats,
            fields=fields,
            limit=limit,
            skip=skip,
            sort=sort,
            stable=stable,
            update=update,
            use_index=use_index,
            r=r,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['selector'] == {}
        assert req_body['bookmark'] == 'testString'
        assert req_body['conflicts'] == True
        assert req_body['execution_stats'] == True
        assert req_body['fields'] == ['_id', 'type', 'name', 'email']
        assert req_body['limit'] == 3
        assert req_body['skip'] == 0
        assert req_body['sort'] == [{}]
        assert req_body['stable'] == True
        assert req_body['update'] == 'false'
        assert req_body['use_index'] == ['testString']
        assert req_body['r'] == 1

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_post_find_as_stream_value_error(self):
        """
        test_post_find_as_stream_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_find')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        selector = {}
        bookmark = 'testString'
        conflicts = True
        execution_stats = True
        fields = ['_id', 'type', 'name', 'email']
        limit = 3
        skip = 0
        sort = [{}]
        stable = True
        update = 'false'
        use_index = ['testString']
        r = 1

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "selector": selector,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_find_as_stream(**req_copy)



class TestGetIndexesInformation():
    """
    Test Class for get_indexes_information
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_indexes_information_all_params(self):
        """
        get_indexes_information()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_index')
        mock_response = '{"total_rows": 0, "indexes": [{"ddoc": "ddoc", "def": {"default_analyzer": {"name": "classic", "stopwords": ["stopwords"]}, "default_field": {"analyzer": {"name": "classic", "stopwords": ["stopwords"]}, "enabled": false}, "fields": [{"name": "name", "type": "boolean"}], "index_array_lengths": false, "partial_filter_selector": {"mapKey": {"anyKey": "anyValue"}}}, "name": "name", "type": "json"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'

        # Invoke method
        response = service.get_indexes_information(
            db,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_indexes_information_value_error(self):
        """
        test_get_indexes_information_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_index')
        mock_response = '{"total_rows": 0, "indexes": [{"ddoc": "ddoc", "def": {"default_analyzer": {"name": "classic", "stopwords": ["stopwords"]}, "default_field": {"analyzer": {"name": "classic", "stopwords": ["stopwords"]}, "enabled": false}, "fields": [{"name": "name", "type": "boolean"}], "index_array_lengths": false, "partial_filter_selector": {"mapKey": {"anyKey": "anyValue"}}}, "name": "name", "type": "json"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_indexes_information(**req_copy)



class TestPostIndex():
    """
    Test Class for post_index
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_index_all_params(self):
        """
        post_index()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_index')
        mock_response = '{"id": "id", "name": "name", "result": "created"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Analyzer model
        analyzer_model = {}
        analyzer_model['name'] = 'classic'
        analyzer_model['stopwords'] = ['testString']

        # Construct a dict representation of a IndexTextOperatorDefaultField model
        index_text_operator_default_field_model = {}
        index_text_operator_default_field_model['analyzer'] = analyzer_model
        index_text_operator_default_field_model['enabled'] = True

        # Construct a dict representation of a IndexField model
        index_field_model = {}
        index_field_model['name'] = 'testString'
        index_field_model['type'] = 'boolean'
        index_field_model['foo'] = 'asc'

        # Construct a dict representation of a IndexDefinition model
        index_definition_model = {}
        index_definition_model['default_analyzer'] = analyzer_model
        index_definition_model['default_field'] = index_text_operator_default_field_model
        index_definition_model['fields'] = [index_field_model]
        index_definition_model['index_array_lengths'] = True
        index_definition_model['partial_filter_selector'] = {}

        # Set up parameter values
        db = 'testString'
        index = index_definition_model
        ddoc = 'testString'
        def_ = index_definition_model
        name = 'testString'
        partitioned = True
        type = 'json'

        # Invoke method
        response = service.post_index(
            db,
            index,
            ddoc=ddoc,
            def_=def_,
            name=name,
            partitioned=partitioned,
            type=type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['index'] == index_definition_model
        assert req_body['ddoc'] == 'testString'
        assert req_body['def'] == index_definition_model
        assert req_body['name'] == 'testString'
        assert req_body['partitioned'] == True
        assert req_body['type'] == 'json'


    @responses.activate
    def test_post_index_value_error(self):
        """
        test_post_index_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_index')
        mock_response = '{"id": "id", "name": "name", "result": "created"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Analyzer model
        analyzer_model = {}
        analyzer_model['name'] = 'classic'
        analyzer_model['stopwords'] = ['testString']

        # Construct a dict representation of a IndexTextOperatorDefaultField model
        index_text_operator_default_field_model = {}
        index_text_operator_default_field_model['analyzer'] = analyzer_model
        index_text_operator_default_field_model['enabled'] = True

        # Construct a dict representation of a IndexField model
        index_field_model = {}
        index_field_model['name'] = 'testString'
        index_field_model['type'] = 'boolean'
        index_field_model['foo'] = 'asc'

        # Construct a dict representation of a IndexDefinition model
        index_definition_model = {}
        index_definition_model['default_analyzer'] = analyzer_model
        index_definition_model['default_field'] = index_text_operator_default_field_model
        index_definition_model['fields'] = [index_field_model]
        index_definition_model['index_array_lengths'] = True
        index_definition_model['partial_filter_selector'] = {}

        # Set up parameter values
        db = 'testString'
        index = index_definition_model
        ddoc = 'testString'
        def_ = index_definition_model
        name = 'testString'
        partitioned = True
        type = 'json'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "index": index,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_index(**req_copy)



class TestDeleteIndex():
    """
    Test Class for delete_index
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_index_all_params(self):
        """
        delete_index()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_index/_design/testString/json/testString')
        mock_response = '{"ok": true}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        type = 'json'
        index = 'testString'

        # Invoke method
        response = service.delete_index(
            db,
            ddoc,
            type,
            index,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_index_value_error(self):
        """
        test_delete_index_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_index/_design/testString/json/testString')
        mock_response = '{"ok": true}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        type = 'json'
        index = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "ddoc": ddoc,
            "type": type,
            "index": index,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_index(**req_copy)



# endregion
##############################################################################
# End of Service: Queries
##############################################################################

##############################################################################
# Start of Service: Searches
##############################################################################
# region

class TestPostSearchAnalyze():
    """
    Test Class for post_search_analyze
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_search_analyze_all_params(self):
        """
        post_search_analyze()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_search_analyze')
        mock_response = '{"tokens": ["tokens"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        analyzer = 'arabic'
        text = 'testString'

        # Invoke method
        response = service.post_search_analyze(
            analyzer,
            text,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['analyzer'] == 'arabic'
        assert req_body['text'] == 'testString'


    @responses.activate
    def test_post_search_analyze_value_error(self):
        """
        test_post_search_analyze_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_search_analyze')
        mock_response = '{"tokens": ["tokens"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        analyzer = 'arabic'
        text = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "analyzer": analyzer,
            "text": text,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_search_analyze(**req_copy)



class TestPostSearch():
    """
    Test Class for post_search
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_search_all_params(self):
        """
        post_search()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_search/testString')
        mock_response = '{"total_rows": 0, "bookmark": "bookmark", "by": "by", "counts": {"mapKey": {"mapKey": 0}}, "ranges": {"mapKey": {"mapKey": 0}}, "rows": [{"doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "fields": {"mapKey": {"anyKey": "anyValue"}}, "highlights": {"mapKey": ["inner"]}, "id": "id"}], "groups": [{"total_rows": 0, "bookmark": "bookmark", "by": "by", "counts": {"mapKey": {"mapKey": 0}}, "ranges": {"mapKey": {"mapKey": 0}}, "rows": [{"doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "fields": {"mapKey": {"anyKey": "anyValue"}}, "highlights": {"mapKey": ["inner"]}, "id": "id"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        index = 'testString'
        query = 'testString'
        bookmark = 'testString'
        highlight_fields = ['testString']
        highlight_number = 1
        highlight_post_tag = 'testString'
        highlight_pre_tag = 'testString'
        highlight_size = 1
        include_docs = True
        include_fields = ['testString']
        limit = 0
        sort = ['testString']
        stale = 'ok'
        counts = ['testString']
        drilldown = [['testString']]
        group_field = 'testString'
        group_limit = 1
        group_sort = ['testString']
        ranges = {}

        # Invoke method
        response = service.post_search(
            db,
            ddoc,
            index,
            query,
            bookmark=bookmark,
            highlight_fields=highlight_fields,
            highlight_number=highlight_number,
            highlight_post_tag=highlight_post_tag,
            highlight_pre_tag=highlight_pre_tag,
            highlight_size=highlight_size,
            include_docs=include_docs,
            include_fields=include_fields,
            limit=limit,
            sort=sort,
            stale=stale,
            counts=counts,
            drilldown=drilldown,
            group_field=group_field,
            group_limit=group_limit,
            group_sort=group_sort,
            ranges=ranges,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['query'] == 'testString'
        assert req_body['bookmark'] == 'testString'
        assert req_body['highlight_fields'] == ['testString']
        assert req_body['highlight_number'] == 1
        assert req_body['highlight_post_tag'] == 'testString'
        assert req_body['highlight_pre_tag'] == 'testString'
        assert req_body['highlight_size'] == 1
        assert req_body['include_docs'] == True
        assert req_body['include_fields'] == ['testString']
        assert req_body['limit'] == 0
        assert req_body['sort'] == ['testString']
        assert req_body['stale'] == 'ok'
        assert req_body['counts'] == ['testString']
        assert req_body['drilldown'] == [['testString']]
        assert req_body['group_field'] == 'testString'
        assert req_body['group_limit'] == 1
        assert req_body['group_sort'] == ['testString']
        assert req_body['ranges'] == {}


    @responses.activate
    def test_post_search_value_error(self):
        """
        test_post_search_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_search/testString')
        mock_response = '{"total_rows": 0, "bookmark": "bookmark", "by": "by", "counts": {"mapKey": {"mapKey": 0}}, "ranges": {"mapKey": {"mapKey": 0}}, "rows": [{"doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "fields": {"mapKey": {"anyKey": "anyValue"}}, "highlights": {"mapKey": ["inner"]}, "id": "id"}], "groups": [{"total_rows": 0, "bookmark": "bookmark", "by": "by", "counts": {"mapKey": {"mapKey": 0}}, "ranges": {"mapKey": {"mapKey": 0}}, "rows": [{"doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "fields": {"mapKey": {"anyKey": "anyValue"}}, "highlights": {"mapKey": ["inner"]}, "id": "id"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        index = 'testString'
        query = 'testString'
        bookmark = 'testString'
        highlight_fields = ['testString']
        highlight_number = 1
        highlight_post_tag = 'testString'
        highlight_pre_tag = 'testString'
        highlight_size = 1
        include_docs = True
        include_fields = ['testString']
        limit = 0
        sort = ['testString']
        stale = 'ok'
        counts = ['testString']
        drilldown = [['testString']]
        group_field = 'testString'
        group_limit = 1
        group_sort = ['testString']
        ranges = {}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "ddoc": ddoc,
            "index": index,
            "query": query,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_search(**req_copy)



class TestPostSearchAsStream():
    """
    Test Class for post_search_as_stream
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_search_as_stream_all_params(self):
        """
        post_search_as_stream()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_search/testString')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        index = 'testString'
        query = 'testString'
        bookmark = 'testString'
        highlight_fields = ['testString']
        highlight_number = 1
        highlight_post_tag = 'testString'
        highlight_pre_tag = 'testString'
        highlight_size = 1
        include_docs = True
        include_fields = ['testString']
        limit = 3
        sort = ['testString']
        stale = 'ok'
        counts = ['testString']
        drilldown = [['testString']]
        group_field = 'testString'
        group_limit = 1
        group_sort = ['testString']
        ranges = {}

        # Invoke method
        response = service.post_search_as_stream(
            db,
            ddoc,
            index,
            query,
            bookmark=bookmark,
            highlight_fields=highlight_fields,
            highlight_number=highlight_number,
            highlight_post_tag=highlight_post_tag,
            highlight_pre_tag=highlight_pre_tag,
            highlight_size=highlight_size,
            include_docs=include_docs,
            include_fields=include_fields,
            limit=limit,
            sort=sort,
            stale=stale,
            counts=counts,
            drilldown=drilldown,
            group_field=group_field,
            group_limit=group_limit,
            group_sort=group_sort,
            ranges=ranges,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['query'] == 'testString'
        assert req_body['bookmark'] == 'testString'
        assert req_body['highlight_fields'] == ['testString']
        assert req_body['highlight_number'] == 1
        assert req_body['highlight_post_tag'] == 'testString'
        assert req_body['highlight_pre_tag'] == 'testString'
        assert req_body['highlight_size'] == 1
        assert req_body['include_docs'] == True
        assert req_body['include_fields'] == ['testString']
        assert req_body['limit'] == 3
        assert req_body['sort'] == ['testString']
        assert req_body['stale'] == 'ok'
        assert req_body['counts'] == ['testString']
        assert req_body['drilldown'] == [['testString']]
        assert req_body['group_field'] == 'testString'
        assert req_body['group_limit'] == 1
        assert req_body['group_sort'] == ['testString']
        assert req_body['ranges'] == {}

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_post_search_as_stream_value_error(self):
        """
        test_post_search_as_stream_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_search/testString')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        index = 'testString'
        query = 'testString'
        bookmark = 'testString'
        highlight_fields = ['testString']
        highlight_number = 1
        highlight_post_tag = 'testString'
        highlight_pre_tag = 'testString'
        highlight_size = 1
        include_docs = True
        include_fields = ['testString']
        limit = 3
        sort = ['testString']
        stale = 'ok'
        counts = ['testString']
        drilldown = [['testString']]
        group_field = 'testString'
        group_limit = 1
        group_sort = ['testString']
        ranges = {}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "ddoc": ddoc,
            "index": index,
            "query": query,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_search_as_stream(**req_copy)



class TestGetSearchInfo():
    """
    Test Class for get_search_info
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_search_info_all_params(self):
        """
        get_search_info()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_search_info/testString')
        mock_response = '{"name": "name", "search_index": {"committed_seq": 13, "disk_size": 0, "doc_count": 0, "doc_del_count": 0, "pending_seq": 11}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        index = 'testString'

        # Invoke method
        response = service.get_search_info(
            db,
            ddoc,
            index,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_search_info_value_error(self):
        """
        test_get_search_info_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_search_info/testString')
        mock_response = '{"name": "name", "search_index": {"committed_seq": 13, "disk_size": 0, "doc_count": 0, "doc_del_count": 0, "pending_seq": 11}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        index = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "ddoc": ddoc,
            "index": index,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_search_info(**req_copy)



# endregion
##############################################################################
# End of Service: Searches
##############################################################################

##############################################################################
# Start of Service: Geospatial
##############################################################################
# region

class TestGetGeo():
    """
    Test Class for get_geo
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_geo_all_params(self):
        """
        get_geo()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_geo/testString')
        mock_response = '{"bookmark": "bookmark", "features": [{"_id": "id", "_rev": "rev", "bbox": [4], "geometry": {"type": "Point", "coordinates": [{"anyKey": "anyValue"}]}, "properties": {"mapKey": {"anyKey": "anyValue"}}, "type": "Feature"}], "rows": [{"doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "geometry": {"type": "Point", "coordinates": [{"anyKey": "anyValue"}]}, "id": "id", "rev": "rev"}], "type": "FeatureCollection"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        index = 'testString'
        bbox = 'testString'
        bookmark = 'testString'
        format = 'legacy'
        g = 'testString'
        include_docs = True
        lat = -90
        limit = 0
        lon = -180
        nearest = True
        radius = 0
        rangex = 0
        rangey = 0
        relation = 'contains'
        skip = 0
        stale = 'ok'

        # Invoke method
        response = service.get_geo(
            db,
            ddoc,
            index,
            bbox=bbox,
            bookmark=bookmark,
            format=format,
            g=g,
            include_docs=include_docs,
            lat=lat,
            limit=limit,
            lon=lon,
            nearest=nearest,
            radius=radius,
            rangex=rangex,
            rangey=rangey,
            relation=relation,
            skip=skip,
            stale=stale,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'bbox={}'.format(bbox) in query_string
        assert 'bookmark={}'.format(bookmark) in query_string
        assert 'format={}'.format(format) in query_string
        assert 'g={}'.format(g) in query_string
        assert 'include_docs={}'.format('true' if include_docs else 'false') in query_string
        assert 'lat={}'.format(lat) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'lon={}'.format(lon) in query_string
        assert 'nearest={}'.format('true' if nearest else 'false') in query_string
        assert 'radius={}'.format(radius) in query_string
        assert 'rangex={}'.format(rangex) in query_string
        assert 'rangey={}'.format(rangey) in query_string
        assert 'relation={}'.format(relation) in query_string
        assert 'skip={}'.format(skip) in query_string
        assert 'stale={}'.format(stale) in query_string


    @responses.activate
    def test_get_geo_required_params(self):
        """
        test_get_geo_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_geo/testString')
        mock_response = '{"bookmark": "bookmark", "features": [{"_id": "id", "_rev": "rev", "bbox": [4], "geometry": {"type": "Point", "coordinates": [{"anyKey": "anyValue"}]}, "properties": {"mapKey": {"anyKey": "anyValue"}}, "type": "Feature"}], "rows": [{"doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "geometry": {"type": "Point", "coordinates": [{"anyKey": "anyValue"}]}, "id": "id", "rev": "rev"}], "type": "FeatureCollection"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        index = 'testString'

        # Invoke method
        response = service.get_geo(
            db,
            ddoc,
            index,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_geo_value_error(self):
        """
        test_get_geo_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_geo/testString')
        mock_response = '{"bookmark": "bookmark", "features": [{"_id": "id", "_rev": "rev", "bbox": [4], "geometry": {"type": "Point", "coordinates": [{"anyKey": "anyValue"}]}, "properties": {"mapKey": {"anyKey": "anyValue"}}, "type": "Feature"}], "rows": [{"doc": {"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}, "geometry": {"type": "Point", "coordinates": [{"anyKey": "anyValue"}]}, "id": "id", "rev": "rev"}], "type": "FeatureCollection"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        index = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "ddoc": ddoc,
            "index": index,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_geo(**req_copy)



class TestGetGeoAsStream():
    """
    Test Class for get_geo_as_stream
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_geo_as_stream_all_params(self):
        """
        get_geo_as_stream()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_geo/testString')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        index = 'testString'
        bbox = 'testString'
        bookmark = 'testString'
        format = 'legacy'
        g = 'testString'
        include_docs = True
        lat = -90
        limit = 0
        lon = -180
        nearest = True
        radius = 0
        rangex = 0
        rangey = 0
        relation = 'contains'
        skip = 0
        stale = 'ok'

        # Invoke method
        response = service.get_geo_as_stream(
            db,
            ddoc,
            index,
            bbox=bbox,
            bookmark=bookmark,
            format=format,
            g=g,
            include_docs=include_docs,
            lat=lat,
            limit=limit,
            lon=lon,
            nearest=nearest,
            radius=radius,
            rangex=rangex,
            rangey=rangey,
            relation=relation,
            skip=skip,
            stale=stale,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'bbox={}'.format(bbox) in query_string
        assert 'bookmark={}'.format(bookmark) in query_string
        assert 'format={}'.format(format) in query_string
        assert 'g={}'.format(g) in query_string
        assert 'include_docs={}'.format('true' if include_docs else 'false') in query_string
        assert 'lat={}'.format(lat) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'lon={}'.format(lon) in query_string
        assert 'nearest={}'.format('true' if nearest else 'false') in query_string
        assert 'radius={}'.format(radius) in query_string
        assert 'rangex={}'.format(rangex) in query_string
        assert 'rangey={}'.format(rangey) in query_string
        assert 'relation={}'.format(relation) in query_string
        assert 'skip={}'.format(skip) in query_string
        assert 'stale={}'.format(stale) in query_string

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_get_geo_as_stream_required_params(self):
        """
        test_get_geo_as_stream_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_geo/testString')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        index = 'testString'

        # Invoke method
        response = service.get_geo_as_stream(
            db,
            ddoc,
            index,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

        # Verify streamed JSON response
        result = response.get_result()
        assert isinstance(result, requests.models.Response)
        response_buf = result.iter_content(chunk_size=1024)
        assert str(next(response_buf), "utf-8") == mock_response


    @responses.activate
    def test_get_geo_as_stream_value_error(self):
        """
        test_get_geo_as_stream_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_geo/testString')
        mock_response = '{"foo": "this is a mock response for JSON streaming"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        index = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "ddoc": ddoc,
            "index": index,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_geo_as_stream(**req_copy)



class TestPostGeoCleanup():
    """
    Test Class for post_geo_cleanup
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_geo_cleanup_all_params(self):
        """
        post_geo_cleanup()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_geo_cleanup')
        mock_response = '{"ok": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        db = 'testString'

        # Invoke method
        response = service.post_geo_cleanup(
            db,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_post_geo_cleanup_value_error(self):
        """
        test_post_geo_cleanup_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_geo_cleanup')
        mock_response = '{"ok": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        db = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_geo_cleanup(**req_copy)



class TestGetGeoIndexInformation():
    """
    Test Class for get_geo_index_information
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_geo_index_information_all_params(self):
        """
        get_geo_index_information()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_geo_info/testString')
        mock_response = '{"geo_index": {"data_size": 0, "disk_size": 0, "doc_count": 0}, "name": "name"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        index = 'testString'

        # Invoke method
        response = service.get_geo_index_information(
            db,
            ddoc,
            index,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_geo_index_information_value_error(self):
        """
        test_get_geo_index_information_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_design/testString/_geo_info/testString')
        mock_response = '{"geo_index": {"data_size": 0, "disk_size": 0, "doc_count": 0}, "name": "name"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        ddoc = 'testString'
        index = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "ddoc": ddoc,
            "index": index,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_geo_index_information(**req_copy)



# endregion
##############################################################################
# End of Service: Geospatial
##############################################################################

##############################################################################
# Start of Service: Replication
##############################################################################
# region

class TestHeadReplicationDocument():
    """
    Test Class for head_replication_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_head_replication_document_all_params(self):
        """
        head_replication_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_replicator/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        doc_id = 'testString'
        if_none_match = 'testString'

        # Invoke method
        response = service.head_replication_document(
            doc_id,
            if_none_match=if_none_match,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_head_replication_document_required_params(self):
        """
        test_head_replication_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_replicator/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        doc_id = 'testString'

        # Invoke method
        response = service.head_replication_document(
            doc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_head_replication_document_value_error(self):
        """
        test_head_replication_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_replicator/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "doc_id": doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.head_replication_document(**req_copy)



class TestHeadSchedulerDocument():
    """
    Test Class for head_scheduler_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_head_scheduler_document_all_params(self):
        """
        head_scheduler_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_scheduler/docs/_replicator/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        doc_id = 'testString'

        # Invoke method
        response = service.head_scheduler_document(
            doc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_head_scheduler_document_value_error(self):
        """
        test_head_scheduler_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_scheduler/docs/_replicator/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "doc_id": doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.head_scheduler_document(**req_copy)



class TestHeadSchedulerJob():
    """
    Test Class for head_scheduler_job
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_head_scheduler_job_all_params(self):
        """
        head_scheduler_job()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_scheduler/jobs/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        job_id = 'testString'

        # Invoke method
        response = service.head_scheduler_job(
            job_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_head_scheduler_job_value_error(self):
        """
        test_head_scheduler_job_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_scheduler/jobs/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        job_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "job_id": job_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.head_scheduler_job(**req_copy)



class TestPostReplicate():
    """
    Test Class for post_replicate
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_replicate_all_params(self):
        """
        post_replicate()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_replicate')
        mock_response = '{"history": [{"doc_write_failures": 0, "docs_read": 0, "docs_written": 0, "end_last_seq": "end_last_seq", "end_time": "end_time", "missing_checked": 0, "missing_found": 0, "recorded_seq": "recorded_seq", "session_id": "session_id", "start_last_seq": "start_last_seq", "start_time": "start_time"}], "ok": true, "replication_id_version": 0, "session_id": "session_id", "source_last_seq": "source_last_seq"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a ReplicationCreateTargetParameters model
        replication_create_target_parameters_model = {}
        replication_create_target_parameters_model['n'] = 1
        replication_create_target_parameters_model['partitioned'] = True
        replication_create_target_parameters_model['q'] = 1

        # Construct a dict representation of a ReplicationDatabaseAuthIam model
        replication_database_auth_iam_model = {}
        replication_database_auth_iam_model['api_key'] = 'testString'

        # Construct a dict representation of a ReplicationDatabaseAuth model
        replication_database_auth_model = {}
        replication_database_auth_model['iam'] = replication_database_auth_iam_model

        # Construct a dict representation of a ReplicationDatabase model
        replication_database_model = {}
        replication_database_model['auth'] = replication_database_auth_model
        replication_database_model['headers'] = {}
        replication_database_model['url'] = 'testString'

        # Construct a dict representation of a UserContext model
        user_context_model = {}
        user_context_model['db'] = 'testString'
        user_context_model['name'] = 'testString'
        user_context_model['roles'] = ['_reader']

        # Construct a dict representation of a ReplicationDocument model
        replication_document_model = {}
        replication_document_model['_attachments'] = {}
        replication_document_model['_conflicts'] = ['testString']
        replication_document_model['_deleted'] = True
        replication_document_model['_deleted_conflicts'] = ['testString']
        replication_document_model['_id'] = 'testString'
        replication_document_model['_local_seq'] = 'testString'
        replication_document_model['_rev'] = 'testString'
        replication_document_model['_revisions'] = revisions_model
        replication_document_model['_revs_info'] = [document_revision_status_model]
        replication_document_model['cancel'] = True
        replication_document_model['checkpoint_interval'] = 0
        replication_document_model['connection_timeout'] = 0
        replication_document_model['continuous'] = True
        replication_document_model['create_target'] = True
        replication_document_model['create_target_params'] = replication_create_target_parameters_model
        replication_document_model['doc_ids'] = ['testString']
        replication_document_model['filter'] = 'testString'
        replication_document_model['http_connections'] = 1
        replication_document_model['query_params'] = {}
        replication_document_model['retries_per_request'] = 0
        replication_document_model['selector'] = {}
        replication_document_model['since_seq'] = 'testString'
        replication_document_model['socket_options'] = 'testString'
        replication_document_model['source'] = replication_database_model
        replication_document_model['source_proxy'] = 'testString'
        replication_document_model['target'] = replication_database_model
        replication_document_model['target_proxy'] = 'testString'
        replication_document_model['use_checkpoints'] = True
        replication_document_model['user_ctx'] = user_context_model
        replication_document_model['worker_batch_size'] = 1
        replication_document_model['worker_processes'] = 1
        replication_document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        replication_document = replication_document_model

        # Invoke method
        response = service.post_replicate(
            replication_document,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == replication_document


    @responses.activate
    def test_post_replicate_value_error(self):
        """
        test_post_replicate_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_replicate')
        mock_response = '{"history": [{"doc_write_failures": 0, "docs_read": 0, "docs_written": 0, "end_last_seq": "end_last_seq", "end_time": "end_time", "missing_checked": 0, "missing_found": 0, "recorded_seq": "recorded_seq", "session_id": "session_id", "start_last_seq": "start_last_seq", "start_time": "start_time"}], "ok": true, "replication_id_version": 0, "session_id": "session_id", "source_last_seq": "source_last_seq"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a ReplicationCreateTargetParameters model
        replication_create_target_parameters_model = {}
        replication_create_target_parameters_model['n'] = 1
        replication_create_target_parameters_model['partitioned'] = True
        replication_create_target_parameters_model['q'] = 1

        # Construct a dict representation of a ReplicationDatabaseAuthIam model
        replication_database_auth_iam_model = {}
        replication_database_auth_iam_model['api_key'] = 'testString'

        # Construct a dict representation of a ReplicationDatabaseAuth model
        replication_database_auth_model = {}
        replication_database_auth_model['iam'] = replication_database_auth_iam_model

        # Construct a dict representation of a ReplicationDatabase model
        replication_database_model = {}
        replication_database_model['auth'] = replication_database_auth_model
        replication_database_model['headers'] = {}
        replication_database_model['url'] = 'testString'

        # Construct a dict representation of a UserContext model
        user_context_model = {}
        user_context_model['db'] = 'testString'
        user_context_model['name'] = 'testString'
        user_context_model['roles'] = ['_reader']

        # Construct a dict representation of a ReplicationDocument model
        replication_document_model = {}
        replication_document_model['_attachments'] = {}
        replication_document_model['_conflicts'] = ['testString']
        replication_document_model['_deleted'] = True
        replication_document_model['_deleted_conflicts'] = ['testString']
        replication_document_model['_id'] = 'testString'
        replication_document_model['_local_seq'] = 'testString'
        replication_document_model['_rev'] = 'testString'
        replication_document_model['_revisions'] = revisions_model
        replication_document_model['_revs_info'] = [document_revision_status_model]
        replication_document_model['cancel'] = True
        replication_document_model['checkpoint_interval'] = 0
        replication_document_model['connection_timeout'] = 0
        replication_document_model['continuous'] = True
        replication_document_model['create_target'] = True
        replication_document_model['create_target_params'] = replication_create_target_parameters_model
        replication_document_model['doc_ids'] = ['testString']
        replication_document_model['filter'] = 'testString'
        replication_document_model['http_connections'] = 1
        replication_document_model['query_params'] = {}
        replication_document_model['retries_per_request'] = 0
        replication_document_model['selector'] = {}
        replication_document_model['since_seq'] = 'testString'
        replication_document_model['socket_options'] = 'testString'
        replication_document_model['source'] = replication_database_model
        replication_document_model['source_proxy'] = 'testString'
        replication_document_model['target'] = replication_database_model
        replication_document_model['target_proxy'] = 'testString'
        replication_document_model['use_checkpoints'] = True
        replication_document_model['user_ctx'] = user_context_model
        replication_document_model['worker_batch_size'] = 1
        replication_document_model['worker_processes'] = 1
        replication_document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        replication_document = replication_document_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "replication_document": replication_document,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_replicate(**req_copy)



class TestDeleteReplicationDocument():
    """
    Test Class for delete_replication_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_replication_document_all_params(self):
        """
        delete_replication_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_replicator/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        doc_id = 'testString'
        if_match = 'testString'
        batch = 'ok'
        rev = 'testString'

        # Invoke method
        response = service.delete_replication_document(
            doc_id,
            if_match=if_match,
            batch=batch,
            rev=rev,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'batch={}'.format(batch) in query_string
        assert 'rev={}'.format(rev) in query_string


    @responses.activate
    def test_delete_replication_document_required_params(self):
        """
        test_delete_replication_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_replicator/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        doc_id = 'testString'

        # Invoke method
        response = service.delete_replication_document(
            doc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_delete_replication_document_value_error(self):
        """
        test_delete_replication_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_replicator/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "doc_id": doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_replication_document(**req_copy)



class TestGetReplicationDocument():
    """
    Test Class for get_replication_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_replication_document_all_params(self):
        """
        get_replication_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_replicator/testString')
        mock_response = '{"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}], "cancel": true, "checkpoint_interval": 0, "connection_timeout": 0, "continuous": true, "create_target": false, "create_target_params": {"n": 1, "partitioned": false, "q": 1}, "doc_ids": ["doc_ids"], "filter": "filter", "http_connections": 1, "query_params": {"mapKey": "inner"}, "retries_per_request": 0, "selector": {"mapKey": {"anyKey": "anyValue"}}, "since_seq": "since_seq", "socket_options": "socket_options", "source": {"auth": {"iam": {"api_key": "api_key"}}, "headers": {"mapKey": "inner"}, "url": "url"}, "source_proxy": "source_proxy", "target": {"auth": {"iam": {"api_key": "api_key"}}, "headers": {"mapKey": "inner"}, "url": "url"}, "target_proxy": "target_proxy", "use_checkpoints": false, "user_ctx": {"db": "db", "name": "name", "roles": ["_reader"]}, "worker_batch_size": 1, "worker_processes": 1}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        doc_id = 'testString'
        if_none_match = 'testString'
        attachments = True
        att_encoding_info = True
        atts_since = ['testString']
        conflicts = True
        deleted_conflicts = True
        latest = True
        local_seq = True
        meta = True
        open_revs = ['testString']
        rev = 'testString'
        revs = True
        revs_info = True

        # Invoke method
        response = service.get_replication_document(
            doc_id,
            if_none_match=if_none_match,
            attachments=attachments,
            att_encoding_info=att_encoding_info,
            atts_since=atts_since,
            conflicts=conflicts,
            deleted_conflicts=deleted_conflicts,
            latest=latest,
            local_seq=local_seq,
            meta=meta,
            open_revs=open_revs,
            rev=rev,
            revs=revs,
            revs_info=revs_info,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'attachments={}'.format('true' if attachments else 'false') in query_string
        assert 'att_encoding_info={}'.format('true' if att_encoding_info else 'false') in query_string
        assert 'atts_since={}'.format(','.join(atts_since)) in query_string
        assert 'conflicts={}'.format('true' if conflicts else 'false') in query_string
        assert 'deleted_conflicts={}'.format('true' if deleted_conflicts else 'false') in query_string
        assert 'latest={}'.format('true' if latest else 'false') in query_string
        assert 'local_seq={}'.format('true' if local_seq else 'false') in query_string
        assert 'meta={}'.format('true' if meta else 'false') in query_string
        assert 'open_revs={}'.format(','.join(open_revs)) in query_string
        assert 'rev={}'.format(rev) in query_string
        assert 'revs={}'.format('true' if revs else 'false') in query_string
        assert 'revs_info={}'.format('true' if revs_info else 'false') in query_string


    @responses.activate
    def test_get_replication_document_required_params(self):
        """
        test_get_replication_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_replicator/testString')
        mock_response = '{"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}], "cancel": true, "checkpoint_interval": 0, "connection_timeout": 0, "continuous": true, "create_target": false, "create_target_params": {"n": 1, "partitioned": false, "q": 1}, "doc_ids": ["doc_ids"], "filter": "filter", "http_connections": 1, "query_params": {"mapKey": "inner"}, "retries_per_request": 0, "selector": {"mapKey": {"anyKey": "anyValue"}}, "since_seq": "since_seq", "socket_options": "socket_options", "source": {"auth": {"iam": {"api_key": "api_key"}}, "headers": {"mapKey": "inner"}, "url": "url"}, "source_proxy": "source_proxy", "target": {"auth": {"iam": {"api_key": "api_key"}}, "headers": {"mapKey": "inner"}, "url": "url"}, "target_proxy": "target_proxy", "use_checkpoints": false, "user_ctx": {"db": "db", "name": "name", "roles": ["_reader"]}, "worker_batch_size": 1, "worker_processes": 1}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        doc_id = 'testString'

        # Invoke method
        response = service.get_replication_document(
            doc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_replication_document_value_error(self):
        """
        test_get_replication_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_replicator/testString')
        mock_response = '{"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}], "cancel": true, "checkpoint_interval": 0, "connection_timeout": 0, "continuous": true, "create_target": false, "create_target_params": {"n": 1, "partitioned": false, "q": 1}, "doc_ids": ["doc_ids"], "filter": "filter", "http_connections": 1, "query_params": {"mapKey": "inner"}, "retries_per_request": 0, "selector": {"mapKey": {"anyKey": "anyValue"}}, "since_seq": "since_seq", "socket_options": "socket_options", "source": {"auth": {"iam": {"api_key": "api_key"}}, "headers": {"mapKey": "inner"}, "url": "url"}, "source_proxy": "source_proxy", "target": {"auth": {"iam": {"api_key": "api_key"}}, "headers": {"mapKey": "inner"}, "url": "url"}, "target_proxy": "target_proxy", "use_checkpoints": false, "user_ctx": {"db": "db", "name": "name", "roles": ["_reader"]}, "worker_batch_size": 1, "worker_processes": 1}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "doc_id": doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_replication_document(**req_copy)



class TestPutReplicationDocument():
    """
    Test Class for put_replication_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_put_replication_document_all_params(self):
        """
        put_replication_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_replicator/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a ReplicationCreateTargetParameters model
        replication_create_target_parameters_model = {}
        replication_create_target_parameters_model['n'] = 1
        replication_create_target_parameters_model['partitioned'] = True
        replication_create_target_parameters_model['q'] = 1

        # Construct a dict representation of a ReplicationDatabaseAuthIam model
        replication_database_auth_iam_model = {}
        replication_database_auth_iam_model['api_key'] = 'testString'

        # Construct a dict representation of a ReplicationDatabaseAuth model
        replication_database_auth_model = {}
        replication_database_auth_model['iam'] = replication_database_auth_iam_model

        # Construct a dict representation of a ReplicationDatabase model
        replication_database_model = {}
        replication_database_model['auth'] = replication_database_auth_model
        replication_database_model['headers'] = {}
        replication_database_model['url'] = 'https://examples.cloudant.com/animaldb'

        # Construct a dict representation of a UserContext model
        user_context_model = {}
        user_context_model['db'] = 'testString'
        user_context_model['name'] = 'john'
        user_context_model['roles'] = ['researcher']

        # Construct a dict representation of a ReplicationDocument model
        replication_document_model = {}
        replication_document_model['_attachments'] = {}
        replication_document_model['_conflicts'] = ['testString']
        replication_document_model['_deleted'] = True
        replication_document_model['_deleted_conflicts'] = ['testString']
        replication_document_model['_id'] = 'testString'
        replication_document_model['_local_seq'] = 'testString'
        replication_document_model['_rev'] = 'testString'
        replication_document_model['_revisions'] = revisions_model
        replication_document_model['_revs_info'] = [document_revision_status_model]
        replication_document_model['cancel'] = False
        replication_document_model['checkpoint_interval'] = 4500
        replication_document_model['connection_timeout'] = 15000
        replication_document_model['continuous'] = True
        replication_document_model['create_target'] = True
        replication_document_model['create_target_params'] = replication_create_target_parameters_model
        replication_document_model['doc_ids'] = ['badger', 'lemur', 'llama']
        replication_document_model['filter'] = 'ddoc/my_filter'
        replication_document_model['http_connections'] = 10
        replication_document_model['query_params'] = {}
        replication_document_model['retries_per_request'] = 3
        replication_document_model['selector'] = {}
        replication_document_model['since_seq'] = '34-g1AAAAGjeJzLYWBgYMlgTmGQT0lKzi9KdU'
        replication_document_model['socket_options'] = '[{keepalive, true}, {nodelay, false}]'
        replication_document_model['source'] = replication_database_model
        replication_document_model['source_proxy'] = 'http://my-source-proxy.example:8888'
        replication_document_model['target'] = replication_database_model
        replication_document_model['target_proxy'] = 'http://my-target-proxy.example:8888'
        replication_document_model['use_checkpoints'] = False
        replication_document_model['user_ctx'] = user_context_model
        replication_document_model['worker_batch_size'] = 400
        replication_document_model['worker_processes'] = 3
        replication_document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        doc_id = 'testString'
        replication_document = replication_document_model
        if_match = 'testString'
        batch = 'ok'
        new_edits = True
        rev = 'testString'

        # Invoke method
        response = service.put_replication_document(
            doc_id,
            replication_document,
            if_match=if_match,
            batch=batch,
            new_edits=new_edits,
            rev=rev,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'batch={}'.format(batch) in query_string
        assert 'new_edits={}'.format('true' if new_edits else 'false') in query_string
        assert 'rev={}'.format(rev) in query_string
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == replication_document


    @responses.activate
    def test_put_replication_document_required_params(self):
        """
        test_put_replication_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_replicator/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a ReplicationCreateTargetParameters model
        replication_create_target_parameters_model = {}
        replication_create_target_parameters_model['n'] = 1
        replication_create_target_parameters_model['partitioned'] = True
        replication_create_target_parameters_model['q'] = 1

        # Construct a dict representation of a ReplicationDatabaseAuthIam model
        replication_database_auth_iam_model = {}
        replication_database_auth_iam_model['api_key'] = 'testString'

        # Construct a dict representation of a ReplicationDatabaseAuth model
        replication_database_auth_model = {}
        replication_database_auth_model['iam'] = replication_database_auth_iam_model

        # Construct a dict representation of a ReplicationDatabase model
        replication_database_model = {}
        replication_database_model['auth'] = replication_database_auth_model
        replication_database_model['headers'] = {}
        replication_database_model['url'] = 'https://examples.cloudant.com/animaldb'

        # Construct a dict representation of a UserContext model
        user_context_model = {}
        user_context_model['db'] = 'testString'
        user_context_model['name'] = 'john'
        user_context_model['roles'] = ['researcher']

        # Construct a dict representation of a ReplicationDocument model
        replication_document_model = {}
        replication_document_model['_attachments'] = {}
        replication_document_model['_conflicts'] = ['testString']
        replication_document_model['_deleted'] = True
        replication_document_model['_deleted_conflicts'] = ['testString']
        replication_document_model['_id'] = 'testString'
        replication_document_model['_local_seq'] = 'testString'
        replication_document_model['_rev'] = 'testString'
        replication_document_model['_revisions'] = revisions_model
        replication_document_model['_revs_info'] = [document_revision_status_model]
        replication_document_model['cancel'] = False
        replication_document_model['checkpoint_interval'] = 4500
        replication_document_model['connection_timeout'] = 15000
        replication_document_model['continuous'] = True
        replication_document_model['create_target'] = True
        replication_document_model['create_target_params'] = replication_create_target_parameters_model
        replication_document_model['doc_ids'] = ['badger', 'lemur', 'llama']
        replication_document_model['filter'] = 'ddoc/my_filter'
        replication_document_model['http_connections'] = 10
        replication_document_model['query_params'] = {}
        replication_document_model['retries_per_request'] = 3
        replication_document_model['selector'] = {}
        replication_document_model['since_seq'] = '34-g1AAAAGjeJzLYWBgYMlgTmGQT0lKzi9KdU'
        replication_document_model['socket_options'] = '[{keepalive, true}, {nodelay, false}]'
        replication_document_model['source'] = replication_database_model
        replication_document_model['source_proxy'] = 'http://my-source-proxy.example:8888'
        replication_document_model['target'] = replication_database_model
        replication_document_model['target_proxy'] = 'http://my-target-proxy.example:8888'
        replication_document_model['use_checkpoints'] = False
        replication_document_model['user_ctx'] = user_context_model
        replication_document_model['worker_batch_size'] = 400
        replication_document_model['worker_processes'] = 3
        replication_document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        doc_id = 'testString'
        replication_document = replication_document_model

        # Invoke method
        response = service.put_replication_document(
            doc_id,
            replication_document,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == replication_document


    @responses.activate
    def test_put_replication_document_value_error(self):
        """
        test_put_replication_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_replicator/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a ReplicationCreateTargetParameters model
        replication_create_target_parameters_model = {}
        replication_create_target_parameters_model['n'] = 1
        replication_create_target_parameters_model['partitioned'] = True
        replication_create_target_parameters_model['q'] = 1

        # Construct a dict representation of a ReplicationDatabaseAuthIam model
        replication_database_auth_iam_model = {}
        replication_database_auth_iam_model['api_key'] = 'testString'

        # Construct a dict representation of a ReplicationDatabaseAuth model
        replication_database_auth_model = {}
        replication_database_auth_model['iam'] = replication_database_auth_iam_model

        # Construct a dict representation of a ReplicationDatabase model
        replication_database_model = {}
        replication_database_model['auth'] = replication_database_auth_model
        replication_database_model['headers'] = {}
        replication_database_model['url'] = 'https://examples.cloudant.com/animaldb'

        # Construct a dict representation of a UserContext model
        user_context_model = {}
        user_context_model['db'] = 'testString'
        user_context_model['name'] = 'john'
        user_context_model['roles'] = ['researcher']

        # Construct a dict representation of a ReplicationDocument model
        replication_document_model = {}
        replication_document_model['_attachments'] = {}
        replication_document_model['_conflicts'] = ['testString']
        replication_document_model['_deleted'] = True
        replication_document_model['_deleted_conflicts'] = ['testString']
        replication_document_model['_id'] = 'testString'
        replication_document_model['_local_seq'] = 'testString'
        replication_document_model['_rev'] = 'testString'
        replication_document_model['_revisions'] = revisions_model
        replication_document_model['_revs_info'] = [document_revision_status_model]
        replication_document_model['cancel'] = False
        replication_document_model['checkpoint_interval'] = 4500
        replication_document_model['connection_timeout'] = 15000
        replication_document_model['continuous'] = True
        replication_document_model['create_target'] = True
        replication_document_model['create_target_params'] = replication_create_target_parameters_model
        replication_document_model['doc_ids'] = ['badger', 'lemur', 'llama']
        replication_document_model['filter'] = 'ddoc/my_filter'
        replication_document_model['http_connections'] = 10
        replication_document_model['query_params'] = {}
        replication_document_model['retries_per_request'] = 3
        replication_document_model['selector'] = {}
        replication_document_model['since_seq'] = '34-g1AAAAGjeJzLYWBgYMlgTmGQT0lKzi9KdU'
        replication_document_model['socket_options'] = '[{keepalive, true}, {nodelay, false}]'
        replication_document_model['source'] = replication_database_model
        replication_document_model['source_proxy'] = 'http://my-source-proxy.example:8888'
        replication_document_model['target'] = replication_database_model
        replication_document_model['target_proxy'] = 'http://my-target-proxy.example:8888'
        replication_document_model['use_checkpoints'] = False
        replication_document_model['user_ctx'] = user_context_model
        replication_document_model['worker_batch_size'] = 400
        replication_document_model['worker_processes'] = 3
        replication_document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        doc_id = 'testString'
        replication_document = replication_document_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "doc_id": doc_id,
            "replication_document": replication_document,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.put_replication_document(**req_copy)



class TestGetSchedulerDocs():
    """
    Test Class for get_scheduler_docs
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_scheduler_docs_all_params(self):
        """
        get_scheduler_docs()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_scheduler/docs')
        mock_response = '{"total_rows": 0, "docs": [{"database": "database", "doc_id": "doc_id", "error_count": 0, "id": "id", "info": {"changes_pending": 0, "checkpointed_source_seq": "checkpointed_source_seq", "doc_write_failures": 0, "docs_read": 0, "docs_written": 0, "error": "error", "missing_revisions_found": 0, "revisions_checked": 0, "source_seq": "source_seq", "through_seq": "through_seq"}, "last_updated": "2019-01-01T12:00:00.000Z", "node": "node", "source": "source", "source_proxy": "source_proxy", "start_time": "2019-01-01T12:00:00.000Z", "state": "initializing", "target": "target", "target_proxy": "target_proxy"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        limit = 0
        skip = 0
        states = ['initializing']

        # Invoke method
        response = service.get_scheduler_docs(
            limit=limit,
            skip=skip,
            states=states,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'skip={}'.format(skip) in query_string
        assert 'states={}'.format(','.join(states)) in query_string


    @responses.activate
    def test_get_scheduler_docs_required_params(self):
        """
        test_get_scheduler_docs_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_scheduler/docs')
        mock_response = '{"total_rows": 0, "docs": [{"database": "database", "doc_id": "doc_id", "error_count": 0, "id": "id", "info": {"changes_pending": 0, "checkpointed_source_seq": "checkpointed_source_seq", "doc_write_failures": 0, "docs_read": 0, "docs_written": 0, "error": "error", "missing_revisions_found": 0, "revisions_checked": 0, "source_seq": "source_seq", "through_seq": "through_seq"}, "last_updated": "2019-01-01T12:00:00.000Z", "node": "node", "source": "source", "source_proxy": "source_proxy", "start_time": "2019-01-01T12:00:00.000Z", "state": "initializing", "target": "target", "target_proxy": "target_proxy"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_scheduler_docs()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetSchedulerDocument():
    """
    Test Class for get_scheduler_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_scheduler_document_all_params(self):
        """
        get_scheduler_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_scheduler/docs/_replicator/testString')
        mock_response = '{"database": "database", "doc_id": "doc_id", "error_count": 0, "id": "id", "info": {"changes_pending": 0, "checkpointed_source_seq": "checkpointed_source_seq", "doc_write_failures": 0, "docs_read": 0, "docs_written": 0, "error": "error", "missing_revisions_found": 0, "revisions_checked": 0, "source_seq": "source_seq", "through_seq": "through_seq"}, "last_updated": "2019-01-01T12:00:00.000Z", "node": "node", "source": "source", "source_proxy": "source_proxy", "start_time": "2019-01-01T12:00:00.000Z", "state": "initializing", "target": "target", "target_proxy": "target_proxy"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        doc_id = 'testString'

        # Invoke method
        response = service.get_scheduler_document(
            doc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_scheduler_document_value_error(self):
        """
        test_get_scheduler_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_scheduler/docs/_replicator/testString')
        mock_response = '{"database": "database", "doc_id": "doc_id", "error_count": 0, "id": "id", "info": {"changes_pending": 0, "checkpointed_source_seq": "checkpointed_source_seq", "doc_write_failures": 0, "docs_read": 0, "docs_written": 0, "error": "error", "missing_revisions_found": 0, "revisions_checked": 0, "source_seq": "source_seq", "through_seq": "through_seq"}, "last_updated": "2019-01-01T12:00:00.000Z", "node": "node", "source": "source", "source_proxy": "source_proxy", "start_time": "2019-01-01T12:00:00.000Z", "state": "initializing", "target": "target", "target_proxy": "target_proxy"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "doc_id": doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_scheduler_document(**req_copy)



class TestGetSchedulerJobs():
    """
    Test Class for get_scheduler_jobs
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_scheduler_jobs_all_params(self):
        """
        get_scheduler_jobs()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_scheduler/jobs')
        mock_response = '{"total_rows": 0, "jobs": [{"database": "database", "doc_id": "doc_id", "history": [{"timestamp": "2019-01-01T12:00:00.000Z", "type": "type"}], "id": "id", "info": {"changes_pending": 0, "checkpointed_source_seq": "checkpointed_source_seq", "doc_write_failures": 0, "docs_read": 0, "docs_written": 0, "error": "error", "missing_revisions_found": 0, "revisions_checked": 0, "source_seq": "source_seq", "through_seq": "through_seq"}, "node": "node", "pid": "pid", "source": "source", "start_time": "2019-01-01T12:00:00.000Z", "target": "target", "user": "user"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        limit = 0
        skip = 0

        # Invoke method
        response = service.get_scheduler_jobs(
            limit=limit,
            skip=skip,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'skip={}'.format(skip) in query_string


    @responses.activate
    def test_get_scheduler_jobs_required_params(self):
        """
        test_get_scheduler_jobs_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_scheduler/jobs')
        mock_response = '{"total_rows": 0, "jobs": [{"database": "database", "doc_id": "doc_id", "history": [{"timestamp": "2019-01-01T12:00:00.000Z", "type": "type"}], "id": "id", "info": {"changes_pending": 0, "checkpointed_source_seq": "checkpointed_source_seq", "doc_write_failures": 0, "docs_read": 0, "docs_written": 0, "error": "error", "missing_revisions_found": 0, "revisions_checked": 0, "source_seq": "source_seq", "through_seq": "through_seq"}, "node": "node", "pid": "pid", "source": "source", "start_time": "2019-01-01T12:00:00.000Z", "target": "target", "user": "user"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_scheduler_jobs()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetSchedulerJob():
    """
    Test Class for get_scheduler_job
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_scheduler_job_all_params(self):
        """
        get_scheduler_job()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_scheduler/jobs/testString')
        mock_response = '{"database": "database", "doc_id": "doc_id", "history": [{"timestamp": "2019-01-01T12:00:00.000Z", "type": "type"}], "id": "id", "info": {"changes_pending": 0, "checkpointed_source_seq": "checkpointed_source_seq", "doc_write_failures": 0, "docs_read": 0, "docs_written": 0, "error": "error", "missing_revisions_found": 0, "revisions_checked": 0, "source_seq": "source_seq", "through_seq": "through_seq"}, "node": "node", "pid": "pid", "source": "source", "start_time": "2019-01-01T12:00:00.000Z", "target": "target", "user": "user"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        job_id = 'testString'

        # Invoke method
        response = service.get_scheduler_job(
            job_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_scheduler_job_value_error(self):
        """
        test_get_scheduler_job_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_scheduler/jobs/testString')
        mock_response = '{"database": "database", "doc_id": "doc_id", "history": [{"timestamp": "2019-01-01T12:00:00.000Z", "type": "type"}], "id": "id", "info": {"changes_pending": 0, "checkpointed_source_seq": "checkpointed_source_seq", "doc_write_failures": 0, "docs_read": 0, "docs_written": 0, "error": "error", "missing_revisions_found": 0, "revisions_checked": 0, "source_seq": "source_seq", "through_seq": "through_seq"}, "node": "node", "pid": "pid", "source": "source", "start_time": "2019-01-01T12:00:00.000Z", "target": "target", "user": "user"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        job_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "job_id": job_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_scheduler_job(**req_copy)



# endregion
##############################################################################
# End of Service: Replication
##############################################################################

##############################################################################
# Start of Service: Authentication
##############################################################################
# region

class TestGetSessionInformation():
    """
    Test Class for get_session_information
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_session_information_all_params(self):
        """
        get_session_information()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_session')
        mock_response = '{"ok": true, "info": {"authenticated": "authenticated", "authentication_db": "authentication_db", "authentication_handlers": ["authentication_handlers"]}, "userCtx": {"db": "db", "name": "name", "roles": ["_reader"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_session_information()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Authentication
##############################################################################

##############################################################################
# Start of Service: Authorization
##############################################################################
# region

class TestGetSecurity():
    """
    Test Class for get_security
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_security_all_params(self):
        """
        get_security()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_security')
        mock_response = '{"admins": {"names": ["names"], "roles": ["roles"]}, "members": {"names": ["names"], "roles": ["roles"]}, "cloudant": {"mapKey": ["_reader"]}, "couchdb_auth_only": false}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'

        # Invoke method
        response = service.get_security(
            db,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_security_value_error(self):
        """
        test_get_security_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_security')
        mock_response = '{"admins": {"names": ["names"], "roles": ["roles"]}, "members": {"names": ["names"], "roles": ["roles"]}, "cloudant": {"mapKey": ["_reader"]}, "couchdb_auth_only": false}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_security(**req_copy)



class TestPutSecurity():
    """
    Test Class for put_security
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_put_security_all_params(self):
        """
        put_security()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_security')
        mock_response = '{"ok": true}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SecurityObject model
        security_object_model = {}
        security_object_model['names'] = ['testString']
        security_object_model['roles'] = ['testString']

        # Set up parameter values
        db = 'testString'
        admins = security_object_model
        members = security_object_model
        cloudant = {}
        couchdb_auth_only = True

        # Invoke method
        response = service.put_security(
            db,
            admins=admins,
            members=members,
            cloudant=cloudant,
            couchdb_auth_only=couchdb_auth_only,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['admins'] == security_object_model
        assert req_body['members'] == security_object_model
        assert req_body['cloudant'] == {}
        assert req_body['couchdb_auth_only'] == True


    @responses.activate
    def test_put_security_value_error(self):
        """
        test_put_security_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_security')
        mock_response = '{"ok": true}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SecurityObject model
        security_object_model = {}
        security_object_model['names'] = ['testString']
        security_object_model['roles'] = ['testString']

        # Set up parameter values
        db = 'testString'
        admins = security_object_model
        members = security_object_model
        cloudant = {}
        couchdb_auth_only = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.put_security(**req_copy)



class TestPostApiKeys():
    """
    Test Class for post_api_keys
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_api_keys_all_params(self):
        """
        post_api_keys()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_api/v2/api_keys')
        mock_response = '{"ok": true, "key": "key", "password": "password"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Invoke method
        response = service.post_api_keys()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


class TestPutCloudantSecurityConfiguration():
    """
    Test Class for put_cloudant_security_configuration
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_put_cloudant_security_configuration_all_params(self):
        """
        put_cloudant_security_configuration()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_api/v2/db/testString/_security')
        mock_response = '{"ok": true}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SecurityObject model
        security_object_model = {}
        security_object_model['names'] = ['testString']
        security_object_model['roles'] = ['testString']

        # Set up parameter values
        db = 'testString'
        cloudant = {}
        admins = security_object_model
        members = security_object_model
        couchdb_auth_only = True

        # Invoke method
        response = service.put_cloudant_security_configuration(
            db,
            cloudant,
            admins=admins,
            members=members,
            couchdb_auth_only=couchdb_auth_only,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['cloudant'] == {}
        assert req_body['admins'] == security_object_model
        assert req_body['members'] == security_object_model
        assert req_body['couchdb_auth_only'] == True


    @responses.activate
    def test_put_cloudant_security_configuration_value_error(self):
        """
        test_put_cloudant_security_configuration_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_api/v2/db/testString/_security')
        mock_response = '{"ok": true}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SecurityObject model
        security_object_model = {}
        security_object_model['names'] = ['testString']
        security_object_model['roles'] = ['testString']

        # Set up parameter values
        db = 'testString'
        cloudant = {}
        admins = security_object_model
        members = security_object_model
        couchdb_auth_only = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "cloudant": cloudant,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.put_cloudant_security_configuration(**req_copy)



# endregion
##############################################################################
# End of Service: Authorization
##############################################################################

##############################################################################
# Start of Service: CORS
##############################################################################
# region

class TestGetCorsInformation():
    """
    Test Class for get_cors_information
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_cors_information_all_params(self):
        """
        get_cors_information()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_api/v2/user/config/cors')
        mock_response = '{"allow_credentials": false, "enable_cors": false, "origins": ["origins"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_cors_information()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestPutCorsConfiguration():
    """
    Test Class for put_cors_configuration
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_put_cors_configuration_all_params(self):
        """
        put_cors_configuration()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_api/v2/user/config/cors')
        mock_response = '{"ok": true}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        origins = ['testString']
        allow_credentials = True
        enable_cors = True

        # Invoke method
        response = service.put_cors_configuration(
            origins,
            allow_credentials=allow_credentials,
            enable_cors=enable_cors,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['origins'] == ['testString']
        assert req_body['allow_credentials'] == True
        assert req_body['enable_cors'] == True


    @responses.activate
    def test_put_cors_configuration_value_error(self):
        """
        test_put_cors_configuration_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_api/v2/user/config/cors')
        mock_response = '{"ok": true}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        origins = ['testString']
        allow_credentials = True
        enable_cors = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "origins": origins,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.put_cors_configuration(**req_copy)



# endregion
##############################################################################
# End of Service: CORS
##############################################################################

##############################################################################
# Start of Service: Attachments
##############################################################################
# region

class TestHeadAttachment():
    """
    Test Class for head_attachment
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_head_attachment_all_params(self):
        """
        head_attachment()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        attachment_name = 'testString'
        if_match = 'testString'
        if_none_match = 'testString'
        rev = 'testString'

        # Invoke method
        response = service.head_attachment(
            db,
            doc_id,
            attachment_name,
            if_match=if_match,
            if_none_match=if_none_match,
            rev=rev,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'rev={}'.format(rev) in query_string


    @responses.activate
    def test_head_attachment_required_params(self):
        """
        test_head_attachment_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        attachment_name = 'testString'

        # Invoke method
        response = service.head_attachment(
            db,
            doc_id,
            attachment_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_head_attachment_value_error(self):
        """
        test_head_attachment_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        attachment_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "doc_id": doc_id,
            "attachment_name": attachment_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.head_attachment(**req_copy)



class TestDeleteAttachment():
    """
    Test Class for delete_attachment
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_attachment_all_params(self):
        """
        delete_attachment()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        attachment_name = 'testString'
        if_match = 'testString'
        rev = 'testString'
        batch = 'ok'

        # Invoke method
        response = service.delete_attachment(
            db,
            doc_id,
            attachment_name,
            if_match=if_match,
            rev=rev,
            batch=batch,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'rev={}'.format(rev) in query_string
        assert 'batch={}'.format(batch) in query_string


    @responses.activate
    def test_delete_attachment_required_params(self):
        """
        test_delete_attachment_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        attachment_name = 'testString'

        # Invoke method
        response = service.delete_attachment(
            db,
            doc_id,
            attachment_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_delete_attachment_value_error(self):
        """
        test_delete_attachment_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        attachment_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "doc_id": doc_id,
            "attachment_name": attachment_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_attachment(**req_copy)



class TestGetAttachment():
    """
    Test Class for get_attachment
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_attachment_all_params(self):
        """
        get_attachment()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        attachment_name = 'testString'
        if_match = 'testString'
        if_none_match = 'testString'
        range = 'testString'
        rev = 'testString'

        # Invoke method
        response = service.get_attachment(
            db,
            doc_id,
            attachment_name,
            if_match=if_match,
            if_none_match=if_none_match,
            range=range,
            rev=rev,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'rev={}'.format(rev) in query_string


    @responses.activate
    def test_get_attachment_required_params(self):
        """
        test_get_attachment_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        attachment_name = 'testString'

        # Invoke method
        response = service.get_attachment(
            db,
            doc_id,
            attachment_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_attachment_value_error(self):
        """
        test_get_attachment_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        attachment_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "doc_id": doc_id,
            "attachment_name": attachment_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_attachment(**req_copy)



class TestPutAttachment():
    """
    Test Class for put_attachment
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_put_attachment_all_params(self):
        """
        put_attachment()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        attachment_name = 'testString'
        attachment = io.BytesIO(b'This is a mock file.').getvalue()
        content_type = 'testString'
        if_match = 'testString'
        rev = 'testString'

        # Invoke method
        response = service.put_attachment(
            db,
            doc_id,
            attachment_name,
            attachment,
            content_type,
            if_match=if_match,
            rev=rev,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'rev={}'.format(rev) in query_string
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params


    @responses.activate
    def test_put_attachment_required_params(self):
        """
        test_put_attachment_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        attachment_name = 'testString'
        attachment = io.BytesIO(b'This is a mock file.').getvalue()
        content_type = 'testString'

        # Invoke method
        response = service.put_attachment(
            db,
            doc_id,
            attachment_name,
            attachment,
            content_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params


    @responses.activate
    def test_put_attachment_value_error(self):
        """
        test_put_attachment_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/testString/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        attachment_name = 'testString'
        attachment = io.BytesIO(b'This is a mock file.').getvalue()
        content_type = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "doc_id": doc_id,
            "attachment_name": attachment_name,
            "attachment": attachment,
            "content_type": content_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.put_attachment(**req_copy)



# endregion
##############################################################################
# End of Service: Attachments
##############################################################################

##############################################################################
# Start of Service: LocalDocuments
##############################################################################
# region

class TestHeadLocalDocument():
    """
    Test Class for head_local_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_head_local_document_all_params(self):
        """
        head_local_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_local/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        if_none_match = 'testString'

        # Invoke method
        response = service.head_local_document(
            db,
            doc_id,
            if_none_match=if_none_match,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_head_local_document_required_params(self):
        """
        test_head_local_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_local/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Invoke method
        response = service.head_local_document(
            db,
            doc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_head_local_document_value_error(self):
        """
        test_head_local_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_local/testString')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "doc_id": doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.head_local_document(**req_copy)



class TestDeleteLocalDocument():
    """
    Test Class for delete_local_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_local_document_all_params(self):
        """
        delete_local_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_local/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        batch = 'ok'

        # Invoke method
        response = service.delete_local_document(
            db,
            doc_id,
            batch=batch,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'batch={}'.format(batch) in query_string


    @responses.activate
    def test_delete_local_document_required_params(self):
        """
        test_delete_local_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_local/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Invoke method
        response = service.delete_local_document(
            db,
            doc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_local_document_value_error(self):
        """
        test_delete_local_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_local/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "doc_id": doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_local_document(**req_copy)



class TestGetLocalDocument():
    """
    Test Class for get_local_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_local_document_all_params(self):
        """
        get_local_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_local/testString')
        mock_response = '{"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        accept = 'application/json'
        if_none_match = 'testString'
        attachments = True
        att_encoding_info = True
        atts_since = ['testString']
        local_seq = True

        # Invoke method
        response = service.get_local_document(
            db,
            doc_id,
            accept=accept,
            if_none_match=if_none_match,
            attachments=attachments,
            att_encoding_info=att_encoding_info,
            atts_since=atts_since,
            local_seq=local_seq,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'attachments={}'.format('true' if attachments else 'false') in query_string
        assert 'att_encoding_info={}'.format('true' if att_encoding_info else 'false') in query_string
        assert 'atts_since={}'.format(','.join(atts_since)) in query_string
        assert 'local_seq={}'.format('true' if local_seq else 'false') in query_string


    @responses.activate
    def test_get_local_document_required_params(self):
        """
        test_get_local_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_local/testString')
        mock_response = '{"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Invoke method
        response = service.get_local_document(
            db,
            doc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_local_document_value_error(self):
        """
        test_get_local_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_local/testString')
        mock_response = '{"_attachments": {"mapKey": {"content_type": "content_type", "data": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "digest": "digest", "encoded_length": 0, "encoding": "encoding", "follows": false, "length": 0, "revpos": 1, "stub": true}}, "_conflicts": ["conflicts"], "_deleted": false, "_deleted_conflicts": ["deleted_conflicts"], "_id": "id", "_local_seq": "local_seq", "_rev": "rev", "_revisions": {"ids": ["ids"], "start": 1}, "_revs_info": [{"rev": "rev", "status": "available"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "doc_id": doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_local_document(**req_copy)



class TestPutLocalDocument():
    """
    Test Class for put_local_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_put_local_document_all_params(self):
        """
        put_local_document()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_local/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a Document model
        document_model = {}
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'exampleid'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        document = document_model
        content_type = 'application/json'
        batch = 'ok'

        # Invoke method
        response = service.put_local_document(
            db,
            doc_id,
            document,
            content_type=content_type,
            batch=batch,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'batch={}'.format(batch) in query_string
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params


    @responses.activate
    def test_put_local_document_required_params(self):
        """
        test_put_local_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_local/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a Document model
        document_model = {}
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'exampleid'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        document = document_model

        # Invoke method
        response = service.put_local_document(
            db,
            doc_id,
            document,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params


    @responses.activate
    def test_put_local_document_value_error(self):
        """
        test_put_local_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_local/testString')
        mock_response = '{"id": "id", "rev": "rev", "ok": true, "caused_by": "caused_by", "error": "error", "reason": "reason"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Attachment model
        attachment_model = {}
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        # Construct a dict representation of a Revisions model
        revisions_model = {}
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {}
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a dict representation of a Document model
        document_model = {}
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'exampleid'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'
        document = document_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "doc_id": doc_id,
            "document": document,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.put_local_document(**req_copy)



# endregion
##############################################################################
# End of Service: LocalDocuments
##############################################################################

##############################################################################
# Start of Service: DatabaseDetails
##############################################################################
# region

class TestPostMissingRevs():
    """
    Test Class for post_missing_revs
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_missing_revs_all_params(self):
        """
        post_missing_revs()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_missing_revs')
        mock_response = '{"missing_revs": {"mapKey": ["inner"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        document_revisions = {}

        # Invoke method
        response = service.post_missing_revs(
            db,
            document_revisions,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == document_revisions


    @responses.activate
    def test_post_missing_revs_value_error(self):
        """
        test_post_missing_revs_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_missing_revs')
        mock_response = '{"missing_revs": {"mapKey": ["inner"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        document_revisions = {}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "document_revisions": document_revisions,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_missing_revs(**req_copy)



class TestPostRevsDiff():
    """
    Test Class for post_revs_diff
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_revs_diff_all_params(self):
        """
        post_revs_diff()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_revs_diff')
        mock_response = '{"mapKey": {"missing": ["missing"], "possible_ancestors": ["possible_ancestors"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        document_revisions = {}

        # Invoke method
        response = service.post_revs_diff(
            db,
            document_revisions,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == document_revisions


    @responses.activate
    def test_post_revs_diff_value_error(self):
        """
        test_post_revs_diff_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_revs_diff')
        mock_response = '{"mapKey": {"missing": ["missing"], "possible_ancestors": ["possible_ancestors"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        document_revisions = {}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "document_revisions": document_revisions,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_revs_diff(**req_copy)



class TestGetShardsInformation():
    """
    Test Class for get_shards_information
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_shards_information_all_params(self):
        """
        get_shards_information()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_shards')
        mock_response = '{"shards": {"mapKey": ["inner"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'

        # Invoke method
        response = service.get_shards_information(
            db,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_shards_information_value_error(self):
        """
        test_get_shards_information_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_shards')
        mock_response = '{"shards": {"mapKey": ["inner"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_shards_information(**req_copy)



class TestGetDocumentShardsInfo():
    """
    Test Class for get_document_shards_info
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_document_shards_info_all_params(self):
        """
        get_document_shards_info()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_shards/testString')
        mock_response = '{"nodes": ["nodes"], "range": "range"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Invoke method
        response = service.get_document_shards_info(
            db,
            doc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_document_shards_info_value_error(self):
        """
        test_get_document_shards_info_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/testString/_shards/testString')
        mock_response = '{"nodes": ["nodes"], "range": "range"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        db = 'testString'
        doc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "db": db,
            "doc_id": doc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_document_shards_info(**req_copy)



# endregion
##############################################################################
# End of Service: DatabaseDetails
##############################################################################

##############################################################################
# Start of Service: Monitoring
##############################################################################
# region

class TestHeadUpInformation():
    """
    Test Class for head_up_information
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_head_up_information_all_params(self):
        """
        head_up_information()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_up')
        responses.add(responses.HEAD,
                      url,
                      status=200)

        # Invoke method
        response = service.head_up_information()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetActiveTasks():
    """
    Test Class for get_active_tasks
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_active_tasks_all_params(self):
        """
        get_active_tasks()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_active_tasks')
        mock_response = '[{"changes_done": 0, "database": "database", "node": "node", "pid": "pid", "progress": 0, "started_on": 0, "status": "status", "task": "task", "total_changes": 0, "type": "type", "updated_on": 0}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_active_tasks()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetUpInformation():
    """
    Test Class for get_up_information
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_up_information_all_params(self):
        """
        get_up_information()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_up')
        mock_response = '{"seeds": {"anyKey": "anyValue"}, "status": "maintenance_mode"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_up_information()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetActivityTrackerEventsInformation():
    """
    Test Class for get_activity_tracker_events_information
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_activity_tracker_events_information_all_params(self):
        """
        get_activity_tracker_events_information()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_api/v2/user/activity_tracker/events')
        mock_response = '{"types": ["management"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_activity_tracker_events_information()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestPostActivityTrackerEventsConfiguration():
    """
    Test Class for post_activity_tracker_events_configuration
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_activity_tracker_events_configuration_all_params(self):
        """
        post_activity_tracker_events_configuration()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_api/v2/user/activity_tracker/events')
        mock_response = '{"ok": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        types = ['management']

        # Invoke method
        response = service.post_activity_tracker_events_configuration(
            types,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # decompress gzip compressed request body
        responses.calls[0].request.body = gzip.decompress(responses.calls[0].request.body)

        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['types'] == ['management']


    @responses.activate
    def test_post_activity_tracker_events_configuration_value_error(self):
        """
        test_post_activity_tracker_events_configuration_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_api/v2/user/activity_tracker/events')
        mock_response = '{"ok": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        types = ['management']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "types": types,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.post_activity_tracker_events_configuration(**req_copy)



class TestGetCurrentThroughputInformation():
    """
    Test Class for get_current_throughput_information
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_current_throughput_information_all_params(self):
        """
        get_current_throughput_information()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/_api/v2/user/current/throughput')
        mock_response = '{"throughput": {"query": 0, "read": 0, "write": 0}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_current_throughput_information()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Monitoring
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestActiveTask():
    """
    Test Class for ActiveTask
    """

    def test_active_task_serialization(self):
        """
        Test serialization/deserialization for ActiveTask
        """

        # Construct a json representation of a ActiveTask model
        active_task_model_json = {}
        active_task_model_json['changes_done'] = 0
        active_task_model_json['database'] = 'testString'
        active_task_model_json['node'] = 'testString'
        active_task_model_json['pid'] = 'testString'
        active_task_model_json['progress'] = 0
        active_task_model_json['started_on'] = 0
        active_task_model_json['status'] = 'testString'
        active_task_model_json['task'] = 'testString'
        active_task_model_json['total_changes'] = 0
        active_task_model_json['type'] = 'testString'
        active_task_model_json['updated_on'] = 0

        # Construct a model instance of ActiveTask by calling from_dict on the json representation
        active_task_model = ActiveTask.from_dict(active_task_model_json)
        assert active_task_model != False

        # Construct a model instance of ActiveTask by calling from_dict on the json representation
        active_task_model_dict = ActiveTask.from_dict(active_task_model_json).__dict__
        active_task_model2 = ActiveTask(**active_task_model_dict)

        # Verify the model instances are equivalent
        assert active_task_model == active_task_model2

        # Convert model instance back to dict and verify no loss of data
        active_task_model_json2 = active_task_model.to_dict()
        assert active_task_model_json2 == active_task_model_json

class TestActivityTrackerEventsConfiguration():
    """
    Test Class for ActivityTrackerEventsConfiguration
    """

    def test_activity_tracker_events_configuration_serialization(self):
        """
        Test serialization/deserialization for ActivityTrackerEventsConfiguration
        """

        # Construct a json representation of a ActivityTrackerEventsConfiguration model
        activity_tracker_events_configuration_model_json = {}
        activity_tracker_events_configuration_model_json['types'] = ['management']

        # Construct a model instance of ActivityTrackerEventsConfiguration by calling from_dict on the json representation
        activity_tracker_events_configuration_model = ActivityTrackerEventsConfiguration.from_dict(activity_tracker_events_configuration_model_json)
        assert activity_tracker_events_configuration_model != False

        # Construct a model instance of ActivityTrackerEventsConfiguration by calling from_dict on the json representation
        activity_tracker_events_configuration_model_dict = ActivityTrackerEventsConfiguration.from_dict(activity_tracker_events_configuration_model_json).__dict__
        activity_tracker_events_configuration_model2 = ActivityTrackerEventsConfiguration(**activity_tracker_events_configuration_model_dict)

        # Verify the model instances are equivalent
        assert activity_tracker_events_configuration_model == activity_tracker_events_configuration_model2

        # Convert model instance back to dict and verify no loss of data
        activity_tracker_events_configuration_model_json2 = activity_tracker_events_configuration_model.to_dict()
        assert activity_tracker_events_configuration_model_json2 == activity_tracker_events_configuration_model_json

class TestAllDocsQueriesResult():
    """
    Test Class for AllDocsQueriesResult
    """

    def test_all_docs_queries_result_serialization(self):
        """
        Test serialization/deserialization for AllDocsQueriesResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        docs_result_row_value_model = {} # DocsResultRowValue
        docs_result_row_value_model['rev'] = 'testString'

        docs_result_row_model = {} # DocsResultRow
        docs_result_row_model['caused_by'] = 'testString'
        docs_result_row_model['error'] = 'testString'
        docs_result_row_model['reason'] = 'testString'
        docs_result_row_model['doc'] = document_model
        docs_result_row_model['id'] = 'testString'
        docs_result_row_model['key'] = 'testString'
        docs_result_row_model['value'] = docs_result_row_value_model

        all_docs_result_model = {} # AllDocsResult
        all_docs_result_model['total_rows'] = 0
        all_docs_result_model['rows'] = [docs_result_row_model]
        all_docs_result_model['update_seq'] = 'testString'

        # Construct a json representation of a AllDocsQueriesResult model
        all_docs_queries_result_model_json = {}
        all_docs_queries_result_model_json['results'] = [all_docs_result_model]

        # Construct a model instance of AllDocsQueriesResult by calling from_dict on the json representation
        all_docs_queries_result_model = AllDocsQueriesResult.from_dict(all_docs_queries_result_model_json)
        assert all_docs_queries_result_model != False

        # Construct a model instance of AllDocsQueriesResult by calling from_dict on the json representation
        all_docs_queries_result_model_dict = AllDocsQueriesResult.from_dict(all_docs_queries_result_model_json).__dict__
        all_docs_queries_result_model2 = AllDocsQueriesResult(**all_docs_queries_result_model_dict)

        # Verify the model instances are equivalent
        assert all_docs_queries_result_model == all_docs_queries_result_model2

        # Convert model instance back to dict and verify no loss of data
        all_docs_queries_result_model_json2 = all_docs_queries_result_model.to_dict()
        assert all_docs_queries_result_model_json2 == all_docs_queries_result_model_json

class TestAllDocsQuery():
    """
    Test Class for AllDocsQuery
    """

    def test_all_docs_query_serialization(self):
        """
        Test serialization/deserialization for AllDocsQuery
        """

        # Construct a json representation of a AllDocsQuery model
        all_docs_query_model_json = {}
        all_docs_query_model_json['att_encoding_info'] = True
        all_docs_query_model_json['attachments'] = True
        all_docs_query_model_json['conflicts'] = True
        all_docs_query_model_json['descending'] = True
        all_docs_query_model_json['include_docs'] = True
        all_docs_query_model_json['inclusive_end'] = True
        all_docs_query_model_json['limit'] = 0
        all_docs_query_model_json['skip'] = 0
        all_docs_query_model_json['update_seq'] = True
        all_docs_query_model_json['endkey'] = 'testString'
        all_docs_query_model_json['key'] = 'testString'
        all_docs_query_model_json['keys'] = ['testString']
        all_docs_query_model_json['startkey'] = 'testString'

        # Construct a model instance of AllDocsQuery by calling from_dict on the json representation
        all_docs_query_model = AllDocsQuery.from_dict(all_docs_query_model_json)
        assert all_docs_query_model != False

        # Construct a model instance of AllDocsQuery by calling from_dict on the json representation
        all_docs_query_model_dict = AllDocsQuery.from_dict(all_docs_query_model_json).__dict__
        all_docs_query_model2 = AllDocsQuery(**all_docs_query_model_dict)

        # Verify the model instances are equivalent
        assert all_docs_query_model == all_docs_query_model2

        # Convert model instance back to dict and verify no loss of data
        all_docs_query_model_json2 = all_docs_query_model.to_dict()
        assert all_docs_query_model_json2 == all_docs_query_model_json

class TestAllDocsResult():
    """
    Test Class for AllDocsResult
    """

    def test_all_docs_result_serialization(self):
        """
        Test serialization/deserialization for AllDocsResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        docs_result_row_value_model = {} # DocsResultRowValue
        docs_result_row_value_model['rev'] = 'testString'

        docs_result_row_model = {} # DocsResultRow
        docs_result_row_model['caused_by'] = 'testString'
        docs_result_row_model['error'] = 'testString'
        docs_result_row_model['reason'] = 'testString'
        docs_result_row_model['doc'] = document_model
        docs_result_row_model['id'] = 'testString'
        docs_result_row_model['key'] = 'testString'
        docs_result_row_model['value'] = docs_result_row_value_model

        # Construct a json representation of a AllDocsResult model
        all_docs_result_model_json = {}
        all_docs_result_model_json['total_rows'] = 0
        all_docs_result_model_json['rows'] = [docs_result_row_model]
        all_docs_result_model_json['update_seq'] = 'testString'

        # Construct a model instance of AllDocsResult by calling from_dict on the json representation
        all_docs_result_model = AllDocsResult.from_dict(all_docs_result_model_json)
        assert all_docs_result_model != False

        # Construct a model instance of AllDocsResult by calling from_dict on the json representation
        all_docs_result_model_dict = AllDocsResult.from_dict(all_docs_result_model_json).__dict__
        all_docs_result_model2 = AllDocsResult(**all_docs_result_model_dict)

        # Verify the model instances are equivalent
        assert all_docs_result_model == all_docs_result_model2

        # Convert model instance back to dict and verify no loss of data
        all_docs_result_model_json2 = all_docs_result_model.to_dict()
        assert all_docs_result_model_json2 == all_docs_result_model_json

class TestAnalyzer():
    """
    Test Class for Analyzer
    """

    def test_analyzer_serialization(self):
        """
        Test serialization/deserialization for Analyzer
        """

        # Construct a json representation of a Analyzer model
        analyzer_model_json = {}
        analyzer_model_json['name'] = 'classic'
        analyzer_model_json['stopwords'] = ['testString']

        # Construct a model instance of Analyzer by calling from_dict on the json representation
        analyzer_model = Analyzer.from_dict(analyzer_model_json)
        assert analyzer_model != False

        # Construct a model instance of Analyzer by calling from_dict on the json representation
        analyzer_model_dict = Analyzer.from_dict(analyzer_model_json).__dict__
        analyzer_model2 = Analyzer(**analyzer_model_dict)

        # Verify the model instances are equivalent
        assert analyzer_model == analyzer_model2

        # Convert model instance back to dict and verify no loss of data
        analyzer_model_json2 = analyzer_model.to_dict()
        assert analyzer_model_json2 == analyzer_model_json

class TestAnalyzerConfiguration():
    """
    Test Class for AnalyzerConfiguration
    """

    def test_analyzer_configuration_serialization(self):
        """
        Test serialization/deserialization for AnalyzerConfiguration
        """

        # Construct dict forms of any model objects needed in order to build this model.

        analyzer_model = {} # Analyzer
        analyzer_model['name'] = 'classic'
        analyzer_model['stopwords'] = ['testString']

        # Construct a json representation of a AnalyzerConfiguration model
        analyzer_configuration_model_json = {}
        analyzer_configuration_model_json['name'] = 'classic'
        analyzer_configuration_model_json['stopwords'] = ['testString']
        analyzer_configuration_model_json['fields'] = {}

        # Construct a model instance of AnalyzerConfiguration by calling from_dict on the json representation
        analyzer_configuration_model = AnalyzerConfiguration.from_dict(analyzer_configuration_model_json)
        assert analyzer_configuration_model != False

        # Construct a model instance of AnalyzerConfiguration by calling from_dict on the json representation
        analyzer_configuration_model_dict = AnalyzerConfiguration.from_dict(analyzer_configuration_model_json).__dict__
        analyzer_configuration_model2 = AnalyzerConfiguration(**analyzer_configuration_model_dict)

        # Verify the model instances are equivalent
        assert analyzer_configuration_model == analyzer_configuration_model2

        # Convert model instance back to dict and verify no loss of data
        analyzer_configuration_model_json2 = analyzer_configuration_model.to_dict()
        assert analyzer_configuration_model_json2 == analyzer_configuration_model_json

class TestApiKeysResult():
    """
    Test Class for ApiKeysResult
    """

    def test_api_keys_result_serialization(self):
        """
        Test serialization/deserialization for ApiKeysResult
        """

        # Construct a json representation of a ApiKeysResult model
        api_keys_result_model_json = {}
        api_keys_result_model_json['ok'] = True
        api_keys_result_model_json['key'] = 'testString'
        api_keys_result_model_json['password'] = 'testString'

        # Construct a model instance of ApiKeysResult by calling from_dict on the json representation
        api_keys_result_model = ApiKeysResult.from_dict(api_keys_result_model_json)
        assert api_keys_result_model != False

        # Construct a model instance of ApiKeysResult by calling from_dict on the json representation
        api_keys_result_model_dict = ApiKeysResult.from_dict(api_keys_result_model_json).__dict__
        api_keys_result_model2 = ApiKeysResult(**api_keys_result_model_dict)

        # Verify the model instances are equivalent
        assert api_keys_result_model == api_keys_result_model2

        # Convert model instance back to dict and verify no loss of data
        api_keys_result_model_json2 = api_keys_result_model.to_dict()
        assert api_keys_result_model_json2 == api_keys_result_model_json

class TestAttachment():
    """
    Test Class for Attachment
    """

    def test_attachment_serialization(self):
        """
        Test serialization/deserialization for Attachment
        """

        # Construct a json representation of a Attachment model
        attachment_model_json = {}
        attachment_model_json['content_type'] = 'testString'
        attachment_model_json['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model_json['digest'] = 'testString'
        attachment_model_json['encoded_length'] = 0
        attachment_model_json['encoding'] = 'testString'
        attachment_model_json['follows'] = True
        attachment_model_json['length'] = 0
        attachment_model_json['revpos'] = 1
        attachment_model_json['stub'] = True

        # Construct a model instance of Attachment by calling from_dict on the json representation
        attachment_model = Attachment.from_dict(attachment_model_json)
        assert attachment_model != False

        # Construct a model instance of Attachment by calling from_dict on the json representation
        attachment_model_dict = Attachment.from_dict(attachment_model_json).__dict__
        attachment_model2 = Attachment(**attachment_model_dict)

        # Verify the model instances are equivalent
        assert attachment_model == attachment_model2

        # Convert model instance back to dict and verify no loss of data
        attachment_model_json2 = attachment_model.to_dict()
        assert attachment_model_json2 == attachment_model_json

class TestBulkDocs():
    """
    Test Class for BulkDocs
    """

    def test_bulk_docs_serialization(self):
        """
        Test serialization/deserialization for BulkDocs
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        # Construct a json representation of a BulkDocs model
        bulk_docs_model_json = {}
        bulk_docs_model_json['docs'] = [document_model]
        bulk_docs_model_json['new_edits'] = True

        # Construct a model instance of BulkDocs by calling from_dict on the json representation
        bulk_docs_model = BulkDocs.from_dict(bulk_docs_model_json)
        assert bulk_docs_model != False

        # Construct a model instance of BulkDocs by calling from_dict on the json representation
        bulk_docs_model_dict = BulkDocs.from_dict(bulk_docs_model_json).__dict__
        bulk_docs_model2 = BulkDocs(**bulk_docs_model_dict)

        # Verify the model instances are equivalent
        assert bulk_docs_model == bulk_docs_model2

        # Convert model instance back to dict and verify no loss of data
        bulk_docs_model_json2 = bulk_docs_model.to_dict()
        assert bulk_docs_model_json2 == bulk_docs_model_json

class TestBulkGetQueryDocument():
    """
    Test Class for BulkGetQueryDocument
    """

    def test_bulk_get_query_document_serialization(self):
        """
        Test serialization/deserialization for BulkGetQueryDocument
        """

        # Construct a json representation of a BulkGetQueryDocument model
        bulk_get_query_document_model_json = {}
        bulk_get_query_document_model_json['atts_since'] = ['testString']
        bulk_get_query_document_model_json['id'] = 'testString'
        bulk_get_query_document_model_json['open_revs'] = ['testString']
        bulk_get_query_document_model_json['rev'] = 'testString'

        # Construct a model instance of BulkGetQueryDocument by calling from_dict on the json representation
        bulk_get_query_document_model = BulkGetQueryDocument.from_dict(bulk_get_query_document_model_json)
        assert bulk_get_query_document_model != False

        # Construct a model instance of BulkGetQueryDocument by calling from_dict on the json representation
        bulk_get_query_document_model_dict = BulkGetQueryDocument.from_dict(bulk_get_query_document_model_json).__dict__
        bulk_get_query_document_model2 = BulkGetQueryDocument(**bulk_get_query_document_model_dict)

        # Verify the model instances are equivalent
        assert bulk_get_query_document_model == bulk_get_query_document_model2

        # Convert model instance back to dict and verify no loss of data
        bulk_get_query_document_model_json2 = bulk_get_query_document_model.to_dict()
        assert bulk_get_query_document_model_json2 == bulk_get_query_document_model_json

class TestBulkGetResult():
    """
    Test Class for BulkGetResult
    """

    def test_bulk_get_result_serialization(self):
        """
        Test serialization/deserialization for BulkGetResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        document_result_model = {} # DocumentResult
        document_result_model['id'] = 'testString'
        document_result_model['rev'] = 'testString'
        document_result_model['ok'] = True
        document_result_model['caused_by'] = 'testString'
        document_result_model['error'] = 'testString'
        document_result_model['reason'] = 'testString'

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        bulk_get_result_document_model = {} # BulkGetResultDocument
        bulk_get_result_document_model['error'] = document_result_model
        bulk_get_result_document_model['ok'] = document_model

        bulk_get_result_item_model = {} # BulkGetResultItem
        bulk_get_result_item_model['docs'] = [bulk_get_result_document_model]
        bulk_get_result_item_model['id'] = 'testString'

        # Construct a json representation of a BulkGetResult model
        bulk_get_result_model_json = {}
        bulk_get_result_model_json['results'] = [bulk_get_result_item_model]

        # Construct a model instance of BulkGetResult by calling from_dict on the json representation
        bulk_get_result_model = BulkGetResult.from_dict(bulk_get_result_model_json)
        assert bulk_get_result_model != False

        # Construct a model instance of BulkGetResult by calling from_dict on the json representation
        bulk_get_result_model_dict = BulkGetResult.from_dict(bulk_get_result_model_json).__dict__
        bulk_get_result_model2 = BulkGetResult(**bulk_get_result_model_dict)

        # Verify the model instances are equivalent
        assert bulk_get_result_model == bulk_get_result_model2

        # Convert model instance back to dict and verify no loss of data
        bulk_get_result_model_json2 = bulk_get_result_model.to_dict()
        assert bulk_get_result_model_json2 == bulk_get_result_model_json

class TestBulkGetResultDocument():
    """
    Test Class for BulkGetResultDocument
    """

    def test_bulk_get_result_document_serialization(self):
        """
        Test serialization/deserialization for BulkGetResultDocument
        """

        # Construct dict forms of any model objects needed in order to build this model.

        document_result_model = {} # DocumentResult
        document_result_model['id'] = 'testString'
        document_result_model['rev'] = 'testString'
        document_result_model['ok'] = True
        document_result_model['caused_by'] = 'testString'
        document_result_model['error'] = 'testString'
        document_result_model['reason'] = 'testString'

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        # Construct a json representation of a BulkGetResultDocument model
        bulk_get_result_document_model_json = {}
        bulk_get_result_document_model_json['error'] = document_result_model
        bulk_get_result_document_model_json['ok'] = document_model

        # Construct a model instance of BulkGetResultDocument by calling from_dict on the json representation
        bulk_get_result_document_model = BulkGetResultDocument.from_dict(bulk_get_result_document_model_json)
        assert bulk_get_result_document_model != False

        # Construct a model instance of BulkGetResultDocument by calling from_dict on the json representation
        bulk_get_result_document_model_dict = BulkGetResultDocument.from_dict(bulk_get_result_document_model_json).__dict__
        bulk_get_result_document_model2 = BulkGetResultDocument(**bulk_get_result_document_model_dict)

        # Verify the model instances are equivalent
        assert bulk_get_result_document_model == bulk_get_result_document_model2

        # Convert model instance back to dict and verify no loss of data
        bulk_get_result_document_model_json2 = bulk_get_result_document_model.to_dict()
        assert bulk_get_result_document_model_json2 == bulk_get_result_document_model_json

class TestBulkGetResultItem():
    """
    Test Class for BulkGetResultItem
    """

    def test_bulk_get_result_item_serialization(self):
        """
        Test serialization/deserialization for BulkGetResultItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        document_result_model = {} # DocumentResult
        document_result_model['id'] = 'testString'
        document_result_model['rev'] = 'testString'
        document_result_model['ok'] = True
        document_result_model['caused_by'] = 'testString'
        document_result_model['error'] = 'testString'
        document_result_model['reason'] = 'testString'

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        bulk_get_result_document_model = {} # BulkGetResultDocument
        bulk_get_result_document_model['error'] = document_result_model
        bulk_get_result_document_model['ok'] = document_model

        # Construct a json representation of a BulkGetResultItem model
        bulk_get_result_item_model_json = {}
        bulk_get_result_item_model_json['docs'] = [bulk_get_result_document_model]
        bulk_get_result_item_model_json['id'] = 'testString'

        # Construct a model instance of BulkGetResultItem by calling from_dict on the json representation
        bulk_get_result_item_model = BulkGetResultItem.from_dict(bulk_get_result_item_model_json)
        assert bulk_get_result_item_model != False

        # Construct a model instance of BulkGetResultItem by calling from_dict on the json representation
        bulk_get_result_item_model_dict = BulkGetResultItem.from_dict(bulk_get_result_item_model_json).__dict__
        bulk_get_result_item_model2 = BulkGetResultItem(**bulk_get_result_item_model_dict)

        # Verify the model instances are equivalent
        assert bulk_get_result_item_model == bulk_get_result_item_model2

        # Convert model instance back to dict and verify no loss of data
        bulk_get_result_item_model_json2 = bulk_get_result_item_model.to_dict()
        assert bulk_get_result_item_model_json2 == bulk_get_result_item_model_json

class TestCapacityThroughputInformation():
    """
    Test Class for CapacityThroughputInformation
    """

    def test_capacity_throughput_information_serialization(self):
        """
        Test serialization/deserialization for CapacityThroughputInformation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        throughput_information_model = {} # ThroughputInformation
        throughput_information_model['blocks'] = 0
        throughput_information_model['query'] = 0
        throughput_information_model['read'] = 0
        throughput_information_model['write'] = 0

        capacity_throughput_information_current_model = {} # CapacityThroughputInformationCurrent
        capacity_throughput_information_current_model['throughput'] = throughput_information_model

        capacity_throughput_information_target_model = {} # CapacityThroughputInformationTarget
        capacity_throughput_information_target_model['throughput'] = throughput_information_model

        # Construct a json representation of a CapacityThroughputInformation model
        capacity_throughput_information_model_json = {}
        capacity_throughput_information_model_json['current'] = capacity_throughput_information_current_model
        capacity_throughput_information_model_json['target'] = capacity_throughput_information_target_model

        # Construct a model instance of CapacityThroughputInformation by calling from_dict on the json representation
        capacity_throughput_information_model = CapacityThroughputInformation.from_dict(capacity_throughput_information_model_json)
        assert capacity_throughput_information_model != False

        # Construct a model instance of CapacityThroughputInformation by calling from_dict on the json representation
        capacity_throughput_information_model_dict = CapacityThroughputInformation.from_dict(capacity_throughput_information_model_json).__dict__
        capacity_throughput_information_model2 = CapacityThroughputInformation(**capacity_throughput_information_model_dict)

        # Verify the model instances are equivalent
        assert capacity_throughput_information_model == capacity_throughput_information_model2

        # Convert model instance back to dict and verify no loss of data
        capacity_throughput_information_model_json2 = capacity_throughput_information_model.to_dict()
        assert capacity_throughput_information_model_json2 == capacity_throughput_information_model_json

class TestCapacityThroughputInformationCurrent():
    """
    Test Class for CapacityThroughputInformationCurrent
    """

    def test_capacity_throughput_information_current_serialization(self):
        """
        Test serialization/deserialization for CapacityThroughputInformationCurrent
        """

        # Construct dict forms of any model objects needed in order to build this model.

        throughput_information_model = {} # ThroughputInformation
        throughput_information_model['blocks'] = 0
        throughput_information_model['query'] = 0
        throughput_information_model['read'] = 0
        throughput_information_model['write'] = 0

        # Construct a json representation of a CapacityThroughputInformationCurrent model
        capacity_throughput_information_current_model_json = {}
        capacity_throughput_information_current_model_json['throughput'] = throughput_information_model

        # Construct a model instance of CapacityThroughputInformationCurrent by calling from_dict on the json representation
        capacity_throughput_information_current_model = CapacityThroughputInformationCurrent.from_dict(capacity_throughput_information_current_model_json)
        assert capacity_throughput_information_current_model != False

        # Construct a model instance of CapacityThroughputInformationCurrent by calling from_dict on the json representation
        capacity_throughput_information_current_model_dict = CapacityThroughputInformationCurrent.from_dict(capacity_throughput_information_current_model_json).__dict__
        capacity_throughput_information_current_model2 = CapacityThroughputInformationCurrent(**capacity_throughput_information_current_model_dict)

        # Verify the model instances are equivalent
        assert capacity_throughput_information_current_model == capacity_throughput_information_current_model2

        # Convert model instance back to dict and verify no loss of data
        capacity_throughput_information_current_model_json2 = capacity_throughput_information_current_model.to_dict()
        assert capacity_throughput_information_current_model_json2 == capacity_throughput_information_current_model_json

class TestCapacityThroughputInformationTarget():
    """
    Test Class for CapacityThroughputInformationTarget
    """

    def test_capacity_throughput_information_target_serialization(self):
        """
        Test serialization/deserialization for CapacityThroughputInformationTarget
        """

        # Construct dict forms of any model objects needed in order to build this model.

        throughput_information_model = {} # ThroughputInformation
        throughput_information_model['blocks'] = 0
        throughput_information_model['query'] = 0
        throughput_information_model['read'] = 0
        throughput_information_model['write'] = 0

        # Construct a json representation of a CapacityThroughputInformationTarget model
        capacity_throughput_information_target_model_json = {}
        capacity_throughput_information_target_model_json['throughput'] = throughput_information_model

        # Construct a model instance of CapacityThroughputInformationTarget by calling from_dict on the json representation
        capacity_throughput_information_target_model = CapacityThroughputInformationTarget.from_dict(capacity_throughput_information_target_model_json)
        assert capacity_throughput_information_target_model != False

        # Construct a model instance of CapacityThroughputInformationTarget by calling from_dict on the json representation
        capacity_throughput_information_target_model_dict = CapacityThroughputInformationTarget.from_dict(capacity_throughput_information_target_model_json).__dict__
        capacity_throughput_information_target_model2 = CapacityThroughputInformationTarget(**capacity_throughput_information_target_model_dict)

        # Verify the model instances are equivalent
        assert capacity_throughput_information_target_model == capacity_throughput_information_target_model2

        # Convert model instance back to dict and verify no loss of data
        capacity_throughput_information_target_model_json2 = capacity_throughput_information_target_model.to_dict()
        assert capacity_throughput_information_target_model_json2 == capacity_throughput_information_target_model_json

class TestChange():
    """
    Test Class for Change
    """

    def test_change_serialization(self):
        """
        Test serialization/deserialization for Change
        """

        # Construct a json representation of a Change model
        change_model_json = {}
        change_model_json['rev'] = 'testString'

        # Construct a model instance of Change by calling from_dict on the json representation
        change_model = Change.from_dict(change_model_json)
        assert change_model != False

        # Construct a model instance of Change by calling from_dict on the json representation
        change_model_dict = Change.from_dict(change_model_json).__dict__
        change_model2 = Change(**change_model_dict)

        # Verify the model instances are equivalent
        assert change_model == change_model2

        # Convert model instance back to dict and verify no loss of data
        change_model_json2 = change_model.to_dict()
        assert change_model_json2 == change_model_json

class TestChangesResult():
    """
    Test Class for ChangesResult
    """

    def test_changes_result_serialization(self):
        """
        Test serialization/deserialization for ChangesResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        change_model = {} # Change
        change_model['rev'] = 'testString'

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        changes_result_item_model = {} # ChangesResultItem
        changes_result_item_model['changes'] = [change_model]
        changes_result_item_model['deleted'] = True
        changes_result_item_model['doc'] = document_model
        changes_result_item_model['id'] = 'testString'
        changes_result_item_model['seq'] = 'testString'

        # Construct a json representation of a ChangesResult model
        changes_result_model_json = {}
        changes_result_model_json['last_seq'] = 'testString'
        changes_result_model_json['pending'] = 26
        changes_result_model_json['results'] = [changes_result_item_model]

        # Construct a model instance of ChangesResult by calling from_dict on the json representation
        changes_result_model = ChangesResult.from_dict(changes_result_model_json)
        assert changes_result_model != False

        # Construct a model instance of ChangesResult by calling from_dict on the json representation
        changes_result_model_dict = ChangesResult.from_dict(changes_result_model_json).__dict__
        changes_result_model2 = ChangesResult(**changes_result_model_dict)

        # Verify the model instances are equivalent
        assert changes_result_model == changes_result_model2

        # Convert model instance back to dict and verify no loss of data
        changes_result_model_json2 = changes_result_model.to_dict()
        assert changes_result_model_json2 == changes_result_model_json

class TestChangesResultItem():
    """
    Test Class for ChangesResultItem
    """

    def test_changes_result_item_serialization(self):
        """
        Test serialization/deserialization for ChangesResultItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        change_model = {} # Change
        change_model['rev'] = 'testString'

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        # Construct a json representation of a ChangesResultItem model
        changes_result_item_model_json = {}
        changes_result_item_model_json['changes'] = [change_model]
        changes_result_item_model_json['deleted'] = True
        changes_result_item_model_json['doc'] = document_model
        changes_result_item_model_json['id'] = 'testString'
        changes_result_item_model_json['seq'] = 'testString'

        # Construct a model instance of ChangesResultItem by calling from_dict on the json representation
        changes_result_item_model = ChangesResultItem.from_dict(changes_result_item_model_json)
        assert changes_result_item_model != False

        # Construct a model instance of ChangesResultItem by calling from_dict on the json representation
        changes_result_item_model_dict = ChangesResultItem.from_dict(changes_result_item_model_json).__dict__
        changes_result_item_model2 = ChangesResultItem(**changes_result_item_model_dict)

        # Verify the model instances are equivalent
        assert changes_result_item_model == changes_result_item_model2

        # Convert model instance back to dict and verify no loss of data
        changes_result_item_model_json2 = changes_result_item_model.to_dict()
        assert changes_result_item_model_json2 == changes_result_item_model_json

class TestContentInformationSizes():
    """
    Test Class for ContentInformationSizes
    """

    def test_content_information_sizes_serialization(self):
        """
        Test serialization/deserialization for ContentInformationSizes
        """

        # Construct a json representation of a ContentInformationSizes model
        content_information_sizes_model_json = {}
        content_information_sizes_model_json['active'] = 26
        content_information_sizes_model_json['external'] = 26
        content_information_sizes_model_json['file'] = 26

        # Construct a model instance of ContentInformationSizes by calling from_dict on the json representation
        content_information_sizes_model = ContentInformationSizes.from_dict(content_information_sizes_model_json)
        assert content_information_sizes_model != False

        # Construct a model instance of ContentInformationSizes by calling from_dict on the json representation
        content_information_sizes_model_dict = ContentInformationSizes.from_dict(content_information_sizes_model_json).__dict__
        content_information_sizes_model2 = ContentInformationSizes(**content_information_sizes_model_dict)

        # Verify the model instances are equivalent
        assert content_information_sizes_model == content_information_sizes_model2

        # Convert model instance back to dict and verify no loss of data
        content_information_sizes_model_json2 = content_information_sizes_model.to_dict()
        assert content_information_sizes_model_json2 == content_information_sizes_model_json

class TestCorsInformation():
    """
    Test Class for CorsInformation
    """

    def test_cors_information_serialization(self):
        """
        Test serialization/deserialization for CorsInformation
        """

        # Construct a json representation of a CorsInformation model
        cors_information_model_json = {}
        cors_information_model_json['allow_credentials'] = True
        cors_information_model_json['enable_cors'] = True
        cors_information_model_json['origins'] = ['testString']

        # Construct a model instance of CorsInformation by calling from_dict on the json representation
        cors_information_model = CorsInformation.from_dict(cors_information_model_json)
        assert cors_information_model != False

        # Construct a model instance of CorsInformation by calling from_dict on the json representation
        cors_information_model_dict = CorsInformation.from_dict(cors_information_model_json).__dict__
        cors_information_model2 = CorsInformation(**cors_information_model_dict)

        # Verify the model instances are equivalent
        assert cors_information_model == cors_information_model2

        # Convert model instance back to dict and verify no loss of data
        cors_information_model_json2 = cors_information_model.to_dict()
        assert cors_information_model_json2 == cors_information_model_json

class TestCurrentThroughputInformation():
    """
    Test Class for CurrentThroughputInformation
    """

    def test_current_throughput_information_serialization(self):
        """
        Test serialization/deserialization for CurrentThroughputInformation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        current_throughput_information_throughput_model = {} # CurrentThroughputInformationThroughput
        current_throughput_information_throughput_model['query'] = 0
        current_throughput_information_throughput_model['read'] = 0
        current_throughput_information_throughput_model['write'] = 0

        # Construct a json representation of a CurrentThroughputInformation model
        current_throughput_information_model_json = {}
        current_throughput_information_model_json['throughput'] = current_throughput_information_throughput_model

        # Construct a model instance of CurrentThroughputInformation by calling from_dict on the json representation
        current_throughput_information_model = CurrentThroughputInformation.from_dict(current_throughput_information_model_json)
        assert current_throughput_information_model != False

        # Construct a model instance of CurrentThroughputInformation by calling from_dict on the json representation
        current_throughput_information_model_dict = CurrentThroughputInformation.from_dict(current_throughput_information_model_json).__dict__
        current_throughput_information_model2 = CurrentThroughputInformation(**current_throughput_information_model_dict)

        # Verify the model instances are equivalent
        assert current_throughput_information_model == current_throughput_information_model2

        # Convert model instance back to dict and verify no loss of data
        current_throughput_information_model_json2 = current_throughput_information_model.to_dict()
        assert current_throughput_information_model_json2 == current_throughput_information_model_json

class TestCurrentThroughputInformationThroughput():
    """
    Test Class for CurrentThroughputInformationThroughput
    """

    def test_current_throughput_information_throughput_serialization(self):
        """
        Test serialization/deserialization for CurrentThroughputInformationThroughput
        """

        # Construct a json representation of a CurrentThroughputInformationThroughput model
        current_throughput_information_throughput_model_json = {}
        current_throughput_information_throughput_model_json['query'] = 0
        current_throughput_information_throughput_model_json['read'] = 0
        current_throughput_information_throughput_model_json['write'] = 0

        # Construct a model instance of CurrentThroughputInformationThroughput by calling from_dict on the json representation
        current_throughput_information_throughput_model = CurrentThroughputInformationThroughput.from_dict(current_throughput_information_throughput_model_json)
        assert current_throughput_information_throughput_model != False

        # Construct a model instance of CurrentThroughputInformationThroughput by calling from_dict on the json representation
        current_throughput_information_throughput_model_dict = CurrentThroughputInformationThroughput.from_dict(current_throughput_information_throughput_model_json).__dict__
        current_throughput_information_throughput_model2 = CurrentThroughputInformationThroughput(**current_throughput_information_throughput_model_dict)

        # Verify the model instances are equivalent
        assert current_throughput_information_throughput_model == current_throughput_information_throughput_model2

        # Convert model instance back to dict and verify no loss of data
        current_throughput_information_throughput_model_json2 = current_throughput_information_throughput_model.to_dict()
        assert current_throughput_information_throughput_model_json2 == current_throughput_information_throughput_model_json

class TestDatabaseInformation():
    """
    Test Class for DatabaseInformation
    """

    def test_database_information_serialization(self):
        """
        Test serialization/deserialization for DatabaseInformation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        database_information_cluster_model = {} # DatabaseInformationCluster
        database_information_cluster_model['n'] = 1
        database_information_cluster_model['q'] = 1
        database_information_cluster_model['r'] = 1
        database_information_cluster_model['w'] = 1

        database_information_props_model = {} # DatabaseInformationProps
        database_information_props_model['partitioned'] = True

        content_information_sizes_model = {} # ContentInformationSizes
        content_information_sizes_model['active'] = 26
        content_information_sizes_model['external'] = 26
        content_information_sizes_model['file'] = 26

        # Construct a json representation of a DatabaseInformation model
        database_information_model_json = {}
        database_information_model_json['cluster'] = database_information_cluster_model
        database_information_model_json['committed_update_seq'] = 'testString'
        database_information_model_json['compact_running'] = True
        database_information_model_json['compacted_seq'] = 'testString'
        database_information_model_json['db_name'] = 'testString'
        database_information_model_json['disk_format_version'] = 26
        database_information_model_json['doc_count'] = 0
        database_information_model_json['doc_del_count'] = 0
        database_information_model_json['engine'] = 'testString'
        database_information_model_json['props'] = database_information_props_model
        database_information_model_json['sizes'] = content_information_sizes_model
        database_information_model_json['update_seq'] = 'testString'
        database_information_model_json['uuid'] = 'testString'

        # Construct a model instance of DatabaseInformation by calling from_dict on the json representation
        database_information_model = DatabaseInformation.from_dict(database_information_model_json)
        assert database_information_model != False

        # Construct a model instance of DatabaseInformation by calling from_dict on the json representation
        database_information_model_dict = DatabaseInformation.from_dict(database_information_model_json).__dict__
        database_information_model2 = DatabaseInformation(**database_information_model_dict)

        # Verify the model instances are equivalent
        assert database_information_model == database_information_model2

        # Convert model instance back to dict and verify no loss of data
        database_information_model_json2 = database_information_model.to_dict()
        assert database_information_model_json2 == database_information_model_json

class TestDatabaseInformationCluster():
    """
    Test Class for DatabaseInformationCluster
    """

    def test_database_information_cluster_serialization(self):
        """
        Test serialization/deserialization for DatabaseInformationCluster
        """

        # Construct a json representation of a DatabaseInformationCluster model
        database_information_cluster_model_json = {}
        database_information_cluster_model_json['n'] = 1
        database_information_cluster_model_json['q'] = 1
        database_information_cluster_model_json['r'] = 1
        database_information_cluster_model_json['w'] = 1

        # Construct a model instance of DatabaseInformationCluster by calling from_dict on the json representation
        database_information_cluster_model = DatabaseInformationCluster.from_dict(database_information_cluster_model_json)
        assert database_information_cluster_model != False

        # Construct a model instance of DatabaseInformationCluster by calling from_dict on the json representation
        database_information_cluster_model_dict = DatabaseInformationCluster.from_dict(database_information_cluster_model_json).__dict__
        database_information_cluster_model2 = DatabaseInformationCluster(**database_information_cluster_model_dict)

        # Verify the model instances are equivalent
        assert database_information_cluster_model == database_information_cluster_model2

        # Convert model instance back to dict and verify no loss of data
        database_information_cluster_model_json2 = database_information_cluster_model.to_dict()
        assert database_information_cluster_model_json2 == database_information_cluster_model_json

class TestDatabaseInformationProps():
    """
    Test Class for DatabaseInformationProps
    """

    def test_database_information_props_serialization(self):
        """
        Test serialization/deserialization for DatabaseInformationProps
        """

        # Construct a json representation of a DatabaseInformationProps model
        database_information_props_model_json = {}
        database_information_props_model_json['partitioned'] = True

        # Construct a model instance of DatabaseInformationProps by calling from_dict on the json representation
        database_information_props_model = DatabaseInformationProps.from_dict(database_information_props_model_json)
        assert database_information_props_model != False

        # Construct a model instance of DatabaseInformationProps by calling from_dict on the json representation
        database_information_props_model_dict = DatabaseInformationProps.from_dict(database_information_props_model_json).__dict__
        database_information_props_model2 = DatabaseInformationProps(**database_information_props_model_dict)

        # Verify the model instances are equivalent
        assert database_information_props_model == database_information_props_model2

        # Convert model instance back to dict and verify no loss of data
        database_information_props_model_json2 = database_information_props_model.to_dict()
        assert database_information_props_model_json2 == database_information_props_model_json

class TestDbEvent():
    """
    Test Class for DbEvent
    """

    def test_db_event_serialization(self):
        """
        Test serialization/deserialization for DbEvent
        """

        # Construct a json representation of a DbEvent model
        db_event_model_json = {}
        db_event_model_json['account'] = 'testString'
        db_event_model_json['db_name'] = 'testString'
        db_event_model_json['seq'] = 'testString'
        db_event_model_json['type'] = 'created'

        # Construct a model instance of DbEvent by calling from_dict on the json representation
        db_event_model = DbEvent.from_dict(db_event_model_json)
        assert db_event_model != False

        # Construct a model instance of DbEvent by calling from_dict on the json representation
        db_event_model_dict = DbEvent.from_dict(db_event_model_json).__dict__
        db_event_model2 = DbEvent(**db_event_model_dict)

        # Verify the model instances are equivalent
        assert db_event_model == db_event_model2

        # Convert model instance back to dict and verify no loss of data
        db_event_model_json2 = db_event_model.to_dict()
        assert db_event_model_json2 == db_event_model_json

class TestDbUpdates():
    """
    Test Class for DbUpdates
    """

    def test_db_updates_serialization(self):
        """
        Test serialization/deserialization for DbUpdates
        """

        # Construct dict forms of any model objects needed in order to build this model.

        db_event_model = {} # DbEvent
        db_event_model['account'] = 'testString'
        db_event_model['db_name'] = 'testString'
        db_event_model['seq'] = 'testString'
        db_event_model['type'] = 'created'

        # Construct a json representation of a DbUpdates model
        db_updates_model_json = {}
        db_updates_model_json['last_seq'] = 'testString'
        db_updates_model_json['results'] = [db_event_model]

        # Construct a model instance of DbUpdates by calling from_dict on the json representation
        db_updates_model = DbUpdates.from_dict(db_updates_model_json)
        assert db_updates_model != False

        # Construct a model instance of DbUpdates by calling from_dict on the json representation
        db_updates_model_dict = DbUpdates.from_dict(db_updates_model_json).__dict__
        db_updates_model2 = DbUpdates(**db_updates_model_dict)

        # Verify the model instances are equivalent
        assert db_updates_model == db_updates_model2

        # Convert model instance back to dict and verify no loss of data
        db_updates_model_json2 = db_updates_model.to_dict()
        assert db_updates_model_json2 == db_updates_model_json

class TestDbsInfoResult():
    """
    Test Class for DbsInfoResult
    """

    def test_dbs_info_result_serialization(self):
        """
        Test serialization/deserialization for DbsInfoResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        database_information_cluster_model = {} # DatabaseInformationCluster
        database_information_cluster_model['n'] = 1
        database_information_cluster_model['q'] = 1
        database_information_cluster_model['r'] = 1
        database_information_cluster_model['w'] = 1

        database_information_props_model = {} # DatabaseInformationProps
        database_information_props_model['partitioned'] = True

        content_information_sizes_model = {} # ContentInformationSizes
        content_information_sizes_model['active'] = 26
        content_information_sizes_model['external'] = 26
        content_information_sizes_model['file'] = 26

        database_information_model = {} # DatabaseInformation
        database_information_model['cluster'] = database_information_cluster_model
        database_information_model['committed_update_seq'] = 'testString'
        database_information_model['compact_running'] = True
        database_information_model['compacted_seq'] = 'testString'
        database_information_model['db_name'] = 'testString'
        database_information_model['disk_format_version'] = 26
        database_information_model['doc_count'] = 0
        database_information_model['doc_del_count'] = 0
        database_information_model['engine'] = 'testString'
        database_information_model['props'] = database_information_props_model
        database_information_model['sizes'] = content_information_sizes_model
        database_information_model['update_seq'] = 'testString'
        database_information_model['uuid'] = 'testString'

        # Construct a json representation of a DbsInfoResult model
        dbs_info_result_model_json = {}
        dbs_info_result_model_json['info'] = database_information_model
        dbs_info_result_model_json['key'] = 'testString'

        # Construct a model instance of DbsInfoResult by calling from_dict on the json representation
        dbs_info_result_model = DbsInfoResult.from_dict(dbs_info_result_model_json)
        assert dbs_info_result_model != False

        # Construct a model instance of DbsInfoResult by calling from_dict on the json representation
        dbs_info_result_model_dict = DbsInfoResult.from_dict(dbs_info_result_model_json).__dict__
        dbs_info_result_model2 = DbsInfoResult(**dbs_info_result_model_dict)

        # Verify the model instances are equivalent
        assert dbs_info_result_model == dbs_info_result_model2

        # Convert model instance back to dict and verify no loss of data
        dbs_info_result_model_json2 = dbs_info_result_model.to_dict()
        assert dbs_info_result_model_json2 == dbs_info_result_model_json

class TestDesignDocument():
    """
    Test Class for DesignDocument
    """

    def test_design_document_serialization(self):
        """
        Test serialization/deserialization for DesignDocument
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        analyzer_model = {} # Analyzer
        analyzer_model['name'] = 'classic'
        analyzer_model['stopwords'] = ['testString']

        analyzer_configuration_model = {} # AnalyzerConfiguration
        analyzer_configuration_model['name'] = 'classic'
        analyzer_configuration_model['stopwords'] = ['testString']
        analyzer_configuration_model['fields'] = {}

        search_index_definition_model = {} # SearchIndexDefinition
        search_index_definition_model['analyzer'] = analyzer_configuration_model
        search_index_definition_model['index'] = 'testString'

        design_document_options_model = {} # DesignDocumentOptions
        design_document_options_model['partitioned'] = True

        design_document_views_map_reduce_model = {} # DesignDocumentViewsMapReduce
        design_document_views_map_reduce_model['map'] = 'testString'
        design_document_views_map_reduce_model['reduce'] = 'testString'

        geo_index_definition_model = {} # GeoIndexDefinition
        geo_index_definition_model['index'] = 'testString'

        # Construct a json representation of a DesignDocument model
        design_document_model_json = {}
        design_document_model_json['_attachments'] = {}
        design_document_model_json['_conflicts'] = ['testString']
        design_document_model_json['_deleted'] = True
        design_document_model_json['_deleted_conflicts'] = ['testString']
        design_document_model_json['_id'] = 'testString'
        design_document_model_json['_local_seq'] = 'testString'
        design_document_model_json['_rev'] = 'testString'
        design_document_model_json['_revisions'] = revisions_model
        design_document_model_json['_revs_info'] = [document_revision_status_model]
        design_document_model_json['autoupdate'] = True
        design_document_model_json['filters'] = {}
        design_document_model_json['indexes'] = {}
        design_document_model_json['language'] = 'testString'
        design_document_model_json['options'] = design_document_options_model
        design_document_model_json['updates'] = {}
        design_document_model_json['validate_doc_update'] = {}
        design_document_model_json['views'] = {}
        design_document_model_json['st_indexes'] = {}
        design_document_model_json['foo'] = { 'foo': 'bar' }

        # Construct a model instance of DesignDocument by calling from_dict on the json representation
        design_document_model = DesignDocument.from_dict(design_document_model_json)
        assert design_document_model != False

        # Construct a model instance of DesignDocument by calling from_dict on the json representation
        design_document_model_dict = DesignDocument.from_dict(design_document_model_json).__dict__
        design_document_model2 = DesignDocument(**design_document_model_dict)

        # Verify the model instances are equivalent
        assert design_document_model == design_document_model2

        # Convert model instance back to dict and verify no loss of data
        design_document_model_json2 = design_document_model.to_dict()
        assert design_document_model_json2 == design_document_model_json

class TestDesignDocumentInformation():
    """
    Test Class for DesignDocumentInformation
    """

    def test_design_document_information_serialization(self):
        """
        Test serialization/deserialization for DesignDocumentInformation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        content_information_sizes_model = {} # ContentInformationSizes
        content_information_sizes_model['active'] = 26
        content_information_sizes_model['external'] = 26
        content_information_sizes_model['file'] = 26

        design_document_view_index_model = {} # DesignDocumentViewIndex
        design_document_view_index_model['compact_running'] = True
        design_document_view_index_model['language'] = 'testString'
        design_document_view_index_model['signature'] = 'testString'
        design_document_view_index_model['sizes'] = content_information_sizes_model
        design_document_view_index_model['update_seq'] = 'testString'
        design_document_view_index_model['updater_running'] = True
        design_document_view_index_model['waiting_clients'] = 0
        design_document_view_index_model['waiting_commit'] = True

        # Construct a json representation of a DesignDocumentInformation model
        design_document_information_model_json = {}
        design_document_information_model_json['name'] = 'testString'
        design_document_information_model_json['view_index'] = design_document_view_index_model

        # Construct a model instance of DesignDocumentInformation by calling from_dict on the json representation
        design_document_information_model = DesignDocumentInformation.from_dict(design_document_information_model_json)
        assert design_document_information_model != False

        # Construct a model instance of DesignDocumentInformation by calling from_dict on the json representation
        design_document_information_model_dict = DesignDocumentInformation.from_dict(design_document_information_model_json).__dict__
        design_document_information_model2 = DesignDocumentInformation(**design_document_information_model_dict)

        # Verify the model instances are equivalent
        assert design_document_information_model == design_document_information_model2

        # Convert model instance back to dict and verify no loss of data
        design_document_information_model_json2 = design_document_information_model.to_dict()
        assert design_document_information_model_json2 == design_document_information_model_json

class TestDesignDocumentOptions():
    """
    Test Class for DesignDocumentOptions
    """

    def test_design_document_options_serialization(self):
        """
        Test serialization/deserialization for DesignDocumentOptions
        """

        # Construct a json representation of a DesignDocumentOptions model
        design_document_options_model_json = {}
        design_document_options_model_json['partitioned'] = True

        # Construct a model instance of DesignDocumentOptions by calling from_dict on the json representation
        design_document_options_model = DesignDocumentOptions.from_dict(design_document_options_model_json)
        assert design_document_options_model != False

        # Construct a model instance of DesignDocumentOptions by calling from_dict on the json representation
        design_document_options_model_dict = DesignDocumentOptions.from_dict(design_document_options_model_json).__dict__
        design_document_options_model2 = DesignDocumentOptions(**design_document_options_model_dict)

        # Verify the model instances are equivalent
        assert design_document_options_model == design_document_options_model2

        # Convert model instance back to dict and verify no loss of data
        design_document_options_model_json2 = design_document_options_model.to_dict()
        assert design_document_options_model_json2 == design_document_options_model_json

class TestDesignDocumentViewIndex():
    """
    Test Class for DesignDocumentViewIndex
    """

    def test_design_document_view_index_serialization(self):
        """
        Test serialization/deserialization for DesignDocumentViewIndex
        """

        # Construct dict forms of any model objects needed in order to build this model.

        content_information_sizes_model = {} # ContentInformationSizes
        content_information_sizes_model['active'] = 26
        content_information_sizes_model['external'] = 26
        content_information_sizes_model['file'] = 26

        # Construct a json representation of a DesignDocumentViewIndex model
        design_document_view_index_model_json = {}
        design_document_view_index_model_json['compact_running'] = True
        design_document_view_index_model_json['language'] = 'testString'
        design_document_view_index_model_json['signature'] = 'testString'
        design_document_view_index_model_json['sizes'] = content_information_sizes_model
        design_document_view_index_model_json['update_seq'] = 'testString'
        design_document_view_index_model_json['updater_running'] = True
        design_document_view_index_model_json['waiting_clients'] = 0
        design_document_view_index_model_json['waiting_commit'] = True

        # Construct a model instance of DesignDocumentViewIndex by calling from_dict on the json representation
        design_document_view_index_model = DesignDocumentViewIndex.from_dict(design_document_view_index_model_json)
        assert design_document_view_index_model != False

        # Construct a model instance of DesignDocumentViewIndex by calling from_dict on the json representation
        design_document_view_index_model_dict = DesignDocumentViewIndex.from_dict(design_document_view_index_model_json).__dict__
        design_document_view_index_model2 = DesignDocumentViewIndex(**design_document_view_index_model_dict)

        # Verify the model instances are equivalent
        assert design_document_view_index_model == design_document_view_index_model2

        # Convert model instance back to dict and verify no loss of data
        design_document_view_index_model_json2 = design_document_view_index_model.to_dict()
        assert design_document_view_index_model_json2 == design_document_view_index_model_json

class TestDesignDocumentViewsMapReduce():
    """
    Test Class for DesignDocumentViewsMapReduce
    """

    def test_design_document_views_map_reduce_serialization(self):
        """
        Test serialization/deserialization for DesignDocumentViewsMapReduce
        """

        # Construct a json representation of a DesignDocumentViewsMapReduce model
        design_document_views_map_reduce_model_json = {}
        design_document_views_map_reduce_model_json['map'] = 'testString'
        design_document_views_map_reduce_model_json['reduce'] = 'testString'

        # Construct a model instance of DesignDocumentViewsMapReduce by calling from_dict on the json representation
        design_document_views_map_reduce_model = DesignDocumentViewsMapReduce.from_dict(design_document_views_map_reduce_model_json)
        assert design_document_views_map_reduce_model != False

        # Construct a model instance of DesignDocumentViewsMapReduce by calling from_dict on the json representation
        design_document_views_map_reduce_model_dict = DesignDocumentViewsMapReduce.from_dict(design_document_views_map_reduce_model_json).__dict__
        design_document_views_map_reduce_model2 = DesignDocumentViewsMapReduce(**design_document_views_map_reduce_model_dict)

        # Verify the model instances are equivalent
        assert design_document_views_map_reduce_model == design_document_views_map_reduce_model2

        # Convert model instance back to dict and verify no loss of data
        design_document_views_map_reduce_model_json2 = design_document_views_map_reduce_model.to_dict()
        assert design_document_views_map_reduce_model_json2 == design_document_views_map_reduce_model_json

class TestDocsResultRow():
    """
    Test Class for DocsResultRow
    """

    def test_docs_result_row_serialization(self):
        """
        Test serialization/deserialization for DocsResultRow
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        docs_result_row_value_model = {} # DocsResultRowValue
        docs_result_row_value_model['rev'] = 'testString'

        # Construct a json representation of a DocsResultRow model
        docs_result_row_model_json = {}
        docs_result_row_model_json['caused_by'] = 'testString'
        docs_result_row_model_json['error'] = 'testString'
        docs_result_row_model_json['reason'] = 'testString'
        docs_result_row_model_json['doc'] = document_model
        docs_result_row_model_json['id'] = 'testString'
        docs_result_row_model_json['key'] = 'testString'
        docs_result_row_model_json['value'] = docs_result_row_value_model

        # Construct a model instance of DocsResultRow by calling from_dict on the json representation
        docs_result_row_model = DocsResultRow.from_dict(docs_result_row_model_json)
        assert docs_result_row_model != False

        # Construct a model instance of DocsResultRow by calling from_dict on the json representation
        docs_result_row_model_dict = DocsResultRow.from_dict(docs_result_row_model_json).__dict__
        docs_result_row_model2 = DocsResultRow(**docs_result_row_model_dict)

        # Verify the model instances are equivalent
        assert docs_result_row_model == docs_result_row_model2

        # Convert model instance back to dict and verify no loss of data
        docs_result_row_model_json2 = docs_result_row_model.to_dict()
        assert docs_result_row_model_json2 == docs_result_row_model_json

class TestDocsResultRowValue():
    """
    Test Class for DocsResultRowValue
    """

    def test_docs_result_row_value_serialization(self):
        """
        Test serialization/deserialization for DocsResultRowValue
        """

        # Construct a json representation of a DocsResultRowValue model
        docs_result_row_value_model_json = {}
        docs_result_row_value_model_json['rev'] = 'testString'

        # Construct a model instance of DocsResultRowValue by calling from_dict on the json representation
        docs_result_row_value_model = DocsResultRowValue.from_dict(docs_result_row_value_model_json)
        assert docs_result_row_value_model != False

        # Construct a model instance of DocsResultRowValue by calling from_dict on the json representation
        docs_result_row_value_model_dict = DocsResultRowValue.from_dict(docs_result_row_value_model_json).__dict__
        docs_result_row_value_model2 = DocsResultRowValue(**docs_result_row_value_model_dict)

        # Verify the model instances are equivalent
        assert docs_result_row_value_model == docs_result_row_value_model2

        # Convert model instance back to dict and verify no loss of data
        docs_result_row_value_model_json2 = docs_result_row_value_model.to_dict()
        assert docs_result_row_value_model_json2 == docs_result_row_value_model_json

class TestDocument():
    """
    Test Class for Document
    """

    def test_document_serialization(self):
        """
        Test serialization/deserialization for Document
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        # Construct a json representation of a Document model
        document_model_json = {}
        document_model_json['_attachments'] = {}
        document_model_json['_conflicts'] = ['testString']
        document_model_json['_deleted'] = True
        document_model_json['_deleted_conflicts'] = ['testString']
        document_model_json['_id'] = 'testString'
        document_model_json['_local_seq'] = 'testString'
        document_model_json['_rev'] = 'testString'
        document_model_json['_revisions'] = revisions_model
        document_model_json['_revs_info'] = [document_revision_status_model]
        document_model_json['foo'] = { 'foo': 'bar' }

        # Construct a model instance of Document by calling from_dict on the json representation
        document_model = Document.from_dict(document_model_json)
        assert document_model != False

        # Construct a model instance of Document by calling from_dict on the json representation
        document_model_dict = Document.from_dict(document_model_json).__dict__
        document_model2 = Document(**document_model_dict)

        # Verify the model instances are equivalent
        assert document_model == document_model2

        # Convert model instance back to dict and verify no loss of data
        document_model_json2 = document_model.to_dict()
        assert document_model_json2 == document_model_json

class TestDocumentResult():
    """
    Test Class for DocumentResult
    """

    def test_document_result_serialization(self):
        """
        Test serialization/deserialization for DocumentResult
        """

        # Construct a json representation of a DocumentResult model
        document_result_model_json = {}
        document_result_model_json['id'] = 'testString'
        document_result_model_json['rev'] = 'testString'
        document_result_model_json['ok'] = True
        document_result_model_json['caused_by'] = 'testString'
        document_result_model_json['error'] = 'testString'
        document_result_model_json['reason'] = 'testString'

        # Construct a model instance of DocumentResult by calling from_dict on the json representation
        document_result_model = DocumentResult.from_dict(document_result_model_json)
        assert document_result_model != False

        # Construct a model instance of DocumentResult by calling from_dict on the json representation
        document_result_model_dict = DocumentResult.from_dict(document_result_model_json).__dict__
        document_result_model2 = DocumentResult(**document_result_model_dict)

        # Verify the model instances are equivalent
        assert document_result_model == document_result_model2

        # Convert model instance back to dict and verify no loss of data
        document_result_model_json2 = document_result_model.to_dict()
        assert document_result_model_json2 == document_result_model_json

class TestDocumentRevisionStatus():
    """
    Test Class for DocumentRevisionStatus
    """

    def test_document_revision_status_serialization(self):
        """
        Test serialization/deserialization for DocumentRevisionStatus
        """

        # Construct a json representation of a DocumentRevisionStatus model
        document_revision_status_model_json = {}
        document_revision_status_model_json['rev'] = 'testString'
        document_revision_status_model_json['status'] = 'available'

        # Construct a model instance of DocumentRevisionStatus by calling from_dict on the json representation
        document_revision_status_model = DocumentRevisionStatus.from_dict(document_revision_status_model_json)
        assert document_revision_status_model != False

        # Construct a model instance of DocumentRevisionStatus by calling from_dict on the json representation
        document_revision_status_model_dict = DocumentRevisionStatus.from_dict(document_revision_status_model_json).__dict__
        document_revision_status_model2 = DocumentRevisionStatus(**document_revision_status_model_dict)

        # Verify the model instances are equivalent
        assert document_revision_status_model == document_revision_status_model2

        # Convert model instance back to dict and verify no loss of data
        document_revision_status_model_json2 = document_revision_status_model.to_dict()
        assert document_revision_status_model_json2 == document_revision_status_model_json

class TestDocumentShardInfo():
    """
    Test Class for DocumentShardInfo
    """

    def test_document_shard_info_serialization(self):
        """
        Test serialization/deserialization for DocumentShardInfo
        """

        # Construct a json representation of a DocumentShardInfo model
        document_shard_info_model_json = {}
        document_shard_info_model_json['nodes'] = ['testString']
        document_shard_info_model_json['range'] = 'testString'

        # Construct a model instance of DocumentShardInfo by calling from_dict on the json representation
        document_shard_info_model = DocumentShardInfo.from_dict(document_shard_info_model_json)
        assert document_shard_info_model != False

        # Construct a model instance of DocumentShardInfo by calling from_dict on the json representation
        document_shard_info_model_dict = DocumentShardInfo.from_dict(document_shard_info_model_json).__dict__
        document_shard_info_model2 = DocumentShardInfo(**document_shard_info_model_dict)

        # Verify the model instances are equivalent
        assert document_shard_info_model == document_shard_info_model2

        # Convert model instance back to dict and verify no loss of data
        document_shard_info_model_json2 = document_shard_info_model.to_dict()
        assert document_shard_info_model_json2 == document_shard_info_model_json

class TestExecutionStats():
    """
    Test Class for ExecutionStats
    """

    def test_execution_stats_serialization(self):
        """
        Test serialization/deserialization for ExecutionStats
        """

        # Construct a json representation of a ExecutionStats model
        execution_stats_model_json = {}
        execution_stats_model_json['execution_time_ms'] = 72.5
        execution_stats_model_json['results_returned'] = 0
        execution_stats_model_json['total_docs_examined'] = 0
        execution_stats_model_json['total_keys_examined'] = 0
        execution_stats_model_json['total_quorum_docs_examined'] = 0

        # Construct a model instance of ExecutionStats by calling from_dict on the json representation
        execution_stats_model = ExecutionStats.from_dict(execution_stats_model_json)
        assert execution_stats_model != False

        # Construct a model instance of ExecutionStats by calling from_dict on the json representation
        execution_stats_model_dict = ExecutionStats.from_dict(execution_stats_model_json).__dict__
        execution_stats_model2 = ExecutionStats(**execution_stats_model_dict)

        # Verify the model instances are equivalent
        assert execution_stats_model == execution_stats_model2

        # Convert model instance back to dict and verify no loss of data
        execution_stats_model_json2 = execution_stats_model.to_dict()
        assert execution_stats_model_json2 == execution_stats_model_json

class TestExplainResult():
    """
    Test Class for ExplainResult
    """

    def test_explain_result_serialization(self):
        """
        Test serialization/deserialization for ExplainResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        analyzer_model = {} # Analyzer
        analyzer_model['name'] = 'classic'
        analyzer_model['stopwords'] = ['testString']

        index_text_operator_default_field_model = {} # IndexTextOperatorDefaultField
        index_text_operator_default_field_model['analyzer'] = analyzer_model
        index_text_operator_default_field_model['enabled'] = True

        index_field_model = {} # IndexField
        index_field_model['name'] = 'testString'
        index_field_model['type'] = 'boolean'
        index_field_model['foo'] = 'asc'

        index_definition_model = {} # IndexDefinition
        index_definition_model['default_analyzer'] = analyzer_model
        index_definition_model['default_field'] = index_text_operator_default_field_model
        index_definition_model['fields'] = [index_field_model]
        index_definition_model['index_array_lengths'] = True
        index_definition_model['partial_filter_selector'] = {}

        index_information_model = {} # IndexInformation
        index_information_model['ddoc'] = 'testString'
        index_information_model['def'] = index_definition_model
        index_information_model['name'] = 'testString'
        index_information_model['type'] = 'json'

        explain_result_range_model = {} # ExplainResultRange
        explain_result_range_model['end_key'] = [{ 'foo': 'bar' }]
        explain_result_range_model['start_key'] = [{ 'foo': 'bar' }]

        # Construct a json representation of a ExplainResult model
        explain_result_model_json = {}
        explain_result_model_json['dbname'] = 'testString'
        explain_result_model_json['fields'] = ['testString']
        explain_result_model_json['index'] = index_information_model
        explain_result_model_json['limit'] = 0
        explain_result_model_json['opts'] = {}
        explain_result_model_json['range'] = explain_result_range_model
        explain_result_model_json['selector'] = {}
        explain_result_model_json['skip'] = 0

        # Construct a model instance of ExplainResult by calling from_dict on the json representation
        explain_result_model = ExplainResult.from_dict(explain_result_model_json)
        assert explain_result_model != False

        # Construct a model instance of ExplainResult by calling from_dict on the json representation
        explain_result_model_dict = ExplainResult.from_dict(explain_result_model_json).__dict__
        explain_result_model2 = ExplainResult(**explain_result_model_dict)

        # Verify the model instances are equivalent
        assert explain_result_model == explain_result_model2

        # Convert model instance back to dict and verify no loss of data
        explain_result_model_json2 = explain_result_model.to_dict()
        assert explain_result_model_json2 == explain_result_model_json

class TestExplainResultRange():
    """
    Test Class for ExplainResultRange
    """

    def test_explain_result_range_serialization(self):
        """
        Test serialization/deserialization for ExplainResultRange
        """

        # Construct a json representation of a ExplainResultRange model
        explain_result_range_model_json = {}
        explain_result_range_model_json['end_key'] = [{ 'foo': 'bar' }]
        explain_result_range_model_json['start_key'] = [{ 'foo': 'bar' }]

        # Construct a model instance of ExplainResultRange by calling from_dict on the json representation
        explain_result_range_model = ExplainResultRange.from_dict(explain_result_range_model_json)
        assert explain_result_range_model != False

        # Construct a model instance of ExplainResultRange by calling from_dict on the json representation
        explain_result_range_model_dict = ExplainResultRange.from_dict(explain_result_range_model_json).__dict__
        explain_result_range_model2 = ExplainResultRange(**explain_result_range_model_dict)

        # Verify the model instances are equivalent
        assert explain_result_range_model == explain_result_range_model2

        # Convert model instance back to dict and verify no loss of data
        explain_result_range_model_json2 = explain_result_range_model.to_dict()
        assert explain_result_range_model_json2 == explain_result_range_model_json

class TestFindResult():
    """
    Test Class for FindResult
    """

    def test_find_result_serialization(self):
        """
        Test serialization/deserialization for FindResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        execution_stats_model = {} # ExecutionStats
        execution_stats_model['execution_time_ms'] = 72.5
        execution_stats_model['results_returned'] = 0
        execution_stats_model['total_docs_examined'] = 0
        execution_stats_model['total_keys_examined'] = 0
        execution_stats_model['total_quorum_docs_examined'] = 0

        # Construct a json representation of a FindResult model
        find_result_model_json = {}
        find_result_model_json['bookmark'] = 'testString'
        find_result_model_json['docs'] = [document_model]
        find_result_model_json['execution_stats'] = execution_stats_model
        find_result_model_json['warning'] = 'testString'

        # Construct a model instance of FindResult by calling from_dict on the json representation
        find_result_model = FindResult.from_dict(find_result_model_json)
        assert find_result_model != False

        # Construct a model instance of FindResult by calling from_dict on the json representation
        find_result_model_dict = FindResult.from_dict(find_result_model_json).__dict__
        find_result_model2 = FindResult(**find_result_model_dict)

        # Verify the model instances are equivalent
        assert find_result_model == find_result_model2

        # Convert model instance back to dict and verify no loss of data
        find_result_model_json2 = find_result_model.to_dict()
        assert find_result_model_json2 == find_result_model_json

class TestGeoIndexDefinition():
    """
    Test Class for GeoIndexDefinition
    """

    def test_geo_index_definition_serialization(self):
        """
        Test serialization/deserialization for GeoIndexDefinition
        """

        # Construct a json representation of a GeoIndexDefinition model
        geo_index_definition_model_json = {}
        geo_index_definition_model_json['index'] = 'testString'

        # Construct a model instance of GeoIndexDefinition by calling from_dict on the json representation
        geo_index_definition_model = GeoIndexDefinition.from_dict(geo_index_definition_model_json)
        assert geo_index_definition_model != False

        # Construct a model instance of GeoIndexDefinition by calling from_dict on the json representation
        geo_index_definition_model_dict = GeoIndexDefinition.from_dict(geo_index_definition_model_json).__dict__
        geo_index_definition_model2 = GeoIndexDefinition(**geo_index_definition_model_dict)

        # Verify the model instances are equivalent
        assert geo_index_definition_model == geo_index_definition_model2

        # Convert model instance back to dict and verify no loss of data
        geo_index_definition_model_json2 = geo_index_definition_model.to_dict()
        assert geo_index_definition_model_json2 == geo_index_definition_model_json

class TestGeoIndexInformation():
    """
    Test Class for GeoIndexInformation
    """

    def test_geo_index_information_serialization(self):
        """
        Test serialization/deserialization for GeoIndexInformation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        geo_index_stats_model = {} # GeoIndexStats
        geo_index_stats_model['data_size'] = 0
        geo_index_stats_model['disk_size'] = 0
        geo_index_stats_model['doc_count'] = 0

        # Construct a json representation of a GeoIndexInformation model
        geo_index_information_model_json = {}
        geo_index_information_model_json['geo_index'] = geo_index_stats_model
        geo_index_information_model_json['name'] = 'testString'

        # Construct a model instance of GeoIndexInformation by calling from_dict on the json representation
        geo_index_information_model = GeoIndexInformation.from_dict(geo_index_information_model_json)
        assert geo_index_information_model != False

        # Construct a model instance of GeoIndexInformation by calling from_dict on the json representation
        geo_index_information_model_dict = GeoIndexInformation.from_dict(geo_index_information_model_json).__dict__
        geo_index_information_model2 = GeoIndexInformation(**geo_index_information_model_dict)

        # Verify the model instances are equivalent
        assert geo_index_information_model == geo_index_information_model2

        # Convert model instance back to dict and verify no loss of data
        geo_index_information_model_json2 = geo_index_information_model.to_dict()
        assert geo_index_information_model_json2 == geo_index_information_model_json

class TestGeoIndexStats():
    """
    Test Class for GeoIndexStats
    """

    def test_geo_index_stats_serialization(self):
        """
        Test serialization/deserialization for GeoIndexStats
        """

        # Construct a json representation of a GeoIndexStats model
        geo_index_stats_model_json = {}
        geo_index_stats_model_json['data_size'] = 0
        geo_index_stats_model_json['disk_size'] = 0
        geo_index_stats_model_json['doc_count'] = 0

        # Construct a model instance of GeoIndexStats by calling from_dict on the json representation
        geo_index_stats_model = GeoIndexStats.from_dict(geo_index_stats_model_json)
        assert geo_index_stats_model != False

        # Construct a model instance of GeoIndexStats by calling from_dict on the json representation
        geo_index_stats_model_dict = GeoIndexStats.from_dict(geo_index_stats_model_json).__dict__
        geo_index_stats_model2 = GeoIndexStats(**geo_index_stats_model_dict)

        # Verify the model instances are equivalent
        assert geo_index_stats_model == geo_index_stats_model2

        # Convert model instance back to dict and verify no loss of data
        geo_index_stats_model_json2 = geo_index_stats_model.to_dict()
        assert geo_index_stats_model_json2 == geo_index_stats_model_json

class TestGeoJsonFeature():
    """
    Test Class for GeoJsonFeature
    """

    def test_geo_json_feature_serialization(self):
        """
        Test serialization/deserialization for GeoJsonFeature
        """

        # Construct dict forms of any model objects needed in order to build this model.

        geo_json_geometry_object_model = {} # GeoJsonGeometry
        geo_json_geometry_object_model['type'] = 'Point'
        geo_json_geometry_object_model['coordinates'] = [{ 'foo': 'bar' }]

        # Construct a json representation of a GeoJsonFeature model
        geo_json_feature_model_json = {}
        geo_json_feature_model_json['_id'] = 'testString'
        geo_json_feature_model_json['_rev'] = 'testString'
        geo_json_feature_model_json['bbox'] = [72.5]
        geo_json_feature_model_json['geometry'] = geo_json_geometry_object_model
        geo_json_feature_model_json['properties'] = {}
        geo_json_feature_model_json['type'] = 'Feature'
        geo_json_feature_model_json['foo'] = { 'foo': 'bar' }

        # Construct a model instance of GeoJsonFeature by calling from_dict on the json representation
        geo_json_feature_model = GeoJsonFeature.from_dict(geo_json_feature_model_json)
        assert geo_json_feature_model != False

        # Construct a model instance of GeoJsonFeature by calling from_dict on the json representation
        geo_json_feature_model_dict = GeoJsonFeature.from_dict(geo_json_feature_model_json).__dict__
        geo_json_feature_model2 = GeoJsonFeature(**geo_json_feature_model_dict)

        # Verify the model instances are equivalent
        assert geo_json_feature_model == geo_json_feature_model2

        # Convert model instance back to dict and verify no loss of data
        geo_json_feature_model_json2 = geo_json_feature_model.to_dict()
        assert geo_json_feature_model_json2 == geo_json_feature_model_json

class TestGeoResult():
    """
    Test Class for GeoResult
    """

    def test_geo_result_serialization(self):
        """
        Test serialization/deserialization for GeoResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        geo_json_geometry_object_model = {} # GeoJsonGeometry
        geo_json_geometry_object_model['type'] = 'Point'
        geo_json_geometry_object_model['coordinates'] = [{ 'foo': 'bar' }]

        geo_json_feature_model = {} # GeoJsonFeature
        geo_json_feature_model['_id'] = 'testString'
        geo_json_feature_model['_rev'] = 'testString'
        geo_json_feature_model['bbox'] = [72.5]
        geo_json_feature_model['geometry'] = geo_json_geometry_object_model
        geo_json_feature_model['properties'] = {}
        geo_json_feature_model['type'] = 'Feature'
        geo_json_feature_model['foo'] = { 'foo': 'bar' }

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        geo_json_geometry_model = {} # GeoJsonGeometry
        geo_json_geometry_model['type'] = 'Point'
        geo_json_geometry_model['coordinates'] = [{ 'foo': 'bar' }]

        geo_result_row_model = {} # GeoResultRow
        geo_result_row_model['doc'] = document_model
        geo_result_row_model['geometry'] = geo_json_geometry_model
        geo_result_row_model['id'] = 'testString'
        geo_result_row_model['rev'] = 'testString'

        # Construct a json representation of a GeoResult model
        geo_result_model_json = {}
        geo_result_model_json['bookmark'] = 'testString'
        geo_result_model_json['features'] = [geo_json_feature_model]
        geo_result_model_json['rows'] = [geo_result_row_model]
        geo_result_model_json['type'] = 'FeatureCollection'

        # Construct a model instance of GeoResult by calling from_dict on the json representation
        geo_result_model = GeoResult.from_dict(geo_result_model_json)
        assert geo_result_model != False

        # Construct a model instance of GeoResult by calling from_dict on the json representation
        geo_result_model_dict = GeoResult.from_dict(geo_result_model_json).__dict__
        geo_result_model2 = GeoResult(**geo_result_model_dict)

        # Verify the model instances are equivalent
        assert geo_result_model == geo_result_model2

        # Convert model instance back to dict and verify no loss of data
        geo_result_model_json2 = geo_result_model.to_dict()
        assert geo_result_model_json2 == geo_result_model_json

class TestGeoResultRow():
    """
    Test Class for GeoResultRow
    """

    def test_geo_result_row_serialization(self):
        """
        Test serialization/deserialization for GeoResultRow
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        geo_json_geometry_model = {} # GeoJsonGeometry
        geo_json_geometry_model['type'] = 'Point'
        geo_json_geometry_model['coordinates'] = [{ 'foo': 'bar' }]

        # Construct a json representation of a GeoResultRow model
        geo_result_row_model_json = {}
        geo_result_row_model_json['doc'] = document_model
        geo_result_row_model_json['geometry'] = geo_json_geometry_model
        geo_result_row_model_json['id'] = 'testString'
        geo_result_row_model_json['rev'] = 'testString'

        # Construct a model instance of GeoResultRow by calling from_dict on the json representation
        geo_result_row_model = GeoResultRow.from_dict(geo_result_row_model_json)
        assert geo_result_row_model != False

        # Construct a model instance of GeoResultRow by calling from_dict on the json representation
        geo_result_row_model_dict = GeoResultRow.from_dict(geo_result_row_model_json).__dict__
        geo_result_row_model2 = GeoResultRow(**geo_result_row_model_dict)

        # Verify the model instances are equivalent
        assert geo_result_row_model == geo_result_row_model2

        # Convert model instance back to dict and verify no loss of data
        geo_result_row_model_json2 = geo_result_row_model.to_dict()
        assert geo_result_row_model_json2 == geo_result_row_model_json

class TestIndexDefinition():
    """
    Test Class for IndexDefinition
    """

    def test_index_definition_serialization(self):
        """
        Test serialization/deserialization for IndexDefinition
        """

        # Construct dict forms of any model objects needed in order to build this model.

        analyzer_model = {} # Analyzer
        analyzer_model['name'] = 'classic'
        analyzer_model['stopwords'] = ['testString']

        index_text_operator_default_field_model = {} # IndexTextOperatorDefaultField
        index_text_operator_default_field_model['analyzer'] = analyzer_model
        index_text_operator_default_field_model['enabled'] = True

        index_field_model = {} # IndexField
        index_field_model['name'] = 'testString'
        index_field_model['type'] = 'boolean'
        index_field_model['foo'] = 'asc'

        # Construct a json representation of a IndexDefinition model
        index_definition_model_json = {}
        index_definition_model_json['default_analyzer'] = analyzer_model
        index_definition_model_json['default_field'] = index_text_operator_default_field_model
        index_definition_model_json['fields'] = [index_field_model]
        index_definition_model_json['index_array_lengths'] = True
        index_definition_model_json['partial_filter_selector'] = {}

        # Construct a model instance of IndexDefinition by calling from_dict on the json representation
        index_definition_model = IndexDefinition.from_dict(index_definition_model_json)
        assert index_definition_model != False

        # Construct a model instance of IndexDefinition by calling from_dict on the json representation
        index_definition_model_dict = IndexDefinition.from_dict(index_definition_model_json).__dict__
        index_definition_model2 = IndexDefinition(**index_definition_model_dict)

        # Verify the model instances are equivalent
        assert index_definition_model == index_definition_model2

        # Convert model instance back to dict and verify no loss of data
        index_definition_model_json2 = index_definition_model.to_dict()
        assert index_definition_model_json2 == index_definition_model_json

class TestIndexField():
    """
    Test Class for IndexField
    """

    def test_index_field_serialization(self):
        """
        Test serialization/deserialization for IndexField
        """

        # Construct a json representation of a IndexField model
        index_field_model_json = {}
        index_field_model_json['name'] = 'testString'
        index_field_model_json['type'] = 'boolean'
        index_field_model_json['foo'] = 'asc'

        # Construct a model instance of IndexField by calling from_dict on the json representation
        index_field_model = IndexField.from_dict(index_field_model_json)
        assert index_field_model != False

        # Construct a model instance of IndexField by calling from_dict on the json representation
        index_field_model_dict = IndexField.from_dict(index_field_model_json).__dict__
        index_field_model2 = IndexField(**index_field_model_dict)

        # Verify the model instances are equivalent
        assert index_field_model == index_field_model2

        # Convert model instance back to dict and verify no loss of data
        index_field_model_json2 = index_field_model.to_dict()
        assert index_field_model_json2 == index_field_model_json

class TestIndexInformation():
    """
    Test Class for IndexInformation
    """

    def test_index_information_serialization(self):
        """
        Test serialization/deserialization for IndexInformation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        analyzer_model = {} # Analyzer
        analyzer_model['name'] = 'classic'
        analyzer_model['stopwords'] = ['testString']

        index_text_operator_default_field_model = {} # IndexTextOperatorDefaultField
        index_text_operator_default_field_model['analyzer'] = analyzer_model
        index_text_operator_default_field_model['enabled'] = True

        index_field_model = {} # IndexField
        index_field_model['name'] = 'testString'
        index_field_model['type'] = 'boolean'
        index_field_model['foo'] = 'asc'

        index_definition_model = {} # IndexDefinition
        index_definition_model['default_analyzer'] = analyzer_model
        index_definition_model['default_field'] = index_text_operator_default_field_model
        index_definition_model['fields'] = [index_field_model]
        index_definition_model['index_array_lengths'] = True
        index_definition_model['partial_filter_selector'] = {}

        # Construct a json representation of a IndexInformation model
        index_information_model_json = {}
        index_information_model_json['ddoc'] = 'testString'
        index_information_model_json['def'] = index_definition_model
        index_information_model_json['name'] = 'testString'
        index_information_model_json['type'] = 'json'

        # Construct a model instance of IndexInformation by calling from_dict on the json representation
        index_information_model = IndexInformation.from_dict(index_information_model_json)
        assert index_information_model != False

        # Construct a model instance of IndexInformation by calling from_dict on the json representation
        index_information_model_dict = IndexInformation.from_dict(index_information_model_json).__dict__
        index_information_model2 = IndexInformation(**index_information_model_dict)

        # Verify the model instances are equivalent
        assert index_information_model == index_information_model2

        # Convert model instance back to dict and verify no loss of data
        index_information_model_json2 = index_information_model.to_dict()
        assert index_information_model_json2 == index_information_model_json

class TestIndexResult():
    """
    Test Class for IndexResult
    """

    def test_index_result_serialization(self):
        """
        Test serialization/deserialization for IndexResult
        """

        # Construct a json representation of a IndexResult model
        index_result_model_json = {}
        index_result_model_json['id'] = 'testString'
        index_result_model_json['name'] = 'testString'
        index_result_model_json['result'] = 'created'

        # Construct a model instance of IndexResult by calling from_dict on the json representation
        index_result_model = IndexResult.from_dict(index_result_model_json)
        assert index_result_model != False

        # Construct a model instance of IndexResult by calling from_dict on the json representation
        index_result_model_dict = IndexResult.from_dict(index_result_model_json).__dict__
        index_result_model2 = IndexResult(**index_result_model_dict)

        # Verify the model instances are equivalent
        assert index_result_model == index_result_model2

        # Convert model instance back to dict and verify no loss of data
        index_result_model_json2 = index_result_model.to_dict()
        assert index_result_model_json2 == index_result_model_json

class TestIndexTextOperatorDefaultField():
    """
    Test Class for IndexTextOperatorDefaultField
    """

    def test_index_text_operator_default_field_serialization(self):
        """
        Test serialization/deserialization for IndexTextOperatorDefaultField
        """

        # Construct dict forms of any model objects needed in order to build this model.

        analyzer_model = {} # Analyzer
        analyzer_model['name'] = 'classic'
        analyzer_model['stopwords'] = ['testString']

        # Construct a json representation of a IndexTextOperatorDefaultField model
        index_text_operator_default_field_model_json = {}
        index_text_operator_default_field_model_json['analyzer'] = analyzer_model
        index_text_operator_default_field_model_json['enabled'] = True

        # Construct a model instance of IndexTextOperatorDefaultField by calling from_dict on the json representation
        index_text_operator_default_field_model = IndexTextOperatorDefaultField.from_dict(index_text_operator_default_field_model_json)
        assert index_text_operator_default_field_model != False

        # Construct a model instance of IndexTextOperatorDefaultField by calling from_dict on the json representation
        index_text_operator_default_field_model_dict = IndexTextOperatorDefaultField.from_dict(index_text_operator_default_field_model_json).__dict__
        index_text_operator_default_field_model2 = IndexTextOperatorDefaultField(**index_text_operator_default_field_model_dict)

        # Verify the model instances are equivalent
        assert index_text_operator_default_field_model == index_text_operator_default_field_model2

        # Convert model instance back to dict and verify no loss of data
        index_text_operator_default_field_model_json2 = index_text_operator_default_field_model.to_dict()
        assert index_text_operator_default_field_model_json2 == index_text_operator_default_field_model_json

class TestIndexesInformation():
    """
    Test Class for IndexesInformation
    """

    def test_indexes_information_serialization(self):
        """
        Test serialization/deserialization for IndexesInformation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        analyzer_model = {} # Analyzer
        analyzer_model['name'] = 'classic'
        analyzer_model['stopwords'] = ['testString']

        index_text_operator_default_field_model = {} # IndexTextOperatorDefaultField
        index_text_operator_default_field_model['analyzer'] = analyzer_model
        index_text_operator_default_field_model['enabled'] = True

        index_field_model = {} # IndexField
        index_field_model['name'] = 'testString'
        index_field_model['type'] = 'boolean'
        index_field_model['foo'] = 'asc'

        index_definition_model = {} # IndexDefinition
        index_definition_model['default_analyzer'] = analyzer_model
        index_definition_model['default_field'] = index_text_operator_default_field_model
        index_definition_model['fields'] = [index_field_model]
        index_definition_model['index_array_lengths'] = True
        index_definition_model['partial_filter_selector'] = {}

        index_information_model = {} # IndexInformation
        index_information_model['ddoc'] = 'testString'
        index_information_model['def'] = index_definition_model
        index_information_model['name'] = 'testString'
        index_information_model['type'] = 'json'

        # Construct a json representation of a IndexesInformation model
        indexes_information_model_json = {}
        indexes_information_model_json['total_rows'] = 0
        indexes_information_model_json['indexes'] = [index_information_model]

        # Construct a model instance of IndexesInformation by calling from_dict on the json representation
        indexes_information_model = IndexesInformation.from_dict(indexes_information_model_json)
        assert indexes_information_model != False

        # Construct a model instance of IndexesInformation by calling from_dict on the json representation
        indexes_information_model_dict = IndexesInformation.from_dict(indexes_information_model_json).__dict__
        indexes_information_model2 = IndexesInformation(**indexes_information_model_dict)

        # Verify the model instances are equivalent
        assert indexes_information_model == indexes_information_model2

        # Convert model instance back to dict and verify no loss of data
        indexes_information_model_json2 = indexes_information_model.to_dict()
        assert indexes_information_model_json2 == indexes_information_model_json

class TestMembershipInformation():
    """
    Test Class for MembershipInformation
    """

    def test_membership_information_serialization(self):
        """
        Test serialization/deserialization for MembershipInformation
        """

        # Construct a json representation of a MembershipInformation model
        membership_information_model_json = {}
        membership_information_model_json['all_nodes'] = ['testString']
        membership_information_model_json['cluster_nodes'] = ['testString']

        # Construct a model instance of MembershipInformation by calling from_dict on the json representation
        membership_information_model = MembershipInformation.from_dict(membership_information_model_json)
        assert membership_information_model != False

        # Construct a model instance of MembershipInformation by calling from_dict on the json representation
        membership_information_model_dict = MembershipInformation.from_dict(membership_information_model_json).__dict__
        membership_information_model2 = MembershipInformation(**membership_information_model_dict)

        # Verify the model instances are equivalent
        assert membership_information_model == membership_information_model2

        # Convert model instance back to dict and verify no loss of data
        membership_information_model_json2 = membership_information_model.to_dict()
        assert membership_information_model_json2 == membership_information_model_json

class TestMissingRevsResult():
    """
    Test Class for MissingRevsResult
    """

    def test_missing_revs_result_serialization(self):
        """
        Test serialization/deserialization for MissingRevsResult
        """

        # Construct a json representation of a MissingRevsResult model
        missing_revs_result_model_json = {}
        missing_revs_result_model_json['missing_revs'] = {}

        # Construct a model instance of MissingRevsResult by calling from_dict on the json representation
        missing_revs_result_model = MissingRevsResult.from_dict(missing_revs_result_model_json)
        assert missing_revs_result_model != False

        # Construct a model instance of MissingRevsResult by calling from_dict on the json representation
        missing_revs_result_model_dict = MissingRevsResult.from_dict(missing_revs_result_model_json).__dict__
        missing_revs_result_model2 = MissingRevsResult(**missing_revs_result_model_dict)

        # Verify the model instances are equivalent
        assert missing_revs_result_model == missing_revs_result_model2

        # Convert model instance back to dict and verify no loss of data
        missing_revs_result_model_json2 = missing_revs_result_model.to_dict()
        assert missing_revs_result_model_json2 == missing_revs_result_model_json

class TestOk():
    """
    Test Class for Ok
    """

    def test_ok_serialization(self):
        """
        Test serialization/deserialization for Ok
        """

        # Construct a json representation of a Ok model
        ok_model_json = {}
        ok_model_json['ok'] = True

        # Construct a model instance of Ok by calling from_dict on the json representation
        ok_model = Ok.from_dict(ok_model_json)
        assert ok_model != False

        # Construct a model instance of Ok by calling from_dict on the json representation
        ok_model_dict = Ok.from_dict(ok_model_json).__dict__
        ok_model2 = Ok(**ok_model_dict)

        # Verify the model instances are equivalent
        assert ok_model == ok_model2

        # Convert model instance back to dict and verify no loss of data
        ok_model_json2 = ok_model.to_dict()
        assert ok_model_json2 == ok_model_json

class TestPartitionInformation():
    """
    Test Class for PartitionInformation
    """

    def test_partition_information_serialization(self):
        """
        Test serialization/deserialization for PartitionInformation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        partition_information_indexes_indexes_model = {} # PartitionInformationIndexesIndexes
        partition_information_indexes_indexes_model['search'] = 0
        partition_information_indexes_indexes_model['view'] = 0

        partition_information_indexes_model = {} # PartitionInformationIndexes
        partition_information_indexes_model['count'] = 0
        partition_information_indexes_model['indexes'] = partition_information_indexes_indexes_model
        partition_information_indexes_model['limit'] = 0

        partition_information_sizes_model = {} # PartitionInformationSizes
        partition_information_sizes_model['active'] = 0
        partition_information_sizes_model['external'] = 0

        # Construct a json representation of a PartitionInformation model
        partition_information_model_json = {}
        partition_information_model_json['db_name'] = 'testString'
        partition_information_model_json['doc_count'] = 0
        partition_information_model_json['doc_del_count'] = 0
        partition_information_model_json['partition'] = 'testString'
        partition_information_model_json['partitioned_indexes'] = partition_information_indexes_model
        partition_information_model_json['sizes'] = partition_information_sizes_model

        # Construct a model instance of PartitionInformation by calling from_dict on the json representation
        partition_information_model = PartitionInformation.from_dict(partition_information_model_json)
        assert partition_information_model != False

        # Construct a model instance of PartitionInformation by calling from_dict on the json representation
        partition_information_model_dict = PartitionInformation.from_dict(partition_information_model_json).__dict__
        partition_information_model2 = PartitionInformation(**partition_information_model_dict)

        # Verify the model instances are equivalent
        assert partition_information_model == partition_information_model2

        # Convert model instance back to dict and verify no loss of data
        partition_information_model_json2 = partition_information_model.to_dict()
        assert partition_information_model_json2 == partition_information_model_json

class TestPartitionInformationIndexes():
    """
    Test Class for PartitionInformationIndexes
    """

    def test_partition_information_indexes_serialization(self):
        """
        Test serialization/deserialization for PartitionInformationIndexes
        """

        # Construct dict forms of any model objects needed in order to build this model.

        partition_information_indexes_indexes_model = {} # PartitionInformationIndexesIndexes
        partition_information_indexes_indexes_model['search'] = 0
        partition_information_indexes_indexes_model['view'] = 0

        # Construct a json representation of a PartitionInformationIndexes model
        partition_information_indexes_model_json = {}
        partition_information_indexes_model_json['count'] = 0
        partition_information_indexes_model_json['indexes'] = partition_information_indexes_indexes_model
        partition_information_indexes_model_json['limit'] = 0

        # Construct a model instance of PartitionInformationIndexes by calling from_dict on the json representation
        partition_information_indexes_model = PartitionInformationIndexes.from_dict(partition_information_indexes_model_json)
        assert partition_information_indexes_model != False

        # Construct a model instance of PartitionInformationIndexes by calling from_dict on the json representation
        partition_information_indexes_model_dict = PartitionInformationIndexes.from_dict(partition_information_indexes_model_json).__dict__
        partition_information_indexes_model2 = PartitionInformationIndexes(**partition_information_indexes_model_dict)

        # Verify the model instances are equivalent
        assert partition_information_indexes_model == partition_information_indexes_model2

        # Convert model instance back to dict and verify no loss of data
        partition_information_indexes_model_json2 = partition_information_indexes_model.to_dict()
        assert partition_information_indexes_model_json2 == partition_information_indexes_model_json

class TestPartitionInformationIndexesIndexes():
    """
    Test Class for PartitionInformationIndexesIndexes
    """

    def test_partition_information_indexes_indexes_serialization(self):
        """
        Test serialization/deserialization for PartitionInformationIndexesIndexes
        """

        # Construct a json representation of a PartitionInformationIndexesIndexes model
        partition_information_indexes_indexes_model_json = {}
        partition_information_indexes_indexes_model_json['search'] = 0
        partition_information_indexes_indexes_model_json['view'] = 0

        # Construct a model instance of PartitionInformationIndexesIndexes by calling from_dict on the json representation
        partition_information_indexes_indexes_model = PartitionInformationIndexesIndexes.from_dict(partition_information_indexes_indexes_model_json)
        assert partition_information_indexes_indexes_model != False

        # Construct a model instance of PartitionInformationIndexesIndexes by calling from_dict on the json representation
        partition_information_indexes_indexes_model_dict = PartitionInformationIndexesIndexes.from_dict(partition_information_indexes_indexes_model_json).__dict__
        partition_information_indexes_indexes_model2 = PartitionInformationIndexesIndexes(**partition_information_indexes_indexes_model_dict)

        # Verify the model instances are equivalent
        assert partition_information_indexes_indexes_model == partition_information_indexes_indexes_model2

        # Convert model instance back to dict and verify no loss of data
        partition_information_indexes_indexes_model_json2 = partition_information_indexes_indexes_model.to_dict()
        assert partition_information_indexes_indexes_model_json2 == partition_information_indexes_indexes_model_json

class TestPartitionInformationSizes():
    """
    Test Class for PartitionInformationSizes
    """

    def test_partition_information_sizes_serialization(self):
        """
        Test serialization/deserialization for PartitionInformationSizes
        """

        # Construct a json representation of a PartitionInformationSizes model
        partition_information_sizes_model_json = {}
        partition_information_sizes_model_json['active'] = 0
        partition_information_sizes_model_json['external'] = 0

        # Construct a model instance of PartitionInformationSizes by calling from_dict on the json representation
        partition_information_sizes_model = PartitionInformationSizes.from_dict(partition_information_sizes_model_json)
        assert partition_information_sizes_model != False

        # Construct a model instance of PartitionInformationSizes by calling from_dict on the json representation
        partition_information_sizes_model_dict = PartitionInformationSizes.from_dict(partition_information_sizes_model_json).__dict__
        partition_information_sizes_model2 = PartitionInformationSizes(**partition_information_sizes_model_dict)

        # Verify the model instances are equivalent
        assert partition_information_sizes_model == partition_information_sizes_model2

        # Convert model instance back to dict and verify no loss of data
        partition_information_sizes_model_json2 = partition_information_sizes_model.to_dict()
        assert partition_information_sizes_model_json2 == partition_information_sizes_model_json

class TestReplicationCreateTargetParameters():
    """
    Test Class for ReplicationCreateTargetParameters
    """

    def test_replication_create_target_parameters_serialization(self):
        """
        Test serialization/deserialization for ReplicationCreateTargetParameters
        """

        # Construct a json representation of a ReplicationCreateTargetParameters model
        replication_create_target_parameters_model_json = {}
        replication_create_target_parameters_model_json['n'] = 1
        replication_create_target_parameters_model_json['partitioned'] = True
        replication_create_target_parameters_model_json['q'] = 1

        # Construct a model instance of ReplicationCreateTargetParameters by calling from_dict on the json representation
        replication_create_target_parameters_model = ReplicationCreateTargetParameters.from_dict(replication_create_target_parameters_model_json)
        assert replication_create_target_parameters_model != False

        # Construct a model instance of ReplicationCreateTargetParameters by calling from_dict on the json representation
        replication_create_target_parameters_model_dict = ReplicationCreateTargetParameters.from_dict(replication_create_target_parameters_model_json).__dict__
        replication_create_target_parameters_model2 = ReplicationCreateTargetParameters(**replication_create_target_parameters_model_dict)

        # Verify the model instances are equivalent
        assert replication_create_target_parameters_model == replication_create_target_parameters_model2

        # Convert model instance back to dict and verify no loss of data
        replication_create_target_parameters_model_json2 = replication_create_target_parameters_model.to_dict()
        assert replication_create_target_parameters_model_json2 == replication_create_target_parameters_model_json

class TestReplicationDatabase():
    """
    Test Class for ReplicationDatabase
    """

    def test_replication_database_serialization(self):
        """
        Test serialization/deserialization for ReplicationDatabase
        """

        # Construct dict forms of any model objects needed in order to build this model.

        replication_database_auth_iam_model = {} # ReplicationDatabaseAuthIam
        replication_database_auth_iam_model['api_key'] = 'testString'

        replication_database_auth_model = {} # ReplicationDatabaseAuth
        replication_database_auth_model['iam'] = replication_database_auth_iam_model

        # Construct a json representation of a ReplicationDatabase model
        replication_database_model_json = {}
        replication_database_model_json['auth'] = replication_database_auth_model
        replication_database_model_json['headers'] = {}
        replication_database_model_json['url'] = 'testString'

        # Construct a model instance of ReplicationDatabase by calling from_dict on the json representation
        replication_database_model = ReplicationDatabase.from_dict(replication_database_model_json)
        assert replication_database_model != False

        # Construct a model instance of ReplicationDatabase by calling from_dict on the json representation
        replication_database_model_dict = ReplicationDatabase.from_dict(replication_database_model_json).__dict__
        replication_database_model2 = ReplicationDatabase(**replication_database_model_dict)

        # Verify the model instances are equivalent
        assert replication_database_model == replication_database_model2

        # Convert model instance back to dict and verify no loss of data
        replication_database_model_json2 = replication_database_model.to_dict()
        assert replication_database_model_json2 == replication_database_model_json

class TestReplicationDatabaseAuth():
    """
    Test Class for ReplicationDatabaseAuth
    """

    def test_replication_database_auth_serialization(self):
        """
        Test serialization/deserialization for ReplicationDatabaseAuth
        """

        # Construct dict forms of any model objects needed in order to build this model.

        replication_database_auth_iam_model = {} # ReplicationDatabaseAuthIam
        replication_database_auth_iam_model['api_key'] = 'testString'

        # Construct a json representation of a ReplicationDatabaseAuth model
        replication_database_auth_model_json = {}
        replication_database_auth_model_json['iam'] = replication_database_auth_iam_model

        # Construct a model instance of ReplicationDatabaseAuth by calling from_dict on the json representation
        replication_database_auth_model = ReplicationDatabaseAuth.from_dict(replication_database_auth_model_json)
        assert replication_database_auth_model != False

        # Construct a model instance of ReplicationDatabaseAuth by calling from_dict on the json representation
        replication_database_auth_model_dict = ReplicationDatabaseAuth.from_dict(replication_database_auth_model_json).__dict__
        replication_database_auth_model2 = ReplicationDatabaseAuth(**replication_database_auth_model_dict)

        # Verify the model instances are equivalent
        assert replication_database_auth_model == replication_database_auth_model2

        # Convert model instance back to dict and verify no loss of data
        replication_database_auth_model_json2 = replication_database_auth_model.to_dict()
        assert replication_database_auth_model_json2 == replication_database_auth_model_json

class TestReplicationDatabaseAuthIam():
    """
    Test Class for ReplicationDatabaseAuthIam
    """

    def test_replication_database_auth_iam_serialization(self):
        """
        Test serialization/deserialization for ReplicationDatabaseAuthIam
        """

        # Construct a json representation of a ReplicationDatabaseAuthIam model
        replication_database_auth_iam_model_json = {}
        replication_database_auth_iam_model_json['api_key'] = 'testString'

        # Construct a model instance of ReplicationDatabaseAuthIam by calling from_dict on the json representation
        replication_database_auth_iam_model = ReplicationDatabaseAuthIam.from_dict(replication_database_auth_iam_model_json)
        assert replication_database_auth_iam_model != False

        # Construct a model instance of ReplicationDatabaseAuthIam by calling from_dict on the json representation
        replication_database_auth_iam_model_dict = ReplicationDatabaseAuthIam.from_dict(replication_database_auth_iam_model_json).__dict__
        replication_database_auth_iam_model2 = ReplicationDatabaseAuthIam(**replication_database_auth_iam_model_dict)

        # Verify the model instances are equivalent
        assert replication_database_auth_iam_model == replication_database_auth_iam_model2

        # Convert model instance back to dict and verify no loss of data
        replication_database_auth_iam_model_json2 = replication_database_auth_iam_model.to_dict()
        assert replication_database_auth_iam_model_json2 == replication_database_auth_iam_model_json

class TestReplicationDocument():
    """
    Test Class for ReplicationDocument
    """

    def test_replication_document_serialization(self):
        """
        Test serialization/deserialization for ReplicationDocument
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        replication_create_target_parameters_model = {} # ReplicationCreateTargetParameters
        replication_create_target_parameters_model['n'] = 1
        replication_create_target_parameters_model['partitioned'] = True
        replication_create_target_parameters_model['q'] = 1

        replication_database_auth_iam_model = {} # ReplicationDatabaseAuthIam
        replication_database_auth_iam_model['api_key'] = 'testString'

        replication_database_auth_model = {} # ReplicationDatabaseAuth
        replication_database_auth_model['iam'] = replication_database_auth_iam_model

        replication_database_model = {} # ReplicationDatabase
        replication_database_model['auth'] = replication_database_auth_model
        replication_database_model['headers'] = {}
        replication_database_model['url'] = 'testString'

        user_context_model = {} # UserContext
        user_context_model['db'] = 'testString'
        user_context_model['name'] = 'testString'
        user_context_model['roles'] = ['_reader']

        # Construct a json representation of a ReplicationDocument model
        replication_document_model_json = {}
        replication_document_model_json['_attachments'] = {}
        replication_document_model_json['_conflicts'] = ['testString']
        replication_document_model_json['_deleted'] = True
        replication_document_model_json['_deleted_conflicts'] = ['testString']
        replication_document_model_json['_id'] = 'testString'
        replication_document_model_json['_local_seq'] = 'testString'
        replication_document_model_json['_rev'] = 'testString'
        replication_document_model_json['_revisions'] = revisions_model
        replication_document_model_json['_revs_info'] = [document_revision_status_model]
        replication_document_model_json['cancel'] = True
        replication_document_model_json['checkpoint_interval'] = 0
        replication_document_model_json['connection_timeout'] = 0
        replication_document_model_json['continuous'] = True
        replication_document_model_json['create_target'] = True
        replication_document_model_json['create_target_params'] = replication_create_target_parameters_model
        replication_document_model_json['doc_ids'] = ['testString']
        replication_document_model_json['filter'] = 'testString'
        replication_document_model_json['http_connections'] = 1
        replication_document_model_json['query_params'] = {}
        replication_document_model_json['retries_per_request'] = 0
        replication_document_model_json['selector'] = {}
        replication_document_model_json['since_seq'] = 'testString'
        replication_document_model_json['socket_options'] = 'testString'
        replication_document_model_json['source'] = replication_database_model
        replication_document_model_json['source_proxy'] = 'testString'
        replication_document_model_json['target'] = replication_database_model
        replication_document_model_json['target_proxy'] = 'testString'
        replication_document_model_json['use_checkpoints'] = True
        replication_document_model_json['user_ctx'] = user_context_model
        replication_document_model_json['worker_batch_size'] = 1
        replication_document_model_json['worker_processes'] = 1
        replication_document_model_json['foo'] = { 'foo': 'bar' }

        # Construct a model instance of ReplicationDocument by calling from_dict on the json representation
        replication_document_model = ReplicationDocument.from_dict(replication_document_model_json)
        assert replication_document_model != False

        # Construct a model instance of ReplicationDocument by calling from_dict on the json representation
        replication_document_model_dict = ReplicationDocument.from_dict(replication_document_model_json).__dict__
        replication_document_model2 = ReplicationDocument(**replication_document_model_dict)

        # Verify the model instances are equivalent
        assert replication_document_model == replication_document_model2

        # Convert model instance back to dict and verify no loss of data
        replication_document_model_json2 = replication_document_model.to_dict()
        assert replication_document_model_json2 == replication_document_model_json

class TestReplicationHistory():
    """
    Test Class for ReplicationHistory
    """

    def test_replication_history_serialization(self):
        """
        Test serialization/deserialization for ReplicationHistory
        """

        # Construct a json representation of a ReplicationHistory model
        replication_history_model_json = {}
        replication_history_model_json['doc_write_failures'] = 0
        replication_history_model_json['docs_read'] = 0
        replication_history_model_json['docs_written'] = 0
        replication_history_model_json['end_last_seq'] = 'testString'
        replication_history_model_json['end_time'] = 'testString'
        replication_history_model_json['missing_checked'] = 0
        replication_history_model_json['missing_found'] = 0
        replication_history_model_json['recorded_seq'] = 'testString'
        replication_history_model_json['session_id'] = 'testString'
        replication_history_model_json['start_last_seq'] = 'testString'
        replication_history_model_json['start_time'] = 'testString'

        # Construct a model instance of ReplicationHistory by calling from_dict on the json representation
        replication_history_model = ReplicationHistory.from_dict(replication_history_model_json)
        assert replication_history_model != False

        # Construct a model instance of ReplicationHistory by calling from_dict on the json representation
        replication_history_model_dict = ReplicationHistory.from_dict(replication_history_model_json).__dict__
        replication_history_model2 = ReplicationHistory(**replication_history_model_dict)

        # Verify the model instances are equivalent
        assert replication_history_model == replication_history_model2

        # Convert model instance back to dict and verify no loss of data
        replication_history_model_json2 = replication_history_model.to_dict()
        assert replication_history_model_json2 == replication_history_model_json

class TestReplicationResult():
    """
    Test Class for ReplicationResult
    """

    def test_replication_result_serialization(self):
        """
        Test serialization/deserialization for ReplicationResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        replication_history_model = {} # ReplicationHistory
        replication_history_model['doc_write_failures'] = 0
        replication_history_model['docs_read'] = 0
        replication_history_model['docs_written'] = 0
        replication_history_model['end_last_seq'] = 'testString'
        replication_history_model['end_time'] = 'testString'
        replication_history_model['missing_checked'] = 0
        replication_history_model['missing_found'] = 0
        replication_history_model['recorded_seq'] = 'testString'
        replication_history_model['session_id'] = 'testString'
        replication_history_model['start_last_seq'] = 'testString'
        replication_history_model['start_time'] = 'testString'

        # Construct a json representation of a ReplicationResult model
        replication_result_model_json = {}
        replication_result_model_json['history'] = [replication_history_model]
        replication_result_model_json['ok'] = True
        replication_result_model_json['replication_id_version'] = 0
        replication_result_model_json['session_id'] = 'testString'
        replication_result_model_json['source_last_seq'] = 'testString'

        # Construct a model instance of ReplicationResult by calling from_dict on the json representation
        replication_result_model = ReplicationResult.from_dict(replication_result_model_json)
        assert replication_result_model != False

        # Construct a model instance of ReplicationResult by calling from_dict on the json representation
        replication_result_model_dict = ReplicationResult.from_dict(replication_result_model_json).__dict__
        replication_result_model2 = ReplicationResult(**replication_result_model_dict)

        # Verify the model instances are equivalent
        assert replication_result_model == replication_result_model2

        # Convert model instance back to dict and verify no loss of data
        replication_result_model_json2 = replication_result_model.to_dict()
        assert replication_result_model_json2 == replication_result_model_json

class TestRevisions():
    """
    Test Class for Revisions
    """

    def test_revisions_serialization(self):
        """
        Test serialization/deserialization for Revisions
        """

        # Construct a json representation of a Revisions model
        revisions_model_json = {}
        revisions_model_json['ids'] = ['testString']
        revisions_model_json['start'] = 1

        # Construct a model instance of Revisions by calling from_dict on the json representation
        revisions_model = Revisions.from_dict(revisions_model_json)
        assert revisions_model != False

        # Construct a model instance of Revisions by calling from_dict on the json representation
        revisions_model_dict = Revisions.from_dict(revisions_model_json).__dict__
        revisions_model2 = Revisions(**revisions_model_dict)

        # Verify the model instances are equivalent
        assert revisions_model == revisions_model2

        # Convert model instance back to dict and verify no loss of data
        revisions_model_json2 = revisions_model.to_dict()
        assert revisions_model_json2 == revisions_model_json

class TestRevsDiff():
    """
    Test Class for RevsDiff
    """

    def test_revs_diff_serialization(self):
        """
        Test serialization/deserialization for RevsDiff
        """

        # Construct a json representation of a RevsDiff model
        revs_diff_model_json = {}
        revs_diff_model_json['missing'] = ['testString']
        revs_diff_model_json['possible_ancestors'] = ['testString']

        # Construct a model instance of RevsDiff by calling from_dict on the json representation
        revs_diff_model = RevsDiff.from_dict(revs_diff_model_json)
        assert revs_diff_model != False

        # Construct a model instance of RevsDiff by calling from_dict on the json representation
        revs_diff_model_dict = RevsDiff.from_dict(revs_diff_model_json).__dict__
        revs_diff_model2 = RevsDiff(**revs_diff_model_dict)

        # Verify the model instances are equivalent
        assert revs_diff_model == revs_diff_model2

        # Convert model instance back to dict and verify no loss of data
        revs_diff_model_json2 = revs_diff_model.to_dict()
        assert revs_diff_model_json2 == revs_diff_model_json

class TestSchedulerDocsResult():
    """
    Test Class for SchedulerDocsResult
    """

    def test_scheduler_docs_result_serialization(self):
        """
        Test serialization/deserialization for SchedulerDocsResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scheduler_info_model = {} # SchedulerInfo
        scheduler_info_model['changes_pending'] = 0
        scheduler_info_model['checkpointed_source_seq'] = 'testString'
        scheduler_info_model['doc_write_failures'] = 0
        scheduler_info_model['docs_read'] = 0
        scheduler_info_model['docs_written'] = 0
        scheduler_info_model['error'] = 'testString'
        scheduler_info_model['missing_revisions_found'] = 0
        scheduler_info_model['revisions_checked'] = 0
        scheduler_info_model['source_seq'] = 'testString'
        scheduler_info_model['through_seq'] = 'testString'

        scheduler_document_model = {} # SchedulerDocument
        scheduler_document_model['database'] = 'testString'
        scheduler_document_model['doc_id'] = 'testString'
        scheduler_document_model['error_count'] = 0
        scheduler_document_model['id'] = 'testString'
        scheduler_document_model['info'] = scheduler_info_model
        scheduler_document_model['last_updated'] = '2020-01-28T18:40:40.123456Z'
        scheduler_document_model['node'] = 'testString'
        scheduler_document_model['source'] = 'testString'
        scheduler_document_model['source_proxy'] = 'testString'
        scheduler_document_model['start_time'] = '2020-01-28T18:40:40.123456Z'
        scheduler_document_model['state'] = 'initializing'
        scheduler_document_model['target'] = 'testString'
        scheduler_document_model['target_proxy'] = 'testString'

        # Construct a json representation of a SchedulerDocsResult model
        scheduler_docs_result_model_json = {}
        scheduler_docs_result_model_json['total_rows'] = 0
        scheduler_docs_result_model_json['docs'] = [scheduler_document_model]

        # Construct a model instance of SchedulerDocsResult by calling from_dict on the json representation
        scheduler_docs_result_model = SchedulerDocsResult.from_dict(scheduler_docs_result_model_json)
        assert scheduler_docs_result_model != False

        # Construct a model instance of SchedulerDocsResult by calling from_dict on the json representation
        scheduler_docs_result_model_dict = SchedulerDocsResult.from_dict(scheduler_docs_result_model_json).__dict__
        scheduler_docs_result_model2 = SchedulerDocsResult(**scheduler_docs_result_model_dict)

        # Verify the model instances are equivalent
        assert scheduler_docs_result_model == scheduler_docs_result_model2

        # Convert model instance back to dict and verify no loss of data
        scheduler_docs_result_model_json2 = scheduler_docs_result_model.to_dict()
        assert scheduler_docs_result_model_json2 == scheduler_docs_result_model_json

class TestSchedulerDocument():
    """
    Test Class for SchedulerDocument
    """

    def test_scheduler_document_serialization(self):
        """
        Test serialization/deserialization for SchedulerDocument
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scheduler_info_model = {} # SchedulerInfo
        scheduler_info_model['changes_pending'] = 0
        scheduler_info_model['checkpointed_source_seq'] = 'testString'
        scheduler_info_model['doc_write_failures'] = 0
        scheduler_info_model['docs_read'] = 0
        scheduler_info_model['docs_written'] = 0
        scheduler_info_model['error'] = 'testString'
        scheduler_info_model['missing_revisions_found'] = 0
        scheduler_info_model['revisions_checked'] = 0
        scheduler_info_model['source_seq'] = 'testString'
        scheduler_info_model['through_seq'] = 'testString'

        # Construct a json representation of a SchedulerDocument model
        scheduler_document_model_json = {}
        scheduler_document_model_json['database'] = 'testString'
        scheduler_document_model_json['doc_id'] = 'testString'
        scheduler_document_model_json['error_count'] = 0
        scheduler_document_model_json['id'] = 'testString'
        scheduler_document_model_json['info'] = scheduler_info_model
        scheduler_document_model_json['last_updated'] = '2020-01-28T18:40:40.123456Z'
        scheduler_document_model_json['node'] = 'testString'
        scheduler_document_model_json['source'] = 'testString'
        scheduler_document_model_json['source_proxy'] = 'testString'
        scheduler_document_model_json['start_time'] = '2020-01-28T18:40:40.123456Z'
        scheduler_document_model_json['state'] = 'initializing'
        scheduler_document_model_json['target'] = 'testString'
        scheduler_document_model_json['target_proxy'] = 'testString'

        # Construct a model instance of SchedulerDocument by calling from_dict on the json representation
        scheduler_document_model = SchedulerDocument.from_dict(scheduler_document_model_json)
        assert scheduler_document_model != False

        # Construct a model instance of SchedulerDocument by calling from_dict on the json representation
        scheduler_document_model_dict = SchedulerDocument.from_dict(scheduler_document_model_json).__dict__
        scheduler_document_model2 = SchedulerDocument(**scheduler_document_model_dict)

        # Verify the model instances are equivalent
        assert scheduler_document_model == scheduler_document_model2

        # Convert model instance back to dict and verify no loss of data
        scheduler_document_model_json2 = scheduler_document_model.to_dict()
        assert scheduler_document_model_json2 == scheduler_document_model_json

class TestSchedulerInfo():
    """
    Test Class for SchedulerInfo
    """

    def test_scheduler_info_serialization(self):
        """
        Test serialization/deserialization for SchedulerInfo
        """

        # Construct a json representation of a SchedulerInfo model
        scheduler_info_model_json = {}
        scheduler_info_model_json['changes_pending'] = 0
        scheduler_info_model_json['checkpointed_source_seq'] = 'testString'
        scheduler_info_model_json['doc_write_failures'] = 0
        scheduler_info_model_json['docs_read'] = 0
        scheduler_info_model_json['docs_written'] = 0
        scheduler_info_model_json['error'] = 'testString'
        scheduler_info_model_json['missing_revisions_found'] = 0
        scheduler_info_model_json['revisions_checked'] = 0
        scheduler_info_model_json['source_seq'] = 'testString'
        scheduler_info_model_json['through_seq'] = 'testString'

        # Construct a model instance of SchedulerInfo by calling from_dict on the json representation
        scheduler_info_model = SchedulerInfo.from_dict(scheduler_info_model_json)
        assert scheduler_info_model != False

        # Construct a model instance of SchedulerInfo by calling from_dict on the json representation
        scheduler_info_model_dict = SchedulerInfo.from_dict(scheduler_info_model_json).__dict__
        scheduler_info_model2 = SchedulerInfo(**scheduler_info_model_dict)

        # Verify the model instances are equivalent
        assert scheduler_info_model == scheduler_info_model2

        # Convert model instance back to dict and verify no loss of data
        scheduler_info_model_json2 = scheduler_info_model.to_dict()
        assert scheduler_info_model_json2 == scheduler_info_model_json

class TestSchedulerJob():
    """
    Test Class for SchedulerJob
    """

    def test_scheduler_job_serialization(self):
        """
        Test serialization/deserialization for SchedulerJob
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scheduler_job_event_model = {} # SchedulerJobEvent
        scheduler_job_event_model['timestamp'] = '2020-01-28T18:40:40.123456Z'
        scheduler_job_event_model['type'] = 'testString'

        scheduler_info_model = {} # SchedulerInfo
        scheduler_info_model['changes_pending'] = 0
        scheduler_info_model['checkpointed_source_seq'] = 'testString'
        scheduler_info_model['doc_write_failures'] = 0
        scheduler_info_model['docs_read'] = 0
        scheduler_info_model['docs_written'] = 0
        scheduler_info_model['error'] = 'testString'
        scheduler_info_model['missing_revisions_found'] = 0
        scheduler_info_model['revisions_checked'] = 0
        scheduler_info_model['source_seq'] = 'testString'
        scheduler_info_model['through_seq'] = 'testString'

        # Construct a json representation of a SchedulerJob model
        scheduler_job_model_json = {}
        scheduler_job_model_json['database'] = 'testString'
        scheduler_job_model_json['doc_id'] = 'testString'
        scheduler_job_model_json['history'] = [scheduler_job_event_model]
        scheduler_job_model_json['id'] = 'testString'
        scheduler_job_model_json['info'] = scheduler_info_model
        scheduler_job_model_json['node'] = 'testString'
        scheduler_job_model_json['pid'] = 'testString'
        scheduler_job_model_json['source'] = 'testString'
        scheduler_job_model_json['start_time'] = '2020-01-28T18:40:40.123456Z'
        scheduler_job_model_json['target'] = 'testString'
        scheduler_job_model_json['user'] = 'testString'

        # Construct a model instance of SchedulerJob by calling from_dict on the json representation
        scheduler_job_model = SchedulerJob.from_dict(scheduler_job_model_json)
        assert scheduler_job_model != False

        # Construct a model instance of SchedulerJob by calling from_dict on the json representation
        scheduler_job_model_dict = SchedulerJob.from_dict(scheduler_job_model_json).__dict__
        scheduler_job_model2 = SchedulerJob(**scheduler_job_model_dict)

        # Verify the model instances are equivalent
        assert scheduler_job_model == scheduler_job_model2

        # Convert model instance back to dict and verify no loss of data
        scheduler_job_model_json2 = scheduler_job_model.to_dict()
        assert scheduler_job_model_json2 == scheduler_job_model_json

class TestSchedulerJobEvent():
    """
    Test Class for SchedulerJobEvent
    """

    def test_scheduler_job_event_serialization(self):
        """
        Test serialization/deserialization for SchedulerJobEvent
        """

        # Construct a json representation of a SchedulerJobEvent model
        scheduler_job_event_model_json = {}
        scheduler_job_event_model_json['timestamp'] = '2020-01-28T18:40:40.123456Z'
        scheduler_job_event_model_json['type'] = 'testString'

        # Construct a model instance of SchedulerJobEvent by calling from_dict on the json representation
        scheduler_job_event_model = SchedulerJobEvent.from_dict(scheduler_job_event_model_json)
        assert scheduler_job_event_model != False

        # Construct a model instance of SchedulerJobEvent by calling from_dict on the json representation
        scheduler_job_event_model_dict = SchedulerJobEvent.from_dict(scheduler_job_event_model_json).__dict__
        scheduler_job_event_model2 = SchedulerJobEvent(**scheduler_job_event_model_dict)

        # Verify the model instances are equivalent
        assert scheduler_job_event_model == scheduler_job_event_model2

        # Convert model instance back to dict and verify no loss of data
        scheduler_job_event_model_json2 = scheduler_job_event_model.to_dict()
        assert scheduler_job_event_model_json2 == scheduler_job_event_model_json

class TestSchedulerJobsResult():
    """
    Test Class for SchedulerJobsResult
    """

    def test_scheduler_jobs_result_serialization(self):
        """
        Test serialization/deserialization for SchedulerJobsResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scheduler_job_event_model = {} # SchedulerJobEvent
        scheduler_job_event_model['timestamp'] = '2020-01-28T18:40:40.123456Z'
        scheduler_job_event_model['type'] = 'testString'

        scheduler_info_model = {} # SchedulerInfo
        scheduler_info_model['changes_pending'] = 0
        scheduler_info_model['checkpointed_source_seq'] = 'testString'
        scheduler_info_model['doc_write_failures'] = 0
        scheduler_info_model['docs_read'] = 0
        scheduler_info_model['docs_written'] = 0
        scheduler_info_model['error'] = 'testString'
        scheduler_info_model['missing_revisions_found'] = 0
        scheduler_info_model['revisions_checked'] = 0
        scheduler_info_model['source_seq'] = 'testString'
        scheduler_info_model['through_seq'] = 'testString'

        scheduler_job_model = {} # SchedulerJob
        scheduler_job_model['database'] = 'testString'
        scheduler_job_model['doc_id'] = 'testString'
        scheduler_job_model['history'] = [scheduler_job_event_model]
        scheduler_job_model['id'] = 'testString'
        scheduler_job_model['info'] = scheduler_info_model
        scheduler_job_model['node'] = 'testString'
        scheduler_job_model['pid'] = 'testString'
        scheduler_job_model['source'] = 'testString'
        scheduler_job_model['start_time'] = '2020-01-28T18:40:40.123456Z'
        scheduler_job_model['target'] = 'testString'
        scheduler_job_model['user'] = 'testString'

        # Construct a json representation of a SchedulerJobsResult model
        scheduler_jobs_result_model_json = {}
        scheduler_jobs_result_model_json['total_rows'] = 0
        scheduler_jobs_result_model_json['jobs'] = [scheduler_job_model]

        # Construct a model instance of SchedulerJobsResult by calling from_dict on the json representation
        scheduler_jobs_result_model = SchedulerJobsResult.from_dict(scheduler_jobs_result_model_json)
        assert scheduler_jobs_result_model != False

        # Construct a model instance of SchedulerJobsResult by calling from_dict on the json representation
        scheduler_jobs_result_model_dict = SchedulerJobsResult.from_dict(scheduler_jobs_result_model_json).__dict__
        scheduler_jobs_result_model2 = SchedulerJobsResult(**scheduler_jobs_result_model_dict)

        # Verify the model instances are equivalent
        assert scheduler_jobs_result_model == scheduler_jobs_result_model2

        # Convert model instance back to dict and verify no loss of data
        scheduler_jobs_result_model_json2 = scheduler_jobs_result_model.to_dict()
        assert scheduler_jobs_result_model_json2 == scheduler_jobs_result_model_json

class TestSearchAnalyzeResult():
    """
    Test Class for SearchAnalyzeResult
    """

    def test_search_analyze_result_serialization(self):
        """
        Test serialization/deserialization for SearchAnalyzeResult
        """

        # Construct a json representation of a SearchAnalyzeResult model
        search_analyze_result_model_json = {}
        search_analyze_result_model_json['tokens'] = ['testString']

        # Construct a model instance of SearchAnalyzeResult by calling from_dict on the json representation
        search_analyze_result_model = SearchAnalyzeResult.from_dict(search_analyze_result_model_json)
        assert search_analyze_result_model != False

        # Construct a model instance of SearchAnalyzeResult by calling from_dict on the json representation
        search_analyze_result_model_dict = SearchAnalyzeResult.from_dict(search_analyze_result_model_json).__dict__
        search_analyze_result_model2 = SearchAnalyzeResult(**search_analyze_result_model_dict)

        # Verify the model instances are equivalent
        assert search_analyze_result_model == search_analyze_result_model2

        # Convert model instance back to dict and verify no loss of data
        search_analyze_result_model_json2 = search_analyze_result_model.to_dict()
        assert search_analyze_result_model_json2 == search_analyze_result_model_json

class TestSearchIndexDefinition():
    """
    Test Class for SearchIndexDefinition
    """

    def test_search_index_definition_serialization(self):
        """
        Test serialization/deserialization for SearchIndexDefinition
        """

        # Construct dict forms of any model objects needed in order to build this model.

        analyzer_model = {} # Analyzer
        analyzer_model['name'] = 'classic'
        analyzer_model['stopwords'] = ['testString']

        analyzer_configuration_model = {} # AnalyzerConfiguration
        analyzer_configuration_model['name'] = 'classic'
        analyzer_configuration_model['stopwords'] = ['testString']
        analyzer_configuration_model['fields'] = {}

        # Construct a json representation of a SearchIndexDefinition model
        search_index_definition_model_json = {}
        search_index_definition_model_json['analyzer'] = analyzer_configuration_model
        search_index_definition_model_json['index'] = 'testString'

        # Construct a model instance of SearchIndexDefinition by calling from_dict on the json representation
        search_index_definition_model = SearchIndexDefinition.from_dict(search_index_definition_model_json)
        assert search_index_definition_model != False

        # Construct a model instance of SearchIndexDefinition by calling from_dict on the json representation
        search_index_definition_model_dict = SearchIndexDefinition.from_dict(search_index_definition_model_json).__dict__
        search_index_definition_model2 = SearchIndexDefinition(**search_index_definition_model_dict)

        # Verify the model instances are equivalent
        assert search_index_definition_model == search_index_definition_model2

        # Convert model instance back to dict and verify no loss of data
        search_index_definition_model_json2 = search_index_definition_model.to_dict()
        assert search_index_definition_model_json2 == search_index_definition_model_json

class TestSearchIndexInfo():
    """
    Test Class for SearchIndexInfo
    """

    def test_search_index_info_serialization(self):
        """
        Test serialization/deserialization for SearchIndexInfo
        """

        # Construct a json representation of a SearchIndexInfo model
        search_index_info_model_json = {}
        search_index_info_model_json['committed_seq'] = 26
        search_index_info_model_json['disk_size'] = 0
        search_index_info_model_json['doc_count'] = 0
        search_index_info_model_json['doc_del_count'] = 0
        search_index_info_model_json['pending_seq'] = 26

        # Construct a model instance of SearchIndexInfo by calling from_dict on the json representation
        search_index_info_model = SearchIndexInfo.from_dict(search_index_info_model_json)
        assert search_index_info_model != False

        # Construct a model instance of SearchIndexInfo by calling from_dict on the json representation
        search_index_info_model_dict = SearchIndexInfo.from_dict(search_index_info_model_json).__dict__
        search_index_info_model2 = SearchIndexInfo(**search_index_info_model_dict)

        # Verify the model instances are equivalent
        assert search_index_info_model == search_index_info_model2

        # Convert model instance back to dict and verify no loss of data
        search_index_info_model_json2 = search_index_info_model.to_dict()
        assert search_index_info_model_json2 == search_index_info_model_json

class TestSearchInfoResult():
    """
    Test Class for SearchInfoResult
    """

    def test_search_info_result_serialization(self):
        """
        Test serialization/deserialization for SearchInfoResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        search_index_info_model = {} # SearchIndexInfo
        search_index_info_model['committed_seq'] = 26
        search_index_info_model['disk_size'] = 0
        search_index_info_model['doc_count'] = 0
        search_index_info_model['doc_del_count'] = 0
        search_index_info_model['pending_seq'] = 26

        # Construct a json representation of a SearchInfoResult model
        search_info_result_model_json = {}
        search_info_result_model_json['name'] = 'testString'
        search_info_result_model_json['search_index'] = search_index_info_model

        # Construct a model instance of SearchInfoResult by calling from_dict on the json representation
        search_info_result_model = SearchInfoResult.from_dict(search_info_result_model_json)
        assert search_info_result_model != False

        # Construct a model instance of SearchInfoResult by calling from_dict on the json representation
        search_info_result_model_dict = SearchInfoResult.from_dict(search_info_result_model_json).__dict__
        search_info_result_model2 = SearchInfoResult(**search_info_result_model_dict)

        # Verify the model instances are equivalent
        assert search_info_result_model == search_info_result_model2

        # Convert model instance back to dict and verify no loss of data
        search_info_result_model_json2 = search_info_result_model.to_dict()
        assert search_info_result_model_json2 == search_info_result_model_json

class TestSearchResult():
    """
    Test Class for SearchResult
    """

    def test_search_result_serialization(self):
        """
        Test serialization/deserialization for SearchResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        search_result_row_model = {} # SearchResultRow
        search_result_row_model['doc'] = document_model
        search_result_row_model['fields'] = {}
        search_result_row_model['highlights'] = {}
        search_result_row_model['id'] = 'testString'

        search_result_properties_model = {} # SearchResultProperties
        search_result_properties_model['total_rows'] = 0
        search_result_properties_model['bookmark'] = 'testString'
        search_result_properties_model['by'] = 'testString'
        search_result_properties_model['counts'] = {}
        search_result_properties_model['ranges'] = {}
        search_result_properties_model['rows'] = [search_result_row_model]

        # Construct a json representation of a SearchResult model
        search_result_model_json = {}
        search_result_model_json['total_rows'] = 0
        search_result_model_json['bookmark'] = 'testString'
        search_result_model_json['by'] = 'testString'
        search_result_model_json['counts'] = {}
        search_result_model_json['ranges'] = {}
        search_result_model_json['rows'] = [search_result_row_model]
        search_result_model_json['groups'] = [search_result_properties_model]

        # Construct a model instance of SearchResult by calling from_dict on the json representation
        search_result_model = SearchResult.from_dict(search_result_model_json)
        assert search_result_model != False

        # Construct a model instance of SearchResult by calling from_dict on the json representation
        search_result_model_dict = SearchResult.from_dict(search_result_model_json).__dict__
        search_result_model2 = SearchResult(**search_result_model_dict)

        # Verify the model instances are equivalent
        assert search_result_model == search_result_model2

        # Convert model instance back to dict and verify no loss of data
        search_result_model_json2 = search_result_model.to_dict()
        assert search_result_model_json2 == search_result_model_json

class TestSearchResultProperties():
    """
    Test Class for SearchResultProperties
    """

    def test_search_result_properties_serialization(self):
        """
        Test serialization/deserialization for SearchResultProperties
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        search_result_row_model = {} # SearchResultRow
        search_result_row_model['doc'] = document_model
        search_result_row_model['fields'] = {}
        search_result_row_model['highlights'] = {}
        search_result_row_model['id'] = 'testString'

        # Construct a json representation of a SearchResultProperties model
        search_result_properties_model_json = {}
        search_result_properties_model_json['total_rows'] = 0
        search_result_properties_model_json['bookmark'] = 'testString'
        search_result_properties_model_json['by'] = 'testString'
        search_result_properties_model_json['counts'] = {}
        search_result_properties_model_json['ranges'] = {}
        search_result_properties_model_json['rows'] = [search_result_row_model]

        # Construct a model instance of SearchResultProperties by calling from_dict on the json representation
        search_result_properties_model = SearchResultProperties.from_dict(search_result_properties_model_json)
        assert search_result_properties_model != False

        # Construct a model instance of SearchResultProperties by calling from_dict on the json representation
        search_result_properties_model_dict = SearchResultProperties.from_dict(search_result_properties_model_json).__dict__
        search_result_properties_model2 = SearchResultProperties(**search_result_properties_model_dict)

        # Verify the model instances are equivalent
        assert search_result_properties_model == search_result_properties_model2

        # Convert model instance back to dict and verify no loss of data
        search_result_properties_model_json2 = search_result_properties_model.to_dict()
        assert search_result_properties_model_json2 == search_result_properties_model_json

class TestSearchResultRow():
    """
    Test Class for SearchResultRow
    """

    def test_search_result_row_serialization(self):
        """
        Test serialization/deserialization for SearchResultRow
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        # Construct a json representation of a SearchResultRow model
        search_result_row_model_json = {}
        search_result_row_model_json['doc'] = document_model
        search_result_row_model_json['fields'] = {}
        search_result_row_model_json['highlights'] = {}
        search_result_row_model_json['id'] = 'testString'

        # Construct a model instance of SearchResultRow by calling from_dict on the json representation
        search_result_row_model = SearchResultRow.from_dict(search_result_row_model_json)
        assert search_result_row_model != False

        # Construct a model instance of SearchResultRow by calling from_dict on the json representation
        search_result_row_model_dict = SearchResultRow.from_dict(search_result_row_model_json).__dict__
        search_result_row_model2 = SearchResultRow(**search_result_row_model_dict)

        # Verify the model instances are equivalent
        assert search_result_row_model == search_result_row_model2

        # Convert model instance back to dict and verify no loss of data
        search_result_row_model_json2 = search_result_row_model.to_dict()
        assert search_result_row_model_json2 == search_result_row_model_json

class TestSecurity():
    """
    Test Class for Security
    """

    def test_security_serialization(self):
        """
        Test serialization/deserialization for Security
        """

        # Construct dict forms of any model objects needed in order to build this model.

        security_object_model = {} # SecurityObject
        security_object_model['names'] = ['testString']
        security_object_model['roles'] = ['testString']

        # Construct a json representation of a Security model
        security_model_json = {}
        security_model_json['admins'] = security_object_model
        security_model_json['members'] = security_object_model
        security_model_json['cloudant'] = {}
        security_model_json['couchdb_auth_only'] = True

        # Construct a model instance of Security by calling from_dict on the json representation
        security_model = Security.from_dict(security_model_json)
        assert security_model != False

        # Construct a model instance of Security by calling from_dict on the json representation
        security_model_dict = Security.from_dict(security_model_json).__dict__
        security_model2 = Security(**security_model_dict)

        # Verify the model instances are equivalent
        assert security_model == security_model2

        # Convert model instance back to dict and verify no loss of data
        security_model_json2 = security_model.to_dict()
        assert security_model_json2 == security_model_json

class TestSecurityObject():
    """
    Test Class for SecurityObject
    """

    def test_security_object_serialization(self):
        """
        Test serialization/deserialization for SecurityObject
        """

        # Construct a json representation of a SecurityObject model
        security_object_model_json = {}
        security_object_model_json['names'] = ['testString']
        security_object_model_json['roles'] = ['testString']

        # Construct a model instance of SecurityObject by calling from_dict on the json representation
        security_object_model = SecurityObject.from_dict(security_object_model_json)
        assert security_object_model != False

        # Construct a model instance of SecurityObject by calling from_dict on the json representation
        security_object_model_dict = SecurityObject.from_dict(security_object_model_json).__dict__
        security_object_model2 = SecurityObject(**security_object_model_dict)

        # Verify the model instances are equivalent
        assert security_object_model == security_object_model2

        # Convert model instance back to dict and verify no loss of data
        security_object_model_json2 = security_object_model.to_dict()
        assert security_object_model_json2 == security_object_model_json

class TestServerInformation():
    """
    Test Class for ServerInformation
    """

    def test_server_information_serialization(self):
        """
        Test serialization/deserialization for ServerInformation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        server_vendor_model = {} # ServerVendor
        server_vendor_model['name'] = 'testString'
        server_vendor_model['variant'] = 'testString'
        server_vendor_model['version'] = 'testString'

        # Construct a json representation of a ServerInformation model
        server_information_model_json = {}
        server_information_model_json['couchdb'] = 'testString'
        server_information_model_json['features'] = ['testString']
        server_information_model_json['vendor'] = server_vendor_model
        server_information_model_json['version'] = 'testString'
        server_information_model_json['features_flags'] = ['testString']

        # Construct a model instance of ServerInformation by calling from_dict on the json representation
        server_information_model = ServerInformation.from_dict(server_information_model_json)
        assert server_information_model != False

        # Construct a model instance of ServerInformation by calling from_dict on the json representation
        server_information_model_dict = ServerInformation.from_dict(server_information_model_json).__dict__
        server_information_model2 = ServerInformation(**server_information_model_dict)

        # Verify the model instances are equivalent
        assert server_information_model == server_information_model2

        # Convert model instance back to dict and verify no loss of data
        server_information_model_json2 = server_information_model.to_dict()
        assert server_information_model_json2 == server_information_model_json

class TestServerVendor():
    """
    Test Class for ServerVendor
    """

    def test_server_vendor_serialization(self):
        """
        Test serialization/deserialization for ServerVendor
        """

        # Construct a json representation of a ServerVendor model
        server_vendor_model_json = {}
        server_vendor_model_json['name'] = 'testString'
        server_vendor_model_json['variant'] = 'testString'
        server_vendor_model_json['version'] = 'testString'

        # Construct a model instance of ServerVendor by calling from_dict on the json representation
        server_vendor_model = ServerVendor.from_dict(server_vendor_model_json)
        assert server_vendor_model != False

        # Construct a model instance of ServerVendor by calling from_dict on the json representation
        server_vendor_model_dict = ServerVendor.from_dict(server_vendor_model_json).__dict__
        server_vendor_model2 = ServerVendor(**server_vendor_model_dict)

        # Verify the model instances are equivalent
        assert server_vendor_model == server_vendor_model2

        # Convert model instance back to dict and verify no loss of data
        server_vendor_model_json2 = server_vendor_model.to_dict()
        assert server_vendor_model_json2 == server_vendor_model_json

class TestSessionAuthentication():
    """
    Test Class for SessionAuthentication
    """

    def test_session_authentication_serialization(self):
        """
        Test serialization/deserialization for SessionAuthentication
        """

        # Construct a json representation of a SessionAuthentication model
        session_authentication_model_json = {}
        session_authentication_model_json['authenticated'] = 'testString'
        session_authentication_model_json['authentication_db'] = 'testString'
        session_authentication_model_json['authentication_handlers'] = ['testString']

        # Construct a model instance of SessionAuthentication by calling from_dict on the json representation
        session_authentication_model = SessionAuthentication.from_dict(session_authentication_model_json)
        assert session_authentication_model != False

        # Construct a model instance of SessionAuthentication by calling from_dict on the json representation
        session_authentication_model_dict = SessionAuthentication.from_dict(session_authentication_model_json).__dict__
        session_authentication_model2 = SessionAuthentication(**session_authentication_model_dict)

        # Verify the model instances are equivalent
        assert session_authentication_model == session_authentication_model2

        # Convert model instance back to dict and verify no loss of data
        session_authentication_model_json2 = session_authentication_model.to_dict()
        assert session_authentication_model_json2 == session_authentication_model_json

class TestSessionInformation():
    """
    Test Class for SessionInformation
    """

    def test_session_information_serialization(self):
        """
        Test serialization/deserialization for SessionInformation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        session_authentication_model = {} # SessionAuthentication
        session_authentication_model['authenticated'] = 'testString'
        session_authentication_model['authentication_db'] = 'testString'
        session_authentication_model['authentication_handlers'] = ['testString']

        user_context_model = {} # UserContext
        user_context_model['db'] = 'testString'
        user_context_model['name'] = 'testString'
        user_context_model['roles'] = ['_reader']

        # Construct a json representation of a SessionInformation model
        session_information_model_json = {}
        session_information_model_json['ok'] = True
        session_information_model_json['info'] = session_authentication_model
        session_information_model_json['userCtx'] = user_context_model

        # Construct a model instance of SessionInformation by calling from_dict on the json representation
        session_information_model = SessionInformation.from_dict(session_information_model_json)
        assert session_information_model != False

        # Construct a model instance of SessionInformation by calling from_dict on the json representation
        session_information_model_dict = SessionInformation.from_dict(session_information_model_json).__dict__
        session_information_model2 = SessionInformation(**session_information_model_dict)

        # Verify the model instances are equivalent
        assert session_information_model == session_information_model2

        # Convert model instance back to dict and verify no loss of data
        session_information_model_json2 = session_information_model.to_dict()
        assert session_information_model_json2 == session_information_model_json

class TestShardsInformation():
    """
    Test Class for ShardsInformation
    """

    def test_shards_information_serialization(self):
        """
        Test serialization/deserialization for ShardsInformation
        """

        # Construct a json representation of a ShardsInformation model
        shards_information_model_json = {}
        shards_information_model_json['shards'] = {}

        # Construct a model instance of ShardsInformation by calling from_dict on the json representation
        shards_information_model = ShardsInformation.from_dict(shards_information_model_json)
        assert shards_information_model != False

        # Construct a model instance of ShardsInformation by calling from_dict on the json representation
        shards_information_model_dict = ShardsInformation.from_dict(shards_information_model_json).__dict__
        shards_information_model2 = ShardsInformation(**shards_information_model_dict)

        # Verify the model instances are equivalent
        assert shards_information_model == shards_information_model2

        # Convert model instance back to dict and verify no loss of data
        shards_information_model_json2 = shards_information_model.to_dict()
        assert shards_information_model_json2 == shards_information_model_json

class TestThroughputInformation():
    """
    Test Class for ThroughputInformation
    """

    def test_throughput_information_serialization(self):
        """
        Test serialization/deserialization for ThroughputInformation
        """

        # Construct a json representation of a ThroughputInformation model
        throughput_information_model_json = {}
        throughput_information_model_json['blocks'] = 0
        throughput_information_model_json['query'] = 0
        throughput_information_model_json['read'] = 0
        throughput_information_model_json['write'] = 0

        # Construct a model instance of ThroughputInformation by calling from_dict on the json representation
        throughput_information_model = ThroughputInformation.from_dict(throughput_information_model_json)
        assert throughput_information_model != False

        # Construct a model instance of ThroughputInformation by calling from_dict on the json representation
        throughput_information_model_dict = ThroughputInformation.from_dict(throughput_information_model_json).__dict__
        throughput_information_model2 = ThroughputInformation(**throughput_information_model_dict)

        # Verify the model instances are equivalent
        assert throughput_information_model == throughput_information_model2

        # Convert model instance back to dict and verify no loss of data
        throughput_information_model_json2 = throughput_information_model.to_dict()
        assert throughput_information_model_json2 == throughput_information_model_json

class TestUpInformation():
    """
    Test Class for UpInformation
    """

    def test_up_information_serialization(self):
        """
        Test serialization/deserialization for UpInformation
        """

        # Construct a json representation of a UpInformation model
        up_information_model_json = {}
        up_information_model_json['seeds'] = { 'foo': 'bar' }
        up_information_model_json['status'] = 'maintenance_mode'

        # Construct a model instance of UpInformation by calling from_dict on the json representation
        up_information_model = UpInformation.from_dict(up_information_model_json)
        assert up_information_model != False

        # Construct a model instance of UpInformation by calling from_dict on the json representation
        up_information_model_dict = UpInformation.from_dict(up_information_model_json).__dict__
        up_information_model2 = UpInformation(**up_information_model_dict)

        # Verify the model instances are equivalent
        assert up_information_model == up_information_model2

        # Convert model instance back to dict and verify no loss of data
        up_information_model_json2 = up_information_model.to_dict()
        assert up_information_model_json2 == up_information_model_json

class TestUserContext():
    """
    Test Class for UserContext
    """

    def test_user_context_serialization(self):
        """
        Test serialization/deserialization for UserContext
        """

        # Construct a json representation of a UserContext model
        user_context_model_json = {}
        user_context_model_json['db'] = 'testString'
        user_context_model_json['name'] = 'testString'
        user_context_model_json['roles'] = ['_reader']

        # Construct a model instance of UserContext by calling from_dict on the json representation
        user_context_model = UserContext.from_dict(user_context_model_json)
        assert user_context_model != False

        # Construct a model instance of UserContext by calling from_dict on the json representation
        user_context_model_dict = UserContext.from_dict(user_context_model_json).__dict__
        user_context_model2 = UserContext(**user_context_model_dict)

        # Verify the model instances are equivalent
        assert user_context_model == user_context_model2

        # Convert model instance back to dict and verify no loss of data
        user_context_model_json2 = user_context_model.to_dict()
        assert user_context_model_json2 == user_context_model_json

class TestUuidsResult():
    """
    Test Class for UuidsResult
    """

    def test_uuids_result_serialization(self):
        """
        Test serialization/deserialization for UuidsResult
        """

        # Construct a json representation of a UuidsResult model
        uuids_result_model_json = {}
        uuids_result_model_json['uuids'] = ['testString']

        # Construct a model instance of UuidsResult by calling from_dict on the json representation
        uuids_result_model = UuidsResult.from_dict(uuids_result_model_json)
        assert uuids_result_model != False

        # Construct a model instance of UuidsResult by calling from_dict on the json representation
        uuids_result_model_dict = UuidsResult.from_dict(uuids_result_model_json).__dict__
        uuids_result_model2 = UuidsResult(**uuids_result_model_dict)

        # Verify the model instances are equivalent
        assert uuids_result_model == uuids_result_model2

        # Convert model instance back to dict and verify no loss of data
        uuids_result_model_json2 = uuids_result_model.to_dict()
        assert uuids_result_model_json2 == uuids_result_model_json

class TestViewQueriesResult():
    """
    Test Class for ViewQueriesResult
    """

    def test_view_queries_result_serialization(self):
        """
        Test serialization/deserialization for ViewQueriesResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        view_result_row_model = {} # ViewResultRow
        view_result_row_model['caused_by'] = 'testString'
        view_result_row_model['error'] = 'testString'
        view_result_row_model['reason'] = 'testString'
        view_result_row_model['doc'] = document_model
        view_result_row_model['id'] = 'testString'
        view_result_row_model['key'] = { 'foo': 'bar' }
        view_result_row_model['value'] = { 'foo': 'bar' }

        view_result_model = {} # ViewResult
        view_result_model['total_rows'] = 0
        view_result_model['update_seq'] = 'testString'
        view_result_model['rows'] = [view_result_row_model]

        # Construct a json representation of a ViewQueriesResult model
        view_queries_result_model_json = {}
        view_queries_result_model_json['results'] = [view_result_model]

        # Construct a model instance of ViewQueriesResult by calling from_dict on the json representation
        view_queries_result_model = ViewQueriesResult.from_dict(view_queries_result_model_json)
        assert view_queries_result_model != False

        # Construct a model instance of ViewQueriesResult by calling from_dict on the json representation
        view_queries_result_model_dict = ViewQueriesResult.from_dict(view_queries_result_model_json).__dict__
        view_queries_result_model2 = ViewQueriesResult(**view_queries_result_model_dict)

        # Verify the model instances are equivalent
        assert view_queries_result_model == view_queries_result_model2

        # Convert model instance back to dict and verify no loss of data
        view_queries_result_model_json2 = view_queries_result_model.to_dict()
        assert view_queries_result_model_json2 == view_queries_result_model_json

class TestViewQuery():
    """
    Test Class for ViewQuery
    """

    def test_view_query_serialization(self):
        """
        Test serialization/deserialization for ViewQuery
        """

        # Construct a json representation of a ViewQuery model
        view_query_model_json = {}
        view_query_model_json['att_encoding_info'] = True
        view_query_model_json['attachments'] = True
        view_query_model_json['conflicts'] = True
        view_query_model_json['descending'] = True
        view_query_model_json['include_docs'] = True
        view_query_model_json['inclusive_end'] = True
        view_query_model_json['limit'] = 0
        view_query_model_json['skip'] = 0
        view_query_model_json['update_seq'] = True
        view_query_model_json['endkey'] = { 'foo': 'bar' }
        view_query_model_json['endkey_docid'] = 'testString'
        view_query_model_json['group'] = True
        view_query_model_json['group_level'] = 1
        view_query_model_json['key'] = { 'foo': 'bar' }
        view_query_model_json['keys'] = [{ 'foo': 'bar' }]
        view_query_model_json['reduce'] = True
        view_query_model_json['stable'] = True
        view_query_model_json['startkey'] = { 'foo': 'bar' }
        view_query_model_json['startkey_docid'] = 'testString'
        view_query_model_json['update'] = 'true'

        # Construct a model instance of ViewQuery by calling from_dict on the json representation
        view_query_model = ViewQuery.from_dict(view_query_model_json)
        assert view_query_model != False

        # Construct a model instance of ViewQuery by calling from_dict on the json representation
        view_query_model_dict = ViewQuery.from_dict(view_query_model_json).__dict__
        view_query_model2 = ViewQuery(**view_query_model_dict)

        # Verify the model instances are equivalent
        assert view_query_model == view_query_model2

        # Convert model instance back to dict and verify no loss of data
        view_query_model_json2 = view_query_model.to_dict()
        assert view_query_model_json2 == view_query_model_json

class TestViewResult():
    """
    Test Class for ViewResult
    """

    def test_view_result_serialization(self):
        """
        Test serialization/deserialization for ViewResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        view_result_row_model = {} # ViewResultRow
        view_result_row_model['caused_by'] = 'testString'
        view_result_row_model['error'] = 'testString'
        view_result_row_model['reason'] = 'testString'
        view_result_row_model['doc'] = document_model
        view_result_row_model['id'] = 'testString'
        view_result_row_model['key'] = { 'foo': 'bar' }
        view_result_row_model['value'] = { 'foo': 'bar' }

        # Construct a json representation of a ViewResult model
        view_result_model_json = {}
        view_result_model_json['total_rows'] = 0
        view_result_model_json['update_seq'] = 'testString'
        view_result_model_json['rows'] = [view_result_row_model]

        # Construct a model instance of ViewResult by calling from_dict on the json representation
        view_result_model = ViewResult.from_dict(view_result_model_json)
        assert view_result_model != False

        # Construct a model instance of ViewResult by calling from_dict on the json representation
        view_result_model_dict = ViewResult.from_dict(view_result_model_json).__dict__
        view_result_model2 = ViewResult(**view_result_model_dict)

        # Verify the model instances are equivalent
        assert view_result_model == view_result_model2

        # Convert model instance back to dict and verify no loss of data
        view_result_model_json2 = view_result_model.to_dict()
        assert view_result_model_json2 == view_result_model_json

class TestViewResultRow():
    """
    Test Class for ViewResultRow
    """

    def test_view_result_row_serialization(self):
        """
        Test serialization/deserialization for ViewResultRow
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_model = {} # Attachment
        attachment_model['content_type'] = 'testString'
        attachment_model['data'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        attachment_model['digest'] = 'testString'
        attachment_model['encoded_length'] = 0
        attachment_model['encoding'] = 'testString'
        attachment_model['follows'] = True
        attachment_model['length'] = 0
        attachment_model['revpos'] = 1
        attachment_model['stub'] = True

        revisions_model = {} # Revisions
        revisions_model['ids'] = ['testString']
        revisions_model['start'] = 1

        document_revision_status_model = {} # DocumentRevisionStatus
        document_revision_status_model['rev'] = 'testString'
        document_revision_status_model['status'] = 'available'

        document_model = {} # Document
        document_model['_attachments'] = {}
        document_model['_conflicts'] = ['testString']
        document_model['_deleted'] = True
        document_model['_deleted_conflicts'] = ['testString']
        document_model['_id'] = 'testString'
        document_model['_local_seq'] = 'testString'
        document_model['_rev'] = 'testString'
        document_model['_revisions'] = revisions_model
        document_model['_revs_info'] = [document_revision_status_model]
        document_model['foo'] = { 'foo': 'bar' }

        # Construct a json representation of a ViewResultRow model
        view_result_row_model_json = {}
        view_result_row_model_json['caused_by'] = 'testString'
        view_result_row_model_json['error'] = 'testString'
        view_result_row_model_json['reason'] = 'testString'
        view_result_row_model_json['doc'] = document_model
        view_result_row_model_json['id'] = 'testString'
        view_result_row_model_json['key'] = { 'foo': 'bar' }
        view_result_row_model_json['value'] = { 'foo': 'bar' }

        # Construct a model instance of ViewResultRow by calling from_dict on the json representation
        view_result_row_model = ViewResultRow.from_dict(view_result_row_model_json)
        assert view_result_row_model != False

        # Construct a model instance of ViewResultRow by calling from_dict on the json representation
        view_result_row_model_dict = ViewResultRow.from_dict(view_result_row_model_json).__dict__
        view_result_row_model2 = ViewResultRow(**view_result_row_model_dict)

        # Verify the model instances are equivalent
        assert view_result_row_model == view_result_row_model2

        # Convert model instance back to dict and verify no loss of data
        view_result_row_model_json2 = view_result_row_model.to_dict()
        assert view_result_row_model_json2 == view_result_row_model_json

class TestGeoJsonGeometry():
    """
    Test Class for GeoJsonGeometry
    """

    def test_geo_json_geometry_serialization(self):
        """
        Test serialization/deserialization for GeoJsonGeometry
        """

        # Construct a json representation of a GeoJsonGeometry model
        geo_json_geometry_model_json = {}
        geo_json_geometry_model_json['type'] = 'Point'
        geo_json_geometry_model_json['coordinates'] = [{ 'foo': 'bar' }]

        # Construct a model instance of GeoJsonGeometry by calling from_dict on the json representation
        geo_json_geometry_model = GeoJsonGeometry.from_dict(geo_json_geometry_model_json)
        assert geo_json_geometry_model != False

        # Construct a model instance of GeoJsonGeometry by calling from_dict on the json representation
        geo_json_geometry_model_dict = GeoJsonGeometry.from_dict(geo_json_geometry_model_json).__dict__
        geo_json_geometry_model2 = GeoJsonGeometry(**geo_json_geometry_model_dict)

        # Verify the model instances are equivalent
        assert geo_json_geometry_model == geo_json_geometry_model2

        # Convert model instance back to dict and verify no loss of data
        geo_json_geometry_model_json2 = geo_json_geometry_model.to_dict()
        assert geo_json_geometry_model_json2 == geo_json_geometry_model_json

class TestGeoJsonGeometryCollection():
    """
    Test Class for GeoJsonGeometryCollection
    """

    def test_geo_json_geometry_collection_serialization(self):
        """
        Test serialization/deserialization for GeoJsonGeometryCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        geo_json_geometry_model = {} # GeoJsonGeometry
        geo_json_geometry_model['type'] = 'Point'
        geo_json_geometry_model['coordinates'] = [{ 'foo': 'bar' }]

        # Construct a json representation of a GeoJsonGeometryCollection model
        geo_json_geometry_collection_model_json = {}
        geo_json_geometry_collection_model_json['type'] = 'Point'
        geo_json_geometry_collection_model_json['geometries'] = [geo_json_geometry_model]

        # Construct a model instance of GeoJsonGeometryCollection by calling from_dict on the json representation
        geo_json_geometry_collection_model = GeoJsonGeometryCollection.from_dict(geo_json_geometry_collection_model_json)
        assert geo_json_geometry_collection_model != False

        # Construct a model instance of GeoJsonGeometryCollection by calling from_dict on the json representation
        geo_json_geometry_collection_model_dict = GeoJsonGeometryCollection.from_dict(geo_json_geometry_collection_model_json).__dict__
        geo_json_geometry_collection_model2 = GeoJsonGeometryCollection(**geo_json_geometry_collection_model_dict)

        # Verify the model instances are equivalent
        assert geo_json_geometry_collection_model == geo_json_geometry_collection_model2

        # Convert model instance back to dict and verify no loss of data
        geo_json_geometry_collection_model_json2 = geo_json_geometry_collection_model.to_dict()
        assert geo_json_geometry_collection_model_json2 == geo_json_geometry_collection_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
