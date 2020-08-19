# coding: utf-8

# (C) Copyright IBM Corp. 2020.
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

# IBM OpenAPI SDK Code Generator Version: 3.10.3-18e3fe12-20200803-172650
 
"""
NoSQL database based on Apache CouchDB
"""

from datetime import datetime
from enum import Enum
from typing import BinaryIO, Dict, List, Union
import base64
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_list, convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class CloudantV1(BaseService):
    """The Cloudant V1 service."""

    DEFAULT_SERVICE_URL = 'http://localhost:5984'
    DEFAULT_SERVICE_NAME = 'cloudant'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'CloudantV1':
        """
        Return a new client for the Cloudant service using the specified parameters
               and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Cloudant service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Server
    #########################


    def get_server_information(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve server instance information.

        When you access the root of an instance, IBM Cloudant returns meta-information
        about the instance. The response includes a JSON structure that contains
        information about the server, including a welcome message and the server's
        version.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServerInformation` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_server_information')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_membership_information(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve cluster membership information.

        Displays the nodes that are part of the cluster as `cluster_nodes`. The field,
        `all_nodes`, displays all nodes this node knows about, including the ones that are
        part of the cluster. This endpoint is useful when you set up a cluster.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MembershipInformation` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_membership_information')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_membership'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_uuids(self,
        *,
        count: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve one or more UUIDs.

        Requests one or more Universally Unique Identifiers (UUIDs) from the instance. The
        response is a JSON object that provides a list of UUIDs.

        :param int count: (optional) Query parameter to specify the number of UUIDs
               to return.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UuidsResult` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_uuids')
        headers.update(sdk_headers)

        params = {
            'count': count
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_uuids'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Databases
    #########################


    def head_database(self,
        db: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve the HTTP headers for a database.

        Returns the HTTP headers that contain a minimal amount of information about the
        specified database. Since the response body is empty, using the HEAD method is a
        lightweight way to check if the database exists or not.

        :param str db: Path parameter to specify the database name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='head_database')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/{0}'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='HEAD',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_all_dbs(self,
        *,
        descending: bool = None,
        endkey: str = None,
        limit: int = None,
        skip: int = None,
        startkey: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a list of all database names in the instance.

        :param bool descending: (optional) Query parameter to specify whether to
               return the documents in descending by key order.
        :param str endkey: (optional) Query parameter to specify to stop returning
               records when the specified key is reached. String representation of any
               JSON type that matches the key type emitted by the view function.
        :param int limit: (optional) Query parameter to specify the number of
               returned documents to limit the result to.
        :param int skip: (optional) Query parameter to specify the number of
               records before starting to return the results.
        :param str startkey: (optional) Query parameter to specify to start
               returning records from the specified key. String representation of any JSON
               type that matches the key type emitted by the view function.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[str]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_all_dbs')
        headers.update(sdk_headers)

        params = {
            'descending': descending,
            'endkey': endkey,
            'limit': limit,
            'skip': skip,
            'startkey': startkey
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_all_dbs'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def post_dbs_info(self,
        *,
        keys: List[str] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query information about multiple databases.

        This operation enables you to request information about multiple databases in a
        single request, instead of issuing multiple `GET /{db}` requests. It returns a
        list that contains an information object for each database specified in the
        request.

        :param List[str] keys: (optional) A list of database names.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[DbsInfoResult]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_dbs_info')
        headers.update(sdk_headers)

        data = {
            'keys': keys
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_dbs_info'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_database(self,
        db: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a database.

        Deletes the specified database and all documents and attachments contained within
        it. To avoid deleting a database, the server responds with a 400 HTTP status code
        when the request URL includes a `?rev=` parameter. This response suggests that a
        user wanted to delete a document but forgot to add the document ID to the URL.

        :param str db: Path parameter to specify the database name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ok` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_database')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_database_information(self,
        db: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve information about a database.

        :param str db: Path parameter to specify the database name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DatabaseInformation` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_database_information')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def put_database(self,
        db: str,
        *,
        partitioned: bool = None,
        q: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a database.

        :param str db: Path parameter to specify the database name.
        :param bool partitioned: (optional) Query parameter to specify whether to
               enable database partitions when creating a database.
        :param int q: (optional) The number of shards in the database. Each shard
               is a partition of the hash value range. Default is 8, unless overridden in
               the `cluster config`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ok` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='put_database')
        headers.update(sdk_headers)

        params = {
            'partitioned': partitioned,
            'q': q
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def post_changes(self,
        db: str,
        *,
        doc_ids: List[str] = None,
        selector: dict = None,
        last_event_id: str = None,
        att_encoding_info: bool = None,
        attachments: bool = None,
        conflicts: bool = None,
        descending: bool = None,
        feed: str = None,
        filter: str = None,
        heartbeat: int = None,
        include_docs: bool = None,
        limit: int = None,
        seq_interval: int = None,
        since: str = None,
        style: str = None,
        timeout: int = None,
        view: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query the database document changes feed.

        Requests the database changes feed in the same way as `GET /{db}/_changes` does.
        It is widely used with the `filter` query parameter because it allows one to pass
        more information to the filter.

        :param str db: Path parameter to specify the database name.
        :param List[str] doc_ids: (optional) Schema for a list of document IDs.
        :param dict selector: (optional) JSON object describing criteria used to
               select documents. The selector specifies fields in the document, and
               provides an expression to evaluate with the field content or other data.
               The selector object must:
                 * Be structured as valid JSON.
                 * Contain a valid query expression.
               Using a selector is significantly more efficient than using a JavaScript
               filter function, and is the recommended option if filtering on document
               attributes only.
               Elementary selector syntax requires you to specify one or more fields, and
               the corresponding values required for those fields. You can create more
               complex selector expressions by combining operators.
               Operators are identified by the use of a dollar sign `$` prefix in the name
               field.
               There are two core types of operators in the selector syntax:
               * Combination operators: applied at the topmost level of selection. They
               are used to combine selectors. In addition to the common boolean operators
               (`$and`, `$or`, `$not`, `$nor`) there are three combination operators:
               `$all`, `$elemMatch`, and `$allMatch`. A combination operator takes a
               single argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
        :param str last_event_id: (optional) Header parameter to specify the ID of
               the last events received by the server on a previous connection. Overrides
               `since` query parameter.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool conflicts: (optional) Query parameter to specify whether to
               include a list of conflicted revisions in the `_conflicts` property of the
               returned document. Ignored if `include_docs` isn't `true`.
        :param bool descending: (optional) Query parameter to specify whether to
               return the documents in descending by key order.
        :param str feed: (optional) Query parameter to specify the changes feed
               type.
        :param str filter: (optional) Query parameter to specify a filter function
               from a design document that will filter the changes stream emitting only
               filtered events. Additionally, several built-in filters are available:
               - `_design`
               - Returns only changes to design documents.
               - `_doc_ids`
               - Returns changes for documents whit an ID matching one specified in
               `doc_ids` request body parameter.
               - `_selector`
               - Returns changes for documents that match the `selector` request body
               parameter. The selector syntax is the same as used for `_find`.
               - `_view`
               - Returns changes for documents that match an existing map function in the
               view specified by the query parameter `view`.
        :param int heartbeat: (optional) Query parameter to specify the period in
               milliseconds after which an empty line is sent in the results. Only
               applicable for longpoll, continuous, and eventsource feeds. Overrides any
               timeout to keep the feed alive indefinitely. May also be `true` to use
               default value of 60000.
        :param bool include_docs: (optional) Query parameter to specify whether to
               include the full content of the documents in the response.
        :param int limit: (optional) Query parameter to specify the number of
               returned documents to limit the result to.
        :param int seq_interval: (optional) Query parameter to specify that the
               update seq should only be calculated with every Nth result returned. When
               fetching changes in a batch, setting <code>seq_interval=&lt;batch
               size&gt;</code>, where &lt;batch size&gt; is the number of results
               requested per batch, load can be reduced on the source database as
               computing the seq value across many shards (especially in highly-sharded
               databases) is expensive.
        :param str since: (optional) Query parameter to specify to start the
               results from the change immediately after the given update sequence. Can be
               a valid update sequence or `now` value. Default is `0` i.e. all changes.
        :param str style: (optional) Query parameter to specify how many revisions
               are returned in the changes array. The default, `main_only`, will only
               return the current "winning" revision; all_docs will return all leaf
               revisions (including conflicts and deleted former conflicts).
        :param int timeout: (optional) Query parameter to specify the maximum
               period in milliseconds to wait for a change before the response is sent,
               even if there are no results. Only applicable for `longpoll` or
               `continuous` feeds. Default value is specified by `httpd/changes_timeout`
               configuration option. Note that `60000` value is also the default maximum
               timeout to prevent undetected dead connections.
        :param str view: (optional) Query parameter to specify a view function as a
               filter. Documents pass the filter if the view's map function emits at least
               one record for them.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ChangesResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {
            'Last-Event-ID': last_event_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_changes')
        headers.update(sdk_headers)

        params = {
            'att_encoding_info': att_encoding_info,
            'attachments': attachments,
            'conflicts': conflicts,
            'descending': descending,
            'feed': feed,
            'filter': filter,
            'heartbeat': heartbeat,
            'include_docs': include_docs,
            'limit': limit,
            'seq_interval': seq_interval,
            'since': since,
            'style': style,
            'timeout': timeout,
            'view': view
        }

        data = {
            'doc_ids': doc_ids,
            'selector': selector
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_changes'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


    def post_changes_as_stream(self,
        db: str,
        *,
        doc_ids: List[str] = None,
        selector: dict = None,
        last_event_id: str = None,
        att_encoding_info: bool = None,
        attachments: bool = None,
        conflicts: bool = None,
        descending: bool = None,
        feed: str = None,
        filter: str = None,
        heartbeat: int = None,
        include_docs: bool = None,
        limit: int = None,
        seq_interval: int = None,
        since: str = None,
        style: str = None,
        timeout: int = None,
        view: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query the database document changes feed as stream.

        Requests the database changes feed in the same way as `GET /{db}/_changes` does.
        It is widely used with the `filter` query parameter because it allows one to pass
        more information to the filter.

        :param str db: Path parameter to specify the database name.
        :param List[str] doc_ids: (optional) Schema for a list of document IDs.
        :param dict selector: (optional) JSON object describing criteria used to
               select documents. The selector specifies fields in the document, and
               provides an expression to evaluate with the field content or other data.
               The selector object must:
                 * Be structured as valid JSON.
                 * Contain a valid query expression.
               Using a selector is significantly more efficient than using a JavaScript
               filter function, and is the recommended option if filtering on document
               attributes only.
               Elementary selector syntax requires you to specify one or more fields, and
               the corresponding values required for those fields. You can create more
               complex selector expressions by combining operators.
               Operators are identified by the use of a dollar sign `$` prefix in the name
               field.
               There are two core types of operators in the selector syntax:
               * Combination operators: applied at the topmost level of selection. They
               are used to combine selectors. In addition to the common boolean operators
               (`$and`, `$or`, `$not`, `$nor`) there are three combination operators:
               `$all`, `$elemMatch`, and `$allMatch`. A combination operator takes a
               single argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
        :param str last_event_id: (optional) Header parameter to specify the ID of
               the last events received by the server on a previous connection. Overrides
               `since` query parameter.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool conflicts: (optional) Query parameter to specify whether to
               include a list of conflicted revisions in the `_conflicts` property of the
               returned document. Ignored if `include_docs` isn't `true`.
        :param bool descending: (optional) Query parameter to specify whether to
               return the documents in descending by key order.
        :param str feed: (optional) Query parameter to specify the changes feed
               type.
        :param str filter: (optional) Query parameter to specify a filter function
               from a design document that will filter the changes stream emitting only
               filtered events. Additionally, several built-in filters are available:
               - `_design`
               - Returns only changes to design documents.
               - `_doc_ids`
               - Returns changes for documents whit an ID matching one specified in
               `doc_ids` request body parameter.
               - `_selector`
               - Returns changes for documents that match the `selector` request body
               parameter. The selector syntax is the same as used for `_find`.
               - `_view`
               - Returns changes for documents that match an existing map function in the
               view specified by the query parameter `view`.
        :param int heartbeat: (optional) Query parameter to specify the period in
               milliseconds after which an empty line is sent in the results. Only
               applicable for longpoll, continuous, and eventsource feeds. Overrides any
               timeout to keep the feed alive indefinitely. May also be `true` to use
               default value of 60000.
        :param bool include_docs: (optional) Query parameter to specify whether to
               include the full content of the documents in the response.
        :param int limit: (optional) Query parameter to specify the number of
               returned documents to limit the result to.
        :param int seq_interval: (optional) Query parameter to specify that the
               update seq should only be calculated with every Nth result returned. When
               fetching changes in a batch, setting <code>seq_interval=&lt;batch
               size&gt;</code>, where &lt;batch size&gt; is the number of results
               requested per batch, load can be reduced on the source database as
               computing the seq value across many shards (especially in highly-sharded
               databases) is expensive.
        :param str since: (optional) Query parameter to specify to start the
               results from the change immediately after the given update sequence. Can be
               a valid update sequence or `now` value. Default is `0` i.e. all changes.
        :param str style: (optional) Query parameter to specify how many revisions
               are returned in the changes array. The default, `main_only`, will only
               return the current "winning" revision; all_docs will return all leaf
               revisions (including conflicts and deleted former conflicts).
        :param int timeout: (optional) Query parameter to specify the maximum
               period in milliseconds to wait for a change before the response is sent,
               even if there are no results. Only applicable for `longpoll` or
               `continuous` feeds. Default value is specified by `httpd/changes_timeout`
               configuration option. Note that `60000` value is also the default maximum
               timeout to prevent undetected dead connections.
        :param str view: (optional) Query parameter to specify a view function as a
               filter. Documents pass the filter if the view's map function emits at least
               one record for them.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {
            'Last-Event-ID': last_event_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_changes_as_stream')
        headers.update(sdk_headers)

        params = {
            'att_encoding_info': att_encoding_info,
            'attachments': attachments,
            'conflicts': conflicts,
            'descending': descending,
            'feed': feed,
            'filter': filter,
            'heartbeat': heartbeat,
            'include_docs': include_docs,
            'limit': limit,
            'seq_interval': seq_interval,
            'since': since,
            'style': style,
            'timeout': timeout,
            'view': view
        }

        data = {
            'doc_ids': doc_ids,
            'selector': selector
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_changes'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, stream=True)
        return response

    #########################
    # Documents
    #########################


    def head_document(self,
        db: str,
        doc_id: str,
        *,
        if_none_match: str = None,
        latest: bool = None,
        rev: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve the HTTP headers for the document.

        This method supports the same query arguments as the `GET /{db}/{docid}` method,
        but only the header information (including document size and the revision as an
        ETag) is returned. The ETag header shows the current revision for the requested
        document, and the Content-Length specifies the length of the data if the document
        was requested in full. Add any of the query arguments, then the resulting HTTP
        headers that correspond to it are returned.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str if_none_match: (optional) Header parameter to specify a double
               quoted document revision token for cache control.
        :param bool latest: (optional) Query parameter to specify whether to force
               retrieving latest leaf revision, no matter what rev was requested.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if db is None:
            raise ValueError('db must be provided')
        if doc_id is None:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-None-Match': if_none_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='head_document')
        headers.update(sdk_headers)

        params = {
            'latest': latest,
            'rev': rev
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/{0}/{1}'.format(
            *self.encode_path_vars(db, doc_id))
        request = self.prepare_request(method='HEAD',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def post_document(self,
        db: str,
        *,
        document: Union['Document', BinaryIO] = None,
        content_type: str = None,
        batch: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create or modify a document in a database.

        Creates or modifies a document in the specified database by using the supplied
        JSON document. If the JSON document doesn't specify an `_id` field, then the
        document is created with a new unique ID generated by the UUID algorithm that is
        configured for the server. If the document includes the `_id` field, then it is
        created with that `_id` or updated if the `_id` already exists, and an appropriate
        `_rev` is included in the JSON document. If the `_id` includes the `_local` or
        `_design` prefix, then this operation is used to create or modify local or design
        documents respectively.

        :param str db: Path parameter to specify the database name.
        :param Document document: (optional) HTTP request body for Document
               operations.
        :param str content_type: (optional) The type of the input.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if  document is not None and isinstance(document, Document):
            document = convert_model(document)
            content_type = content_type or 'application/json'
        headers = {
            'Content-Type': content_type
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_document')
        headers.update(sdk_headers)

        params = {
            'batch': batch
        }

        if document is not None and isinstance(document, dict):
            data = json.dumps(document)
            if content_type is None:
                headers['Content-Type'] = 'application/json'
        else:
            data = document

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


    def post_all_docs(self,
        db: str,
        *,
        att_encoding_info: bool = None,
        attachments: bool = None,
        conflicts: bool = None,
        descending: bool = None,
        include_docs: bool = None,
        inclusive_end: bool = None,
        limit: int = None,
        skip: int = None,
        update_seq: bool = None,
        endkey: str = None,
        key: str = None,
        keys: List[str] = None,
        startkey: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a list of all documents in a database.

        Queries the primary index (all document IDs). The results that match the request
        body parameters are returned in a JSON object, including a list of matching
        documents with basic contents, such as the ID and revision. When no request body
        parameters are specified, results for all documents in the database are returned.
        Optionally, document content or additional metadata can be included in the
        response.

        :param str db: Path parameter to specify the database name.
        :param bool att_encoding_info: (optional) Parameter to specify whether to
               include the encoding information in attachment stubs if the particular
               attachment is compressed.
        :param bool attachments: (optional) Parameter to specify whether to include
               attachments bodies in a response.
        :param bool conflicts: (optional) Parameter to specify whether to include a
               list of conflicted revisions in the `_conflicts` property of the returned
               document. Ignored if `include_docs` isn't `true`.
        :param bool descending: (optional) Parameter to specify whether to return
               the documents in descending by key order.
        :param bool include_docs: (optional) Parameter to specify whether to
               include the full content of the documents in the response.
        :param bool inclusive_end: (optional) Parameter to specify whether the
               specified end key should be included in the result.
        :param int limit: (optional) Parameter to specify the number of returned
               documents to limit the result to.
        :param int skip: (optional) Parameter to specify the number of records
               before starting to return the results.
        :param bool update_seq: (optional) Parameter to specify whether to include
               in the response an update_seq value indicating the sequence id of the
               database the view reflects.
        :param str endkey: (optional) Schema for a document ID.
        :param str key: (optional) Schema for a document ID.
        :param List[str] keys: (optional) Schema for a list of document IDs.
        :param str startkey: (optional) Schema for a document ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllDocsResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_all_docs')
        headers.update(sdk_headers)

        data = {
            'att_encoding_info': att_encoding_info,
            'attachments': attachments,
            'conflicts': conflicts,
            'descending': descending,
            'include_docs': include_docs,
            'inclusive_end': inclusive_end,
            'limit': limit,
            'skip': skip,
            'update_seq': update_seq,
            'endkey': endkey,
            'key': key,
            'keys': keys,
            'startkey': startkey
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_all_docs'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_all_docs_as_stream(self,
        db: str,
        *,
        att_encoding_info: bool = None,
        attachments: bool = None,
        conflicts: bool = None,
        descending: bool = None,
        include_docs: bool = None,
        inclusive_end: bool = None,
        limit: int = None,
        skip: int = None,
        update_seq: bool = None,
        endkey: str = None,
        key: str = None,
        keys: List[str] = None,
        startkey: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a list of all documents in a database as stream.

        Queries the primary index (all document IDs). The results that match the request
        body parameters are returned in a JSON object, including a list of matching
        documents with basic contents, such as the ID and revision. When no request body
        parameters are specified, results for all documents in the database are returned.
        Optionally, document content or additional metadata can be included in the
        response.

        :param str db: Path parameter to specify the database name.
        :param bool att_encoding_info: (optional) Parameter to specify whether to
               include the encoding information in attachment stubs if the particular
               attachment is compressed.
        :param bool attachments: (optional) Parameter to specify whether to include
               attachments bodies in a response.
        :param bool conflicts: (optional) Parameter to specify whether to include a
               list of conflicted revisions in the `_conflicts` property of the returned
               document. Ignored if `include_docs` isn't `true`.
        :param bool descending: (optional) Parameter to specify whether to return
               the documents in descending by key order.
        :param bool include_docs: (optional) Parameter to specify whether to
               include the full content of the documents in the response.
        :param bool inclusive_end: (optional) Parameter to specify whether the
               specified end key should be included in the result.
        :param int limit: (optional) Parameter to specify the number of returned
               documents to limit the result to.
        :param int skip: (optional) Parameter to specify the number of records
               before starting to return the results.
        :param bool update_seq: (optional) Parameter to specify whether to include
               in the response an update_seq value indicating the sequence id of the
               database the view reflects.
        :param str endkey: (optional) Schema for a document ID.
        :param str key: (optional) Schema for a document ID.
        :param List[str] keys: (optional) Schema for a list of document IDs.
        :param str startkey: (optional) Schema for a document ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_all_docs_as_stream')
        headers.update(sdk_headers)

        data = {
            'att_encoding_info': att_encoding_info,
            'attachments': attachments,
            'conflicts': conflicts,
            'descending': descending,
            'include_docs': include_docs,
            'inclusive_end': inclusive_end,
            'limit': limit,
            'skip': skip,
            'update_seq': update_seq,
            'endkey': endkey,
            'key': key,
            'keys': keys,
            'startkey': startkey
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_all_docs'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, stream=True)
        return response


    def post_all_docs_queries(self,
        db: str,
        *,
        queries: List['AllDocsQuery'] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Multi-query the list of all documents in a database.

        Runs multiple queries using the primary index (all document IDs). Returns a JSON
        object that contains a list of result objects, one for each query, with a
        structure equivalent to that of a single `_all_docs` request. This enables you to
        request multiple queries in a single request, in place of multiple `POST
        /{db}/_all_docs` requests.

        :param str db: Path parameter to specify the database name.
        :param List[AllDocsQuery] queries: (optional) An array of query objects
               with fields for the parameters of each individual view query to be
               executed. The field names and their meaning are the same as the query
               parameters of a regular `/_all_docs` request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllDocsQueriesResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if queries is not None:
            queries = [convert_model(x) for x in queries]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_all_docs_queries')
        headers.update(sdk_headers)

        data = {
            'queries': queries
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_all_docs/queries'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_all_docs_queries_as_stream(self,
        db: str,
        *,
        queries: List['AllDocsQuery'] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Multi-query the list of all documents in a database as stream.

        Runs multiple queries using the primary index (all document IDs). Returns a JSON
        object that contains a list of result objects, one for each query, with a
        structure equivalent to that of a single `_all_docs` request. This enables you to
        request multiple queries in a single request, in place of multiple `POST
        /{db}/_all_docs` requests.

        :param str db: Path parameter to specify the database name.
        :param List[AllDocsQuery] queries: (optional) An array of query objects
               with fields for the parameters of each individual view query to be
               executed. The field names and their meaning are the same as the query
               parameters of a regular `/_all_docs` request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if queries is not None:
            queries = [convert_model(x) for x in queries]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_all_docs_queries_as_stream')
        headers.update(sdk_headers)

        data = {
            'queries': queries
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_all_docs/queries'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, stream=True)
        return response


    def post_bulk_docs(self,
        db: str,
        *,
        bulk_docs: Union['BulkDocs', BinaryIO] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Bulk modify multiple documents in a database.

        The bulk document API allows you to create and update multiple documents at the
        same time within a single request. The basic operation is similar to creating or
        updating a single document, except that you batch the document structure and
        information.

        :param str db: Path parameter to specify the database name.
        :param BulkDocs bulk_docs: (optional) HTTP request body for postBulkDocs.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[DocumentResult]` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if  bulk_docs is not None and isinstance(bulk_docs, BulkDocs):
            bulk_docs = convert_model(bulk_docs)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_bulk_docs')
        headers.update(sdk_headers)

        if isinstance(bulk_docs, dict):
            data = json.dumps(bulk_docs)
        else:
            data = bulk_docs
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_bulk_docs'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_bulk_get(self,
        db: str,
        *,
        docs: List['BulkGetQueryDocument'] = None,
        attachments: bool = None,
        att_encoding_info: bool = None,
        latest: bool = None,
        revs: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Bulk query revision information for multiple documents.

        Fetch specific revisions or revision histories for multiple documents in bulk as
        replicators do.

        :param str db: Path parameter to specify the database name.
        :param List[BulkGetQueryDocument] docs: (optional) List of document items
               to get in bulk.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param bool latest: (optional) Query parameter to specify whether to force
               retrieving latest leaf revision, no matter what rev was requested.
        :param bool revs: (optional) Query parameter to specify whether to include
               a list of all known document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BulkGetResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if docs is not None:
            docs = [convert_model(x) for x in docs]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_bulk_get')
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'latest': latest,
            'revs': revs
        }

        data = {
            'docs': docs
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_bulk_get'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


    def post_bulk_get_as_mixed(self,
        db: str,
        *,
        docs: List['BulkGetQueryDocument'] = None,
        attachments: bool = None,
        att_encoding_info: bool = None,
        latest: bool = None,
        revs: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Bulk query revision information for multiple documents as mixed.

        Fetch specific revisions or revision histories for multiple documents in bulk as
        replicators do.

        :param str db: Path parameter to specify the database name.
        :param List[BulkGetQueryDocument] docs: (optional) List of document items
               to get in bulk.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param bool latest: (optional) Query parameter to specify whether to force
               retrieving latest leaf revision, no matter what rev was requested.
        :param bool revs: (optional) Query parameter to specify whether to include
               a list of all known document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if docs is not None:
            docs = [convert_model(x) for x in docs]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_bulk_get_as_mixed')
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'latest': latest,
            'revs': revs
        }

        data = {
            'docs': docs
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'multipart/mixed'

        url = '/{0}/_bulk_get'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


    def post_bulk_get_as_related(self,
        db: str,
        *,
        docs: List['BulkGetQueryDocument'] = None,
        attachments: bool = None,
        att_encoding_info: bool = None,
        latest: bool = None,
        revs: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Bulk query revision information for multiple documents as related.

        Fetch specific revisions or revision histories for multiple documents in bulk as
        replicators do.

        :param str db: Path parameter to specify the database name.
        :param List[BulkGetQueryDocument] docs: (optional) List of document items
               to get in bulk.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param bool latest: (optional) Query parameter to specify whether to force
               retrieving latest leaf revision, no matter what rev was requested.
        :param bool revs: (optional) Query parameter to specify whether to include
               a list of all known document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if docs is not None:
            docs = [convert_model(x) for x in docs]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_bulk_get_as_related')
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'latest': latest,
            'revs': revs
        }

        data = {
            'docs': docs
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'multipart/related'

        url = '/{0}/_bulk_get'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


    def post_bulk_get_as_stream(self,
        db: str,
        *,
        docs: List['BulkGetQueryDocument'] = None,
        attachments: bool = None,
        att_encoding_info: bool = None,
        latest: bool = None,
        revs: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Bulk query revision information for multiple documents as stream.

        Fetch specific revisions or revision histories for multiple documents in bulk as
        replicators do.

        :param str db: Path parameter to specify the database name.
        :param List[BulkGetQueryDocument] docs: (optional) List of document items
               to get in bulk.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param bool latest: (optional) Query parameter to specify whether to force
               retrieving latest leaf revision, no matter what rev was requested.
        :param bool revs: (optional) Query parameter to specify whether to include
               a list of all known document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if docs is not None:
            docs = [convert_model(x) for x in docs]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_bulk_get_as_stream')
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'latest': latest,
            'revs': revs
        }

        data = {
            'docs': docs
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_bulk_get'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, stream=True)
        return response


    def delete_document(self,
        db: str,
        doc_id: str,
        *,
        if_match: str = None,
        batch: str = None,
        rev: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a document.

        Marks the specified document as deleted by adding a `_deleted` field with the
        value `true`. Documents with this field are not returned within requests anymore
        but stay in the database. You must supply the current (latest) revision, either by
        using the `rev` parameter or by using the `If-Match` header to specify the
        revision.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str if_match: (optional) Header parameter to specify the document
               revision. Alternative to rev query parameter.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if doc_id is None:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_document')
        headers.update(sdk_headers)

        params = {
            'batch': batch,
            'rev': rev
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/{1}'.format(
            *self.encode_path_vars(db, doc_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_document(self,
        db: str,
        doc_id: str,
        *,
        if_none_match: str = None,
        attachments: bool = None,
        att_encoding_info: bool = None,
        atts_since: List[str] = None,
        conflicts: bool = None,
        deleted_conflicts: bool = None,
        latest: bool = None,
        local_seq: bool = None,
        meta: bool = None,
        open_revs: List[str] = None,
        rev: str = None,
        revs: bool = None,
        revs_info: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve a document.

        Returns document with the specified `doc_id` from the specified database. Unless
        you request a specific revision, the latest revision of the document is always
        returned.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str if_none_match: (optional) Header parameter to specify a double
               quoted document revision token for cache control.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param List[str] atts_since: (optional) Query parameter to specify whether
               to include attachments only since specified revisions. Note this does not
               include the attachments for the specified revisions.
        :param bool conflicts: (optional) Query parameter to specify whether to
               include a list of conflicted revisions in the `_conflicts` property of the
               returned document. Ignored if `include_docs` isn't `true`.
        :param bool deleted_conflicts: (optional) Query parameter to specify
               whether to include a list of deleted conflicted revisions in the
               `_deleted_conflicts` property of the returned document.
        :param bool latest: (optional) Query parameter to specify whether to force
               retrieving latest leaf revision, no matter what rev was requested.
        :param bool local_seq: (optional) Query parameter to specify whether to
               include the last update sequence for the document.
        :param bool meta: (optional) Query parameter to specify whether to include
               document meta information. Acts the same as specifying all of the
               conflicts, deleted_conflicts and open_revs query parameters.
        :param List[str] open_revs: (optional) Query parameter to specify leaf
               revisions to retrieve. Additionally, it accepts a value of `all` to return
               all leaf revisions.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param bool revs: (optional) Query parameter to specify whether to include
               a list of all known document revisions.
        :param bool revs_info: (optional) Query parameter to specify whether to
               includes detailed information for all known document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Document` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if doc_id is None:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-None-Match': if_none_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_document')
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'atts_since': convert_list(atts_since),
            'conflicts': conflicts,
            'deleted_conflicts': deleted_conflicts,
            'latest': latest,
            'local_seq': local_seq,
            'meta': meta,
            'open_revs': convert_list(open_revs),
            'rev': rev,
            'revs': revs,
            'revs_info': revs_info
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/{1}'.format(
            *self.encode_path_vars(db, doc_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_document_as_mixed(self,
        db: str,
        doc_id: str,
        *,
        if_none_match: str = None,
        attachments: bool = None,
        att_encoding_info: bool = None,
        atts_since: List[str] = None,
        conflicts: bool = None,
        deleted_conflicts: bool = None,
        latest: bool = None,
        local_seq: bool = None,
        meta: bool = None,
        open_revs: List[str] = None,
        rev: str = None,
        revs: bool = None,
        revs_info: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve a document as mixed.

        Returns document with the specified `doc_id` from the specified database. Unless
        you request a specific revision, the latest revision of the document is always
        returned.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str if_none_match: (optional) Header parameter to specify a double
               quoted document revision token for cache control.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param List[str] atts_since: (optional) Query parameter to specify whether
               to include attachments only since specified revisions. Note this does not
               include the attachments for the specified revisions.
        :param bool conflicts: (optional) Query parameter to specify whether to
               include a list of conflicted revisions in the `_conflicts` property of the
               returned document. Ignored if `include_docs` isn't `true`.
        :param bool deleted_conflicts: (optional) Query parameter to specify
               whether to include a list of deleted conflicted revisions in the
               `_deleted_conflicts` property of the returned document.
        :param bool latest: (optional) Query parameter to specify whether to force
               retrieving latest leaf revision, no matter what rev was requested.
        :param bool local_seq: (optional) Query parameter to specify whether to
               include the last update sequence for the document.
        :param bool meta: (optional) Query parameter to specify whether to include
               document meta information. Acts the same as specifying all of the
               conflicts, deleted_conflicts and open_revs query parameters.
        :param List[str] open_revs: (optional) Query parameter to specify leaf
               revisions to retrieve. Additionally, it accepts a value of `all` to return
               all leaf revisions.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param bool revs: (optional) Query parameter to specify whether to include
               a list of all known document revisions.
        :param bool revs_info: (optional) Query parameter to specify whether to
               includes detailed information for all known document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if doc_id is None:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-None-Match': if_none_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_document_as_mixed')
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'atts_since': convert_list(atts_since),
            'conflicts': conflicts,
            'deleted_conflicts': deleted_conflicts,
            'latest': latest,
            'local_seq': local_seq,
            'meta': meta,
            'open_revs': convert_list(open_revs),
            'rev': rev,
            'revs': revs,
            'revs_info': revs_info
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'multipart/mixed'

        url = '/{0}/{1}'.format(
            *self.encode_path_vars(db, doc_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_document_as_related(self,
        db: str,
        doc_id: str,
        *,
        if_none_match: str = None,
        attachments: bool = None,
        att_encoding_info: bool = None,
        atts_since: List[str] = None,
        conflicts: bool = None,
        deleted_conflicts: bool = None,
        latest: bool = None,
        local_seq: bool = None,
        meta: bool = None,
        open_revs: List[str] = None,
        rev: str = None,
        revs: bool = None,
        revs_info: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve a document as related.

        Returns document with the specified `doc_id` from the specified database. Unless
        you request a specific revision, the latest revision of the document is always
        returned.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str if_none_match: (optional) Header parameter to specify a double
               quoted document revision token for cache control.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param List[str] atts_since: (optional) Query parameter to specify whether
               to include attachments only since specified revisions. Note this does not
               include the attachments for the specified revisions.
        :param bool conflicts: (optional) Query parameter to specify whether to
               include a list of conflicted revisions in the `_conflicts` property of the
               returned document. Ignored if `include_docs` isn't `true`.
        :param bool deleted_conflicts: (optional) Query parameter to specify
               whether to include a list of deleted conflicted revisions in the
               `_deleted_conflicts` property of the returned document.
        :param bool latest: (optional) Query parameter to specify whether to force
               retrieving latest leaf revision, no matter what rev was requested.
        :param bool local_seq: (optional) Query parameter to specify whether to
               include the last update sequence for the document.
        :param bool meta: (optional) Query parameter to specify whether to include
               document meta information. Acts the same as specifying all of the
               conflicts, deleted_conflicts and open_revs query parameters.
        :param List[str] open_revs: (optional) Query parameter to specify leaf
               revisions to retrieve. Additionally, it accepts a value of `all` to return
               all leaf revisions.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param bool revs: (optional) Query parameter to specify whether to include
               a list of all known document revisions.
        :param bool revs_info: (optional) Query parameter to specify whether to
               includes detailed information for all known document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if doc_id is None:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-None-Match': if_none_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_document_as_related')
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'atts_since': convert_list(atts_since),
            'conflicts': conflicts,
            'deleted_conflicts': deleted_conflicts,
            'latest': latest,
            'local_seq': local_seq,
            'meta': meta,
            'open_revs': convert_list(open_revs),
            'rev': rev,
            'revs': revs,
            'revs_info': revs_info
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'multipart/related'

        url = '/{0}/{1}'.format(
            *self.encode_path_vars(db, doc_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_document_as_stream(self,
        db: str,
        doc_id: str,
        *,
        if_none_match: str = None,
        attachments: bool = None,
        att_encoding_info: bool = None,
        atts_since: List[str] = None,
        conflicts: bool = None,
        deleted_conflicts: bool = None,
        latest: bool = None,
        local_seq: bool = None,
        meta: bool = None,
        open_revs: List[str] = None,
        rev: str = None,
        revs: bool = None,
        revs_info: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve a document as stream.

        Returns document with the specified `doc_id` from the specified database. Unless
        you request a specific revision, the latest revision of the document is always
        returned.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str if_none_match: (optional) Header parameter to specify a double
               quoted document revision token for cache control.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param List[str] atts_since: (optional) Query parameter to specify whether
               to include attachments only since specified revisions. Note this does not
               include the attachments for the specified revisions.
        :param bool conflicts: (optional) Query parameter to specify whether to
               include a list of conflicted revisions in the `_conflicts` property of the
               returned document. Ignored if `include_docs` isn't `true`.
        :param bool deleted_conflicts: (optional) Query parameter to specify
               whether to include a list of deleted conflicted revisions in the
               `_deleted_conflicts` property of the returned document.
        :param bool latest: (optional) Query parameter to specify whether to force
               retrieving latest leaf revision, no matter what rev was requested.
        :param bool local_seq: (optional) Query parameter to specify whether to
               include the last update sequence for the document.
        :param bool meta: (optional) Query parameter to specify whether to include
               document meta information. Acts the same as specifying all of the
               conflicts, deleted_conflicts and open_revs query parameters.
        :param List[str] open_revs: (optional) Query parameter to specify leaf
               revisions to retrieve. Additionally, it accepts a value of `all` to return
               all leaf revisions.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param bool revs: (optional) Query parameter to specify whether to include
               a list of all known document revisions.
        :param bool revs_info: (optional) Query parameter to specify whether to
               includes detailed information for all known document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if doc_id is None:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-None-Match': if_none_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_document_as_stream')
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'atts_since': convert_list(atts_since),
            'conflicts': conflicts,
            'deleted_conflicts': deleted_conflicts,
            'latest': latest,
            'local_seq': local_seq,
            'meta': meta,
            'open_revs': convert_list(open_revs),
            'rev': rev,
            'revs': revs,
            'revs_info': revs_info
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/{1}'.format(
            *self.encode_path_vars(db, doc_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, stream=True)
        return response


    def put_document(self,
        db: str,
        doc_id: str,
        *,
        document: Union['Document', BinaryIO] = None,
        content_type: str = None,
        if_match: str = None,
        batch: str = None,
        new_edits: bool = None,
        rev: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create or modify a document.

        The PUT method creates a new named document, or creates a new revision of the
        existing document. Unlike the `POST /{db}` request, you must specify the document
        ID in the request URL.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param Document document: (optional) HTTP request body for Document
               operations.
        :param str content_type: (optional) The type of the input.
        :param str if_match: (optional) Header parameter to specify the document
               revision. Alternative to rev query parameter.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param bool new_edits: (optional) Query parameter to specify whether to
               prevent insertion of conflicting document revisions. If false, a
               well-formed _rev must be included in the document. False is used by the
               replicator to insert documents into the target database even if that leads
               to the creation of conflicts.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if doc_id is None:
            raise ValueError('doc_id must be provided')
        if  document is not None and isinstance(document, Document):
            document = convert_model(document)
            content_type = content_type or 'application/json'
        headers = {
            'Content-Type': content_type,
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='put_document')
        headers.update(sdk_headers)

        params = {
            'batch': batch,
            'new_edits': new_edits,
            'rev': rev
        }

        if document is not None and isinstance(document, dict):
            data = json.dumps(document)
            if content_type is None:
                headers['Content-Type'] = 'application/json'
        else:
            data = document

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/{1}'.format(
            *self.encode_path_vars(db, doc_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Design Documents
    #########################


    def head_design_document(self,
        db: str,
        ddoc: str,
        *,
        if_none_match: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve the HTTP headers for a design document.

        This method supports the same query arguments as the `GET /{db}/_design/{ddoc}`
        method, but the results include only the header information (including design
        document size, and the revision as an ETag). The ETag header shows the current
        revision for the requested design document, and if you requested the design
        document in full, the Content-Length specifies the length of the data. If you add
        any of the query arguments, then the resulting HTTP headers correspond to what is
        returned for the equivalent GET request.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str if_none_match: (optional) Header parameter to specify a double
               quoted document revision token for cache control.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if db is None:
            raise ValueError('db must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        headers = {
            'If-None-Match': if_none_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='head_design_document')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/{0}/_design/{1}'.format(
            *self.encode_path_vars(db, ddoc))
        request = self.prepare_request(method='HEAD',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def delete_design_document(self,
        db: str,
        ddoc: str,
        *,
        if_match: str = None,
        batch: str = None,
        rev: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a design document.

        Marks the specified design document as deleted by adding a `_deleted` field with
        the value `true`. Documents with this field are not returned with requests but
        stay in the database. You must supply the current (latest) revision, either by
        using the `rev` parameter or by using the `If-Match` header to specify the
        revision.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str if_match: (optional) Header parameter to specify the document
               revision. Alternative to rev query parameter.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        headers = {
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_design_document')
        headers.update(sdk_headers)

        params = {
            'batch': batch,
            'rev': rev
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_design/{1}'.format(
            *self.encode_path_vars(db, ddoc))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_design_document(self,
        db: str,
        ddoc: str,
        *,
        if_none_match: str = None,
        attachments: bool = None,
        att_encoding_info: bool = None,
        atts_since: List[str] = None,
        conflicts: bool = None,
        deleted_conflicts: bool = None,
        latest: bool = None,
        local_seq: bool = None,
        meta: bool = None,
        open_revs: List[str] = None,
        rev: str = None,
        revs: bool = None,
        revs_info: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve a design document.

        Returns design document with the specified `doc_id` from the specified database.
        Unless you request a specific revision, the current revision of the design
        document is always returned.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str if_none_match: (optional) Header parameter to specify a double
               quoted document revision token for cache control.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param List[str] atts_since: (optional) Query parameter to specify whether
               to include attachments only since specified revisions. Note this does not
               include the attachments for the specified revisions.
        :param bool conflicts: (optional) Query parameter to specify whether to
               include a list of conflicted revisions in the `_conflicts` property of the
               returned document. Ignored if `include_docs` isn't `true`.
        :param bool deleted_conflicts: (optional) Query parameter to specify
               whether to include a list of deleted conflicted revisions in the
               `_deleted_conflicts` property of the returned document.
        :param bool latest: (optional) Query parameter to specify whether to force
               retrieving latest leaf revision, no matter what rev was requested.
        :param bool local_seq: (optional) Query parameter to specify whether to
               include the last update sequence for the document.
        :param bool meta: (optional) Query parameter to specify whether to include
               document meta information. Acts the same as specifying all of the
               conflicts, deleted_conflicts and open_revs query parameters.
        :param List[str] open_revs: (optional) Query parameter to specify leaf
               revisions to retrieve. Additionally, it accepts a value of `all` to return
               all leaf revisions.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param bool revs: (optional) Query parameter to specify whether to include
               a list of all known document revisions.
        :param bool revs_info: (optional) Query parameter to specify whether to
               includes detailed information for all known document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DesignDocument` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        headers = {
            'If-None-Match': if_none_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_design_document')
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'atts_since': convert_list(atts_since),
            'conflicts': conflicts,
            'deleted_conflicts': deleted_conflicts,
            'latest': latest,
            'local_seq': local_seq,
            'meta': meta,
            'open_revs': convert_list(open_revs),
            'rev': rev,
            'revs': revs,
            'revs_info': revs_info
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_design/{1}'.format(
            *self.encode_path_vars(db, ddoc))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def put_design_document(self,
        db: str,
        ddoc: str,
        *,
        design_document: 'DesignDocument' = None,
        if_match: str = None,
        batch: str = None,
        new_edits: bool = None,
        rev: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create or modify a design document.

        The PUT method creates a new named design document, or creates a new revision of
        the existing design document.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param DesignDocument design_document: (optional) HTTP request body for
               DesignDocument operations.
        :param str if_match: (optional) Header parameter to specify the document
               revision. Alternative to rev query parameter.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param bool new_edits: (optional) Query parameter to specify whether to
               prevent insertion of conflicting document revisions. If false, a
               well-formed _rev must be included in the document. False is used by the
               replicator to insert documents into the target database even if that leads
               to the creation of conflicts.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        if  design_document is not None and isinstance(design_document, DesignDocument):
            design_document = convert_model(design_document)
        headers = {
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='put_design_document')
        headers.update(sdk_headers)

        params = {
            'batch': batch,
            'new_edits': new_edits,
            'rev': rev
        }

        data = json.dumps(design_document)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_design/{1}'.format(
            *self.encode_path_vars(db, ddoc))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


    def get_design_document_information(self,
        db: str,
        ddoc: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve information about a design document.

        Retrieves information about the specified design document, including the index,
        index size, and current status of the design document and associated index
        information.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DesignDocumentInformation` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_design_document_information')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_design/{1}/_info'.format(
            *self.encode_path_vars(db, ddoc))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def post_design_docs(self,
        db: str,
        *,
        accept: str = None,
        att_encoding_info: bool = None,
        attachments: bool = None,
        conflicts: bool = None,
        descending: bool = None,
        include_docs: bool = None,
        inclusive_end: bool = None,
        limit: int = None,
        skip: int = None,
        update_seq: bool = None,
        endkey: str = None,
        key: str = None,
        keys: List[str] = None,
        startkey: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a list of all design documents in a database.

        Queries the index of all design document IDs. The results matching the request
        body parameters are returned in a JSON object, including a list of matching design
        documents with basic contents, such as the ID and revision. When no request body
        parameters are specified, results for all design documents in the database are
        returned. Optionally, the design document content or additional metadata can be
        included in the response.

        :param str db: Path parameter to specify the database name.
        :param str accept: (optional) The type of the response: application/json or
               application/octet-stream.
        :param bool att_encoding_info: (optional) Parameter to specify whether to
               include the encoding information in attachment stubs if the particular
               attachment is compressed.
        :param bool attachments: (optional) Parameter to specify whether to include
               attachments bodies in a response.
        :param bool conflicts: (optional) Parameter to specify whether to include a
               list of conflicted revisions in the `_conflicts` property of the returned
               document. Ignored if `include_docs` isn't `true`.
        :param bool descending: (optional) Parameter to specify whether to return
               the documents in descending by key order.
        :param bool include_docs: (optional) Parameter to specify whether to
               include the full content of the documents in the response.
        :param bool inclusive_end: (optional) Parameter to specify whether the
               specified end key should be included in the result.
        :param int limit: (optional) Parameter to specify the number of returned
               documents to limit the result to.
        :param int skip: (optional) Parameter to specify the number of records
               before starting to return the results.
        :param bool update_seq: (optional) Parameter to specify whether to include
               in the response an update_seq value indicating the sequence id of the
               database the view reflects.
        :param str endkey: (optional) Schema for a document ID.
        :param str key: (optional) Schema for a document ID.
        :param List[str] keys: (optional) Schema for a list of document IDs.
        :param str startkey: (optional) Schema for a document ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllDocsResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_design_docs')
        headers.update(sdk_headers)

        data = {
            'att_encoding_info': att_encoding_info,
            'attachments': attachments,
            'conflicts': conflicts,
            'descending': descending,
            'include_docs': include_docs,
            'inclusive_end': inclusive_end,
            'limit': limit,
            'skip': skip,
            'update_seq': update_seq,
            'endkey': endkey,
            'key': key,
            'keys': keys,
            'startkey': startkey
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/{0}/_design_docs'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_design_docs_queries(self,
        db: str,
        *,
        accept: str = None,
        queries: List['AllDocsQuery'] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Multi-query the list of all design documents.

        This operation runs multiple view queries of all design documents in the database.
        This operation enables you to request numerous queries in a single request, in
        place of multiple POST `/{db}/_design_docs` requests.

        :param str db: Path parameter to specify the database name.
        :param str accept: (optional) The type of the response: application/json or
               application/octet-stream.
        :param List[AllDocsQuery] queries: (optional) An array of query objects
               with fields for the parameters of each individual view query to be
               executed. The field names and their meaning are the same as the query
               parameters of a regular `/_all_docs` request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllDocsQueriesResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if queries is not None:
            queries = [convert_model(x) for x in queries]
        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_design_docs_queries')
        headers.update(sdk_headers)

        data = {
            'queries': queries
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/{0}/_design_docs/queries'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Views
    #########################


    def post_view(self,
        db: str,
        ddoc: str,
        view: str,
        *,
        att_encoding_info: bool = None,
        attachments: bool = None,
        conflicts: bool = None,
        descending: bool = None,
        include_docs: bool = None,
        inclusive_end: bool = None,
        limit: int = None,
        skip: int = None,
        update_seq: bool = None,
        endkey: object = None,
        endkey_docid: str = None,
        group: bool = None,
        group_level: int = None,
        key: object = None,
        keys: List[object] = None,
        reduce: bool = None,
        stable: bool = None,
        startkey: object = None,
        startkey_docid: str = None,
        update: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a MapReduce view.

        This operation queries the specified MapReduce view of the specified design
        document. By default, the map and reduce functions of the view are run to update
        the view before returning the response. The advantage of using the HTTP `POST`
        method is that the query is submitted as a JSON object in the request body. This
        avoids the limitations of passing query options as URL query parameters of a `GET`
        request.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str view: Path parameter to specify the map reduce view function
               name.
        :param bool att_encoding_info: (optional) Parameter to specify whether to
               include the encoding information in attachment stubs if the particular
               attachment is compressed.
        :param bool attachments: (optional) Parameter to specify whether to include
               attachments bodies in a response.
        :param bool conflicts: (optional) Parameter to specify whether to include a
               list of conflicted revisions in the `_conflicts` property of the returned
               document. Ignored if `include_docs` isn't `true`.
        :param bool descending: (optional) Parameter to specify whether to return
               the documents in descending by key order.
        :param bool include_docs: (optional) Parameter to specify whether to
               include the full content of the documents in the response.
        :param bool inclusive_end: (optional) Parameter to specify whether the
               specified end key should be included in the result.
        :param int limit: (optional) Parameter to specify the number of returned
               documents to limit the result to.
        :param int skip: (optional) Parameter to specify the number of records
               before starting to return the results.
        :param bool update_seq: (optional) Parameter to specify whether to include
               in the response an update_seq value indicating the sequence id of the
               database the view reflects.
        :param object endkey: (optional) Schema for any JSON type.
        :param str endkey_docid: (optional) Schema for a document ID.
        :param bool group: (optional) Parameter to specify whether to group the
               results using the reduce function to a group rather than a single row.
               Implies reduce is true and the maximum group_level.
        :param int group_level: (optional) Parameter to specify the group level to
               be used. Implies group is true.
        :param object key: (optional) Schema for any JSON type.
        :param List[object] keys: (optional) Parameter to specify to return only
               documents that match the specified keys. String representation of a JSON
               array containing elements that match the key type emitted by the view
               function.
        :param bool reduce: (optional) Parameter to specify whether to use the
               reduce function in a map-reduce view. Default is true when a reduce
               function is defined.
        :param bool stable: (optional) Parameter to specify whether view results
               should be returned from a stable set of shards.
        :param object startkey: (optional) Schema for any JSON type.
        :param str startkey_docid: (optional) Schema for a document ID.
        :param str update: (optional) Parameter to specify whether or not the view
               in question should be updated prior to responding to the user.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ViewResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        if view is None:
            raise ValueError('view must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_view')
        headers.update(sdk_headers)

        data = {
            'att_encoding_info': att_encoding_info,
            'attachments': attachments,
            'conflicts': conflicts,
            'descending': descending,
            'include_docs': include_docs,
            'inclusive_end': inclusive_end,
            'limit': limit,
            'skip': skip,
            'update_seq': update_seq,
            'endkey': endkey,
            'endkey_docid': endkey_docid,
            'group': group,
            'group_level': group_level,
            'key': key,
            'keys': keys,
            'reduce': reduce,
            'stable': stable,
            'startkey': startkey,
            'startkey_docid': startkey_docid,
            'update': update
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_design/{1}/_view/{2}'.format(
            *self.encode_path_vars(db, ddoc, view))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_view_as_stream(self,
        db: str,
        ddoc: str,
        view: str,
        *,
        att_encoding_info: bool = None,
        attachments: bool = None,
        conflicts: bool = None,
        descending: bool = None,
        include_docs: bool = None,
        inclusive_end: bool = None,
        limit: int = None,
        skip: int = None,
        update_seq: bool = None,
        endkey: object = None,
        endkey_docid: str = None,
        group: bool = None,
        group_level: int = None,
        key: object = None,
        keys: List[object] = None,
        reduce: bool = None,
        stable: bool = None,
        startkey: object = None,
        startkey_docid: str = None,
        update: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a MapReduce view as stream.

        This operation queries the specified MapReduce view of the specified design
        document. By default, the map and reduce functions of the view are run to update
        the view before returning the response. The advantage of using the HTTP `POST`
        method is that the query is submitted as a JSON object in the request body. This
        avoids the limitations of passing query options as URL query parameters of a `GET`
        request.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str view: Path parameter to specify the map reduce view function
               name.
        :param bool att_encoding_info: (optional) Parameter to specify whether to
               include the encoding information in attachment stubs if the particular
               attachment is compressed.
        :param bool attachments: (optional) Parameter to specify whether to include
               attachments bodies in a response.
        :param bool conflicts: (optional) Parameter to specify whether to include a
               list of conflicted revisions in the `_conflicts` property of the returned
               document. Ignored if `include_docs` isn't `true`.
        :param bool descending: (optional) Parameter to specify whether to return
               the documents in descending by key order.
        :param bool include_docs: (optional) Parameter to specify whether to
               include the full content of the documents in the response.
        :param bool inclusive_end: (optional) Parameter to specify whether the
               specified end key should be included in the result.
        :param int limit: (optional) Parameter to specify the number of returned
               documents to limit the result to.
        :param int skip: (optional) Parameter to specify the number of records
               before starting to return the results.
        :param bool update_seq: (optional) Parameter to specify whether to include
               in the response an update_seq value indicating the sequence id of the
               database the view reflects.
        :param object endkey: (optional) Schema for any JSON type.
        :param str endkey_docid: (optional) Schema for a document ID.
        :param bool group: (optional) Parameter to specify whether to group the
               results using the reduce function to a group rather than a single row.
               Implies reduce is true and the maximum group_level.
        :param int group_level: (optional) Parameter to specify the group level to
               be used. Implies group is true.
        :param object key: (optional) Schema for any JSON type.
        :param List[object] keys: (optional) Parameter to specify to return only
               documents that match the specified keys. String representation of a JSON
               array containing elements that match the key type emitted by the view
               function.
        :param bool reduce: (optional) Parameter to specify whether to use the
               reduce function in a map-reduce view. Default is true when a reduce
               function is defined.
        :param bool stable: (optional) Parameter to specify whether view results
               should be returned from a stable set of shards.
        :param object startkey: (optional) Schema for any JSON type.
        :param str startkey_docid: (optional) Schema for a document ID.
        :param str update: (optional) Parameter to specify whether or not the view
               in question should be updated prior to responding to the user.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        if view is None:
            raise ValueError('view must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_view_as_stream')
        headers.update(sdk_headers)

        data = {
            'att_encoding_info': att_encoding_info,
            'attachments': attachments,
            'conflicts': conflicts,
            'descending': descending,
            'include_docs': include_docs,
            'inclusive_end': inclusive_end,
            'limit': limit,
            'skip': skip,
            'update_seq': update_seq,
            'endkey': endkey,
            'endkey_docid': endkey_docid,
            'group': group,
            'group_level': group_level,
            'key': key,
            'keys': keys,
            'reduce': reduce,
            'stable': stable,
            'startkey': startkey,
            'startkey_docid': startkey_docid,
            'update': update
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_design/{1}/_view/{2}'.format(
            *self.encode_path_vars(db, ddoc, view))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, stream=True)
        return response


    def post_view_queries(self,
        db: str,
        ddoc: str,
        view: str,
        *,
        queries: List['ViewQuery'] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Multi-query a MapReduce view.

        This operation runs multiple specified view queries against the view function from
        the specified design document.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str view: Path parameter to specify the map reduce view function
               name.
        :param List[ViewQuery] queries: (optional) An array of query objects with
               fields for the parameters of each individual view query to be executed. The
               field names and their meaning are the same as the query parameters of a
               regular view request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ViewQueriesResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        if view is None:
            raise ValueError('view must be provided')
        if queries is not None:
            queries = [convert_model(x) for x in queries]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_view_queries')
        headers.update(sdk_headers)

        data = {
            'queries': queries
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_design/{1}/_view/{2}/queries'.format(
            *self.encode_path_vars(db, ddoc, view))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_view_queries_as_stream(self,
        db: str,
        ddoc: str,
        view: str,
        *,
        queries: List['ViewQuery'] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Multi-query a MapReduce view as stream.

        This operation runs multiple specified view queries against the view function from
        the specified design document.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str view: Path parameter to specify the map reduce view function
               name.
        :param List[ViewQuery] queries: (optional) An array of query objects with
               fields for the parameters of each individual view query to be executed. The
               field names and their meaning are the same as the query parameters of a
               regular view request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        if view is None:
            raise ValueError('view must be provided')
        if queries is not None:
            queries = [convert_model(x) for x in queries]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_view_queries_as_stream')
        headers.update(sdk_headers)

        data = {
            'queries': queries
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_design/{1}/_view/{2}/queries'.format(
            *self.encode_path_vars(db, ddoc, view))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, stream=True)
        return response

    #########################
    # Queries
    #########################


    def get_partition_information(self,
        db: str,
        partition_key: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve information about a database partition.

        Given a partition key, return the database name, sizes, partition, doc count, and
        doc delete count.

        :param str db: Path parameter to specify the database name.
        :param str partition_key: Path parameter to specify the database partition
               key.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PartitionInformation` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if partition_key is None:
            raise ValueError('partition_key must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_partition_information')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_partition/{1}'.format(
            *self.encode_path_vars(db, partition_key))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def post_partition_all_docs(self,
        db: str,
        partition_key: str,
        *,
        att_encoding_info: bool = None,
        attachments: bool = None,
        conflicts: bool = None,
        descending: bool = None,
        include_docs: bool = None,
        inclusive_end: bool = None,
        limit: int = None,
        skip: int = None,
        update_seq: bool = None,
        endkey: str = None,
        key: str = None,
        keys: List[str] = None,
        startkey: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a list of all documents in a database partition.

        Queries the primary index (all document IDs). The results that match the query
        parameters are returned in a JSON object, including a list of matching documents
        with basic contents, such as the ID and revision. When no query parameters are
        specified, results for all documents in the database partition are returned.
        Optionally, document content or additional metadata can be included in the
        response.

        :param str db: Path parameter to specify the database name.
        :param str partition_key: Path parameter to specify the database partition
               key.
        :param bool att_encoding_info: (optional) Parameter to specify whether to
               include the encoding information in attachment stubs if the particular
               attachment is compressed.
        :param bool attachments: (optional) Parameter to specify whether to include
               attachments bodies in a response.
        :param bool conflicts: (optional) Parameter to specify whether to include a
               list of conflicted revisions in the `_conflicts` property of the returned
               document. Ignored if `include_docs` isn't `true`.
        :param bool descending: (optional) Parameter to specify whether to return
               the documents in descending by key order.
        :param bool include_docs: (optional) Parameter to specify whether to
               include the full content of the documents in the response.
        :param bool inclusive_end: (optional) Parameter to specify whether the
               specified end key should be included in the result.
        :param int limit: (optional) Parameter to specify the number of returned
               documents to limit the result to.
        :param int skip: (optional) Parameter to specify the number of records
               before starting to return the results.
        :param bool update_seq: (optional) Parameter to specify whether to include
               in the response an update_seq value indicating the sequence id of the
               database the view reflects.
        :param str endkey: (optional) Schema for a document ID.
        :param str key: (optional) Schema for a document ID.
        :param List[str] keys: (optional) Schema for a list of document IDs.
        :param str startkey: (optional) Schema for a document ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllDocsResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if partition_key is None:
            raise ValueError('partition_key must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_partition_all_docs')
        headers.update(sdk_headers)

        data = {
            'att_encoding_info': att_encoding_info,
            'attachments': attachments,
            'conflicts': conflicts,
            'descending': descending,
            'include_docs': include_docs,
            'inclusive_end': inclusive_end,
            'limit': limit,
            'skip': skip,
            'update_seq': update_seq,
            'endkey': endkey,
            'key': key,
            'keys': keys,
            'startkey': startkey
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_partition/{1}/_all_docs'.format(
            *self.encode_path_vars(db, partition_key))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_partition_all_docs_as_stream(self,
        db: str,
        partition_key: str,
        *,
        att_encoding_info: bool = None,
        attachments: bool = None,
        conflicts: bool = None,
        descending: bool = None,
        include_docs: bool = None,
        inclusive_end: bool = None,
        limit: int = None,
        skip: int = None,
        update_seq: bool = None,
        endkey: str = None,
        key: str = None,
        keys: List[str] = None,
        startkey: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a list of all documents in a database partition as stream.

        Queries the primary index (all document IDs). The results that match the query
        parameters are returned in a JSON object, including a list of matching documents
        with basic contents, such as the ID and revision. When no query parameters are
        specified, results for all documents in the database partition are returned.
        Optionally, document content or additional metadata can be included in the
        response.

        :param str db: Path parameter to specify the database name.
        :param str partition_key: Path parameter to specify the database partition
               key.
        :param bool att_encoding_info: (optional) Parameter to specify whether to
               include the encoding information in attachment stubs if the particular
               attachment is compressed.
        :param bool attachments: (optional) Parameter to specify whether to include
               attachments bodies in a response.
        :param bool conflicts: (optional) Parameter to specify whether to include a
               list of conflicted revisions in the `_conflicts` property of the returned
               document. Ignored if `include_docs` isn't `true`.
        :param bool descending: (optional) Parameter to specify whether to return
               the documents in descending by key order.
        :param bool include_docs: (optional) Parameter to specify whether to
               include the full content of the documents in the response.
        :param bool inclusive_end: (optional) Parameter to specify whether the
               specified end key should be included in the result.
        :param int limit: (optional) Parameter to specify the number of returned
               documents to limit the result to.
        :param int skip: (optional) Parameter to specify the number of records
               before starting to return the results.
        :param bool update_seq: (optional) Parameter to specify whether to include
               in the response an update_seq value indicating the sequence id of the
               database the view reflects.
        :param str endkey: (optional) Schema for a document ID.
        :param str key: (optional) Schema for a document ID.
        :param List[str] keys: (optional) Schema for a list of document IDs.
        :param str startkey: (optional) Schema for a document ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if partition_key is None:
            raise ValueError('partition_key must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_partition_all_docs_as_stream')
        headers.update(sdk_headers)

        data = {
            'att_encoding_info': att_encoding_info,
            'attachments': attachments,
            'conflicts': conflicts,
            'descending': descending,
            'include_docs': include_docs,
            'inclusive_end': inclusive_end,
            'limit': limit,
            'skip': skip,
            'update_seq': update_seq,
            'endkey': endkey,
            'key': key,
            'keys': keys,
            'startkey': startkey
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_partition/{1}/_all_docs'.format(
            *self.encode_path_vars(db, partition_key))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, stream=True)
        return response


    def post_partition_search(self,
        db: str,
        partition_key: str,
        ddoc: str,
        index: str,
        *,
        query: str = None,
        bookmark: str = None,
        highlight_fields: List[str] = None,
        highlight_number: int = None,
        highlight_post_tag: str = None,
        highlight_pre_tag: str = None,
        highlight_size: int = None,
        include_docs: bool = None,
        include_fields: List[str] = None,
        limit: int = None,
        sort: List[str] = None,
        stale: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a database partition search index.

        Partitioned Search indexes, which are defined in design documents, allow partition
        databases to be queried by using Lucene Query Parser Syntax. Search indexes are
        defined by an index function, similar to a map function in MapReduce views. The
        index function decides what data to index and store in the index.

        :param str db: Path parameter to specify the database name.
        :param str partition_key: Path parameter to specify the database partition
               key.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str index: Path parameter to specify the index name.
        :param str query: (optional) The Lucene query to execute.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param List[str] highlight_fields: (optional) Specifies which fields to
               highlight. If specified, the result object contains a highlights field with
               an entry for each specified field.
        :param int highlight_number: (optional) Number of fragments that are
               returned in highlights. If the search term occurs less often than the
               number of fragments that are specified, longer fragments are returned.
        :param str highlight_post_tag: (optional) A string that is inserted after
               the highlighted word in the highlights output.
        :param str highlight_pre_tag: (optional) A string that is inserted before
               the highlighted word in the highlights output.
        :param int highlight_size: (optional) Number of characters in each fragment
               for highlights.
        :param bool include_docs: (optional) Include the full content of the
               documents in the return.
        :param List[str] include_fields: (optional) A JSON array of field names to
               include in search results. Any fields that are included must be indexed
               with the store:true option. The default is all fields.
        :param int limit: (optional) Limit the number of the returned documents to
               the specified number.
        :param List[str] sort: (optional) Specifies the sort order of the results.
               In a grouped search (when group_field is used), this parameter specifies
               the sort order within a group. The default sort order is relevance.  A JSON
               string of the form "fieldname&lt;type&gt;" or "-fieldname&lt;type&gt;" for
               descending order, where fieldname is the name of a string or number field,
               and type is either a number, a string, or a JSON array of strings. The type
               part is optional, and defaults to number. Some examples are "foo", "-foo",
               "bar&lt;string&gt;", "-foo&lt;number&gt;" and ["-foo&lt;number&gt;",
               "bar&lt;string&gt;"]. String fields that are used for sorting must not be
               analyzed fields. Fields that are used for sorting must be indexed by the
               same indexer that is used for the search query.
        :param str stale: (optional) Do not wait for the index to finish building
               to return results.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SearchResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if partition_key is None:
            raise ValueError('partition_key must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        if index is None:
            raise ValueError('index must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_partition_search')
        headers.update(sdk_headers)

        data = {
            'query': query,
            'bookmark': bookmark,
            'highlight_fields': highlight_fields,
            'highlight_number': highlight_number,
            'highlight_post_tag': highlight_post_tag,
            'highlight_pre_tag': highlight_pre_tag,
            'highlight_size': highlight_size,
            'include_docs': include_docs,
            'include_fields': include_fields,
            'limit': limit,
            'sort': sort,
            'stale': stale
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_partition/{1}/_design/{2}/_search/{3}'.format(
            *self.encode_path_vars(db, partition_key, ddoc, index))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_partition_search_as_stream(self,
        db: str,
        partition_key: str,
        ddoc: str,
        index: str,
        *,
        query: str = None,
        bookmark: str = None,
        highlight_fields: List[str] = None,
        highlight_number: int = None,
        highlight_post_tag: str = None,
        highlight_pre_tag: str = None,
        highlight_size: int = None,
        include_docs: bool = None,
        include_fields: List[str] = None,
        limit: int = None,
        sort: List[str] = None,
        stale: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a database partition search index as stream.

        Partitioned Search indexes, which are defined in design documents, allow partition
        databases to be queried by using Lucene Query Parser Syntax. Search indexes are
        defined by an index function, similar to a map function in MapReduce views. The
        index function decides what data to index and store in the index.

        :param str db: Path parameter to specify the database name.
        :param str partition_key: Path parameter to specify the database partition
               key.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str index: Path parameter to specify the index name.
        :param str query: (optional) The Lucene query to execute.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param List[str] highlight_fields: (optional) Specifies which fields to
               highlight. If specified, the result object contains a highlights field with
               an entry for each specified field.
        :param int highlight_number: (optional) Number of fragments that are
               returned in highlights. If the search term occurs less often than the
               number of fragments that are specified, longer fragments are returned.
        :param str highlight_post_tag: (optional) A string that is inserted after
               the highlighted word in the highlights output.
        :param str highlight_pre_tag: (optional) A string that is inserted before
               the highlighted word in the highlights output.
        :param int highlight_size: (optional) Number of characters in each fragment
               for highlights.
        :param bool include_docs: (optional) Include the full content of the
               documents in the return.
        :param List[str] include_fields: (optional) A JSON array of field names to
               include in search results. Any fields that are included must be indexed
               with the store:true option. The default is all fields.
        :param int limit: (optional) Limit the number of the returned documents to
               the specified number.
        :param List[str] sort: (optional) Specifies the sort order of the results.
               In a grouped search (when group_field is used), this parameter specifies
               the sort order within a group. The default sort order is relevance.  A JSON
               string of the form "fieldname&lt;type&gt;" or "-fieldname&lt;type&gt;" for
               descending order, where fieldname is the name of a string or number field,
               and type is either a number, a string, or a JSON array of strings. The type
               part is optional, and defaults to number. Some examples are "foo", "-foo",
               "bar&lt;string&gt;", "-foo&lt;number&gt;" and ["-foo&lt;number&gt;",
               "bar&lt;string&gt;"]. String fields that are used for sorting must not be
               analyzed fields. Fields that are used for sorting must be indexed by the
               same indexer that is used for the search query.
        :param str stale: (optional) Do not wait for the index to finish building
               to return results.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if partition_key is None:
            raise ValueError('partition_key must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        if index is None:
            raise ValueError('index must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_partition_search_as_stream')
        headers.update(sdk_headers)

        data = {
            'query': query,
            'bookmark': bookmark,
            'highlight_fields': highlight_fields,
            'highlight_number': highlight_number,
            'highlight_post_tag': highlight_post_tag,
            'highlight_pre_tag': highlight_pre_tag,
            'highlight_size': highlight_size,
            'include_docs': include_docs,
            'include_fields': include_fields,
            'limit': limit,
            'sort': sort,
            'stale': stale
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_partition/{1}/_design/{2}/_search/{3}'.format(
            *self.encode_path_vars(db, partition_key, ddoc, index))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, stream=True)
        return response


    def post_partition_view(self,
        db: str,
        partition_key: str,
        ddoc: str,
        view: str,
        *,
        att_encoding_info: bool = None,
        attachments: bool = None,
        conflicts: bool = None,
        descending: bool = None,
        include_docs: bool = None,
        inclusive_end: bool = None,
        limit: int = None,
        skip: int = None,
        update_seq: bool = None,
        endkey: object = None,
        endkey_docid: str = None,
        group: bool = None,
        group_level: int = None,
        key: object = None,
        keys: List[object] = None,
        reduce: bool = None,
        stable: bool = None,
        startkey: object = None,
        startkey_docid: str = None,
        update: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a database partition MapReduce view function.

        Runs the specified view function from the specified design document. Unlike `GET
        /{db}/_design/{ddoc}/_view/{view}` for accessing views, the POST method supports
        the specification of explicit keys to be retrieved from the view results. The
        remainder of the POST view functionality is identical to the `GET
        /{db}/_design/{ddoc}/_view/{view}` API.

        :param str db: Path parameter to specify the database name.
        :param str partition_key: Path parameter to specify the database partition
               key.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str view: Path parameter to specify the map reduce view function
               name.
        :param bool att_encoding_info: (optional) Parameter to specify whether to
               include the encoding information in attachment stubs if the particular
               attachment is compressed.
        :param bool attachments: (optional) Parameter to specify whether to include
               attachments bodies in a response.
        :param bool conflicts: (optional) Parameter to specify whether to include a
               list of conflicted revisions in the `_conflicts` property of the returned
               document. Ignored if `include_docs` isn't `true`.
        :param bool descending: (optional) Parameter to specify whether to return
               the documents in descending by key order.
        :param bool include_docs: (optional) Parameter to specify whether to
               include the full content of the documents in the response.
        :param bool inclusive_end: (optional) Parameter to specify whether the
               specified end key should be included in the result.
        :param int limit: (optional) Parameter to specify the number of returned
               documents to limit the result to.
        :param int skip: (optional) Parameter to specify the number of records
               before starting to return the results.
        :param bool update_seq: (optional) Parameter to specify whether to include
               in the response an update_seq value indicating the sequence id of the
               database the view reflects.
        :param object endkey: (optional) Schema for any JSON type.
        :param str endkey_docid: (optional) Schema for a document ID.
        :param bool group: (optional) Parameter to specify whether to group the
               results using the reduce function to a group rather than a single row.
               Implies reduce is true and the maximum group_level.
        :param int group_level: (optional) Parameter to specify the group level to
               be used. Implies group is true.
        :param object key: (optional) Schema for any JSON type.
        :param List[object] keys: (optional) Parameter to specify to return only
               documents that match the specified keys. String representation of a JSON
               array containing elements that match the key type emitted by the view
               function.
        :param bool reduce: (optional) Parameter to specify whether to use the
               reduce function in a map-reduce view. Default is true when a reduce
               function is defined.
        :param bool stable: (optional) Parameter to specify whether view results
               should be returned from a stable set of shards.
        :param object startkey: (optional) Schema for any JSON type.
        :param str startkey_docid: (optional) Schema for a document ID.
        :param str update: (optional) Parameter to specify whether or not the view
               in question should be updated prior to responding to the user.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ViewResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if partition_key is None:
            raise ValueError('partition_key must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        if view is None:
            raise ValueError('view must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_partition_view')
        headers.update(sdk_headers)

        data = {
            'att_encoding_info': att_encoding_info,
            'attachments': attachments,
            'conflicts': conflicts,
            'descending': descending,
            'include_docs': include_docs,
            'inclusive_end': inclusive_end,
            'limit': limit,
            'skip': skip,
            'update_seq': update_seq,
            'endkey': endkey,
            'endkey_docid': endkey_docid,
            'group': group,
            'group_level': group_level,
            'key': key,
            'keys': keys,
            'reduce': reduce,
            'stable': stable,
            'startkey': startkey,
            'startkey_docid': startkey_docid,
            'update': update
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_partition/{1}/_design/{2}/_view/{3}'.format(
            *self.encode_path_vars(db, partition_key, ddoc, view))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_partition_view_as_stream(self,
        db: str,
        partition_key: str,
        ddoc: str,
        view: str,
        *,
        att_encoding_info: bool = None,
        attachments: bool = None,
        conflicts: bool = None,
        descending: bool = None,
        include_docs: bool = None,
        inclusive_end: bool = None,
        limit: int = None,
        skip: int = None,
        update_seq: bool = None,
        endkey: object = None,
        endkey_docid: str = None,
        group: bool = None,
        group_level: int = None,
        key: object = None,
        keys: List[object] = None,
        reduce: bool = None,
        stable: bool = None,
        startkey: object = None,
        startkey_docid: str = None,
        update: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a database partition MapReduce view function as stream.

        Runs the specified view function from the specified design document. Unlike `GET
        /{db}/_design/{ddoc}/_view/{view}` for accessing views, the POST method supports
        the specification of explicit keys to be retrieved from the view results. The
        remainder of the POST view functionality is identical to the `GET
        /{db}/_design/{ddoc}/_view/{view}` API.

        :param str db: Path parameter to specify the database name.
        :param str partition_key: Path parameter to specify the database partition
               key.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str view: Path parameter to specify the map reduce view function
               name.
        :param bool att_encoding_info: (optional) Parameter to specify whether to
               include the encoding information in attachment stubs if the particular
               attachment is compressed.
        :param bool attachments: (optional) Parameter to specify whether to include
               attachments bodies in a response.
        :param bool conflicts: (optional) Parameter to specify whether to include a
               list of conflicted revisions in the `_conflicts` property of the returned
               document. Ignored if `include_docs` isn't `true`.
        :param bool descending: (optional) Parameter to specify whether to return
               the documents in descending by key order.
        :param bool include_docs: (optional) Parameter to specify whether to
               include the full content of the documents in the response.
        :param bool inclusive_end: (optional) Parameter to specify whether the
               specified end key should be included in the result.
        :param int limit: (optional) Parameter to specify the number of returned
               documents to limit the result to.
        :param int skip: (optional) Parameter to specify the number of records
               before starting to return the results.
        :param bool update_seq: (optional) Parameter to specify whether to include
               in the response an update_seq value indicating the sequence id of the
               database the view reflects.
        :param object endkey: (optional) Schema for any JSON type.
        :param str endkey_docid: (optional) Schema for a document ID.
        :param bool group: (optional) Parameter to specify whether to group the
               results using the reduce function to a group rather than a single row.
               Implies reduce is true and the maximum group_level.
        :param int group_level: (optional) Parameter to specify the group level to
               be used. Implies group is true.
        :param object key: (optional) Schema for any JSON type.
        :param List[object] keys: (optional) Parameter to specify to return only
               documents that match the specified keys. String representation of a JSON
               array containing elements that match the key type emitted by the view
               function.
        :param bool reduce: (optional) Parameter to specify whether to use the
               reduce function in a map-reduce view. Default is true when a reduce
               function is defined.
        :param bool stable: (optional) Parameter to specify whether view results
               should be returned from a stable set of shards.
        :param object startkey: (optional) Schema for any JSON type.
        :param str startkey_docid: (optional) Schema for a document ID.
        :param str update: (optional) Parameter to specify whether or not the view
               in question should be updated prior to responding to the user.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if partition_key is None:
            raise ValueError('partition_key must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        if view is None:
            raise ValueError('view must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_partition_view_as_stream')
        headers.update(sdk_headers)

        data = {
            'att_encoding_info': att_encoding_info,
            'attachments': attachments,
            'conflicts': conflicts,
            'descending': descending,
            'include_docs': include_docs,
            'inclusive_end': inclusive_end,
            'limit': limit,
            'skip': skip,
            'update_seq': update_seq,
            'endkey': endkey,
            'endkey_docid': endkey_docid,
            'group': group,
            'group_level': group_level,
            'key': key,
            'keys': keys,
            'reduce': reduce,
            'stable': stable,
            'startkey': startkey,
            'startkey_docid': startkey_docid,
            'update': update
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_partition/{1}/_design/{2}/_view/{3}'.format(
            *self.encode_path_vars(db, partition_key, ddoc, view))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, stream=True)
        return response


    def post_partition_find(self,
        db: str,
        partition_key: str,
        *,
        selector: dict = None,
        bookmark: str = None,
        conflicts: bool = None,
        execution_stats: bool = None,
        fields: List[str] = None,
        limit: int = None,
        skip: int = None,
        sort: List[dict] = None,
        stable: bool = None,
        update: str = None,
        use_index: List[str] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a database partition index by using selector syntax (POST).

        Query documents by using a declarative JSON querying syntax. Queries can use the
        built-in `_all_docs` index or custom indices, specified by using the `_index`
        endpoint.

        :param str db: Path parameter to specify the database name.
        :param str partition_key: Path parameter to specify the database partition
               key.
        :param dict selector: (optional) JSON object describing criteria used to
               select documents. The selector specifies fields in the document, and
               provides an expression to evaluate with the field content or other data.
               The selector object must:
                 * Be structured as valid JSON.
                 * Contain a valid query expression.
               Using a selector is significantly more efficient than using a JavaScript
               filter function, and is the recommended option if filtering on document
               attributes only.
               Elementary selector syntax requires you to specify one or more fields, and
               the corresponding values required for those fields. You can create more
               complex selector expressions by combining operators.
               Operators are identified by the use of a dollar sign `$` prefix in the name
               field.
               There are two core types of operators in the selector syntax:
               * Combination operators: applied at the topmost level of selection. They
               are used to combine selectors. In addition to the common boolean operators
               (`$and`, `$or`, `$not`, `$nor`) there are three combination operators:
               `$all`, `$elemMatch`, and `$allMatch`. A combination operator takes a
               single argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param bool conflicts: (optional) A boolean value that indicates whether or
               not to include information about existing conflicts in the document.
        :param bool execution_stats: (optional) Use this option to find information
               about the query that was run. This information includes total key lookups,
               total document lookups (when `include_docs=true` is used), and total quorum
               document lookups (when each document replica is fetched).
        :param List[str] fields: (optional) JSON array that uses the field syntax
               as described in the following information. Use this parameter to specify
               which fields of a document must be returned. If it is omitted, the entire
               document is returned.
        :param int limit: (optional) Maximum number of results returned. The `type:
               text` indexes are limited to 200 results when queried.
        :param int skip: (optional) Skip the first 'n' results, where 'n' is the
               value that is specified.
        :param List[dict] sort: (optional) JSON array of sort syntax elements to
               determine the sort order of the results.
        :param bool stable: (optional) Whether or not the view results should be
               returned from a "stable" set of shards.
        :param str update: (optional) Whether to update the index prior to
               returning the result.
        :param List[str] use_index: (optional) Use this option to identify a
               specific index for query to run against, rather than by using the IBM
               Cloudant Query algorithm to find the best index.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `FindResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if partition_key is None:
            raise ValueError('partition_key must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_partition_find')
        headers.update(sdk_headers)

        data = {
            'selector': selector,
            'bookmark': bookmark,
            'conflicts': conflicts,
            'execution_stats': execution_stats,
            'fields': fields,
            'limit': limit,
            'skip': skip,
            'sort': sort,
            'stable': stable,
            'update': update,
            'use_index': use_index
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_partition/{1}/_find'.format(
            *self.encode_path_vars(db, partition_key))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_partition_find_as_stream(self,
        db: str,
        partition_key: str,
        *,
        selector: dict = None,
        bookmark: str = None,
        conflicts: bool = None,
        execution_stats: bool = None,
        fields: List[str] = None,
        limit: int = None,
        skip: int = None,
        sort: List[dict] = None,
        stable: bool = None,
        update: str = None,
        use_index: List[str] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a database partition index by using selector syntax (POST) as stream.

        Query documents by using a declarative JSON querying syntax. Queries can use the
        built-in `_all_docs` index or custom indices, specified by using the `_index`
        endpoint.

        :param str db: Path parameter to specify the database name.
        :param str partition_key: Path parameter to specify the database partition
               key.
        :param dict selector: (optional) JSON object describing criteria used to
               select documents. The selector specifies fields in the document, and
               provides an expression to evaluate with the field content or other data.
               The selector object must:
                 * Be structured as valid JSON.
                 * Contain a valid query expression.
               Using a selector is significantly more efficient than using a JavaScript
               filter function, and is the recommended option if filtering on document
               attributes only.
               Elementary selector syntax requires you to specify one or more fields, and
               the corresponding values required for those fields. You can create more
               complex selector expressions by combining operators.
               Operators are identified by the use of a dollar sign `$` prefix in the name
               field.
               There are two core types of operators in the selector syntax:
               * Combination operators: applied at the topmost level of selection. They
               are used to combine selectors. In addition to the common boolean operators
               (`$and`, `$or`, `$not`, `$nor`) there are three combination operators:
               `$all`, `$elemMatch`, and `$allMatch`. A combination operator takes a
               single argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param bool conflicts: (optional) A boolean value that indicates whether or
               not to include information about existing conflicts in the document.
        :param bool execution_stats: (optional) Use this option to find information
               about the query that was run. This information includes total key lookups,
               total document lookups (when `include_docs=true` is used), and total quorum
               document lookups (when each document replica is fetched).
        :param List[str] fields: (optional) JSON array that uses the field syntax
               as described in the following information. Use this parameter to specify
               which fields of a document must be returned. If it is omitted, the entire
               document is returned.
        :param int limit: (optional) Maximum number of results returned. The `type:
               text` indexes are limited to 200 results when queried.
        :param int skip: (optional) Skip the first 'n' results, where 'n' is the
               value that is specified.
        :param List[dict] sort: (optional) JSON array of sort syntax elements to
               determine the sort order of the results.
        :param bool stable: (optional) Whether or not the view results should be
               returned from a "stable" set of shards.
        :param str update: (optional) Whether to update the index prior to
               returning the result.
        :param List[str] use_index: (optional) Use this option to identify a
               specific index for query to run against, rather than by using the IBM
               Cloudant Query algorithm to find the best index.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if partition_key is None:
            raise ValueError('partition_key must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_partition_find_as_stream')
        headers.update(sdk_headers)

        data = {
            'selector': selector,
            'bookmark': bookmark,
            'conflicts': conflicts,
            'execution_stats': execution_stats,
            'fields': fields,
            'limit': limit,
            'skip': skip,
            'sort': sort,
            'stable': stable,
            'update': update,
            'use_index': use_index
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_partition/{1}/_find'.format(
            *self.encode_path_vars(db, partition_key))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, stream=True)
        return response

    #########################
    # Queries
    #########################


    def post_explain(self,
        db: str,
        *,
        selector: dict = None,
        bookmark: str = None,
        conflicts: bool = None,
        execution_stats: bool = None,
        fields: List[str] = None,
        limit: int = None,
        skip: int = None,
        sort: List[dict] = None,
        stable: bool = None,
        update: str = None,
        use_index: List[str] = None,
        r: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve information about which index is used for a query.

        Shows which index is being used by the query. Parameters are the same as the
        [`_find` endpoint](#query-an-index-by-using-selector-syntax.

        :param str db: Path parameter to specify the database name.
        :param dict selector: (optional) JSON object describing criteria used to
               select documents. The selector specifies fields in the document, and
               provides an expression to evaluate with the field content or other data.
               The selector object must:
                 * Be structured as valid JSON.
                 * Contain a valid query expression.
               Using a selector is significantly more efficient than using a JavaScript
               filter function, and is the recommended option if filtering on document
               attributes only.
               Elementary selector syntax requires you to specify one or more fields, and
               the corresponding values required for those fields. You can create more
               complex selector expressions by combining operators.
               Operators are identified by the use of a dollar sign `$` prefix in the name
               field.
               There are two core types of operators in the selector syntax:
               * Combination operators: applied at the topmost level of selection. They
               are used to combine selectors. In addition to the common boolean operators
               (`$and`, `$or`, `$not`, `$nor`) there are three combination operators:
               `$all`, `$elemMatch`, and `$allMatch`. A combination operator takes a
               single argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param bool conflicts: (optional) A boolean value that indicates whether or
               not to include information about existing conflicts in the document.
        :param bool execution_stats: (optional) Use this option to find information
               about the query that was run. This information includes total key lookups,
               total document lookups (when `include_docs=true` is used), and total quorum
               document lookups (when each document replica is fetched).
        :param List[str] fields: (optional) JSON array that uses the field syntax
               as described in the following information. Use this parameter to specify
               which fields of a document must be returned. If it is omitted, the entire
               document is returned.
        :param int limit: (optional) Maximum number of results returned. The `type:
               text` indexes are limited to 200 results when queried.
        :param int skip: (optional) Skip the first 'n' results, where 'n' is the
               value that is specified.
        :param List[dict] sort: (optional) JSON array of sort syntax elements to
               determine the sort order of the results.
        :param bool stable: (optional) Whether or not the view results should be
               returned from a "stable" set of shards.
        :param str update: (optional) Whether to update the index prior to
               returning the result.
        :param List[str] use_index: (optional) Use this option to identify a
               specific index for query to run against, rather than by using the IBM
               Cloudant Query algorithm to find the best index.
        :param int r: (optional) The read quorum that is needed for the result. The
               value defaults to 1, in which case the document that was found in the index
               is returned. If set to a higher value, each document is read from at least
               that many replicas before it is returned in the results. The request will
               take more time than using only the document that is stored locally with the
               index.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ExplainResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_explain')
        headers.update(sdk_headers)

        data = {
            'selector': selector,
            'bookmark': bookmark,
            'conflicts': conflicts,
            'execution_stats': execution_stats,
            'fields': fields,
            'limit': limit,
            'skip': skip,
            'sort': sort,
            'stable': stable,
            'update': update,
            'use_index': use_index,
            'r': r
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_explain'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_find(self,
        db: str,
        *,
        selector: dict = None,
        bookmark: str = None,
        conflicts: bool = None,
        execution_stats: bool = None,
        fields: List[str] = None,
        limit: int = None,
        skip: int = None,
        sort: List[dict] = None,
        stable: bool = None,
        update: str = None,
        use_index: List[str] = None,
        r: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query an index by using selector syntax.

        Query documents by using a declarative JSON querying syntax. Queries can use the
        built-in `_all_docs` index or custom indices, specified by using the `_index`
        endpoint.

        :param str db: Path parameter to specify the database name.
        :param dict selector: (optional) JSON object describing criteria used to
               select documents. The selector specifies fields in the document, and
               provides an expression to evaluate with the field content or other data.
               The selector object must:
                 * Be structured as valid JSON.
                 * Contain a valid query expression.
               Using a selector is significantly more efficient than using a JavaScript
               filter function, and is the recommended option if filtering on document
               attributes only.
               Elementary selector syntax requires you to specify one or more fields, and
               the corresponding values required for those fields. You can create more
               complex selector expressions by combining operators.
               Operators are identified by the use of a dollar sign `$` prefix in the name
               field.
               There are two core types of operators in the selector syntax:
               * Combination operators: applied at the topmost level of selection. They
               are used to combine selectors. In addition to the common boolean operators
               (`$and`, `$or`, `$not`, `$nor`) there are three combination operators:
               `$all`, `$elemMatch`, and `$allMatch`. A combination operator takes a
               single argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param bool conflicts: (optional) A boolean value that indicates whether or
               not to include information about existing conflicts in the document.
        :param bool execution_stats: (optional) Use this option to find information
               about the query that was run. This information includes total key lookups,
               total document lookups (when `include_docs=true` is used), and total quorum
               document lookups (when each document replica is fetched).
        :param List[str] fields: (optional) JSON array that uses the field syntax
               as described in the following information. Use this parameter to specify
               which fields of a document must be returned. If it is omitted, the entire
               document is returned.
        :param int limit: (optional) Maximum number of results returned. The `type:
               text` indexes are limited to 200 results when queried.
        :param int skip: (optional) Skip the first 'n' results, where 'n' is the
               value that is specified.
        :param List[dict] sort: (optional) JSON array of sort syntax elements to
               determine the sort order of the results.
        :param bool stable: (optional) Whether or not the view results should be
               returned from a "stable" set of shards.
        :param str update: (optional) Whether to update the index prior to
               returning the result.
        :param List[str] use_index: (optional) Use this option to identify a
               specific index for query to run against, rather than by using the IBM
               Cloudant Query algorithm to find the best index.
        :param int r: (optional) The read quorum that is needed for the result. The
               value defaults to 1, in which case the document that was found in the index
               is returned. If set to a higher value, each document is read from at least
               that many replicas before it is returned in the results. The request will
               take more time than using only the document that is stored locally with the
               index.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `FindResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_find')
        headers.update(sdk_headers)

        data = {
            'selector': selector,
            'bookmark': bookmark,
            'conflicts': conflicts,
            'execution_stats': execution_stats,
            'fields': fields,
            'limit': limit,
            'skip': skip,
            'sort': sort,
            'stable': stable,
            'update': update,
            'use_index': use_index,
            'r': r
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_find'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_find_as_stream(self,
        db: str,
        *,
        selector: dict = None,
        bookmark: str = None,
        conflicts: bool = None,
        execution_stats: bool = None,
        fields: List[str] = None,
        limit: int = None,
        skip: int = None,
        sort: List[dict] = None,
        stable: bool = None,
        update: str = None,
        use_index: List[str] = None,
        r: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query an index by using selector syntax as stream.

        Query documents by using a declarative JSON querying syntax. Queries can use the
        built-in `_all_docs` index or custom indices, specified by using the `_index`
        endpoint.

        :param str db: Path parameter to specify the database name.
        :param dict selector: (optional) JSON object describing criteria used to
               select documents. The selector specifies fields in the document, and
               provides an expression to evaluate with the field content or other data.
               The selector object must:
                 * Be structured as valid JSON.
                 * Contain a valid query expression.
               Using a selector is significantly more efficient than using a JavaScript
               filter function, and is the recommended option if filtering on document
               attributes only.
               Elementary selector syntax requires you to specify one or more fields, and
               the corresponding values required for those fields. You can create more
               complex selector expressions by combining operators.
               Operators are identified by the use of a dollar sign `$` prefix in the name
               field.
               There are two core types of operators in the selector syntax:
               * Combination operators: applied at the topmost level of selection. They
               are used to combine selectors. In addition to the common boolean operators
               (`$and`, `$or`, `$not`, `$nor`) there are three combination operators:
               `$all`, `$elemMatch`, and `$allMatch`. A combination operator takes a
               single argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param bool conflicts: (optional) A boolean value that indicates whether or
               not to include information about existing conflicts in the document.
        :param bool execution_stats: (optional) Use this option to find information
               about the query that was run. This information includes total key lookups,
               total document lookups (when `include_docs=true` is used), and total quorum
               document lookups (when each document replica is fetched).
        :param List[str] fields: (optional) JSON array that uses the field syntax
               as described in the following information. Use this parameter to specify
               which fields of a document must be returned. If it is omitted, the entire
               document is returned.
        :param int limit: (optional) Maximum number of results returned. The `type:
               text` indexes are limited to 200 results when queried.
        :param int skip: (optional) Skip the first 'n' results, where 'n' is the
               value that is specified.
        :param List[dict] sort: (optional) JSON array of sort syntax elements to
               determine the sort order of the results.
        :param bool stable: (optional) Whether or not the view results should be
               returned from a "stable" set of shards.
        :param str update: (optional) Whether to update the index prior to
               returning the result.
        :param List[str] use_index: (optional) Use this option to identify a
               specific index for query to run against, rather than by using the IBM
               Cloudant Query algorithm to find the best index.
        :param int r: (optional) The read quorum that is needed for the result. The
               value defaults to 1, in which case the document that was found in the index
               is returned. If set to a higher value, each document is read from at least
               that many replicas before it is returned in the results. The request will
               take more time than using only the document that is stored locally with the
               index.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_find_as_stream')
        headers.update(sdk_headers)

        data = {
            'selector': selector,
            'bookmark': bookmark,
            'conflicts': conflicts,
            'execution_stats': execution_stats,
            'fields': fields,
            'limit': limit,
            'skip': skip,
            'sort': sort,
            'stable': stable,
            'update': update,
            'use_index': use_index,
            'r': r
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_find'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, stream=True)
        return response


    def get_indexes_information(self,
        db: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve information about all indexes.

        When you make a GET request to `/db/_index`, you get a list of all indexes used by
        Cloudant Query in the database, including the primary index. In addition to the
        information available through this API, indexes are also stored in the `indexes`
        property of design documents.

        :param str db: Path parameter to specify the database name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IndexesInformation` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_indexes_information')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_index'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def post_index(self,
        db: str,
        *,
        ddoc: str = None,
        def_: 'IndexDefinition' = None,
        index: 'IndexDefinition' = None,
        name: str = None,
        partial_filter_selector: dict = None,
        partitioned: bool = None,
        type: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a new index on a database.

        Create a new index on a database.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: (optional) Name of the design document in which the index
               will be created.
        :param IndexDefinition def_: (optional) Schema for a `json` or `text` query
               index definition. Indexes of type `text` have additional configuration
               properties that do not apply to `json` indexes, these are:
               * `default_analyzer` - the default text analyzer to use * `default_field` -
               whether to index the text in all document fields and what analyzer to use
               for that purpose.
        :param IndexDefinition index: (optional) Schema for a `json` or `text`
               query index definition. Indexes of type `text` have additional
               configuration properties that do not apply to `json` indexes, these are:
               * `default_analyzer` - the default text analyzer to use * `default_field` -
               whether to index the text in all document fields and what analyzer to use
               for that purpose.
        :param str name: (optional) name.
        :param dict partial_filter_selector: (optional) JSON object describing
               criteria used to select documents. The selector specifies fields in the
               document, and provides an expression to evaluate with the field content or
               other data.
               The selector object must:
                 * Be structured as valid JSON.
                 * Contain a valid query expression.
               Using a selector is significantly more efficient than using a JavaScript
               filter function, and is the recommended option if filtering on document
               attributes only.
               Elementary selector syntax requires you to specify one or more fields, and
               the corresponding values required for those fields. You can create more
               complex selector expressions by combining operators.
               Operators are identified by the use of a dollar sign `$` prefix in the name
               field.
               There are two core types of operators in the selector syntax:
               * Combination operators: applied at the topmost level of selection. They
               are used to combine selectors. In addition to the common boolean operators
               (`$and`, `$or`, `$not`, `$nor`) there are three combination operators:
               `$all`, `$elemMatch`, and `$allMatch`. A combination operator takes a
               single argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
        :param bool partitioned: (optional) The default value is `true` for
               databases with `partitioned: true` and `false` otherwise. For databases
               with `partitioned: false` if this option is specified the value must be
               `false`.
        :param str type: (optional) Schema for the type of an index.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IndexResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if def_ is not None:
            def_ = convert_model(def_)
        if index is not None:
            index = convert_model(index)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_index')
        headers.update(sdk_headers)

        data = {
            'ddoc': ddoc,
            'def': def_,
            'index': index,
            'name': name,
            'partial_filter_selector': partial_filter_selector,
            'partitioned': partitioned,
            'type': type
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_index'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_index(self,
        db: str,
        ddoc: str,
        type: str,
        index: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete an index.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str type: Path parameter to specify the index type.
        :param str index: Path parameter to specify the index name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ok` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        if type is None:
            raise ValueError('type must be provided')
        if index is None:
            raise ValueError('index must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_index')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_index/_design/{1}/{2}/{3}'.format(
            *self.encode_path_vars(db, ddoc, type, index))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Searches
    #########################


    def post_search_analyze(self,
        *,
        analyzer: str = None,
        text: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query tokenization of sample text.

        Returns the results of analyzer tokenization of the provided sample text. This
        endpoint can be used for testing analyzer tokenization.

        :param str analyzer: (optional) analyzer.
        :param str text: (optional) text.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SearchAnalyzeResult` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_search_analyze')
        headers.update(sdk_headers)

        data = {
            'analyzer': analyzer,
            'text': text
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_search_analyze'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_search(self,
        db: str,
        ddoc: str,
        index: str,
        *,
        query: str = None,
        bookmark: str = None,
        highlight_fields: List[str] = None,
        highlight_number: int = None,
        highlight_post_tag: str = None,
        highlight_pre_tag: str = None,
        highlight_size: int = None,
        include_docs: bool = None,
        include_fields: List[str] = None,
        limit: int = None,
        sort: List[str] = None,
        stale: str = None,
        counts: List[str] = None,
        drilldown: List[List[str]] = None,
        group_field: str = None,
        group_limit: int = None,
        group_sort: List[str] = None,
        ranges: dict = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a search index.

        Search indexes, which are defined in design documents, allow databases to be
        queried by using Lucene Query Parser Syntax. An index function defines a search
        index, similar to a map function in MapReduce views. The index function decides
        what data to index and what data to store in the index. The advantage of using the
        HTTP `POST` method is that the query is submitted as a JSON object in the request
        body. This avoids the limitations of passing query options as URL query parameters
        of a `GET` request.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str index: Path parameter to specify the index name.
        :param str query: (optional) The Lucene query to execute.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param List[str] highlight_fields: (optional) Specifies which fields to
               highlight. If specified, the result object contains a highlights field with
               an entry for each specified field.
        :param int highlight_number: (optional) Number of fragments that are
               returned in highlights. If the search term occurs less often than the
               number of fragments that are specified, longer fragments are returned.
        :param str highlight_post_tag: (optional) A string that is inserted after
               the highlighted word in the highlights output.
        :param str highlight_pre_tag: (optional) A string that is inserted before
               the highlighted word in the highlights output.
        :param int highlight_size: (optional) Number of characters in each fragment
               for highlights.
        :param bool include_docs: (optional) Include the full content of the
               documents in the return.
        :param List[str] include_fields: (optional) A JSON array of field names to
               include in search results. Any fields that are included must be indexed
               with the store:true option. The default is all fields.
        :param int limit: (optional) Limit the number of the returned documents to
               the specified number.
        :param List[str] sort: (optional) Specifies the sort order of the results.
               In a grouped search (when group_field is used), this parameter specifies
               the sort order within a group. The default sort order is relevance.  A JSON
               string of the form "fieldname&lt;type&gt;" or "-fieldname&lt;type&gt;" for
               descending order, where fieldname is the name of a string or number field,
               and type is either a number, a string, or a JSON array of strings. The type
               part is optional, and defaults to number. Some examples are "foo", "-foo",
               "bar&lt;string&gt;", "-foo&lt;number&gt;" and ["-foo&lt;number&gt;",
               "bar&lt;string&gt;"]. String fields that are used for sorting must not be
               analyzed fields. Fields that are used for sorting must be indexed by the
               same indexer that is used for the search query.
        :param str stale: (optional) Do not wait for the index to finish building
               to return results.
        :param List[str] counts: (optional) This field defines an array of names of
               string fields, for which counts are requested. The response contains counts
               for each unique value of this field name among the documents that match the
               search query. Faceting must be enabled for this parameter to function. This
               option is only available when making global queries.
        :param List[List[str]] drilldown: (optional) Restrict results to documents
               with a dimension equal to the specified label(s). The search matches only
               documents containing the value that was provided in the named field. It
               differs from using "fieldname:value" in the q parameter only in that the
               values are not analyzed. Faceting must be enabled for this parameter to
               function.
        :param str group_field: (optional) Field by which to group search matches.
               A string that contains the name of a string field. Fields containing other
               data such as numbers, objects, or arrays cannot be used. This option is
               only available when making global queries.
        :param int group_limit: (optional) Maximum group count. This field can be
               used only if group_field is specified. This option is only available when
               making global queries.
        :param List[str] group_sort: (optional) This field defines the order of the
               groups in a search that uses group_field. The default sort order is
               relevance. This field can have the same values as the sort field, so single
               fields and arrays of fields are supported. This option is only available
               when making global queries.
        :param dict ranges: (optional) This field defines ranges for faceted,
               numeric search fields. The value is a JSON object where the fields names
               are faceted numeric search fields, and the values of the fields are JSON
               objects. The field names of the JSON objects are names for ranges. The
               values are strings that describe the range, for example "[0 TO 10]". This
               option is only available when making global queries.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SearchResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        if index is None:
            raise ValueError('index must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_search')
        headers.update(sdk_headers)

        data = {
            'query': query,
            'bookmark': bookmark,
            'highlight_fields': highlight_fields,
            'highlight_number': highlight_number,
            'highlight_post_tag': highlight_post_tag,
            'highlight_pre_tag': highlight_pre_tag,
            'highlight_size': highlight_size,
            'include_docs': include_docs,
            'include_fields': include_fields,
            'limit': limit,
            'sort': sort,
            'stale': stale,
            'counts': counts,
            'drilldown': drilldown,
            'group_field': group_field,
            'group_limit': group_limit,
            'group_sort': group_sort,
            'ranges': ranges
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_design/{1}/_search/{2}'.format(
            *self.encode_path_vars(db, ddoc, index))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_search_as_stream(self,
        db: str,
        ddoc: str,
        index: str,
        *,
        query: str = None,
        bookmark: str = None,
        highlight_fields: List[str] = None,
        highlight_number: int = None,
        highlight_post_tag: str = None,
        highlight_pre_tag: str = None,
        highlight_size: int = None,
        include_docs: bool = None,
        include_fields: List[str] = None,
        limit: int = None,
        sort: List[str] = None,
        stale: str = None,
        counts: List[str] = None,
        drilldown: List[List[str]] = None,
        group_field: str = None,
        group_limit: int = None,
        group_sort: List[str] = None,
        ranges: dict = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a search index as stream.

        Search indexes, which are defined in design documents, allow databases to be
        queried by using Lucene Query Parser Syntax. An index function defines a search
        index, similar to a map function in MapReduce views. The index function decides
        what data to index and what data to store in the index. The advantage of using the
        HTTP `POST` method is that the query is submitted as a JSON object in the request
        body. This avoids the limitations of passing query options as URL query parameters
        of a `GET` request.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str index: Path parameter to specify the index name.
        :param str query: (optional) The Lucene query to execute.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param List[str] highlight_fields: (optional) Specifies which fields to
               highlight. If specified, the result object contains a highlights field with
               an entry for each specified field.
        :param int highlight_number: (optional) Number of fragments that are
               returned in highlights. If the search term occurs less often than the
               number of fragments that are specified, longer fragments are returned.
        :param str highlight_post_tag: (optional) A string that is inserted after
               the highlighted word in the highlights output.
        :param str highlight_pre_tag: (optional) A string that is inserted before
               the highlighted word in the highlights output.
        :param int highlight_size: (optional) Number of characters in each fragment
               for highlights.
        :param bool include_docs: (optional) Include the full content of the
               documents in the return.
        :param List[str] include_fields: (optional) A JSON array of field names to
               include in search results. Any fields that are included must be indexed
               with the store:true option. The default is all fields.
        :param int limit: (optional) Limit the number of the returned documents to
               the specified number.
        :param List[str] sort: (optional) Specifies the sort order of the results.
               In a grouped search (when group_field is used), this parameter specifies
               the sort order within a group. The default sort order is relevance.  A JSON
               string of the form "fieldname&lt;type&gt;" or "-fieldname&lt;type&gt;" for
               descending order, where fieldname is the name of a string or number field,
               and type is either a number, a string, or a JSON array of strings. The type
               part is optional, and defaults to number. Some examples are "foo", "-foo",
               "bar&lt;string&gt;", "-foo&lt;number&gt;" and ["-foo&lt;number&gt;",
               "bar&lt;string&gt;"]. String fields that are used for sorting must not be
               analyzed fields. Fields that are used for sorting must be indexed by the
               same indexer that is used for the search query.
        :param str stale: (optional) Do not wait for the index to finish building
               to return results.
        :param List[str] counts: (optional) This field defines an array of names of
               string fields, for which counts are requested. The response contains counts
               for each unique value of this field name among the documents that match the
               search query. Faceting must be enabled for this parameter to function. This
               option is only available when making global queries.
        :param List[List[str]] drilldown: (optional) Restrict results to documents
               with a dimension equal to the specified label(s). The search matches only
               documents containing the value that was provided in the named field. It
               differs from using "fieldname:value" in the q parameter only in that the
               values are not analyzed. Faceting must be enabled for this parameter to
               function.
        :param str group_field: (optional) Field by which to group search matches.
               A string that contains the name of a string field. Fields containing other
               data such as numbers, objects, or arrays cannot be used. This option is
               only available when making global queries.
        :param int group_limit: (optional) Maximum group count. This field can be
               used only if group_field is specified. This option is only available when
               making global queries.
        :param List[str] group_sort: (optional) This field defines the order of the
               groups in a search that uses group_field. The default sort order is
               relevance. This field can have the same values as the sort field, so single
               fields and arrays of fields are supported. This option is only available
               when making global queries.
        :param dict ranges: (optional) This field defines ranges for faceted,
               numeric search fields. The value is a JSON object where the fields names
               are faceted numeric search fields, and the values of the fields are JSON
               objects. The field names of the JSON objects are names for ranges. The
               values are strings that describe the range, for example "[0 TO 10]". This
               option is only available when making global queries.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        if index is None:
            raise ValueError('index must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_search_as_stream')
        headers.update(sdk_headers)

        data = {
            'query': query,
            'bookmark': bookmark,
            'highlight_fields': highlight_fields,
            'highlight_number': highlight_number,
            'highlight_post_tag': highlight_post_tag,
            'highlight_pre_tag': highlight_pre_tag,
            'highlight_size': highlight_size,
            'include_docs': include_docs,
            'include_fields': include_fields,
            'limit': limit,
            'sort': sort,
            'stale': stale,
            'counts': counts,
            'drilldown': drilldown,
            'group_field': group_field,
            'group_limit': group_limit,
            'group_sort': group_sort,
            'ranges': ranges
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_design/{1}/_search/{2}'.format(
            *self.encode_path_vars(db, ddoc, index))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, stream=True)
        return response


    def get_search_info(self,
        db: str,
        ddoc: str,
        index: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve information about a search index.

        Retrieve search index metadata information, such as the size of the index on disk.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str index: Path parameter to specify the index name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SearchInfoResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        if index is None:
            raise ValueError('index must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_search_info')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_design/{1}/_search_info/{2}'.format(
            *self.encode_path_vars(db, ddoc, index))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Geospatial
    #########################


    def get_geo(self,
        db: str,
        ddoc: str,
        index: str,
        *,
        bbox: str = None,
        bookmark: str = None,
        format: str = None,
        g: str = None,
        include_docs: bool = None,
        lat: float = None,
        limit: int = None,
        lon: float = None,
        nearest: bool = None,
        radius: float = None,
        rangex: float = None,
        rangey: float = None,
        relation: str = None,
        skip: int = None,
        stale: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a geospatial index.

        Executes a query against the requested geospatial index from the specified design
        document.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str index: Path parameter to specify the index name.
        :param str bbox: (optional) Query parameter to specify a geospatial query
               bounding box with two latitude,longitude coordinates for the lower-left and
               upper-right corners. An example is
               `-11.05987446,12.28339928,-101.05987446,62.28339928`.
        :param str bookmark: (optional) Query parameter to specify a bookmark that
               was received from a previous request. This parameter enables paging through
               the results. If there are no more results after the bookmark, you get a
               response containing no further results and the same bookmark, confirming
               the end of the result list.
        :param str format: (optional) Query parameter that causes the geospatial
               query output to be returned in the specified format.
        :param str g: (optional) Query parameter to specify a Well Known Text (WKT)
               representation of a geospatial query geometry. The valid values for the WKT
               parameter include `Point`, `LineString`, `Polygon`, `MultiPoint`,
               `MultiLineString`, `MultiPolygon`, and `GeometryCollection`.
        :param bool include_docs: (optional) Query parameter to specify whether to
               include the full content of the documents in the response.
        :param float lat: (optional) Query parameter to specify a latitude
               coordinate for use with radius or ellipse geospatial queries.
        :param int limit: (optional) Query parameter to specify the number of
               returned documents to limit the result to.
        :param float lon: (optional) Query parameter to specify a longitude
               coordinate for use with radius or ellipse geospatial queries.
        :param bool nearest: (optional) Query parameter to specify whether to
               perform a nearest neighbour (NN) search. If provided, the `nearest=true`
               search returns all results by sorting their distances to the center of the
               query geometry. NN search can be used alone or with any of the supported
               DE-9IM (Dimensionally Extended nine-Intersection Model) specification
               geometric relations documented.
        :param float radius: (optional) Query parameter to specify the radius, in
               meters, to search from a lat,lon coordinate point in a circular geospatial
               query.
        :param float rangex: (optional) Query parameter to specify the first
               radius, in meters, to search from a lat,lon coordinate point in an ellipse
               geospatial query.
        :param float rangey: (optional) Query parameter to specify the second
               radius, in meters, to search from a lat,lon coordinate point in an ellipse
               geospatial query.
        :param str relation: (optional) Query parameter to specify the DE-9IM
               (Dimensionally Extended nine-Intersection Model)geospatial relationship
               between the query geometry and the result documents.
        :param int skip: (optional) Query parameter to specify the number of
               records before starting to return the results.
        :param str stale: (optional) Query parameter to specify to not wait for the
               index to finish building before returning results.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GeoResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        if index is None:
            raise ValueError('index must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_geo')
        headers.update(sdk_headers)

        params = {
            'bbox': bbox,
            'bookmark': bookmark,
            'format': format,
            'g': g,
            'include_docs': include_docs,
            'lat': lat,
            'limit': limit,
            'lon': lon,
            'nearest': nearest,
            'radius': radius,
            'rangex': rangex,
            'rangey': rangey,
            'relation': relation,
            'skip': skip,
            'stale': stale
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_design/{1}/_geo/{2}'.format(
            *self.encode_path_vars(db, ddoc, index))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_geo_as_stream(self,
        db: str,
        ddoc: str,
        index: str,
        *,
        bbox: str = None,
        bookmark: str = None,
        format: str = None,
        g: str = None,
        include_docs: bool = None,
        lat: float = None,
        limit: int = None,
        lon: float = None,
        nearest: bool = None,
        radius: float = None,
        rangex: float = None,
        rangey: float = None,
        relation: str = None,
        skip: int = None,
        stale: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a geospatial index as stream.

        Executes a query against the requested geospatial index from the specified design
        document.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str index: Path parameter to specify the index name.
        :param str bbox: (optional) Query parameter to specify a geospatial query
               bounding box with two latitude,longitude coordinates for the lower-left and
               upper-right corners. An example is
               `-11.05987446,12.28339928,-101.05987446,62.28339928`.
        :param str bookmark: (optional) Query parameter to specify a bookmark that
               was received from a previous request. This parameter enables paging through
               the results. If there are no more results after the bookmark, you get a
               response containing no further results and the same bookmark, confirming
               the end of the result list.
        :param str format: (optional) Query parameter that causes the geospatial
               query output to be returned in the specified format.
        :param str g: (optional) Query parameter to specify a Well Known Text (WKT)
               representation of a geospatial query geometry. The valid values for the WKT
               parameter include `Point`, `LineString`, `Polygon`, `MultiPoint`,
               `MultiLineString`, `MultiPolygon`, and `GeometryCollection`.
        :param bool include_docs: (optional) Query parameter to specify whether to
               include the full content of the documents in the response.
        :param float lat: (optional) Query parameter to specify a latitude
               coordinate for use with radius or ellipse geospatial queries.
        :param int limit: (optional) Query parameter to specify the number of
               returned documents to limit the result to.
        :param float lon: (optional) Query parameter to specify a longitude
               coordinate for use with radius or ellipse geospatial queries.
        :param bool nearest: (optional) Query parameter to specify whether to
               perform a nearest neighbour (NN) search. If provided, the `nearest=true`
               search returns all results by sorting their distances to the center of the
               query geometry. NN search can be used alone or with any of the supported
               DE-9IM (Dimensionally Extended nine-Intersection Model) specification
               geometric relations documented.
        :param float radius: (optional) Query parameter to specify the radius, in
               meters, to search from a lat,lon coordinate point in a circular geospatial
               query.
        :param float rangex: (optional) Query parameter to specify the first
               radius, in meters, to search from a lat,lon coordinate point in an ellipse
               geospatial query.
        :param float rangey: (optional) Query parameter to specify the second
               radius, in meters, to search from a lat,lon coordinate point in an ellipse
               geospatial query.
        :param str relation: (optional) Query parameter to specify the DE-9IM
               (Dimensionally Extended nine-Intersection Model)geospatial relationship
               between the query geometry and the result documents.
        :param int skip: (optional) Query parameter to specify the number of
               records before starting to return the results.
        :param str stale: (optional) Query parameter to specify to not wait for the
               index to finish building before returning results.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        if index is None:
            raise ValueError('index must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_geo_as_stream')
        headers.update(sdk_headers)

        params = {
            'bbox': bbox,
            'bookmark': bookmark,
            'format': format,
            'g': g,
            'include_docs': include_docs,
            'lat': lat,
            'limit': limit,
            'lon': lon,
            'nearest': nearest,
            'radius': radius,
            'rangex': rangex,
            'rangey': rangey,
            'relation': relation,
            'skip': skip,
            'stale': stale
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_design/{1}/_geo/{2}'.format(
            *self.encode_path_vars(db, ddoc, index))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, stream=True)
        return response


    def post_geo_cleanup(self,
        db: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Cleanup old geospatial indexes.

        Cleanup old geospatial indexes from disk that have been superseded by newer index
        builds.

        :param str db: Path parameter to specify the database name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ok` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_geo_cleanup')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_geo_cleanup'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_geo_index_information(self,
        db: str,
        ddoc: str,
        index: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve information about a geospatial index.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str index: Path parameter to specify the index name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GeoIndexInformation` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if ddoc is None:
            raise ValueError('ddoc must be provided')
        if index is None:
            raise ValueError('index must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_geo_index_information')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_design/{1}/_geo_info/{2}'.format(
            *self.encode_path_vars(db, ddoc, index))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Changes
    #########################


    def get_db_updates(self,
        *,
        feed: str = None,
        heartbeat: int = None,
        timeout: int = None,
        since: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve change events for all databases.

        Lists changes to databases, like a global changes feed. Types of changes include
        updating the database and creating or deleting a database. Like the changes feed,
        the feed is not guaranteed to return changes in the correct order and might repeat
        changes. Polling modes for this method work like polling modes for the changes
        feed.
        **Note: This endpoint requires _admin or _db_updates role and is only available on
        dedicated clusters.**.

        :param str feed: (optional) Query parameter to specify the changes feed
               type.
        :param int heartbeat: (optional) Query parameter to specify the period in
               milliseconds after which an empty line is sent in the results. Only
               applicable for longpoll, continuous, and eventsource feeds. Overrides any
               timeout to keep the feed alive indefinitely. May also be `true` to use
               default value of 60000.
        :param int timeout: (optional) Query parameter to specify the maximum
               period in milliseconds to wait for a change before the response is sent,
               even if there are no results. Only applicable for `longpoll` or
               `continuous` feeds. Default value is specified by `httpd/changes_timeout`
               configuration option. Note that `60000` value is also the default maximum
               timeout to prevent undetected dead connections.
        :param str since: (optional) Query parameter to specify to start the
               results from the change immediately after the given update sequence. Can be
               a valid update sequence or `now` value. Default is `0` i.e. all changes.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DbUpdates` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_db_updates')
        headers.update(sdk_headers)

        params = {
            'feed': feed,
            'heartbeat': heartbeat,
            'timeout': timeout,
            'since': since
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_db_updates'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Replication
    #########################


    def head_replication_document(self,
        doc_id: str,
        *,
        if_none_match: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve the HTTP headers for a replication document.

        Retrieves the HTTP headers for a replication document from the `_replicator`
        database.

        :param str doc_id: Path parameter to specify the document ID.
        :param str if_none_match: (optional) Header parameter to specify a double
               quoted document revision token for cache control.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if doc_id is None:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-None-Match': if_none_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='head_replication_document')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/_replicator/{0}'.format(
            *self.encode_path_vars(doc_id))
        request = self.prepare_request(method='HEAD',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def head_scheduler_job(self,
        job_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve the HTTP headers for a replication scheduler job.

        Returns the HTTP headers that contain a minimal amount of information about the
        specified replication task. Only the header information is returned.

        :param str job_id: Path parameter to specify the replication job id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if job_id is None:
            raise ValueError('job_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='head_scheduler_job')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/_scheduler/jobs/{0}'.format(
            *self.encode_path_vars(job_id))
        request = self.prepare_request(method='HEAD',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def post_replicate(self,
        *,
        replication_document: 'ReplicationDocument' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create or modify a replication operation.

        Requests, configures, or stops a replicate operation.

        :param ReplicationDocument replication_document: (optional) HTTP request
               body for replication operations.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReplicationResult` object
        """

        if  replication_document is not None and isinstance(replication_document, ReplicationDocument):
            replication_document = convert_model(replication_document)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_replicate')
        headers.update(sdk_headers)

        data = json.dumps(replication_document)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_replicate'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_replication_document(self,
        doc_id: str,
        *,
        if_match: str = None,
        batch: str = None,
        rev: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Cancel a replication.

        Cancels a replication by deleting the document that describes it from the
        `_replicator` database.

        :param str doc_id: Path parameter to specify the document ID.
        :param str if_match: (optional) Header parameter to specify the document
               revision. Alternative to rev query parameter.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if doc_id is None:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_replication_document')
        headers.update(sdk_headers)

        params = {
            'batch': batch,
            'rev': rev
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_replicator/{0}'.format(
            *self.encode_path_vars(doc_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_replication_document(self,
        doc_id: str,
        *,
        if_none_match: str = None,
        attachments: bool = None,
        att_encoding_info: bool = None,
        atts_since: List[str] = None,
        conflicts: bool = None,
        deleted_conflicts: bool = None,
        latest: bool = None,
        local_seq: bool = None,
        meta: bool = None,
        open_revs: List[str] = None,
        rev: str = None,
        revs: bool = None,
        revs_info: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve a replication document.

        Retrieves a replication document from the `_replicator` database to view the
        configuration of the replication. The status of the replication is no longer
        recorded in the document but can be checked via the replication scheduler.

        :param str doc_id: Path parameter to specify the document ID.
        :param str if_none_match: (optional) Header parameter to specify a double
               quoted document revision token for cache control.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param List[str] atts_since: (optional) Query parameter to specify whether
               to include attachments only since specified revisions. Note this does not
               include the attachments for the specified revisions.
        :param bool conflicts: (optional) Query parameter to specify whether to
               include a list of conflicted revisions in the `_conflicts` property of the
               returned document. Ignored if `include_docs` isn't `true`.
        :param bool deleted_conflicts: (optional) Query parameter to specify
               whether to include a list of deleted conflicted revisions in the
               `_deleted_conflicts` property of the returned document.
        :param bool latest: (optional) Query parameter to specify whether to force
               retrieving latest leaf revision, no matter what rev was requested.
        :param bool local_seq: (optional) Query parameter to specify whether to
               include the last update sequence for the document.
        :param bool meta: (optional) Query parameter to specify whether to include
               document meta information. Acts the same as specifying all of the
               conflicts, deleted_conflicts and open_revs query parameters.
        :param List[str] open_revs: (optional) Query parameter to specify leaf
               revisions to retrieve. Additionally, it accepts a value of `all` to return
               all leaf revisions.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param bool revs: (optional) Query parameter to specify whether to include
               a list of all known document revisions.
        :param bool revs_info: (optional) Query parameter to specify whether to
               includes detailed information for all known document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReplicationDocument` object
        """

        if doc_id is None:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-None-Match': if_none_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_replication_document')
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'atts_since': convert_list(atts_since),
            'conflicts': conflicts,
            'deleted_conflicts': deleted_conflicts,
            'latest': latest,
            'local_seq': local_seq,
            'meta': meta,
            'open_revs': convert_list(open_revs),
            'rev': rev,
            'revs': revs,
            'revs_info': revs_info
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_replicator/{0}'.format(
            *self.encode_path_vars(doc_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def put_replication_document(self,
        doc_id: str,
        *,
        replication_document: 'ReplicationDocument' = None,
        if_match: str = None,
        batch: str = None,
        new_edits: bool = None,
        rev: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Start or update a replication.

        Creates or modifies a document in the `_replicator` database to start a new
        replication or to edit an existing replication.

        :param str doc_id: Path parameter to specify the document ID.
        :param ReplicationDocument replication_document: (optional) HTTP request
               body for replication operations.
        :param str if_match: (optional) Header parameter to specify the document
               revision. Alternative to rev query parameter.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param bool new_edits: (optional) Query parameter to specify whether to
               prevent insertion of conflicting document revisions. If false, a
               well-formed _rev must be included in the document. False is used by the
               replicator to insert documents into the target database even if that leads
               to the creation of conflicts.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if doc_id is None:
            raise ValueError('doc_id must be provided')
        if  replication_document is not None and isinstance(replication_document, ReplicationDocument):
            replication_document = convert_model(replication_document)
        headers = {
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='put_replication_document')
        headers.update(sdk_headers)

        params = {
            'batch': batch,
            'new_edits': new_edits,
            'rev': rev
        }

        data = json.dumps(replication_document)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_replicator/{0}'.format(
            *self.encode_path_vars(doc_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


    def get_scheduler_docs(self,
        *,
        limit: int = None,
        skip: int = None,
        states: List[str] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve replication scheduler documents.

        Lists replication documents, including information about all documents, even the
        ones in a completed or failed state. For each document, the endpoint returns the
        document ID, database, replication ID, source and target, and other information.

        :param int limit: (optional) Query parameter to specify the number of
               returned documents to limit the result to.
        :param int skip: (optional) Query parameter to specify the number of
               records before starting to return the results.
        :param List[str] states: (optional) Query parameter to include only
               replication documents in the specified states. String must be a
               comma-delimited string.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SchedulerDocsResult` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_scheduler_docs')
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'skip': skip,
            'states': convert_list(states)
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_scheduler/docs'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_scheduler_document(self,
        doc_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve a replication scheduler document.

        Retrieves information about a replication document from the replicator database.
        The endpoint returns the document ID, database, replication ID, source and target,
        and other information.

        :param str doc_id: Path parameter to specify the document ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SchedulerDocument` object
        """

        if doc_id is None:
            raise ValueError('doc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_scheduler_document')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_scheduler/docs/_replicator/{0}'.format(
            *self.encode_path_vars(doc_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_scheduler_jobs(self,
        *,
        limit: int = None,
        skip: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve replication scheduler jobs.

        Retrieves information about replications that were created via `/_replicate`
        endpoint, as well as those created from replication documents. It doesn't include
        replications that completed or failed to start because replication documents were
        malformed. Each job description includes source and target information,
        replication ID, history of recent events, and other information.

        :param int limit: (optional) Query parameter to specify the number of
               returned documents to limit the result to.
        :param int skip: (optional) Query parameter to specify the number of
               records before starting to return the results.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SchedulerJobsResult` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_scheduler_jobs')
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'skip': skip
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_scheduler/jobs'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_scheduler_job(self,
        job_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve a replication scheduler job.

        Retrieves the state of a single replication task based on its replication ID.

        :param str job_id: Path parameter to specify the replication job id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SchedulerJob` object
        """

        if job_id is None:
            raise ValueError('job_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_scheduler_job')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_scheduler/jobs/{0}'.format(
            *self.encode_path_vars(job_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Authentication
    #########################


    def get_session_information(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve current session cookie information.

        Retrieves information about the authenticated user's session.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SessionInformation` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_session_information')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_session'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def delete_iam_session(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete an IAM cookie session.

        Returns a response that instructs the HTTP client to clear the cookie. The session
        cookies are stateless and cannot be invalidated; hence, this operation is optional
        and does not invalidate the cookie on the server.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ok` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_iam_session')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_iam_session'
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_iam_session_information(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve current IAM cookie session information.

        Retrieves information about an IAM cookie session.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IamSessionInformation` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_iam_session_information')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_iam_session'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def post_iam_session(self,
        *,
        access_token: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a session cookie by using an IAM token.

        Log in by exchanging an IAM token for an IBM Cloudant cookie.

        :param str access_token: (optional) Token obtained from the IAM service.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ok` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_iam_session')
        headers.update(sdk_headers)

        data = {
            'access_token': access_token
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_iam_session'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Authorization
    #########################


    def get_security(self,
        db: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve database permissions information.

        See who has permission to read, write, and manage the database. The credentials
        you use to log in to the dashboard automatically include `_admin` permissions to
        all databases you create. Everyone and everything else, including users you share
        databases with and API keys you create, must be given a permission level
        explicitly.

        :param str db: Path parameter to specify the database name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Security` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_security')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_security'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def put_security(self,
        db: str,
        *,
        admins: 'SecurityObject' = None,
        members: 'SecurityObject' = None,
        cloudant: dict = None,
        couchdb_auth_only: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Modify database permissions.

        Modify who has permission to read, write, or manage a database. This endpoint can
        be used to modify both Cloudant and CouchDB related permissions. Be careful: by
        removing a Cloudant API key, a member or an admin from the list of users that have
        access permissions, you remove it from the list of users that have access to the
        database.

        :param str db: Path parameter to specify the database name.
        :param SecurityObject admins: (optional) Schema for names and roles to map
               to a database permission.
        :param SecurityObject members: (optional) Schema for names and roles to map
               to a database permission.
        :param dict cloudant: (optional) Database permissions for Cloudant users
               and/or API keys.
        :param bool couchdb_auth_only: (optional) Manage permissions using the
               `_users` database only.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ok` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if admins is not None:
            admins = convert_model(admins)
        if members is not None:
            members = convert_model(members)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='put_security')
        headers.update(sdk_headers)

        data = {
            'admins': admins,
            'members': members,
            'cloudant': cloudant,
            'couchdb_auth_only': couchdb_auth_only
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_security'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_api_keys(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Generates API keys for apps or persons to enable database access.

        Generates API keys to enable database access for a person or application, but
        without creating a new IBM Cloudant account for that person or application. An API
        key is a randomly generated username and password. The key is given the wanted
        access permissions for a database.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiKeysResult` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_api_keys')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_api/v2/api_keys'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def put_cloudant_security(self,
        db: str,
        *,
        cloudant: dict = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Modify only Cloudant related database permissions.

        Modify only Cloudant related permissions to database. Be careful: by removing an
        API key from the list, you remove the API key from the list of users that have
        access to the database.

        :param str db: Path parameter to specify the database name.
        :param dict cloudant: (optional) Database permissions for Cloudant users
               and/or API keys.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ok` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='put_cloudant_security')
        headers.update(sdk_headers)

        data = {
            'cloudant': cloudant
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_api/v2/db/{0}/_security'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # CORS
    #########################


    def get_cors_information(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve CORS configuration information.

        Lists all Cross-origin resource sharing (CORS) configuration. CORS defines a way
        in which the browser and the server interact to determine whether or not to allow
        the request.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CorsConfiguration` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_cors_information')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_api/v2/user/config/cors'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def put_cors_configuration(self,
        *,
        origins: List[str] = None,
        allow_credentials: bool = None,
        enable_cors: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Modify CORS configuration.

        Sets the CORS configuration. The configuration applies to all databases and all
        account level endpoints in your account.

        :param List[str] origins: (optional) An array of strings that contain
               allowed origin domains. You have to specify the full URL including the
               protocol. It is recommended that only the HTTPS protocol is used.
               Subdomains count as separate domains, so you have to specify all subdomains
               used.
        :param bool allow_credentials: (optional) Boolean value to allow
               authentication credentials. If set to true, browser requests must be done
               by using withCredentials = true.
        :param bool enable_cors: (optional) Boolean value to turn CORS on and off.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ok` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='put_cors_configuration')
        headers.update(sdk_headers)

        data = {
            'origins': origins,
            'allow_credentials': allow_credentials,
            'enable_cors': enable_cors
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_api/v2/user/config/cors'
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Attachments
    #########################


    def head_attachment(self,
        db: str,
        doc_id: str,
        attachment_name: str,
        *,
        if_match: str = None,
        if_none_match: str = None,
        rev: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve the HTTP headers for an attachment.

        Returns the HTTP headers that contain a minimal amount of information about the
        specified attachment. This method supports the same query arguments as the `GET
        /{db}/{doc_id}/{attachment_name}` method, but only the header information
        (including attachment size, encoding, and the MD5 hash as an ETag), is returned.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str attachment_name: Path parameter to specify the attachment name.
        :param str if_match: (optional) Header parameter to specify the document
               revision. Alternative to rev query parameter.
        :param str if_none_match: (optional) Header parameter to specify a double
               quoted document revision token for cache control.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if db is None:
            raise ValueError('db must be provided')
        if doc_id is None:
            raise ValueError('doc_id must be provided')
        if attachment_name is None:
            raise ValueError('attachment_name must be provided')
        headers = {
            'If-Match': if_match,
            'If-None-Match': if_none_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='head_attachment')
        headers.update(sdk_headers)

        params = {
            'rev': rev
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/{0}/{1}/{2}'.format(
            *self.encode_path_vars(db, doc_id, attachment_name))
        request = self.prepare_request(method='HEAD',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def delete_attachment(self,
        db: str,
        doc_id: str,
        attachment_name: str,
        *,
        if_match: str = None,
        rev: str = None,
        batch: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete an attachment.

        Deletes the attachment with the filename, `{attachment_name}`, from the specified
        doc. You must supply the `rev` query parameter or `If-Match` header with the
        current revision to delete the attachment.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str attachment_name: Path parameter to specify the attachment name.
        :param str if_match: (optional) Header parameter to specify the document
               revision. Alternative to rev query parameter.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if doc_id is None:
            raise ValueError('doc_id must be provided')
        if attachment_name is None:
            raise ValueError('attachment_name must be provided')
        headers = {
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_attachment')
        headers.update(sdk_headers)

        params = {
            'rev': rev,
            'batch': batch
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/{1}/{2}'.format(
            *self.encode_path_vars(db, doc_id, attachment_name))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_attachment(self,
        db: str,
        doc_id: str,
        attachment_name: str,
        *,
        if_match: str = None,
        if_none_match: str = None,
        range: str = None,
        rev: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve an attachment.

        Returns the file attachment that is associated with the document. The raw data of
        the associated attachment is returned, just as if you were accessing a static
        file. The returned Content-Type header is the same as the content type set when
        the document attachment was submitted to the database.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str attachment_name: Path parameter to specify the attachment name.
        :param str if_match: (optional) Header parameter to specify the document
               revision. Alternative to rev query parameter.
        :param str if_none_match: (optional) Header parameter to specify a double
               quoted document revision token for cache control.
        :param str range: (optional) Header parameter to specify the byte range for
               a request. This allows the implementation of resumable downloads and
               skippable streams. This is available for all attachments inside CouchDB.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if db is None:
            raise ValueError('db must be provided')
        if doc_id is None:
            raise ValueError('doc_id must be provided')
        if attachment_name is None:
            raise ValueError('attachment_name must be provided')
        headers = {
            'If-Match': if_match,
            'If-None-Match': if_none_match,
            'Range': range
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_attachment')
        headers.update(sdk_headers)

        params = {
            'rev': rev
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = '*/*'

        url = '/{0}/{1}/{2}'.format(
            *self.encode_path_vars(db, doc_id, attachment_name))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def put_attachment(self,
        db: str,
        doc_id: str,
        attachment_name: str,
        attachment: BinaryIO,
        content_type: str,
        *,
        if_match: str = None,
        rev: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create or modify an attachment.

        Uploads the supplied content as an attachment to the specified document. The
        attachment name that you provide must be a URL encoded string. You must supply the
        Content-Type header, and for an existing document, you must also supply either the
        `rev` query argument or the `If-Match` HTTP header. If you omit the revision, a
        new, otherwise empty, document is created with the provided attachment, or a
        conflict occurs. If the uploaded attachment uses an existing attachment name in
        the remote database, it updates the corresponding stored content of the database.
        Since you must supply the revision information to add an attachment to the
        document, this serves as validation to update the existing attachment.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str attachment_name: Path parameter to specify the attachment name.
        :param BinaryIO attachment: HTTP request body for attachment operations.
        :param str content_type: Content-Type of the attachment.
        :param str if_match: (optional) Header parameter to specify the document
               revision. Alternative to rev query parameter.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if doc_id is None:
            raise ValueError('doc_id must be provided')
        if attachment_name is None:
            raise ValueError('attachment_name must be provided')
        if attachment is None:
            raise ValueError('attachment must be provided')
        if content_type is None:
            raise ValueError('content_type must be provided')
        headers = {
            'Content-Type': content_type,
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='put_attachment')
        headers.update(sdk_headers)

        params = {
            'rev': rev
        }

        data = attachment

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/{1}/{2}'.format(
            *self.encode_path_vars(db, doc_id, attachment_name))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Local Documents
    #########################


    def delete_local_document(self,
        db: str,
        doc_id: str,
        *,
        batch: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a local document.

        Deletes the specified local document. The semantics are identical to deleting a
        standard document in the specified database, except that the document is not
        replicated.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if doc_id is None:
            raise ValueError('doc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_local_document')
        headers.update(sdk_headers)

        params = {
            'batch': batch
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_local/{1}'.format(
            *self.encode_path_vars(db, doc_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_local_document(self,
        db: str,
        doc_id: str,
        *,
        accept: str = None,
        if_none_match: str = None,
        attachments: bool = None,
        att_encoding_info: bool = None,
        atts_since: List[str] = None,
        local_seq: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve a local document.

        Retrieves the specified local document. The semantics are identical to accessing a
        standard document in the specified database, except that the document is not
        replicated.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str accept: (optional) The type of the response: application/json,
               multipart/mixed, multipart/related, or application/octet-stream.
        :param str if_none_match: (optional) Header parameter to specify a double
               quoted document revision token for cache control.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param List[str] atts_since: (optional) Query parameter to specify whether
               to include attachments only since specified revisions. Note this does not
               include the attachments for the specified revisions.
        :param bool local_seq: (optional) Query parameter to specify whether to
               include the last update sequence for the document.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Document` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if doc_id is None:
            raise ValueError('doc_id must be provided')
        headers = {
            'Accept': accept,
            'If-None-Match': if_none_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_local_document')
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'atts_since': convert_list(atts_since),
            'local_seq': local_seq
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/{0}/_local/{1}'.format(
            *self.encode_path_vars(db, doc_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def put_local_document(self,
        db: str,
        doc_id: str,
        *,
        document: Union['Document', BinaryIO] = None,
        content_type: str = None,
        batch: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create or modify a local document.

        Stores the specified local document. The semantics are identical to storing a
        standard document in the specified database, except that the document is not
        replicated.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param Document document: (optional) HTTP request body for Document
               operations.
        :param str content_type: (optional) The type of the input.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if doc_id is None:
            raise ValueError('doc_id must be provided')
        if  document is not None and isinstance(document, Document):
            document = convert_model(document)
            content_type = content_type or 'application/json'
        headers = {
            'Content-Type': content_type
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='put_local_document')
        headers.update(sdk_headers)

        params = {
            'batch': batch
        }

        if document is not None and isinstance(document, dict):
            data = json.dumps(document)
            if content_type is None:
                headers['Content-Type'] = 'application/json'
        else:
            data = document

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_local/{1}'.format(
            *self.encode_path_vars(db, doc_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


    def post_local_docs(self,
        db: str,
        *,
        accept: str = None,
        att_encoding_info: bool = None,
        attachments: bool = None,
        conflicts: bool = None,
        descending: bool = None,
        include_docs: bool = None,
        inclusive_end: bool = None,
        limit: int = None,
        skip: int = None,
        update_seq: bool = None,
        endkey: str = None,
        key: str = None,
        keys: List[str] = None,
        startkey: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query a list of all local documents in a database.

        Queries the list of all local document IDs. The results matching the request body
        parameters are returned in a JSON object, including a list of matching local
        documents with basic contents, such as the ID. When no request body parameters are
        specified, results for all local documents in the database are returned.
        Optionally, document content or additional metadata can be included in the
        response.

        :param str db: Path parameter to specify the database name.
        :param str accept: (optional) The type of the response: application/json or
               application/octet-stream.
        :param bool att_encoding_info: (optional) Parameter to specify whether to
               include the encoding information in attachment stubs if the particular
               attachment is compressed.
        :param bool attachments: (optional) Parameter to specify whether to include
               attachments bodies in a response.
        :param bool conflicts: (optional) Parameter to specify whether to include a
               list of conflicted revisions in the `_conflicts` property of the returned
               document. Ignored if `include_docs` isn't `true`.
        :param bool descending: (optional) Parameter to specify whether to return
               the documents in descending by key order.
        :param bool include_docs: (optional) Parameter to specify whether to
               include the full content of the documents in the response.
        :param bool inclusive_end: (optional) Parameter to specify whether the
               specified end key should be included in the result.
        :param int limit: (optional) Parameter to specify the number of returned
               documents to limit the result to.
        :param int skip: (optional) Parameter to specify the number of records
               before starting to return the results.
        :param bool update_seq: (optional) Parameter to specify whether to include
               in the response an update_seq value indicating the sequence id of the
               database the view reflects.
        :param str endkey: (optional) Schema for a document ID.
        :param str key: (optional) Schema for a document ID.
        :param List[str] keys: (optional) Schema for a list of document IDs.
        :param str startkey: (optional) Schema for a document ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllDocsResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_local_docs')
        headers.update(sdk_headers)

        data = {
            'att_encoding_info': att_encoding_info,
            'attachments': attachments,
            'conflicts': conflicts,
            'descending': descending,
            'include_docs': include_docs,
            'inclusive_end': inclusive_end,
            'limit': limit,
            'skip': skip,
            'update_seq': update_seq,
            'endkey': endkey,
            'key': key,
            'keys': keys,
            'startkey': startkey
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/{0}/_local_docs'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_local_docs_queries(self,
        db: str,
        *,
        accept: str = None,
        queries: List['AllDocsQuery'] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Multi-query the list of all local documents in a database.

        Runs multiple view queries of all local documents in this database. This operation
        enables you to request multiple queries in a single request, in place of multiple
        `POST /{db}/_local_docs` requests.

        :param str db: Path parameter to specify the database name.
        :param str accept: (optional) The type of the response: application/json or
               application/octet-stream.
        :param List[AllDocsQuery] queries: (optional) An array of query objects
               with fields for the parameters of each individual view query to be
               executed. The field names and their meaning are the same as the query
               parameters of a regular `/_all_docs` request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllDocsQueriesResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if queries is not None:
            queries = [convert_model(x) for x in queries]
        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_local_docs_queries')
        headers.update(sdk_headers)

        data = {
            'queries': queries
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/{0}/_local_docs/queries'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Database Details
    #########################


    def post_ensure_full_commit(self,
        db: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Commit any recent changes to the specified database to disk.

        Commits any recent changes to the specified database to disk. You must make a
        request to this endpoint if you want to ensure that recent changes have been
        flushed. This function is likely not required, assuming you have the recommended
        configuration setting, `delayed_commits=false`. This setting requires that changes
        are written to disk before a 200 or similar result is returned.

        :param str db: Path parameter to specify the database name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `EnsureFullCommitInformation` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_ensure_full_commit')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_ensure_full_commit'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def post_missing_revs(self,
        db: str,
        *,
        missing_revs: dict = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query which document revisions are missing from the database.

        Given a list of document revisions, returns the document revisions that do not
        exist in the database.

        :param str db: Path parameter to specify the database name.
        :param dict missing_revs: (optional) HTTP request body for postMissingRevs
               and postRevsDiff.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MissingRevsResult` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_missing_revs')
        headers.update(sdk_headers)

        data = json.dumps(missing_revs)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_missing_revs'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def post_revs_diff(self,
        db: str,
        *,
        revs_diff_request: dict = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query the document revisions and possible ancestors missing from the database.

        The replicator is the primary user of this operation. After receiving a set of new
        revision IDs from the source database, the replicator sends this set to the
        destination database's `_revs_diff` to find out which of them already exists
        there. It can then avoid fetching and sending already-known document bodies.

        :param str db: Path parameter to specify the database name.
        :param dict revs_diff_request: (optional) HTTP request body for
               postMissingRevs and postRevsDiff.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `dict` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_revs_diff')
        headers.update(sdk_headers)

        data = json.dumps(revs_diff_request)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_revs_diff'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_shards_information(self,
        db: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve shard information.

        List each shard range and the corresponding replicas for a specified database.

        :param str db: Path parameter to specify the database name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ShardsInformation` object
        """

        if db is None:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_shards_information')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_shards'.format(
            *self.encode_path_vars(db))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_document_shards_info(self,
        db: str,
        doc_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve shard information for a specific document.

        Retrieves information about a specific shard where a particular document is
        stored, along with information about the nodes where that shard has a replica.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentShardInfo` object
        """

        if db is None:
            raise ValueError('db must be provided')
        if doc_id is None:
            raise ValueError('doc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_document_shards_info')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/{0}/_shards/{1}'.format(
            *self.encode_path_vars(db, doc_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Monitoring
    #########################


    def get_active_tasks(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve list of running tasks.

        Lists running tasks, including the task type, name, status, and process ID. The
        result includes a JSON array of the currently running tasks, with each task
        described as a single object. Depending on the operation type, the set of response
        object fields might be different.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[ActiveTask]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_active_tasks')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_active_tasks'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_up_information(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve information about whether the server is up.

        Confirms that the server is up, running, and ready to respond to requests. If
        `maintenance_mode` is `true` or `nolb`, the endpoint returns a 404 response.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UpInformation` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_up_information')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/_up'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


class PostChangesEnums:
    """
    Enums for post_changes parameters.
    """

    class Feed(str, Enum):
        """
        Query parameter to specify the changes feed type.
        """
        CONTINUOUS = 'continuous'
        EVENTSOURCE = 'eventsource'
        LONGPOLL = 'longpoll'
        NORMAL = 'normal'


class PostChangesEnums:
    """
    Enums for post_changes_as_stream parameters.
    """

    class Feed(str, Enum):
        """
        Query parameter to specify the changes feed type.
        """
        CONTINUOUS = 'continuous'
        EVENTSOURCE = 'eventsource'
        LONGPOLL = 'longpoll'
        NORMAL = 'normal'


class PostDocumentEnums:
    """
    Enums for post_document parameters.
    """

    class ContentType(str, Enum):
        """
        The type of the input.
        """
        APPLICATION_JSON = 'application/json'
        MULTIPART_MIXED = 'multipart/mixed'
        MULTIPART_RELATED = 'multipart/related'
        APPLICATION_OCTET_STREAM = 'application/octet-stream'
    class Batch(str, Enum):
        """
        Query parameter to specify whether to store in batch mode. The server will respond
        with a HTTP 202 Accepted response code immediately.
        """
        OK = 'ok'


class DeleteDocumentEnums:
    """
    Enums for delete_document parameters.
    """

    class Batch(str, Enum):
        """
        Query parameter to specify whether to store in batch mode. The server will respond
        with a HTTP 202 Accepted response code immediately.
        """
        OK = 'ok'


class PutDocumentEnums:
    """
    Enums for put_document parameters.
    """

    class ContentType(str, Enum):
        """
        The type of the input.
        """
        APPLICATION_JSON = 'application/json'
        MULTIPART_MIXED = 'multipart/mixed'
        MULTIPART_RELATED = 'multipart/related'
        APPLICATION_OCTET_STREAM = 'application/octet-stream'
    class Batch(str, Enum):
        """
        Query parameter to specify whether to store in batch mode. The server will respond
        with a HTTP 202 Accepted response code immediately.
        """
        OK = 'ok'


class DeleteDesignDocumentEnums:
    """
    Enums for delete_design_document parameters.
    """

    class Batch(str, Enum):
        """
        Query parameter to specify whether to store in batch mode. The server will respond
        with a HTTP 202 Accepted response code immediately.
        """
        OK = 'ok'


class PutDesignDocumentEnums:
    """
    Enums for put_design_document parameters.
    """

    class Batch(str, Enum):
        """
        Query parameter to specify whether to store in batch mode. The server will respond
        with a HTTP 202 Accepted response code immediately.
        """
        OK = 'ok'


class PostDesignDocsEnums:
    """
    Enums for post_design_docs parameters.
    """

    class Accept(str, Enum):
        """
        The type of the response: application/json or application/octet-stream.
        """
        APPLICATION_JSON = 'application/json'
        APPLICATION_OCTET_STREAM = 'application/octet-stream'


class PostDesignDocsQueriesEnums:
    """
    Enums for post_design_docs_queries parameters.
    """

    class Accept(str, Enum):
        """
        The type of the response: application/json or application/octet-stream.
        """
        APPLICATION_JSON = 'application/json'
        APPLICATION_OCTET_STREAM = 'application/octet-stream'


class DeleteIndexEnums:
    """
    Enums for delete_index parameters.
    """

    class Type(str, Enum):
        """
        Path parameter to specify the index type.
        """
        JSON = 'json'
        SPECIAL = 'special'
        TEXT = 'text'


class GetGeoEnums:
    """
    Enums for get_geo parameters.
    """

    class Format(str, Enum):
        """
        Query parameter that causes the geospatial query output to be returned in the
        specified format.
        """
        LEGACY = 'legacy'
        GEOJSON = 'geojson'
        VIEW = 'view'
        APPLICATION_VND_GEO_JSON = 'application/vnd.geo+json'
    class Relation(str, Enum):
        """
        Query parameter to specify the DE-9IM (Dimensionally Extended nine-Intersection
        Model)geospatial relationship between the query geometry and the result documents.
        """
        CONTAINS = 'contains'
        CONTAINS_PROPERLY = 'contains_properly'
        COVERED_BY = 'covered_by'
        COVERS = 'covers'
        CROSSES = 'crosses'
        DISJOINT = 'disjoint'
        INTERSECTS = 'intersects'
        OVERLAPS = 'overlaps'
        TOUCHES = 'touches'
        WITHIN = 'within'
    class Stale(str, Enum):
        """
        Query parameter to specify to not wait for the index to finish building before
        returning results.
        """
        OK = 'ok'


class GetGeoEnums:
    """
    Enums for get_geo_as_stream parameters.
    """

    class Format(str, Enum):
        """
        Query parameter that causes the geospatial query output to be returned in the
        specified format.
        """
        LEGACY = 'legacy'
        GEOJSON = 'geojson'
        VIEW = 'view'
        APPLICATION_VND_GEO_JSON = 'application/vnd.geo+json'
    class Relation(str, Enum):
        """
        Query parameter to specify the DE-9IM (Dimensionally Extended nine-Intersection
        Model)geospatial relationship between the query geometry and the result documents.
        """
        CONTAINS = 'contains'
        CONTAINS_PROPERLY = 'contains_properly'
        COVERED_BY = 'covered_by'
        COVERS = 'covers'
        CROSSES = 'crosses'
        DISJOINT = 'disjoint'
        INTERSECTS = 'intersects'
        OVERLAPS = 'overlaps'
        TOUCHES = 'touches'
        WITHIN = 'within'
    class Stale(str, Enum):
        """
        Query parameter to specify to not wait for the index to finish building before
        returning results.
        """
        OK = 'ok'


class GetDbUpdatesEnums:
    """
    Enums for get_db_updates parameters.
    """

    class Feed(str, Enum):
        """
        Query parameter to specify the changes feed type.
        """
        CONTINUOUS = 'continuous'
        EVENTSOURCE = 'eventsource'
        LONGPOLL = 'longpoll'
        NORMAL = 'normal'


class DeleteReplicationDocumentEnums:
    """
    Enums for delete_replication_document parameters.
    """

    class Batch(str, Enum):
        """
        Query parameter to specify whether to store in batch mode. The server will respond
        with a HTTP 202 Accepted response code immediately.
        """
        OK = 'ok'


class PutReplicationDocumentEnums:
    """
    Enums for put_replication_document parameters.
    """

    class Batch(str, Enum):
        """
        Query parameter to specify whether to store in batch mode. The server will respond
        with a HTTP 202 Accepted response code immediately.
        """
        OK = 'ok'


class GetSchedulerDocsEnums:
    """
    Enums for get_scheduler_docs parameters.
    """

    class States(str, Enum):
        """
        Query parameter to include only replication documents in the specified states.
        String must be a comma-delimited string.
        """
        INITIALIZING = 'initializing'
        ERROR = 'error'
        PENDING = 'pending'
        RUNNING = 'running'
        CRASHING = 'crashing'
        COMPLETED = 'completed'
        FAILED = 'failed'


class DeleteAttachmentEnums:
    """
    Enums for delete_attachment parameters.
    """

    class Batch(str, Enum):
        """
        Query parameter to specify whether to store in batch mode. The server will respond
        with a HTTP 202 Accepted response code immediately.
        """
        OK = 'ok'


class DeleteLocalDocumentEnums:
    """
    Enums for delete_local_document parameters.
    """

    class Batch(str, Enum):
        """
        Query parameter to specify whether to store in batch mode. The server will respond
        with a HTTP 202 Accepted response code immediately.
        """
        OK = 'ok'


class GetLocalDocumentEnums:
    """
    Enums for get_local_document parameters.
    """

    class Accept(str, Enum):
        """
        The type of the response: application/json, multipart/mixed, multipart/related, or
        application/octet-stream.
        """
        APPLICATION_JSON = 'application/json'
        MULTIPART_MIXED = 'multipart/mixed'
        MULTIPART_RELATED = 'multipart/related'
        APPLICATION_OCTET_STREAM = 'application/octet-stream'


class PutLocalDocumentEnums:
    """
    Enums for put_local_document parameters.
    """

    class ContentType(str, Enum):
        """
        The type of the input.
        """
        APPLICATION_JSON = 'application/json'
        MULTIPART_MIXED = 'multipart/mixed'
        MULTIPART_RELATED = 'multipart/related'
        APPLICATION_OCTET_STREAM = 'application/octet-stream'
    class Batch(str, Enum):
        """
        Query parameter to specify whether to store in batch mode. The server will respond
        with a HTTP 202 Accepted response code immediately.
        """
        OK = 'ok'


class PostLocalDocsEnums:
    """
    Enums for post_local_docs parameters.
    """

    class Accept(str, Enum):
        """
        The type of the response: application/json or application/octet-stream.
        """
        APPLICATION_JSON = 'application/json'
        APPLICATION_OCTET_STREAM = 'application/octet-stream'


class PostLocalDocsQueriesEnums:
    """
    Enums for post_local_docs_queries parameters.
    """

    class Accept(str, Enum):
        """
        The type of the response: application/json or application/octet-stream.
        """
        APPLICATION_JSON = 'application/json'
        APPLICATION_OCTET_STREAM = 'application/octet-stream'


##############################################################################
# Models
##############################################################################


class ActiveTask():
    """
    Schema for information about a running task.

    :attr int changes_done: (optional) Processed changes.
    :attr str database: (optional) Source database.
    :attr str pid: (optional) Process ID.
    :attr int progress: (optional) Current percentage progress.
    :attr int started_on: (optional) Schema for a Unix epoch timestamp.
    :attr str status: (optional) Task status message.
    :attr str task: (optional) Task name.
    :attr int total_changes: (optional) Total changes to process.
    :attr str type: (optional) Operation type.
    :attr int updated_on: (optional) Schema for a Unix epoch timestamp.
    """

    def __init__(self,
                 *,
                 changes_done: int = None,
                 database: str = None,
                 pid: str = None,
                 progress: int = None,
                 started_on: int = None,
                 status: str = None,
                 task: str = None,
                 total_changes: int = None,
                 type: str = None,
                 updated_on: int = None) -> None:
        """
        Initialize a ActiveTask object.

        :param int changes_done: (optional) Processed changes.
        :param str database: (optional) Source database.
        :param str pid: (optional) Process ID.
        :param int progress: (optional) Current percentage progress.
        :param int started_on: (optional) Schema for a Unix epoch timestamp.
        :param str status: (optional) Task status message.
        :param str task: (optional) Task name.
        :param int total_changes: (optional) Total changes to process.
        :param str type: (optional) Operation type.
        :param int updated_on: (optional) Schema for a Unix epoch timestamp.
        """
        self.changes_done = changes_done
        self.database = database
        self.pid = pid
        self.progress = progress
        self.started_on = started_on
        self.status = status
        self.task = task
        self.total_changes = total_changes
        self.type = type
        self.updated_on = updated_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActiveTask':
        """Initialize a ActiveTask object from a json dictionary."""
        args = {}
        if 'changes_done' in _dict:
            args['changes_done'] = _dict.get('changes_done')
        if 'database' in _dict:
            args['database'] = _dict.get('database')
        if 'pid' in _dict:
            args['pid'] = _dict.get('pid')
        if 'progress' in _dict:
            args['progress'] = _dict.get('progress')
        if 'started_on' in _dict:
            args['started_on'] = _dict.get('started_on')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'task' in _dict:
            args['task'] = _dict.get('task')
        if 'total_changes' in _dict:
            args['total_changes'] = _dict.get('total_changes')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'updated_on' in _dict:
            args['updated_on'] = _dict.get('updated_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActiveTask object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'changes_done') and self.changes_done is not None:
            _dict['changes_done'] = self.changes_done
        if hasattr(self, 'database') and self.database is not None:
            _dict['database'] = self.database
        if hasattr(self, 'pid') and self.pid is not None:
            _dict['pid'] = self.pid
        if hasattr(self, 'progress') and self.progress is not None:
            _dict['progress'] = self.progress
        if hasattr(self, 'started_on') and self.started_on is not None:
            _dict['started_on'] = self.started_on
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'task') and self.task is not None:
            _dict['task'] = self.task
        if hasattr(self, 'total_changes') and self.total_changes is not None:
            _dict['total_changes'] = self.total_changes
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = self.updated_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ActiveTask object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ActiveTask') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ActiveTask') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AllDocsQueriesResult():
    """
    Schema for the result of an all documents queries operation.

    :attr List[AllDocsResult] results: An array of result objects - one for each
          query. Each result object contains the same fields as the response to a regular
          `/_all_docs` request.
    """

    def __init__(self,
                 results: List['AllDocsResult']) -> None:
        """
        Initialize a AllDocsQueriesResult object.

        :param List[AllDocsResult] results: An array of result objects - one for
               each query. Each result object contains the same fields as the response to
               a regular `/_all_docs` request.
        """
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AllDocsQueriesResult':
        """Initialize a AllDocsQueriesResult object from a json dictionary."""
        args = {}
        if 'results' in _dict:
            args['results'] = [AllDocsResult.from_dict(x) for x in _dict.get('results')]
        else:
            raise ValueError('Required property \'results\' not present in AllDocsQueriesResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AllDocsQueriesResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x.to_dict() for x in self.results]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AllDocsQueriesResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AllDocsQueriesResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AllDocsQueriesResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AllDocsQuery():
    """
    Schema for an all documents query operation.

    :attr bool att_encoding_info: (optional) Parameter to specify whether to include
          the encoding information in attachment stubs if the particular attachment is
          compressed.
    :attr bool attachments: (optional) Parameter to specify whether to include
          attachments bodies in a response.
    :attr bool conflicts: (optional) Parameter to specify whether to include a list
          of conflicted revisions in the `_conflicts` property of the returned document.
          Ignored if `include_docs` isn't `true`.
    :attr bool descending: (optional) Parameter to specify whether to return the
          documents in descending by key order.
    :attr bool include_docs: (optional) Parameter to specify whether to include the
          full content of the documents in the response.
    :attr bool inclusive_end: (optional) Parameter to specify whether the specified
          end key should be included in the result.
    :attr int limit: (optional) Parameter to specify the number of returned
          documents to limit the result to.
    :attr int skip: (optional) Parameter to specify the number of records before
          starting to return the results.
    :attr bool update_seq: (optional) Parameter to specify whether to include in the
          response an update_seq value indicating the sequence id of the database the view
          reflects.
    :attr str endkey: (optional) Schema for a document ID.
    :attr str key: (optional) Schema for a document ID.
    :attr List[str] keys: (optional) Schema for a list of document IDs.
    :attr str startkey: (optional) Schema for a document ID.
    """

    def __init__(self,
                 *,
                 att_encoding_info: bool = None,
                 attachments: bool = None,
                 conflicts: bool = None,
                 descending: bool = None,
                 include_docs: bool = None,
                 inclusive_end: bool = None,
                 limit: int = None,
                 skip: int = None,
                 update_seq: bool = None,
                 endkey: str = None,
                 key: str = None,
                 keys: List[str] = None,
                 startkey: str = None) -> None:
        """
        Initialize a AllDocsQuery object.

        :param bool att_encoding_info: (optional) Parameter to specify whether to
               include the encoding information in attachment stubs if the particular
               attachment is compressed.
        :param bool attachments: (optional) Parameter to specify whether to include
               attachments bodies in a response.
        :param bool conflicts: (optional) Parameter to specify whether to include a
               list of conflicted revisions in the `_conflicts` property of the returned
               document. Ignored if `include_docs` isn't `true`.
        :param bool descending: (optional) Parameter to specify whether to return
               the documents in descending by key order.
        :param bool include_docs: (optional) Parameter to specify whether to
               include the full content of the documents in the response.
        :param bool inclusive_end: (optional) Parameter to specify whether the
               specified end key should be included in the result.
        :param int limit: (optional) Parameter to specify the number of returned
               documents to limit the result to.
        :param int skip: (optional) Parameter to specify the number of records
               before starting to return the results.
        :param bool update_seq: (optional) Parameter to specify whether to include
               in the response an update_seq value indicating the sequence id of the
               database the view reflects.
        :param str endkey: (optional) Schema for a document ID.
        :param str key: (optional) Schema for a document ID.
        :param List[str] keys: (optional) Schema for a list of document IDs.
        :param str startkey: (optional) Schema for a document ID.
        """
        self.att_encoding_info = att_encoding_info
        self.attachments = attachments
        self.conflicts = conflicts
        self.descending = descending
        self.include_docs = include_docs
        self.inclusive_end = inclusive_end
        self.limit = limit
        self.skip = skip
        self.update_seq = update_seq
        self.endkey = endkey
        self.key = key
        self.keys = keys
        self.startkey = startkey

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AllDocsQuery':
        """Initialize a AllDocsQuery object from a json dictionary."""
        args = {}
        if 'att_encoding_info' in _dict:
            args['att_encoding_info'] = _dict.get('att_encoding_info')
        if 'attachments' in _dict:
            args['attachments'] = _dict.get('attachments')
        if 'conflicts' in _dict:
            args['conflicts'] = _dict.get('conflicts')
        if 'descending' in _dict:
            args['descending'] = _dict.get('descending')
        if 'include_docs' in _dict:
            args['include_docs'] = _dict.get('include_docs')
        if 'inclusive_end' in _dict:
            args['inclusive_end'] = _dict.get('inclusive_end')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'skip' in _dict:
            args['skip'] = _dict.get('skip')
        if 'update_seq' in _dict:
            args['update_seq'] = _dict.get('update_seq')
        if 'endkey' in _dict:
            args['endkey'] = _dict.get('endkey')
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        if 'keys' in _dict:
            args['keys'] = _dict.get('keys')
        if 'startkey' in _dict:
            args['startkey'] = _dict.get('startkey')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AllDocsQuery object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'att_encoding_info') and self.att_encoding_info is not None:
            _dict['att_encoding_info'] = self.att_encoding_info
        if hasattr(self, 'attachments') and self.attachments is not None:
            _dict['attachments'] = self.attachments
        if hasattr(self, 'conflicts') and self.conflicts is not None:
            _dict['conflicts'] = self.conflicts
        if hasattr(self, 'descending') and self.descending is not None:
            _dict['descending'] = self.descending
        if hasattr(self, 'include_docs') and self.include_docs is not None:
            _dict['include_docs'] = self.include_docs
        if hasattr(self, 'inclusive_end') and self.inclusive_end is not None:
            _dict['inclusive_end'] = self.inclusive_end
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'skip') and self.skip is not None:
            _dict['skip'] = self.skip
        if hasattr(self, 'update_seq') and self.update_seq is not None:
            _dict['update_seq'] = self.update_seq
        if hasattr(self, 'endkey') and self.endkey is not None:
            _dict['endkey'] = self.endkey
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self, 'keys') and self.keys is not None:
            _dict['keys'] = self.keys
        if hasattr(self, 'startkey') and self.startkey is not None:
            _dict['startkey'] = self.startkey
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AllDocsQuery object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AllDocsQuery') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AllDocsQuery') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AllDocsResult():
    """
    Schema for the result of an all documents operation.

    :attr int total_rows: (optional) Number of total rows.
    :attr List[DocsResultRow] rows: (optional) List of doc results.
    :attr str update_seq: (optional) Current update sequence for the database.
    """

    def __init__(self,
                 *,
                 total_rows: int = None,
                 rows: List['DocsResultRow'] = None,
                 update_seq: str = None) -> None:
        """
        Initialize a AllDocsResult object.

        :param int total_rows: (optional) Number of total rows.
        :param List[DocsResultRow] rows: (optional) List of doc results.
        :param str update_seq: (optional) Current update sequence for the database.
        """
        self.total_rows = total_rows
        self.rows = rows
        self.update_seq = update_seq

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AllDocsResult':
        """Initialize a AllDocsResult object from a json dictionary."""
        args = {}
        if 'total_rows' in _dict:
            args['total_rows'] = _dict.get('total_rows')
        if 'rows' in _dict:
            args['rows'] = [DocsResultRow.from_dict(x) for x in _dict.get('rows')]
        if 'update_seq' in _dict:
            args['update_seq'] = _dict.get('update_seq')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AllDocsResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_rows') and self.total_rows is not None:
            _dict['total_rows'] = self.total_rows
        if hasattr(self, 'rows') and self.rows is not None:
            _dict['rows'] = [x.to_dict() for x in self.rows]
        if hasattr(self, 'update_seq') and self.update_seq is not None:
            _dict['update_seq'] = self.update_seq
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AllDocsResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AllDocsResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AllDocsResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Analyzer():
    """
    Schema for a full text search analyzer.

    :attr str name: (optional) Schema for the name of the Apache Lucene analyzer to
          use for text indexing. The default value varies depending on the analyzer usage:
          * For search indexes the default is `standard` * For query text indexes the
          default is `keyword` * For a query text index default_field the default is
          `standard`.
    :attr List[str] stopwords: (optional) Custom stopwords to use with the named
          analyzer.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 stopwords: List[str] = None) -> None:
        """
        Initialize a Analyzer object.

        :param str name: (optional) Schema for the name of the Apache Lucene
               analyzer to use for text indexing. The default value varies depending on
               the analyzer usage:
               * For search indexes the default is `standard` * For query text indexes the
               default is `keyword` * For a query text index default_field the default is
               `standard`.
        :param List[str] stopwords: (optional) Custom stopwords to use with the
               named analyzer.
        """
        self.name = name
        self.stopwords = stopwords

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Analyzer':
        """Initialize a Analyzer object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'stopwords' in _dict:
            args['stopwords'] = _dict.get('stopwords')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Analyzer object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'stopwords') and self.stopwords is not None:
            _dict['stopwords'] = self.stopwords
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Analyzer object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Analyzer') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Analyzer') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class NameEnum(str, Enum):
        """
        Schema for the name of the Apache Lucene analyzer to use for text indexing. The
        default value varies depending on the analyzer usage:
        * For search indexes the default is `standard` * For query text indexes the
        default is `keyword` * For a query text index default_field the default is
        `standard`.
        """
        CLASSIC = 'classic'
        EMAIL = 'email'
        KEYWORD = 'keyword'
        SIMPLE = 'simple'
        STANDARD = 'standard'
        WHITESPACE = 'whitespace'
        ARABIC = 'arabic'
        ARMENIAN = 'armenian'
        BASQUE = 'basque'
        BULGARIAN = 'bulgarian'
        BRAZILIAN = 'brazilian'
        CATALAN = 'catalan'
        CJK = 'cjk'
        CHINESE = 'chinese'
        CZECH = 'czech'
        DANISH = 'danish'
        DUTCH = 'dutch'
        ENGLISH = 'english'
        FINNISH = 'finnish'
        FRENCH = 'french'
        GERMAN = 'german'
        GREEK = 'greek'
        GALICIAN = 'galician'
        HINDI = 'hindi'
        HUNGARIAN = 'hungarian'
        INDONESIAN = 'indonesian'
        IRISH = 'irish'
        ITALIAN = 'italian'
        JAPANESE = 'japanese'
        LATVIAN = 'latvian'
        NORWEGIAN = 'norwegian'
        PERSIAN = 'persian'
        POLISH = 'polish'
        PORTUGUESE = 'portuguese'
        ROMANIAN = 'romanian'
        RUSSIAN = 'russian'
        SPANISH = 'spanish'
        SWEDISH = 'swedish'
        THAI = 'thai'
        TURKISH = 'turkish'
        PERFIELD = 'perfield'


class AnalyzerConfiguration():
    """
    Schema for a search analyzer configuration.

    :attr str name: (optional) Schema for the name of the Apache Lucene analyzer to
          use for text indexing. The default value varies depending on the analyzer usage:
          * For search indexes the default is `standard` * For query text indexes the
          default is `keyword` * For a query text index default_field the default is
          `standard`.
    :attr List[str] stopwords: (optional) Custom stopwords to use with the named
          analyzer.
    :attr dict fields: (optional) Schema for mapping a field name to a per field
          analyzer.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 stopwords: List[str] = None,
                 fields: dict = None) -> None:
        """
        Initialize a AnalyzerConfiguration object.

        :param str name: (optional) Schema for the name of the Apache Lucene
               analyzer to use for text indexing. The default value varies depending on
               the analyzer usage:
               * For search indexes the default is `standard` * For query text indexes the
               default is `keyword` * For a query text index default_field the default is
               `standard`.
        :param List[str] stopwords: (optional) Custom stopwords to use with the
               named analyzer.
        :param dict fields: (optional) Schema for mapping a field name to a per
               field analyzer.
        """
        self.name = name
        self.stopwords = stopwords
        self.fields = fields

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyzerConfiguration':
        """Initialize a AnalyzerConfiguration object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'stopwords' in _dict:
            args['stopwords'] = _dict.get('stopwords')
        if 'fields' in _dict:
            args['fields'] = {k : Analyzer.from_dict(v) for k, v in _dict.get('fields').items()}
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyzerConfiguration object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'stopwords') and self.stopwords is not None:
            _dict['stopwords'] = self.stopwords
        if hasattr(self, 'fields') and self.fields is not None:
            _dict['fields'] = {k : v.to_dict() for k, v in self.fields.items()}
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyzerConfiguration object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyzerConfiguration') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyzerConfiguration') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class NameEnum(str, Enum):
        """
        Schema for the name of the Apache Lucene analyzer to use for text indexing. The
        default value varies depending on the analyzer usage:
        * For search indexes the default is `standard` * For query text indexes the
        default is `keyword` * For a query text index default_field the default is
        `standard`.
        """
        CLASSIC = 'classic'
        EMAIL = 'email'
        KEYWORD = 'keyword'
        SIMPLE = 'simple'
        STANDARD = 'standard'
        WHITESPACE = 'whitespace'
        ARABIC = 'arabic'
        ARMENIAN = 'armenian'
        BASQUE = 'basque'
        BULGARIAN = 'bulgarian'
        BRAZILIAN = 'brazilian'
        CATALAN = 'catalan'
        CJK = 'cjk'
        CHINESE = 'chinese'
        CZECH = 'czech'
        DANISH = 'danish'
        DUTCH = 'dutch'
        ENGLISH = 'english'
        FINNISH = 'finnish'
        FRENCH = 'french'
        GERMAN = 'german'
        GREEK = 'greek'
        GALICIAN = 'galician'
        HINDI = 'hindi'
        HUNGARIAN = 'hungarian'
        INDONESIAN = 'indonesian'
        IRISH = 'irish'
        ITALIAN = 'italian'
        JAPANESE = 'japanese'
        LATVIAN = 'latvian'
        NORWEGIAN = 'norwegian'
        PERSIAN = 'persian'
        POLISH = 'polish'
        PORTUGUESE = 'portuguese'
        ROMANIAN = 'romanian'
        RUSSIAN = 'russian'
        SPANISH = 'spanish'
        SWEDISH = 'swedish'
        THAI = 'thai'
        TURKISH = 'turkish'
        PERFIELD = 'perfield'


class ApiKeysResult():
    """
    Schema for api keys.

    :attr str key: (optional) The generated api key.
    :attr Ok ok: (optional) Schema for an OK result.
    :attr str password: (optional) The password associated with the api key.
    """

    def __init__(self,
                 *,
                 key: str = None,
                 ok: 'Ok' = None,
                 password: str = None) -> None:
        """
        Initialize a ApiKeysResult object.

        :param str key: (optional) The generated api key.
        :param Ok ok: (optional) Schema for an OK result.
        :param str password: (optional) The password associated with the api key.
        """
        self.key = key
        self.ok = ok
        self.password = password

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiKeysResult':
        """Initialize a ApiKeysResult object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        if 'ok' in _dict:
            args['ok'] = Ok.from_dict(_dict.get('ok'))
        if 'password' in _dict:
            args['password'] = _dict.get('password')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiKeysResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self, 'ok') and self.ok is not None:
            _dict['ok'] = self.ok.to_dict()
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiKeysResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiKeysResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiKeysResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Attachment():
    """
    Schema for an attachment.

    :attr str content_type: (optional) Attachment MIME type.
    :attr bytes data: (optional) Base64-encoded content. Available if attachment
          content is requested by using the query parameters `attachments=true` or
          `atts_since`. Note that when used with a view or changes feed `include_docs`
          must also be `true`.
    :attr str digest: (optional) Content hash digest. It starts with prefix which
          announce hash type (e.g. `md5-`) and continues with Base64-encoded hash digest.
    :attr int encoded_length: (optional) Compressed attachment size in bytes.
          Available if content_type was in list of compressible types when the attachment
          was added and the query parameter `att_encoding_info` is `true`. Note that when
          used with a view or changes feed `include_docs` must also be `true`.
    :attr str encoding: (optional) Compression codec. Available if content_type was
          in list of compressible types when the attachment was added and the and the
          query parameter `att_encoding_info` is `true`. Note that when used with a view
          or changes feed `include_docs` must also be `true`.
    :attr bool follows: (optional) True if the attachment follows in a multipart
          request or response.
    :attr int length: (optional) Real attachment size in bytes. Not available if
          inline attachment content requested.
    :attr int revpos: (optional) Revision number when attachment was added.
    :attr bool stub: (optional) Has `true` value if object contains stub info and no
          content. Otherwise omitted in response.
    """

    def __init__(self,
                 *,
                 content_type: str = None,
                 data: bytes = None,
                 digest: str = None,
                 encoded_length: int = None,
                 encoding: str = None,
                 follows: bool = None,
                 length: int = None,
                 revpos: int = None,
                 stub: bool = None) -> None:
        """
        Initialize a Attachment object.

        :param str content_type: (optional) Attachment MIME type.
        :param bytes data: (optional) Base64-encoded content. Available if
               attachment content is requested by using the query parameters
               `attachments=true` or `atts_since`. Note that when used with a view or
               changes feed `include_docs` must also be `true`.
        :param str digest: (optional) Content hash digest. It starts with prefix
               which announce hash type (e.g. `md5-`) and continues with Base64-encoded
               hash digest.
        :param int encoded_length: (optional) Compressed attachment size in bytes.
               Available if content_type was in list of compressible types when the
               attachment was added and the query parameter `att_encoding_info` is `true`.
               Note that when used with a view or changes feed `include_docs` must also be
               `true`.
        :param str encoding: (optional) Compression codec. Available if
               content_type was in list of compressible types when the attachment was
               added and the and the query parameter `att_encoding_info` is `true`. Note
               that when used with a view or changes feed `include_docs` must also be
               `true`.
        :param bool follows: (optional) True if the attachment follows in a
               multipart request or response.
        :param int length: (optional) Real attachment size in bytes. Not available
               if inline attachment content requested.
        :param int revpos: (optional) Revision number when attachment was added.
        :param bool stub: (optional) Has `true` value if object contains stub info
               and no content. Otherwise omitted in response.
        """
        self.content_type = content_type
        self.data = data
        self.digest = digest
        self.encoded_length = encoded_length
        self.encoding = encoding
        self.follows = follows
        self.length = length
        self.revpos = revpos
        self.stub = stub

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Attachment':
        """Initialize a Attachment object from a json dictionary."""
        args = {}
        if 'content_type' in _dict:
            args['content_type'] = _dict.get('content_type')
        if 'data' in _dict:
            args['data'] = base64.b64decode(_dict.get('data'))
        if 'digest' in _dict:
            args['digest'] = _dict.get('digest')
        if 'encoded_length' in _dict:
            args['encoded_length'] = _dict.get('encoded_length')
        if 'encoding' in _dict:
            args['encoding'] = _dict.get('encoding')
        if 'follows' in _dict:
            args['follows'] = _dict.get('follows')
        if 'length' in _dict:
            args['length'] = _dict.get('length')
        if 'revpos' in _dict:
            args['revpos'] = _dict.get('revpos')
        if 'stub' in _dict:
            args['stub'] = _dict.get('stub')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Attachment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'content_type') and self.content_type is not None:
            _dict['content_type'] = self.content_type
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = str(base64.b64encode(self.data), 'utf-8')
        if hasattr(self, 'digest') and self.digest is not None:
            _dict['digest'] = self.digest
        if hasattr(self, 'encoded_length') and self.encoded_length is not None:
            _dict['encoded_length'] = self.encoded_length
        if hasattr(self, 'encoding') and self.encoding is not None:
            _dict['encoding'] = self.encoding
        if hasattr(self, 'follows') and self.follows is not None:
            _dict['follows'] = self.follows
        if hasattr(self, 'length') and self.length is not None:
            _dict['length'] = self.length
        if hasattr(self, 'revpos') and self.revpos is not None:
            _dict['revpos'] = self.revpos
        if hasattr(self, 'stub') and self.stub is not None:
            _dict['stub'] = self.stub
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Attachment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Attachment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Attachment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class BulkDocs():
    """
    Schema for submitting documents for bulk modifications.

    :attr List[Document] docs: (optional) Array of documents.
    :attr bool new_edits: (optional) If `false`, prevents the database from
          assigning them new revision IDs. Default is `true`.
    """

    def __init__(self,
                 *,
                 docs: List['Document'] = None,
                 new_edits: bool = None) -> None:
        """
        Initialize a BulkDocs object.

        :param List[Document] docs: (optional) Array of documents.
        :param bool new_edits: (optional) If `false`, prevents the database from
               assigning them new revision IDs. Default is `true`.
        """
        self.docs = docs
        self.new_edits = new_edits

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BulkDocs':
        """Initialize a BulkDocs object from a json dictionary."""
        args = {}
        if 'docs' in _dict:
            args['docs'] = [Document.from_dict(x) for x in _dict.get('docs')]
        if 'new_edits' in _dict:
            args['new_edits'] = _dict.get('new_edits')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BulkDocs object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'docs') and self.docs is not None:
            _dict['docs'] = [x.to_dict() for x in self.docs]
        if hasattr(self, 'new_edits') and self.new_edits is not None:
            _dict['new_edits'] = self.new_edits
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BulkDocs object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BulkDocs') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BulkDocs') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class BulkGetQueryDocument():
    """
    Schema for a document item in a bulk get query.

    :attr List[str] atts_since: (optional) Includes attachments only since specified
          revisions.
    :attr str id: Schema for a document ID.
    :attr List[str] open_revs: (optional) Retrieves documents of specified leaf
          revisions.
    :attr str rev: (optional) Schema for a document revision identifier.
    """

    def __init__(self,
                 id: str,
                 *,
                 atts_since: List[str] = None,
                 open_revs: List[str] = None,
                 rev: str = None) -> None:
        """
        Initialize a BulkGetQueryDocument object.

        :param str id: Schema for a document ID.
        :param List[str] atts_since: (optional) Includes attachments only since
               specified revisions.
        :param List[str] open_revs: (optional) Retrieves documents of specified
               leaf revisions.
        :param str rev: (optional) Schema for a document revision identifier.
        """
        self.atts_since = atts_since
        self.id = id
        self.open_revs = open_revs
        self.rev = rev

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BulkGetQueryDocument':
        """Initialize a BulkGetQueryDocument object from a json dictionary."""
        args = {}
        if 'atts_since' in _dict:
            args['atts_since'] = _dict.get('atts_since')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in BulkGetQueryDocument JSON')
        if 'open_revs' in _dict:
            args['open_revs'] = _dict.get('open_revs')
        if 'rev' in _dict:
            args['rev'] = _dict.get('rev')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BulkGetQueryDocument object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'atts_since') and self.atts_since is not None:
            _dict['atts_since'] = self.atts_since
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'open_revs') and self.open_revs is not None:
            _dict['open_revs'] = self.open_revs
        if hasattr(self, 'rev') and self.rev is not None:
            _dict['rev'] = self.rev
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BulkGetQueryDocument object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BulkGetQueryDocument') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BulkGetQueryDocument') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class BulkGetResult():
    """
    Schema for the results object of a bulk get operation.

    :attr List[BulkGetResultItem] results: (optional) Results.
    """

    def __init__(self,
                 *,
                 results: List['BulkGetResultItem'] = None) -> None:
        """
        Initialize a BulkGetResult object.

        :param List[BulkGetResultItem] results: (optional) Results.
        """
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BulkGetResult':
        """Initialize a BulkGetResult object from a json dictionary."""
        args = {}
        if 'results' in _dict:
            args['results'] = [BulkGetResultItem.from_dict(x) for x in _dict.get('results')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BulkGetResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x.to_dict() for x in self.results]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BulkGetResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BulkGetResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BulkGetResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class BulkGetResultDocument():
    """
    Schema for BulkGetResult object containing a successfully retrieved document or error
    information.

    :attr DocumentResult error: (optional) Schema for the result of a document
          modification.
    :attr Document ok: (optional) Schema for a document.
    """

    def __init__(self,
                 *,
                 error: 'DocumentResult' = None,
                 ok: 'Document' = None) -> None:
        """
        Initialize a BulkGetResultDocument object.

        :param DocumentResult error: (optional) Schema for the result of a document
               modification.
        :param Document ok: (optional) Schema for a document.
        """
        self.error = error
        self.ok = ok

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BulkGetResultDocument':
        """Initialize a BulkGetResultDocument object from a json dictionary."""
        args = {}
        if 'error' in _dict:
            args['error'] = DocumentResult.from_dict(_dict.get('error'))
        if 'ok' in _dict:
            args['ok'] = Document.from_dict(_dict.get('ok'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BulkGetResultDocument object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error.to_dict()
        if hasattr(self, 'ok') and self.ok is not None:
            _dict['ok'] = self.ok.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BulkGetResultDocument object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BulkGetResultDocument') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BulkGetResultDocument') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class BulkGetResultItem():
    """
    Schema for the document revisions information from a bulk get operation.

    :attr List[BulkGetResultDocument] docs: (optional) Array of document revisions
          or error information.
    :attr str id: (optional) Schema for a document ID.
    """

    def __init__(self,
                 *,
                 docs: List['BulkGetResultDocument'] = None,
                 id: str = None) -> None:
        """
        Initialize a BulkGetResultItem object.

        :param List[BulkGetResultDocument] docs: (optional) Array of document
               revisions or error information.
        :param str id: (optional) Schema for a document ID.
        """
        self.docs = docs
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BulkGetResultItem':
        """Initialize a BulkGetResultItem object from a json dictionary."""
        args = {}
        if 'docs' in _dict:
            args['docs'] = [BulkGetResultDocument.from_dict(x) for x in _dict.get('docs')]
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BulkGetResultItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'docs') and self.docs is not None:
            _dict['docs'] = [x.to_dict() for x in self.docs]
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BulkGetResultItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BulkGetResultItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BulkGetResultItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Change():
    """
    Schema for a document leaf with single field rev.

    :attr str rev: (optional) Schema for a document revision identifier.
    """

    def __init__(self,
                 *,
                 rev: str = None) -> None:
        """
        Initialize a Change object.

        :param str rev: (optional) Schema for a document revision identifier.
        """
        self.rev = rev

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Change':
        """Initialize a Change object from a json dictionary."""
        args = {}
        if 'rev' in _dict:
            args['rev'] = _dict.get('rev')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Change object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'rev') and self.rev is not None:
            _dict['rev'] = self.rev
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Change object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Change') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Change') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ChangesResult():
    """
    Schema for normal changes feed result.

    :attr str last_seq: (optional) last_seq.
    :attr int pending: (optional) pending.
    :attr List[ChangesResultItem] results: (optional) results.
    """

    def __init__(self,
                 *,
                 last_seq: str = None,
                 pending: int = None,
                 results: List['ChangesResultItem'] = None) -> None:
        """
        Initialize a ChangesResult object.

        :param str last_seq: (optional) last_seq.
        :param int pending: (optional) pending.
        :param List[ChangesResultItem] results: (optional) results.
        """
        self.last_seq = last_seq
        self.pending = pending
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ChangesResult':
        """Initialize a ChangesResult object from a json dictionary."""
        args = {}
        if 'last_seq' in _dict:
            args['last_seq'] = _dict.get('last_seq')
        if 'pending' in _dict:
            args['pending'] = _dict.get('pending')
        if 'results' in _dict:
            args['results'] = [ChangesResultItem.from_dict(x) for x in _dict.get('results')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ChangesResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'last_seq') and self.last_seq is not None:
            _dict['last_seq'] = self.last_seq
        if hasattr(self, 'pending') and self.pending is not None:
            _dict['pending'] = self.pending
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x.to_dict() for x in self.results]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ChangesResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ChangesResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ChangesResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ChangesResultItem():
    """
    Schema for an item in the changes results array.

    :attr List[Change] changes: (optional) List of document's leaves with single
          field rev.
    :attr bool deleted: (optional) if `true` then the document is deleted.
    :attr str id: (optional) Schema for a document ID.
    :attr str seq: (optional) Update sequence.
    """

    def __init__(self,
                 *,
                 changes: List['Change'] = None,
                 deleted: bool = None,
                 id: str = None,
                 seq: str = None) -> None:
        """
        Initialize a ChangesResultItem object.

        :param List[Change] changes: (optional) List of document's leaves with
               single field rev.
        :param bool deleted: (optional) if `true` then the document is deleted.
        :param str id: (optional) Schema for a document ID.
        :param str seq: (optional) Update sequence.
        """
        self.changes = changes
        self.deleted = deleted
        self.id = id
        self.seq = seq

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ChangesResultItem':
        """Initialize a ChangesResultItem object from a json dictionary."""
        args = {}
        if 'changes' in _dict:
            args['changes'] = [Change.from_dict(x) for x in _dict.get('changes')]
        if 'deleted' in _dict:
            args['deleted'] = _dict.get('deleted')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'seq' in _dict:
            args['seq'] = _dict.get('seq')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ChangesResultItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'changes') and self.changes is not None:
            _dict['changes'] = [x.to_dict() for x in self.changes]
        if hasattr(self, 'deleted') and self.deleted is not None:
            _dict['deleted'] = self.deleted
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'seq') and self.seq is not None:
            _dict['seq'] = self.seq
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ChangesResultItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ChangesResultItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ChangesResultItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ContentInformationSizes():
    """
    Schema for size information of content.

    :attr int active: (optional) The active size of the content, in bytes.
    :attr int external: (optional) The total uncompressed size of the content, in
          bytes.
    :attr int file: (optional) The total size of the content as stored on disk, in
          bytes.
    """

    def __init__(self,
                 *,
                 active: int = None,
                 external: int = None,
                 file: int = None) -> None:
        """
        Initialize a ContentInformationSizes object.

        :param int active: (optional) The active size of the content, in bytes.
        :param int external: (optional) The total uncompressed size of the content,
               in bytes.
        :param int file: (optional) The total size of the content as stored on
               disk, in bytes.
        """
        self.active = active
        self.external = external
        self.file = file

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContentInformationSizes':
        """Initialize a ContentInformationSizes object from a json dictionary."""
        args = {}
        if 'active' in _dict:
            args['active'] = _dict.get('active')
        if 'external' in _dict:
            args['external'] = _dict.get('external')
        if 'file' in _dict:
            args['file'] = _dict.get('file')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContentInformationSizes object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'active') and self.active is not None:
            _dict['active'] = self.active
        if hasattr(self, 'external') and self.external is not None:
            _dict['external'] = self.external
        if hasattr(self, 'file') and self.file is not None:
            _dict['file'] = self.file
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContentInformationSizes object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ContentInformationSizes') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContentInformationSizes') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CorsConfiguration():
    """
    Schema for a CORS configuration.

    :attr bool allow_credentials: (optional) Boolean value to allow authentication
          credentials. If set to true, browser requests must be done by using
          withCredentials = true.
    :attr bool enable_cors: (optional) Boolean value to turn CORS on and off.
    :attr List[str] origins: An array of strings that contain allowed origin
          domains. You have to specify the full URL including the protocol. It is
          recommended that only the HTTPS protocol is used. Subdomains count as separate
          domains, so you have to specify all subdomains used.
    """

    def __init__(self,
                 origins: List[str],
                 *,
                 allow_credentials: bool = None,
                 enable_cors: bool = None) -> None:
        """
        Initialize a CorsConfiguration object.

        :param List[str] origins: An array of strings that contain allowed origin
               domains. You have to specify the full URL including the protocol. It is
               recommended that only the HTTPS protocol is used. Subdomains count as
               separate domains, so you have to specify all subdomains used.
        :param bool allow_credentials: (optional) Boolean value to allow
               authentication credentials. If set to true, browser requests must be done
               by using withCredentials = true.
        :param bool enable_cors: (optional) Boolean value to turn CORS on and off.
        """
        self.allow_credentials = allow_credentials
        self.enable_cors = enable_cors
        self.origins = origins

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CorsConfiguration':
        """Initialize a CorsConfiguration object from a json dictionary."""
        args = {}
        if 'allow_credentials' in _dict:
            args['allow_credentials'] = _dict.get('allow_credentials')
        if 'enable_cors' in _dict:
            args['enable_cors'] = _dict.get('enable_cors')
        if 'origins' in _dict:
            args['origins'] = _dict.get('origins')
        else:
            raise ValueError('Required property \'origins\' not present in CorsConfiguration JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CorsConfiguration object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'allow_credentials') and self.allow_credentials is not None:
            _dict['allow_credentials'] = self.allow_credentials
        if hasattr(self, 'enable_cors') and self.enable_cors is not None:
            _dict['enable_cors'] = self.enable_cors
        if hasattr(self, 'origins') and self.origins is not None:
            _dict['origins'] = self.origins
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CorsConfiguration object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CorsConfiguration') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CorsConfiguration') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DatabaseInformation():
    """
    Schema for information about a database.

    :attr DatabaseInformationCluster cluster: (optional) Schema for database cluster
          information.
    :attr str committed_update_seq: (optional) An opaque string that describes the
          committed state of the database.
    :attr bool compact_running: (optional) True if the database compaction routine
          is operating on this database.
    :attr str compacted_seq: (optional) An opaque string that describes the
          compaction state of the database.
    :attr str db_name: (optional) The name of the database.
    :attr int disk_format_version: (optional) The version of the physical format
          used for the data when it is stored on disk.
    :attr int doc_count: (optional) A count of the documents in the specified
          database.
    :attr int doc_del_count: (optional) Number of deleted documents.
    :attr str engine: (optional) The engine used for the database.
    :attr DatabaseInformationProps props: (optional) Schema for database properties.
    :attr ContentInformationSizes sizes: (optional) Schema for size information of
          content.
    :attr str update_seq: (optional) An opaque string that describes the state of
          the database. Do not rely on this string for counting the number of updates.
    :attr str uuid: (optional) The UUID of the database.
    """

    def __init__(self,
                 *,
                 cluster: 'DatabaseInformationCluster' = None,
                 committed_update_seq: str = None,
                 compact_running: bool = None,
                 compacted_seq: str = None,
                 db_name: str = None,
                 disk_format_version: int = None,
                 doc_count: int = None,
                 doc_del_count: int = None,
                 engine: str = None,
                 props: 'DatabaseInformationProps' = None,
                 sizes: 'ContentInformationSizes' = None,
                 update_seq: str = None,
                 uuid: str = None) -> None:
        """
        Initialize a DatabaseInformation object.

        :param DatabaseInformationCluster cluster: (optional) Schema for database
               cluster information.
        :param str committed_update_seq: (optional) An opaque string that describes
               the committed state of the database.
        :param bool compact_running: (optional) True if the database compaction
               routine is operating on this database.
        :param str compacted_seq: (optional) An opaque string that describes the
               compaction state of the database.
        :param str db_name: (optional) The name of the database.
        :param int disk_format_version: (optional) The version of the physical
               format used for the data when it is stored on disk.
        :param int doc_count: (optional) A count of the documents in the specified
               database.
        :param int doc_del_count: (optional) Number of deleted documents.
        :param str engine: (optional) The engine used for the database.
        :param DatabaseInformationProps props: (optional) Schema for database
               properties.
        :param ContentInformationSizes sizes: (optional) Schema for size
               information of content.
        :param str update_seq: (optional) An opaque string that describes the state
               of the database. Do not rely on this string for counting the number of
               updates.
        :param str uuid: (optional) The UUID of the database.
        """
        self.cluster = cluster
        self.committed_update_seq = committed_update_seq
        self.compact_running = compact_running
        self.compacted_seq = compacted_seq
        self.db_name = db_name
        self.disk_format_version = disk_format_version
        self.doc_count = doc_count
        self.doc_del_count = doc_del_count
        self.engine = engine
        self.props = props
        self.sizes = sizes
        self.update_seq = update_seq
        self.uuid = uuid

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DatabaseInformation':
        """Initialize a DatabaseInformation object from a json dictionary."""
        args = {}
        if 'cluster' in _dict:
            args['cluster'] = DatabaseInformationCluster.from_dict(_dict.get('cluster'))
        if 'committed_update_seq' in _dict:
            args['committed_update_seq'] = _dict.get('committed_update_seq')
        if 'compact_running' in _dict:
            args['compact_running'] = _dict.get('compact_running')
        if 'compacted_seq' in _dict:
            args['compacted_seq'] = _dict.get('compacted_seq')
        if 'db_name' in _dict:
            args['db_name'] = _dict.get('db_name')
        if 'disk_format_version' in _dict:
            args['disk_format_version'] = _dict.get('disk_format_version')
        if 'doc_count' in _dict:
            args['doc_count'] = _dict.get('doc_count')
        if 'doc_del_count' in _dict:
            args['doc_del_count'] = _dict.get('doc_del_count')
        if 'engine' in _dict:
            args['engine'] = _dict.get('engine')
        if 'props' in _dict:
            args['props'] = DatabaseInformationProps.from_dict(_dict.get('props'))
        if 'sizes' in _dict:
            args['sizes'] = ContentInformationSizes.from_dict(_dict.get('sizes'))
        if 'update_seq' in _dict:
            args['update_seq'] = _dict.get('update_seq')
        if 'uuid' in _dict:
            args['uuid'] = _dict.get('uuid')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DatabaseInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cluster') and self.cluster is not None:
            _dict['cluster'] = self.cluster.to_dict()
        if hasattr(self, 'committed_update_seq') and self.committed_update_seq is not None:
            _dict['committed_update_seq'] = self.committed_update_seq
        if hasattr(self, 'compact_running') and self.compact_running is not None:
            _dict['compact_running'] = self.compact_running
        if hasattr(self, 'compacted_seq') and self.compacted_seq is not None:
            _dict['compacted_seq'] = self.compacted_seq
        if hasattr(self, 'db_name') and self.db_name is not None:
            _dict['db_name'] = self.db_name
        if hasattr(self, 'disk_format_version') and self.disk_format_version is not None:
            _dict['disk_format_version'] = self.disk_format_version
        if hasattr(self, 'doc_count') and self.doc_count is not None:
            _dict['doc_count'] = self.doc_count
        if hasattr(self, 'doc_del_count') and self.doc_del_count is not None:
            _dict['doc_del_count'] = self.doc_del_count
        if hasattr(self, 'engine') and self.engine is not None:
            _dict['engine'] = self.engine
        if hasattr(self, 'props') and self.props is not None:
            _dict['props'] = self.props.to_dict()
        if hasattr(self, 'sizes') and self.sizes is not None:
            _dict['sizes'] = self.sizes.to_dict()
        if hasattr(self, 'update_seq') and self.update_seq is not None:
            _dict['update_seq'] = self.update_seq
        if hasattr(self, 'uuid') and self.uuid is not None:
            _dict['uuid'] = self.uuid
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DatabaseInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DatabaseInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DatabaseInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DatabaseInformationCluster():
    """
    Schema for database cluster information.

    :attr int n: (optional) Schema for the number of replicas of a database in a
          cluster.
    :attr int q: (optional) Schema for the number of shards in a database. Each
          shard is a partition of the hash value range.
    :attr int r: (optional) Read quorum. The number of consistent copies of a
          document that need to be read before a successful reply.
    :attr int w: (optional) Write quorum. The number of copies of a document that
          need to be written before a successful reply.
    """

    def __init__(self,
                 *,
                 n: int = None,
                 q: int = None,
                 r: int = None,
                 w: int = None) -> None:
        """
        Initialize a DatabaseInformationCluster object.

        :param int n: (optional) Schema for the number of replicas of a database in
               a cluster.
        :param int q: (optional) Schema for the number of shards in a database.
               Each shard is a partition of the hash value range.
        :param int r: (optional) Read quorum. The number of consistent copies of a
               document that need to be read before a successful reply.
        :param int w: (optional) Write quorum. The number of copies of a document
               that need to be written before a successful reply.
        """
        self.n = n
        self.q = q
        self.r = r
        self.w = w

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DatabaseInformationCluster':
        """Initialize a DatabaseInformationCluster object from a json dictionary."""
        args = {}
        if 'n' in _dict:
            args['n'] = _dict.get('n')
        if 'q' in _dict:
            args['q'] = _dict.get('q')
        if 'r' in _dict:
            args['r'] = _dict.get('r')
        if 'w' in _dict:
            args['w'] = _dict.get('w')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DatabaseInformationCluster object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'n') and self.n is not None:
            _dict['n'] = self.n
        if hasattr(self, 'q') and self.q is not None:
            _dict['q'] = self.q
        if hasattr(self, 'r') and self.r is not None:
            _dict['r'] = self.r
        if hasattr(self, 'w') and self.w is not None:
            _dict['w'] = self.w
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DatabaseInformationCluster object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DatabaseInformationCluster') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DatabaseInformationCluster') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DatabaseInformationProps():
    """
    Schema for database properties.

    :attr bool partitioned: (optional) The value is `true` for a partitioned
          database.
    """

    def __init__(self,
                 *,
                 partitioned: bool = None) -> None:
        """
        Initialize a DatabaseInformationProps object.

        :param bool partitioned: (optional) The value is `true` for a partitioned
               database.
        """
        self.partitioned = partitioned

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DatabaseInformationProps':
        """Initialize a DatabaseInformationProps object from a json dictionary."""
        args = {}
        if 'partitioned' in _dict:
            args['partitioned'] = _dict.get('partitioned')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DatabaseInformationProps object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'partitioned') and self.partitioned is not None:
            _dict['partitioned'] = self.partitioned
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DatabaseInformationProps object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DatabaseInformationProps') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DatabaseInformationProps') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DbEvent():
    """
    Schema for a database change event.

    :attr str account: (optional) Account name.
    :attr str dbname: (optional) Database name.
    :attr str seq: (optional) Sequence number.
    :attr str type: (optional) A database event.
    """

    def __init__(self,
                 *,
                 account: str = None,
                 dbname: str = None,
                 seq: str = None,
                 type: str = None) -> None:
        """
        Initialize a DbEvent object.

        :param str account: (optional) Account name.
        :param str dbname: (optional) Database name.
        :param str seq: (optional) Sequence number.
        :param str type: (optional) A database event.
        """
        self.account = account
        self.dbname = dbname
        self.seq = seq
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DbEvent':
        """Initialize a DbEvent object from a json dictionary."""
        args = {}
        if 'account' in _dict:
            args['account'] = _dict.get('account')
        if 'dbname' in _dict:
            args['dbname'] = _dict.get('dbname')
        if 'seq' in _dict:
            args['seq'] = _dict.get('seq')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DbEvent object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'account') and self.account is not None:
            _dict['account'] = self.account
        if hasattr(self, 'dbname') and self.dbname is not None:
            _dict['dbname'] = self.dbname
        if hasattr(self, 'seq') and self.seq is not None:
            _dict['seq'] = self.seq
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DbEvent object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DbEvent') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DbEvent') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        A database event.
        """
        CREATED = 'created'
        DELETED = 'deleted'
        UPDATED = 'updated'


class DbUpdates():
    """
    Schema for database updates.

    :attr str last_seq: (optional) Last sequence number.
    :attr List[DbEvent] results: (optional) results.
    """

    def __init__(self,
                 *,
                 last_seq: str = None,
                 results: List['DbEvent'] = None) -> None:
        """
        Initialize a DbUpdates object.

        :param str last_seq: (optional) Last sequence number.
        :param List[DbEvent] results: (optional) results.
        """
        self.last_seq = last_seq
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DbUpdates':
        """Initialize a DbUpdates object from a json dictionary."""
        args = {}
        if 'last_seq' in _dict:
            args['last_seq'] = _dict.get('last_seq')
        if 'results' in _dict:
            args['results'] = [DbEvent.from_dict(x) for x in _dict.get('results')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DbUpdates object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'last_seq') and self.last_seq is not None:
            _dict['last_seq'] = self.last_seq
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x.to_dict() for x in self.results]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DbUpdates object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DbUpdates') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DbUpdates') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DbsInfoResult():
    """
    Schema for database information keyed by database name.

    :attr DatabaseInformation info: (optional) Schema for information about a
          database.
    :attr str key: (optional) Database name.
    """

    def __init__(self,
                 *,
                 info: 'DatabaseInformation' = None,
                 key: str = None) -> None:
        """
        Initialize a DbsInfoResult object.

        :param DatabaseInformation info: (optional) Schema for information about a
               database.
        :param str key: (optional) Database name.
        """
        self.info = info
        self.key = key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DbsInfoResult':
        """Initialize a DbsInfoResult object from a json dictionary."""
        args = {}
        if 'info' in _dict:
            args['info'] = DatabaseInformation.from_dict(_dict.get('info'))
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DbsInfoResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'info') and self.info is not None:
            _dict['info'] = self.info.to_dict()
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DbsInfoResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DbsInfoResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DbsInfoResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DesignDocument():
    """
    Schema for a design document.

    :attr dict attachments: (optional) Schema for a map of attachment name to
          attachment metadata.
    :attr List[str] conflicts: (optional) Schema for a list of document revision
          identifiers.
    :attr bool deleted: (optional) Deletion flag. Available if document was removed.
    :attr List[str] deleted_conflicts: (optional) Schema for a list of document
          revision identifiers.
    :attr str id: (optional) Document ID.
    :attr str local_seq: (optional) Document's update sequence in current database.
          Available if requested with local_seq=true query parameter.
    :attr str rev: (optional) Schema for a document revision identifier.
    :attr Revisions revisions: (optional) Schema for list of revision information.
    :attr List[DocumentRevisionStatus] revs_info: (optional) Schema for a list of
          objects with information about local revisions and their status.
    :attr bool autoupdate: (optional) Indicates whether to automatically build
          indexes defined in this design document.
    :attr dict filters: (optional) Schema for filter functions definition. This
          schema is a map where keys are the names of the filter functions and values are
          the function definition in string format.
    :attr dict indexes: (optional) Search (text) index function definitions.
    :attr str language: (optional) Defines Query Server key to process design
          document functions.
    :attr DesignDocumentOptions options: (optional) Schema for design document
          options.
    :attr dict updates: (optional) Schema for update function definitions.
    :attr dict validate_doc_update: (optional) Schema for validate document update
          functions definition.
    :attr dict views: (optional) Schema for design document views.
    :attr dict st_indexes: (optional) Schema for geospatial index function
          definitions.
    """

    # The set of defined properties for the class
    _properties = frozenset(['attachments', '_attachments', 'conflicts', '_conflicts', 'deleted', '_deleted', 'deleted_conflicts', '_deleted_conflicts', 'id', '_id', 'local_seq', '_local_seq', 'rev', '_rev', 'revisions', '_revisions', 'revs_info', '_revs_info', 'autoupdate', 'filters', 'indexes', 'language', 'options', 'updates', 'validate_doc_update', 'views', 'st_indexes'])

    def __init__(self,
                 *,
                 attachments: dict = None,
                 conflicts: List[str] = None,
                 deleted: bool = None,
                 deleted_conflicts: List[str] = None,
                 id: str = None,
                 local_seq: str = None,
                 rev: str = None,
                 revisions: 'Revisions' = None,
                 revs_info: List['DocumentRevisionStatus'] = None,
                 autoupdate: bool = None,
                 filters: dict = None,
                 indexes: dict = None,
                 language: str = None,
                 options: 'DesignDocumentOptions' = None,
                 updates: dict = None,
                 validate_doc_update: dict = None,
                 views: dict = None,
                 st_indexes: dict = None,
                 **kwargs) -> None:
        """
        Initialize a DesignDocument object.

        :param dict attachments: (optional) Schema for a map of attachment name to
               attachment metadata.
        :param List[str] conflicts: (optional) Schema for a list of document
               revision identifiers.
        :param bool deleted: (optional) Deletion flag. Available if document was
               removed.
        :param List[str] deleted_conflicts: (optional) Schema for a list of
               document revision identifiers.
        :param str id: (optional) Document ID.
        :param str local_seq: (optional) Document's update sequence in current
               database. Available if requested with local_seq=true query parameter.
        :param str rev: (optional) Schema for a document revision identifier.
        :param Revisions revisions: (optional) Schema for list of revision
               information.
        :param List[DocumentRevisionStatus] revs_info: (optional) Schema for a list
               of objects with information about local revisions and their status.
        :param bool autoupdate: (optional) Indicates whether to automatically build
               indexes defined in this design document.
        :param dict filters: (optional) Schema for filter functions definition.
               This schema is a map where keys are the names of the filter functions and
               values are the function definition in string format.
        :param dict indexes: (optional) Search (text) index function definitions.
        :param str language: (optional) Defines Query Server key to process design
               document functions.
        :param DesignDocumentOptions options: (optional) Schema for design document
               options.
        :param dict updates: (optional) Schema for update function definitions.
        :param dict validate_doc_update: (optional) Schema for validate document
               update functions definition.
        :param dict views: (optional) Schema for design document views.
        :param dict st_indexes: (optional) Schema for geospatial index function
               definitions.
        :param **kwargs: (optional) Any additional properties.
        """
        self.attachments = attachments
        self.conflicts = conflicts
        self.deleted = deleted
        self.deleted_conflicts = deleted_conflicts
        self.id = id
        self.local_seq = local_seq
        self.rev = rev
        self.revisions = revisions
        self.revs_info = revs_info
        self.autoupdate = autoupdate
        self.filters = filters
        self.indexes = indexes
        self.language = language
        self.options = options
        self.updates = updates
        self.validate_doc_update = validate_doc_update
        self.views = views
        self.st_indexes = st_indexes
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DesignDocument':
        """Initialize a DesignDocument object from a json dictionary."""
        args = {}
        if '_attachments' in _dict:
            args['attachments'] = {k : Attachment.from_dict(v) for k, v in _dict.get('_attachments').items()}
        if '_conflicts' in _dict:
            args['conflicts'] = _dict.get('_conflicts')
        if '_deleted' in _dict:
            args['deleted'] = _dict.get('_deleted')
        if '_deleted_conflicts' in _dict:
            args['deleted_conflicts'] = _dict.get('_deleted_conflicts')
        if '_id' in _dict:
            args['id'] = _dict.get('_id')
        if '_local_seq' in _dict:
            args['local_seq'] = _dict.get('_local_seq')
        if '_rev' in _dict:
            args['rev'] = _dict.get('_rev')
        if '_revisions' in _dict:
            args['revisions'] = Revisions.from_dict(_dict.get('_revisions'))
        if '_revs_info' in _dict:
            args['revs_info'] = [DocumentRevisionStatus.from_dict(x) for x in _dict.get('_revs_info')]
        if 'autoupdate' in _dict:
            args['autoupdate'] = _dict.get('autoupdate')
        if 'filters' in _dict:
            args['filters'] = _dict.get('filters')
        if 'indexes' in _dict:
            args['indexes'] = {k : SearchIndexDefinition.from_dict(v) for k, v in _dict.get('indexes').items()}
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        if 'options' in _dict:
            args['options'] = DesignDocumentOptions.from_dict(_dict.get('options'))
        if 'updates' in _dict:
            args['updates'] = _dict.get('updates')
        if 'validate_doc_update' in _dict:
            args['validate_doc_update'] = _dict.get('validate_doc_update')
        if 'views' in _dict:
            args['views'] = {k : DesignDocumentViewsMapReduce.from_dict(v) for k, v in _dict.get('views').items()}
        if 'st_indexes' in _dict:
            args['st_indexes'] = {k : GeoIndexDefinition.from_dict(v) for k, v in _dict.get('st_indexes').items()}
        args.update({k:v for (k, v) in _dict.items() if k not in cls._properties})
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DesignDocument object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attachments') and self.attachments is not None:
            _dict['_attachments'] = {k : v.to_dict() for k, v in self.attachments.items()}
        if hasattr(self, 'conflicts') and self.conflicts is not None:
            _dict['_conflicts'] = self.conflicts
        if hasattr(self, 'deleted') and self.deleted is not None:
            _dict['_deleted'] = self.deleted
        if hasattr(self, 'deleted_conflicts') and self.deleted_conflicts is not None:
            _dict['_deleted_conflicts'] = self.deleted_conflicts
        if hasattr(self, 'id') and self.id is not None:
            _dict['_id'] = self.id
        if hasattr(self, 'local_seq') and self.local_seq is not None:
            _dict['_local_seq'] = self.local_seq
        if hasattr(self, 'rev') and self.rev is not None:
            _dict['_rev'] = self.rev
        if hasattr(self, 'revisions') and self.revisions is not None:
            _dict['_revisions'] = self.revisions.to_dict()
        if hasattr(self, 'revs_info') and self.revs_info is not None:
            _dict['_revs_info'] = [x.to_dict() for x in self.revs_info]
        if hasattr(self, 'autoupdate') and self.autoupdate is not None:
            _dict['autoupdate'] = self.autoupdate
        if hasattr(self, 'filters') and self.filters is not None:
            _dict['filters'] = self.filters
        if hasattr(self, 'indexes') and self.indexes is not None:
            _dict['indexes'] = {k : v.to_dict() for k, v in self.indexes.items()}
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'options') and self.options is not None:
            _dict['options'] = self.options.to_dict()
        if hasattr(self, 'updates') and self.updates is not None:
            _dict['updates'] = self.updates
        if hasattr(self, 'validate_doc_update') and self.validate_doc_update is not None:
            _dict['validate_doc_update'] = self.validate_doc_update
        if hasattr(self, 'views') and self.views is not None:
            _dict['views'] = {k : v.to_dict() for k, v in self.views.items()}
        if hasattr(self, 'st_indexes') and self.st_indexes is not None:
            _dict['st_indexes'] = {k : v.to_dict() for k, v in self.st_indexes.items()}
        for _key in [k for k in vars(self).keys() if k not in DesignDocument._properties]:
            if getattr(self, _key, None) is not None:
                _dict[_key] = getattr(self, _key)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DesignDocument object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DesignDocument') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DesignDocument') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DesignDocumentInformation():
    """
    Schema for information about a design document.

    :attr str name: (optional) name.
    :attr DesignDocumentInformationViewIndex view_index: (optional) View index
          information.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 view_index: 'DesignDocumentInformationViewIndex' = None) -> None:
        """
        Initialize a DesignDocumentInformation object.

        :param str name: (optional) name.
        :param DesignDocumentInformationViewIndex view_index: (optional) View index
               information.
        """
        self.name = name
        self.view_index = view_index

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DesignDocumentInformation':
        """Initialize a DesignDocumentInformation object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'view_index' in _dict:
            args['view_index'] = DesignDocumentInformationViewIndex.from_dict(_dict.get('view_index'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DesignDocumentInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'view_index') and self.view_index is not None:
            _dict['view_index'] = self.view_index.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DesignDocumentInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DesignDocumentInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DesignDocumentInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DesignDocumentInformationViewIndex():
    """
    View index information.

    :attr bool compact_running: (optional) Indicates whether a compaction routine is
          currently running on the view.
    :attr str language: (optional) Language for the defined views.
    :attr str signature: (optional) MD5 signature of the views for the design
          document.
    :attr ContentInformationSizes sizes: (optional) Schema for size information of
          content.
    :attr str update_seq: (optional) The update sequence of the corresponding
          database that has been indexed.
    :attr bool updater_running: (optional) Indicates if the view is currently being
          updated.
    :attr int waiting_clients: (optional) Number of clients waiting on views from
          this design document.
    :attr bool waiting_commit: (optional) Indicates if there are outstanding commits
          to the underlying database that need to processed.
    """

    def __init__(self,
                 *,
                 compact_running: bool = None,
                 language: str = None,
                 signature: str = None,
                 sizes: 'ContentInformationSizes' = None,
                 update_seq: str = None,
                 updater_running: bool = None,
                 waiting_clients: int = None,
                 waiting_commit: bool = None) -> None:
        """
        Initialize a DesignDocumentInformationViewIndex object.

        :param bool compact_running: (optional) Indicates whether a compaction
               routine is currently running on the view.
        :param str language: (optional) Language for the defined views.
        :param str signature: (optional) MD5 signature of the views for the design
               document.
        :param ContentInformationSizes sizes: (optional) Schema for size
               information of content.
        :param str update_seq: (optional) The update sequence of the corresponding
               database that has been indexed.
        :param bool updater_running: (optional) Indicates if the view is currently
               being updated.
        :param int waiting_clients: (optional) Number of clients waiting on views
               from this design document.
        :param bool waiting_commit: (optional) Indicates if there are outstanding
               commits to the underlying database that need to processed.
        """
        self.compact_running = compact_running
        self.language = language
        self.signature = signature
        self.sizes = sizes
        self.update_seq = update_seq
        self.updater_running = updater_running
        self.waiting_clients = waiting_clients
        self.waiting_commit = waiting_commit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DesignDocumentInformationViewIndex':
        """Initialize a DesignDocumentInformationViewIndex object from a json dictionary."""
        args = {}
        if 'compact_running' in _dict:
            args['compact_running'] = _dict.get('compact_running')
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        if 'signature' in _dict:
            args['signature'] = _dict.get('signature')
        if 'sizes' in _dict:
            args['sizes'] = ContentInformationSizes.from_dict(_dict.get('sizes'))
        if 'update_seq' in _dict:
            args['update_seq'] = _dict.get('update_seq')
        if 'updater_running' in _dict:
            args['updater_running'] = _dict.get('updater_running')
        if 'waiting_clients' in _dict:
            args['waiting_clients'] = _dict.get('waiting_clients')
        if 'waiting_commit' in _dict:
            args['waiting_commit'] = _dict.get('waiting_commit')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DesignDocumentInformationViewIndex object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'compact_running') and self.compact_running is not None:
            _dict['compact_running'] = self.compact_running
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'signature') and self.signature is not None:
            _dict['signature'] = self.signature
        if hasattr(self, 'sizes') and self.sizes is not None:
            _dict['sizes'] = self.sizes.to_dict()
        if hasattr(self, 'update_seq') and self.update_seq is not None:
            _dict['update_seq'] = self.update_seq
        if hasattr(self, 'updater_running') and self.updater_running is not None:
            _dict['updater_running'] = self.updater_running
        if hasattr(self, 'waiting_clients') and self.waiting_clients is not None:
            _dict['waiting_clients'] = self.waiting_clients
        if hasattr(self, 'waiting_commit') and self.waiting_commit is not None:
            _dict['waiting_commit'] = self.waiting_commit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DesignDocumentInformationViewIndex object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DesignDocumentInformationViewIndex') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DesignDocumentInformationViewIndex') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DesignDocumentOptions():
    """
    Schema for design document options.

    :attr bool partitioned: (optional) Whether this design document describes
          partitioned or global indexes.
    """

    def __init__(self,
                 *,
                 partitioned: bool = None) -> None:
        """
        Initialize a DesignDocumentOptions object.

        :param bool partitioned: (optional) Whether this design document describes
               partitioned or global indexes.
        """
        self.partitioned = partitioned

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DesignDocumentOptions':
        """Initialize a DesignDocumentOptions object from a json dictionary."""
        args = {}
        if 'partitioned' in _dict:
            args['partitioned'] = _dict.get('partitioned')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DesignDocumentOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'partitioned') and self.partitioned is not None:
            _dict['partitioned'] = self.partitioned
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DesignDocumentOptions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DesignDocumentOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DesignDocumentOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DesignDocumentViewsMapReduce():
    """
    Schema for view functions definition.

    :attr str map: (optional) JavaScript map function as a string.
    :attr str reduce: (optional) JavaScript reduce function as a string.
    """

    def __init__(self,
                 *,
                 map: str = None,
                 reduce: str = None) -> None:
        """
        Initialize a DesignDocumentViewsMapReduce object.

        :param str map: (optional) JavaScript map function as a string.
        :param str reduce: (optional) JavaScript reduce function as a string.
        """
        self.map = map
        self.reduce = reduce

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DesignDocumentViewsMapReduce':
        """Initialize a DesignDocumentViewsMapReduce object from a json dictionary."""
        args = {}
        if 'map' in _dict:
            args['map'] = _dict.get('map')
        if 'reduce' in _dict:
            args['reduce'] = _dict.get('reduce')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DesignDocumentViewsMapReduce object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'map') and self.map is not None:
            _dict['map'] = self.map
        if hasattr(self, 'reduce') and self.reduce is not None:
            _dict['reduce'] = self.reduce
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DesignDocumentViewsMapReduce object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DesignDocumentViewsMapReduce') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DesignDocumentViewsMapReduce') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DocsResultRow():
    """
    Schema for a row of document information in a DocsResult.

    :attr str caused_by: (optional) The cause of the error (if available).
    :attr str error: (optional) The name of the error.
    :attr str reason: (optional) The reason the error occurred (if available).
    :attr Document doc: (optional) Schema for a document.
    :attr str id: (optional) id.
    :attr str key: (optional) Document ID.
    :attr DocsResultRowValue value: (optional) Value of built-in `/_all_docs` style
          view.
    """

    def __init__(self,
                 *,
                 caused_by: str = None,
                 error: str = None,
                 reason: str = None,
                 doc: 'Document' = None,
                 id: str = None,
                 key: str = None,
                 value: 'DocsResultRowValue' = None) -> None:
        """
        Initialize a DocsResultRow object.

        :param str caused_by: (optional) The cause of the error (if available).
        :param str error: (optional) The name of the error.
        :param str reason: (optional) The reason the error occurred (if available).
        :param Document doc: (optional) Schema for a document.
        :param str id: (optional) id.
        :param str key: (optional) Document ID.
        :param DocsResultRowValue value: (optional) Value of built-in `/_all_docs`
               style view.
        """
        self.caused_by = caused_by
        self.error = error
        self.reason = reason
        self.doc = doc
        self.id = id
        self.key = key
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocsResultRow':
        """Initialize a DocsResultRow object from a json dictionary."""
        args = {}
        if 'caused_by' in _dict:
            args['caused_by'] = _dict.get('caused_by')
        if 'error' in _dict:
            args['error'] = _dict.get('error')
        if 'reason' in _dict:
            args['reason'] = _dict.get('reason')
        if 'doc' in _dict:
            args['doc'] = Document.from_dict(_dict.get('doc'))
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        if 'value' in _dict:
            args['value'] = DocsResultRowValue.from_dict(_dict.get('value'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocsResultRow object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'caused_by') and self.caused_by is not None:
            _dict['caused_by'] = self.caused_by
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error
        if hasattr(self, 'reason') and self.reason is not None:
            _dict['reason'] = self.reason
        if hasattr(self, 'doc') and self.doc is not None:
            _dict['doc'] = self.doc.to_dict()
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocsResultRow object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DocsResultRow') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocsResultRow') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DocsResultRowValue():
    """
    Value of built-in `/_all_docs` style view.

    :attr str rev: (optional) Schema for a document revision identifier.
    """

    def __init__(self,
                 *,
                 rev: str = None) -> None:
        """
        Initialize a DocsResultRowValue object.

        :param str rev: (optional) Schema for a document revision identifier.
        """
        self.rev = rev

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocsResultRowValue':
        """Initialize a DocsResultRowValue object from a json dictionary."""
        args = {}
        if 'rev' in _dict:
            args['rev'] = _dict.get('rev')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocsResultRowValue object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'rev') and self.rev is not None:
            _dict['rev'] = self.rev
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocsResultRowValue object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DocsResultRowValue') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocsResultRowValue') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Document():
    """
    Schema for a document.

    :attr dict attachments: (optional) Schema for a map of attachment name to
          attachment metadata.
    :attr List[str] conflicts: (optional) Schema for a list of document revision
          identifiers.
    :attr bool deleted: (optional) Deletion flag. Available if document was removed.
    :attr List[str] deleted_conflicts: (optional) Schema for a list of document
          revision identifiers.
    :attr str id: (optional) Document ID.
    :attr str local_seq: (optional) Document's update sequence in current database.
          Available if requested with local_seq=true query parameter.
    :attr str rev: (optional) Schema for a document revision identifier.
    :attr Revisions revisions: (optional) Schema for list of revision information.
    :attr List[DocumentRevisionStatus] revs_info: (optional) Schema for a list of
          objects with information about local revisions and their status.
    """

    # The set of defined properties for the class
    _properties = frozenset(['attachments', '_attachments', 'conflicts', '_conflicts', 'deleted', '_deleted', 'deleted_conflicts', '_deleted_conflicts', 'id', '_id', 'local_seq', '_local_seq', 'rev', '_rev', 'revisions', '_revisions', 'revs_info', '_revs_info'])

    def __init__(self,
                 *,
                 attachments: dict = None,
                 conflicts: List[str] = None,
                 deleted: bool = None,
                 deleted_conflicts: List[str] = None,
                 id: str = None,
                 local_seq: str = None,
                 rev: str = None,
                 revisions: 'Revisions' = None,
                 revs_info: List['DocumentRevisionStatus'] = None,
                 **kwargs) -> None:
        """
        Initialize a Document object.

        :param dict attachments: (optional) Schema for a map of attachment name to
               attachment metadata.
        :param List[str] conflicts: (optional) Schema for a list of document
               revision identifiers.
        :param bool deleted: (optional) Deletion flag. Available if document was
               removed.
        :param List[str] deleted_conflicts: (optional) Schema for a list of
               document revision identifiers.
        :param str id: (optional) Document ID.
        :param str local_seq: (optional) Document's update sequence in current
               database. Available if requested with local_seq=true query parameter.
        :param str rev: (optional) Schema for a document revision identifier.
        :param Revisions revisions: (optional) Schema for list of revision
               information.
        :param List[DocumentRevisionStatus] revs_info: (optional) Schema for a list
               of objects with information about local revisions and their status.
        :param **kwargs: (optional) Any additional properties.
        """
        self.attachments = attachments
        self.conflicts = conflicts
        self.deleted = deleted
        self.deleted_conflicts = deleted_conflicts
        self.id = id
        self.local_seq = local_seq
        self.rev = rev
        self.revisions = revisions
        self.revs_info = revs_info
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Document':
        """Initialize a Document object from a json dictionary."""
        args = {}
        if '_attachments' in _dict:
            args['attachments'] = {k : Attachment.from_dict(v) for k, v in _dict.get('_attachments').items()}
        if '_conflicts' in _dict:
            args['conflicts'] = _dict.get('_conflicts')
        if '_deleted' in _dict:
            args['deleted'] = _dict.get('_deleted')
        if '_deleted_conflicts' in _dict:
            args['deleted_conflicts'] = _dict.get('_deleted_conflicts')
        if '_id' in _dict:
            args['id'] = _dict.get('_id')
        if '_local_seq' in _dict:
            args['local_seq'] = _dict.get('_local_seq')
        if '_rev' in _dict:
            args['rev'] = _dict.get('_rev')
        if '_revisions' in _dict:
            args['revisions'] = Revisions.from_dict(_dict.get('_revisions'))
        if '_revs_info' in _dict:
            args['revs_info'] = [DocumentRevisionStatus.from_dict(x) for x in _dict.get('_revs_info')]
        args.update({k:v for (k, v) in _dict.items() if k not in cls._properties})
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Document object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attachments') and self.attachments is not None:
            _dict['_attachments'] = {k : v.to_dict() for k, v in self.attachments.items()}
        if hasattr(self, 'conflicts') and self.conflicts is not None:
            _dict['_conflicts'] = self.conflicts
        if hasattr(self, 'deleted') and self.deleted is not None:
            _dict['_deleted'] = self.deleted
        if hasattr(self, 'deleted_conflicts') and self.deleted_conflicts is not None:
            _dict['_deleted_conflicts'] = self.deleted_conflicts
        if hasattr(self, 'id') and self.id is not None:
            _dict['_id'] = self.id
        if hasattr(self, 'local_seq') and self.local_seq is not None:
            _dict['_local_seq'] = self.local_seq
        if hasattr(self, 'rev') and self.rev is not None:
            _dict['_rev'] = self.rev
        if hasattr(self, 'revisions') and self.revisions is not None:
            _dict['_revisions'] = self.revisions.to_dict()
        if hasattr(self, 'revs_info') and self.revs_info is not None:
            _dict['_revs_info'] = [x.to_dict() for x in self.revs_info]
        for _key in [k for k in vars(self).keys() if k not in Document._properties]:
            if getattr(self, _key, None) is not None:
                _dict[_key] = getattr(self, _key)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Document object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Document') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Document') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DocumentResult():
    """
    Schema for the result of a document modification.

    :attr str id: (optional) Schema for a document ID.
    :attr str rev: (optional) Schema for a document revision identifier.
    :attr bool ok: (optional) ok.
    :attr str caused_by: (optional) The cause of the error (if available).
    :attr str error: (optional) The name of the error.
    :attr str reason: (optional) The reason the error occurred (if available).
    """

    def __init__(self,
                 *,
                 id: str = None,
                 rev: str = None,
                 ok: bool = None,
                 caused_by: str = None,
                 error: str = None,
                 reason: str = None) -> None:
        """
        Initialize a DocumentResult object.

        :param str id: (optional) Schema for a document ID.
        :param str rev: (optional) Schema for a document revision identifier.
        :param bool ok: (optional) ok.
        :param str caused_by: (optional) The cause of the error (if available).
        :param str error: (optional) The name of the error.
        :param str reason: (optional) The reason the error occurred (if available).
        """
        self.id = id
        self.rev = rev
        self.ok = ok
        self.caused_by = caused_by
        self.error = error
        self.reason = reason

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentResult':
        """Initialize a DocumentResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'rev' in _dict:
            args['rev'] = _dict.get('rev')
        if 'ok' in _dict:
            args['ok'] = _dict.get('ok')
        if 'caused_by' in _dict:
            args['caused_by'] = _dict.get('caused_by')
        if 'error' in _dict:
            args['error'] = _dict.get('error')
        if 'reason' in _dict:
            args['reason'] = _dict.get('reason')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'rev') and self.rev is not None:
            _dict['rev'] = self.rev
        if hasattr(self, 'ok') and self.ok is not None:
            _dict['ok'] = self.ok
        if hasattr(self, 'caused_by') and self.caused_by is not None:
            _dict['caused_by'] = self.caused_by
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error
        if hasattr(self, 'reason') and self.reason is not None:
            _dict['reason'] = self.reason
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DocumentResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DocumentRevisionStatus():
    """
    Schema for information about revisions and their status.

    :attr str rev: (optional) Schema for a document revision identifier.
    :attr str status: (optional) Status of the revision. May be one of: -
          `available`: Revision is available for retrieving with rev query parameter -
          `missing`: Revision is not available - `deleted`: Revision belongs to deleted
          document.
    """

    def __init__(self,
                 *,
                 rev: str = None,
                 status: str = None) -> None:
        """
        Initialize a DocumentRevisionStatus object.

        :param str rev: (optional) Schema for a document revision identifier.
        :param str status: (optional) Status of the revision. May be one of: -
               `available`: Revision is available for retrieving with rev query parameter
               - `missing`: Revision is not available - `deleted`: Revision belongs to
               deleted document.
        """
        self.rev = rev
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentRevisionStatus':
        """Initialize a DocumentRevisionStatus object from a json dictionary."""
        args = {}
        if 'rev' in _dict:
            args['rev'] = _dict.get('rev')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentRevisionStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'rev') and self.rev is not None:
            _dict['rev'] = self.rev
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentRevisionStatus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DocumentRevisionStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentRevisionStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        Status of the revision. May be one of: - `available`: Revision is available for
        retrieving with rev query parameter - `missing`: Revision is not available -
        `deleted`: Revision belongs to deleted document.
        """
        AVAILABLE = 'available'
        MISSING = 'missing'
        DELETED = 'deleted'


class DocumentShardInfo():
    """
    Schema for document shard information.

    :attr List[str] nodes: (optional) List of nodes serving a replica of the shard.
    :attr str range: (optional) The shard range in which the document is stored.
    """

    def __init__(self,
                 *,
                 nodes: List[str] = None,
                 range: str = None) -> None:
        """
        Initialize a DocumentShardInfo object.

        :param List[str] nodes: (optional) List of nodes serving a replica of the
               shard.
        :param str range: (optional) The shard range in which the document is
               stored.
        """
        self.nodes = nodes
        self.range = range

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentShardInfo':
        """Initialize a DocumentShardInfo object from a json dictionary."""
        args = {}
        if 'nodes' in _dict:
            args['nodes'] = _dict.get('nodes')
        if 'range' in _dict:
            args['range'] = _dict.get('range')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentShardInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'nodes') and self.nodes is not None:
            _dict['nodes'] = self.nodes
        if hasattr(self, 'range') and self.range is not None:
            _dict['range'] = self.range
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentShardInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DocumentShardInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentShardInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class EnsureFullCommitInformation():
    """
    Schema for the status of a commit operation.

    :attr str instance_start_time: (optional) Timestamp of when the database was
          opened, expressed in microseconds since the epoch.
    :attr bool ok: (optional) Operation status.
    """

    def __init__(self,
                 *,
                 instance_start_time: str = None,
                 ok: bool = None) -> None:
        """
        Initialize a EnsureFullCommitInformation object.

        :param str instance_start_time: (optional) Timestamp of when the database
               was opened, expressed in microseconds since the epoch.
        :param bool ok: (optional) Operation status.
        """
        self.instance_start_time = instance_start_time
        self.ok = ok

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnsureFullCommitInformation':
        """Initialize a EnsureFullCommitInformation object from a json dictionary."""
        args = {}
        if 'instance_start_time' in _dict:
            args['instance_start_time'] = _dict.get('instance_start_time')
        if 'ok' in _dict:
            args['ok'] = _dict.get('ok')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnsureFullCommitInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'instance_start_time') and self.instance_start_time is not None:
            _dict['instance_start_time'] = self.instance_start_time
        if hasattr(self, 'ok') and self.ok is not None:
            _dict['ok'] = self.ok
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnsureFullCommitInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnsureFullCommitInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnsureFullCommitInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ExecutionStats():
    """
    Schema for find query execution statistics.

    :attr float execution_time_ms: (optional) Time to execute the query.
    :attr int results_returned: (optional) Number of results returned.
    :attr int total_docs_examined: (optional) Number of documents fetched from the
          index.
    :attr int total_keys_examined: (optional) Number of rows scanned in the index.
    :attr int total_quorum_docs_examined: (optional) Number of documents fetched
          from the primary index with the specified read quorum.
    """

    def __init__(self,
                 *,
                 execution_time_ms: float = None,
                 results_returned: int = None,
                 total_docs_examined: int = None,
                 total_keys_examined: int = None,
                 total_quorum_docs_examined: int = None) -> None:
        """
        Initialize a ExecutionStats object.

        :param float execution_time_ms: (optional) Time to execute the query.
        :param int results_returned: (optional) Number of results returned.
        :param int total_docs_examined: (optional) Number of documents fetched from
               the index.
        :param int total_keys_examined: (optional) Number of rows scanned in the
               index.
        :param int total_quorum_docs_examined: (optional) Number of documents
               fetched from the primary index with the specified read quorum.
        """
        self.execution_time_ms = execution_time_ms
        self.results_returned = results_returned
        self.total_docs_examined = total_docs_examined
        self.total_keys_examined = total_keys_examined
        self.total_quorum_docs_examined = total_quorum_docs_examined

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ExecutionStats':
        """Initialize a ExecutionStats object from a json dictionary."""
        args = {}
        if 'execution_time_ms' in _dict:
            args['execution_time_ms'] = _dict.get('execution_time_ms')
        if 'results_returned' in _dict:
            args['results_returned'] = _dict.get('results_returned')
        if 'total_docs_examined' in _dict:
            args['total_docs_examined'] = _dict.get('total_docs_examined')
        if 'total_keys_examined' in _dict:
            args['total_keys_examined'] = _dict.get('total_keys_examined')
        if 'total_quorum_docs_examined' in _dict:
            args['total_quorum_docs_examined'] = _dict.get('total_quorum_docs_examined')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExecutionStats object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'execution_time_ms') and self.execution_time_ms is not None:
            _dict['execution_time_ms'] = self.execution_time_ms
        if hasattr(self, 'results_returned') and self.results_returned is not None:
            _dict['results_returned'] = self.results_returned
        if hasattr(self, 'total_docs_examined') and self.total_docs_examined is not None:
            _dict['total_docs_examined'] = self.total_docs_examined
        if hasattr(self, 'total_keys_examined') and self.total_keys_examined is not None:
            _dict['total_keys_examined'] = self.total_keys_examined
        if hasattr(self, 'total_quorum_docs_examined') and self.total_quorum_docs_examined is not None:
            _dict['total_quorum_docs_examined'] = self.total_quorum_docs_examined
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ExecutionStats object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ExecutionStats') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ExecutionStats') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ExplainResult():
    """
    Schema for information about the index used for a find query.

    :attr str dbname: (optional) dbname.
    :attr List[str] fields: (optional) fields.
    :attr IndexInformation index: (optional) Schema for information about an index.
    :attr int limit: (optional) limit.
    :attr dict opts: (optional) opts.
    :attr ExplainResultRange range: (optional) range.
    :attr dict selector: (optional) JSON object describing criteria used to select
          documents. The selector specifies fields in the document, and provides an
          expression to evaluate with the field content or other data.
          The selector object must:
            * Be structured as valid JSON.
            * Contain a valid query expression.
          Using a selector is significantly more efficient than using a JavaScript filter
          function, and is the recommended option if filtering on document attributes
          only.
          Elementary selector syntax requires you to specify one or more fields, and the
          corresponding values required for those fields. You can create more complex
          selector expressions by combining operators.
          Operators are identified by the use of a dollar sign `$` prefix in the name
          field.
          There are two core types of operators in the selector syntax:
          * Combination operators: applied at the topmost level of selection. They are
          used to combine selectors. In addition to the common boolean operators (`$and`,
          `$or`, `$not`, `$nor`) there are three combination operators: `$all`,
          `$elemMatch`, and `$allMatch`. A combination operator takes a single argument.
          The argument is either another selector, or an array of selectors.
          * Condition operators: are specific to a field, and are used to evaluate the
          value stored in that field. For instance, the basic `$eq` operator matches when
          the specified field contains a value that is equal to the supplied argument.
    :attr int skip: (optional) skip.
    """

    def __init__(self,
                 *,
                 dbname: str = None,
                 fields: List[str] = None,
                 index: 'IndexInformation' = None,
                 limit: int = None,
                 opts: dict = None,
                 range: 'ExplainResultRange' = None,
                 selector: dict = None,
                 skip: int = None) -> None:
        """
        Initialize a ExplainResult object.

        :param str dbname: (optional) dbname.
        :param List[str] fields: (optional) fields.
        :param IndexInformation index: (optional) Schema for information about an
               index.
        :param int limit: (optional) limit.
        :param dict opts: (optional) opts.
        :param ExplainResultRange range: (optional) range.
        :param dict selector: (optional) JSON object describing criteria used to
               select documents. The selector specifies fields in the document, and
               provides an expression to evaluate with the field content or other data.
               The selector object must:
                 * Be structured as valid JSON.
                 * Contain a valid query expression.
               Using a selector is significantly more efficient than using a JavaScript
               filter function, and is the recommended option if filtering on document
               attributes only.
               Elementary selector syntax requires you to specify one or more fields, and
               the corresponding values required for those fields. You can create more
               complex selector expressions by combining operators.
               Operators are identified by the use of a dollar sign `$` prefix in the name
               field.
               There are two core types of operators in the selector syntax:
               * Combination operators: applied at the topmost level of selection. They
               are used to combine selectors. In addition to the common boolean operators
               (`$and`, `$or`, `$not`, `$nor`) there are three combination operators:
               `$all`, `$elemMatch`, and `$allMatch`. A combination operator takes a
               single argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
        :param int skip: (optional) skip.
        """
        self.dbname = dbname
        self.fields = fields
        self.index = index
        self.limit = limit
        self.opts = opts
        self.range = range
        self.selector = selector
        self.skip = skip

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ExplainResult':
        """Initialize a ExplainResult object from a json dictionary."""
        args = {}
        if 'dbname' in _dict:
            args['dbname'] = _dict.get('dbname')
        if 'fields' in _dict:
            args['fields'] = _dict.get('fields')
        if 'index' in _dict:
            args['index'] = IndexInformation.from_dict(_dict.get('index'))
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'opts' in _dict:
            args['opts'] = _dict.get('opts')
        if 'range' in _dict:
            args['range'] = ExplainResultRange.from_dict(_dict.get('range'))
        if 'selector' in _dict:
            args['selector'] = _dict.get('selector')
        if 'skip' in _dict:
            args['skip'] = _dict.get('skip')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExplainResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'dbname') and self.dbname is not None:
            _dict['dbname'] = self.dbname
        if hasattr(self, 'fields') and self.fields is not None:
            _dict['fields'] = self.fields
        if hasattr(self, 'index') and self.index is not None:
            _dict['index'] = self.index.to_dict()
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'opts') and self.opts is not None:
            _dict['opts'] = self.opts
        if hasattr(self, 'range') and self.range is not None:
            _dict['range'] = self.range.to_dict()
        if hasattr(self, 'selector') and self.selector is not None:
            _dict['selector'] = self.selector
        if hasattr(self, 'skip') and self.skip is not None:
            _dict['skip'] = self.skip
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ExplainResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ExplainResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ExplainResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ExplainResultRange():
    """
    range.

    :attr List[object] end_key: (optional) end_key.
    :attr List[object] start_key: (optional) start_key.
    """

    def __init__(self,
                 *,
                 end_key: List[object] = None,
                 start_key: List[object] = None) -> None:
        """
        Initialize a ExplainResultRange object.

        :param List[object] end_key: (optional) end_key.
        :param List[object] start_key: (optional) start_key.
        """
        self.end_key = end_key
        self.start_key = start_key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ExplainResultRange':
        """Initialize a ExplainResultRange object from a json dictionary."""
        args = {}
        if 'end_key' in _dict:
            args['end_key'] = _dict.get('end_key')
        if 'start_key' in _dict:
            args['start_key'] = _dict.get('start_key')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExplainResultRange object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'end_key') and self.end_key is not None:
            _dict['end_key'] = self.end_key
        if hasattr(self, 'start_key') and self.start_key is not None:
            _dict['start_key'] = self.start_key
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ExplainResultRange object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ExplainResultRange') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ExplainResultRange') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FindResult():
    """
    Schema for the result of a query find operation.

    :attr str bookmark: (optional) Opaque bookmark token used when paginating
          results.
    :attr List[Document] docs: (optional) Documents matching the selector.
    :attr ExecutionStats execution_stats: (optional) Schema for find query execution
          statistics.
    :attr str warning: (optional) warning.
    """

    def __init__(self,
                 *,
                 bookmark: str = None,
                 docs: List['Document'] = None,
                 execution_stats: 'ExecutionStats' = None,
                 warning: str = None) -> None:
        """
        Initialize a FindResult object.

        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param List[Document] docs: (optional) Documents matching the selector.
        :param ExecutionStats execution_stats: (optional) Schema for find query
               execution statistics.
        :param str warning: (optional) warning.
        """
        self.bookmark = bookmark
        self.docs = docs
        self.execution_stats = execution_stats
        self.warning = warning

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FindResult':
        """Initialize a FindResult object from a json dictionary."""
        args = {}
        if 'bookmark' in _dict:
            args['bookmark'] = _dict.get('bookmark')
        if 'docs' in _dict:
            args['docs'] = [Document.from_dict(x) for x in _dict.get('docs')]
        if 'execution_stats' in _dict:
            args['execution_stats'] = ExecutionStats.from_dict(_dict.get('execution_stats'))
        if 'warning' in _dict:
            args['warning'] = _dict.get('warning')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FindResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'bookmark') and self.bookmark is not None:
            _dict['bookmark'] = self.bookmark
        if hasattr(self, 'docs') and self.docs is not None:
            _dict['docs'] = [x.to_dict() for x in self.docs]
        if hasattr(self, 'execution_stats') and self.execution_stats is not None:
            _dict['execution_stats'] = self.execution_stats.to_dict()
        if hasattr(self, 'warning') and self.warning is not None:
            _dict['warning'] = self.warning
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FindResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FindResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FindResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GeoIndexDefinition():
    """
    Schema for a geospatial index definition.

    :attr str index: String form of a JavaScript function that is called for each
          document in the database. The function takes the document as a parameter,
          extracts some geospatial data from it, and then calls the `st_index` function to
          index that data. The `st_index` takes a GeoJSON geometry as a parameter.
    """

    def __init__(self,
                 index: str) -> None:
        """
        Initialize a GeoIndexDefinition object.

        :param str index: String form of a JavaScript function that is called for
               each document in the database. The function takes the document as a
               parameter, extracts some geospatial data from it, and then calls the
               `st_index` function to index that data. The `st_index` takes a GeoJSON
               geometry as a parameter.
        """
        self.index = index

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GeoIndexDefinition':
        """Initialize a GeoIndexDefinition object from a json dictionary."""
        args = {}
        if 'index' in _dict:
            args['index'] = _dict.get('index')
        else:
            raise ValueError('Required property \'index\' not present in GeoIndexDefinition JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GeoIndexDefinition object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'index') and self.index is not None:
            _dict['index'] = self.index
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GeoIndexDefinition object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GeoIndexDefinition') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GeoIndexDefinition') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GeoIndexInformation():
    """
    Schema for information about a geospatial index.

    :attr GeoIndexStats geo_index: (optional) Schema for geospatial index
          statistics.
    """

    def __init__(self,
                 *,
                 geo_index: 'GeoIndexStats' = None) -> None:
        """
        Initialize a GeoIndexInformation object.

        :param GeoIndexStats geo_index: (optional) Schema for geospatial index
               statistics.
        """
        self.geo_index = geo_index

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GeoIndexInformation':
        """Initialize a GeoIndexInformation object from a json dictionary."""
        args = {}
        if 'geo_index' in _dict:
            args['geo_index'] = GeoIndexStats.from_dict(_dict.get('geo_index'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GeoIndexInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'geo_index') and self.geo_index is not None:
            _dict['geo_index'] = self.geo_index.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GeoIndexInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GeoIndexInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GeoIndexInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GeoIndexStats():
    """
    Schema for geospatial index statistics.

    :attr int data_size: (optional) The size of the geospatial index, in bytes.
    :attr int disk_size: (optional) The size of the geospatial index, as stored on
          disk, in bytes.
    :attr int doc_count: (optional) Number of documents in the geospatial index.
    """

    def __init__(self,
                 *,
                 data_size: int = None,
                 disk_size: int = None,
                 doc_count: int = None) -> None:
        """
        Initialize a GeoIndexStats object.

        :param int data_size: (optional) The size of the geospatial index, in
               bytes.
        :param int disk_size: (optional) The size of the geospatial index, as
               stored on disk, in bytes.
        :param int doc_count: (optional) Number of documents in the geospatial
               index.
        """
        self.data_size = data_size
        self.disk_size = disk_size
        self.doc_count = doc_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GeoIndexStats':
        """Initialize a GeoIndexStats object from a json dictionary."""
        args = {}
        if 'data_size' in _dict:
            args['data_size'] = _dict.get('data_size')
        if 'disk_size' in _dict:
            args['disk_size'] = _dict.get('disk_size')
        if 'doc_count' in _dict:
            args['doc_count'] = _dict.get('doc_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GeoIndexStats object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'data_size') and self.data_size is not None:
            _dict['data_size'] = self.data_size
        if hasattr(self, 'disk_size') and self.disk_size is not None:
            _dict['disk_size'] = self.disk_size
        if hasattr(self, 'doc_count') and self.doc_count is not None:
            _dict['doc_count'] = self.doc_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GeoIndexStats object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GeoIndexStats') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GeoIndexStats') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GeoJsonFeature():
    """
    Schema for a GeoJSON feature object. Note that the content of the feature objects
    varies depending on the response format chosen and whether the `include_docs`
    parameter is `true`.

    :attr str id: (optional) Schema for a document ID.
    :attr str rev: (optional) Schema for a document revision identifier.
    :attr List[float] bbox: (optional) Schema for a GeoJSON bounding box.
    :attr GeoJsonGeometryObject geometry: Schema for a GeoJSON geometry object.
    :attr dict properties: (optional) Schema for the properties of a GeoJSON feature
          object.
    :attr str type: Declaration of the GeoJSON type: Feature Object.
    """

    # The set of defined properties for the class
    _properties = frozenset(['id', '_id', 'rev', '_rev', 'bbox', 'geometry', 'properties', 'type'])

    def __init__(self,
                 geometry: 'GeoJsonGeometryObject',
                 type: str,
                 *,
                 id: str = None,
                 rev: str = None,
                 bbox: List[float] = None,
                 properties: dict = None,
                 **kwargs) -> None:
        """
        Initialize a GeoJsonFeature object.

        :param GeoJsonGeometryObject geometry: Schema for a GeoJSON geometry
               object.
        :param str type: Declaration of the GeoJSON type: Feature Object.
        :param str id: (optional) Schema for a document ID.
        :param str rev: (optional) Schema for a document revision identifier.
        :param List[float] bbox: (optional) Schema for a GeoJSON bounding box.
        :param dict properties: (optional) Schema for the properties of a GeoJSON
               feature object.
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.rev = rev
        self.bbox = bbox
        self.geometry = geometry
        self.properties = properties
        self.type = type
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GeoJsonFeature':
        """Initialize a GeoJsonFeature object from a json dictionary."""
        args = {}
        if '_id' in _dict:
            args['id'] = _dict.get('_id')
        if '_rev' in _dict:
            args['rev'] = _dict.get('_rev')
        if 'bbox' in _dict:
            args['bbox'] = _dict.get('bbox')
        if 'geometry' in _dict:
            args['geometry'] = _dict.get('geometry')
        else:
            raise ValueError('Required property \'geometry\' not present in GeoJsonFeature JSON')
        if 'properties' in _dict:
            args['properties'] = _dict.get('properties')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in GeoJsonFeature JSON')
        args.update({k:v for (k, v) in _dict.items() if k not in cls._properties})
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GeoJsonFeature object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['_id'] = self.id
        if hasattr(self, 'rev') and self.rev is not None:
            _dict['_rev'] = self.rev
        if hasattr(self, 'bbox') and self.bbox is not None:
            _dict['bbox'] = self.bbox
        if hasattr(self, 'geometry') and self.geometry is not None:
            if isinstance(self.geometry, dict):
                _dict['geometry'] = self.geometry
            else:
                _dict['geometry'] = self.geometry.to_dict()
        if hasattr(self, 'properties') and self.properties is not None:
            _dict['properties'] = self.properties
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        for _key in [k for k in vars(self).keys() if k not in GeoJsonFeature._properties]:
            if getattr(self, _key, None) is not None:
                _dict[_key] = getattr(self, _key)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GeoJsonFeature object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GeoJsonFeature') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GeoJsonFeature') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Declaration of the GeoJSON type: Feature Object.
        """
        FEATURE = 'Feature'


class GeoJsonGeometryObject():
    """
    Schema for a GeoJSON geometry object.

    """

    def __init__(self) -> None:
        """
        Initialize a GeoJsonGeometryObject object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['GeoJsonGeometry', 'GeoJsonGeometryCollection']))
        raise Exception(msg)

class GeoResult():
    """
    Schema for the result of a geospatial query operation. For the `legacy`, `geojson`, or
    `application/vnd.geo+json` format this is a GeoJson FeatureCollection with additional
    metadata in foreign members.

    :attr str bookmark: (optional) Opaque bookmark token used when paginating
          results.
    :attr List[GeoJsonFeature] features: (optional) The array of GeoJSON Feature
          Objects matching the geospatial query.
    :attr List[GeoResultRow] rows: (optional) The array of rows matching the
          geospatial query. Present only when using `view` format.
    :attr str type: (optional) Declaration of the GeoJSON type: FeatureCollection
          Object.
    """

    def __init__(self,
                 *,
                 bookmark: str = None,
                 features: List['GeoJsonFeature'] = None,
                 rows: List['GeoResultRow'] = None,
                 type: str = None) -> None:
        """
        Initialize a GeoResult object.

        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param List[GeoJsonFeature] features: (optional) The array of GeoJSON
               Feature Objects matching the geospatial query.
        :param List[GeoResultRow] rows: (optional) The array of rows matching the
               geospatial query. Present only when using `view` format.
        :param str type: (optional) Declaration of the GeoJSON type:
               FeatureCollection Object.
        """
        self.bookmark = bookmark
        self.features = features
        self.rows = rows
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GeoResult':
        """Initialize a GeoResult object from a json dictionary."""
        args = {}
        if 'bookmark' in _dict:
            args['bookmark'] = _dict.get('bookmark')
        if 'features' in _dict:
            args['features'] = [GeoJsonFeature.from_dict(x) for x in _dict.get('features')]
        if 'rows' in _dict:
            args['rows'] = [GeoResultRow.from_dict(x) for x in _dict.get('rows')]
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GeoResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'bookmark') and self.bookmark is not None:
            _dict['bookmark'] = self.bookmark
        if hasattr(self, 'features') and self.features is not None:
            _dict['features'] = [x.to_dict() for x in self.features]
        if hasattr(self, 'rows') and self.rows is not None:
            _dict['rows'] = [x.to_dict() for x in self.rows]
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GeoResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GeoResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GeoResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Declaration of the GeoJSON type: FeatureCollection Object.
        """
        FEATURECOLLECTION = 'FeatureCollection'


class GeoResultRow():
    """
    Schema for a row of a geospatial result using view format.

    :attr Document doc: (optional) Schema for a document.
    :attr GeoJsonGeometry geometry: (optional) Schema for a GeoJSON geometry.
    :attr str id: (optional) Schema for a document ID.
    :attr str rev: (optional) Schema for a document revision identifier.
    """

    def __init__(self,
                 *,
                 doc: 'Document' = None,
                 geometry: 'GeoJsonGeometry' = None,
                 id: str = None,
                 rev: str = None) -> None:
        """
        Initialize a GeoResultRow object.

        :param Document doc: (optional) Schema for a document.
        :param GeoJsonGeometry geometry: (optional) Schema for a GeoJSON geometry.
        :param str id: (optional) Schema for a document ID.
        :param str rev: (optional) Schema for a document revision identifier.
        """
        self.doc = doc
        self.geometry = geometry
        self.id = id
        self.rev = rev

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GeoResultRow':
        """Initialize a GeoResultRow object from a json dictionary."""
        args = {}
        if 'doc' in _dict:
            args['doc'] = Document.from_dict(_dict.get('doc'))
        if 'geometry' in _dict:
            args['geometry'] = GeoJsonGeometry.from_dict(_dict.get('geometry'))
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'rev' in _dict:
            args['rev'] = _dict.get('rev')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GeoResultRow object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'doc') and self.doc is not None:
            _dict['doc'] = self.doc.to_dict()
        if hasattr(self, 'geometry') and self.geometry is not None:
            _dict['geometry'] = self.geometry.to_dict()
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'rev') and self.rev is not None:
            _dict['rev'] = self.rev
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GeoResultRow object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GeoResultRow') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GeoResultRow') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class IamSessionInformation():
    """
    Schema for information about an IAM session.

    :attr str id: (optional) User ID.
    :attr bool ok: (optional) Session is ok.
    :attr str scope: (optional) Scope of the session.
    :attr str type: (optional) Type of the session.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 ok: bool = None,
                 scope: str = None,
                 type: str = None) -> None:
        """
        Initialize a IamSessionInformation object.

        :param str id: (optional) User ID.
        :param bool ok: (optional) Session is ok.
        :param str scope: (optional) Scope of the session.
        :param str type: (optional) Type of the session.
        """
        self.id = id
        self.ok = ok
        self.scope = scope
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IamSessionInformation':
        """Initialize a IamSessionInformation object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'ok' in _dict:
            args['ok'] = _dict.get('ok')
        if 'scope' in _dict:
            args['scope'] = _dict.get('scope')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IamSessionInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'ok') and self.ok is not None:
            _dict['ok'] = self.ok
        if hasattr(self, 'scope') and self.scope is not None:
            _dict['scope'] = self.scope
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IamSessionInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IamSessionInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IamSessionInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class IndexDefinition():
    """
    Schema for a `json` or `text` query index definition. Indexes of type `text` have
    additional configuration properties that do not apply to `json` indexes, these are:
    * `default_analyzer` - the default text analyzer to use * `default_field` - whether to
    index the text in all document fields and what analyzer to use for that purpose.

    :attr Analyzer default_analyzer: (optional) Schema for a full text search
          analyzer.
    :attr IndexTextOperatorDefaultField default_field: (optional) Schema for the
          text index default field configuration. The default field is used to index the
          text of all fields within a document for use with the `$text` operator.
    :attr List[IndexField] fields: (optional) List of fields to index.
    :attr bool index_array_lengths: (optional) Whether to scan every document for
          arrays and store the length for each array found. Set the index_array_lengths
          field to false if:
          * You do not need to know the length of an array. * You do not use the `$size`
          operator. * The documents in your database are complex, or not completely under
          your control. As a result, it is difficult to estimate the impact of the extra
          processing that is needed to determine and store the arrays lengths.
    """

    def __init__(self,
                 *,
                 default_analyzer: 'Analyzer' = None,
                 default_field: 'IndexTextOperatorDefaultField' = None,
                 fields: List['IndexField'] = None,
                 index_array_lengths: bool = None) -> None:
        """
        Initialize a IndexDefinition object.

        :param Analyzer default_analyzer: (optional) Schema for a full text search
               analyzer.
        :param IndexTextOperatorDefaultField default_field: (optional) Schema for
               the text index default field configuration. The default field is used to
               index the text of all fields within a document for use with the `$text`
               operator.
        :param List[IndexField] fields: (optional) List of fields to index.
        :param bool index_array_lengths: (optional) Whether to scan every document
               for arrays and store the length for each array found. Set the
               index_array_lengths field to false if:
               * You do not need to know the length of an array. * You do not use the
               `$size` operator. * The documents in your database are complex, or not
               completely under your control. As a result, it is difficult to estimate the
               impact of the extra processing that is needed to determine and store the
               arrays lengths.
        """
        self.default_analyzer = default_analyzer
        self.default_field = default_field
        self.fields = fields
        self.index_array_lengths = index_array_lengths

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IndexDefinition':
        """Initialize a IndexDefinition object from a json dictionary."""
        args = {}
        if 'default_analyzer' in _dict:
            args['default_analyzer'] = Analyzer.from_dict(_dict.get('default_analyzer'))
        if 'default_field' in _dict:
            args['default_field'] = IndexTextOperatorDefaultField.from_dict(_dict.get('default_field'))
        if 'fields' in _dict:
            args['fields'] = [IndexField.from_dict(x) for x in _dict.get('fields')]
        if 'index_array_lengths' in _dict:
            args['index_array_lengths'] = _dict.get('index_array_lengths')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IndexDefinition object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'default_analyzer') and self.default_analyzer is not None:
            _dict['default_analyzer'] = self.default_analyzer.to_dict()
        if hasattr(self, 'default_field') and self.default_field is not None:
            _dict['default_field'] = self.default_field.to_dict()
        if hasattr(self, 'fields') and self.fields is not None:
            _dict['fields'] = [x.to_dict() for x in self.fields]
        if hasattr(self, 'index_array_lengths') and self.index_array_lengths is not None:
            _dict['index_array_lengths'] = self.index_array_lengths
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IndexDefinition object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IndexDefinition') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IndexDefinition') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class IndexField():
    """
    Schema for indexed fields for use with declarative JSON query.

    :attr str name: (optional) Name of the field.
    :attr str type: (optional) The type of the named field.
    """

    # The set of defined properties for the class
    _properties = frozenset(['name', 'type'])

    def __init__(self,
                 *,
                 name: str = None,
                 type: str = None,
                 **kwargs) -> None:
        """
        Initialize a IndexField object.

        :param str name: (optional) Name of the field.
        :param str type: (optional) The type of the named field.
        :param **kwargs: (optional) Any additional properties.
        """
        self.name = name
        self.type = type
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IndexField':
        """Initialize a IndexField object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        args.update({k:v for (k, v) in _dict.items() if k not in cls._properties})
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IndexField object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        for _key in [k for k in vars(self).keys() if k not in IndexField._properties]:
            if getattr(self, _key, None) is not None:
                _dict[_key] = getattr(self, _key)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IndexField object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IndexField') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IndexField') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of the named field.
        """
        BOOLEAN = 'boolean'
        NUMBER = 'number'
        STRING = 'string'


class IndexInformation():
    """
    Schema for information about an index.

    :attr str ddoc: (optional) Design document ID.
    :attr IndexDefinition def_: (optional) Schema for a `json` or `text` query index
          definition. Indexes of type `text` have additional configuration properties that
          do not apply to `json` indexes, these are:
          * `default_analyzer` - the default text analyzer to use * `default_field` -
          whether to index the text in all document fields and what analyzer to use for
          that purpose.
    :attr str name: (optional) Index name.
    :attr str type: (optional) Schema for the type of an index.
    """

    def __init__(self,
                 *,
                 ddoc: str = None,
                 def_: 'IndexDefinition' = None,
                 name: str = None,
                 type: str = None) -> None:
        """
        Initialize a IndexInformation object.

        :param str ddoc: (optional) Design document ID.
        :param IndexDefinition def_: (optional) Schema for a `json` or `text` query
               index definition. Indexes of type `text` have additional configuration
               properties that do not apply to `json` indexes, these are:
               * `default_analyzer` - the default text analyzer to use * `default_field` -
               whether to index the text in all document fields and what analyzer to use
               for that purpose.
        :param str name: (optional) Index name.
        :param str type: (optional) Schema for the type of an index.
        """
        self.ddoc = ddoc
        self.def_ = def_
        self.name = name
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IndexInformation':
        """Initialize a IndexInformation object from a json dictionary."""
        args = {}
        if 'ddoc' in _dict:
            args['ddoc'] = _dict.get('ddoc')
        if 'def' in _dict:
            args['def_'] = IndexDefinition.from_dict(_dict.get('def'))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IndexInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ddoc') and self.ddoc is not None:
            _dict['ddoc'] = self.ddoc
        if hasattr(self, 'def_') and self.def_ is not None:
            _dict['def'] = self.def_.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IndexInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IndexInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IndexInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Schema for the type of an index.
        """
        JSON = 'json'
        SPECIAL = 'special'
        TEXT = 'text'


class IndexResult():
    """
    Schema for the result of creating an index.

    :attr str id: (optional) Id of the design document the index was created in.
    :attr str name: (optional) Name of the index created.
    :attr str result: (optional) Flag to show whether the index was created or one
          already exists.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 result: str = None) -> None:
        """
        Initialize a IndexResult object.

        :param str id: (optional) Id of the design document the index was created
               in.
        :param str name: (optional) Name of the index created.
        :param str result: (optional) Flag to show whether the index was created or
               one already exists.
        """
        self.id = id
        self.name = name
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IndexResult':
        """Initialize a IndexResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'result' in _dict:
            args['result'] = _dict.get('result')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IndexResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IndexResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IndexResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IndexResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResultEnum(str, Enum):
        """
        Flag to show whether the index was created or one already exists.
        """
        CREATED = 'created'
        EXISTS = 'exists'


class IndexTextOperatorDefaultField():
    """
    Schema for the text index default field configuration. The default field is used to
    index the text of all fields within a document for use with the `$text` operator.

    :attr Analyzer analyzer: (optional) Schema for a full text search analyzer.
    :attr bool enabled: (optional) Whether or not the default_field is enabled.
    """

    def __init__(self,
                 *,
                 analyzer: 'Analyzer' = None,
                 enabled: bool = None) -> None:
        """
        Initialize a IndexTextOperatorDefaultField object.

        :param Analyzer analyzer: (optional) Schema for a full text search
               analyzer.
        :param bool enabled: (optional) Whether or not the default_field is
               enabled.
        """
        self.analyzer = analyzer
        self.enabled = enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IndexTextOperatorDefaultField':
        """Initialize a IndexTextOperatorDefaultField object from a json dictionary."""
        args = {}
        if 'analyzer' in _dict:
            args['analyzer'] = Analyzer.from_dict(_dict.get('analyzer'))
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IndexTextOperatorDefaultField object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'analyzer') and self.analyzer is not None:
            _dict['analyzer'] = self.analyzer.to_dict()
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IndexTextOperatorDefaultField object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IndexTextOperatorDefaultField') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IndexTextOperatorDefaultField') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class IndexesInformation():
    """
    Schema for information about the indexes in a database.

    :attr int total_rows: (optional) Number of total rows.
    :attr List[IndexInformation] indexes: (optional) Indexes.
    """

    def __init__(self,
                 *,
                 total_rows: int = None,
                 indexes: List['IndexInformation'] = None) -> None:
        """
        Initialize a IndexesInformation object.

        :param int total_rows: (optional) Number of total rows.
        :param List[IndexInformation] indexes: (optional) Indexes.
        """
        self.total_rows = total_rows
        self.indexes = indexes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IndexesInformation':
        """Initialize a IndexesInformation object from a json dictionary."""
        args = {}
        if 'total_rows' in _dict:
            args['total_rows'] = _dict.get('total_rows')
        if 'indexes' in _dict:
            args['indexes'] = [IndexInformation.from_dict(x) for x in _dict.get('indexes')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IndexesInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_rows') and self.total_rows is not None:
            _dict['total_rows'] = self.total_rows
        if hasattr(self, 'indexes') and self.indexes is not None:
            _dict['indexes'] = [x.to_dict() for x in self.indexes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IndexesInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IndexesInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IndexesInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MembershipInformation():
    """
    Schema for information about known nodes and cluster membership.

    :attr List[str] all_nodes: (optional) List of nodes this node knows about,
          including the ones that are part of the cluster.
    :attr List[str] cluster_nodes: (optional) All cluster nodes.
    """

    def __init__(self,
                 *,
                 all_nodes: List[str] = None,
                 cluster_nodes: List[str] = None) -> None:
        """
        Initialize a MembershipInformation object.

        :param List[str] all_nodes: (optional) List of nodes this node knows about,
               including the ones that are part of the cluster.
        :param List[str] cluster_nodes: (optional) All cluster nodes.
        """
        self.all_nodes = all_nodes
        self.cluster_nodes = cluster_nodes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MembershipInformation':
        """Initialize a MembershipInformation object from a json dictionary."""
        args = {}
        if 'all_nodes' in _dict:
            args['all_nodes'] = _dict.get('all_nodes')
        if 'cluster_nodes' in _dict:
            args['cluster_nodes'] = _dict.get('cluster_nodes')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MembershipInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'all_nodes') and self.all_nodes is not None:
            _dict['all_nodes'] = self.all_nodes
        if hasattr(self, 'cluster_nodes') and self.cluster_nodes is not None:
            _dict['cluster_nodes'] = self.cluster_nodes
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MembershipInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MembershipInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MembershipInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MissingRevsResult():
    """
    Schema for mapping document IDs to lists of missed revisions.

    :attr dict missed_revs: (optional) Schema for mapping document IDs to lists of
          revisions.
    """

    def __init__(self,
                 *,
                 missed_revs: dict = None) -> None:
        """
        Initialize a MissingRevsResult object.

        :param dict missed_revs: (optional) Schema for mapping document IDs to
               lists of revisions.
        """
        self.missed_revs = missed_revs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MissingRevsResult':
        """Initialize a MissingRevsResult object from a json dictionary."""
        args = {}
        if 'missed_revs' in _dict:
            args['missed_revs'] = _dict.get('missed_revs')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MissingRevsResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'missed_revs') and self.missed_revs is not None:
            _dict['missed_revs'] = self.missed_revs
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MissingRevsResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MissingRevsResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MissingRevsResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Ok():
    """
    Schema for an OK result.

    :attr bool ok: (optional) ok.
    """

    def __init__(self,
                 *,
                 ok: bool = None) -> None:
        """
        Initialize a Ok object.

        :param bool ok: (optional) ok.
        """
        self.ok = ok

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Ok':
        """Initialize a Ok object from a json dictionary."""
        args = {}
        if 'ok' in _dict:
            args['ok'] = _dict.get('ok')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Ok object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ok') and self.ok is not None:
            _dict['ok'] = self.ok
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Ok object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Ok') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Ok') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PartitionInformation():
    """
    Schema for information about a database partition.

    :attr str db_name: (optional) The name of the database.
    :attr int doc_count: (optional) A count of the documents in the specified
          database partition.
    :attr int doc_del_count: (optional) Number of deleted documents.
    :attr str partition: (optional) The name of the partition in the database.
    :attr PartitionInformationIndexes partitioned_indexes: (optional) Schema for
          information about the partition index count and limit in a database.
    :attr PartitionInformationSizes sizes: (optional) The size of active and
          external data, in bytes.
    """

    def __init__(self,
                 *,
                 db_name: str = None,
                 doc_count: int = None,
                 doc_del_count: int = None,
                 partition: str = None,
                 partitioned_indexes: 'PartitionInformationIndexes' = None,
                 sizes: 'PartitionInformationSizes' = None) -> None:
        """
        Initialize a PartitionInformation object.

        :param str db_name: (optional) The name of the database.
        :param int doc_count: (optional) A count of the documents in the specified
               database partition.
        :param int doc_del_count: (optional) Number of deleted documents.
        :param str partition: (optional) The name of the partition in the database.
        :param PartitionInformationIndexes partitioned_indexes: (optional) Schema
               for information about the partition index count and limit in a database.
        :param PartitionInformationSizes sizes: (optional) The size of active and
               external data, in bytes.
        """
        self.db_name = db_name
        self.doc_count = doc_count
        self.doc_del_count = doc_del_count
        self.partition = partition
        self.partitioned_indexes = partitioned_indexes
        self.sizes = sizes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PartitionInformation':
        """Initialize a PartitionInformation object from a json dictionary."""
        args = {}
        if 'db_name' in _dict:
            args['db_name'] = _dict.get('db_name')
        if 'doc_count' in _dict:
            args['doc_count'] = _dict.get('doc_count')
        if 'doc_del_count' in _dict:
            args['doc_del_count'] = _dict.get('doc_del_count')
        if 'partition' in _dict:
            args['partition'] = _dict.get('partition')
        if 'partitioned_indexes' in _dict:
            args['partitioned_indexes'] = PartitionInformationIndexes.from_dict(_dict.get('partitioned_indexes'))
        if 'sizes' in _dict:
            args['sizes'] = PartitionInformationSizes.from_dict(_dict.get('sizes'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PartitionInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'db_name') and self.db_name is not None:
            _dict['db_name'] = self.db_name
        if hasattr(self, 'doc_count') and self.doc_count is not None:
            _dict['doc_count'] = self.doc_count
        if hasattr(self, 'doc_del_count') and self.doc_del_count is not None:
            _dict['doc_del_count'] = self.doc_del_count
        if hasattr(self, 'partition') and self.partition is not None:
            _dict['partition'] = self.partition
        if hasattr(self, 'partitioned_indexes') and self.partitioned_indexes is not None:
            _dict['partitioned_indexes'] = self.partitioned_indexes.to_dict()
        if hasattr(self, 'sizes') and self.sizes is not None:
            _dict['sizes'] = self.sizes.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PartitionInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PartitionInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PartitionInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PartitionInformationIndexes():
    """
    Schema for information about the partition index count and limit in a database.

    :attr int count: (optional) Total count of the partitioned indexes.
    :attr PartitionInformationIndexesIndexes indexes: (optional) The count breakdown
          of partitioned indexes.
    :attr int limit: (optional) The partitioned index limit.
    """

    def __init__(self,
                 *,
                 count: int = None,
                 indexes: 'PartitionInformationIndexesIndexes' = None,
                 limit: int = None) -> None:
        """
        Initialize a PartitionInformationIndexes object.

        :param int count: (optional) Total count of the partitioned indexes.
        :param PartitionInformationIndexesIndexes indexes: (optional) The count
               breakdown of partitioned indexes.
        :param int limit: (optional) The partitioned index limit.
        """
        self.count = count
        self.indexes = indexes
        self.limit = limit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PartitionInformationIndexes':
        """Initialize a PartitionInformationIndexes object from a json dictionary."""
        args = {}
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        if 'indexes' in _dict:
            args['indexes'] = PartitionInformationIndexesIndexes.from_dict(_dict.get('indexes'))
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PartitionInformationIndexes object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'indexes') and self.indexes is not None:
            _dict['indexes'] = self.indexes.to_dict()
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PartitionInformationIndexes object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PartitionInformationIndexes') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PartitionInformationIndexes') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PartitionInformationIndexesIndexes():
    """
    The count breakdown of partitioned indexes.

    :attr int search: (optional) Number of partitioned search indexes.
    :attr int view: (optional) Number of partitioned view indexes.
    """

    def __init__(self,
                 *,
                 search: int = None,
                 view: int = None) -> None:
        """
        Initialize a PartitionInformationIndexesIndexes object.

        :param int search: (optional) Number of partitioned search indexes.
        :param int view: (optional) Number of partitioned view indexes.
        """
        self.search = search
        self.view = view

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PartitionInformationIndexesIndexes':
        """Initialize a PartitionInformationIndexesIndexes object from a json dictionary."""
        args = {}
        if 'search' in _dict:
            args['search'] = _dict.get('search')
        if 'view' in _dict:
            args['view'] = _dict.get('view')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PartitionInformationIndexesIndexes object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'search') and self.search is not None:
            _dict['search'] = self.search
        if hasattr(self, 'view') and self.view is not None:
            _dict['view'] = self.view
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PartitionInformationIndexesIndexes object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PartitionInformationIndexesIndexes') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PartitionInformationIndexesIndexes') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PartitionInformationSizes():
    """
    The size of active and external data, in bytes.

    :attr int active: (optional) The size of live data inside the database, in
          bytes.
    :attr int external: (optional) The uncompressed size of database contents in
          bytes.
    """

    def __init__(self,
                 *,
                 active: int = None,
                 external: int = None) -> None:
        """
        Initialize a PartitionInformationSizes object.

        :param int active: (optional) The size of live data inside the database, in
               bytes.
        :param int external: (optional) The uncompressed size of database contents
               in bytes.
        """
        self.active = active
        self.external = external

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PartitionInformationSizes':
        """Initialize a PartitionInformationSizes object from a json dictionary."""
        args = {}
        if 'active' in _dict:
            args['active'] = _dict.get('active')
        if 'external' in _dict:
            args['external'] = _dict.get('external')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PartitionInformationSizes object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'active') and self.active is not None:
            _dict['active'] = self.active
        if hasattr(self, 'external') and self.external is not None:
            _dict['external'] = self.external
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PartitionInformationSizes object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PartitionInformationSizes') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PartitionInformationSizes') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ReplicationCreateTargetParameters():
    """
    Request parameters to use during target database creation.

    :attr int n: (optional) Schema for the number of replicas of a database in a
          cluster.
    :attr bool partitioned: (optional) Parameter to specify whether to enable
          database partitions when creating the target database.
    :attr int q: (optional) Schema for the number of shards in a database. Each
          shard is a partition of the hash value range.
    """

    def __init__(self,
                 *,
                 n: int = None,
                 partitioned: bool = None,
                 q: int = None) -> None:
        """
        Initialize a ReplicationCreateTargetParameters object.

        :param int n: (optional) Schema for the number of replicas of a database in
               a cluster.
        :param bool partitioned: (optional) Parameter to specify whether to enable
               database partitions when creating the target database.
        :param int q: (optional) Schema for the number of shards in a database.
               Each shard is a partition of the hash value range.
        """
        self.n = n
        self.partitioned = partitioned
        self.q = q

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReplicationCreateTargetParameters':
        """Initialize a ReplicationCreateTargetParameters object from a json dictionary."""
        args = {}
        if 'n' in _dict:
            args['n'] = _dict.get('n')
        if 'partitioned' in _dict:
            args['partitioned'] = _dict.get('partitioned')
        if 'q' in _dict:
            args['q'] = _dict.get('q')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReplicationCreateTargetParameters object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'n') and self.n is not None:
            _dict['n'] = self.n
        if hasattr(self, 'partitioned') and self.partitioned is not None:
            _dict['partitioned'] = self.partitioned
        if hasattr(self, 'q') and self.q is not None:
            _dict['q'] = self.q
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReplicationCreateTargetParameters object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReplicationCreateTargetParameters') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReplicationCreateTargetParameters') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ReplicationDatabase():
    """
    Schema for a replication source or target database.

    :attr ReplicationDatabaseAuth auth: (optional) Schema for replication source or
          target database authentication.
    :attr dict headers_: (optional) Replication request headers.
    :attr str url: (optional) Replication database URL.
    """

    def __init__(self,
                 *,
                 auth: 'ReplicationDatabaseAuth' = None,
                 headers_: dict = None,
                 url: str = None) -> None:
        """
        Initialize a ReplicationDatabase object.

        :param ReplicationDatabaseAuth auth: (optional) Schema for replication
               source or target database authentication.
        :param dict headers_: (optional) Replication request headers.
        :param str url: (optional) Replication database URL.
        """
        self.auth = auth
        self.headers_ = headers_
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReplicationDatabase':
        """Initialize a ReplicationDatabase object from a json dictionary."""
        args = {}
        if 'auth' in _dict:
            args['auth'] = ReplicationDatabaseAuth.from_dict(_dict.get('auth'))
        if 'headers' in _dict:
            args['headers_'] = _dict.get('headers')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReplicationDatabase object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'auth') and self.auth is not None:
            _dict['auth'] = self.auth.to_dict()
        if hasattr(self, 'headers_') and self.headers_ is not None:
            _dict['headers'] = self.headers_
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReplicationDatabase object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReplicationDatabase') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReplicationDatabase') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ReplicationDatabaseAuth():
    """
    Schema for replication source or target database authentication.

    :attr ReplicationDatabaseAuthIam iam: (optional) Schema for an IAM API key for
          replication database authentication.
    """

    def __init__(self,
                 *,
                 iam: 'ReplicationDatabaseAuthIam' = None) -> None:
        """
        Initialize a ReplicationDatabaseAuth object.

        :param ReplicationDatabaseAuthIam iam: (optional) Schema for an IAM API key
               for replication database authentication.
        """
        self.iam = iam

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReplicationDatabaseAuth':
        """Initialize a ReplicationDatabaseAuth object from a json dictionary."""
        args = {}
        if 'iam' in _dict:
            args['iam'] = ReplicationDatabaseAuthIam.from_dict(_dict.get('iam'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReplicationDatabaseAuth object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'iam') and self.iam is not None:
            _dict['iam'] = self.iam.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReplicationDatabaseAuth object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReplicationDatabaseAuth') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReplicationDatabaseAuth') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ReplicationDatabaseAuthIam():
    """
    Schema for an IAM API key for replication database authentication.

    :attr str api_key: (optional) IAM API key.
    """

    def __init__(self,
                 *,
                 api_key: str = None) -> None:
        """
        Initialize a ReplicationDatabaseAuthIam object.

        :param str api_key: (optional) IAM API key.
        """
        self.api_key = api_key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReplicationDatabaseAuthIam':
        """Initialize a ReplicationDatabaseAuthIam object from a json dictionary."""
        args = {}
        if 'api_key' in _dict:
            args['api_key'] = _dict.get('api_key')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReplicationDatabaseAuthIam object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'api_key') and self.api_key is not None:
            _dict['api_key'] = self.api_key
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReplicationDatabaseAuthIam object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReplicationDatabaseAuthIam') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReplicationDatabaseAuthIam') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ReplicationDocument():
    """
    Schema for a replication document. Note that `selector`, `doc_ids`, and `filter` are
    incompatible with each other.

    :attr dict attachments: (optional) Schema for a map of attachment name to
          attachment metadata.
    :attr List[str] conflicts: (optional) Schema for a list of document revision
          identifiers.
    :attr bool deleted: (optional) Deletion flag. Available if document was removed.
    :attr List[str] deleted_conflicts: (optional) Schema for a list of document
          revision identifiers.
    :attr str id: (optional) Document ID.
    :attr str local_seq: (optional) Document's update sequence in current database.
          Available if requested with local_seq=true query parameter.
    :attr str rev: (optional) Schema for a document revision identifier.
    :attr Revisions revisions: (optional) Schema for list of revision information.
    :attr List[DocumentRevisionStatus] revs_info: (optional) Schema for a list of
          objects with information about local revisions and their status.
    :attr bool cancel: (optional) Cancels the replication.
    :attr int checkpoint_interval: (optional) Defines replication checkpoint
          interval in milliseconds.
    :attr int connection_timeout: (optional) HTTP connection timeout per
          replication. Even for very fast/reliable networks it might need to be increased
          if a remote database is too busy.
    :attr bool continuous: (optional) Configure the replication to be continuous.
    :attr bool create_target: (optional) Creates the target database. Requires
          administrator privileges on target server.
    :attr ReplicationCreateTargetParameters create_target_params: (optional) Request
          parameters to use during target database creation.
    :attr List[str] doc_ids: (optional) Schema for a list of document IDs.
    :attr str filter: (optional) The name of a filter function which is defined in a
          design document in the source database in {ddoc_id}/{filter} format. It
          determines which documents get replicated. Using the selector option provides
          performance benefits when compared with using the filter option. Use the
          selector option when possible.
    :attr int http_connections: (optional) Maximum number of HTTP connections per
          replication.
    :attr dict query_params: (optional) Schema for a map of string key value pairs,
          such as query parameters.
    :attr int retries_per_request: (optional) Number of times a replication request
          is retried. The requests are retried with a doubling exponential backoff
          starting at 0.25 seconds, with a cap at 5 minutes.
    :attr dict selector: (optional) JSON object describing criteria used to select
          documents. The selector specifies fields in the document, and provides an
          expression to evaluate with the field content or other data.
          The selector object must:
            * Be structured as valid JSON.
            * Contain a valid query expression.
          Using a selector is significantly more efficient than using a JavaScript filter
          function, and is the recommended option if filtering on document attributes
          only.
          Elementary selector syntax requires you to specify one or more fields, and the
          corresponding values required for those fields. You can create more complex
          selector expressions by combining operators.
          Operators are identified by the use of a dollar sign `$` prefix in the name
          field.
          There are two core types of operators in the selector syntax:
          * Combination operators: applied at the topmost level of selection. They are
          used to combine selectors. In addition to the common boolean operators (`$and`,
          `$or`, `$not`, `$nor`) there are three combination operators: `$all`,
          `$elemMatch`, and `$allMatch`. A combination operator takes a single argument.
          The argument is either another selector, or an array of selectors.
          * Condition operators: are specific to a field, and are used to evaluate the
          value stored in that field. For instance, the basic `$eq` operator matches when
          the specified field contains a value that is equal to the supplied argument.
    :attr str since_seq: (optional) Start the replication at a specific sequence
          value.
    :attr str socket_options: (optional) Replication socket options.
    :attr ReplicationDatabase source: (optional) Schema for a replication source or
          target database.
    :attr str source_proxy: (optional) Address of a (http or socks5 protocol) proxy
          server through which replication with the source database should occur.
    :attr ReplicationDatabase target: (optional) Schema for a replication source or
          target database.
    :attr str target_proxy: (optional) Address of a (http or socks5 protocol) proxy
          server through which replication with the target database should occur.
    :attr bool use_checkpoints: (optional) Specify if checkpoints should be saved
          during replication. Using checkpoints means a replication can be efficiently
          resumed.
    :attr UserContext user_ctx: (optional) Schema for the user context of a session.
    :attr int worker_batch_size: (optional) Controls how many documents are
          processed. After each batch a checkpoint is written so this controls how
          frequently checkpointing occurs.
    :attr int worker_processes: (optional) Controls how many separate processes will
          read from the changes manager and write to the target. A higher number can
          improve throughput.
    """

    # The set of defined properties for the class
    _properties = frozenset(['attachments', '_attachments', 'conflicts', '_conflicts', 'deleted', '_deleted', 'deleted_conflicts', '_deleted_conflicts', 'id', '_id', 'local_seq', '_local_seq', 'rev', '_rev', 'revisions', '_revisions', 'revs_info', '_revs_info', 'cancel', 'checkpoint_interval', 'connection_timeout', 'continuous', 'create_target', 'create_target_params', 'doc_ids', 'filter', 'http_connections', 'query_params', 'retries_per_request', 'selector', 'since_seq', 'socket_options', 'source', 'source_proxy', 'target', 'target_proxy', 'use_checkpoints', 'user_ctx', 'worker_batch_size', 'worker_processes'])

    def __init__(self,
                 *,
                 attachments: dict = None,
                 conflicts: List[str] = None,
                 deleted: bool = None,
                 deleted_conflicts: List[str] = None,
                 id: str = None,
                 local_seq: str = None,
                 rev: str = None,
                 revisions: 'Revisions' = None,
                 revs_info: List['DocumentRevisionStatus'] = None,
                 cancel: bool = None,
                 checkpoint_interval: int = None,
                 connection_timeout: int = None,
                 continuous: bool = None,
                 create_target: bool = None,
                 create_target_params: 'ReplicationCreateTargetParameters' = None,
                 doc_ids: List[str] = None,
                 filter: str = None,
                 http_connections: int = None,
                 query_params: dict = None,
                 retries_per_request: int = None,
                 selector: dict = None,
                 since_seq: str = None,
                 socket_options: str = None,
                 source: 'ReplicationDatabase' = None,
                 source_proxy: str = None,
                 target: 'ReplicationDatabase' = None,
                 target_proxy: str = None,
                 use_checkpoints: bool = None,
                 user_ctx: 'UserContext' = None,
                 worker_batch_size: int = None,
                 worker_processes: int = None,
                 **kwargs) -> None:
        """
        Initialize a ReplicationDocument object.

        :param dict attachments: (optional) Schema for a map of attachment name to
               attachment metadata.
        :param List[str] conflicts: (optional) Schema for a list of document
               revision identifiers.
        :param bool deleted: (optional) Deletion flag. Available if document was
               removed.
        :param List[str] deleted_conflicts: (optional) Schema for a list of
               document revision identifiers.
        :param str id: (optional) Document ID.
        :param str local_seq: (optional) Document's update sequence in current
               database. Available if requested with local_seq=true query parameter.
        :param str rev: (optional) Schema for a document revision identifier.
        :param Revisions revisions: (optional) Schema for list of revision
               information.
        :param List[DocumentRevisionStatus] revs_info: (optional) Schema for a list
               of objects with information about local revisions and their status.
        :param bool cancel: (optional) Cancels the replication.
        :param int checkpoint_interval: (optional) Defines replication checkpoint
               interval in milliseconds.
        :param int connection_timeout: (optional) HTTP connection timeout per
               replication. Even for very fast/reliable networks it might need to be
               increased if a remote database is too busy.
        :param bool continuous: (optional) Configure the replication to be
               continuous.
        :param bool create_target: (optional) Creates the target database. Requires
               administrator privileges on target server.
        :param ReplicationCreateTargetParameters create_target_params: (optional)
               Request parameters to use during target database creation.
        :param List[str] doc_ids: (optional) Schema for a list of document IDs.
        :param str filter: (optional) The name of a filter function which is
               defined in a design document in the source database in {ddoc_id}/{filter}
               format. It determines which documents get replicated. Using the selector
               option provides performance benefits when compared with using the filter
               option. Use the selector option when possible.
        :param int http_connections: (optional) Maximum number of HTTP connections
               per replication.
        :param dict query_params: (optional) Schema for a map of string key value
               pairs, such as query parameters.
        :param int retries_per_request: (optional) Number of times a replication
               request is retried. The requests are retried with a doubling exponential
               backoff starting at 0.25 seconds, with a cap at 5 minutes.
        :param dict selector: (optional) JSON object describing criteria used to
               select documents. The selector specifies fields in the document, and
               provides an expression to evaluate with the field content or other data.
               The selector object must:
                 * Be structured as valid JSON.
                 * Contain a valid query expression.
               Using a selector is significantly more efficient than using a JavaScript
               filter function, and is the recommended option if filtering on document
               attributes only.
               Elementary selector syntax requires you to specify one or more fields, and
               the corresponding values required for those fields. You can create more
               complex selector expressions by combining operators.
               Operators are identified by the use of a dollar sign `$` prefix in the name
               field.
               There are two core types of operators in the selector syntax:
               * Combination operators: applied at the topmost level of selection. They
               are used to combine selectors. In addition to the common boolean operators
               (`$and`, `$or`, `$not`, `$nor`) there are three combination operators:
               `$all`, `$elemMatch`, and `$allMatch`. A combination operator takes a
               single argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
        :param str since_seq: (optional) Start the replication at a specific
               sequence value.
        :param str socket_options: (optional) Replication socket options.
        :param ReplicationDatabase source: (optional) Schema for a replication
               source or target database.
        :param str source_proxy: (optional) Address of a (http or socks5 protocol)
               proxy server through which replication with the source database should
               occur.
        :param ReplicationDatabase target: (optional) Schema for a replication
               source or target database.
        :param str target_proxy: (optional) Address of a (http or socks5 protocol)
               proxy server through which replication with the target database should
               occur.
        :param bool use_checkpoints: (optional) Specify if checkpoints should be
               saved during replication. Using checkpoints means a replication can be
               efficiently resumed.
        :param UserContext user_ctx: (optional) Schema for the user context of a
               session.
        :param int worker_batch_size: (optional) Controls how many documents are
               processed. After each batch a checkpoint is written so this controls how
               frequently checkpointing occurs.
        :param int worker_processes: (optional) Controls how many separate
               processes will read from the changes manager and write to the target. A
               higher number can improve throughput.
        :param **kwargs: (optional) Any additional properties.
        """
        self.attachments = attachments
        self.conflicts = conflicts
        self.deleted = deleted
        self.deleted_conflicts = deleted_conflicts
        self.id = id
        self.local_seq = local_seq
        self.rev = rev
        self.revisions = revisions
        self.revs_info = revs_info
        self.cancel = cancel
        self.checkpoint_interval = checkpoint_interval
        self.connection_timeout = connection_timeout
        self.continuous = continuous
        self.create_target = create_target
        self.create_target_params = create_target_params
        self.doc_ids = doc_ids
        self.filter = filter
        self.http_connections = http_connections
        self.query_params = query_params
        self.retries_per_request = retries_per_request
        self.selector = selector
        self.since_seq = since_seq
        self.socket_options = socket_options
        self.source = source
        self.source_proxy = source_proxy
        self.target = target
        self.target_proxy = target_proxy
        self.use_checkpoints = use_checkpoints
        self.user_ctx = user_ctx
        self.worker_batch_size = worker_batch_size
        self.worker_processes = worker_processes
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReplicationDocument':
        """Initialize a ReplicationDocument object from a json dictionary."""
        args = {}
        if '_attachments' in _dict:
            args['attachments'] = {k : Attachment.from_dict(v) for k, v in _dict.get('_attachments').items()}
        if '_conflicts' in _dict:
            args['conflicts'] = _dict.get('_conflicts')
        if '_deleted' in _dict:
            args['deleted'] = _dict.get('_deleted')
        if '_deleted_conflicts' in _dict:
            args['deleted_conflicts'] = _dict.get('_deleted_conflicts')
        if '_id' in _dict:
            args['id'] = _dict.get('_id')
        if '_local_seq' in _dict:
            args['local_seq'] = _dict.get('_local_seq')
        if '_rev' in _dict:
            args['rev'] = _dict.get('_rev')
        if '_revisions' in _dict:
            args['revisions'] = Revisions.from_dict(_dict.get('_revisions'))
        if '_revs_info' in _dict:
            args['revs_info'] = [DocumentRevisionStatus.from_dict(x) for x in _dict.get('_revs_info')]
        if 'cancel' in _dict:
            args['cancel'] = _dict.get('cancel')
        if 'checkpoint_interval' in _dict:
            args['checkpoint_interval'] = _dict.get('checkpoint_interval')
        if 'connection_timeout' in _dict:
            args['connection_timeout'] = _dict.get('connection_timeout')
        if 'continuous' in _dict:
            args['continuous'] = _dict.get('continuous')
        if 'create_target' in _dict:
            args['create_target'] = _dict.get('create_target')
        if 'create_target_params' in _dict:
            args['create_target_params'] = ReplicationCreateTargetParameters.from_dict(_dict.get('create_target_params'))
        if 'doc_ids' in _dict:
            args['doc_ids'] = _dict.get('doc_ids')
        if 'filter' in _dict:
            args['filter'] = _dict.get('filter')
        if 'http_connections' in _dict:
            args['http_connections'] = _dict.get('http_connections')
        if 'query_params' in _dict:
            args['query_params'] = _dict.get('query_params')
        if 'retries_per_request' in _dict:
            args['retries_per_request'] = _dict.get('retries_per_request')
        if 'selector' in _dict:
            args['selector'] = _dict.get('selector')
        if 'since_seq' in _dict:
            args['since_seq'] = _dict.get('since_seq')
        if 'socket_options' in _dict:
            args['socket_options'] = _dict.get('socket_options')
        if 'source' in _dict:
            args['source'] = ReplicationDatabase.from_dict(_dict.get('source'))
        if 'source_proxy' in _dict:
            args['source_proxy'] = _dict.get('source_proxy')
        if 'target' in _dict:
            args['target'] = ReplicationDatabase.from_dict(_dict.get('target'))
        if 'target_proxy' in _dict:
            args['target_proxy'] = _dict.get('target_proxy')
        if 'use_checkpoints' in _dict:
            args['use_checkpoints'] = _dict.get('use_checkpoints')
        if 'user_ctx' in _dict:
            args['user_ctx'] = UserContext.from_dict(_dict.get('user_ctx'))
        if 'worker_batch_size' in _dict:
            args['worker_batch_size'] = _dict.get('worker_batch_size')
        if 'worker_processes' in _dict:
            args['worker_processes'] = _dict.get('worker_processes')
        args.update({k:v for (k, v) in _dict.items() if k not in cls._properties})
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReplicationDocument object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attachments') and self.attachments is not None:
            _dict['_attachments'] = {k : v.to_dict() for k, v in self.attachments.items()}
        if hasattr(self, 'conflicts') and self.conflicts is not None:
            _dict['_conflicts'] = self.conflicts
        if hasattr(self, 'deleted') and self.deleted is not None:
            _dict['_deleted'] = self.deleted
        if hasattr(self, 'deleted_conflicts') and self.deleted_conflicts is not None:
            _dict['_deleted_conflicts'] = self.deleted_conflicts
        if hasattr(self, 'id') and self.id is not None:
            _dict['_id'] = self.id
        if hasattr(self, 'local_seq') and self.local_seq is not None:
            _dict['_local_seq'] = self.local_seq
        if hasattr(self, 'rev') and self.rev is not None:
            _dict['_rev'] = self.rev
        if hasattr(self, 'revisions') and self.revisions is not None:
            _dict['_revisions'] = self.revisions.to_dict()
        if hasattr(self, 'revs_info') and self.revs_info is not None:
            _dict['_revs_info'] = [x.to_dict() for x in self.revs_info]
        if hasattr(self, 'cancel') and self.cancel is not None:
            _dict['cancel'] = self.cancel
        if hasattr(self, 'checkpoint_interval') and self.checkpoint_interval is not None:
            _dict['checkpoint_interval'] = self.checkpoint_interval
        if hasattr(self, 'connection_timeout') and self.connection_timeout is not None:
            _dict['connection_timeout'] = self.connection_timeout
        if hasattr(self, 'continuous') and self.continuous is not None:
            _dict['continuous'] = self.continuous
        if hasattr(self, 'create_target') and self.create_target is not None:
            _dict['create_target'] = self.create_target
        if hasattr(self, 'create_target_params') and self.create_target_params is not None:
            _dict['create_target_params'] = self.create_target_params.to_dict()
        if hasattr(self, 'doc_ids') and self.doc_ids is not None:
            _dict['doc_ids'] = self.doc_ids
        if hasattr(self, 'filter') and self.filter is not None:
            _dict['filter'] = self.filter
        if hasattr(self, 'http_connections') and self.http_connections is not None:
            _dict['http_connections'] = self.http_connections
        if hasattr(self, 'query_params') and self.query_params is not None:
            _dict['query_params'] = self.query_params
        if hasattr(self, 'retries_per_request') and self.retries_per_request is not None:
            _dict['retries_per_request'] = self.retries_per_request
        if hasattr(self, 'selector') and self.selector is not None:
            _dict['selector'] = self.selector
        if hasattr(self, 'since_seq') and self.since_seq is not None:
            _dict['since_seq'] = self.since_seq
        if hasattr(self, 'socket_options') and self.socket_options is not None:
            _dict['socket_options'] = self.socket_options
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source.to_dict()
        if hasattr(self, 'source_proxy') and self.source_proxy is not None:
            _dict['source_proxy'] = self.source_proxy
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target.to_dict()
        if hasattr(self, 'target_proxy') and self.target_proxy is not None:
            _dict['target_proxy'] = self.target_proxy
        if hasattr(self, 'use_checkpoints') and self.use_checkpoints is not None:
            _dict['use_checkpoints'] = self.use_checkpoints
        if hasattr(self, 'user_ctx') and self.user_ctx is not None:
            _dict['user_ctx'] = self.user_ctx.to_dict()
        if hasattr(self, 'worker_batch_size') and self.worker_batch_size is not None:
            _dict['worker_batch_size'] = self.worker_batch_size
        if hasattr(self, 'worker_processes') and self.worker_processes is not None:
            _dict['worker_processes'] = self.worker_processes
        for _key in [k for k in vars(self).keys() if k not in ReplicationDocument._properties]:
            if getattr(self, _key, None) is not None:
                _dict[_key] = getattr(self, _key)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReplicationDocument object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReplicationDocument') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReplicationDocument') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ReplicationHistory():
    """
    Schema for replication history information.

    :attr int doc_write_failures: (optional) Number of document write failures.
    :attr int docs_read: (optional) Number of documents read.
    :attr int docs_written: (optional) Number of documents written to target.
    :attr str end_last_seq: (optional) Last sequence number in changes stream.
    :attr str end_time: (optional) Date/Time replication operation completed in RFC
          2822 format.
    :attr int missing_checked: (optional) Number of missing documents checked.
    :attr int missing_found: (optional) Number of missing documents found.
    :attr str recorded_seq: (optional) Last recorded sequence number.
    :attr str session_id: (optional) Session ID for this replication operation.
    :attr str start_last_seq: (optional) First sequence number in changes stream.
    :attr str start_time: (optional) Date/Time replication operation started in RFC
          2822 format.
    """

    def __init__(self,
                 *,
                 doc_write_failures: int = None,
                 docs_read: int = None,
                 docs_written: int = None,
                 end_last_seq: str = None,
                 end_time: str = None,
                 missing_checked: int = None,
                 missing_found: int = None,
                 recorded_seq: str = None,
                 session_id: str = None,
                 start_last_seq: str = None,
                 start_time: str = None) -> None:
        """
        Initialize a ReplicationHistory object.

        :param int doc_write_failures: (optional) Number of document write
               failures.
        :param int docs_read: (optional) Number of documents read.
        :param int docs_written: (optional) Number of documents written to target.
        :param str end_last_seq: (optional) Last sequence number in changes stream.
        :param str end_time: (optional) Date/Time replication operation completed
               in RFC 2822 format.
        :param int missing_checked: (optional) Number of missing documents checked.
        :param int missing_found: (optional) Number of missing documents found.
        :param str recorded_seq: (optional) Last recorded sequence number.
        :param str session_id: (optional) Session ID for this replication
               operation.
        :param str start_last_seq: (optional) First sequence number in changes
               stream.
        :param str start_time: (optional) Date/Time replication operation started
               in RFC 2822 format.
        """
        self.doc_write_failures = doc_write_failures
        self.docs_read = docs_read
        self.docs_written = docs_written
        self.end_last_seq = end_last_seq
        self.end_time = end_time
        self.missing_checked = missing_checked
        self.missing_found = missing_found
        self.recorded_seq = recorded_seq
        self.session_id = session_id
        self.start_last_seq = start_last_seq
        self.start_time = start_time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReplicationHistory':
        """Initialize a ReplicationHistory object from a json dictionary."""
        args = {}
        if 'doc_write_failures' in _dict:
            args['doc_write_failures'] = _dict.get('doc_write_failures')
        if 'docs_read' in _dict:
            args['docs_read'] = _dict.get('docs_read')
        if 'docs_written' in _dict:
            args['docs_written'] = _dict.get('docs_written')
        if 'end_last_seq' in _dict:
            args['end_last_seq'] = _dict.get('end_last_seq')
        if 'end_time' in _dict:
            args['end_time'] = _dict.get('end_time')
        if 'missing_checked' in _dict:
            args['missing_checked'] = _dict.get('missing_checked')
        if 'missing_found' in _dict:
            args['missing_found'] = _dict.get('missing_found')
        if 'recorded_seq' in _dict:
            args['recorded_seq'] = _dict.get('recorded_seq')
        if 'session_id' in _dict:
            args['session_id'] = _dict.get('session_id')
        if 'start_last_seq' in _dict:
            args['start_last_seq'] = _dict.get('start_last_seq')
        if 'start_time' in _dict:
            args['start_time'] = _dict.get('start_time')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReplicationHistory object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'doc_write_failures') and self.doc_write_failures is not None:
            _dict['doc_write_failures'] = self.doc_write_failures
        if hasattr(self, 'docs_read') and self.docs_read is not None:
            _dict['docs_read'] = self.docs_read
        if hasattr(self, 'docs_written') and self.docs_written is not None:
            _dict['docs_written'] = self.docs_written
        if hasattr(self, 'end_last_seq') and self.end_last_seq is not None:
            _dict['end_last_seq'] = self.end_last_seq
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['end_time'] = self.end_time
        if hasattr(self, 'missing_checked') and self.missing_checked is not None:
            _dict['missing_checked'] = self.missing_checked
        if hasattr(self, 'missing_found') and self.missing_found is not None:
            _dict['missing_found'] = self.missing_found
        if hasattr(self, 'recorded_seq') and self.recorded_seq is not None:
            _dict['recorded_seq'] = self.recorded_seq
        if hasattr(self, 'session_id') and self.session_id is not None:
            _dict['session_id'] = self.session_id
        if hasattr(self, 'start_last_seq') and self.start_last_seq is not None:
            _dict['start_last_seq'] = self.start_last_seq
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = self.start_time
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReplicationHistory object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReplicationHistory') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReplicationHistory') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ReplicationResult():
    """
    Schema for a replication result.

    :attr List[ReplicationHistory] history: (optional) Replication history.
    :attr bool ok: (optional) Replication status.
    :attr int replication_id_version: (optional) Replication protocol version.
    :attr str session_id: (optional) Unique session ID.
    :attr str source_last_seq: (optional) Last sequence number read from source
          database.
    """

    def __init__(self,
                 *,
                 history: List['ReplicationHistory'] = None,
                 ok: bool = None,
                 replication_id_version: int = None,
                 session_id: str = None,
                 source_last_seq: str = None) -> None:
        """
        Initialize a ReplicationResult object.

        :param List[ReplicationHistory] history: (optional) Replication history.
        :param bool ok: (optional) Replication status.
        :param int replication_id_version: (optional) Replication protocol version.
        :param str session_id: (optional) Unique session ID.
        :param str source_last_seq: (optional) Last sequence number read from
               source database.
        """
        self.history = history
        self.ok = ok
        self.replication_id_version = replication_id_version
        self.session_id = session_id
        self.source_last_seq = source_last_seq

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReplicationResult':
        """Initialize a ReplicationResult object from a json dictionary."""
        args = {}
        if 'history' in _dict:
            args['history'] = [ReplicationHistory.from_dict(x) for x in _dict.get('history')]
        if 'ok' in _dict:
            args['ok'] = _dict.get('ok')
        if 'replication_id_version' in _dict:
            args['replication_id_version'] = _dict.get('replication_id_version')
        if 'session_id' in _dict:
            args['session_id'] = _dict.get('session_id')
        if 'source_last_seq' in _dict:
            args['source_last_seq'] = _dict.get('source_last_seq')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReplicationResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'history') and self.history is not None:
            _dict['history'] = [x.to_dict() for x in self.history]
        if hasattr(self, 'ok') and self.ok is not None:
            _dict['ok'] = self.ok
        if hasattr(self, 'replication_id_version') and self.replication_id_version is not None:
            _dict['replication_id_version'] = self.replication_id_version
        if hasattr(self, 'session_id') and self.session_id is not None:
            _dict['session_id'] = self.session_id
        if hasattr(self, 'source_last_seq') and self.source_last_seq is not None:
            _dict['source_last_seq'] = self.source_last_seq
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReplicationResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReplicationResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReplicationResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Revisions():
    """
    Schema for list of revision information.

    :attr List[str] ids: (optional) Array of valid revision IDs, in reverse order
          (latest first).
    :attr int start: (optional) Prefix number for the latest revision.
    """

    def __init__(self,
                 *,
                 ids: List[str] = None,
                 start: int = None) -> None:
        """
        Initialize a Revisions object.

        :param List[str] ids: (optional) Array of valid revision IDs, in reverse
               order (latest first).
        :param int start: (optional) Prefix number for the latest revision.
        """
        self.ids = ids
        self.start = start

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Revisions':
        """Initialize a Revisions object from a json dictionary."""
        args = {}
        if 'ids' in _dict:
            args['ids'] = _dict.get('ids')
        if 'start' in _dict:
            args['start'] = _dict.get('start')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Revisions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ids') and self.ids is not None:
            _dict['ids'] = self.ids
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Revisions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Revisions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Revisions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RevsDiff():
    """
    Schema for information about missing revs and possible ancestors.

    :attr List[str] missing: (optional) List of missing revisions.
    :attr List[str] possible_ancestors: (optional) List of possible ancestor
          revisions.
    """

    def __init__(self,
                 *,
                 missing: List[str] = None,
                 possible_ancestors: List[str] = None) -> None:
        """
        Initialize a RevsDiff object.

        :param List[str] missing: (optional) List of missing revisions.
        :param List[str] possible_ancestors: (optional) List of possible ancestor
               revisions.
        """
        self.missing = missing
        self.possible_ancestors = possible_ancestors

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RevsDiff':
        """Initialize a RevsDiff object from a json dictionary."""
        args = {}
        if 'missing' in _dict:
            args['missing'] = _dict.get('missing')
        if 'possible_ancestors' in _dict:
            args['possible_ancestors'] = _dict.get('possible_ancestors')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RevsDiff object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'missing') and self.missing is not None:
            _dict['missing'] = self.missing
        if hasattr(self, 'possible_ancestors') and self.possible_ancestors is not None:
            _dict['possible_ancestors'] = self.possible_ancestors
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RevsDiff object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RevsDiff') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RevsDiff') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SchedulerDocsResult():
    """
    Schema for a listing of replication scheduler documents.

    :attr int total_rows: (optional) Number of total rows.
    :attr List[SchedulerDocument] docs: (optional) Array of replication scheduler
          doc objects.
    """

    def __init__(self,
                 *,
                 total_rows: int = None,
                 docs: List['SchedulerDocument'] = None) -> None:
        """
        Initialize a SchedulerDocsResult object.

        :param int total_rows: (optional) Number of total rows.
        :param List[SchedulerDocument] docs: (optional) Array of replication
               scheduler doc objects.
        """
        self.total_rows = total_rows
        self.docs = docs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchedulerDocsResult':
        """Initialize a SchedulerDocsResult object from a json dictionary."""
        args = {}
        if 'total_rows' in _dict:
            args['total_rows'] = _dict.get('total_rows')
        if 'docs' in _dict:
            args['docs'] = [SchedulerDocument.from_dict(x) for x in _dict.get('docs')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchedulerDocsResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_rows') and self.total_rows is not None:
            _dict['total_rows'] = self.total_rows
        if hasattr(self, 'docs') and self.docs is not None:
            _dict['docs'] = [x.to_dict() for x in self.docs]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SchedulerDocsResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SchedulerDocsResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SchedulerDocsResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SchedulerDocument():
    """
    Schema for a replication scheduler document.

    :attr str database: (optional) Database where replication document came from.
    :attr str doc_id: (optional) Replication document ID.
    :attr int error_count: (optional) Consecutive errors count. Indicates how many
          times in a row this replication has crashed. Replication will be retried with an
          exponential backoff based on this number. As soon as the replication succeeds
          this count is reset to 0. To can be used to get an idea why a particular
          replication is not making progress.
    :attr str id: (optional) Replication ID, or null if state is completed or
          failed.
    :attr SchedulerInfo info: (optional) Schema for scheduler document information.
          A JSON object that may contain additional information about the state. For error
          states this will contain an error field and string value.
    :attr datetime last_updated: (optional) Timestamp of last state update.
    :attr str node: (optional) Cluster node where the job is running.
    :attr str source: (optional) Replication source.
    :attr str source_proxy: (optional) Address of the (http or socks5 protocol)
          proxy server through which replication with the source database occurs.
    :attr datetime start_time: (optional) Timestamp of when the replication was
          started.
    :attr str state: (optional) Schema for replication state.
    :attr str target: (optional) Replication target.
    :attr str target_proxy: (optional) Address of the (http or socks5 protocol)
          proxy server through which replication with the target database occurs.
    """

    def __init__(self,
                 *,
                 database: str = None,
                 doc_id: str = None,
                 error_count: int = None,
                 id: str = None,
                 info: 'SchedulerInfo' = None,
                 last_updated: datetime = None,
                 node: str = None,
                 source: str = None,
                 source_proxy: str = None,
                 start_time: datetime = None,
                 state: str = None,
                 target: str = None,
                 target_proxy: str = None) -> None:
        """
        Initialize a SchedulerDocument object.

        :param str database: (optional) Database where replication document came
               from.
        :param str doc_id: (optional) Replication document ID.
        :param int error_count: (optional) Consecutive errors count. Indicates how
               many times in a row this replication has crashed. Replication will be
               retried with an exponential backoff based on this number. As soon as the
               replication succeeds this count is reset to 0. To can be used to get an
               idea why a particular replication is not making progress.
        :param str id: (optional) Replication ID, or null if state is completed or
               failed.
        :param SchedulerInfo info: (optional) Schema for scheduler document
               information. A JSON object that may contain additional information about
               the state. For error states this will contain an error field and string
               value.
        :param datetime last_updated: (optional) Timestamp of last state update.
        :param str node: (optional) Cluster node where the job is running.
        :param str source: (optional) Replication source.
        :param str source_proxy: (optional) Address of the (http or socks5
               protocol) proxy server through which replication with the source database
               occurs.
        :param datetime start_time: (optional) Timestamp of when the replication
               was started.
        :param str state: (optional) Schema for replication state.
        :param str target: (optional) Replication target.
        :param str target_proxy: (optional) Address of the (http or socks5
               protocol) proxy server through which replication with the target database
               occurs.
        """
        self.database = database
        self.doc_id = doc_id
        self.error_count = error_count
        self.id = id
        self.info = info
        self.last_updated = last_updated
        self.node = node
        self.source = source
        self.source_proxy = source_proxy
        self.start_time = start_time
        self.state = state
        self.target = target
        self.target_proxy = target_proxy

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchedulerDocument':
        """Initialize a SchedulerDocument object from a json dictionary."""
        args = {}
        if 'database' in _dict:
            args['database'] = _dict.get('database')
        if 'doc_id' in _dict:
            args['doc_id'] = _dict.get('doc_id')
        if 'error_count' in _dict:
            args['error_count'] = _dict.get('error_count')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'info' in _dict:
            args['info'] = SchedulerInfo.from_dict(_dict.get('info'))
        if 'last_updated' in _dict:
            args['last_updated'] = string_to_datetime(_dict.get('last_updated'))
        if 'node' in _dict:
            args['node'] = _dict.get('node')
        if 'source' in _dict:
            args['source'] = _dict.get('source')
        if 'source_proxy' in _dict:
            args['source_proxy'] = _dict.get('source_proxy')
        if 'start_time' in _dict:
            args['start_time'] = string_to_datetime(_dict.get('start_time'))
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        if 'target_proxy' in _dict:
            args['target_proxy'] = _dict.get('target_proxy')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchedulerDocument object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'database') and self.database is not None:
            _dict['database'] = self.database
        if hasattr(self, 'doc_id') and self.doc_id is not None:
            _dict['doc_id'] = self.doc_id
        if hasattr(self, 'error_count') and self.error_count is not None:
            _dict['error_count'] = self.error_count
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'info') and self.info is not None:
            _dict['info'] = self.info.to_dict()
        if hasattr(self, 'last_updated') and self.last_updated is not None:
            _dict['last_updated'] = datetime_to_string(self.last_updated)
        if hasattr(self, 'node') and self.node is not None:
            _dict['node'] = self.node
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'source_proxy') and self.source_proxy is not None:
            _dict['source_proxy'] = self.source_proxy
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = datetime_to_string(self.start_time)
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target
        if hasattr(self, 'target_proxy') and self.target_proxy is not None:
            _dict['target_proxy'] = self.target_proxy
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SchedulerDocument object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SchedulerDocument') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SchedulerDocument') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        Schema for replication state.
        """
        INITIALIZING = 'initializing'
        ERROR = 'error'
        PENDING = 'pending'
        RUNNING = 'running'
        CRASHING = 'crashing'
        COMPLETED = 'completed'
        FAILED = 'failed'


class SchedulerInfo():
    """
    Schema for scheduler document information. A JSON object that may contain additional
    information about the state. For error states this will contain an error field and
    string value.

    :attr int changes_pending: (optional) The count of changes not yet replicated.
    :attr str checkpointed_source_seq: (optional) The source sequence id which was
          last successfully replicated.
    :attr int doc_write_failures: (optional) The count of docs which failed to be
          written to the target.
    :attr int docs_read: (optional) The count of docs which have been read from the
          source.
    :attr int docs_written: (optional) The count of docs which have been written to
          the target.
    :attr str error: (optional) Replication error message.
    :attr int missing_revisions_found: (optional) The count of revisions which were
          found on the source, but missing from the target.
    :attr int revisions_checked: (optional) The count of revisions which have been
          checked since this replication began.
    :attr str source_seq: (optional) The last sequence number obtained from the
          source database changes feed.
    :attr str through_seq: (optional) The last sequence number processed by the
          replicator.
    """

    def __init__(self,
                 *,
                 changes_pending: int = None,
                 checkpointed_source_seq: str = None,
                 doc_write_failures: int = None,
                 docs_read: int = None,
                 docs_written: int = None,
                 error: str = None,
                 missing_revisions_found: int = None,
                 revisions_checked: int = None,
                 source_seq: str = None,
                 through_seq: str = None) -> None:
        """
        Initialize a SchedulerInfo object.

        :param int changes_pending: (optional) The count of changes not yet
               replicated.
        :param str checkpointed_source_seq: (optional) The source sequence id which
               was last successfully replicated.
        :param int doc_write_failures: (optional) The count of docs which failed to
               be written to the target.
        :param int docs_read: (optional) The count of docs which have been read
               from the source.
        :param int docs_written: (optional) The count of docs which have been
               written to the target.
        :param str error: (optional) Replication error message.
        :param int missing_revisions_found: (optional) The count of revisions which
               were found on the source, but missing from the target.
        :param int revisions_checked: (optional) The count of revisions which have
               been checked since this replication began.
        :param str source_seq: (optional) The last sequence number obtained from
               the source database changes feed.
        :param str through_seq: (optional) The last sequence number processed by
               the replicator.
        """
        self.changes_pending = changes_pending
        self.checkpointed_source_seq = checkpointed_source_seq
        self.doc_write_failures = doc_write_failures
        self.docs_read = docs_read
        self.docs_written = docs_written
        self.error = error
        self.missing_revisions_found = missing_revisions_found
        self.revisions_checked = revisions_checked
        self.source_seq = source_seq
        self.through_seq = through_seq

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchedulerInfo':
        """Initialize a SchedulerInfo object from a json dictionary."""
        args = {}
        if 'changes_pending' in _dict:
            args['changes_pending'] = _dict.get('changes_pending')
        if 'checkpointed_source_seq' in _dict:
            args['checkpointed_source_seq'] = _dict.get('checkpointed_source_seq')
        if 'doc_write_failures' in _dict:
            args['doc_write_failures'] = _dict.get('doc_write_failures')
        if 'docs_read' in _dict:
            args['docs_read'] = _dict.get('docs_read')
        if 'docs_written' in _dict:
            args['docs_written'] = _dict.get('docs_written')
        if 'error' in _dict:
            args['error'] = _dict.get('error')
        if 'missing_revisions_found' in _dict:
            args['missing_revisions_found'] = _dict.get('missing_revisions_found')
        if 'revisions_checked' in _dict:
            args['revisions_checked'] = _dict.get('revisions_checked')
        if 'source_seq' in _dict:
            args['source_seq'] = _dict.get('source_seq')
        if 'through_seq' in _dict:
            args['through_seq'] = _dict.get('through_seq')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchedulerInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'changes_pending') and self.changes_pending is not None:
            _dict['changes_pending'] = self.changes_pending
        if hasattr(self, 'checkpointed_source_seq') and self.checkpointed_source_seq is not None:
            _dict['checkpointed_source_seq'] = self.checkpointed_source_seq
        if hasattr(self, 'doc_write_failures') and self.doc_write_failures is not None:
            _dict['doc_write_failures'] = self.doc_write_failures
        if hasattr(self, 'docs_read') and self.docs_read is not None:
            _dict['docs_read'] = self.docs_read
        if hasattr(self, 'docs_written') and self.docs_written is not None:
            _dict['docs_written'] = self.docs_written
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error
        if hasattr(self, 'missing_revisions_found') and self.missing_revisions_found is not None:
            _dict['missing_revisions_found'] = self.missing_revisions_found
        if hasattr(self, 'revisions_checked') and self.revisions_checked is not None:
            _dict['revisions_checked'] = self.revisions_checked
        if hasattr(self, 'source_seq') and self.source_seq is not None:
            _dict['source_seq'] = self.source_seq
        if hasattr(self, 'through_seq') and self.through_seq is not None:
            _dict['through_seq'] = self.through_seq
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SchedulerInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SchedulerInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SchedulerInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SchedulerJob():
    """
    Schema for a replication scheduler job.

    :attr str database: (optional) Replication document database.
    :attr str doc_id: (optional) Replication document ID.
    :attr List[SchedulerJobEvent] history: (optional) Timestamped history of events
          as a list of objects.
    :attr str id: (optional) Schema for a replication job id.
    :attr SchedulerInfo info: (optional) Schema for scheduler document information.
          A JSON object that may contain additional information about the state. For error
          states this will contain an error field and string value.
    :attr str node: (optional) Cluster node where the job is running.
    :attr str pid: (optional) Replication process ID.
    :attr str source: (optional) Replication source.
    :attr datetime start_time: (optional) Timestamp of when the replication was
          started.
    :attr str target: (optional) Replication target.
    :attr str user: (optional) Name of user running replication.
    """

    def __init__(self,
                 *,
                 database: str = None,
                 doc_id: str = None,
                 history: List['SchedulerJobEvent'] = None,
                 id: str = None,
                 info: 'SchedulerInfo' = None,
                 node: str = None,
                 pid: str = None,
                 source: str = None,
                 start_time: datetime = None,
                 target: str = None,
                 user: str = None) -> None:
        """
        Initialize a SchedulerJob object.

        :param str database: (optional) Replication document database.
        :param str doc_id: (optional) Replication document ID.
        :param List[SchedulerJobEvent] history: (optional) Timestamped history of
               events as a list of objects.
        :param str id: (optional) Schema for a replication job id.
        :param SchedulerInfo info: (optional) Schema for scheduler document
               information. A JSON object that may contain additional information about
               the state. For error states this will contain an error field and string
               value.
        :param str node: (optional) Cluster node where the job is running.
        :param str pid: (optional) Replication process ID.
        :param str source: (optional) Replication source.
        :param datetime start_time: (optional) Timestamp of when the replication
               was started.
        :param str target: (optional) Replication target.
        :param str user: (optional) Name of user running replication.
        """
        self.database = database
        self.doc_id = doc_id
        self.history = history
        self.id = id
        self.info = info
        self.node = node
        self.pid = pid
        self.source = source
        self.start_time = start_time
        self.target = target
        self.user = user

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchedulerJob':
        """Initialize a SchedulerJob object from a json dictionary."""
        args = {}
        if 'database' in _dict:
            args['database'] = _dict.get('database')
        if 'doc_id' in _dict:
            args['doc_id'] = _dict.get('doc_id')
        if 'history' in _dict:
            args['history'] = [SchedulerJobEvent.from_dict(x) for x in _dict.get('history')]
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'info' in _dict:
            args['info'] = SchedulerInfo.from_dict(_dict.get('info'))
        if 'node' in _dict:
            args['node'] = _dict.get('node')
        if 'pid' in _dict:
            args['pid'] = _dict.get('pid')
        if 'source' in _dict:
            args['source'] = _dict.get('source')
        if 'start_time' in _dict:
            args['start_time'] = string_to_datetime(_dict.get('start_time'))
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        if 'user' in _dict:
            args['user'] = _dict.get('user')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchedulerJob object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'database') and self.database is not None:
            _dict['database'] = self.database
        if hasattr(self, 'doc_id') and self.doc_id is not None:
            _dict['doc_id'] = self.doc_id
        if hasattr(self, 'history') and self.history is not None:
            _dict['history'] = [x.to_dict() for x in self.history]
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'info') and self.info is not None:
            _dict['info'] = self.info.to_dict()
        if hasattr(self, 'node') and self.node is not None:
            _dict['node'] = self.node
        if hasattr(self, 'pid') and self.pid is not None:
            _dict['pid'] = self.pid
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = datetime_to_string(self.start_time)
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target
        if hasattr(self, 'user') and self.user is not None:
            _dict['user'] = self.user
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SchedulerJob object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SchedulerJob') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SchedulerJob') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SchedulerJobEvent():
    """
    Schema for a replication scheduler job event.

    :attr datetime timestamp: (optional) Timestamp of the event.
    :attr str type: (optional) Type of the event.
    """

    def __init__(self,
                 *,
                 timestamp: datetime = None,
                 type: str = None) -> None:
        """
        Initialize a SchedulerJobEvent object.

        :param datetime timestamp: (optional) Timestamp of the event.
        :param str type: (optional) Type of the event.
        """
        self.timestamp = timestamp
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchedulerJobEvent':
        """Initialize a SchedulerJobEvent object from a json dictionary."""
        args = {}
        if 'timestamp' in _dict:
            args['timestamp'] = string_to_datetime(_dict.get('timestamp'))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchedulerJobEvent object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'timestamp') and self.timestamp is not None:
            _dict['timestamp'] = datetime_to_string(self.timestamp)
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SchedulerJobEvent object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SchedulerJobEvent') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SchedulerJobEvent') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SchedulerJobsResult():
    """
    Schema for a listing of replication scheduler jobs.

    :attr int total_rows: (optional) Number of total rows.
    :attr List[SchedulerJob] jobs: (optional) Array of replication job objects.
    """

    def __init__(self,
                 *,
                 total_rows: int = None,
                 jobs: List['SchedulerJob'] = None) -> None:
        """
        Initialize a SchedulerJobsResult object.

        :param int total_rows: (optional) Number of total rows.
        :param List[SchedulerJob] jobs: (optional) Array of replication job
               objects.
        """
        self.total_rows = total_rows
        self.jobs = jobs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchedulerJobsResult':
        """Initialize a SchedulerJobsResult object from a json dictionary."""
        args = {}
        if 'total_rows' in _dict:
            args['total_rows'] = _dict.get('total_rows')
        if 'jobs' in _dict:
            args['jobs'] = [SchedulerJob.from_dict(x) for x in _dict.get('jobs')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchedulerJobsResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_rows') and self.total_rows is not None:
            _dict['total_rows'] = self.total_rows
        if hasattr(self, 'jobs') and self.jobs is not None:
            _dict['jobs'] = [x.to_dict() for x in self.jobs]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SchedulerJobsResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SchedulerJobsResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SchedulerJobsResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SearchAnalyzeResult():
    """
    Schema for the output of testing search analyzer tokenization.

    :attr List[str] tokens: (optional) tokens.
    """

    def __init__(self,
                 *,
                 tokens: List[str] = None) -> None:
        """
        Initialize a SearchAnalyzeResult object.

        :param List[str] tokens: (optional) tokens.
        """
        self.tokens = tokens

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchAnalyzeResult':
        """Initialize a SearchAnalyzeResult object from a json dictionary."""
        args = {}
        if 'tokens' in _dict:
            args['tokens'] = _dict.get('tokens')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchAnalyzeResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'tokens') and self.tokens is not None:
            _dict['tokens'] = self.tokens
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchAnalyzeResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchAnalyzeResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchAnalyzeResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SearchIndexDefinition():
    """
    Schema for a search index definition.

    :attr AnalyzerConfiguration analyzer: (optional) Schema for a search analyzer
          configuration.
    :attr str index: String form of a JavaScript function that is called for each
          document in the database. The function takes the document as a parameter,
          extracts some data from it, and then calls the `index` function to index that
          data. The index function takes 2, or optionally 3, parameters.
          * The first parameter is the name of the field you intend to use when
            querying the index. If the special value `"default"` is used when you
            define the name, you do not have to specify a field name at query time.
          * The second parameter is the data to be indexed. This data must be only a
            string, number, or boolean. Other types will cause an error to be thrown
            by the index function call.
          * The optional third parameter is a JavaScript object with these
            properties:
              * `facet` - boolean, default `false` - Creates a faceted index.
              * `index` - boolean, default `true` - If set to `false`, the data
                cannot be used for searches, but can still be retrieved from the
                index if `store` is set to `true`.
              * `store` - boolean, default `true` - If true, the value is returned
                in the search result; otherwise, the value is not returned.
    """

    def __init__(self,
                 index: str,
                 *,
                 analyzer: 'AnalyzerConfiguration' = None) -> None:
        """
        Initialize a SearchIndexDefinition object.

        :param str index: String form of a JavaScript function that is called for
               each document in the database. The function takes the document as a
               parameter, extracts some data from it, and then calls the `index` function
               to index that data. The index function takes 2, or optionally 3,
               parameters.
               * The first parameter is the name of the field you intend to use when
                 querying the index. If the special value `"default"` is used when you
                 define the name, you do not have to specify a field name at query time.
               * The second parameter is the data to be indexed. This data must be only a
                 string, number, or boolean. Other types will cause an error to be thrown
                 by the index function call.
               * The optional third parameter is a JavaScript object with these
                 properties:
                   * `facet` - boolean, default `false` - Creates a faceted index.
                   * `index` - boolean, default `true` - If set to `false`, the data
                     cannot be used for searches, but can still be retrieved from the
                     index if `store` is set to `true`.
                   * `store` - boolean, default `true` - If true, the value is returned
                     in the search result; otherwise, the value is not returned.
        :param AnalyzerConfiguration analyzer: (optional) Schema for a search
               analyzer configuration.
        """
        self.analyzer = analyzer
        self.index = index

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchIndexDefinition':
        """Initialize a SearchIndexDefinition object from a json dictionary."""
        args = {}
        if 'analyzer' in _dict:
            args['analyzer'] = AnalyzerConfiguration.from_dict(_dict.get('analyzer'))
        if 'index' in _dict:
            args['index'] = _dict.get('index')
        else:
            raise ValueError('Required property \'index\' not present in SearchIndexDefinition JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchIndexDefinition object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'analyzer') and self.analyzer is not None:
            _dict['analyzer'] = self.analyzer.to_dict()
        if hasattr(self, 'index') and self.index is not None:
            _dict['index'] = self.index
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchIndexDefinition object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchIndexDefinition') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchIndexDefinition') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SearchIndexInfo():
    """
    Schema for metadata information about a search index.

    :attr int committed_seq: The committed sequence identifier.
    :attr int disk_size: The size of the search index on disk.
    :attr int doc_count: The count of the number of indexed documents.
    :attr int doc_del_count: The number of deleted documents.
    :attr int pending_seq: The pending sequence identifier.
    """

    def __init__(self,
                 committed_seq: int,
                 disk_size: int,
                 doc_count: int,
                 doc_del_count: int,
                 pending_seq: int) -> None:
        """
        Initialize a SearchIndexInfo object.

        :param int committed_seq: The committed sequence identifier.
        :param int disk_size: The size of the search index on disk.
        :param int doc_count: The count of the number of indexed documents.
        :param int doc_del_count: The number of deleted documents.
        :param int pending_seq: The pending sequence identifier.
        """
        self.committed_seq = committed_seq
        self.disk_size = disk_size
        self.doc_count = doc_count
        self.doc_del_count = doc_del_count
        self.pending_seq = pending_seq

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchIndexInfo':
        """Initialize a SearchIndexInfo object from a json dictionary."""
        args = {}
        if 'committed_seq' in _dict:
            args['committed_seq'] = _dict.get('committed_seq')
        else:
            raise ValueError('Required property \'committed_seq\' not present in SearchIndexInfo JSON')
        if 'disk_size' in _dict:
            args['disk_size'] = _dict.get('disk_size')
        else:
            raise ValueError('Required property \'disk_size\' not present in SearchIndexInfo JSON')
        if 'doc_count' in _dict:
            args['doc_count'] = _dict.get('doc_count')
        else:
            raise ValueError('Required property \'doc_count\' not present in SearchIndexInfo JSON')
        if 'doc_del_count' in _dict:
            args['doc_del_count'] = _dict.get('doc_del_count')
        else:
            raise ValueError('Required property \'doc_del_count\' not present in SearchIndexInfo JSON')
        if 'pending_seq' in _dict:
            args['pending_seq'] = _dict.get('pending_seq')
        else:
            raise ValueError('Required property \'pending_seq\' not present in SearchIndexInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchIndexInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'committed_seq') and self.committed_seq is not None:
            _dict['committed_seq'] = self.committed_seq
        if hasattr(self, 'disk_size') and self.disk_size is not None:
            _dict['disk_size'] = self.disk_size
        if hasattr(self, 'doc_count') and self.doc_count is not None:
            _dict['doc_count'] = self.doc_count
        if hasattr(self, 'doc_del_count') and self.doc_del_count is not None:
            _dict['doc_del_count'] = self.doc_del_count
        if hasattr(self, 'pending_seq') and self.pending_seq is not None:
            _dict['pending_seq'] = self.pending_seq
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchIndexInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchIndexInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchIndexInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SearchInfoResult():
    """
    Schema for search index information.

    :attr str name: The name of the search index prefixed by the design document ID
          where the index is stored.
    :attr SearchIndexInfo search_index: Schema for metadata information about a
          search index.
    """

    def __init__(self,
                 name: str,
                 search_index: 'SearchIndexInfo') -> None:
        """
        Initialize a SearchInfoResult object.

        :param str name: The name of the search index prefixed by the design
               document ID where the index is stored.
        :param SearchIndexInfo search_index: Schema for metadata information about
               a search index.
        """
        self.name = name
        self.search_index = search_index

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchInfoResult':
        """Initialize a SearchInfoResult object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in SearchInfoResult JSON')
        if 'search_index' in _dict:
            args['search_index'] = SearchIndexInfo.from_dict(_dict.get('search_index'))
        else:
            raise ValueError('Required property \'search_index\' not present in SearchInfoResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchInfoResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'search_index') and self.search_index is not None:
            _dict['search_index'] = self.search_index.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchInfoResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchInfoResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchInfoResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SearchResult():
    """
    Schema for the result of a query search operation.

    :attr int total_rows: (optional) Number of total rows.
    :attr str bookmark: (optional) Opaque bookmark token used when paginating
          results.
    :attr str by: (optional) Grouped search matches.
    :attr dict counts: (optional) The counts facet syntax returns the number of
          query results for each unique value of each named field.
    :attr dict ranges: (optional) The range facet syntax reuses the standard Lucene
          syntax for ranges to return counts of results that fit into each specified
          category.
    :attr List[SearchResultRow] rows: (optional) Array of row objects.
    :attr List[SearchResultProperties] groups: (optional) Array of grouped search
          matches.
    """

    def __init__(self,
                 *,
                 total_rows: int = None,
                 bookmark: str = None,
                 by: str = None,
                 counts: dict = None,
                 ranges: dict = None,
                 rows: List['SearchResultRow'] = None,
                 groups: List['SearchResultProperties'] = None) -> None:
        """
        Initialize a SearchResult object.

        :param int total_rows: (optional) Number of total rows.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param str by: (optional) Grouped search matches.
        :param dict counts: (optional) The counts facet syntax returns the number
               of query results for each unique value of each named field.
        :param dict ranges: (optional) The range facet syntax reuses the standard
               Lucene syntax for ranges to return counts of results that fit into each
               specified category.
        :param List[SearchResultRow] rows: (optional) Array of row objects.
        :param List[SearchResultProperties] groups: (optional) Array of grouped
               search matches.
        """
        self.total_rows = total_rows
        self.bookmark = bookmark
        self.by = by
        self.counts = counts
        self.ranges = ranges
        self.rows = rows
        self.groups = groups

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchResult':
        """Initialize a SearchResult object from a json dictionary."""
        args = {}
        if 'total_rows' in _dict:
            args['total_rows'] = _dict.get('total_rows')
        if 'bookmark' in _dict:
            args['bookmark'] = _dict.get('bookmark')
        if 'by' in _dict:
            args['by'] = _dict.get('by')
        if 'counts' in _dict:
            args['counts'] = _dict.get('counts')
        if 'ranges' in _dict:
            args['ranges'] = _dict.get('ranges')
        if 'rows' in _dict:
            args['rows'] = [SearchResultRow.from_dict(x) for x in _dict.get('rows')]
        if 'groups' in _dict:
            args['groups'] = [SearchResultProperties.from_dict(x) for x in _dict.get('groups')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_rows') and self.total_rows is not None:
            _dict['total_rows'] = self.total_rows
        if hasattr(self, 'bookmark') and self.bookmark is not None:
            _dict['bookmark'] = self.bookmark
        if hasattr(self, 'by') and self.by is not None:
            _dict['by'] = self.by
        if hasattr(self, 'counts') and self.counts is not None:
            _dict['counts'] = self.counts
        if hasattr(self, 'ranges') and self.ranges is not None:
            _dict['ranges'] = self.ranges
        if hasattr(self, 'rows') and self.rows is not None:
            _dict['rows'] = [x.to_dict() for x in self.rows]
        if hasattr(self, 'groups') and self.groups is not None:
            _dict['groups'] = [x.to_dict() for x in self.groups]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SearchResultProperties():
    """
    Schema for the result of a query search operation.

    :attr int total_rows: (optional) Number of total rows.
    :attr str bookmark: (optional) Opaque bookmark token used when paginating
          results.
    :attr str by: (optional) Grouped search matches.
    :attr dict counts: (optional) The counts facet syntax returns the number of
          query results for each unique value of each named field.
    :attr dict ranges: (optional) The range facet syntax reuses the standard Lucene
          syntax for ranges to return counts of results that fit into each specified
          category.
    :attr List[SearchResultRow] rows: (optional) Array of row objects.
    """

    def __init__(self,
                 *,
                 total_rows: int = None,
                 bookmark: str = None,
                 by: str = None,
                 counts: dict = None,
                 ranges: dict = None,
                 rows: List['SearchResultRow'] = None) -> None:
        """
        Initialize a SearchResultProperties object.

        :param int total_rows: (optional) Number of total rows.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param str by: (optional) Grouped search matches.
        :param dict counts: (optional) The counts facet syntax returns the number
               of query results for each unique value of each named field.
        :param dict ranges: (optional) The range facet syntax reuses the standard
               Lucene syntax for ranges to return counts of results that fit into each
               specified category.
        :param List[SearchResultRow] rows: (optional) Array of row objects.
        """
        self.total_rows = total_rows
        self.bookmark = bookmark
        self.by = by
        self.counts = counts
        self.ranges = ranges
        self.rows = rows

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchResultProperties':
        """Initialize a SearchResultProperties object from a json dictionary."""
        args = {}
        if 'total_rows' in _dict:
            args['total_rows'] = _dict.get('total_rows')
        if 'bookmark' in _dict:
            args['bookmark'] = _dict.get('bookmark')
        if 'by' in _dict:
            args['by'] = _dict.get('by')
        if 'counts' in _dict:
            args['counts'] = _dict.get('counts')
        if 'ranges' in _dict:
            args['ranges'] = _dict.get('ranges')
        if 'rows' in _dict:
            args['rows'] = [SearchResultRow.from_dict(x) for x in _dict.get('rows')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchResultProperties object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_rows') and self.total_rows is not None:
            _dict['total_rows'] = self.total_rows
        if hasattr(self, 'bookmark') and self.bookmark is not None:
            _dict['bookmark'] = self.bookmark
        if hasattr(self, 'by') and self.by is not None:
            _dict['by'] = self.by
        if hasattr(self, 'counts') and self.counts is not None:
            _dict['counts'] = self.counts
        if hasattr(self, 'ranges') and self.ranges is not None:
            _dict['ranges'] = self.ranges
        if hasattr(self, 'rows') and self.rows is not None:
            _dict['rows'] = [x.to_dict() for x in self.rows]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchResultProperties object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchResultProperties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchResultProperties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SearchResultRow():
    """
    Schema for a row of the result of a query search operation.

    :attr Document doc: (optional) Schema for a document.
    :attr dict fields: (optional) Schema for the fields returned by a query search
          operation, a map of field name to value.
    :attr dict highlights: (optional) Returns the context in which a search term was
          mentioned so that you can display more emphasized results to a user.
    :attr str id: (optional) Schema for a document ID.
    """

    def __init__(self,
                 *,
                 doc: 'Document' = None,
                 fields: dict = None,
                 highlights: dict = None,
                 id: str = None) -> None:
        """
        Initialize a SearchResultRow object.

        :param Document doc: (optional) Schema for a document.
        :param dict fields: (optional) Schema for the fields returned by a query
               search operation, a map of field name to value.
        :param dict highlights: (optional) Returns the context in which a search
               term was mentioned so that you can display more emphasized results to a
               user.
        :param str id: (optional) Schema for a document ID.
        """
        self.doc = doc
        self.fields = fields
        self.highlights = highlights
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchResultRow':
        """Initialize a SearchResultRow object from a json dictionary."""
        args = {}
        if 'doc' in _dict:
            args['doc'] = Document.from_dict(_dict.get('doc'))
        if 'fields' in _dict:
            args['fields'] = _dict.get('fields')
        if 'highlights' in _dict:
            args['highlights'] = _dict.get('highlights')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchResultRow object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'doc') and self.doc is not None:
            _dict['doc'] = self.doc.to_dict()
        if hasattr(self, 'fields') and self.fields is not None:
            _dict['fields'] = self.fields
        if hasattr(self, 'highlights') and self.highlights is not None:
            _dict['highlights'] = self.highlights
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchResultRow object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchResultRow') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchResultRow') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Security():
    """
    Schema for a security document.

    :attr SecurityObject admins: (optional) Schema for names and roles to map to a
          database permission.
    :attr SecurityObject members: (optional) Schema for names and roles to map to a
          database permission.
    :attr dict cloudant: (optional) Database permissions for Cloudant users and/or
          API keys.
    :attr bool couchdb_auth_only: (optional) Manage permissions using the `_users`
          database only.
    """

    def __init__(self,
                 *,
                 admins: 'SecurityObject' = None,
                 members: 'SecurityObject' = None,
                 cloudant: dict = None,
                 couchdb_auth_only: bool = None) -> None:
        """
        Initialize a Security object.

        :param SecurityObject admins: (optional) Schema for names and roles to map
               to a database permission.
        :param SecurityObject members: (optional) Schema for names and roles to map
               to a database permission.
        :param dict cloudant: (optional) Database permissions for Cloudant users
               and/or API keys.
        :param bool couchdb_auth_only: (optional) Manage permissions using the
               `_users` database only.
        """
        self.admins = admins
        self.members = members
        self.cloudant = cloudant
        self.couchdb_auth_only = couchdb_auth_only

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Security':
        """Initialize a Security object from a json dictionary."""
        args = {}
        if 'admins' in _dict:
            args['admins'] = SecurityObject.from_dict(_dict.get('admins'))
        if 'members' in _dict:
            args['members'] = SecurityObject.from_dict(_dict.get('members'))
        if 'cloudant' in _dict:
            args['cloudant'] = _dict.get('cloudant')
        if 'couchdb_auth_only' in _dict:
            args['couchdb_auth_only'] = _dict.get('couchdb_auth_only')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Security object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'admins') and self.admins is not None:
            _dict['admins'] = self.admins.to_dict()
        if hasattr(self, 'members') and self.members is not None:
            _dict['members'] = self.members.to_dict()
        if hasattr(self, 'cloudant') and self.cloudant is not None:
            _dict['cloudant'] = self.cloudant
        if hasattr(self, 'couchdb_auth_only') and self.couchdb_auth_only is not None:
            _dict['couchdb_auth_only'] = self.couchdb_auth_only
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Security object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Security') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Security') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class CloudantEnum(str, Enum):
        """
        Database permissions for Cloudant users and/or API keys.
        """
        READER = '_reader'
        WRITER = '_writer'
        ADMIN = '_admin'
        REPLICATOR = '_replicator'
        DB_UPDATES = '_db_updates'
        DESIGN = '_design'
        SHARDS = '_shards'
        SECURITY = '_security'


class SecurityObject():
    """
    Schema for names and roles to map to a database permission.

    :attr List[str] names: (optional) List of usernames.
    :attr List[str] roles: (optional) List of roles.
    """

    def __init__(self,
                 *,
                 names: List[str] = None,
                 roles: List[str] = None) -> None:
        """
        Initialize a SecurityObject object.

        :param List[str] names: (optional) List of usernames.
        :param List[str] roles: (optional) List of roles.
        """
        self.names = names
        self.roles = roles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecurityObject':
        """Initialize a SecurityObject object from a json dictionary."""
        args = {}
        if 'names' in _dict:
            args['names'] = _dict.get('names')
        if 'roles' in _dict:
            args['roles'] = _dict.get('roles')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecurityObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'names') and self.names is not None:
            _dict['names'] = self.names
        if hasattr(self, 'roles') and self.roles is not None:
            _dict['roles'] = self.roles
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SecurityObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecurityObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecurityObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ServerInformation():
    """
    Schema for information about the server instance.

    :attr str couchdb: (optional) Welcome message.
    :attr List[str] features: (optional) List of enabled optional features.
    :attr ServerVendor vendor: (optional) Schema for server vendor information.
    :attr str version: (optional) Apache CouchDB version.
    """

    def __init__(self,
                 *,
                 couchdb: str = None,
                 features: List[str] = None,
                 vendor: 'ServerVendor' = None,
                 version: str = None) -> None:
        """
        Initialize a ServerInformation object.

        :param str couchdb: (optional) Welcome message.
        :param List[str] features: (optional) List of enabled optional features.
        :param ServerVendor vendor: (optional) Schema for server vendor
               information.
        :param str version: (optional) Apache CouchDB version.
        """
        self.couchdb = couchdb
        self.features = features
        self.vendor = vendor
        self.version = version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServerInformation':
        """Initialize a ServerInformation object from a json dictionary."""
        args = {}
        if 'couchdb' in _dict:
            args['couchdb'] = _dict.get('couchdb')
        if 'features' in _dict:
            args['features'] = _dict.get('features')
        if 'vendor' in _dict:
            args['vendor'] = ServerVendor.from_dict(_dict.get('vendor'))
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServerInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'couchdb') and self.couchdb is not None:
            _dict['couchdb'] = self.couchdb
        if hasattr(self, 'features') and self.features is not None:
            _dict['features'] = self.features
        if hasattr(self, 'vendor') and self.vendor is not None:
            _dict['vendor'] = self.vendor.to_dict()
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServerInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServerInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServerInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ServerVendor():
    """
    Schema for server vendor information.

    :attr str name: (optional) Vendor name.
    :attr str variant: (optional) Vendor variant.
    :attr str version: (optional) Vendor version.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 variant: str = None,
                 version: str = None) -> None:
        """
        Initialize a ServerVendor object.

        :param str name: (optional) Vendor name.
        :param str variant: (optional) Vendor variant.
        :param str version: (optional) Vendor version.
        """
        self.name = name
        self.variant = variant
        self.version = version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServerVendor':
        """Initialize a ServerVendor object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'variant' in _dict:
            args['variant'] = _dict.get('variant')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServerVendor object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'variant') and self.variant is not None:
            _dict['variant'] = self.variant
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServerVendor object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServerVendor') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServerVendor') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SessionAuthentication():
    """
    Schema for session authentication information.

    :attr str authenticated: (optional) authenticated.
    :attr str authentication_db: (optional) authentication_db.
    :attr List[str] authentication_handlers: (optional) authentication_handlers.
    """

    def __init__(self,
                 *,
                 authenticated: str = None,
                 authentication_db: str = None,
                 authentication_handlers: List[str] = None) -> None:
        """
        Initialize a SessionAuthentication object.

        :param str authenticated: (optional) authenticated.
        :param str authentication_db: (optional) authentication_db.
        :param List[str] authentication_handlers: (optional)
               authentication_handlers.
        """
        self.authenticated = authenticated
        self.authentication_db = authentication_db
        self.authentication_handlers = authentication_handlers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SessionAuthentication':
        """Initialize a SessionAuthentication object from a json dictionary."""
        args = {}
        if 'authenticated' in _dict:
            args['authenticated'] = _dict.get('authenticated')
        if 'authentication_db' in _dict:
            args['authentication_db'] = _dict.get('authentication_db')
        if 'authentication_handlers' in _dict:
            args['authentication_handlers'] = _dict.get('authentication_handlers')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SessionAuthentication object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'authenticated') and self.authenticated is not None:
            _dict['authenticated'] = self.authenticated
        if hasattr(self, 'authentication_db') and self.authentication_db is not None:
            _dict['authentication_db'] = self.authentication_db
        if hasattr(self, 'authentication_handlers') and self.authentication_handlers is not None:
            _dict['authentication_handlers'] = self.authentication_handlers
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SessionAuthentication object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SessionAuthentication') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SessionAuthentication') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SessionInformation():
    """
    Schema for information about a session.

    :attr bool ok: (optional) ok.
    :attr SessionAuthentication info: (optional) Schema for session authentication
          information.
    :attr UserContext user_ctx: (optional) Schema for the user context of a session.
    """

    def __init__(self,
                 *,
                 ok: bool = None,
                 info: 'SessionAuthentication' = None,
                 user_ctx: 'UserContext' = None) -> None:
        """
        Initialize a SessionInformation object.

        :param bool ok: (optional) ok.
        :param SessionAuthentication info: (optional) Schema for session
               authentication information.
        :param UserContext user_ctx: (optional) Schema for the user context of a
               session.
        """
        self.ok = ok
        self.info = info
        self.user_ctx = user_ctx

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SessionInformation':
        """Initialize a SessionInformation object from a json dictionary."""
        args = {}
        if 'ok' in _dict:
            args['ok'] = _dict.get('ok')
        if 'info' in _dict:
            args['info'] = SessionAuthentication.from_dict(_dict.get('info'))
        if 'userCtx' in _dict:
            args['user_ctx'] = UserContext.from_dict(_dict.get('userCtx'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SessionInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ok') and self.ok is not None:
            _dict['ok'] = self.ok
        if hasattr(self, 'info') and self.info is not None:
            _dict['info'] = self.info.to_dict()
        if hasattr(self, 'user_ctx') and self.user_ctx is not None:
            _dict['userCtx'] = self.user_ctx.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SessionInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SessionInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SessionInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ShardsInformation():
    """
    Schema for a shards object that maps the hash value range for each shard to the array
    of nodes that contain a copy of that shard.

    :attr dict shards: (optional) Mapping of shard hash value range to a list of
          nodes.
    """

    def __init__(self,
                 *,
                 shards: dict = None) -> None:
        """
        Initialize a ShardsInformation object.

        :param dict shards: (optional) Mapping of shard hash value range to a list
               of nodes.
        """
        self.shards = shards

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ShardsInformation':
        """Initialize a ShardsInformation object from a json dictionary."""
        args = {}
        if 'shards' in _dict:
            args['shards'] = _dict.get('shards')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ShardsInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'shards') and self.shards is not None:
            _dict['shards'] = self.shards
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ShardsInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ShardsInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ShardsInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class UpInformation():
    """
    Schema for information about the up state of the server.

    :attr str status: (optional) status.
    """

    def __init__(self,
                 *,
                 status: str = None) -> None:
        """
        Initialize a UpInformation object.

        :param str status: (optional) status.
        """
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpInformation':
        """Initialize a UpInformation object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UpInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UpInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        status.
        """
        MAINTENANCE_MODE = 'maintenance_mode'
        NOLB = 'nolb'
        OK = 'ok'


class UserContext():
    """
    Schema for the user context of a session.

    :attr str db: (optional) Database name in the context of the provided operation.
    :attr str name: (optional) User name.
    :attr List[str] roles: (optional) List of user roles.
    """

    def __init__(self,
                 *,
                 db: str = None,
                 name: str = None,
                 roles: List[str] = None) -> None:
        """
        Initialize a UserContext object.

        :param str db: (optional) Database name in the context of the provided
               operation.
        :param str name: (optional) User name.
        :param List[str] roles: (optional) List of user roles.
        """
        self.db = db
        self.name = name
        self.roles = roles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UserContext':
        """Initialize a UserContext object from a json dictionary."""
        args = {}
        if 'db' in _dict:
            args['db'] = _dict.get('db')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'roles' in _dict:
            args['roles'] = _dict.get('roles')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UserContext object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'db') and self.db is not None:
            _dict['db'] = self.db
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'roles') and self.roles is not None:
            _dict['roles'] = self.roles
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UserContext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UserContext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UserContext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class RolesEnum(str, Enum):
        """
        Schema for a security role.
        """
        READER = '_reader'
        WRITER = '_writer'
        ADMIN = '_admin'
        REPLICATOR = '_replicator'
        DB_UPDATES = '_db_updates'
        DESIGN = '_design'
        SHARDS = '_shards'
        SECURITY = '_security'


class UuidsResult():
    """
    Schema for a set of uuids generated by the server.

    :attr List[str] uuids: (optional) uuids.
    """

    def __init__(self,
                 *,
                 uuids: List[str] = None) -> None:
        """
        Initialize a UuidsResult object.

        :param List[str] uuids: (optional) uuids.
        """
        self.uuids = uuids

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UuidsResult':
        """Initialize a UuidsResult object from a json dictionary."""
        args = {}
        if 'uuids' in _dict:
            args['uuids'] = _dict.get('uuids')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UuidsResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'uuids') and self.uuids is not None:
            _dict['uuids'] = self.uuids
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UuidsResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UuidsResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UuidsResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ViewQueriesResult():
    """
    Schema for the results of a queries view operation.

    :attr List[ViewResult] results: An array of result objects - one for each query.
          Each result object contains the same fields as the response to a regular view
          request.
    """

    def __init__(self,
                 results: List['ViewResult']) -> None:
        """
        Initialize a ViewQueriesResult object.

        :param List[ViewResult] results: An array of result objects - one for each
               query. Each result object contains the same fields as the response to a
               regular view request.
        """
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ViewQueriesResult':
        """Initialize a ViewQueriesResult object from a json dictionary."""
        args = {}
        if 'results' in _dict:
            args['results'] = [ViewResult.from_dict(x) for x in _dict.get('results')]
        else:
            raise ValueError('Required property \'results\' not present in ViewQueriesResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ViewQueriesResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x.to_dict() for x in self.results]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ViewQueriesResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ViewQueriesResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ViewQueriesResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ViewQuery():
    """
    Schema for a query view operation.

    :attr bool att_encoding_info: (optional) Parameter to specify whether to include
          the encoding information in attachment stubs if the particular attachment is
          compressed.
    :attr bool attachments: (optional) Parameter to specify whether to include
          attachments bodies in a response.
    :attr bool conflicts: (optional) Parameter to specify whether to include a list
          of conflicted revisions in the `_conflicts` property of the returned document.
          Ignored if `include_docs` isn't `true`.
    :attr bool descending: (optional) Parameter to specify whether to return the
          documents in descending by key order.
    :attr bool include_docs: (optional) Parameter to specify whether to include the
          full content of the documents in the response.
    :attr bool inclusive_end: (optional) Parameter to specify whether the specified
          end key should be included in the result.
    :attr int limit: (optional) Parameter to specify the number of returned
          documents to limit the result to.
    :attr int skip: (optional) Parameter to specify the number of records before
          starting to return the results.
    :attr bool update_seq: (optional) Parameter to specify whether to include in the
          response an update_seq value indicating the sequence id of the database the view
          reflects.
    :attr object endkey: (optional) Schema for any JSON type.
    :attr str endkey_docid: (optional) Schema for a document ID.
    :attr bool group: (optional) Parameter to specify whether to group the results
          using the reduce function to a group rather than a single row. Implies reduce is
          true and the maximum group_level.
    :attr int group_level: (optional) Parameter to specify the group level to be
          used. Implies group is true.
    :attr object key: (optional) Schema for any JSON type.
    :attr List[object] keys: (optional) Parameter to specify to return only
          documents that match the specified keys. String representation of a JSON array
          containing elements that match the key type emitted by the view function.
    :attr bool reduce: (optional) Parameter to specify whether to use the reduce
          function in a map-reduce view. Default is true when a reduce function is
          defined.
    :attr bool stable: (optional) Parameter to specify whether view results should
          be returned from a stable set of shards.
    :attr object startkey: (optional) Schema for any JSON type.
    :attr str startkey_docid: (optional) Schema for a document ID.
    :attr str update: (optional) Parameter to specify whether or not the view in
          question should be updated prior to responding to the user.
    """

    def __init__(self,
                 *,
                 att_encoding_info: bool = None,
                 attachments: bool = None,
                 conflicts: bool = None,
                 descending: bool = None,
                 include_docs: bool = None,
                 inclusive_end: bool = None,
                 limit: int = None,
                 skip: int = None,
                 update_seq: bool = None,
                 endkey: object = None,
                 endkey_docid: str = None,
                 group: bool = None,
                 group_level: int = None,
                 key: object = None,
                 keys: List[object] = None,
                 reduce: bool = None,
                 stable: bool = None,
                 startkey: object = None,
                 startkey_docid: str = None,
                 update: str = None) -> None:
        """
        Initialize a ViewQuery object.

        :param bool att_encoding_info: (optional) Parameter to specify whether to
               include the encoding information in attachment stubs if the particular
               attachment is compressed.
        :param bool attachments: (optional) Parameter to specify whether to include
               attachments bodies in a response.
        :param bool conflicts: (optional) Parameter to specify whether to include a
               list of conflicted revisions in the `_conflicts` property of the returned
               document. Ignored if `include_docs` isn't `true`.
        :param bool descending: (optional) Parameter to specify whether to return
               the documents in descending by key order.
        :param bool include_docs: (optional) Parameter to specify whether to
               include the full content of the documents in the response.
        :param bool inclusive_end: (optional) Parameter to specify whether the
               specified end key should be included in the result.
        :param int limit: (optional) Parameter to specify the number of returned
               documents to limit the result to.
        :param int skip: (optional) Parameter to specify the number of records
               before starting to return the results.
        :param bool update_seq: (optional) Parameter to specify whether to include
               in the response an update_seq value indicating the sequence id of the
               database the view reflects.
        :param object endkey: (optional) Schema for any JSON type.
        :param str endkey_docid: (optional) Schema for a document ID.
        :param bool group: (optional) Parameter to specify whether to group the
               results using the reduce function to a group rather than a single row.
               Implies reduce is true and the maximum group_level.
        :param int group_level: (optional) Parameter to specify the group level to
               be used. Implies group is true.
        :param object key: (optional) Schema for any JSON type.
        :param List[object] keys: (optional) Parameter to specify to return only
               documents that match the specified keys. String representation of a JSON
               array containing elements that match the key type emitted by the view
               function.
        :param bool reduce: (optional) Parameter to specify whether to use the
               reduce function in a map-reduce view. Default is true when a reduce
               function is defined.
        :param bool stable: (optional) Parameter to specify whether view results
               should be returned from a stable set of shards.
        :param object startkey: (optional) Schema for any JSON type.
        :param str startkey_docid: (optional) Schema for a document ID.
        :param str update: (optional) Parameter to specify whether or not the view
               in question should be updated prior to responding to the user.
        """
        self.att_encoding_info = att_encoding_info
        self.attachments = attachments
        self.conflicts = conflicts
        self.descending = descending
        self.include_docs = include_docs
        self.inclusive_end = inclusive_end
        self.limit = limit
        self.skip = skip
        self.update_seq = update_seq
        self.endkey = endkey
        self.endkey_docid = endkey_docid
        self.group = group
        self.group_level = group_level
        self.key = key
        self.keys = keys
        self.reduce = reduce
        self.stable = stable
        self.startkey = startkey
        self.startkey_docid = startkey_docid
        self.update = update

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ViewQuery':
        """Initialize a ViewQuery object from a json dictionary."""
        args = {}
        if 'att_encoding_info' in _dict:
            args['att_encoding_info'] = _dict.get('att_encoding_info')
        if 'attachments' in _dict:
            args['attachments'] = _dict.get('attachments')
        if 'conflicts' in _dict:
            args['conflicts'] = _dict.get('conflicts')
        if 'descending' in _dict:
            args['descending'] = _dict.get('descending')
        if 'include_docs' in _dict:
            args['include_docs'] = _dict.get('include_docs')
        if 'inclusive_end' in _dict:
            args['inclusive_end'] = _dict.get('inclusive_end')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'skip' in _dict:
            args['skip'] = _dict.get('skip')
        if 'update_seq' in _dict:
            args['update_seq'] = _dict.get('update_seq')
        if 'endkey' in _dict:
            args['endkey'] = _dict.get('endkey')
        if 'endkey_docid' in _dict:
            args['endkey_docid'] = _dict.get('endkey_docid')
        if 'group' in _dict:
            args['group'] = _dict.get('group')
        if 'group_level' in _dict:
            args['group_level'] = _dict.get('group_level')
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        if 'keys' in _dict:
            args['keys'] = _dict.get('keys')
        if 'reduce' in _dict:
            args['reduce'] = _dict.get('reduce')
        if 'stable' in _dict:
            args['stable'] = _dict.get('stable')
        if 'startkey' in _dict:
            args['startkey'] = _dict.get('startkey')
        if 'startkey_docid' in _dict:
            args['startkey_docid'] = _dict.get('startkey_docid')
        if 'update' in _dict:
            args['update'] = _dict.get('update')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ViewQuery object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'att_encoding_info') and self.att_encoding_info is not None:
            _dict['att_encoding_info'] = self.att_encoding_info
        if hasattr(self, 'attachments') and self.attachments is not None:
            _dict['attachments'] = self.attachments
        if hasattr(self, 'conflicts') and self.conflicts is not None:
            _dict['conflicts'] = self.conflicts
        if hasattr(self, 'descending') and self.descending is not None:
            _dict['descending'] = self.descending
        if hasattr(self, 'include_docs') and self.include_docs is not None:
            _dict['include_docs'] = self.include_docs
        if hasattr(self, 'inclusive_end') and self.inclusive_end is not None:
            _dict['inclusive_end'] = self.inclusive_end
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'skip') and self.skip is not None:
            _dict['skip'] = self.skip
        if hasattr(self, 'update_seq') and self.update_seq is not None:
            _dict['update_seq'] = self.update_seq
        if hasattr(self, 'endkey') and self.endkey is not None:
            _dict['endkey'] = self.endkey
        if hasattr(self, 'endkey_docid') and self.endkey_docid is not None:
            _dict['endkey_docid'] = self.endkey_docid
        if hasattr(self, 'group') and self.group is not None:
            _dict['group'] = self.group
        if hasattr(self, 'group_level') and self.group_level is not None:
            _dict['group_level'] = self.group_level
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self, 'keys') and self.keys is not None:
            _dict['keys'] = self.keys
        if hasattr(self, 'reduce') and self.reduce is not None:
            _dict['reduce'] = self.reduce
        if hasattr(self, 'stable') and self.stable is not None:
            _dict['stable'] = self.stable
        if hasattr(self, 'startkey') and self.startkey is not None:
            _dict['startkey'] = self.startkey
        if hasattr(self, 'startkey_docid') and self.startkey_docid is not None:
            _dict['startkey_docid'] = self.startkey_docid
        if hasattr(self, 'update') and self.update is not None:
            _dict['update'] = self.update
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ViewQuery object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ViewQuery') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ViewQuery') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class UpdateEnum(str, Enum):
        """
        Parameter to specify whether or not the view in question should be updated prior
        to responding to the user.
        """
        TRUE = 'true'
        FALSE = 'false'
        LAZY = 'lazy'


class ViewResult():
    """
    Schema for the result of a query view operation.

    :attr int total_rows: (optional) Number of total rows.
    :attr str update_seq: (optional) Current update sequence for the database.
    :attr List[ViewResultRow] rows: (optional) rows.
    """

    def __init__(self,
                 *,
                 total_rows: int = None,
                 update_seq: str = None,
                 rows: List['ViewResultRow'] = None) -> None:
        """
        Initialize a ViewResult object.

        :param int total_rows: (optional) Number of total rows.
        :param str update_seq: (optional) Current update sequence for the database.
        :param List[ViewResultRow] rows: (optional) rows.
        """
        self.total_rows = total_rows
        self.update_seq = update_seq
        self.rows = rows

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ViewResult':
        """Initialize a ViewResult object from a json dictionary."""
        args = {}
        if 'total_rows' in _dict:
            args['total_rows'] = _dict.get('total_rows')
        if 'update_seq' in _dict:
            args['update_seq'] = _dict.get('update_seq')
        if 'rows' in _dict:
            args['rows'] = [ViewResultRow.from_dict(x) for x in _dict.get('rows')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ViewResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_rows') and self.total_rows is not None:
            _dict['total_rows'] = self.total_rows
        if hasattr(self, 'update_seq') and self.update_seq is not None:
            _dict['update_seq'] = self.update_seq
        if hasattr(self, 'rows') and self.rows is not None:
            _dict['rows'] = [x.to_dict() for x in self.rows]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ViewResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ViewResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ViewResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ViewResultRow():
    """
    Schema for a row of a view result.

    :attr str caused_by: (optional) The cause of the error (if available).
    :attr str error: (optional) The name of the error.
    :attr str reason: (optional) The reason the error occurred (if available).
    :attr str id: (optional) Schema for a document ID.
    :attr object key: (optional) Schema for any JSON type.
    :attr object value: (optional) Schema for any JSON type.
    """

    def __init__(self,
                 *,
                 caused_by: str = None,
                 error: str = None,
                 reason: str = None,
                 id: str = None,
                 key: object = None,
                 value: object = None) -> None:
        """
        Initialize a ViewResultRow object.

        :param str caused_by: (optional) The cause of the error (if available).
        :param str error: (optional) The name of the error.
        :param str reason: (optional) The reason the error occurred (if available).
        :param str id: (optional) Schema for a document ID.
        :param object key: (optional) Schema for any JSON type.
        :param object value: (optional) Schema for any JSON type.
        """
        self.caused_by = caused_by
        self.error = error
        self.reason = reason
        self.id = id
        self.key = key
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ViewResultRow':
        """Initialize a ViewResultRow object from a json dictionary."""
        args = {}
        if 'caused_by' in _dict:
            args['caused_by'] = _dict.get('caused_by')
        if 'error' in _dict:
            args['error'] = _dict.get('error')
        if 'reason' in _dict:
            args['reason'] = _dict.get('reason')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ViewResultRow object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'caused_by') and self.caused_by is not None:
            _dict['caused_by'] = self.caused_by
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error
        if hasattr(self, 'reason') and self.reason is not None:
            _dict['reason'] = self.reason
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ViewResultRow object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ViewResultRow') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ViewResultRow') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GeoJsonGeometry(GeoJsonGeometryObject):
    """
    Schema for a GeoJSON geometry.

    :attr str type: The type of GeoJSON Geometry.
    :attr List[object] coordinates: Used for all geometry types except
          `GeometryCollection`. The structure of the elements in the array varies by
          geometry type.
    """

    def __init__(self,
                 type: str,
                 coordinates: List[object]) -> None:
        """
        Initialize a GeoJsonGeometry object.

        :param str type: The type of GeoJSON Geometry.
        :param List[object] coordinates: Used for all geometry types except
               `GeometryCollection`. The structure of the elements in the array varies by
               geometry type.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.coordinates = coordinates

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GeoJsonGeometry':
        """Initialize a GeoJsonGeometry object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in GeoJsonGeometry JSON')
        if 'coordinates' in _dict:
            args['coordinates'] = _dict.get('coordinates')
        else:
            raise ValueError('Required property \'coordinates\' not present in GeoJsonGeometry JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GeoJsonGeometry object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'coordinates') and self.coordinates is not None:
            _dict['coordinates'] = self.coordinates
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GeoJsonGeometry object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GeoJsonGeometry') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GeoJsonGeometry') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of GeoJSON Geometry.
        """
        POINT = 'Point'
        MULTIPOINT = 'MultiPoint'
        LINESTRING = 'LineString'
        MULTILINESTRING = 'MultiLineString'
        POLYGON = 'Polygon'
        MULTIPOLYGON = 'MultiPolygon'
        GEOMETRYCOLLECTION = 'GeometryCollection'


class GeoJsonGeometryCollection(GeoJsonGeometryObject):
    """
    Schema for a GeoJSON GeometryCollection type geometry.

    :attr str type: The type of GeoJSON Geometry.
    :attr List[GeoJsonGeometry] geometries: Used for the `GeometryCollection` type.
    """

    def __init__(self,
                 type: str,
                 geometries: List['GeoJsonGeometry']) -> None:
        """
        Initialize a GeoJsonGeometryCollection object.

        :param str type: The type of GeoJSON Geometry.
        :param List[GeoJsonGeometry] geometries: Used for the `GeometryCollection`
               type.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.geometries = geometries

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GeoJsonGeometryCollection':
        """Initialize a GeoJsonGeometryCollection object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in GeoJsonGeometryCollection JSON')
        if 'geometries' in _dict:
            args['geometries'] = [GeoJsonGeometry.from_dict(x) for x in _dict.get('geometries')]
        else:
            raise ValueError('Required property \'geometries\' not present in GeoJsonGeometryCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GeoJsonGeometryCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'geometries') and self.geometries is not None:
            _dict['geometries'] = [x.to_dict() for x in self.geometries]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GeoJsonGeometryCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GeoJsonGeometryCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GeoJsonGeometryCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of GeoJSON Geometry.
        """
        POINT = 'Point'
        MULTIPOINT = 'MultiPoint'
        LINESTRING = 'LineString'
        MULTILINESTRING = 'MultiLineString'
        POLYGON = 'Polygon'
        MULTIPOLYGON = 'MultiPolygon'
        GEOMETRYCOLLECTION = 'GeometryCollection'

