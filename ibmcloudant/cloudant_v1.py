# coding: utf-8

# (C) Copyright IBM Corp. 2025.
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
NoSQL database based on Apache CouchDB

See: https://cloud.ibm.com/docs/services/Cloudant/
"""

from datetime import datetime
from enum import Enum
from typing import BinaryIO, Dict, List, Optional, Union
import base64
import json
import logging

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

    DEFAULT_SERVICE_URL = 'https://~replace-with-cloudant-host~.cloudantnosqldb.appdomain.cloud'
    DEFAULT_SERVICE_NAME = 'cloudant'

    @classmethod
    def new_instance(
        cls,
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

    def __init__(
        self,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the Cloudant service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)
        # enable gzip compression of request bodies
        self.set_enable_gzip_compression(True)

    #########################
    # Server
    #########################

    def get_server_information(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve server instance information.

        When you access the root of an instance, IBM Cloudant returns meta-information
        about the instance. The response includes a JSON structure that contains
        information about the server, including a welcome message and the server's
        version.
        **Tip:**  The authentication for this endpoint is only enforced when using IAM.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServerInformation` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_server_information',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_capacity_throughput_information(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve provisioned throughput capacity information.

        View the amount of provisioned throughput capacity that is allocated to an IBM
        Cloudant instance and what is the target provisioned throughput capacity.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CapacityThroughputInformation` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_capacity_throughput_information',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_api/v2/user/capacity/throughput'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def put_capacity_throughput_configuration(
        self,
        blocks: int,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update the target provisioned throughput capacity.

        Sets the target provisioned throughput capacity for an IBM Cloudant instance. When
        target capacity is changed, the current capacity asynchronously changes to meet
        the target capacity.

        :param int blocks: A number of blocks of throughput units. A block consists
               of 100 reads/sec, 50 writes/sec, and 5 global queries/sec of provisioned
               throughput capacity. Not available for some plans.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CapacityThroughputInformation` object
        """

        if blocks is None:
            raise ValueError('blocks must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='put_capacity_throughput_configuration',
        )
        headers.update(sdk_headers)

        data = {
            'blocks': blocks,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_api/v2/user/capacity/throughput'
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_uuids(
        self,
        *,
        count: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve one or more UUIDs.

        Requests one or more Universally Unique Identifiers (UUIDs) from the instance. The
        response is a JSON object that provides a list of UUIDs.
        **Tip:**  The authentication for this endpoint is only enforced when using IAM.

        :param int count: (optional) Query parameter to specify the number of UUIDs
               to return.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UuidsResult` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_uuids',
        )
        headers.update(sdk_headers)

        params = {
            'count': count,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_uuids'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Databases
    #########################

    def get_db_updates(
        self,
        *,
        descending: Optional[bool] = None,
        feed: Optional[str] = None,
        heartbeat: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        since: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve change events for all databases.

        **This endpoint is not available in IBM Cloudant.**
        Lists changes to databases, like a global changes feed. Types of changes include
        updating the database and creating or deleting a database. Like the changes feed,
        the feed is not guaranteed to return changes in the correct order and might repeat
        changes. Polling modes for this method work like polling modes for the changes
        feed.

        :param bool descending: (optional) Query parameter to specify whether to
               return the documents in descending by key order.
        :param str feed: (optional) Query parameter to specify the changes feed
               type.
        :param int heartbeat: (optional) Query parameter to specify the period in
               milliseconds after which an empty line is sent in the results. Off by
               default and only applicable for
               `continuous` and `eventsource` feeds. Overrides any timeout to keep the
               feed alive indefinitely. May also be `true` to use a value of `60000`.
               **Note:** Delivery of heartbeats cannot be relied on at specific intervals.
               If your application runs in an environment where idle network connections
               may break, `heartbeat` is not suitable as a keepalive mechanism. Instead,
               consider one of the following options:
                 * Use the `timeout` parameter with a value that is compatible with your
               network environment.
                 * Switch to scheduled usage of one of the non-continuous changes feed
               types
                   (`normal` or `longpoll`).
                 * Use TCP keepalive.
        :param int limit: (optional) Query parameter to specify the number of
               returned documents to limit the result to.
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

        Deprecated: this method is deprecated and may be removed in a future release.
        """

        logging.warning('A deprecated operation has been invoked: get_db_updates')

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_db_updates',
        )
        headers.update(sdk_headers)

        params = {
            'descending': descending,
            'feed': feed,
            'heartbeat': heartbeat,
            'limit': limit,
            'timeout': timeout,
            'since': since,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_db_updates'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def post_changes(
        self,
        db: str,
        *,
        doc_ids: Optional[List[str]] = None,
        fields: Optional[List[str]] = None,
        selector: Optional[dict] = None,
        last_event_id: Optional[str] = None,
        att_encoding_info: Optional[bool] = None,
        attachments: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        descending: Optional[bool] = None,
        feed: Optional[str] = None,
        filter: Optional[str] = None,
        heartbeat: Optional[int] = None,
        include_docs: Optional[bool] = None,
        limit: Optional[int] = None,
        seq_interval: Optional[int] = None,
        since: Optional[str] = None,
        style: Optional[str] = None,
        timeout: Optional[int] = None,
        view: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Query the database document changes feed.

        Requests the database changes feed in the same way as `GET /{db}/_changes` does.
        It is widely used with the `filter` query parameter because it allows one to pass
        more information to the filter.
        ### Note
        Before using the changes feed read the
        [FAQs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-faq-using-changes-feed)
        to understand the limitations and appropriate use cases.
        If you need to pass parameters to dynamically change the filtered content use the
        `_selector` filter type for better performance and compatibility. The SDKs have
        full support for change requests using selector filters, but don't support passing
        parameters to design document filters.

        :param str db: Path parameter to specify the database name.
        :param List[str] doc_ids: (optional) Schema for a list of document IDs.
        :param List[str] fields: (optional) JSON array that uses the field syntax.
               Use this parameter to specify which fields of a document must be returned.
               If it is omitted or empty, the entire document is returned.
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
               are used to combine selectors. A combination operator takes a single
               argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
               It is important for query performance to use appropriate selectors:
               * Only equality operators such as `$eq`, `$gt`, `$gte`, `$lt`, and `$lte`
               (but not `$ne`) can be used as the basis of a query. You should include at
               least one of these in a selector.
               * Some operators such as `$not`, `$or`, `$in`, and `$regex` cannot be
               answered from an index. For query selectors use these operators in
               conjunction with equality operators or create and use a partial index to
               reduce the number of documents that will need to be scanned.
               See [the Cloudant
               Docs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-operators)for a
               list of all available combination and conditional operators.
               For further reference see [selector
               syntax](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-selector-syntax).
        :param str last_event_id: (optional) Header parameter to specify the ID of
               the last events received by the server on a previous connection. Overrides
               `since` query parameter.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool conflicts: (optional) Query parameter to specify whether to
               include a list of conflicted revisions in each returned document. Active
               only when `include_docs` is `true`.
        :param bool descending: (optional) Query parameter to specify whether to
               return the documents in descending by key order.
        :param str feed: (optional) Query parameter to specify the changes feed
               type.
        :param str filter: (optional) Query parameter to specify a filter to emit
               only specific events from the changes stream.
               The built-in filter types are:
                 * `_design` - Returns only changes to design documents.
                 * `_doc_ids` - Returns changes for documents with an ID matching one
               specified in
                     `doc_ids` request body parameter. (`POST` only)
                 * `_selector` - Returns changes for documents that match the `selector`
                     request body parameter. The selector syntax is the same as used for
                     `_find`. (`POST` only)
                 * `_view` - Returns changes for documents that match an existing map
                     function in the view specified by the query parameter `view`.
               Additionally, the value can be the name of a JS filter function from a
               design document. For example: `design_doc/filtername`.
               **Note:** For better performance use the built-in `_selector`, `_design` or
               `_doc_ids` filters rather than JS based `_view` or design document filters.
               If you need to pass values to change the filtered content use the
               `_selector` filter type.
        :param int heartbeat: (optional) Query parameter to specify the period in
               milliseconds after which an empty line is sent in the results. Off by
               default and only applicable for
               `continuous` and `eventsource` feeds. Overrides any timeout to keep the
               feed alive indefinitely. May also be `true` to use a value of `60000`.
               **Note:** Delivery of heartbeats cannot be relied on at specific intervals.
               If your application runs in an environment where idle network connections
               may break, `heartbeat` is not suitable as a keepalive mechanism. Instead,
               consider one of the following options:
                 * Use the `timeout` parameter with a value that is compatible with your
               network environment.
                 * Switch to scheduled usage of one of the non-continuous changes feed
               types
                   (`normal` or `longpoll`).
                 * Use TCP keepalive.
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

        if not db:
            raise ValueError('db must be provided')
        headers = {
            'Last-Event-ID': last_event_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_changes',
        )
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
            'view': view,
        }

        data = {
            'doc_ids': doc_ids,
            'fields': fields,
            'selector': selector,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_changes'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_changes_as_stream(
        self,
        db: str,
        *,
        doc_ids: Optional[List[str]] = None,
        fields: Optional[List[str]] = None,
        selector: Optional[dict] = None,
        last_event_id: Optional[str] = None,
        att_encoding_info: Optional[bool] = None,
        attachments: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        descending: Optional[bool] = None,
        feed: Optional[str] = None,
        filter: Optional[str] = None,
        heartbeat: Optional[int] = None,
        include_docs: Optional[bool] = None,
        limit: Optional[int] = None,
        seq_interval: Optional[int] = None,
        since: Optional[str] = None,
        style: Optional[str] = None,
        timeout: Optional[int] = None,
        view: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Query the database document changes feed as stream.

        Requests the database changes feed in the same way as `GET /{db}/_changes` does.
        It is widely used with the `filter` query parameter because it allows one to pass
        more information to the filter.
        ### Note
        Before using the changes feed read the
        [FAQs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-faq-using-changes-feed)
        to understand the limitations and appropriate use cases.
        If you need to pass parameters to dynamically change the filtered content use the
        `_selector` filter type for better performance and compatibility. The SDKs have
        full support for change requests using selector filters, but don't support passing
        parameters to design document filters.

        :param str db: Path parameter to specify the database name.
        :param List[str] doc_ids: (optional) Schema for a list of document IDs.
        :param List[str] fields: (optional) JSON array that uses the field syntax.
               Use this parameter to specify which fields of a document must be returned.
               If it is omitted or empty, the entire document is returned.
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
               are used to combine selectors. A combination operator takes a single
               argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
               It is important for query performance to use appropriate selectors:
               * Only equality operators such as `$eq`, `$gt`, `$gte`, `$lt`, and `$lte`
               (but not `$ne`) can be used as the basis of a query. You should include at
               least one of these in a selector.
               * Some operators such as `$not`, `$or`, `$in`, and `$regex` cannot be
               answered from an index. For query selectors use these operators in
               conjunction with equality operators or create and use a partial index to
               reduce the number of documents that will need to be scanned.
               See [the Cloudant
               Docs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-operators)for a
               list of all available combination and conditional operators.
               For further reference see [selector
               syntax](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-selector-syntax).
        :param str last_event_id: (optional) Header parameter to specify the ID of
               the last events received by the server on a previous connection. Overrides
               `since` query parameter.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool conflicts: (optional) Query parameter to specify whether to
               include a list of conflicted revisions in each returned document. Active
               only when `include_docs` is `true`.
        :param bool descending: (optional) Query parameter to specify whether to
               return the documents in descending by key order.
        :param str feed: (optional) Query parameter to specify the changes feed
               type.
        :param str filter: (optional) Query parameter to specify a filter to emit
               only specific events from the changes stream.
               The built-in filter types are:
                 * `_design` - Returns only changes to design documents.
                 * `_doc_ids` - Returns changes for documents with an ID matching one
               specified in
                     `doc_ids` request body parameter. (`POST` only)
                 * `_selector` - Returns changes for documents that match the `selector`
                     request body parameter. The selector syntax is the same as used for
                     `_find`. (`POST` only)
                 * `_view` - Returns changes for documents that match an existing map
                     function in the view specified by the query parameter `view`.
               Additionally, the value can be the name of a JS filter function from a
               design document. For example: `design_doc/filtername`.
               **Note:** For better performance use the built-in `_selector`, `_design` or
               `_doc_ids` filters rather than JS based `_view` or design document filters.
               If you need to pass values to change the filtered content use the
               `_selector` filter type.
        :param int heartbeat: (optional) Query parameter to specify the period in
               milliseconds after which an empty line is sent in the results. Off by
               default and only applicable for
               `continuous` and `eventsource` feeds. Overrides any timeout to keep the
               feed alive indefinitely. May also be `true` to use a value of `60000`.
               **Note:** Delivery of heartbeats cannot be relied on at specific intervals.
               If your application runs in an environment where idle network connections
               may break, `heartbeat` is not suitable as a keepalive mechanism. Instead,
               consider one of the following options:
                 * Use the `timeout` parameter with a value that is compatible with your
               network environment.
                 * Switch to scheduled usage of one of the non-continuous changes feed
               types
                   (`normal` or `longpoll`).
                 * Use TCP keepalive.
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

        if not db:
            raise ValueError('db must be provided')
        headers = {
            'Last-Event-ID': last_event_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_changes_as_stream',
        )
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
            'view': view,
        }

        data = {
            'doc_ids': doc_ids,
            'fields': fields,
            'selector': selector,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_changes'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, stream=True, **kwargs)
        return response

    #########################
    # Databases
    #########################

    def head_database(
        self,
        db: str,
        **kwargs,
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

        if not db:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='head_database',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}'.format(**path_param_dict)
        request = self.prepare_request(
            method='HEAD',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_all_dbs(
        self,
        *,
        descending: Optional[bool] = None,
        end_key: Optional[str] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        start_key: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Query a list of all database names in the instance.

        Query to retrieve a list of database names from the instance.

        :param bool descending: (optional) Query parameter to specify whether to
               return the documents in descending by key order.
        :param str end_key: (optional) Query parameter to specify to stop returning
               records when the specified key is reached. String representation of any
               JSON type that matches the key type emitted by the view function.
        :param int limit: (optional) Query parameter to specify the number of
               returned documents to limit the result to.
        :param int skip: (optional) Query parameter to specify the number of
               records before starting to return the results.
        :param str start_key: (optional) Query parameter to specify to start
               returning records from the specified key. String representation of any JSON
               type that matches the key type emitted by the view function.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[str]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_all_dbs',
        )
        headers.update(sdk_headers)

        params = {
            'descending': descending,
            'end_key': end_key,
            'limit': limit,
            'skip': skip,
            'start_key': start_key,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_all_dbs'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def post_dbs_info(
        self,
        keys: List[str],
        **kwargs,
    ) -> DetailedResponse:
        """
        Query information about multiple databases.

        This operation enables you to request information about multiple databases in a
        single request, instead of issuing multiple `GET /{db}` requests. It returns a
        list that contains an information object for each database specified in the
        request.

        :param List[str] keys: A list of database names.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[DbsInfoResult]` result
        """

        if keys is None:
            raise ValueError('keys must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_dbs_info',
        )
        headers.update(sdk_headers)

        data = {
            'keys': keys,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_dbs_info'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_database(
        self,
        db: str,
        **kwargs,
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

        if not db:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_database',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_database_information(
        self,
        db: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve information about a database.

        Retrieve detailed information about the database.

        :param str db: Path parameter to specify the database name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DatabaseInformation` object
        """

        if not db:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_database_information',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def put_database(
        self,
        db: str,
        *,
        partitioned: Optional[bool] = None,
        q: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a database.

        Create a new database with the requested properties.

        :param str db: Path parameter to specify the database name.
        :param bool partitioned: (optional) Query parameter to specify whether to
               enable database partitions when creating a database.
               Before using read the
               [FAQs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-database-partitioning#partitioned-databases-database-partitioning)
               to understand the limitations and appropriate use cases.
        :param int q: (optional) The number of shards in the database. Each shard
               is a partition of the hash value range. Cloudant recommends using the
               default value for most databases. However, if your database is expected to
               be larger than 250 GB or have a lot of indexes, you may need to adjust the
               settings. In these cases, it's best to reach out to IBM Cloudant customer
               support for guidance on how to meet your specific needs and requirements.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ok` object
        """

        if not db:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='put_database',
        )
        headers.update(sdk_headers)

        params = {
            'partitioned': partitioned,
            'q': q,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Documents
    #########################

    def head_document(
        self,
        db: str,
        doc_id: str,
        *,
        if_none_match: Optional[str] = None,
        latest: Optional[bool] = None,
        rev: Optional[str] = None,
        **kwargs,
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
        :param str if_none_match: (optional) Header parameter for a conditional
               HTTP request not matching an ETag.
        :param bool latest: (optional) Query parameter to specify whether to force
               retrieving latest leaf revision, no matter what rev was requested.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not db:
            raise ValueError('db must be provided')
        if not doc_id:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-None-Match': if_none_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='head_document',
        )
        headers.update(sdk_headers)

        params = {
            'latest': latest,
            'rev': rev,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['db', 'doc_id']
        path_param_values = self.encode_path_vars(db, doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='HEAD',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def post_document(
        self,
        db: str,
        document: Union['Document', BinaryIO],
        *,
        content_type: Optional[str] = None,
        batch: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create or modify a document in a database.

        Creates or modifies a document in the specified database by using the supplied
        JSON document.
        For creation, you may specify the document ID but you should not specify the
        revision. If you don't specify the document ID, then the server generates an ID
        for your document.
        For modification, you must specify the document ID and a revision identifier in
        the JSON document.
        If your document ID includes the `_local/` or `_design/` prefix, then this
        operation creates or modifies a local or a design document respectively.

        :param str db: Path parameter to specify the database name.
        :param Document document: HTTP request body for Document operations.
        :param str content_type: (optional) The type of the input.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if document is None:
            raise ValueError('document must be provided')
        if isinstance(document, Document):
            document = convert_model(document)
            content_type = content_type or 'application/json'
        headers = {
            'Content-Type': content_type,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_document',
        )
        headers.update(sdk_headers)

        params = {
            'batch': batch,
        }

        if isinstance(document, dict):
            data = json.dumps(document)
            if content_type is None:
                headers['Content-Type'] = 'application/json'
        else:
            data = document

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_all_docs(
        self,
        db: str,
        *,
        att_encoding_info: Optional[bool] = None,
        attachments: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        descending: Optional[bool] = None,
        include_docs: Optional[bool] = None,
        inclusive_end: Optional[bool] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        update_seq: Optional[bool] = None,
        end_key: Optional[str] = None,
        key: Optional[str] = None,
        keys: Optional[List[str]] = None,
        start_key: Optional[str] = None,
        **kwargs,
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
               list of conflicted revisions in each returned document. Active only when
               `include_docs` is `true`.
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
        :param str end_key: (optional) Schema for a document ID.
        :param str key: (optional) Schema for a document ID.
        :param List[str] keys: (optional) Schema for a list of document IDs.
        :param str start_key: (optional) Schema for a document ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllDocsResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_all_docs',
        )
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
            'end_key': end_key,
            'key': key,
            'keys': keys,
            'start_key': start_key,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_all_docs'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_all_docs_as_stream(
        self,
        db: str,
        *,
        att_encoding_info: Optional[bool] = None,
        attachments: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        descending: Optional[bool] = None,
        include_docs: Optional[bool] = None,
        inclusive_end: Optional[bool] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        update_seq: Optional[bool] = None,
        end_key: Optional[str] = None,
        key: Optional[str] = None,
        keys: Optional[List[str]] = None,
        start_key: Optional[str] = None,
        **kwargs,
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
               list of conflicted revisions in each returned document. Active only when
               `include_docs` is `true`.
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
        :param str end_key: (optional) Schema for a document ID.
        :param str key: (optional) Schema for a document ID.
        :param List[str] keys: (optional) Schema for a list of document IDs.
        :param str start_key: (optional) Schema for a document ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not db:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_all_docs_as_stream',
        )
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
            'end_key': end_key,
            'key': key,
            'keys': keys,
            'start_key': start_key,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_all_docs'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, stream=True, **kwargs)
        return response

    def post_all_docs_queries(
        self,
        db: str,
        queries: List['AllDocsQuery'],
        **kwargs,
    ) -> DetailedResponse:
        """
        Multi-query the list of all documents in a database.

        Runs multiple queries using the primary index (all document IDs). Returns a JSON
        object that contains a list of result objects, one for each query, with a
        structure equivalent to that of a single `_all_docs` request. This enables you to
        request multiple queries in a single request, in place of multiple `POST
        /{db}/_all_docs` requests.

        :param str db: Path parameter to specify the database name.
        :param List[AllDocsQuery] queries: An array of query objects with fields
               for the parameters of each individual view query to be executed. The field
               names and their meaning are the same as the query parameters of a regular
               `/_all_docs` request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllDocsQueriesResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if queries is None:
            raise ValueError('queries must be provided')
        queries = [convert_model(x) for x in queries]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_all_docs_queries',
        )
        headers.update(sdk_headers)

        data = {
            'queries': queries,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_all_docs/queries'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_all_docs_queries_as_stream(
        self,
        db: str,
        queries: List['AllDocsQuery'],
        **kwargs,
    ) -> DetailedResponse:
        """
        Multi-query the list of all documents in a database as stream.

        Runs multiple queries using the primary index (all document IDs). Returns a JSON
        object that contains a list of result objects, one for each query, with a
        structure equivalent to that of a single `_all_docs` request. This enables you to
        request multiple queries in a single request, in place of multiple `POST
        /{db}/_all_docs` requests.

        :param str db: Path parameter to specify the database name.
        :param List[AllDocsQuery] queries: An array of query objects with fields
               for the parameters of each individual view query to be executed. The field
               names and their meaning are the same as the query parameters of a regular
               `/_all_docs` request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not db:
            raise ValueError('db must be provided')
        if queries is None:
            raise ValueError('queries must be provided')
        queries = [convert_model(x) for x in queries]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_all_docs_queries_as_stream',
        )
        headers.update(sdk_headers)

        data = {
            'queries': queries,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_all_docs/queries'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, stream=True, **kwargs)
        return response

    def post_bulk_docs(
        self,
        db: str,
        bulk_docs: Union['BulkDocs', BinaryIO],
        **kwargs,
    ) -> DetailedResponse:
        """
        Bulk modify multiple documents in a database.

        The bulk document API allows you to create, update, and delete multiple documents
        at the same time within a single request. The basic operation is similar to
        creating, updating, or deleting a single document, except that you batch the
        document structure and information.

        :param str db: Path parameter to specify the database name.
        :param BulkDocs bulk_docs: HTTP request body for postBulkDocs.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[DocumentResult]` result
        """

        if not db:
            raise ValueError('db must be provided')
        if bulk_docs is None:
            raise ValueError('bulk_docs must be provided')
        if isinstance(bulk_docs, BulkDocs):
            bulk_docs = convert_model(bulk_docs)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_bulk_docs',
        )
        headers.update(sdk_headers)

        if isinstance(bulk_docs, dict):
            data = json.dumps(bulk_docs)
        else:
            data = bulk_docs
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_bulk_docs'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_bulk_get(
        self,
        db: str,
        docs: List['BulkGetQueryDocument'],
        *,
        attachments: Optional[bool] = None,
        att_encoding_info: Optional[bool] = None,
        latest: Optional[bool] = None,
        revs: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Bulk query revision information for multiple documents.

        Fetch specific revisions or revision histories for multiple documents in bulk as
        replicators do.

        :param str db: Path parameter to specify the database name.
        :param List[BulkGetQueryDocument] docs: List of document items to get in
               bulk.
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

        if not db:
            raise ValueError('db must be provided')
        if docs is None:
            raise ValueError('docs must be provided')
        docs = [convert_model(x) for x in docs]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_bulk_get',
        )
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'latest': latest,
            'revs': revs,
        }

        data = {
            'docs': docs,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_bulk_get'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_bulk_get_as_mixed(
        self,
        db: str,
        docs: List['BulkGetQueryDocument'],
        *,
        attachments: Optional[bool] = None,
        att_encoding_info: Optional[bool] = None,
        latest: Optional[bool] = None,
        revs: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Bulk query revision information for multiple documents as mixed.

        Fetch specific revisions or revision histories for multiple documents in bulk as
        replicators do.

        :param str db: Path parameter to specify the database name.
        :param List[BulkGetQueryDocument] docs: List of document items to get in
               bulk.
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

        if not db:
            raise ValueError('db must be provided')
        if docs is None:
            raise ValueError('docs must be provided')
        docs = [convert_model(x) for x in docs]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_bulk_get_as_mixed',
        )
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'latest': latest,
            'revs': revs,
        }

        data = {
            'docs': docs,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'multipart/mixed'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_bulk_get'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_bulk_get_as_related(
        self,
        db: str,
        docs: List['BulkGetQueryDocument'],
        *,
        attachments: Optional[bool] = None,
        att_encoding_info: Optional[bool] = None,
        latest: Optional[bool] = None,
        revs: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Bulk query revision information for multiple documents as related.

        Fetch specific revisions or revision histories for multiple documents in bulk as
        replicators do.

        :param str db: Path parameter to specify the database name.
        :param List[BulkGetQueryDocument] docs: List of document items to get in
               bulk.
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

        if not db:
            raise ValueError('db must be provided')
        if docs is None:
            raise ValueError('docs must be provided')
        docs = [convert_model(x) for x in docs]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_bulk_get_as_related',
        )
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'latest': latest,
            'revs': revs,
        }

        data = {
            'docs': docs,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'multipart/related'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_bulk_get'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_bulk_get_as_stream(
        self,
        db: str,
        docs: List['BulkGetQueryDocument'],
        *,
        attachments: Optional[bool] = None,
        att_encoding_info: Optional[bool] = None,
        latest: Optional[bool] = None,
        revs: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Bulk query revision information for multiple documents as stream.

        Fetch specific revisions or revision histories for multiple documents in bulk as
        replicators do.

        :param str db: Path parameter to specify the database name.
        :param List[BulkGetQueryDocument] docs: List of document items to get in
               bulk.
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

        if not db:
            raise ValueError('db must be provided')
        if docs is None:
            raise ValueError('docs must be provided')
        docs = [convert_model(x) for x in docs]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_bulk_get_as_stream',
        )
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'latest': latest,
            'revs': revs,
        }

        data = {
            'docs': docs,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_bulk_get'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, stream=True, **kwargs)
        return response

    def delete_document(
        self,
        db: str,
        doc_id: str,
        *,
        if_match: Optional[str] = None,
        batch: Optional[str] = None,
        rev: Optional[str] = None,
        **kwargs,
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
        :param str if_match: (optional) Header parameter for a conditional HTTP
               request matching an ETag.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not doc_id:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_document',
        )
        headers.update(sdk_headers)

        params = {
            'batch': batch,
            'rev': rev,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'doc_id']
        path_param_values = self.encode_path_vars(db, doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_document(
        self,
        db: str,
        doc_id: str,
        *,
        if_none_match: Optional[str] = None,
        attachments: Optional[bool] = None,
        att_encoding_info: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        deleted_conflicts: Optional[bool] = None,
        latest: Optional[bool] = None,
        local_seq: Optional[bool] = None,
        meta: Optional[bool] = None,
        rev: Optional[str] = None,
        revs: Optional[bool] = None,
        revs_info: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a document.

        Returns document with the specified `doc_id` from the specified database. Unless
        you request a specific revision, the latest revision of the document is always
        returned.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str if_none_match: (optional) Header parameter for a conditional
               HTTP request not matching an ETag.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param bool conflicts: (optional) Query parameter to specify whether to
               include a list of conflicted revisions in each returned document. Active
               only when `include_docs` is `true`.
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
        :param str rev: (optional) Query parameter to specify a document revision.
        :param bool revs: (optional) Query parameter to specify whether to include
               a list of all known document revisions.
        :param bool revs_info: (optional) Query parameter to specify whether to
               includes detailed information for all known document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Document` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not doc_id:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-None-Match': if_none_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_document',
        )
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'conflicts': conflicts,
            'deleted_conflicts': deleted_conflicts,
            'latest': latest,
            'local_seq': local_seq,
            'meta': meta,
            'rev': rev,
            'revs': revs,
            'revs_info': revs_info,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'doc_id']
        path_param_values = self.encode_path_vars(db, doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_document_as_mixed(
        self,
        db: str,
        doc_id: str,
        *,
        if_none_match: Optional[str] = None,
        attachments: Optional[bool] = None,
        att_encoding_info: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        deleted_conflicts: Optional[bool] = None,
        latest: Optional[bool] = None,
        local_seq: Optional[bool] = None,
        meta: Optional[bool] = None,
        rev: Optional[str] = None,
        revs: Optional[bool] = None,
        revs_info: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a document as mixed.

        Returns document with the specified `doc_id` from the specified database. Unless
        you request a specific revision, the latest revision of the document is always
        returned.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str if_none_match: (optional) Header parameter for a conditional
               HTTP request not matching an ETag.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param bool conflicts: (optional) Query parameter to specify whether to
               include a list of conflicted revisions in each returned document. Active
               only when `include_docs` is `true`.
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
        :param str rev: (optional) Query parameter to specify a document revision.
        :param bool revs: (optional) Query parameter to specify whether to include
               a list of all known document revisions.
        :param bool revs_info: (optional) Query parameter to specify whether to
               includes detailed information for all known document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not db:
            raise ValueError('db must be provided')
        if not doc_id:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-None-Match': if_none_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_document_as_mixed',
        )
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'conflicts': conflicts,
            'deleted_conflicts': deleted_conflicts,
            'latest': latest,
            'local_seq': local_seq,
            'meta': meta,
            'rev': rev,
            'revs': revs,
            'revs_info': revs_info,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'multipart/mixed'

        path_param_keys = ['db', 'doc_id']
        path_param_values = self.encode_path_vars(db, doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_document_as_related(
        self,
        db: str,
        doc_id: str,
        *,
        if_none_match: Optional[str] = None,
        attachments: Optional[bool] = None,
        att_encoding_info: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        deleted_conflicts: Optional[bool] = None,
        latest: Optional[bool] = None,
        local_seq: Optional[bool] = None,
        meta: Optional[bool] = None,
        rev: Optional[str] = None,
        revs: Optional[bool] = None,
        revs_info: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a document as related.

        Returns document with the specified `doc_id` from the specified database. Unless
        you request a specific revision, the latest revision of the document is always
        returned.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str if_none_match: (optional) Header parameter for a conditional
               HTTP request not matching an ETag.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param bool conflicts: (optional) Query parameter to specify whether to
               include a list of conflicted revisions in each returned document. Active
               only when `include_docs` is `true`.
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
        :param str rev: (optional) Query parameter to specify a document revision.
        :param bool revs: (optional) Query parameter to specify whether to include
               a list of all known document revisions.
        :param bool revs_info: (optional) Query parameter to specify whether to
               includes detailed information for all known document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not db:
            raise ValueError('db must be provided')
        if not doc_id:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-None-Match': if_none_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_document_as_related',
        )
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'conflicts': conflicts,
            'deleted_conflicts': deleted_conflicts,
            'latest': latest,
            'local_seq': local_seq,
            'meta': meta,
            'rev': rev,
            'revs': revs,
            'revs_info': revs_info,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'multipart/related'

        path_param_keys = ['db', 'doc_id']
        path_param_values = self.encode_path_vars(db, doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_document_as_stream(
        self,
        db: str,
        doc_id: str,
        *,
        if_none_match: Optional[str] = None,
        attachments: Optional[bool] = None,
        att_encoding_info: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        deleted_conflicts: Optional[bool] = None,
        latest: Optional[bool] = None,
        local_seq: Optional[bool] = None,
        meta: Optional[bool] = None,
        rev: Optional[str] = None,
        revs: Optional[bool] = None,
        revs_info: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a document as stream.

        Returns document with the specified `doc_id` from the specified database. Unless
        you request a specific revision, the latest revision of the document is always
        returned.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str if_none_match: (optional) Header parameter for a conditional
               HTTP request not matching an ETag.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param bool conflicts: (optional) Query parameter to specify whether to
               include a list of conflicted revisions in each returned document. Active
               only when `include_docs` is `true`.
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
        :param str rev: (optional) Query parameter to specify a document revision.
        :param bool revs: (optional) Query parameter to specify whether to include
               a list of all known document revisions.
        :param bool revs_info: (optional) Query parameter to specify whether to
               includes detailed information for all known document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not db:
            raise ValueError('db must be provided')
        if not doc_id:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-None-Match': if_none_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_document_as_stream',
        )
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'conflicts': conflicts,
            'deleted_conflicts': deleted_conflicts,
            'latest': latest,
            'local_seq': local_seq,
            'meta': meta,
            'rev': rev,
            'revs': revs,
            'revs_info': revs_info,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'doc_id']
        path_param_values = self.encode_path_vars(db, doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, stream=True, **kwargs)
        return response

    def put_document(
        self,
        db: str,
        doc_id: str,
        document: Union['Document', BinaryIO],
        *,
        content_type: Optional[str] = None,
        if_match: Optional[str] = None,
        batch: Optional[str] = None,
        new_edits: Optional[bool] = None,
        rev: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create or modify a document.

        Creates or modifies a document in the specified database.
        For creation, you must specify the document ID but you should not specify the
        revision.
        For modification, you must specify the document ID and a revision  identifier.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param Document document: HTTP request body for Document operations.
        :param str content_type: (optional) The type of the input.
        :param str if_match: (optional) Header parameter for a conditional HTTP
               request matching an ETag.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param bool new_edits: (optional) Query parameter to specify whether to
               prevent insertion of conflicting document revisions. If false, a
               well-formed _rev must be included in the document. False is used by the
               replicator to insert documents into the target database even if that leads
               to the creation of conflicts.
               Avoid using this parameter, since this option applies document revisions
               without checking for conflicts, so it is very easy to accidentally end up
               with a large number of conflicts.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not doc_id:
            raise ValueError('doc_id must be provided')
        if document is None:
            raise ValueError('document must be provided')
        if isinstance(document, Document):
            document = convert_model(document)
            content_type = content_type or 'application/json'
        headers = {
            'Content-Type': content_type,
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='put_document',
        )
        headers.update(sdk_headers)

        params = {
            'batch': batch,
            'new_edits': new_edits,
            'rev': rev,
        }

        if isinstance(document, dict):
            data = json.dumps(document)
            if content_type is None:
                headers['Content-Type'] = 'application/json'
        else:
            data = document

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'doc_id']
        path_param_values = self.encode_path_vars(db, doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Design Documents
    #########################

    def head_design_document(
        self,
        db: str,
        ddoc: str,
        *,
        if_none_match: Optional[str] = None,
        **kwargs,
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
        :param str if_none_match: (optional) Header parameter for a conditional
               HTTP request not matching an ETag.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not db:
            raise ValueError('db must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        headers = {
            'If-None-Match': if_none_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='head_design_document',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['db', 'ddoc']
        path_param_values = self.encode_path_vars(db, ddoc)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_design/{ddoc}'.format(**path_param_dict)
        request = self.prepare_request(
            method='HEAD',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_design_document(
        self,
        db: str,
        ddoc: str,
        *,
        if_match: Optional[str] = None,
        batch: Optional[str] = None,
        rev: Optional[str] = None,
        **kwargs,
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
        :param str if_match: (optional) Header parameter for a conditional HTTP
               request matching an ETag.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_design_document',
        )
        headers.update(sdk_headers)

        params = {
            'batch': batch,
            'rev': rev,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'ddoc']
        path_param_values = self.encode_path_vars(db, ddoc)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_design/{ddoc}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_design_document(
        self,
        db: str,
        ddoc: str,
        *,
        if_none_match: Optional[str] = None,
        attachments: Optional[bool] = None,
        att_encoding_info: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        deleted_conflicts: Optional[bool] = None,
        latest: Optional[bool] = None,
        local_seq: Optional[bool] = None,
        meta: Optional[bool] = None,
        rev: Optional[str] = None,
        revs: Optional[bool] = None,
        revs_info: Optional[bool] = None,
        **kwargs,
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
        :param str if_none_match: (optional) Header parameter for a conditional
               HTTP request not matching an ETag.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param bool conflicts: (optional) Query parameter to specify whether to
               include a list of conflicted revisions in each returned document. Active
               only when `include_docs` is `true`.
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
        :param str rev: (optional) Query parameter to specify a document revision.
        :param bool revs: (optional) Query parameter to specify whether to include
               a list of all known document revisions.
        :param bool revs_info: (optional) Query parameter to specify whether to
               includes detailed information for all known document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DesignDocument` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        headers = {
            'If-None-Match': if_none_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_design_document',
        )
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'conflicts': conflicts,
            'deleted_conflicts': deleted_conflicts,
            'latest': latest,
            'local_seq': local_seq,
            'meta': meta,
            'rev': rev,
            'revs': revs,
            'revs_info': revs_info,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'ddoc']
        path_param_values = self.encode_path_vars(db, ddoc)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_design/{ddoc}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def put_design_document(
        self,
        db: str,
        ddoc: str,
        design_document: 'DesignDocument',
        *,
        if_match: Optional[str] = None,
        batch: Optional[str] = None,
        new_edits: Optional[bool] = None,
        rev: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create or modify a design document.

        The PUT method creates a new named design document, or creates a new revision of
        the existing design document.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param DesignDocument design_document: HTTP request body for DesignDocument
               operations.
        :param str if_match: (optional) Header parameter for a conditional HTTP
               request matching an ETag.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param bool new_edits: (optional) Query parameter to specify whether to
               prevent insertion of conflicting document revisions. If false, a
               well-formed _rev must be included in the document. False is used by the
               replicator to insert documents into the target database even if that leads
               to the creation of conflicts.
               Avoid using this parameter, since this option applies document revisions
               without checking for conflicts, so it is very easy to accidentally end up
               with a large number of conflicts.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        if design_document is None:
            raise ValueError('design_document must be provided')
        if isinstance(design_document, DesignDocument):
            design_document = convert_model(design_document)
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='put_design_document',
        )
        headers.update(sdk_headers)

        params = {
            'batch': batch,
            'new_edits': new_edits,
            'rev': rev,
        }

        data = json.dumps(design_document)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'ddoc']
        path_param_values = self.encode_path_vars(db, ddoc)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_design/{ddoc}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_design_document_information(
        self,
        db: str,
        ddoc: str,
        **kwargs,
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

        if not db:
            raise ValueError('db must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_design_document_information',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'ddoc']
        path_param_values = self.encode_path_vars(db, ddoc)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_design/{ddoc}/_info'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def post_design_docs(
        self,
        db: str,
        *,
        att_encoding_info: Optional[bool] = None,
        attachments: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        descending: Optional[bool] = None,
        include_docs: Optional[bool] = None,
        inclusive_end: Optional[bool] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        update_seq: Optional[bool] = None,
        end_key: Optional[str] = None,
        key: Optional[str] = None,
        keys: Optional[List[str]] = None,
        start_key: Optional[str] = None,
        **kwargs,
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
        :param bool att_encoding_info: (optional) Parameter to specify whether to
               include the encoding information in attachment stubs if the particular
               attachment is compressed.
        :param bool attachments: (optional) Parameter to specify whether to include
               attachments bodies in a response.
        :param bool conflicts: (optional) Parameter to specify whether to include a
               list of conflicted revisions in each returned document. Active only when
               `include_docs` is `true`.
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
        :param str end_key: (optional) Schema for a document ID.
        :param str key: (optional) Schema for a document ID.
        :param List[str] keys: (optional) Schema for a list of document IDs.
        :param str start_key: (optional) Schema for a document ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllDocsResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_design_docs',
        )
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
            'end_key': end_key,
            'key': key,
            'keys': keys,
            'start_key': start_key,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_design_docs'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_design_docs_queries(
        self,
        db: str,
        queries: List['AllDocsQuery'],
        *,
        accept: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Multi-query the list of all design documents.

        This operation runs multiple view queries of all design documents in the database.
        This operation enables you to request numerous queries in a single request, in
        place of multiple POST `/{db}/_design_docs` requests.

        :param str db: Path parameter to specify the database name.
        :param List[AllDocsQuery] queries: An array of query objects with fields
               for the parameters of each individual view query to be executed. The field
               names and their meaning are the same as the query parameters of a regular
               `/_all_docs` request.
        :param str accept: (optional) The type of the response: application/json or
               application/octet-stream.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllDocsQueriesResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if queries is None:
            raise ValueError('queries must be provided')
        queries = [convert_model(x) for x in queries]
        headers = {
            'Accept': accept,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_design_docs_queries',
        )
        headers.update(sdk_headers)

        data = {
            'queries': queries,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_design_docs/queries'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Views
    #########################

    def post_view(
        self,
        db: str,
        ddoc: str,
        view: str,
        *,
        att_encoding_info: Optional[bool] = None,
        attachments: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        descending: Optional[bool] = None,
        include_docs: Optional[bool] = None,
        inclusive_end: Optional[bool] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        update_seq: Optional[bool] = None,
        end_key: Optional[object] = None,
        end_key_doc_id: Optional[str] = None,
        group: Optional[bool] = None,
        group_level: Optional[int] = None,
        key: Optional[object] = None,
        keys: Optional[List[object]] = None,
        reduce: Optional[bool] = None,
        stable: Optional[bool] = None,
        start_key: Optional[object] = None,
        start_key_doc_id: Optional[str] = None,
        update: Optional[str] = None,
        **kwargs,
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
               list of conflicted revisions in each returned document. Active only when
               `include_docs` is `true`.
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
        :param object end_key: (optional) Schema for any JSON type.
        :param str end_key_doc_id: (optional) Schema for a document ID.
        :param bool group: (optional) Parameter to specify whether to group reduced
               results by key. Valid only if a reduce function defined in the view. If the
               view emits key in JSON array format, then it is possible to reduce groups
               further based on the number of array elements with the `group_level`
               parameter.
        :param int group_level: (optional) Parameter to specify a group level to be
               used. Only applicable if the view uses keys that are JSON arrays. Implies
               group is `true`. Group level groups the reduced results by the specified
               number of array elements. If unset, results are grouped by the entire array
               key, returning a reduced value for each complete key.
        :param object key: (optional) Schema for any JSON type.
        :param List[object] keys: (optional) Parameter to specify returning only
               documents that match any of the specified keys. A JSON array of keys that
               match the key type emitted by the view function.
        :param bool reduce: (optional) Parameter to specify whether to use the
               reduce function in a map-reduce view. Default is true when a reduce
               function is defined.
               A default `reduce` view type can be disabled to behave like a `map` by
               setting `reduce=false` explicitly.
               Be aware that `include_docs=true` can only be used with `map` views.
        :param bool stable: (optional) Query parameter to specify whether use the
               same replica of  the index on each request. The default value `false`
               contacts all  replicas and returns the result from the first, fastest,
               responder. Setting it to `true` when used in conjunction with
               `update=false`  may improve consistency at the expense of increased latency
               and decreased throughput if the selected replica is not the fastest of the
               available  replicas.
               **Note:** In general setting `true` is discouraged and is strictly not
               recommended when using `update=true`.
        :param object start_key: (optional) Schema for any JSON type.
        :param str start_key_doc_id: (optional) Schema for a document ID.
        :param str update: (optional) Parameter to specify whether or not the view
               in question should be updated prior to responding to the user.
               * `true` - Return results after the view is updated.
               * `false` - Return results without updating the view.
               * `lazy` - Return the view results without waiting for an update, but
               update them immediately after the request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ViewResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        if not view:
            raise ValueError('view must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_view',
        )
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
            'end_key': end_key,
            'end_key_doc_id': end_key_doc_id,
            'group': group,
            'group_level': group_level,
            'key': key,
            'keys': keys,
            'reduce': reduce,
            'stable': stable,
            'start_key': start_key,
            'start_key_doc_id': start_key_doc_id,
            'update': update,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'ddoc', 'view']
        path_param_values = self.encode_path_vars(db, ddoc, view)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_design/{ddoc}/_view/{view}'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_view_as_stream(
        self,
        db: str,
        ddoc: str,
        view: str,
        *,
        att_encoding_info: Optional[bool] = None,
        attachments: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        descending: Optional[bool] = None,
        include_docs: Optional[bool] = None,
        inclusive_end: Optional[bool] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        update_seq: Optional[bool] = None,
        end_key: Optional[object] = None,
        end_key_doc_id: Optional[str] = None,
        group: Optional[bool] = None,
        group_level: Optional[int] = None,
        key: Optional[object] = None,
        keys: Optional[List[object]] = None,
        reduce: Optional[bool] = None,
        stable: Optional[bool] = None,
        start_key: Optional[object] = None,
        start_key_doc_id: Optional[str] = None,
        update: Optional[str] = None,
        **kwargs,
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
               list of conflicted revisions in each returned document. Active only when
               `include_docs` is `true`.
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
        :param object end_key: (optional) Schema for any JSON type.
        :param str end_key_doc_id: (optional) Schema for a document ID.
        :param bool group: (optional) Parameter to specify whether to group reduced
               results by key. Valid only if a reduce function defined in the view. If the
               view emits key in JSON array format, then it is possible to reduce groups
               further based on the number of array elements with the `group_level`
               parameter.
        :param int group_level: (optional) Parameter to specify a group level to be
               used. Only applicable if the view uses keys that are JSON arrays. Implies
               group is `true`. Group level groups the reduced results by the specified
               number of array elements. If unset, results are grouped by the entire array
               key, returning a reduced value for each complete key.
        :param object key: (optional) Schema for any JSON type.
        :param List[object] keys: (optional) Parameter to specify returning only
               documents that match any of the specified keys. A JSON array of keys that
               match the key type emitted by the view function.
        :param bool reduce: (optional) Parameter to specify whether to use the
               reduce function in a map-reduce view. Default is true when a reduce
               function is defined.
               A default `reduce` view type can be disabled to behave like a `map` by
               setting `reduce=false` explicitly.
               Be aware that `include_docs=true` can only be used with `map` views.
        :param bool stable: (optional) Query parameter to specify whether use the
               same replica of  the index on each request. The default value `false`
               contacts all  replicas and returns the result from the first, fastest,
               responder. Setting it to `true` when used in conjunction with
               `update=false`  may improve consistency at the expense of increased latency
               and decreased throughput if the selected replica is not the fastest of the
               available  replicas.
               **Note:** In general setting `true` is discouraged and is strictly not
               recommended when using `update=true`.
        :param object start_key: (optional) Schema for any JSON type.
        :param str start_key_doc_id: (optional) Schema for a document ID.
        :param str update: (optional) Parameter to specify whether or not the view
               in question should be updated prior to responding to the user.
               * `true` - Return results after the view is updated.
               * `false` - Return results without updating the view.
               * `lazy` - Return the view results without waiting for an update, but
               update them immediately after the request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not db:
            raise ValueError('db must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        if not view:
            raise ValueError('view must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_view_as_stream',
        )
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
            'end_key': end_key,
            'end_key_doc_id': end_key_doc_id,
            'group': group,
            'group_level': group_level,
            'key': key,
            'keys': keys,
            'reduce': reduce,
            'stable': stable,
            'start_key': start_key,
            'start_key_doc_id': start_key_doc_id,
            'update': update,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'ddoc', 'view']
        path_param_values = self.encode_path_vars(db, ddoc, view)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_design/{ddoc}/_view/{view}'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, stream=True, **kwargs)
        return response

    def post_view_queries(
        self,
        db: str,
        ddoc: str,
        view: str,
        queries: List['ViewQuery'],
        **kwargs,
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
        :param List[ViewQuery] queries: An array of query objects with fields for
               the parameters of each individual view query to be executed. The field
               names and their meaning are the same as the query parameters of a regular
               view request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ViewQueriesResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        if not view:
            raise ValueError('view must be provided')
        if queries is None:
            raise ValueError('queries must be provided')
        queries = [convert_model(x) for x in queries]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_view_queries',
        )
        headers.update(sdk_headers)

        data = {
            'queries': queries,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'ddoc', 'view']
        path_param_values = self.encode_path_vars(db, ddoc, view)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_design/{ddoc}/_view/{view}/queries'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_view_queries_as_stream(
        self,
        db: str,
        ddoc: str,
        view: str,
        queries: List['ViewQuery'],
        **kwargs,
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
        :param List[ViewQuery] queries: An array of query objects with fields for
               the parameters of each individual view query to be executed. The field
               names and their meaning are the same as the query parameters of a regular
               view request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not db:
            raise ValueError('db must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        if not view:
            raise ValueError('view must be provided')
        if queries is None:
            raise ValueError('queries must be provided')
        queries = [convert_model(x) for x in queries]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_view_queries_as_stream',
        )
        headers.update(sdk_headers)

        data = {
            'queries': queries,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'ddoc', 'view']
        path_param_values = self.encode_path_vars(db, ddoc, view)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_design/{ddoc}/_view/{view}/queries'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, stream=True, **kwargs)
        return response

    #########################
    # Queries
    #########################

    def get_partition_information(
        self,
        db: str,
        partition_key: str,
        **kwargs,
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

        if not db:
            raise ValueError('db must be provided')
        if not partition_key:
            raise ValueError('partition_key must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_partition_information',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'partition_key']
        path_param_values = self.encode_path_vars(db, partition_key)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_partition/{partition_key}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def post_partition_all_docs(
        self,
        db: str,
        partition_key: str,
        *,
        att_encoding_info: Optional[bool] = None,
        attachments: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        descending: Optional[bool] = None,
        include_docs: Optional[bool] = None,
        inclusive_end: Optional[bool] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        update_seq: Optional[bool] = None,
        end_key: Optional[str] = None,
        key: Optional[str] = None,
        keys: Optional[List[str]] = None,
        start_key: Optional[str] = None,
        **kwargs,
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
               list of conflicted revisions in each returned document. Active only when
               `include_docs` is `true`.
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
        :param str end_key: (optional) Schema for a document ID.
        :param str key: (optional) Schema for a document ID.
        :param List[str] keys: (optional) Schema for a list of document IDs.
        :param str start_key: (optional) Schema for a document ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllDocsResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not partition_key:
            raise ValueError('partition_key must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_partition_all_docs',
        )
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
            'end_key': end_key,
            'key': key,
            'keys': keys,
            'start_key': start_key,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'partition_key']
        path_param_values = self.encode_path_vars(db, partition_key)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_partition/{partition_key}/_all_docs'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_partition_all_docs_as_stream(
        self,
        db: str,
        partition_key: str,
        *,
        att_encoding_info: Optional[bool] = None,
        attachments: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        descending: Optional[bool] = None,
        include_docs: Optional[bool] = None,
        inclusive_end: Optional[bool] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        update_seq: Optional[bool] = None,
        end_key: Optional[str] = None,
        key: Optional[str] = None,
        keys: Optional[List[str]] = None,
        start_key: Optional[str] = None,
        **kwargs,
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
               list of conflicted revisions in each returned document. Active only when
               `include_docs` is `true`.
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
        :param str end_key: (optional) Schema for a document ID.
        :param str key: (optional) Schema for a document ID.
        :param List[str] keys: (optional) Schema for a list of document IDs.
        :param str start_key: (optional) Schema for a document ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not db:
            raise ValueError('db must be provided')
        if not partition_key:
            raise ValueError('partition_key must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_partition_all_docs_as_stream',
        )
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
            'end_key': end_key,
            'key': key,
            'keys': keys,
            'start_key': start_key,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'partition_key']
        path_param_values = self.encode_path_vars(db, partition_key)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_partition/{partition_key}/_all_docs'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, stream=True, **kwargs)
        return response

    def post_partition_search(
        self,
        db: str,
        partition_key: str,
        ddoc: str,
        index: str,
        query: str,
        *,
        bookmark: Optional[str] = None,
        highlight_fields: Optional[List[str]] = None,
        highlight_number: Optional[int] = None,
        highlight_post_tag: Optional[str] = None,
        highlight_pre_tag: Optional[str] = None,
        highlight_size: Optional[int] = None,
        include_docs: Optional[bool] = None,
        include_fields: Optional[List[str]] = None,
        limit: Optional[int] = None,
        sort: Optional[List[str]] = None,
        stale: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Query a database partition search index.

        Partitioned Search indexes, which are defined in design documents, allow partition
        databases to be queried by using Lucene Query Parser Syntax. Search indexes are
        defined by an index function, similar to a map function in MapReduce views. The
        index function decides what data to index and store in the index.
        Before using read the
        [FAQs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-database-partitioning#partition-querying)
        to understand the limitations and appropriate use cases.

        :param str db: Path parameter to specify the database name.
        :param str partition_key: Path parameter to specify the database partition
               key.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str index: Path parameter to specify the index name.
        :param str query: The Lucene query to execute.
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

        if not db:
            raise ValueError('db must be provided')
        if not partition_key:
            raise ValueError('partition_key must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        if not index:
            raise ValueError('index must be provided')
        if query is None:
            raise ValueError('query must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_partition_search',
        )
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
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'partition_key', 'ddoc', 'index']
        path_param_values = self.encode_path_vars(db, partition_key, ddoc, index)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_partition/{partition_key}/_design/{ddoc}/_search/{index}'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_partition_search_as_stream(
        self,
        db: str,
        partition_key: str,
        ddoc: str,
        index: str,
        query: str,
        *,
        bookmark: Optional[str] = None,
        highlight_fields: Optional[List[str]] = None,
        highlight_number: Optional[int] = None,
        highlight_post_tag: Optional[str] = None,
        highlight_pre_tag: Optional[str] = None,
        highlight_size: Optional[int] = None,
        include_docs: Optional[bool] = None,
        include_fields: Optional[List[str]] = None,
        limit: Optional[int] = None,
        sort: Optional[List[str]] = None,
        stale: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Query a database partition search index as stream.

        Partitioned Search indexes, which are defined in design documents, allow partition
        databases to be queried by using Lucene Query Parser Syntax. Search indexes are
        defined by an index function, similar to a map function in MapReduce views. The
        index function decides what data to index and store in the index.
        Before using read the
        [FAQs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-database-partitioning#partition-querying)
        to understand the limitations and appropriate use cases.

        :param str db: Path parameter to specify the database name.
        :param str partition_key: Path parameter to specify the database partition
               key.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str index: Path parameter to specify the index name.
        :param str query: The Lucene query to execute.
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

        if not db:
            raise ValueError('db must be provided')
        if not partition_key:
            raise ValueError('partition_key must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        if not index:
            raise ValueError('index must be provided')
        if query is None:
            raise ValueError('query must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_partition_search_as_stream',
        )
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
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'partition_key', 'ddoc', 'index']
        path_param_values = self.encode_path_vars(db, partition_key, ddoc, index)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_partition/{partition_key}/_design/{ddoc}/_search/{index}'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, stream=True, **kwargs)
        return response

    def post_partition_view(
        self,
        db: str,
        partition_key: str,
        ddoc: str,
        view: str,
        *,
        att_encoding_info: Optional[bool] = None,
        attachments: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        descending: Optional[bool] = None,
        include_docs: Optional[bool] = None,
        inclusive_end: Optional[bool] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        update_seq: Optional[bool] = None,
        end_key: Optional[object] = None,
        end_key_doc_id: Optional[str] = None,
        group: Optional[bool] = None,
        group_level: Optional[int] = None,
        key: Optional[object] = None,
        keys: Optional[List[object]] = None,
        reduce: Optional[bool] = None,
        start_key: Optional[object] = None,
        start_key_doc_id: Optional[str] = None,
        update: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Query a database partition MapReduce view function.

        Runs the specified view function from the specified design document. Unlike `GET
        /{db}/_design/{ddoc}/_view/{view}` for accessing views, the POST method supports
        the specification of explicit keys to be retrieved from the view results. The
        remainder of the POST view functionality is identical to the `GET
        /{db}/_design/{ddoc}/_view/{view}` API.
        Before using read the
        [FAQs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-database-partitioning#partition-querying)
        to understand the limitations and appropriate use cases.

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
               list of conflicted revisions in each returned document. Active only when
               `include_docs` is `true`.
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
        :param object end_key: (optional) Schema for any JSON type.
        :param str end_key_doc_id: (optional) Schema for a document ID.
        :param bool group: (optional) Parameter to specify whether to group reduced
               results by key. Valid only if a reduce function defined in the view. If the
               view emits key in JSON array format, then it is possible to reduce groups
               further based on the number of array elements with the `group_level`
               parameter.
        :param int group_level: (optional) Parameter to specify a group level to be
               used. Only applicable if the view uses keys that are JSON arrays. Implies
               group is `true`. Group level groups the reduced results by the specified
               number of array elements. If unset, results are grouped by the entire array
               key, returning a reduced value for each complete key.
        :param object key: (optional) Schema for any JSON type.
        :param List[object] keys: (optional) Parameter to specify returning only
               documents that match any of the specified keys. A JSON array of keys that
               match the key type emitted by the view function.
        :param bool reduce: (optional) Parameter to specify whether to use the
               reduce function in a map-reduce view. Default is true when a reduce
               function is defined.
               A default `reduce` view type can be disabled to behave like a `map` by
               setting `reduce=false` explicitly.
               Be aware that `include_docs=true` can only be used with `map` views.
        :param object start_key: (optional) Schema for any JSON type.
        :param str start_key_doc_id: (optional) Schema for a document ID.
        :param str update: (optional) Parameter to specify whether or not the view
               in question should be updated prior to responding to the user.
               * `true` - Return results after the view is updated.
               * `false` - Return results without updating the view.
               * `lazy` - Return the view results without waiting for an update, but
               update them immediately after the request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ViewResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not partition_key:
            raise ValueError('partition_key must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        if not view:
            raise ValueError('view must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_partition_view',
        )
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
            'end_key': end_key,
            'end_key_doc_id': end_key_doc_id,
            'group': group,
            'group_level': group_level,
            'key': key,
            'keys': keys,
            'reduce': reduce,
            'start_key': start_key,
            'start_key_doc_id': start_key_doc_id,
            'update': update,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'partition_key', 'ddoc', 'view']
        path_param_values = self.encode_path_vars(db, partition_key, ddoc, view)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_partition/{partition_key}/_design/{ddoc}/_view/{view}'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_partition_view_as_stream(
        self,
        db: str,
        partition_key: str,
        ddoc: str,
        view: str,
        *,
        att_encoding_info: Optional[bool] = None,
        attachments: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        descending: Optional[bool] = None,
        include_docs: Optional[bool] = None,
        inclusive_end: Optional[bool] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        update_seq: Optional[bool] = None,
        end_key: Optional[object] = None,
        end_key_doc_id: Optional[str] = None,
        group: Optional[bool] = None,
        group_level: Optional[int] = None,
        key: Optional[object] = None,
        keys: Optional[List[object]] = None,
        reduce: Optional[bool] = None,
        start_key: Optional[object] = None,
        start_key_doc_id: Optional[str] = None,
        update: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Query a database partition MapReduce view function as stream.

        Runs the specified view function from the specified design document. Unlike `GET
        /{db}/_design/{ddoc}/_view/{view}` for accessing views, the POST method supports
        the specification of explicit keys to be retrieved from the view results. The
        remainder of the POST view functionality is identical to the `GET
        /{db}/_design/{ddoc}/_view/{view}` API.
        Before using read the
        [FAQs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-database-partitioning#partition-querying)
        to understand the limitations and appropriate use cases.

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
               list of conflicted revisions in each returned document. Active only when
               `include_docs` is `true`.
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
        :param object end_key: (optional) Schema for any JSON type.
        :param str end_key_doc_id: (optional) Schema for a document ID.
        :param bool group: (optional) Parameter to specify whether to group reduced
               results by key. Valid only if a reduce function defined in the view. If the
               view emits key in JSON array format, then it is possible to reduce groups
               further based on the number of array elements with the `group_level`
               parameter.
        :param int group_level: (optional) Parameter to specify a group level to be
               used. Only applicable if the view uses keys that are JSON arrays. Implies
               group is `true`. Group level groups the reduced results by the specified
               number of array elements. If unset, results are grouped by the entire array
               key, returning a reduced value for each complete key.
        :param object key: (optional) Schema for any JSON type.
        :param List[object] keys: (optional) Parameter to specify returning only
               documents that match any of the specified keys. A JSON array of keys that
               match the key type emitted by the view function.
        :param bool reduce: (optional) Parameter to specify whether to use the
               reduce function in a map-reduce view. Default is true when a reduce
               function is defined.
               A default `reduce` view type can be disabled to behave like a `map` by
               setting `reduce=false` explicitly.
               Be aware that `include_docs=true` can only be used with `map` views.
        :param object start_key: (optional) Schema for any JSON type.
        :param str start_key_doc_id: (optional) Schema for a document ID.
        :param str update: (optional) Parameter to specify whether or not the view
               in question should be updated prior to responding to the user.
               * `true` - Return results after the view is updated.
               * `false` - Return results without updating the view.
               * `lazy` - Return the view results without waiting for an update, but
               update them immediately after the request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not db:
            raise ValueError('db must be provided')
        if not partition_key:
            raise ValueError('partition_key must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        if not view:
            raise ValueError('view must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_partition_view_as_stream',
        )
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
            'end_key': end_key,
            'end_key_doc_id': end_key_doc_id,
            'group': group,
            'group_level': group_level,
            'key': key,
            'keys': keys,
            'reduce': reduce,
            'start_key': start_key,
            'start_key_doc_id': start_key_doc_id,
            'update': update,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'partition_key', 'ddoc', 'view']
        path_param_values = self.encode_path_vars(db, partition_key, ddoc, view)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_partition/{partition_key}/_design/{ddoc}/_view/{view}'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, stream=True, **kwargs)
        return response

    def post_partition_explain(
        self,
        db: str,
        partition_key: str,
        selector: dict,
        *,
        allow_fallback: Optional[bool] = None,
        bookmark: Optional[str] = None,
        conflicts: Optional[bool] = None,
        execution_stats: Optional[bool] = None,
        fields: Optional[List[str]] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        sort: Optional[List[dict]] = None,
        stable: Optional[bool] = None,
        update: Optional[str] = None,
        use_index: Optional[List[str]] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve information about which partition index is used for a query.

        Shows which index is being used by the query. Parameters are the same as the
        [`/{db}/_partition/{partition_key}/_find` endpoint](#postpartitionfind-queries).

        :param str db: Path parameter to specify the database name.
        :param str partition_key: Path parameter to specify the database partition
               key.
        :param dict selector: JSON object describing criteria used to select
               documents. The selector specifies fields in the document, and provides an
               expression to evaluate with the field content or other data.
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
               are used to combine selectors. A combination operator takes a single
               argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
               It is important for query performance to use appropriate selectors:
               * Only equality operators such as `$eq`, `$gt`, `$gte`, `$lt`, and `$lte`
               (but not `$ne`) can be used as the basis of a query. You should include at
               least one of these in a selector.
               * Some operators such as `$not`, `$or`, `$in`, and `$regex` cannot be
               answered from an index. For query selectors use these operators in
               conjunction with equality operators or create and use a partial index to
               reduce the number of documents that will need to be scanned.
               See [the Cloudant
               Docs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-operators)for a
               list of all available combination and conditional operators.
               For further reference see [selector
               syntax](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-selector-syntax).
        :param bool allow_fallback: (optional) Whether to allow fallback to other
               indexes.  Default is true.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param bool conflicts: (optional) A boolean value that indicates whether or
               not to include information about existing conflicts in the document.
        :param bool execution_stats: (optional) Use this option to find information
               about the query that was run. This information includes total key lookups,
               total document lookups (when `include_docs=true` is used), and total quorum
               document lookups (when each document replica is fetched).
        :param List[str] fields: (optional) JSON array that uses the field syntax.
               Use this parameter to specify which fields of a document must be returned.
               If it is omitted or empty, the entire document is returned.
        :param int limit: (optional) Maximum number of results returned. The `type:
               text` indexes are limited to 200 results when queried.
        :param int skip: (optional) Skip the first 'n' results, where 'n' is the
               value that is specified.
        :param List[dict] sort: (optional) The sort field contains a list of pairs,
               each mapping a field name to a sort direction (asc or desc). The first
               field name and direction pair is the topmost level of sort. The second
               pair, if provided, is the next level of sort. The field can be any field,
               using dotted notation if desired for sub-document fields.
               For example in JSON: `[{"fieldName1": "desc"}, {"fieldName2.subFieldName1":
               "desc"}]`
               When sorting with multiple fields, ensure that there is an index already
               defined with all the sort fields in the same order and each object in the
               sort array has a single key or at least one of the sort fields is included
               in the selector. All sorting fields must use the same sort direction,
               either all ascending or all descending.
        :param bool stable: (optional) Whether or not the view results should be
               returned from a "stable" set of shards.
        :param str update: (optional) Whether to update the index prior to
               returning the result.
        :param List[str] use_index: (optional) Use this option to identify a
               specific index to answer the query, rather than letting the IBM Cloudant
               query planner choose an index. Specified as a two element array of design
               document id followed by index name, for example `["my_design_doc",
               "my_index"]`.
               It’s recommended to specify indexes explicitly in your queries to prevent
               existing queries being affected by new indexes that might get added later.
               If the specified index doesn't exist or can't answer the query then the
               server ignores the value and answers using another index or a full scan of
               all documents. To change this behavior set `allow_fallback` to `false` and
               the server responds instead with a `400` status code if the requested index
               is unsuitable to answer the query.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ExplainResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not partition_key:
            raise ValueError('partition_key must be provided')
        if selector is None:
            raise ValueError('selector must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_partition_explain',
        )
        headers.update(sdk_headers)

        data = {
            'selector': selector,
            'allow_fallback': allow_fallback,
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
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'partition_key']
        path_param_values = self.encode_path_vars(db, partition_key)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_partition/{partition_key}/_explain'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_partition_find(
        self,
        db: str,
        partition_key: str,
        selector: dict,
        *,
        allow_fallback: Optional[bool] = None,
        bookmark: Optional[str] = None,
        conflicts: Optional[bool] = None,
        execution_stats: Optional[bool] = None,
        fields: Optional[List[str]] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        sort: Optional[List[dict]] = None,
        stable: Optional[bool] = None,
        update: Optional[str] = None,
        use_index: Optional[List[str]] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Query a database partition index by using selector syntax.

        Query documents by using a declarative JSON querying syntax. It's best practice to
        create an appropriate index for all fields in selector by using the `_index`
        endpoint.
        Queries without an appropriate backing index by default fallback to using the
        built-in `_all_docs` index. This isn't recommended because it has a significant
        performance impact causing a full scan of the partition with each request. In this
        case the response body includes a warning field recommending the creation of an
        index.
        To avoid the fallback behavior set the `allow_fallback` option to `false` and the
        server responds with a `400` status code if no suitable index exists. If you want
        to use only a specific index for your query set
        `allow_fallback` to `false` and set the `use_index` option.
        Before using read the
        [FAQs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-database-partitioning#partition-querying)
        to understand the limitations and appropriate use cases.

        :param str db: Path parameter to specify the database name.
        :param str partition_key: Path parameter to specify the database partition
               key.
        :param dict selector: JSON object describing criteria used to select
               documents. The selector specifies fields in the document, and provides an
               expression to evaluate with the field content or other data.
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
               are used to combine selectors. A combination operator takes a single
               argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
               It is important for query performance to use appropriate selectors:
               * Only equality operators such as `$eq`, `$gt`, `$gte`, `$lt`, and `$lte`
               (but not `$ne`) can be used as the basis of a query. You should include at
               least one of these in a selector.
               * Some operators such as `$not`, `$or`, `$in`, and `$regex` cannot be
               answered from an index. For query selectors use these operators in
               conjunction with equality operators or create and use a partial index to
               reduce the number of documents that will need to be scanned.
               See [the Cloudant
               Docs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-operators)for a
               list of all available combination and conditional operators.
               For further reference see [selector
               syntax](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-selector-syntax).
        :param bool allow_fallback: (optional) Whether to allow fallback to other
               indexes.  Default is true.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param bool conflicts: (optional) A boolean value that indicates whether or
               not to include information about existing conflicts in the document.
        :param bool execution_stats: (optional) Use this option to find information
               about the query that was run. This information includes total key lookups,
               total document lookups (when `include_docs=true` is used), and total quorum
               document lookups (when each document replica is fetched).
        :param List[str] fields: (optional) JSON array that uses the field syntax.
               Use this parameter to specify which fields of a document must be returned.
               If it is omitted or empty, the entire document is returned.
        :param int limit: (optional) Maximum number of results returned. The `type:
               text` indexes are limited to 200 results when queried.
        :param int skip: (optional) Skip the first 'n' results, where 'n' is the
               value that is specified.
        :param List[dict] sort: (optional) The sort field contains a list of pairs,
               each mapping a field name to a sort direction (asc or desc). The first
               field name and direction pair is the topmost level of sort. The second
               pair, if provided, is the next level of sort. The field can be any field,
               using dotted notation if desired for sub-document fields.
               For example in JSON: `[{"fieldName1": "desc"}, {"fieldName2.subFieldName1":
               "desc"}]`
               When sorting with multiple fields, ensure that there is an index already
               defined with all the sort fields in the same order and each object in the
               sort array has a single key or at least one of the sort fields is included
               in the selector. All sorting fields must use the same sort direction,
               either all ascending or all descending.
        :param bool stable: (optional) Whether or not the view results should be
               returned from a "stable" set of shards.
        :param str update: (optional) Whether to update the index prior to
               returning the result.
        :param List[str] use_index: (optional) Use this option to identify a
               specific index to answer the query, rather than letting the IBM Cloudant
               query planner choose an index. Specified as a two element array of design
               document id followed by index name, for example `["my_design_doc",
               "my_index"]`.
               It’s recommended to specify indexes explicitly in your queries to prevent
               existing queries being affected by new indexes that might get added later.
               If the specified index doesn't exist or can't answer the query then the
               server ignores the value and answers using another index or a full scan of
               all documents. To change this behavior set `allow_fallback` to `false` and
               the server responds instead with a `400` status code if the requested index
               is unsuitable to answer the query.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `FindResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not partition_key:
            raise ValueError('partition_key must be provided')
        if selector is None:
            raise ValueError('selector must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_partition_find',
        )
        headers.update(sdk_headers)

        data = {
            'selector': selector,
            'allow_fallback': allow_fallback,
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
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'partition_key']
        path_param_values = self.encode_path_vars(db, partition_key)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_partition/{partition_key}/_find'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_partition_find_as_stream(
        self,
        db: str,
        partition_key: str,
        selector: dict,
        *,
        allow_fallback: Optional[bool] = None,
        bookmark: Optional[str] = None,
        conflicts: Optional[bool] = None,
        execution_stats: Optional[bool] = None,
        fields: Optional[List[str]] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        sort: Optional[List[dict]] = None,
        stable: Optional[bool] = None,
        update: Optional[str] = None,
        use_index: Optional[List[str]] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Query a database partition index by using selector syntax as stream.

        Query documents by using a declarative JSON querying syntax. It's best practice to
        create an appropriate index for all fields in selector by using the `_index`
        endpoint.
        Queries without an appropriate backing index by default fallback to using the
        built-in `_all_docs` index. This isn't recommended because it has a significant
        performance impact causing a full scan of the partition with each request. In this
        case the response body includes a warning field recommending the creation of an
        index.
        To avoid the fallback behavior set the `allow_fallback` option to `false` and the
        server responds with a `400` status code if no suitable index exists. If you want
        to use only a specific index for your query set
        `allow_fallback` to `false` and set the `use_index` option.
        Before using read the
        [FAQs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-database-partitioning#partition-querying)
        to understand the limitations and appropriate use cases.

        :param str db: Path parameter to specify the database name.
        :param str partition_key: Path parameter to specify the database partition
               key.
        :param dict selector: JSON object describing criteria used to select
               documents. The selector specifies fields in the document, and provides an
               expression to evaluate with the field content or other data.
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
               are used to combine selectors. A combination operator takes a single
               argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
               It is important for query performance to use appropriate selectors:
               * Only equality operators such as `$eq`, `$gt`, `$gte`, `$lt`, and `$lte`
               (but not `$ne`) can be used as the basis of a query. You should include at
               least one of these in a selector.
               * Some operators such as `$not`, `$or`, `$in`, and `$regex` cannot be
               answered from an index. For query selectors use these operators in
               conjunction with equality operators or create and use a partial index to
               reduce the number of documents that will need to be scanned.
               See [the Cloudant
               Docs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-operators)for a
               list of all available combination and conditional operators.
               For further reference see [selector
               syntax](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-selector-syntax).
        :param bool allow_fallback: (optional) Whether to allow fallback to other
               indexes.  Default is true.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param bool conflicts: (optional) A boolean value that indicates whether or
               not to include information about existing conflicts in the document.
        :param bool execution_stats: (optional) Use this option to find information
               about the query that was run. This information includes total key lookups,
               total document lookups (when `include_docs=true` is used), and total quorum
               document lookups (when each document replica is fetched).
        :param List[str] fields: (optional) JSON array that uses the field syntax.
               Use this parameter to specify which fields of a document must be returned.
               If it is omitted or empty, the entire document is returned.
        :param int limit: (optional) Maximum number of results returned. The `type:
               text` indexes are limited to 200 results when queried.
        :param int skip: (optional) Skip the first 'n' results, where 'n' is the
               value that is specified.
        :param List[dict] sort: (optional) The sort field contains a list of pairs,
               each mapping a field name to a sort direction (asc or desc). The first
               field name and direction pair is the topmost level of sort. The second
               pair, if provided, is the next level of sort. The field can be any field,
               using dotted notation if desired for sub-document fields.
               For example in JSON: `[{"fieldName1": "desc"}, {"fieldName2.subFieldName1":
               "desc"}]`
               When sorting with multiple fields, ensure that there is an index already
               defined with all the sort fields in the same order and each object in the
               sort array has a single key or at least one of the sort fields is included
               in the selector. All sorting fields must use the same sort direction,
               either all ascending or all descending.
        :param bool stable: (optional) Whether or not the view results should be
               returned from a "stable" set of shards.
        :param str update: (optional) Whether to update the index prior to
               returning the result.
        :param List[str] use_index: (optional) Use this option to identify a
               specific index to answer the query, rather than letting the IBM Cloudant
               query planner choose an index. Specified as a two element array of design
               document id followed by index name, for example `["my_design_doc",
               "my_index"]`.
               It’s recommended to specify indexes explicitly in your queries to prevent
               existing queries being affected by new indexes that might get added later.
               If the specified index doesn't exist or can't answer the query then the
               server ignores the value and answers using another index or a full scan of
               all documents. To change this behavior set `allow_fallback` to `false` and
               the server responds instead with a `400` status code if the requested index
               is unsuitable to answer the query.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not db:
            raise ValueError('db must be provided')
        if not partition_key:
            raise ValueError('partition_key must be provided')
        if selector is None:
            raise ValueError('selector must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_partition_find_as_stream',
        )
        headers.update(sdk_headers)

        data = {
            'selector': selector,
            'allow_fallback': allow_fallback,
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
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'partition_key']
        path_param_values = self.encode_path_vars(db, partition_key)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_partition/{partition_key}/_find'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, stream=True, **kwargs)
        return response

    #########################
    # Queries
    #########################

    def post_explain(
        self,
        db: str,
        selector: dict,
        *,
        allow_fallback: Optional[bool] = None,
        bookmark: Optional[str] = None,
        conflicts: Optional[bool] = None,
        execution_stats: Optional[bool] = None,
        fields: Optional[List[str]] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        sort: Optional[List[dict]] = None,
        stable: Optional[bool] = None,
        update: Optional[str] = None,
        use_index: Optional[List[str]] = None,
        r: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve information about which index is used for a query.

        Shows which index is being used by the query. Parameters are the same as the
        [`_find` endpoint](#postfind).

        :param str db: Path parameter to specify the database name.
        :param dict selector: JSON object describing criteria used to select
               documents. The selector specifies fields in the document, and provides an
               expression to evaluate with the field content or other data.
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
               are used to combine selectors. A combination operator takes a single
               argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
               It is important for query performance to use appropriate selectors:
               * Only equality operators such as `$eq`, `$gt`, `$gte`, `$lt`, and `$lte`
               (but not `$ne`) can be used as the basis of a query. You should include at
               least one of these in a selector.
               * Some operators such as `$not`, `$or`, `$in`, and `$regex` cannot be
               answered from an index. For query selectors use these operators in
               conjunction with equality operators or create and use a partial index to
               reduce the number of documents that will need to be scanned.
               See [the Cloudant
               Docs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-operators)for a
               list of all available combination and conditional operators.
               For further reference see [selector
               syntax](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-selector-syntax).
        :param bool allow_fallback: (optional) Whether to allow fallback to other
               indexes.  Default is true.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param bool conflicts: (optional) A boolean value that indicates whether or
               not to include information about existing conflicts in the document.
        :param bool execution_stats: (optional) Use this option to find information
               about the query that was run. This information includes total key lookups,
               total document lookups (when `include_docs=true` is used), and total quorum
               document lookups (when each document replica is fetched).
        :param List[str] fields: (optional) JSON array that uses the field syntax.
               Use this parameter to specify which fields of a document must be returned.
               If it is omitted or empty, the entire document is returned.
        :param int limit: (optional) Maximum number of results returned. The `type:
               text` indexes are limited to 200 results when queried.
        :param int skip: (optional) Skip the first 'n' results, where 'n' is the
               value that is specified.
        :param List[dict] sort: (optional) The sort field contains a list of pairs,
               each mapping a field name to a sort direction (asc or desc). The first
               field name and direction pair is the topmost level of sort. The second
               pair, if provided, is the next level of sort. The field can be any field,
               using dotted notation if desired for sub-document fields.
               For example in JSON: `[{"fieldName1": "desc"}, {"fieldName2.subFieldName1":
               "desc"}]`
               When sorting with multiple fields, ensure that there is an index already
               defined with all the sort fields in the same order and each object in the
               sort array has a single key or at least one of the sort fields is included
               in the selector. All sorting fields must use the same sort direction,
               either all ascending or all descending.
        :param bool stable: (optional) Whether or not the view results should be
               returned from a "stable" set of shards.
        :param str update: (optional) Whether to update the index prior to
               returning the result.
        :param List[str] use_index: (optional) Use this option to identify a
               specific index to answer the query, rather than letting the IBM Cloudant
               query planner choose an index. Specified as a two element array of design
               document id followed by index name, for example `["my_design_doc",
               "my_index"]`.
               It’s recommended to specify indexes explicitly in your queries to prevent
               existing queries being affected by new indexes that might get added later.
               If the specified index doesn't exist or can't answer the query then the
               server ignores the value and answers using another index or a full scan of
               all documents. To change this behavior set `allow_fallback` to `false` and
               the server responds instead with a `400` status code if the requested index
               is unsuitable to answer the query.
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

        if not db:
            raise ValueError('db must be provided')
        if selector is None:
            raise ValueError('selector must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_explain',
        )
        headers.update(sdk_headers)

        data = {
            'selector': selector,
            'allow_fallback': allow_fallback,
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
            'r': r,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_explain'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_find(
        self,
        db: str,
        selector: dict,
        *,
        allow_fallback: Optional[bool] = None,
        bookmark: Optional[str] = None,
        conflicts: Optional[bool] = None,
        execution_stats: Optional[bool] = None,
        fields: Optional[List[str]] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        sort: Optional[List[dict]] = None,
        stable: Optional[bool] = None,
        update: Optional[str] = None,
        use_index: Optional[List[str]] = None,
        r: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Query an index by using selector syntax.

        Query documents by using a declarative JSON querying syntax. It's best practice to
        create an appropriate index for all fields in selector by using the `_index`
        endpoint.
        Queries without an appropriate backing index by default fallback to using the
        built-in `_all_docs` index. This isn't recommended because it has a significant
        performance impact causing a full scan of the database with each request. In this
        case the response body includes a warning field recommending the creation of an
        index.
        To avoid the fallback behavior set the `allow_fallback` option to `false` and the
        server responds with a `400` status code if no suitable index exists. If you want
        to use only a specific index for your query set
        `allow_fallback` to `false` and set the `use_index` option.

        :param str db: Path parameter to specify the database name.
        :param dict selector: JSON object describing criteria used to select
               documents. The selector specifies fields in the document, and provides an
               expression to evaluate with the field content or other data.
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
               are used to combine selectors. A combination operator takes a single
               argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
               It is important for query performance to use appropriate selectors:
               * Only equality operators such as `$eq`, `$gt`, `$gte`, `$lt`, and `$lte`
               (but not `$ne`) can be used as the basis of a query. You should include at
               least one of these in a selector.
               * Some operators such as `$not`, `$or`, `$in`, and `$regex` cannot be
               answered from an index. For query selectors use these operators in
               conjunction with equality operators or create and use a partial index to
               reduce the number of documents that will need to be scanned.
               See [the Cloudant
               Docs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-operators)for a
               list of all available combination and conditional operators.
               For further reference see [selector
               syntax](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-selector-syntax).
        :param bool allow_fallback: (optional) Whether to allow fallback to other
               indexes.  Default is true.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param bool conflicts: (optional) A boolean value that indicates whether or
               not to include information about existing conflicts in the document.
        :param bool execution_stats: (optional) Use this option to find information
               about the query that was run. This information includes total key lookups,
               total document lookups (when `include_docs=true` is used), and total quorum
               document lookups (when each document replica is fetched).
        :param List[str] fields: (optional) JSON array that uses the field syntax.
               Use this parameter to specify which fields of a document must be returned.
               If it is omitted or empty, the entire document is returned.
        :param int limit: (optional) Maximum number of results returned. The `type:
               text` indexes are limited to 200 results when queried.
        :param int skip: (optional) Skip the first 'n' results, where 'n' is the
               value that is specified.
        :param List[dict] sort: (optional) The sort field contains a list of pairs,
               each mapping a field name to a sort direction (asc or desc). The first
               field name and direction pair is the topmost level of sort. The second
               pair, if provided, is the next level of sort. The field can be any field,
               using dotted notation if desired for sub-document fields.
               For example in JSON: `[{"fieldName1": "desc"}, {"fieldName2.subFieldName1":
               "desc"}]`
               When sorting with multiple fields, ensure that there is an index already
               defined with all the sort fields in the same order and each object in the
               sort array has a single key or at least one of the sort fields is included
               in the selector. All sorting fields must use the same sort direction,
               either all ascending or all descending.
        :param bool stable: (optional) Whether or not the view results should be
               returned from a "stable" set of shards.
        :param str update: (optional) Whether to update the index prior to
               returning the result.
        :param List[str] use_index: (optional) Use this option to identify a
               specific index to answer the query, rather than letting the IBM Cloudant
               query planner choose an index. Specified as a two element array of design
               document id followed by index name, for example `["my_design_doc",
               "my_index"]`.
               It’s recommended to specify indexes explicitly in your queries to prevent
               existing queries being affected by new indexes that might get added later.
               If the specified index doesn't exist or can't answer the query then the
               server ignores the value and answers using another index or a full scan of
               all documents. To change this behavior set `allow_fallback` to `false` and
               the server responds instead with a `400` status code if the requested index
               is unsuitable to answer the query.
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

        if not db:
            raise ValueError('db must be provided')
        if selector is None:
            raise ValueError('selector must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_find',
        )
        headers.update(sdk_headers)

        data = {
            'selector': selector,
            'allow_fallback': allow_fallback,
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
            'r': r,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_find'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_find_as_stream(
        self,
        db: str,
        selector: dict,
        *,
        allow_fallback: Optional[bool] = None,
        bookmark: Optional[str] = None,
        conflicts: Optional[bool] = None,
        execution_stats: Optional[bool] = None,
        fields: Optional[List[str]] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        sort: Optional[List[dict]] = None,
        stable: Optional[bool] = None,
        update: Optional[str] = None,
        use_index: Optional[List[str]] = None,
        r: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Query an index by using selector syntax as stream.

        Query documents by using a declarative JSON querying syntax. It's best practice to
        create an appropriate index for all fields in selector by using the `_index`
        endpoint.
        Queries without an appropriate backing index by default fallback to using the
        built-in `_all_docs` index. This isn't recommended because it has a significant
        performance impact causing a full scan of the database with each request. In this
        case the response body includes a warning field recommending the creation of an
        index.
        To avoid the fallback behavior set the `allow_fallback` option to `false` and the
        server responds with a `400` status code if no suitable index exists. If you want
        to use only a specific index for your query set
        `allow_fallback` to `false` and set the `use_index` option.

        :param str db: Path parameter to specify the database name.
        :param dict selector: JSON object describing criteria used to select
               documents. The selector specifies fields in the document, and provides an
               expression to evaluate with the field content or other data.
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
               are used to combine selectors. A combination operator takes a single
               argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
               It is important for query performance to use appropriate selectors:
               * Only equality operators such as `$eq`, `$gt`, `$gte`, `$lt`, and `$lte`
               (but not `$ne`) can be used as the basis of a query. You should include at
               least one of these in a selector.
               * Some operators such as `$not`, `$or`, `$in`, and `$regex` cannot be
               answered from an index. For query selectors use these operators in
               conjunction with equality operators or create and use a partial index to
               reduce the number of documents that will need to be scanned.
               See [the Cloudant
               Docs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-operators)for a
               list of all available combination and conditional operators.
               For further reference see [selector
               syntax](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-selector-syntax).
        :param bool allow_fallback: (optional) Whether to allow fallback to other
               indexes.  Default is true.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param bool conflicts: (optional) A boolean value that indicates whether or
               not to include information about existing conflicts in the document.
        :param bool execution_stats: (optional) Use this option to find information
               about the query that was run. This information includes total key lookups,
               total document lookups (when `include_docs=true` is used), and total quorum
               document lookups (when each document replica is fetched).
        :param List[str] fields: (optional) JSON array that uses the field syntax.
               Use this parameter to specify which fields of a document must be returned.
               If it is omitted or empty, the entire document is returned.
        :param int limit: (optional) Maximum number of results returned. The `type:
               text` indexes are limited to 200 results when queried.
        :param int skip: (optional) Skip the first 'n' results, where 'n' is the
               value that is specified.
        :param List[dict] sort: (optional) The sort field contains a list of pairs,
               each mapping a field name to a sort direction (asc or desc). The first
               field name and direction pair is the topmost level of sort. The second
               pair, if provided, is the next level of sort. The field can be any field,
               using dotted notation if desired for sub-document fields.
               For example in JSON: `[{"fieldName1": "desc"}, {"fieldName2.subFieldName1":
               "desc"}]`
               When sorting with multiple fields, ensure that there is an index already
               defined with all the sort fields in the same order and each object in the
               sort array has a single key or at least one of the sort fields is included
               in the selector. All sorting fields must use the same sort direction,
               either all ascending or all descending.
        :param bool stable: (optional) Whether or not the view results should be
               returned from a "stable" set of shards.
        :param str update: (optional) Whether to update the index prior to
               returning the result.
        :param List[str] use_index: (optional) Use this option to identify a
               specific index to answer the query, rather than letting the IBM Cloudant
               query planner choose an index. Specified as a two element array of design
               document id followed by index name, for example `["my_design_doc",
               "my_index"]`.
               It’s recommended to specify indexes explicitly in your queries to prevent
               existing queries being affected by new indexes that might get added later.
               If the specified index doesn't exist or can't answer the query then the
               server ignores the value and answers using another index or a full scan of
               all documents. To change this behavior set `allow_fallback` to `false` and
               the server responds instead with a `400` status code if the requested index
               is unsuitable to answer the query.
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

        if not db:
            raise ValueError('db must be provided')
        if selector is None:
            raise ValueError('selector must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_find_as_stream',
        )
        headers.update(sdk_headers)

        data = {
            'selector': selector,
            'allow_fallback': allow_fallback,
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
            'r': r,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_find'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, stream=True, **kwargs)
        return response

    def get_indexes_information(
        self,
        db: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve information about all indexes.

        When you make a GET request to `/db/_index`, you get a list of all the indexes
        using `"language":"query"` in the database and the primary index. In addition to
        the information available through this API, the indexes are stored in the
        `indexes` property of their respective design documents.

        :param str db: Path parameter to specify the database name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IndexesInformation` object
        """

        if not db:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_indexes_information',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_index'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def post_index(
        self,
        db: str,
        index: 'IndexDefinition',
        *,
        ddoc: Optional[str] = None,
        name: Optional[str] = None,
        partitioned: Optional[bool] = None,
        type: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a new index on a database.

        Create a new index on a database.

        :param str db: Path parameter to specify the database name.
        :param IndexDefinition index: Schema for a `json` or `text` query index
               definition. Indexes of type `text` have additional configuration properties
               that do not apply to `json` indexes, these are:
               * `default_analyzer` - the default text analyzer to use * `default_field` -
               whether to index the text in all document fields and what analyzer to use
               for that purpose.
        :param str ddoc: (optional) Specifies the design document name in which the
               index will be created. The design document name is the design document ID
               excluding the `_design/` prefix.
        :param str name: (optional) name.
        :param bool partitioned: (optional) The default value is `true` for
               databases with `partitioned: true` and `false` otherwise. For databases
               with `partitioned: false` if this option is specified the value must be
               `false`.
        :param str type: (optional) Schema for the type of an index.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IndexResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if index is None:
            raise ValueError('index must be provided')
        index = convert_model(index)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_index',
        )
        headers.update(sdk_headers)

        data = {
            'index': index,
            'ddoc': ddoc,
            'name': name,
            'partitioned': partitioned,
            'type': type,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_index'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_index(
        self,
        db: str,
        ddoc: str,
        type: str,
        index: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete an index.

        Delete the index functions from the design document and index files on the server.

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

        if not db:
            raise ValueError('db must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        if not type:
            raise ValueError('type must be provided')
        if not index:
            raise ValueError('index must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_index',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'ddoc', 'type', 'index']
        path_param_values = self.encode_path_vars(db, ddoc, type, index)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_index/_design/{ddoc}/{type}/{index}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Searches
    #########################

    def post_search_analyze(
        self,
        analyzer: str,
        text: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Query tokenization of sample text.

        Returns the results of analyzer tokenization of the provided sample text. This
        endpoint can be used for testing analyzer tokenization.

        :param str analyzer: The analyzer type that is being used at the
               tokenization.
        :param str text: The text to tokenize with the analyzer.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SearchAnalyzeResult` object
        """

        if analyzer is None:
            raise ValueError('analyzer must be provided')
        if text is None:
            raise ValueError('text must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_search_analyze',
        )
        headers.update(sdk_headers)

        data = {
            'analyzer': analyzer,
            'text': text,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_search_analyze'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_search(
        self,
        db: str,
        ddoc: str,
        index: str,
        query: str,
        *,
        bookmark: Optional[str] = None,
        highlight_fields: Optional[List[str]] = None,
        highlight_number: Optional[int] = None,
        highlight_post_tag: Optional[str] = None,
        highlight_pre_tag: Optional[str] = None,
        highlight_size: Optional[int] = None,
        include_docs: Optional[bool] = None,
        include_fields: Optional[List[str]] = None,
        limit: Optional[int] = None,
        sort: Optional[List[str]] = None,
        stale: Optional[str] = None,
        counts: Optional[List[str]] = None,
        drilldown: Optional[List[List[str]]] = None,
        group_field: Optional[str] = None,
        group_limit: Optional[int] = None,
        group_sort: Optional[List[str]] = None,
        ranges: Optional[dict] = None,
        **kwargs,
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
        :param str query: The Lucene query to execute.
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
        :param dict ranges: (optional) Object mapping faceted, numeric search field
               names to the required ranges. Each key is a field name and each value is
               another object defining the ranges by mapping range name keys to string
               values describing the numeric ranges, for example "[0 TO 10]". This option
               is only available when making global queries.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SearchResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        if not index:
            raise ValueError('index must be provided')
        if query is None:
            raise ValueError('query must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_search',
        )
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
            'ranges': ranges,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'ddoc', 'index']
        path_param_values = self.encode_path_vars(db, ddoc, index)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_design/{ddoc}/_search/{index}'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_search_as_stream(
        self,
        db: str,
        ddoc: str,
        index: str,
        query: str,
        *,
        bookmark: Optional[str] = None,
        highlight_fields: Optional[List[str]] = None,
        highlight_number: Optional[int] = None,
        highlight_post_tag: Optional[str] = None,
        highlight_pre_tag: Optional[str] = None,
        highlight_size: Optional[int] = None,
        include_docs: Optional[bool] = None,
        include_fields: Optional[List[str]] = None,
        limit: Optional[int] = None,
        sort: Optional[List[str]] = None,
        stale: Optional[str] = None,
        counts: Optional[List[str]] = None,
        drilldown: Optional[List[List[str]]] = None,
        group_field: Optional[str] = None,
        group_limit: Optional[int] = None,
        group_sort: Optional[List[str]] = None,
        ranges: Optional[dict] = None,
        **kwargs,
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
        :param str query: The Lucene query to execute.
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
        :param dict ranges: (optional) Object mapping faceted, numeric search field
               names to the required ranges. Each key is a field name and each value is
               another object defining the ranges by mapping range name keys to string
               values describing the numeric ranges, for example "[0 TO 10]". This option
               is only available when making global queries.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not db:
            raise ValueError('db must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        if not index:
            raise ValueError('index must be provided')
        if query is None:
            raise ValueError('query must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_search_as_stream',
        )
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
            'ranges': ranges,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'ddoc', 'index']
        path_param_values = self.encode_path_vars(db, ddoc, index)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_design/{ddoc}/_search/{index}'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, stream=True, **kwargs)
        return response

    def get_search_disk_size(
        self,
        db: str,
        ddoc: str,
        index: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve information about the search index disk size.

        Retrieve size of the search index on disk.

        :param str db: Path parameter to specify the database name.
        :param str ddoc: Path parameter to specify the design document name. The
               design document name is the design document ID excluding the `_design/`
               prefix.
        :param str index: Path parameter to specify the index name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SearchDiskSizeInformation` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        if not index:
            raise ValueError('index must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_search_disk_size',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'ddoc', 'index']
        path_param_values = self.encode_path_vars(db, ddoc, index)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_design/{ddoc}/_search_disk_size/{index}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_search_info(
        self,
        db: str,
        ddoc: str,
        index: str,
        **kwargs,
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

        if not db:
            raise ValueError('db must be provided')
        if not ddoc:
            raise ValueError('ddoc must be provided')
        if not index:
            raise ValueError('index must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_search_info',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'ddoc', 'index']
        path_param_values = self.encode_path_vars(db, ddoc, index)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_design/{ddoc}/_search_info/{index}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Replication
    #########################

    def head_replication_document(
        self,
        doc_id: str,
        *,
        if_none_match: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve the HTTP headers for a persistent replication.

        Retrieves the HTTP headers containing minimal amount of information about the
        specified replication document from the `_replicator` database.  The method
        supports the same query arguments as the `GET /_replicator/{doc_id}` method, but
        only headers like content length and the revision (ETag header) are returned.

        :param str doc_id: Path parameter to specify the ID of the stored
               replication configuration in the `_replicator` database.
        :param str if_none_match: (optional) Header parameter for a conditional
               HTTP request not matching an ETag.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not doc_id:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-None-Match': if_none_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='head_replication_document',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['doc_id']
        path_param_values = self.encode_path_vars(doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/_replicator/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='HEAD',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def head_scheduler_document(
        self,
        doc_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve HTTP headers for a replication scheduler document.

        Retrieves the HTTP headers containing minimal amount of information about the
        specified replication scheduler document.  Since the response body is empty, using
        the HEAD method is a lightweight way to check if the replication scheduler
        document exists or not.

        :param str doc_id: Path parameter to specify the document ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not doc_id:
            raise ValueError('doc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='head_scheduler_document',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['doc_id']
        path_param_values = self.encode_path_vars(doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/_scheduler/docs/_replicator/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='HEAD',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def head_scheduler_job(
        self,
        job_id: str,
        **kwargs,
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

        if not job_id:
            raise ValueError('job_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='head_scheduler_job',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['job_id']
        path_param_values = self.encode_path_vars(job_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/_scheduler/jobs/{job_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='HEAD',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def post_replicator(
        self,
        replication_document: 'ReplicationDocument',
        *,
        batch: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a persistent replication with a generated ID.

        Creates or modifies a document in the `_replicator` database to start a new
        replication or to edit an existing replication.

        :param ReplicationDocument replication_document: HTTP request body for
               replication operations.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if replication_document is None:
            raise ValueError('replication_document must be provided')
        if isinstance(replication_document, ReplicationDocument):
            replication_document = convert_model(replication_document)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_replicator',
        )
        headers.update(sdk_headers)

        params = {
            'batch': batch,
        }

        data = json.dumps(replication_document)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_replicator'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_replication_document(
        self,
        doc_id: str,
        *,
        if_match: Optional[str] = None,
        batch: Optional[str] = None,
        rev: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Cancel a persistent replication.

        Cancels a replication by deleting the document that describes it from the
        `_replicator` database.

        :param str doc_id: Path parameter to specify the ID of the stored
               replication configuration in the `_replicator` database.
        :param str if_match: (optional) Header parameter for a conditional HTTP
               request matching an ETag.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if not doc_id:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_replication_document',
        )
        headers.update(sdk_headers)

        params = {
            'batch': batch,
            'rev': rev,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['doc_id']
        path_param_values = self.encode_path_vars(doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/_replicator/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_replication_document(
        self,
        doc_id: str,
        *,
        if_none_match: Optional[str] = None,
        attachments: Optional[bool] = None,
        att_encoding_info: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        deleted_conflicts: Optional[bool] = None,
        latest: Optional[bool] = None,
        local_seq: Optional[bool] = None,
        meta: Optional[bool] = None,
        rev: Optional[str] = None,
        revs: Optional[bool] = None,
        revs_info: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve the configuration for a persistent replication.

        Retrieves a replication document from the `_replicator` database to view the
        configuration of the replication. The status of the replication is no longer
        recorded in the document but can be checked via the replication scheduler.

        :param str doc_id: Path parameter to specify the ID of the stored
               replication configuration in the `_replicator` database.
        :param str if_none_match: (optional) Header parameter for a conditional
               HTTP request not matching an ETag.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param bool conflicts: (optional) Query parameter to specify whether to
               include a list of conflicted revisions in each returned document. Active
               only when `include_docs` is `true`.
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
        :param str rev: (optional) Query parameter to specify a document revision.
        :param bool revs: (optional) Query parameter to specify whether to include
               a list of all known document revisions.
        :param bool revs_info: (optional) Query parameter to specify whether to
               includes detailed information for all known document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReplicationDocument` object
        """

        if not doc_id:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-None-Match': if_none_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_replication_document',
        )
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'conflicts': conflicts,
            'deleted_conflicts': deleted_conflicts,
            'latest': latest,
            'local_seq': local_seq,
            'meta': meta,
            'rev': rev,
            'revs': revs,
            'revs_info': revs_info,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['doc_id']
        path_param_values = self.encode_path_vars(doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/_replicator/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def put_replication_document(
        self,
        doc_id: str,
        replication_document: 'ReplicationDocument',
        *,
        if_match: Optional[str] = None,
        batch: Optional[str] = None,
        new_edits: Optional[bool] = None,
        rev: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create or modify a persistent replication.

        Creates or modifies a document in the `_replicator` database to start a new
        replication or to edit an existing replication.

        :param str doc_id: Path parameter to specify the ID of the stored
               replication configuration in the `_replicator` database.
        :param ReplicationDocument replication_document: HTTP request body for
               replication operations.
        :param str if_match: (optional) Header parameter for a conditional HTTP
               request matching an ETag.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param bool new_edits: (optional) Query parameter to specify whether to
               prevent insertion of conflicting document revisions. If false, a
               well-formed _rev must be included in the document. False is used by the
               replicator to insert documents into the target database even if that leads
               to the creation of conflicts.
               Avoid using this parameter, since this option applies document revisions
               without checking for conflicts, so it is very easy to accidentally end up
               with a large number of conflicts.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if not doc_id:
            raise ValueError('doc_id must be provided')
        if replication_document is None:
            raise ValueError('replication_document must be provided')
        if isinstance(replication_document, ReplicationDocument):
            replication_document = convert_model(replication_document)
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='put_replication_document',
        )
        headers.update(sdk_headers)

        params = {
            'batch': batch,
            'new_edits': new_edits,
            'rev': rev,
        }

        data = json.dumps(replication_document)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['doc_id']
        path_param_values = self.encode_path_vars(doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/_replicator/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_scheduler_docs(
        self,
        *,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        states: Optional[List[str]] = None,
        **kwargs,
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
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_scheduler_docs',
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'skip': skip,
            'states': convert_list(states),
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_scheduler/docs'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_scheduler_document(
        self,
        doc_id: str,
        **kwargs,
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

        if not doc_id:
            raise ValueError('doc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_scheduler_document',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['doc_id']
        path_param_values = self.encode_path_vars(doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/_scheduler/docs/_replicator/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_scheduler_jobs(
        self,
        *,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve replication scheduler jobs.

        Retrieves information about replications that were created via `/_replicate`
        endpoint, as well as those created from replication documents. It doesn't include
        replications that completed or failed to start because replication documents were
        malformed. Each job description includes source and target information,
        replication ID, history of recent events, and other information.

        :param int limit: (optional) Query parameter to specify the number of
               returned jobs to limit the result to.
        :param int skip: (optional) Query parameter to specify the number of
               records before starting to return the results.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SchedulerJobsResult` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_scheduler_jobs',
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'skip': skip,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_scheduler/jobs'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_scheduler_job(
        self,
        job_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a replication scheduler job.

        Retrieves the state of a single replication task based on its replication ID.

        :param str job_id: Path parameter to specify the replication job id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SchedulerJob` object
        """

        if not job_id:
            raise ValueError('job_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_scheduler_job',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['job_id']
        path_param_values = self.encode_path_vars(job_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/_scheduler/jobs/{job_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Authentication
    #########################

    def get_session_information(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve current session cookie information.

        Retrieves information about the authenticated user's session.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SessionInformation` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_session_information',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_session'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Authorization
    #########################

    def post_api_keys(
        self,
        **kwargs,
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
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_api_keys',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_api/v2/api_keys'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def put_cloudant_security_configuration(
        self,
        db: str,
        cloudant: dict,
        *,
        admins: Optional['SecurityObject'] = None,
        couchdb_auth_only: Optional[bool] = None,
        members: Optional['SecurityObject'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Modify only Cloudant related database permissions.

        Modify only Cloudant related permissions to database. Be careful: by removing an
        API key from the list, you remove the API key from the list of users that have
        access to the database.
        ### Note about nobody role
        The `nobody` username applies to all unauthenticated connection attempts. For
        example, if an application tries to read data from a database, but did not
        identify itself, the task can continue only if the `nobody` user has the role
        `_reader`.

        :param str db: Path parameter to specify the database name.
        :param dict cloudant: Database permissions for Cloudant users and/or API
               keys.
        :param SecurityObject admins: (optional) Schema for names and roles to map
               to a database permission.
        :param bool couchdb_auth_only: (optional) Manage permissions using the
               `_users` database only.
        :param SecurityObject members: (optional) Schema for names and roles to map
               to a database permission.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ok` object
        """

        if not db:
            raise ValueError('db must be provided')
        if cloudant is None:
            raise ValueError('cloudant must be provided')
        if admins is not None:
            admins = convert_model(admins)
        if members is not None:
            members = convert_model(members)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='put_cloudant_security_configuration',
        )
        headers.update(sdk_headers)

        data = {
            'cloudant': cloudant,
            'admins': admins,
            'couchdb_auth_only': couchdb_auth_only,
            'members': members,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/_api/v2/db/{db}/_security'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_security(
        self,
        db: str,
        **kwargs,
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

        if not db:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_security',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_security'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def put_security(
        self,
        db: str,
        *,
        admins: Optional['SecurityObject'] = None,
        cloudant: Optional[dict] = None,
        couchdb_auth_only: Optional[bool] = None,
        members: Optional['SecurityObject'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Modify database permissions.

        Modify who has permission to read, write, or manage a database. This endpoint can
        be used to modify both Cloudant and CouchDB related permissions. Be careful: by
        removing a Cloudant API key, a member or an admin from the list of users that have
        access permissions, you remove it from the list of users that have access to the
        database.
        ### Note about nobody role
        The `nobody` username applies to all unauthenticated connection attempts. For
        example, if an application tries to read data from a database, but did not
        identify itself, the task can continue only if the `nobody` user has the role
        `_reader`.

        :param str db: Path parameter to specify the database name.
        :param SecurityObject admins: (optional) Schema for names and roles to map
               to a database permission.
        :param dict cloudant: (optional) Database permissions for Cloudant users
               and/or API keys.
        :param bool couchdb_auth_only: (optional) Manage permissions using the
               `_users` database only.
        :param SecurityObject members: (optional) Schema for names and roles to map
               to a database permission.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ok` object
        """

        if not db:
            raise ValueError('db must be provided')
        if admins is not None:
            admins = convert_model(admins)
        if members is not None:
            members = convert_model(members)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='put_security',
        )
        headers.update(sdk_headers)

        data = {
            'admins': admins,
            'cloudant': cloudant,
            'couchdb_auth_only': couchdb_auth_only,
            'members': members,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_security'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # CORS
    #########################

    def get_cors_information(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve CORS configuration information.

        Lists all Cross-origin resource sharing (CORS) configuration. CORS defines a way
        in which the browser and the server interact to determine whether or not to allow
        the request.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CorsInformation` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_cors_information',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_api/v2/user/config/cors'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def put_cors_configuration(
        self,
        origins: List[str],
        *,
        allow_credentials: Optional[bool] = None,
        enable_cors: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Modify CORS configuration.

        Sets the CORS configuration. The configuration applies to all databases and all
        account level endpoints in your account.

        :param List[str] origins: An array of strings that contain allowed origin
               domains. You have to specify the full URL including the protocol. It is
               recommended that only the HTTPS protocol is used. Subdomains count as
               separate domains, so you have to specify all subdomains used.
        :param bool allow_credentials: (optional) Boolean value to allow
               authentication credentials. If set to true, browser requests must be done
               by using withCredentials = true.
        :param bool enable_cors: (optional) Boolean value to turn CORS on and off.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ok` object
        """

        if origins is None:
            raise ValueError('origins must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='put_cors_configuration',
        )
        headers.update(sdk_headers)

        data = {
            'origins': origins,
            'allow_credentials': allow_credentials,
            'enable_cors': enable_cors,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_api/v2/user/config/cors'
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Attachments
    #########################

    def head_attachment(
        self,
        db: str,
        doc_id: str,
        attachment_name: str,
        *,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        rev: Optional[str] = None,
        **kwargs,
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
        :param str if_match: (optional) Header parameter for a conditional HTTP
               request matching an ETag.
        :param str if_none_match: (optional) Header parameter for a conditional
               HTTP request not matching an ETag.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not db:
            raise ValueError('db must be provided')
        if not doc_id:
            raise ValueError('doc_id must be provided')
        if not attachment_name:
            raise ValueError('attachment_name must be provided')
        headers = {
            'If-Match': if_match,
            'If-None-Match': if_none_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='head_attachment',
        )
        headers.update(sdk_headers)

        params = {
            'rev': rev,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['db', 'doc_id', 'attachment_name']
        path_param_values = self.encode_path_vars(db, doc_id, attachment_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/{doc_id}/{attachment_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='HEAD',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_attachment(
        self,
        db: str,
        doc_id: str,
        attachment_name: str,
        *,
        if_match: Optional[str] = None,
        rev: Optional[str] = None,
        batch: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete an attachment.

        Deletes the attachment with the filename, `{attachment_name}`, from the specified
        doc. You must supply the `rev` query parameter or `If-Match` header with the
        current revision to delete the attachment.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str attachment_name: Path parameter to specify the attachment name.
        :param str if_match: (optional) Header parameter for a conditional HTTP
               request matching an ETag.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not doc_id:
            raise ValueError('doc_id must be provided')
        if not attachment_name:
            raise ValueError('attachment_name must be provided')
        headers = {
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_attachment',
        )
        headers.update(sdk_headers)

        params = {
            'rev': rev,
            'batch': batch,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'doc_id', 'attachment_name']
        path_param_values = self.encode_path_vars(db, doc_id, attachment_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/{doc_id}/{attachment_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_attachment(
        self,
        db: str,
        doc_id: str,
        attachment_name: str,
        *,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        range: Optional[str] = None,
        rev: Optional[str] = None,
        **kwargs,
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
        :param str if_match: (optional) Header parameter for a conditional HTTP
               request matching an ETag.
        :param str if_none_match: (optional) Header parameter for a conditional
               HTTP request not matching an ETag.
        :param str range: (optional) Header parameter to specify the byte range for
               a request. This allows the implementation of resumable downloads and
               skippable streams. This is available for all attachments inside CouchDB.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not db:
            raise ValueError('db must be provided')
        if not doc_id:
            raise ValueError('doc_id must be provided')
        if not attachment_name:
            raise ValueError('attachment_name must be provided')
        headers = {
            'If-Match': if_match,
            'If-None-Match': if_none_match,
            'Range': range,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_attachment',
        )
        headers.update(sdk_headers)

        params = {
            'rev': rev,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = '*/*'

        path_param_keys = ['db', 'doc_id', 'attachment_name']
        path_param_values = self.encode_path_vars(db, doc_id, attachment_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/{doc_id}/{attachment_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def put_attachment(
        self,
        db: str,
        doc_id: str,
        attachment_name: str,
        attachment: BinaryIO,
        content_type: str,
        *,
        if_match: Optional[str] = None,
        rev: Optional[str] = None,
        **kwargs,
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
        :param str if_match: (optional) Header parameter for a conditional HTTP
               request matching an ETag.
        :param str rev: (optional) Query parameter to specify a document revision.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not doc_id:
            raise ValueError('doc_id must be provided')
        if not attachment_name:
            raise ValueError('attachment_name must be provided')
        if attachment is None:
            raise ValueError('attachment must be provided')
        if not content_type:
            raise ValueError('content_type must be provided')
        headers = {
            'Content-Type': content_type,
            'If-Match': if_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='put_attachment',
        )
        headers.update(sdk_headers)

        params = {
            'rev': rev,
        }

        data = attachment

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'doc_id', 'attachment_name']
        path_param_values = self.encode_path_vars(db, doc_id, attachment_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/{doc_id}/{attachment_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Local Documents
    #########################

    def head_local_document(
        self,
        db: str,
        doc_id: str,
        *,
        if_none_match: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve HTTP headers for a local document.

        Retrieves the HTTP headers containing minimal amount of information about the
        specified local document. Since the response body is empty, using the HEAD method
        is a lightweight way to check if the local document exists or not.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param str if_none_match: (optional) Header parameter for a conditional
               HTTP request not matching an ETag.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not db:
            raise ValueError('db must be provided')
        if not doc_id:
            raise ValueError('doc_id must be provided')
        headers = {
            'If-None-Match': if_none_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='head_local_document',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['db', 'doc_id']
        path_param_values = self.encode_path_vars(db, doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_local/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='HEAD',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_local_document(
        self,
        db: str,
        doc_id: str,
        *,
        batch: Optional[str] = None,
        **kwargs,
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

        if not db:
            raise ValueError('db must be provided')
        if not doc_id:
            raise ValueError('doc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_local_document',
        )
        headers.update(sdk_headers)

        params = {
            'batch': batch,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'doc_id']
        path_param_values = self.encode_path_vars(db, doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_local/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_local_document(
        self,
        db: str,
        doc_id: str,
        *,
        accept: Optional[str] = None,
        if_none_match: Optional[str] = None,
        attachments: Optional[bool] = None,
        att_encoding_info: Optional[bool] = None,
        local_seq: Optional[bool] = None,
        **kwargs,
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
        :param str if_none_match: (optional) Header parameter for a conditional
               HTTP request not matching an ETag.
        :param bool attachments: (optional) Query parameter to specify whether to
               include attachments bodies in a response.
        :param bool att_encoding_info: (optional) Query parameter to specify
               whether to include the encoding information in attachment stubs if the
               particular attachment is compressed.
        :param bool local_seq: (optional) Query parameter to specify whether to
               include the last update sequence for the document.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Document` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not doc_id:
            raise ValueError('doc_id must be provided')
        headers = {
            'Accept': accept,
            'If-None-Match': if_none_match,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_local_document',
        )
        headers.update(sdk_headers)

        params = {
            'attachments': attachments,
            'att_encoding_info': att_encoding_info,
            'local_seq': local_seq,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['db', 'doc_id']
        path_param_values = self.encode_path_vars(db, doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_local/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def put_local_document(
        self,
        db: str,
        doc_id: str,
        document: Union['Document', BinaryIO],
        *,
        content_type: Optional[str] = None,
        batch: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create or modify a local document.

        Stores the specified local document. The semantics are identical to storing a
        standard document in the specified database, except that the document is not
        replicated.

        :param str db: Path parameter to specify the database name.
        :param str doc_id: Path parameter to specify the document ID.
        :param Document document: HTTP request body for Document operations.
        :param str content_type: (optional) The type of the input.
        :param str batch: (optional) Query parameter to specify whether to store in
               batch mode. The server will respond with a HTTP 202 Accepted response code
               immediately.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentResult` object
        """

        if not db:
            raise ValueError('db must be provided')
        if not doc_id:
            raise ValueError('doc_id must be provided')
        if document is None:
            raise ValueError('document must be provided')
        if isinstance(document, Document):
            document = convert_model(document)
            content_type = content_type or 'application/json'
        headers = {
            'Content-Type': content_type,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='put_local_document',
        )
        headers.update(sdk_headers)

        params = {
            'batch': batch,
        }

        if isinstance(document, dict):
            data = json.dumps(document)
            if content_type is None:
                headers['Content-Type'] = 'application/json'
        else:
            data = document

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'doc_id']
        path_param_values = self.encode_path_vars(db, doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_local/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Database Details
    #########################

    def post_revs_diff(
        self,
        db: str,
        document_revisions: dict,
        **kwargs,
    ) -> DetailedResponse:
        """
        Query the document revisions and possible ancestors missing from the database.

        The replicator is the primary user of this operation. After receiving a set of new
        revision IDs from the source database, the replicator sends this set to the
        destination database's `_revs_diff` to find out which of them already exists
        there. It can then avoid fetching and sending already-known document bodies.

        :param str db: Path parameter to specify the database name.
        :param dict document_revisions: HTTP request body for operations with
               Document revisions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `dict` object
        """

        if not db:
            raise ValueError('db must be provided')
        if document_revisions is None:
            raise ValueError('document_revisions must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_revs_diff',
        )
        headers.update(sdk_headers)

        data = json.dumps(document_revisions)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_revs_diff'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_shards_information(
        self,
        db: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve shard information.

        List each shard range and the corresponding replicas for a specified database.

        :param str db: Path parameter to specify the database name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ShardsInformation` object
        """

        if not db:
            raise ValueError('db must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_shards_information',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db']
        path_param_values = self.encode_path_vars(db)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_shards'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_document_shards_info(
        self,
        db: str,
        doc_id: str,
        **kwargs,
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

        if not db:
            raise ValueError('db must be provided')
        if not doc_id:
            raise ValueError('doc_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_document_shards_info',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['db', 'doc_id']
        path_param_values = self.encode_path_vars(db, doc_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/{db}/_shards/{doc_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Monitoring
    #########################

    def head_up_information(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve HTTP headers about whether the server is up.

        Retrieves the HTTP headers about whether the server is up.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='head_up_information',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        url = '/_up'
        request = self.prepare_request(
            method='HEAD',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_active_tasks(
        self,
        **kwargs,
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
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_active_tasks',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_active_tasks'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_activity_tracker_events(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve Activity Tracker events information.

        Check event types that are being sent to IBM Cloud Activity Tracker for the IBM
        Cloudant instance.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ActivityTrackerEvents` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_activity_tracker_events',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_api/v2/user/activity_tracker/events'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def post_activity_tracker_events(
        self,
        types: List[str],
        **kwargs,
    ) -> DetailedResponse:
        """
        Modify Activity Tracker events configuration.

        Configure event types that are being sent to IBM Cloud Activity Tracker for the
        IBM Cloudant instance.

        :param List[str] types: An array of event types that are being sent to IBM
               Cloud Activity Tracker for the IBM Cloudant instance. "management" is a
               required element of this array.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ok` object
        """

        if types is None:
            raise ValueError('types must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='post_activity_tracker_events',
        )
        headers.update(sdk_headers)

        data = {
            'types': types,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_api/v2/user/activity_tracker/events'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_current_throughput_information(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve the current provisioned throughput capacity consumption.

        View the current consumption of provisioned throughput capacity for an IBM
        Cloudant instance. The current consumption shows the quantities of reads, writes,
        and global queries conducted against the instance for a given second.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CurrentThroughputInformation` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_current_throughput_information',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_api/v2/user/current/throughput'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_membership_information(
        self,
        **kwargs,
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
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_membership_information',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_membership'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_up_information(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve information about whether the server is up.

        Confirms that the server is up, running, and ready to respond to requests. If
        `maintenance_mode` is `true` or `nolb`, the endpoint returns a 404 response.
        **Tip:**  The authentication for this endpoint is only enforced when using IAM.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UpInformation` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_up_information',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/_up'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


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
    class Style(str, Enum):
        """
        Query parameter to specify how many revisions are returned in the changes array.
        The default, `main_only`, will only return the current "winning" revision;
        all_docs will return all leaf revisions (including conflicts and deleted former
        conflicts).
        """

        MAIN_ONLY = 'main_only'
        ALL_DOCS = 'all_docs'


class PostChangesAsStreamEnums:
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
    class Style(str, Enum):
        """
        Query parameter to specify how many revisions are returned in the changes array.
        The default, `main_only`, will only return the current "winning" revision;
        all_docs will return all leaf revisions (including conflicts and deleted former
        conflicts).
        """

        MAIN_ONLY = 'main_only'
        ALL_DOCS = 'all_docs'


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


class PostReplicatorEnums:
    """
    Enums for post_replicator parameters.
    """

    class Batch(str, Enum):
        """
        Query parameter to specify whether to store in batch mode. The server will respond
        with a HTTP 202 Accepted response code immediately.
        """

        OK = 'ok'


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


##############################################################################
# Models
##############################################################################


class ActiveTask:
    """
    Schema for information about a running task.

    :param int bulk_get_attempts: (optional) The total count of attempted doc
          revisions fetched with `_bulk_get`. Available for `replication` type tasks.
    :param int bulk_get_docs: (optional) The total count of successful docs fetched
          with `_bulk_get`. Available for `replication` type tasks.
    :param int changes_done: (optional) Processed changes. Available for
          `database_compaction`, `indexer`, `search_indexer`, `view_compaction` type
          tasks.
    :param int changes_pending: (optional) The count of changes not yet replicated.
          Available for `replication` type tasks.
    :param int checkpoint_interval: (optional) Specifies the checkpoint interval in
          ms. Available for `replication` type tasks.
    :param str checkpointed_source_seq: (optional) The source sequence id which was
          last successfully replicated. Available for `replication` type tasks.
    :param bool continuous: (optional) The replication configured to be continuous.
          Available for `replication` type tasks.
    :param str database: Source database.
    :param str design_document: (optional) The design document that belongs to this
          task. Available for `indexer`, `search_indexer`, `view_compaction` type tasks.
    :param str doc_id: (optional) Replication document ID. Available for
          `replication` type tasks.
    :param int doc_write_failures: (optional) Number of document write failures.
          Available for `replication` type tasks.
    :param int docs_read: (optional) Number of documents read. Available for
          `replication` type tasks.
    :param int docs_written: (optional) Number of documents written to target.
          Available for `replication` type tasks.
    :param str index: (optional) The search index that belongs to this task.
          Available for `search_indexer` type tasks.
    :param str indexer_pid: (optional) Indexer process ID. Available for `indexer`
          type tasks.
    :param int missing_revisions_found: (optional) The count of docs which have been
          read from the source. Available for `replication` type tasks.
    :param str node: Cluster node where the task is running.
    :param str phase: (optional) The phase the active task is in. `docid_sort`,
          `docid_copy`, `document_copy` phases are available for `database_compaction`,
          while `ids` and `view` phases are available for `view_compaction` type tasks.
    :param str pid: Process ID.
    :param str process_status: (optional) Process status.
    :param int progress: (optional) Current percentage progress. Available for
          `database_compaction`, `indexer`, `search_indexer`, `view_compaction` type
          tasks.
    :param str replication_id: (optional) Replication ID. Available for
          `replication` type tasks.
    :param bool retry: (optional) Indicates whether a compaction retry is currently
          running on the database. Available for `database_compaction` type tasks.
    :param int revisions_checked: (optional) The count of revisions which have been
          checked since this replication began. Available for `replication` type tasks.
    :param str source: (optional) Replication source. Available for `replication`
          type tasks.
    :param str source_seq: (optional) The last sequence number obtained from the
          source database changes feed. Available for `replication` type tasks.
    :param int started_on: Schema for a Unix epoch timestamp.
    :param str target: (optional) Replication target. Available for `replication`
          type tasks.
    :param str through_seq: (optional) The last sequence number processed by the
          replicator. Available for `replication` type tasks.
    :param int total_changes: (optional) Total changes to process. Available for
          `database_compaction`, `indexer`, `search_indexer`, `view_compaction` type
          tasks.
    :param str type: Operation type.
    :param int updated_on: Schema for a Unix epoch timestamp.
    :param str user: (optional) Name of user running the process.
    :param int view: (optional) Number of view indexes. Available for
          `view_compaction` type tasks.
    """

    def __init__(
        self,
        database: str,
        node: str,
        pid: str,
        started_on: int,
        type: str,
        updated_on: int,
        *,
        bulk_get_attempts: Optional[int] = None,
        bulk_get_docs: Optional[int] = None,
        changes_done: Optional[int] = None,
        changes_pending: Optional[int] = None,
        checkpoint_interval: Optional[int] = None,
        checkpointed_source_seq: Optional[str] = None,
        continuous: Optional[bool] = None,
        design_document: Optional[str] = None,
        doc_id: Optional[str] = None,
        doc_write_failures: Optional[int] = None,
        docs_read: Optional[int] = None,
        docs_written: Optional[int] = None,
        index: Optional[str] = None,
        indexer_pid: Optional[str] = None,
        missing_revisions_found: Optional[int] = None,
        phase: Optional[str] = None,
        process_status: Optional[str] = None,
        progress: Optional[int] = None,
        replication_id: Optional[str] = None,
        retry: Optional[bool] = None,
        revisions_checked: Optional[int] = None,
        source: Optional[str] = None,
        source_seq: Optional[str] = None,
        target: Optional[str] = None,
        through_seq: Optional[str] = None,
        total_changes: Optional[int] = None,
        user: Optional[str] = None,
        view: Optional[int] = None,
    ) -> None:
        """
        Initialize a ActiveTask object.

        :param str database: Source database.
        :param str node: Cluster node where the task is running.
        :param str pid: Process ID.
        :param int started_on: Schema for a Unix epoch timestamp.
        :param str type: Operation type.
        :param int updated_on: Schema for a Unix epoch timestamp.
        :param int bulk_get_attempts: (optional) The total count of attempted doc
               revisions fetched with `_bulk_get`. Available for `replication` type tasks.
        :param int bulk_get_docs: (optional) The total count of successful docs
               fetched with `_bulk_get`. Available for `replication` type tasks.
        :param int changes_done: (optional) Processed changes. Available for
               `database_compaction`, `indexer`, `search_indexer`, `view_compaction` type
               tasks.
        :param int changes_pending: (optional) The count of changes not yet
               replicated. Available for `replication` type tasks.
        :param int checkpoint_interval: (optional) Specifies the checkpoint
               interval in ms. Available for `replication` type tasks.
        :param str checkpointed_source_seq: (optional) The source sequence id which
               was last successfully replicated. Available for `replication` type tasks.
        :param bool continuous: (optional) The replication configured to be
               continuous. Available for `replication` type tasks.
        :param str design_document: (optional) The design document that belongs to
               this task. Available for `indexer`, `search_indexer`, `view_compaction`
               type tasks.
        :param str doc_id: (optional) Replication document ID. Available for
               `replication` type tasks.
        :param int doc_write_failures: (optional) Number of document write
               failures. Available for `replication` type tasks.
        :param int docs_read: (optional) Number of documents read. Available for
               `replication` type tasks.
        :param int docs_written: (optional) Number of documents written to target.
               Available for `replication` type tasks.
        :param str index: (optional) The search index that belongs to this task.
               Available for `search_indexer` type tasks.
        :param str indexer_pid: (optional) Indexer process ID. Available for
               `indexer` type tasks.
        :param int missing_revisions_found: (optional) The count of docs which have
               been read from the source. Available for `replication` type tasks.
        :param str phase: (optional) The phase the active task is in. `docid_sort`,
               `docid_copy`, `document_copy` phases are available for
               `database_compaction`, while `ids` and `view` phases are available for
               `view_compaction` type tasks.
        :param str process_status: (optional) Process status.
        :param int progress: (optional) Current percentage progress. Available for
               `database_compaction`, `indexer`, `search_indexer`, `view_compaction` type
               tasks.
        :param str replication_id: (optional) Replication ID. Available for
               `replication` type tasks.
        :param bool retry: (optional) Indicates whether a compaction retry is
               currently running on the database. Available for `database_compaction` type
               tasks.
        :param int revisions_checked: (optional) The count of revisions which have
               been checked since this replication began. Available for `replication` type
               tasks.
        :param str source: (optional) Replication source. Available for
               `replication` type tasks.
        :param str source_seq: (optional) The last sequence number obtained from
               the source database changes feed. Available for `replication` type tasks.
        :param str target: (optional) Replication target. Available for
               `replication` type tasks.
        :param str through_seq: (optional) The last sequence number processed by
               the replicator. Available for `replication` type tasks.
        :param int total_changes: (optional) Total changes to process. Available
               for `database_compaction`, `indexer`, `search_indexer`, `view_compaction`
               type tasks.
        :param str user: (optional) Name of user running the process.
        :param int view: (optional) Number of view indexes. Available for
               `view_compaction` type tasks.
        """
        self.bulk_get_attempts = bulk_get_attempts
        self.bulk_get_docs = bulk_get_docs
        self.changes_done = changes_done
        self.changes_pending = changes_pending
        self.checkpoint_interval = checkpoint_interval
        self.checkpointed_source_seq = checkpointed_source_seq
        self.continuous = continuous
        self.database = database
        self.design_document = design_document
        self.doc_id = doc_id
        self.doc_write_failures = doc_write_failures
        self.docs_read = docs_read
        self.docs_written = docs_written
        self.index = index
        self.indexer_pid = indexer_pid
        self.missing_revisions_found = missing_revisions_found
        self.node = node
        self.phase = phase
        self.pid = pid
        self.process_status = process_status
        self.progress = progress
        self.replication_id = replication_id
        self.retry = retry
        self.revisions_checked = revisions_checked
        self.source = source
        self.source_seq = source_seq
        self.started_on = started_on
        self.target = target
        self.through_seq = through_seq
        self.total_changes = total_changes
        self.type = type
        self.updated_on = updated_on
        self.user = user
        self.view = view

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActiveTask':
        """Initialize a ActiveTask object from a json dictionary."""
        args = {}
        if (bulk_get_attempts := _dict.get('bulk_get_attempts')) is not None:
            args['bulk_get_attempts'] = bulk_get_attempts
        if (bulk_get_docs := _dict.get('bulk_get_docs')) is not None:
            args['bulk_get_docs'] = bulk_get_docs
        if (changes_done := _dict.get('changes_done')) is not None:
            args['changes_done'] = changes_done
        if (changes_pending := _dict.get('changes_pending')) is not None:
            args['changes_pending'] = changes_pending
        if (checkpoint_interval := _dict.get('checkpoint_interval')) is not None:
            args['checkpoint_interval'] = checkpoint_interval
        if (checkpointed_source_seq := _dict.get('checkpointed_source_seq')) is not None:
            args['checkpointed_source_seq'] = checkpointed_source_seq
        if (continuous := _dict.get('continuous')) is not None:
            args['continuous'] = continuous
        if (database := _dict.get('database')) is not None:
            args['database'] = database
        else:
            raise ValueError('Required property \'database\' not present in ActiveTask JSON')
        if (design_document := _dict.get('design_document')) is not None:
            args['design_document'] = design_document
        if (doc_id := _dict.get('doc_id')) is not None:
            args['doc_id'] = doc_id
        if (doc_write_failures := _dict.get('doc_write_failures')) is not None:
            args['doc_write_failures'] = doc_write_failures
        if (docs_read := _dict.get('docs_read')) is not None:
            args['docs_read'] = docs_read
        if (docs_written := _dict.get('docs_written')) is not None:
            args['docs_written'] = docs_written
        if (index := _dict.get('index')) is not None:
            args['index'] = index
        if (indexer_pid := _dict.get('indexer_pid')) is not None:
            args['indexer_pid'] = indexer_pid
        if (missing_revisions_found := _dict.get('missing_revisions_found')) is not None:
            args['missing_revisions_found'] = missing_revisions_found
        if (node := _dict.get('node')) is not None:
            args['node'] = node
        else:
            raise ValueError('Required property \'node\' not present in ActiveTask JSON')
        if (phase := _dict.get('phase')) is not None:
            args['phase'] = phase
        if (pid := _dict.get('pid')) is not None:
            args['pid'] = pid
        else:
            raise ValueError('Required property \'pid\' not present in ActiveTask JSON')
        if (process_status := _dict.get('process_status')) is not None:
            args['process_status'] = process_status
        if (progress := _dict.get('progress')) is not None:
            args['progress'] = progress
        if (replication_id := _dict.get('replication_id')) is not None:
            args['replication_id'] = replication_id
        if (retry := _dict.get('retry')) is not None:
            args['retry'] = retry
        if (revisions_checked := _dict.get('revisions_checked')) is not None:
            args['revisions_checked'] = revisions_checked
        if (source := _dict.get('source')) is not None:
            args['source'] = source
        if (source_seq := _dict.get('source_seq')) is not None:
            args['source_seq'] = source_seq
        if (started_on := _dict.get('started_on')) is not None:
            args['started_on'] = started_on
        else:
            raise ValueError('Required property \'started_on\' not present in ActiveTask JSON')
        if (target := _dict.get('target')) is not None:
            args['target'] = target
        if (through_seq := _dict.get('through_seq')) is not None:
            args['through_seq'] = through_seq
        if (total_changes := _dict.get('total_changes')) is not None:
            args['total_changes'] = total_changes
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in ActiveTask JSON')
        if (updated_on := _dict.get('updated_on')) is not None:
            args['updated_on'] = updated_on
        else:
            raise ValueError('Required property \'updated_on\' not present in ActiveTask JSON')
        if (user := _dict.get('user')) is not None:
            args['user'] = user
        if (view := _dict.get('view')) is not None:
            args['view'] = view
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActiveTask object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'bulk_get_attempts') and self.bulk_get_attempts is not None:
            _dict['bulk_get_attempts'] = self.bulk_get_attempts
        if hasattr(self, 'bulk_get_docs') and self.bulk_get_docs is not None:
            _dict['bulk_get_docs'] = self.bulk_get_docs
        if hasattr(self, 'changes_done') and self.changes_done is not None:
            _dict['changes_done'] = self.changes_done
        if hasattr(self, 'changes_pending') and self.changes_pending is not None:
            _dict['changes_pending'] = self.changes_pending
        if hasattr(self, 'checkpoint_interval') and self.checkpoint_interval is not None:
            _dict['checkpoint_interval'] = self.checkpoint_interval
        if hasattr(self, 'checkpointed_source_seq') and self.checkpointed_source_seq is not None:
            _dict['checkpointed_source_seq'] = self.checkpointed_source_seq
        if hasattr(self, 'continuous') and self.continuous is not None:
            _dict['continuous'] = self.continuous
        if hasattr(self, 'database') and self.database is not None:
            _dict['database'] = self.database
        if hasattr(self, 'design_document') and self.design_document is not None:
            _dict['design_document'] = self.design_document
        if hasattr(self, 'doc_id') and self.doc_id is not None:
            _dict['doc_id'] = self.doc_id
        if hasattr(self, 'doc_write_failures') and self.doc_write_failures is not None:
            _dict['doc_write_failures'] = self.doc_write_failures
        if hasattr(self, 'docs_read') and self.docs_read is not None:
            _dict['docs_read'] = self.docs_read
        if hasattr(self, 'docs_written') and self.docs_written is not None:
            _dict['docs_written'] = self.docs_written
        if hasattr(self, 'index') and self.index is not None:
            _dict['index'] = self.index
        if hasattr(self, 'indexer_pid') and self.indexer_pid is not None:
            _dict['indexer_pid'] = self.indexer_pid
        if hasattr(self, 'missing_revisions_found') and self.missing_revisions_found is not None:
            _dict['missing_revisions_found'] = self.missing_revisions_found
        if hasattr(self, 'node') and self.node is not None:
            _dict['node'] = self.node
        if hasattr(self, 'phase') and self.phase is not None:
            _dict['phase'] = self.phase
        if hasattr(self, 'pid') and self.pid is not None:
            _dict['pid'] = self.pid
        if hasattr(self, 'process_status') and self.process_status is not None:
            _dict['process_status'] = self.process_status
        if hasattr(self, 'progress') and self.progress is not None:
            _dict['progress'] = self.progress
        if hasattr(self, 'replication_id') and self.replication_id is not None:
            _dict['replication_id'] = self.replication_id
        if hasattr(self, 'retry') and self.retry is not None:
            _dict['retry'] = self.retry
        if hasattr(self, 'revisions_checked') and self.revisions_checked is not None:
            _dict['revisions_checked'] = self.revisions_checked
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'source_seq') and self.source_seq is not None:
            _dict['source_seq'] = self.source_seq
        if hasattr(self, 'started_on') and self.started_on is not None:
            _dict['started_on'] = self.started_on
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target
        if hasattr(self, 'through_seq') and self.through_seq is not None:
            _dict['through_seq'] = self.through_seq
        if hasattr(self, 'total_changes') and self.total_changes is not None:
            _dict['total_changes'] = self.total_changes
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = self.updated_on
        if hasattr(self, 'user') and self.user is not None:
            _dict['user'] = self.user
        if hasattr(self, 'view') and self.view is not None:
            _dict['view'] = self.view
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

    class PhaseEnum(str, Enum):
        """
        The phase the active task is in. `docid_sort`, `docid_copy`, `document_copy`
        phases are available for `database_compaction`, while `ids` and `view` phases are
        available for `view_compaction` type tasks.
        """

        DOCID_SORT = 'docid_sort'
        DOCID_COPY = 'docid_copy'
        DOCUMENT_COPY = 'document_copy'
        IDS = 'ids'
        VIEW = 'view'


    class ProcessStatusEnum(str, Enum):
        """
        Process status.
        """

        EXITING = 'exiting'
        GARBAGE_COLLECTING = 'garbage_collecting'
        RUNNABLE = 'runnable'
        RUNNING = 'running'
        SUSPENDED = 'suspended'
        WAITING = 'waiting'


    class TypeEnum(str, Enum):
        """
        Operation type.
        """

        DATABASE_COMPACTION = 'database_compaction'
        INDEXER = 'indexer'
        REPLICATION = 'replication'
        SEARCH_INDEXER = 'search_indexer'
        VIEW_COMPACTION = 'view_compaction'



class ActivityTrackerEvents:
    """
    Schema for Activity Tracker events.

    :param List[str] types: An array of event types that are being sent to IBM Cloud
          Activity Tracker for the IBM Cloudant instance. "management" is a required
          element of this array.
    """

    def __init__(
        self,
        types: List[str],
    ) -> None:
        """
        Initialize a ActivityTrackerEvents object.

        :param List[str] types: An array of event types that are being sent to IBM
               Cloud Activity Tracker for the IBM Cloudant instance. "management" is a
               required element of this array.
        """
        self.types = types

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActivityTrackerEvents':
        """Initialize a ActivityTrackerEvents object from a json dictionary."""
        args = {}
        if (types := _dict.get('types')) is not None:
            args['types'] = types
        else:
            raise ValueError('Required property \'types\' not present in ActivityTrackerEvents JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActivityTrackerEvents object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = self.types
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ActivityTrackerEvents object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ActivityTrackerEvents') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ActivityTrackerEvents') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypesEnum(str, Enum):
        """
        types.
        """

        MANAGEMENT = 'management'
        DATA = 'data'



class AllDocsQueriesResult:
    """
    Schema for the result of an all documents queries operation.

    :param List[AllDocsResult] results: An array of result objects - one for each
          query. Each result object contains the same fields as the response to a regular
          `/_all_docs` request.
    """

    def __init__(
        self,
        results: List['AllDocsResult'],
    ) -> None:
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
        if (results := _dict.get('results')) is not None:
            args['results'] = [AllDocsResult.from_dict(v) for v in results]
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
            results_list = []
            for v in self.results:
                if isinstance(v, dict):
                    results_list.append(v)
                else:
                    results_list.append(v.to_dict())
            _dict['results'] = results_list
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


class AllDocsQuery:
    """
    Schema for an all documents query operation.

    :param bool att_encoding_info: (optional) Parameter to specify whether to
          include the encoding information in attachment stubs if the particular
          attachment is compressed.
    :param bool attachments: (optional) Parameter to specify whether to include
          attachments bodies in a response.
    :param bool conflicts: (optional) Parameter to specify whether to include a list
          of conflicted revisions in each returned document. Active only when
          `include_docs` is `true`.
    :param bool descending: (optional) Parameter to specify whether to return the
          documents in descending by key order.
    :param bool include_docs: (optional) Parameter to specify whether to include the
          full content of the documents in the response.
    :param bool inclusive_end: (optional) Parameter to specify whether the specified
          end key should be included in the result.
    :param int limit: (optional) Parameter to specify the number of returned
          documents to limit the result to.
    :param int skip: (optional) Parameter to specify the number of records before
          starting to return the results.
    :param bool update_seq: (optional) Parameter to specify whether to include in
          the response an update_seq value indicating the sequence id of the database the
          view reflects.
    :param str end_key: (optional) Schema for a document ID.
    :param str key: (optional) Schema for a document ID.
    :param List[str] keys: (optional) Schema for a list of document IDs.
    :param str start_key: (optional) Schema for a document ID.
    """

    def __init__(
        self,
        *,
        att_encoding_info: Optional[bool] = None,
        attachments: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        descending: Optional[bool] = None,
        include_docs: Optional[bool] = None,
        inclusive_end: Optional[bool] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        update_seq: Optional[bool] = None,
        end_key: Optional[str] = None,
        key: Optional[str] = None,
        keys: Optional[List[str]] = None,
        start_key: Optional[str] = None,
    ) -> None:
        """
        Initialize a AllDocsQuery object.

        :param bool att_encoding_info: (optional) Parameter to specify whether to
               include the encoding information in attachment stubs if the particular
               attachment is compressed.
        :param bool attachments: (optional) Parameter to specify whether to include
               attachments bodies in a response.
        :param bool conflicts: (optional) Parameter to specify whether to include a
               list of conflicted revisions in each returned document. Active only when
               `include_docs` is `true`.
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
        :param str end_key: (optional) Schema for a document ID.
        :param str key: (optional) Schema for a document ID.
        :param List[str] keys: (optional) Schema for a list of document IDs.
        :param str start_key: (optional) Schema for a document ID.
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
        self.end_key = end_key
        self.key = key
        self.keys = keys
        self.start_key = start_key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AllDocsQuery':
        """Initialize a AllDocsQuery object from a json dictionary."""
        args = {}
        if (att_encoding_info := _dict.get('att_encoding_info')) is not None:
            args['att_encoding_info'] = att_encoding_info
        if (attachments := _dict.get('attachments')) is not None:
            args['attachments'] = attachments
        if (conflicts := _dict.get('conflicts')) is not None:
            args['conflicts'] = conflicts
        if (descending := _dict.get('descending')) is not None:
            args['descending'] = descending
        if (include_docs := _dict.get('include_docs')) is not None:
            args['include_docs'] = include_docs
        if (inclusive_end := _dict.get('inclusive_end')) is not None:
            args['inclusive_end'] = inclusive_end
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        if (skip := _dict.get('skip')) is not None:
            args['skip'] = skip
        if (update_seq := _dict.get('update_seq')) is not None:
            args['update_seq'] = update_seq
        if (end_key := _dict.get('end_key')) is not None:
            args['end_key'] = end_key
        if (key := _dict.get('key')) is not None:
            args['key'] = key
        if (keys := _dict.get('keys')) is not None:
            args['keys'] = keys
        if (start_key := _dict.get('start_key')) is not None:
            args['start_key'] = start_key
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
        if hasattr(self, 'end_key') and self.end_key is not None:
            _dict['end_key'] = self.end_key
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self, 'keys') and self.keys is not None:
            _dict['keys'] = self.keys
        if hasattr(self, 'start_key') and self.start_key is not None:
            _dict['start_key'] = self.start_key
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


class AllDocsResult:
    """
    Schema for the result of an all documents operation.

    :param int total_rows: Total number of document results.
    :param List[DocsResultRow] rows: List of doc results.
    :param str update_seq: (optional) Current update sequence for the database.
    """

    def __init__(
        self,
        total_rows: int,
        rows: List['DocsResultRow'],
        *,
        update_seq: Optional[str] = None,
    ) -> None:
        """
        Initialize a AllDocsResult object.

        :param int total_rows: Total number of document results.
        :param List[DocsResultRow] rows: List of doc results.
        :param str update_seq: (optional) Current update sequence for the database.
        """
        self.total_rows = total_rows
        self.rows = rows
        self.update_seq = update_seq

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AllDocsResult':
        """Initialize a AllDocsResult object from a json dictionary."""
        args = {}
        if (total_rows := _dict.get('total_rows')) is not None:
            args['total_rows'] = total_rows
        else:
            raise ValueError('Required property \'total_rows\' not present in AllDocsResult JSON')
        if (rows := _dict.get('rows')) is not None:
            args['rows'] = [DocsResultRow.from_dict(v) for v in rows]
        else:
            raise ValueError('Required property \'rows\' not present in AllDocsResult JSON')
        if (update_seq := _dict.get('update_seq')) is not None:
            args['update_seq'] = update_seq
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
            rows_list = []
            for v in self.rows:
                if isinstance(v, dict):
                    rows_list.append(v)
                else:
                    rows_list.append(v.to_dict())
            _dict['rows'] = rows_list
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


class Analyzer:
    """
    Schema for a full text search analyzer.

    :param str name: Schema for the name of the Apache Lucene analyzer to use for
          text indexing. The default value varies depending on the analyzer usage:
          * For search indexes the default is `standard` * For query text indexes the
          default is `keyword` * For a query text index default_field the default is
          `standard`.
    :param List[str] stopwords: (optional) Custom stopwords to use with the named
          analyzer.
    """

    def __init__(
        self,
        name: str,
        *,
        stopwords: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a Analyzer object.

        :param str name: Schema for the name of the Apache Lucene analyzer to use
               for text indexing. The default value varies depending on the analyzer
               usage:
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
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in Analyzer JSON')
        if (stopwords := _dict.get('stopwords')) is not None:
            args['stopwords'] = stopwords
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



class AnalyzerConfiguration:
    """
    Schema for a search analyzer configuration.

    :param str name: Schema for the name of the Apache Lucene analyzer to use for
          text indexing. The default value varies depending on the analyzer usage:
          * For search indexes the default is `standard` * For query text indexes the
          default is `keyword` * For a query text index default_field the default is
          `standard`.
    :param List[str] stopwords: (optional) Custom stopwords to use with the named
          analyzer.
    :param dict fields: (optional) Schema for mapping a field name to a per field
          analyzer.
    """

    def __init__(
        self,
        name: str,
        *,
        stopwords: Optional[List[str]] = None,
        fields: Optional[dict] = None,
    ) -> None:
        """
        Initialize a AnalyzerConfiguration object.

        :param str name: Schema for the name of the Apache Lucene analyzer to use
               for text indexing. The default value varies depending on the analyzer
               usage:
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
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in AnalyzerConfiguration JSON')
        if (stopwords := _dict.get('stopwords')) is not None:
            args['stopwords'] = stopwords
        if (fields := _dict.get('fields')) is not None:
            args['fields'] = {k: Analyzer.from_dict(v) for k, v in fields.items()}
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
            fields_map = {}
            for k, v in self.fields.items():
                if isinstance(v, dict):
                    fields_map[k] = v
                else:
                    fields_map[k] = v.to_dict()
            _dict['fields'] = fields_map
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



class ApiKeysResult:
    """
    Schema for api keys.

    :param bool ok: ok.
    :param str key: The generated api key.
    :param str password: The password associated with the api key.
    """

    def __init__(
        self,
        ok: bool,
        key: str,
        password: str,
    ) -> None:
        """
        Initialize a ApiKeysResult object.

        :param bool ok: ok.
        :param str key: The generated api key.
        :param str password: The password associated with the api key.
        """
        self.ok = ok
        self.key = key
        self.password = password

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiKeysResult':
        """Initialize a ApiKeysResult object from a json dictionary."""
        args = {}
        if (ok := _dict.get('ok')) is not None:
            args['ok'] = ok
        else:
            raise ValueError('Required property \'ok\' not present in ApiKeysResult JSON')
        if (key := _dict.get('key')) is not None:
            args['key'] = key
        else:
            raise ValueError('Required property \'key\' not present in ApiKeysResult JSON')
        if (password := _dict.get('password')) is not None:
            args['password'] = password
        else:
            raise ValueError('Required property \'password\' not present in ApiKeysResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiKeysResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ok') and self.ok is not None:
            _dict['ok'] = self.ok
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
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


class Attachment:
    """
    Schema for an attachment.

    :param str content_type: (optional) Attachment MIME type.
    :param bytes data: (optional) Base64-encoded content. Available if attachment
          content is requested by using the query parameters `attachments=true` or
          `atts_since`. Note that when used with a view or changes feed `include_docs`
          must also be `true`.
    :param str digest: (optional) Content hash digest. It starts with prefix which
          announce hash type (e.g. `md5-`) and continues with Base64-encoded hash digest.
    :param int encoded_length: (optional) Compressed attachment size in bytes.
          Available if content_type was in list of compressible types when the attachment
          was added and the query parameter `att_encoding_info` is `true`. Note that when
          used with a view or changes feed `include_docs` must also be `true`.
    :param str encoding: (optional) Compression codec. Available if content_type was
          in list of compressible types when the attachment was added and the and the
          query parameter `att_encoding_info` is `true`. Note that when used with a view
          or changes feed `include_docs` must also be `true`.
    :param bool follows: (optional) True if the attachment follows in a multipart
          request or response.
    :param int length: (optional) Real attachment size in bytes. Not available if
          inline attachment content requested.
    :param int revpos: (optional) Revision number when attachment was added.
    :param bool stub: (optional) Has `true` value if object contains stub info and
          no content. Otherwise omitted in response.
    """

    def __init__(
        self,
        *,
        content_type: Optional[str] = None,
        data: Optional[bytes] = None,
        digest: Optional[str] = None,
        encoded_length: Optional[int] = None,
        encoding: Optional[str] = None,
        follows: Optional[bool] = None,
        length: Optional[int] = None,
        revpos: Optional[int] = None,
        stub: Optional[bool] = None,
    ) -> None:
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
        if (content_type := _dict.get('content_type')) is not None:
            args['content_type'] = content_type
        if (data := _dict.get('data')) is not None:
            args['data'] = base64.b64decode(data)
        if (digest := _dict.get('digest')) is not None:
            args['digest'] = digest
        if (encoded_length := _dict.get('encoded_length')) is not None:
            args['encoded_length'] = encoded_length
        if (encoding := _dict.get('encoding')) is not None:
            args['encoding'] = encoding
        if (follows := _dict.get('follows')) is not None:
            args['follows'] = follows
        if (length := _dict.get('length')) is not None:
            args['length'] = length
        if (revpos := _dict.get('revpos')) is not None:
            args['revpos'] = revpos
        if (stub := _dict.get('stub')) is not None:
            args['stub'] = stub
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


class BulkDocs:
    """
    Schema for submitting documents for bulk modifications.

    :param List[Document] docs: Array of documents.
    :param bool new_edits: (optional) If `false`, prevents the database from
          assigning them new revision IDs. Default is `true`.
          Avoid using this parameter, since this option applies document revisions without
          checking for conflicts, so it is very easy to accidentally end up with a large
          number of conflicts.
    """

    def __init__(
        self,
        docs: List['Document'],
        *,
        new_edits: Optional[bool] = None,
    ) -> None:
        """
        Initialize a BulkDocs object.

        :param List[Document] docs: Array of documents.
        :param bool new_edits: (optional) If `false`, prevents the database from
               assigning them new revision IDs. Default is `true`.
               Avoid using this parameter, since this option applies document revisions
               without checking for conflicts, so it is very easy to accidentally end up
               with a large number of conflicts.
        """
        self.docs = docs
        self.new_edits = new_edits

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BulkDocs':
        """Initialize a BulkDocs object from a json dictionary."""
        args = {}
        if (docs := _dict.get('docs')) is not None:
            args['docs'] = [Document.from_dict(v) for v in docs]
        else:
            raise ValueError('Required property \'docs\' not present in BulkDocs JSON')
        if (new_edits := _dict.get('new_edits')) is not None:
            args['new_edits'] = new_edits
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BulkDocs object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'docs') and self.docs is not None:
            docs_list = []
            for v in self.docs:
                if isinstance(v, dict):
                    docs_list.append(v)
                else:
                    docs_list.append(v.to_dict())
            _dict['docs'] = docs_list
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


class BulkGetQueryDocument:
    """
    Schema for a document item in a bulk get query.

    :param List[str] atts_since: (optional) Includes attachments only since
          specified revisions.
    :param str id: Schema for a document ID.
    :param str rev: (optional) Schema for a document revision identifier.
    """

    def __init__(
        self,
        id: str,
        *,
        atts_since: Optional[List[str]] = None,
        rev: Optional[str] = None,
    ) -> None:
        """
        Initialize a BulkGetQueryDocument object.

        :param str id: Schema for a document ID.
        :param List[str] atts_since: (optional) Includes attachments only since
               specified revisions.
        :param str rev: (optional) Schema for a document revision identifier.
        """
        self.atts_since = atts_since
        self.id = id
        self.rev = rev

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BulkGetQueryDocument':
        """Initialize a BulkGetQueryDocument object from a json dictionary."""
        args = {}
        if (atts_since := _dict.get('atts_since')) is not None:
            args['atts_since'] = atts_since
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in BulkGetQueryDocument JSON')
        if (rev := _dict.get('rev')) is not None:
            args['rev'] = rev
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


class BulkGetResult:
    """
    Schema for the results object of a bulk get operation.

    :param List[BulkGetResultItem] results: Results.
    """

    def __init__(
        self,
        results: List['BulkGetResultItem'],
    ) -> None:
        """
        Initialize a BulkGetResult object.

        :param List[BulkGetResultItem] results: Results.
        """
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BulkGetResult':
        """Initialize a BulkGetResult object from a json dictionary."""
        args = {}
        if (results := _dict.get('results')) is not None:
            args['results'] = [BulkGetResultItem.from_dict(v) for v in results]
        else:
            raise ValueError('Required property \'results\' not present in BulkGetResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BulkGetResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'results') and self.results is not None:
            results_list = []
            for v in self.results:
                if isinstance(v, dict):
                    results_list.append(v)
                else:
                    results_list.append(v.to_dict())
            _dict['results'] = results_list
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


class BulkGetResultDocument:
    """
    Schema for BulkGetResult object containing a successfully retrieved document or error
    information.

    :param DocumentResult error: (optional) Schema for the result of a document
          modification.
    :param Document ok: (optional) Schema for a document.
    """

    def __init__(
        self,
        *,
        error: Optional['DocumentResult'] = None,
        ok: Optional['Document'] = None,
    ) -> None:
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
        if (error := _dict.get('error')) is not None:
            args['error'] = DocumentResult.from_dict(error)
        if (ok := _dict.get('ok')) is not None:
            args['ok'] = Document.from_dict(ok)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BulkGetResultDocument object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'error') and self.error is not None:
            if isinstance(self.error, dict):
                _dict['error'] = self.error
            else:
                _dict['error'] = self.error.to_dict()
        if hasattr(self, 'ok') and self.ok is not None:
            if isinstance(self.ok, dict):
                _dict['ok'] = self.ok
            else:
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


class BulkGetResultItem:
    """
    Schema for the document revisions information from a bulk get operation.

    :param List[BulkGetResultDocument] docs: Array of document revisions or error
          information.
    :param str id: Schema for a document ID.
    """

    def __init__(
        self,
        docs: List['BulkGetResultDocument'],
        id: str,
    ) -> None:
        """
        Initialize a BulkGetResultItem object.

        :param List[BulkGetResultDocument] docs: Array of document revisions or
               error information.
        :param str id: Schema for a document ID.
        """
        self.docs = docs
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BulkGetResultItem':
        """Initialize a BulkGetResultItem object from a json dictionary."""
        args = {}
        if (docs := _dict.get('docs')) is not None:
            args['docs'] = [BulkGetResultDocument.from_dict(v) for v in docs]
        else:
            raise ValueError('Required property \'docs\' not present in BulkGetResultItem JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in BulkGetResultItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BulkGetResultItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'docs') and self.docs is not None:
            docs_list = []
            for v in self.docs:
                if isinstance(v, dict):
                    docs_list.append(v)
                else:
                    docs_list.append(v.to_dict())
            _dict['docs'] = docs_list
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


class CapacityThroughputInformation:
    """
    Schema for information about the currently provisioned and target throughput capacity.

    :param CapacityThroughputInformationCurrent current: Detailed information about
          provisioned throughput capacity.
    :param CapacityThroughputInformationTarget target: (optional) Detailed
          information about target throughput capacity.
    """

    def __init__(
        self,
        current: 'CapacityThroughputInformationCurrent',
        *,
        target: Optional['CapacityThroughputInformationTarget'] = None,
    ) -> None:
        """
        Initialize a CapacityThroughputInformation object.

        :param CapacityThroughputInformationCurrent current: Detailed information
               about provisioned throughput capacity.
        :param CapacityThroughputInformationTarget target: (optional) Detailed
               information about target throughput capacity.
        """
        self.current = current
        self.target = target

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CapacityThroughputInformation':
        """Initialize a CapacityThroughputInformation object from a json dictionary."""
        args = {}
        if (current := _dict.get('current')) is not None:
            args['current'] = CapacityThroughputInformationCurrent.from_dict(current)
        else:
            raise ValueError('Required property \'current\' not present in CapacityThroughputInformation JSON')
        if (target := _dict.get('target')) is not None:
            args['target'] = CapacityThroughputInformationTarget.from_dict(target)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CapacityThroughputInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'current') and self.current is not None:
            if isinstance(self.current, dict):
                _dict['current'] = self.current
            else:
                _dict['current'] = self.current.to_dict()
        if hasattr(self, 'target') and self.target is not None:
            if isinstance(self.target, dict):
                _dict['target'] = self.target
            else:
                _dict['target'] = self.target.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CapacityThroughputInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CapacityThroughputInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CapacityThroughputInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CapacityThroughputInformationCurrent:
    """
    Detailed information about provisioned throughput capacity.

    :param ThroughputInformation throughput: Schema for detailed information about
          throughput capacity with breakdown by specific throughput requests classes.
    """

    def __init__(
        self,
        throughput: 'ThroughputInformation',
    ) -> None:
        """
        Initialize a CapacityThroughputInformationCurrent object.

        :param ThroughputInformation throughput: Schema for detailed information
               about throughput capacity with breakdown by specific throughput requests
               classes.
        """
        self.throughput = throughput

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CapacityThroughputInformationCurrent':
        """Initialize a CapacityThroughputInformationCurrent object from a json dictionary."""
        args = {}
        if (throughput := _dict.get('throughput')) is not None:
            args['throughput'] = ThroughputInformation.from_dict(throughput)
        else:
            raise ValueError('Required property \'throughput\' not present in CapacityThroughputInformationCurrent JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CapacityThroughputInformationCurrent object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'throughput') and self.throughput is not None:
            if isinstance(self.throughput, dict):
                _dict['throughput'] = self.throughput
            else:
                _dict['throughput'] = self.throughput.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CapacityThroughputInformationCurrent object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CapacityThroughputInformationCurrent') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CapacityThroughputInformationCurrent') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CapacityThroughputInformationTarget:
    """
    Detailed information about target throughput capacity.

    :param ThroughputInformation throughput: Schema for detailed information about
          throughput capacity with breakdown by specific throughput requests classes.
    """

    def __init__(
        self,
        throughput: 'ThroughputInformation',
    ) -> None:
        """
        Initialize a CapacityThroughputInformationTarget object.

        :param ThroughputInformation throughput: Schema for detailed information
               about throughput capacity with breakdown by specific throughput requests
               classes.
        """
        self.throughput = throughput

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CapacityThroughputInformationTarget':
        """Initialize a CapacityThroughputInformationTarget object from a json dictionary."""
        args = {}
        if (throughput := _dict.get('throughput')) is not None:
            args['throughput'] = ThroughputInformation.from_dict(throughput)
        else:
            raise ValueError('Required property \'throughput\' not present in CapacityThroughputInformationTarget JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CapacityThroughputInformationTarget object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'throughput') and self.throughput is not None:
            if isinstance(self.throughput, dict):
                _dict['throughput'] = self.throughput
            else:
                _dict['throughput'] = self.throughput.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CapacityThroughputInformationTarget object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CapacityThroughputInformationTarget') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CapacityThroughputInformationTarget') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Change:
    """
    Schema for a document leaf with single field rev.

    :param str rev: Schema for a document revision identifier.
    """

    def __init__(
        self,
        rev: str,
    ) -> None:
        """
        Initialize a Change object.

        :param str rev: Schema for a document revision identifier.
        """
        self.rev = rev

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Change':
        """Initialize a Change object from a json dictionary."""
        args = {}
        if (rev := _dict.get('rev')) is not None:
            args['rev'] = rev
        else:
            raise ValueError('Required property \'rev\' not present in Change JSON')
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


class ChangesResult:
    """
    Schema for normal changes feed result.

    :param str last_seq: last_seq.
    :param int pending: pending.
    :param List[ChangesResultItem] results: results.
    """

    def __init__(
        self,
        last_seq: str,
        pending: int,
        results: List['ChangesResultItem'],
    ) -> None:
        """
        Initialize a ChangesResult object.

        :param str last_seq: last_seq.
        :param int pending: pending.
        :param List[ChangesResultItem] results: results.
        """
        self.last_seq = last_seq
        self.pending = pending
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ChangesResult':
        """Initialize a ChangesResult object from a json dictionary."""
        args = {}
        if (last_seq := _dict.get('last_seq')) is not None:
            args['last_seq'] = last_seq
        else:
            raise ValueError('Required property \'last_seq\' not present in ChangesResult JSON')
        if (pending := _dict.get('pending')) is not None:
            args['pending'] = pending
        else:
            raise ValueError('Required property \'pending\' not present in ChangesResult JSON')
        if (results := _dict.get('results')) is not None:
            args['results'] = [ChangesResultItem.from_dict(v) for v in results]
        else:
            raise ValueError('Required property \'results\' not present in ChangesResult JSON')
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
            results_list = []
            for v in self.results:
                if isinstance(v, dict):
                    results_list.append(v)
                else:
                    results_list.append(v.to_dict())
            _dict['results'] = results_list
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


class ChangesResultItem:
    """
    Schema for an item in the changes results array.

    :param List[Change] changes: List of document's leaves with single field rev.
    :param bool deleted: (optional) if `true` then the document is deleted.
    :param Document doc: (optional) Schema for a document.
    :param str id: Schema for a document ID.
    :param str seq: Update sequence.
    """

    def __init__(
        self,
        changes: List['Change'],
        id: str,
        seq: str,
        *,
        deleted: Optional[bool] = None,
        doc: Optional['Document'] = None,
    ) -> None:
        """
        Initialize a ChangesResultItem object.

        :param List[Change] changes: List of document's leaves with single field
               rev.
        :param str id: Schema for a document ID.
        :param str seq: Update sequence.
        :param bool deleted: (optional) if `true` then the document is deleted.
        :param Document doc: (optional) Schema for a document.
        """
        self.changes = changes
        self.deleted = deleted
        self.doc = doc
        self.id = id
        self.seq = seq

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ChangesResultItem':
        """Initialize a ChangesResultItem object from a json dictionary."""
        args = {}
        if (changes := _dict.get('changes')) is not None:
            args['changes'] = [Change.from_dict(v) for v in changes]
        else:
            raise ValueError('Required property \'changes\' not present in ChangesResultItem JSON')
        if (deleted := _dict.get('deleted')) is not None:
            args['deleted'] = deleted
        if (doc := _dict.get('doc')) is not None:
            args['doc'] = Document.from_dict(doc)
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in ChangesResultItem JSON')
        if (seq := _dict.get('seq')) is not None:
            args['seq'] = seq
        else:
            raise ValueError('Required property \'seq\' not present in ChangesResultItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ChangesResultItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'changes') and self.changes is not None:
            changes_list = []
            for v in self.changes:
                if isinstance(v, dict):
                    changes_list.append(v)
                else:
                    changes_list.append(v.to_dict())
            _dict['changes'] = changes_list
        if hasattr(self, 'deleted') and self.deleted is not None:
            _dict['deleted'] = self.deleted
        if hasattr(self, 'doc') and self.doc is not None:
            if isinstance(self.doc, dict):
                _dict['doc'] = self.doc
            else:
                _dict['doc'] = self.doc.to_dict()
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


class ContentInformationSizes:
    """
    Schema for size information of content.

    :param int active: The active size of the content, in bytes.
    :param int external: The total uncompressed size of the content, in bytes.
    :param int file: The total size of the content as stored on disk, in bytes.
    """

    def __init__(
        self,
        active: int,
        external: int,
        file: int,
    ) -> None:
        """
        Initialize a ContentInformationSizes object.

        :param int active: The active size of the content, in bytes.
        :param int external: The total uncompressed size of the content, in bytes.
        :param int file: The total size of the content as stored on disk, in bytes.
        """
        self.active = active
        self.external = external
        self.file = file

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContentInformationSizes':
        """Initialize a ContentInformationSizes object from a json dictionary."""
        args = {}
        if (active := _dict.get('active')) is not None:
            args['active'] = active
        else:
            raise ValueError('Required property \'active\' not present in ContentInformationSizes JSON')
        if (external := _dict.get('external')) is not None:
            args['external'] = external
        else:
            raise ValueError('Required property \'external\' not present in ContentInformationSizes JSON')
        if (file := _dict.get('file')) is not None:
            args['file'] = file
        else:
            raise ValueError('Required property \'file\' not present in ContentInformationSizes JSON')
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


class CorsInformation:
    """
    Schema for information about the CORS configuration.

    :param bool allow_credentials: Boolean value to allow authentication
          credentials. If set to true, browser requests must be done by using
          withCredentials = true.
    :param bool enable_cors: Boolean value to turn CORS on and off.
    :param List[str] origins: An array of strings that contain allowed origin
          domains. You have to specify the full URL including the protocol. It is
          recommended that only the HTTPS protocol is used. Subdomains count as separate
          domains, so you have to specify all subdomains used.
    """

    def __init__(
        self,
        allow_credentials: bool,
        enable_cors: bool,
        origins: List[str],
    ) -> None:
        """
        Initialize a CorsInformation object.

        :param bool allow_credentials: Boolean value to allow authentication
               credentials. If set to true, browser requests must be done by using
               withCredentials = true.
        :param bool enable_cors: Boolean value to turn CORS on and off.
        :param List[str] origins: An array of strings that contain allowed origin
               domains. You have to specify the full URL including the protocol. It is
               recommended that only the HTTPS protocol is used. Subdomains count as
               separate domains, so you have to specify all subdomains used.
        """
        self.allow_credentials = allow_credentials
        self.enable_cors = enable_cors
        self.origins = origins

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CorsInformation':
        """Initialize a CorsInformation object from a json dictionary."""
        args = {}
        if (allow_credentials := _dict.get('allow_credentials')) is not None:
            args['allow_credentials'] = allow_credentials
        else:
            raise ValueError('Required property \'allow_credentials\' not present in CorsInformation JSON')
        if (enable_cors := _dict.get('enable_cors')) is not None:
            args['enable_cors'] = enable_cors
        else:
            raise ValueError('Required property \'enable_cors\' not present in CorsInformation JSON')
        if (origins := _dict.get('origins')) is not None:
            args['origins'] = origins
        else:
            raise ValueError('Required property \'origins\' not present in CorsInformation JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CorsInformation object from a json dictionary."""
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
        """Return a `str` version of this CorsInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CorsInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CorsInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CurrentThroughputInformation:
    """
    Schema for information about current consumption of a provisioned throughput capacity.

    :param CurrentThroughputInformationThroughput throughput: Detailed information
          about current consumption.
    """

    def __init__(
        self,
        throughput: 'CurrentThroughputInformationThroughput',
    ) -> None:
        """
        Initialize a CurrentThroughputInformation object.

        :param CurrentThroughputInformationThroughput throughput: Detailed
               information about current consumption.
        """
        self.throughput = throughput

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CurrentThroughputInformation':
        """Initialize a CurrentThroughputInformation object from a json dictionary."""
        args = {}
        if (throughput := _dict.get('throughput')) is not None:
            args['throughput'] = CurrentThroughputInformationThroughput.from_dict(throughput)
        else:
            raise ValueError('Required property \'throughput\' not present in CurrentThroughputInformation JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CurrentThroughputInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'throughput') and self.throughput is not None:
            if isinstance(self.throughput, dict):
                _dict['throughput'] = self.throughput
            else:
                _dict['throughput'] = self.throughput.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CurrentThroughputInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CurrentThroughputInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CurrentThroughputInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CurrentThroughputInformationThroughput:
    """
    Detailed information about current consumption.

    :param int query: Number of global queries conducted against the instance for a
          given second.
    :param int read: Number of reads conducted against the instance for a given
          second.
    :param int write: Number of writes conducted against the instance for a given
          second.
    """

    def __init__(
        self,
        query: int,
        read: int,
        write: int,
    ) -> None:
        """
        Initialize a CurrentThroughputInformationThroughput object.

        :param int query: Number of global queries conducted against the instance
               for a given second.
        :param int read: Number of reads conducted against the instance for a given
               second.
        :param int write: Number of writes conducted against the instance for a
               given second.
        """
        self.query = query
        self.read = read
        self.write = write

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CurrentThroughputInformationThroughput':
        """Initialize a CurrentThroughputInformationThroughput object from a json dictionary."""
        args = {}
        if (query := _dict.get('query')) is not None:
            args['query'] = query
        else:
            raise ValueError('Required property \'query\' not present in CurrentThroughputInformationThroughput JSON')
        if (read := _dict.get('read')) is not None:
            args['read'] = read
        else:
            raise ValueError('Required property \'read\' not present in CurrentThroughputInformationThroughput JSON')
        if (write := _dict.get('write')) is not None:
            args['write'] = write
        else:
            raise ValueError('Required property \'write\' not present in CurrentThroughputInformationThroughput JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CurrentThroughputInformationThroughput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'query') and self.query is not None:
            _dict['query'] = self.query
        if hasattr(self, 'read') and self.read is not None:
            _dict['read'] = self.read
        if hasattr(self, 'write') and self.write is not None:
            _dict['write'] = self.write
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CurrentThroughputInformationThroughput object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CurrentThroughputInformationThroughput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CurrentThroughputInformationThroughput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DatabaseInformation:
    """
    Schema for information about a database.

    :param DatabaseInformationCluster cluster: Schema for database cluster
          information.
    :param str committed_update_seq: (optional) An opaque string that describes the
          committed state of the database.
    :param bool compact_running: True if the database compaction routine is
          operating on this database.
    :param str compacted_seq: (optional) An opaque string that describes the
          compaction state of the database.
    :param str db_name: Schema for a database name.
    :param int disk_format_version: The version of the physical format used for the
          data when it is stored on disk.
    :param int doc_count: A count of the documents in the specified database.
    :param int doc_del_count: Number of deleted documents.
    :param str engine: (optional) The engine used for the database.
    :param str instance_start_time: An opaque string to detect whether a database
          has been recreated. The field name is for compatibility with old replicator
          versions. Do not use the value to infer timing infromation. Typically only used
          by replicators.
    :param PartitionedIndexesInformation partitioned_indexes: (optional) Information
          about database's partitioned indexes.
    :param DatabaseInformationProps props: Schema for database properties.
    :param ContentInformationSizes sizes: Schema for size information of content.
    :param str update_seq: An opaque string that describes the state of the
          database. Do not rely on this string for counting the number of updates.
    :param str uuid: (optional) The UUID of the database.
    """

    def __init__(
        self,
        cluster: 'DatabaseInformationCluster',
        compact_running: bool,
        db_name: str,
        disk_format_version: int,
        doc_count: int,
        doc_del_count: int,
        instance_start_time: str,
        props: 'DatabaseInformationProps',
        sizes: 'ContentInformationSizes',
        update_seq: str,
        *,
        committed_update_seq: Optional[str] = None,
        compacted_seq: Optional[str] = None,
        engine: Optional[str] = None,
        partitioned_indexes: Optional['PartitionedIndexesInformation'] = None,
        uuid: Optional[str] = None,
    ) -> None:
        """
        Initialize a DatabaseInformation object.

        :param DatabaseInformationCluster cluster: Schema for database cluster
               information.
        :param bool compact_running: True if the database compaction routine is
               operating on this database.
        :param str db_name: Schema for a database name.
        :param int disk_format_version: The version of the physical format used for
               the data when it is stored on disk.
        :param int doc_count: A count of the documents in the specified database.
        :param int doc_del_count: Number of deleted documents.
        :param str instance_start_time: An opaque string to detect whether a
               database has been recreated. The field name is for compatibility with old
               replicator versions. Do not use the value to infer timing infromation.
               Typically only used by replicators.
        :param DatabaseInformationProps props: Schema for database properties.
        :param ContentInformationSizes sizes: Schema for size information of
               content.
        :param str update_seq: An opaque string that describes the state of the
               database. Do not rely on this string for counting the number of updates.
        :param str committed_update_seq: (optional) An opaque string that describes
               the committed state of the database.
        :param str compacted_seq: (optional) An opaque string that describes the
               compaction state of the database.
        :param str engine: (optional) The engine used for the database.
        :param PartitionedIndexesInformation partitioned_indexes: (optional)
               Information about database's partitioned indexes.
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
        self.instance_start_time = instance_start_time
        self.partitioned_indexes = partitioned_indexes
        self.props = props
        self.sizes = sizes
        self.update_seq = update_seq
        self.uuid = uuid

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DatabaseInformation':
        """Initialize a DatabaseInformation object from a json dictionary."""
        args = {}
        if (cluster := _dict.get('cluster')) is not None:
            args['cluster'] = DatabaseInformationCluster.from_dict(cluster)
        else:
            raise ValueError('Required property \'cluster\' not present in DatabaseInformation JSON')
        if (committed_update_seq := _dict.get('committed_update_seq')) is not None:
            args['committed_update_seq'] = committed_update_seq
        if (compact_running := _dict.get('compact_running')) is not None:
            args['compact_running'] = compact_running
        else:
            raise ValueError('Required property \'compact_running\' not present in DatabaseInformation JSON')
        if (compacted_seq := _dict.get('compacted_seq')) is not None:
            args['compacted_seq'] = compacted_seq
        if (db_name := _dict.get('db_name')) is not None:
            args['db_name'] = db_name
        else:
            raise ValueError('Required property \'db_name\' not present in DatabaseInformation JSON')
        if (disk_format_version := _dict.get('disk_format_version')) is not None:
            args['disk_format_version'] = disk_format_version
        else:
            raise ValueError('Required property \'disk_format_version\' not present in DatabaseInformation JSON')
        if (doc_count := _dict.get('doc_count')) is not None:
            args['doc_count'] = doc_count
        else:
            raise ValueError('Required property \'doc_count\' not present in DatabaseInformation JSON')
        if (doc_del_count := _dict.get('doc_del_count')) is not None:
            args['doc_del_count'] = doc_del_count
        else:
            raise ValueError('Required property \'doc_del_count\' not present in DatabaseInformation JSON')
        if (engine := _dict.get('engine')) is not None:
            args['engine'] = engine
        if (instance_start_time := _dict.get('instance_start_time')) is not None:
            args['instance_start_time'] = instance_start_time
        else:
            raise ValueError('Required property \'instance_start_time\' not present in DatabaseInformation JSON')
        if (partitioned_indexes := _dict.get('partitioned_indexes')) is not None:
            args['partitioned_indexes'] = PartitionedIndexesInformation.from_dict(partitioned_indexes)
        if (props := _dict.get('props')) is not None:
            args['props'] = DatabaseInformationProps.from_dict(props)
        else:
            raise ValueError('Required property \'props\' not present in DatabaseInformation JSON')
        if (sizes := _dict.get('sizes')) is not None:
            args['sizes'] = ContentInformationSizes.from_dict(sizes)
        else:
            raise ValueError('Required property \'sizes\' not present in DatabaseInformation JSON')
        if (update_seq := _dict.get('update_seq')) is not None:
            args['update_seq'] = update_seq
        else:
            raise ValueError('Required property \'update_seq\' not present in DatabaseInformation JSON')
        if (uuid := _dict.get('uuid')) is not None:
            args['uuid'] = uuid
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DatabaseInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cluster') and self.cluster is not None:
            if isinstance(self.cluster, dict):
                _dict['cluster'] = self.cluster
            else:
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
        if hasattr(self, 'instance_start_time') and self.instance_start_time is not None:
            _dict['instance_start_time'] = self.instance_start_time
        if hasattr(self, 'partitioned_indexes') and self.partitioned_indexes is not None:
            if isinstance(self.partitioned_indexes, dict):
                _dict['partitioned_indexes'] = self.partitioned_indexes
            else:
                _dict['partitioned_indexes'] = self.partitioned_indexes.to_dict()
        if hasattr(self, 'props') and self.props is not None:
            if isinstance(self.props, dict):
                _dict['props'] = self.props
            else:
                _dict['props'] = self.props.to_dict()
        if hasattr(self, 'sizes') and self.sizes is not None:
            if isinstance(self.sizes, dict):
                _dict['sizes'] = self.sizes
            else:
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


class DatabaseInformationCluster:
    """
    Schema for database cluster information.

    :param int n: Schema for the number of replicas of a database in a cluster. The
          cluster is using the default value and it cannot be changed by the user.
    :param int q: Schema for the number of shards in a database. Each shard is a
          partition of the hash value range.
    :param int r: Read quorum. The number of consistent copies of a document that
          need to be read before a successful reply.
    :param int w: Write quorum. The number of copies of a document that need to be
          written before a successful reply.
    """

    def __init__(
        self,
        n: int,
        q: int,
        r: int,
        w: int,
    ) -> None:
        """
        Initialize a DatabaseInformationCluster object.

        :param int n: Schema for the number of replicas of a database in a cluster.
               The cluster is using the default value and it cannot be changed by the
               user.
        :param int q: Schema for the number of shards in a database. Each shard is
               a partition of the hash value range.
        :param int r: Read quorum. The number of consistent copies of a document
               that need to be read before a successful reply.
        :param int w: Write quorum. The number of copies of a document that need to
               be written before a successful reply.
        """
        self.n = n
        self.q = q
        self.r = r
        self.w = w

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DatabaseInformationCluster':
        """Initialize a DatabaseInformationCluster object from a json dictionary."""
        args = {}
        if (n := _dict.get('n')) is not None:
            args['n'] = n
        else:
            raise ValueError('Required property \'n\' not present in DatabaseInformationCluster JSON')
        if (q := _dict.get('q')) is not None:
            args['q'] = q
        else:
            raise ValueError('Required property \'q\' not present in DatabaseInformationCluster JSON')
        if (r := _dict.get('r')) is not None:
            args['r'] = r
        else:
            raise ValueError('Required property \'r\' not present in DatabaseInformationCluster JSON')
        if (w := _dict.get('w')) is not None:
            args['w'] = w
        else:
            raise ValueError('Required property \'w\' not present in DatabaseInformationCluster JSON')
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


class DatabaseInformationProps:
    """
    Schema for database properties.

    :param bool partitioned: (optional) The value is `true` for a partitioned
          database.
    """

    def __init__(
        self,
        *,
        partitioned: Optional[bool] = None,
    ) -> None:
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
        if (partitioned := _dict.get('partitioned')) is not None:
            args['partitioned'] = partitioned
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


class DbEvent:
    """
    Schema for a database change event.

    :param str db_name: Schema for a database name.
    :param str seq: Sequence number.
    :param str type: A database event.
    """

    def __init__(
        self,
        db_name: str,
        seq: str,
        type: str,
    ) -> None:
        """
        Initialize a DbEvent object.

        :param str db_name: Schema for a database name.
        :param str seq: Sequence number.
        :param str type: A database event.
        """
        self.db_name = db_name
        self.seq = seq
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DbEvent':
        """Initialize a DbEvent object from a json dictionary."""
        args = {}
        if (db_name := _dict.get('db_name')) is not None:
            args['db_name'] = db_name
        else:
            raise ValueError('Required property \'db_name\' not present in DbEvent JSON')
        if (seq := _dict.get('seq')) is not None:
            args['seq'] = seq
        else:
            raise ValueError('Required property \'seq\' not present in DbEvent JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in DbEvent JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DbEvent object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'db_name') and self.db_name is not None:
            _dict['db_name'] = self.db_name
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



class DbUpdates:
    """
    Schema for database updates.

    :param str last_seq: Last sequence number.
    :param List[DbEvent] results: results.
    """

    def __init__(
        self,
        last_seq: str,
        results: List['DbEvent'],
    ) -> None:
        """
        Initialize a DbUpdates object.

        :param str last_seq: Last sequence number.
        :param List[DbEvent] results: results.
        """
        self.last_seq = last_seq
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DbUpdates':
        """Initialize a DbUpdates object from a json dictionary."""
        args = {}
        if (last_seq := _dict.get('last_seq')) is not None:
            args['last_seq'] = last_seq
        else:
            raise ValueError('Required property \'last_seq\' not present in DbUpdates JSON')
        if (results := _dict.get('results')) is not None:
            args['results'] = [DbEvent.from_dict(v) for v in results]
        else:
            raise ValueError('Required property \'results\' not present in DbUpdates JSON')
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
            results_list = []
            for v in self.results:
                if isinstance(v, dict):
                    results_list.append(v)
                else:
                    results_list.append(v.to_dict())
            _dict['results'] = results_list
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


class DbsInfoResult:
    """
    Schema for database information keyed by database name.

    :param str error: (optional) The name of the error.
    :param DatabaseInformation info: (optional) Schema for information about a
          database.
    :param str key: Schema for a database name.
    """

    def __init__(
        self,
        key: str,
        *,
        error: Optional[str] = None,
        info: Optional['DatabaseInformation'] = None,
    ) -> None:
        """
        Initialize a DbsInfoResult object.

        :param str key: Schema for a database name.
        :param str error: (optional) The name of the error.
        :param DatabaseInformation info: (optional) Schema for information about a
               database.
        """
        self.error = error
        self.info = info
        self.key = key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DbsInfoResult':
        """Initialize a DbsInfoResult object from a json dictionary."""
        args = {}
        if (error := _dict.get('error')) is not None:
            args['error'] = error
        if (info := _dict.get('info')) is not None:
            args['info'] = DatabaseInformation.from_dict(info)
        if (key := _dict.get('key')) is not None:
            args['key'] = key
        else:
            raise ValueError('Required property \'key\' not present in DbsInfoResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DbsInfoResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error
        if hasattr(self, 'info') and self.info is not None:
            if isinstance(self.info, dict):
                _dict['info'] = self.info
            else:
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


class DesignDocument:
    """
    Schema for a design document.

    :param dict _attachments: (optional) Schema for a map of attachment name to
          attachment metadata.
    :param List[str] _conflicts: (optional) Schema for a list of document revision
          identifiers.
    :param bool _deleted: (optional) Deletion flag. Available if document was
          removed.
    :param List[str] _deleted_conflicts: (optional) Schema for a list of document
          revision identifiers.
    :param str _id: (optional) Schema for a design document ID including a
          `_design/` prefix.
    :param str _local_seq: (optional) Document's update sequence in current
          database. Available if requested with local_seq=true query parameter.
    :param str _rev: (optional) Schema for a document revision identifier.
    :param Revisions _revisions: (optional) Schema for list of revision information.
    :param List[DocumentRevisionStatus] _revs_info: (optional) Schema for a list of
          objects with information about local revisions and their status.
    :param bool autoupdate: (optional) Indicates whether to automatically build
          indexes defined in this design document.
    :param dict filters: (optional) Schema for filter functions definition. This
          schema is a map where keys are the names of the filter functions and values are
          the function definition in string format.
          Filter function formats, or filters the changes feed that pass filter rules. The
          function takes 2 parameters:
            * `doc`: The document that is being processed.
            * `req`: A Request JavaScript object with these properties:
              * `body` - string, Request body data as string.
                If the request method is GET this field contains the value
                `"undefined"`.
                If the method is DELETE or HEAD the value is `""` (empty string).
              * `cookie` - Cookies object.
              * `form` - Form Data object, contains the decoded body as key-value
                pairs if the Content-Type header was
                application/x-www-form-urlencoded.
              * `headers` - Request Headers object.
              * `id` - string, requested document id if it was specified
                or null otherwise.
              * `info` - Database Information object,
                see `DatabaseInformation`.
              * `method` - string or an array of chars, request method.
                String value is a method as one of: HEAD, GET, POST, PUT,
                DELETE, OPTIONS, TRACE, COPY. For not supported methods
                it will be represented as an array of char codes e.g. for VIEW
                it will be 86,73,69,87.
              * `path` - array of strings, requested path sections.
              * `peer` - string, request source IP address.
              * `query` - string, URL query parameters object. Note that multiple
                keys are not supported and the last key value suppresses others.
              * `requested_path` - array of strings,
                actual requested path section.
              * `raw_path` - string, raw requested path.
              * `userCtx`: User Context Object, containing information about the
                user writing the document (if present), see the `UserContext`.
              * `secObj`: Security Object, with lists of database security roles,
                see the `SecurityObject`.
              * `uuid` - string, generated UUID by a specified algorithm in the
                config file.
          Filter functions must return true if a document passed all the rules.
    :param dict indexes: (optional) Search (text) index function definitions.
    :param str language: (optional) Defines Query Server key to process design
          document functions.
    :param DesignDocumentOptions options: (optional) Schema for design document
          options.
    :param str validate_doc_update: (optional) Validate document update function can
          be used to prevent invalid or unauthorized document update requests from being
          stored. Validation functions typically examine the structure of the new document
          to ensure that required fields are present and to verify that the requesting
          user should be allowed to make changes to the document properties. When a write
          request is received for a given database, the validation function in each design
          document in that database is called in an unspecified order. If any of the
          validation functions throw an error, the write will not succeed.
          The validation function can abort the pending document write by throwing one of
          two error objects:
          ```
          // user is not authorized to make the change but may re-authenticate throw({
          unauthorized: 'Error message here.' });
          // change is not allowed throw({ forbidden: 'Error message here.' });
          ```
          The function takes 4 parameters:
            * `newDoc` - New version of document that will be stored
              from the update request.
            * `oldDoc` - Previous version of document that is already stored.
            * `userCtx` - User Context Object, containing information about the
              user writing the document (if present), see the `UserContext`.
            * `secObj` - Security Object, with lists of database security roles,
              see the `SecurityObject`.
    :param dict views: (optional) Schema for design document views.

    This type supports additional properties of type object.
    """

    # The set of defined properties for the class
    _properties = frozenset(['_attachments', '_conflicts', '_deleted', '_deleted_conflicts', '_id', '_local_seq', '_rev', '_revisions', '_revs_info', 'autoupdate', 'filters', 'indexes', 'language', 'options', 'validate_doc_update', 'views'])

    def __init__(
        self,
        *,
        _attachments: Optional[dict] = None,
        _conflicts: Optional[List[str]] = None,
        _deleted: Optional[bool] = None,
        _deleted_conflicts: Optional[List[str]] = None,
        _id: Optional[str] = None,
        _local_seq: Optional[str] = None,
        _rev: Optional[str] = None,
        _revisions: Optional['Revisions'] = None,
        _revs_info: Optional[List['DocumentRevisionStatus']] = None,
        autoupdate: Optional[bool] = None,
        filters: Optional[dict] = None,
        indexes: Optional[dict] = None,
        language: Optional[str] = None,
        options: Optional['DesignDocumentOptions'] = None,
        validate_doc_update: Optional[str] = None,
        views: Optional[dict] = None,
        **kwargs: Optional[object],
    ) -> None:
        """
        Initialize a DesignDocument object.

        :param dict _attachments: (optional) Schema for a map of attachment name to
               attachment metadata.
        :param List[str] _conflicts: (optional) Schema for a list of document
               revision identifiers.
        :param bool _deleted: (optional) Deletion flag. Available if document was
               removed.
        :param List[str] _deleted_conflicts: (optional) Schema for a list of
               document revision identifiers.
        :param str _id: (optional) Schema for a design document ID including a
               `_design/` prefix.
        :param str _local_seq: (optional) Document's update sequence in current
               database. Available if requested with local_seq=true query parameter.
        :param str _rev: (optional) Schema for a document revision identifier.
        :param Revisions _revisions: (optional) Schema for list of revision
               information.
        :param List[DocumentRevisionStatus] _revs_info: (optional) Schema for a
               list of objects with information about local revisions and their status.
        :param bool autoupdate: (optional) Indicates whether to automatically build
               indexes defined in this design document.
        :param dict filters: (optional) Schema for filter functions definition.
               This schema is a map where keys are the names of the filter functions and
               values are the function definition in string format.
               Filter function formats, or filters the changes feed that pass filter
               rules. The function takes 2 parameters:
                 * `doc`: The document that is being processed.
                 * `req`: A Request JavaScript object with these properties:
                   * `body` - string, Request body data as string.
                     If the request method is GET this field contains the value
                     `"undefined"`.
                     If the method is DELETE or HEAD the value is `""` (empty string).
                   * `cookie` - Cookies object.
                   * `form` - Form Data object, contains the decoded body as key-value
                     pairs if the Content-Type header was
                     application/x-www-form-urlencoded.
                   * `headers` - Request Headers object.
                   * `id` - string, requested document id if it was specified
                     or null otherwise.
                   * `info` - Database Information object,
                     see `DatabaseInformation`.
                   * `method` - string or an array of chars, request method.
                     String value is a method as one of: HEAD, GET, POST, PUT,
                     DELETE, OPTIONS, TRACE, COPY. For not supported methods
                     it will be represented as an array of char codes e.g. for VIEW
                     it will be 86,73,69,87.
                   * `path` - array of strings, requested path sections.
                   * `peer` - string, request source IP address.
                   * `query` - string, URL query parameters object. Note that multiple
                     keys are not supported and the last key value suppresses others.
                   * `requested_path` - array of strings,
                     actual requested path section.
                   * `raw_path` - string, raw requested path.
                   * `userCtx`: User Context Object, containing information about the
                     user writing the document (if present), see the `UserContext`.
                   * `secObj`: Security Object, with lists of database security roles,
                     see the `SecurityObject`.
                   * `uuid` - string, generated UUID by a specified algorithm in the
                     config file.
               Filter functions must return true if a document passed all the rules.
        :param dict indexes: (optional) Search (text) index function definitions.
        :param str language: (optional) Defines Query Server key to process design
               document functions.
        :param DesignDocumentOptions options: (optional) Schema for design document
               options.
        :param str validate_doc_update: (optional) Validate document update
               function can be used to prevent invalid or unauthorized document update
               requests from being stored. Validation functions typically examine the
               structure of the new document to ensure that required fields are present
               and to verify that the requesting user should be allowed to make changes to
               the document properties. When a write request is received for a given
               database, the validation function in each design document in that database
               is called in an unspecified order. If any of the validation functions throw
               an error, the write will not succeed.
               The validation function can abort the pending document write by throwing
               one of two error objects:
               ```
               // user is not authorized to make the change but may re-authenticate
               throw({ unauthorized: 'Error message here.' });
               // change is not allowed throw({ forbidden: 'Error message here.' });
               ```
               The function takes 4 parameters:
                 * `newDoc` - New version of document that will be stored
                   from the update request.
                 * `oldDoc` - Previous version of document that is already stored.
                 * `userCtx` - User Context Object, containing information about the
                   user writing the document (if present), see the `UserContext`.
                 * `secObj` - Security Object, with lists of database security roles,
                   see the `SecurityObject`.
        :param dict views: (optional) Schema for design document views.
        :param object **kwargs: (optional) Additional properties of type object
        """
        self._attachments = _attachments
        self._conflicts = _conflicts
        self._deleted = _deleted
        self._deleted_conflicts = _deleted_conflicts
        self._id = _id
        self._local_seq = _local_seq
        self._rev = _rev
        self._revisions = _revisions
        self._revs_info = _revs_info
        self.autoupdate = autoupdate
        self.filters = filters
        self.indexes = indexes
        self.language = language
        self.options = options
        self.validate_doc_update = validate_doc_update
        self.views = views
        for k, v in kwargs.items():
            if k not in DesignDocument._properties:
                if not isinstance(v, object):
                    raise ValueError('Value for additional property {} must be of type object'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(k))

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DesignDocument':
        """Initialize a DesignDocument object from a json dictionary."""
        args = {}
        if (attachments := _dict.get('_attachments')) is not None:
            args['_attachments'] = {k: Attachment.from_dict(v) for k, v in attachments.items()}
        if (conflicts := _dict.get('_conflicts')) is not None:
            args['_conflicts'] = conflicts
        if (deleted := _dict.get('_deleted')) is not None:
            args['_deleted'] = deleted
        if (deleted_conflicts := _dict.get('_deleted_conflicts')) is not None:
            args['_deleted_conflicts'] = deleted_conflicts
        if (id := _dict.get('_id')) is not None:
            args['_id'] = id
        if (local_seq := _dict.get('_local_seq')) is not None:
            args['_local_seq'] = local_seq
        if (rev := _dict.get('_rev')) is not None:
            args['_rev'] = rev
        if (revisions := _dict.get('_revisions')) is not None:
            args['_revisions'] = Revisions.from_dict(revisions)
        if (revs_info := _dict.get('_revs_info')) is not None:
            args['_revs_info'] = [DocumentRevisionStatus.from_dict(v) for v in revs_info]
        if (autoupdate := _dict.get('autoupdate')) is not None:
            args['autoupdate'] = autoupdate
        if (filters := _dict.get('filters')) is not None:
            args['filters'] = filters
        if (indexes := _dict.get('indexes')) is not None:
            args['indexes'] = {k: SearchIndexDefinition.from_dict(v) for k, v in indexes.items()}
        if (language := _dict.get('language')) is not None:
            args['language'] = language
        if (options := _dict.get('options')) is not None:
            args['options'] = DesignDocumentOptions.from_dict(options)
        if (validate_doc_update := _dict.get('validate_doc_update')) is not None:
            args['validate_doc_update'] = validate_doc_update
        if (views := _dict.get('views')) is not None:
            args['views'] = {k: DesignDocumentViewsMapReduce.from_dict(v) for k, v in views.items()}
        for k, v in _dict.items():
            if k not in cls._properties:
                    if not isinstance(v, object):
                        raise ValueError('Value for additional property {} must be of type object'.format(k))
                    args[k] = v
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DesignDocument object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, '_attachments') and self._attachments is not None:
            _attachments_map = {}
            for k, v in self._attachments.items():
                if isinstance(v, dict):
                    _attachments_map[k] = v
                else:
                    _attachments_map[k] = v.to_dict()
            _dict['_attachments'] = _attachments_map
        if hasattr(self, '_conflicts') and self._conflicts is not None:
            _dict['_conflicts'] = self._conflicts
        if hasattr(self, '_deleted') and self._deleted is not None:
            _dict['_deleted'] = self._deleted
        if hasattr(self, '_deleted_conflicts') and self._deleted_conflicts is not None:
            _dict['_deleted_conflicts'] = self._deleted_conflicts
        if hasattr(self, '_id') and self._id is not None:
            _dict['_id'] = self._id
        if hasattr(self, '_local_seq') and self._local_seq is not None:
            _dict['_local_seq'] = self._local_seq
        if hasattr(self, '_rev') and self._rev is not None:
            _dict['_rev'] = self._rev
        if hasattr(self, '_revisions') and self._revisions is not None:
            if isinstance(self._revisions, dict):
                _dict['_revisions'] = self._revisions
            else:
                _dict['_revisions'] = self._revisions.to_dict()
        if hasattr(self, '_revs_info') and self._revs_info is not None:
            _revs_info_list = []
            for v in self._revs_info:
                if isinstance(v, dict):
                    _revs_info_list.append(v)
                else:
                    _revs_info_list.append(v.to_dict())
            _dict['_revs_info'] = _revs_info_list
        if hasattr(self, 'autoupdate') and self.autoupdate is not None:
            _dict['autoupdate'] = self.autoupdate
        if hasattr(self, 'filters') and self.filters is not None:
            _dict['filters'] = self.filters
        if hasattr(self, 'indexes') and self.indexes is not None:
            indexes_map = {}
            for k, v in self.indexes.items():
                if isinstance(v, dict):
                    indexes_map[k] = v
                else:
                    indexes_map[k] = v.to_dict()
            _dict['indexes'] = indexes_map
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'options') and self.options is not None:
            if isinstance(self.options, dict):
                _dict['options'] = self.options
            else:
                _dict['options'] = self.options.to_dict()
        if hasattr(self, 'validate_doc_update') and self.validate_doc_update is not None:
            _dict['validate_doc_update'] = self.validate_doc_update
        if hasattr(self, 'views') and self.views is not None:
            views_map = {}
            for k, v in self.views.items():
                if isinstance(v, dict):
                    views_map[k] = v
                else:
                    views_map[k] = v.to_dict()
            _dict['views'] = views_map
        for k in [_k for _k in vars(self).keys() if _k not in DesignDocument._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of DesignDocument in the form of a dict."""
        _dict = {}
        for k in [_k for _k in vars(self).keys() if _k not in DesignDocument._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of DesignDocument"""
        for k in [_k for _k in vars(self).keys() if _k not in DesignDocument._properties]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in DesignDocument._properties:
                if not isinstance(v, object):
                    raise ValueError('Value for additional property {} must be of type object'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(k))

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


class DesignDocumentInformation:
    """
    Schema for information about a design document.

    :param str name: name.
    :param DesignDocumentViewIndex view_index: View index information.
    """

    def __init__(
        self,
        name: str,
        view_index: 'DesignDocumentViewIndex',
    ) -> None:
        """
        Initialize a DesignDocumentInformation object.

        :param str name: name.
        :param DesignDocumentViewIndex view_index: View index information.
        """
        self.name = name
        self.view_index = view_index

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DesignDocumentInformation':
        """Initialize a DesignDocumentInformation object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in DesignDocumentInformation JSON')
        if (view_index := _dict.get('view_index')) is not None:
            args['view_index'] = DesignDocumentViewIndex.from_dict(view_index)
        else:
            raise ValueError('Required property \'view_index\' not present in DesignDocumentInformation JSON')
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
            if isinstance(self.view_index, dict):
                _dict['view_index'] = self.view_index
            else:
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


class DesignDocumentOptions:
    """
    Schema for design document options.

    :param bool partitioned: (optional) Whether this design document describes
          partitioned or global indexes.
    """

    def __init__(
        self,
        *,
        partitioned: Optional[bool] = None,
    ) -> None:
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
        if (partitioned := _dict.get('partitioned')) is not None:
            args['partitioned'] = partitioned
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


class DesignDocumentViewIndex:
    """
    View index information.

    :param List[str] collator_versions: List of collator versions. If there are
          multiple entries this implies a libicu upgrade has occurred but compaction has
          not run yet.
    :param bool compact_running: Indicates whether a compaction routine is currently
          running on the view.
    :param str language: Language for the defined views.
    :param str signature: MD5 signature of the views for the design document.
    :param ContentInformationSizes sizes: Schema for size information of content.
    :param bool updater_running: Indicates if the view is currently being updated.
    :param UpdatesPending updates_pending: Schema for an ability to tell if view is
          up-to-date without querying it.
    :param int waiting_clients: Number of clients waiting on views from this design
          document.
    :param bool waiting_commit: Indicates if there are outstanding commits to the
          underlying database that need to processed.
    """

    def __init__(
        self,
        collator_versions: List[str],
        compact_running: bool,
        language: str,
        signature: str,
        sizes: 'ContentInformationSizes',
        updater_running: bool,
        updates_pending: 'UpdatesPending',
        waiting_clients: int,
        waiting_commit: bool,
    ) -> None:
        """
        Initialize a DesignDocumentViewIndex object.

        :param List[str] collator_versions: List of collator versions. If there are
               multiple entries this implies a libicu upgrade has occurred but compaction
               has not run yet.
        :param bool compact_running: Indicates whether a compaction routine is
               currently running on the view.
        :param str language: Language for the defined views.
        :param str signature: MD5 signature of the views for the design document.
        :param ContentInformationSizes sizes: Schema for size information of
               content.
        :param bool updater_running: Indicates if the view is currently being
               updated.
        :param UpdatesPending updates_pending: Schema for an ability to tell if
               view is up-to-date without querying it.
        :param int waiting_clients: Number of clients waiting on views from this
               design document.
        :param bool waiting_commit: Indicates if there are outstanding commits to
               the underlying database that need to processed.
        """
        self.collator_versions = collator_versions
        self.compact_running = compact_running
        self.language = language
        self.signature = signature
        self.sizes = sizes
        self.updater_running = updater_running
        self.updates_pending = updates_pending
        self.waiting_clients = waiting_clients
        self.waiting_commit = waiting_commit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DesignDocumentViewIndex':
        """Initialize a DesignDocumentViewIndex object from a json dictionary."""
        args = {}
        if (collator_versions := _dict.get('collator_versions')) is not None:
            args['collator_versions'] = collator_versions
        else:
            raise ValueError('Required property \'collator_versions\' not present in DesignDocumentViewIndex JSON')
        if (compact_running := _dict.get('compact_running')) is not None:
            args['compact_running'] = compact_running
        else:
            raise ValueError('Required property \'compact_running\' not present in DesignDocumentViewIndex JSON')
        if (language := _dict.get('language')) is not None:
            args['language'] = language
        else:
            raise ValueError('Required property \'language\' not present in DesignDocumentViewIndex JSON')
        if (signature := _dict.get('signature')) is not None:
            args['signature'] = signature
        else:
            raise ValueError('Required property \'signature\' not present in DesignDocumentViewIndex JSON')
        if (sizes := _dict.get('sizes')) is not None:
            args['sizes'] = ContentInformationSizes.from_dict(sizes)
        else:
            raise ValueError('Required property \'sizes\' not present in DesignDocumentViewIndex JSON')
        if (updater_running := _dict.get('updater_running')) is not None:
            args['updater_running'] = updater_running
        else:
            raise ValueError('Required property \'updater_running\' not present in DesignDocumentViewIndex JSON')
        if (updates_pending := _dict.get('updates_pending')) is not None:
            args['updates_pending'] = UpdatesPending.from_dict(updates_pending)
        else:
            raise ValueError('Required property \'updates_pending\' not present in DesignDocumentViewIndex JSON')
        if (waiting_clients := _dict.get('waiting_clients')) is not None:
            args['waiting_clients'] = waiting_clients
        else:
            raise ValueError('Required property \'waiting_clients\' not present in DesignDocumentViewIndex JSON')
        if (waiting_commit := _dict.get('waiting_commit')) is not None:
            args['waiting_commit'] = waiting_commit
        else:
            raise ValueError('Required property \'waiting_commit\' not present in DesignDocumentViewIndex JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DesignDocumentViewIndex object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'collator_versions') and self.collator_versions is not None:
            _dict['collator_versions'] = self.collator_versions
        if hasattr(self, 'compact_running') and self.compact_running is not None:
            _dict['compact_running'] = self.compact_running
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'signature') and self.signature is not None:
            _dict['signature'] = self.signature
        if hasattr(self, 'sizes') and self.sizes is not None:
            if isinstance(self.sizes, dict):
                _dict['sizes'] = self.sizes
            else:
                _dict['sizes'] = self.sizes.to_dict()
        if hasattr(self, 'updater_running') and self.updater_running is not None:
            _dict['updater_running'] = self.updater_running
        if hasattr(self, 'updates_pending') and self.updates_pending is not None:
            if isinstance(self.updates_pending, dict):
                _dict['updates_pending'] = self.updates_pending
            else:
                _dict['updates_pending'] = self.updates_pending.to_dict()
        if hasattr(self, 'waiting_clients') and self.waiting_clients is not None:
            _dict['waiting_clients'] = self.waiting_clients
        if hasattr(self, 'waiting_commit') and self.waiting_commit is not None:
            _dict['waiting_commit'] = self.waiting_commit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DesignDocumentViewIndex object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DesignDocumentViewIndex') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DesignDocumentViewIndex') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DesignDocumentViewsMapReduce:
    """
    Schema for view functions definition.

    :param str map: JavaScript map function as a string.
    :param str reduce: (optional) JavaScript reduce function as a string.
    """

    def __init__(
        self,
        map: str,
        *,
        reduce: Optional[str] = None,
    ) -> None:
        """
        Initialize a DesignDocumentViewsMapReduce object.

        :param str map: JavaScript map function as a string.
        :param str reduce: (optional) JavaScript reduce function as a string.
        """
        self.map = map
        self.reduce = reduce

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DesignDocumentViewsMapReduce':
        """Initialize a DesignDocumentViewsMapReduce object from a json dictionary."""
        args = {}
        if (map := _dict.get('map')) is not None:
            args['map'] = map
        else:
            raise ValueError('Required property \'map\' not present in DesignDocumentViewsMapReduce JSON')
        if (reduce := _dict.get('reduce')) is not None:
            args['reduce'] = reduce
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


class DocsResultRow:
    """
    Schema for a row of document information in a DocsResult.

    :param str caused_by: (optional) The cause of the error (if available).
    :param str error: (optional) The name of the error.
    :param str reason: (optional) The reason the error occurred (if available).
    :param int ref: (optional) An internal error reference (if available).
    :param Document doc: (optional) Schema for a document.
    :param str id: (optional) Schema for a document ID.
    :param str key: Schema for a document ID.
    :param DocsResultRowValue value: (optional) Value of built-in `/_all_docs` style
          view.
    """

    def __init__(
        self,
        key: str,
        *,
        caused_by: Optional[str] = None,
        error: Optional[str] = None,
        reason: Optional[str] = None,
        ref: Optional[int] = None,
        doc: Optional['Document'] = None,
        id: Optional[str] = None,
        value: Optional['DocsResultRowValue'] = None,
    ) -> None:
        """
        Initialize a DocsResultRow object.

        :param str key: Schema for a document ID.
        :param str caused_by: (optional) The cause of the error (if available).
        :param str error: (optional) The name of the error.
        :param str reason: (optional) The reason the error occurred (if available).
        :param int ref: (optional) An internal error reference (if available).
        :param Document doc: (optional) Schema for a document.
        :param str id: (optional) Schema for a document ID.
        :param DocsResultRowValue value: (optional) Value of built-in `/_all_docs`
               style view.
        """
        self.caused_by = caused_by
        self.error = error
        self.reason = reason
        self.ref = ref
        self.doc = doc
        self.id = id
        self.key = key
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocsResultRow':
        """Initialize a DocsResultRow object from a json dictionary."""
        args = {}
        if (caused_by := _dict.get('caused_by')) is not None:
            args['caused_by'] = caused_by
        if (error := _dict.get('error')) is not None:
            args['error'] = error
        if (reason := _dict.get('reason')) is not None:
            args['reason'] = reason
        if (ref := _dict.get('ref')) is not None:
            args['ref'] = ref
        if (doc := _dict.get('doc')) is not None:
            args['doc'] = Document.from_dict(doc)
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (key := _dict.get('key')) is not None:
            args['key'] = key
        else:
            raise ValueError('Required property \'key\' not present in DocsResultRow JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = DocsResultRowValue.from_dict(value)
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
        if hasattr(self, 'ref') and self.ref is not None:
            _dict['ref'] = self.ref
        if hasattr(self, 'doc') and self.doc is not None:
            if isinstance(self.doc, dict):
                _dict['doc'] = self.doc
            else:
                _dict['doc'] = self.doc.to_dict()
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self, 'value') and self.value is not None:
            if isinstance(self.value, dict):
                _dict['value'] = self.value
            else:
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


class DocsResultRowValue:
    """
    Value of built-in `/_all_docs` style view.

    :param bool deleted: (optional) If `true` then the document is deleted. Not
          present for undeleted documents.
    :param str rev: Schema for a document revision identifier.
    """

    def __init__(
        self,
        rev: str,
        *,
        deleted: Optional[bool] = None,
    ) -> None:
        """
        Initialize a DocsResultRowValue object.

        :param str rev: Schema for a document revision identifier.
        :param bool deleted: (optional) If `true` then the document is deleted. Not
               present for undeleted documents.
        """
        self.deleted = deleted
        self.rev = rev

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocsResultRowValue':
        """Initialize a DocsResultRowValue object from a json dictionary."""
        args = {}
        if (deleted := _dict.get('deleted')) is not None:
            args['deleted'] = deleted
        if (rev := _dict.get('rev')) is not None:
            args['rev'] = rev
        else:
            raise ValueError('Required property \'rev\' not present in DocsResultRowValue JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocsResultRowValue object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'deleted') and self.deleted is not None:
            _dict['deleted'] = self.deleted
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


class Document:
    """
    Schema for a document.

    :param dict _attachments: (optional) Schema for a map of attachment name to
          attachment metadata.
    :param List[str] _conflicts: (optional) Schema for a list of document revision
          identifiers.
    :param bool _deleted: (optional) Deletion flag. Available if document was
          removed.
    :param List[str] _deleted_conflicts: (optional) Schema for a list of document
          revision identifiers.
    :param str _id: (optional) Schema for a document ID.
    :param str _local_seq: (optional) Document's update sequence in current
          database. Available if requested with local_seq=true query parameter.
    :param str _rev: (optional) Schema for a document revision identifier.
    :param Revisions _revisions: (optional) Schema for list of revision information.
    :param List[DocumentRevisionStatus] _revs_info: (optional) Schema for a list of
          objects with information about local revisions and their status.

    This type supports additional properties of type object.
    """

    # The set of defined properties for the class
    _properties = frozenset(['_attachments', '_conflicts', '_deleted', '_deleted_conflicts', '_id', '_local_seq', '_rev', '_revisions', '_revs_info'])

    def __init__(
        self,
        *,
        _attachments: Optional[dict] = None,
        _conflicts: Optional[List[str]] = None,
        _deleted: Optional[bool] = None,
        _deleted_conflicts: Optional[List[str]] = None,
        _id: Optional[str] = None,
        _local_seq: Optional[str] = None,
        _rev: Optional[str] = None,
        _revisions: Optional['Revisions'] = None,
        _revs_info: Optional[List['DocumentRevisionStatus']] = None,
        **kwargs: Optional[object],
    ) -> None:
        """
        Initialize a Document object.

        :param dict _attachments: (optional) Schema for a map of attachment name to
               attachment metadata.
        :param List[str] _conflicts: (optional) Schema for a list of document
               revision identifiers.
        :param bool _deleted: (optional) Deletion flag. Available if document was
               removed.
        :param List[str] _deleted_conflicts: (optional) Schema for a list of
               document revision identifiers.
        :param str _id: (optional) Schema for a document ID.
        :param str _local_seq: (optional) Document's update sequence in current
               database. Available if requested with local_seq=true query parameter.
        :param str _rev: (optional) Schema for a document revision identifier.
        :param Revisions _revisions: (optional) Schema for list of revision
               information.
        :param List[DocumentRevisionStatus] _revs_info: (optional) Schema for a
               list of objects with information about local revisions and their status.
        :param object **kwargs: (optional) Additional properties of type object
        """
        self._attachments = _attachments
        self._conflicts = _conflicts
        self._deleted = _deleted
        self._deleted_conflicts = _deleted_conflicts
        self._id = _id
        self._local_seq = _local_seq
        self._rev = _rev
        self._revisions = _revisions
        self._revs_info = _revs_info
        for k, v in kwargs.items():
            if k not in Document._properties:
                if not isinstance(v, object):
                    raise ValueError('Value for additional property {} must be of type object'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(k))

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Document':
        """Initialize a Document object from a json dictionary."""
        args = {}
        if (attachments := _dict.get('_attachments')) is not None:
            args['_attachments'] = {k: Attachment.from_dict(v) for k, v in attachments.items()}
        if (conflicts := _dict.get('_conflicts')) is not None:
            args['_conflicts'] = conflicts
        if (deleted := _dict.get('_deleted')) is not None:
            args['_deleted'] = deleted
        if (deleted_conflicts := _dict.get('_deleted_conflicts')) is not None:
            args['_deleted_conflicts'] = deleted_conflicts
        if (id := _dict.get('_id')) is not None:
            args['_id'] = id
        if (local_seq := _dict.get('_local_seq')) is not None:
            args['_local_seq'] = local_seq
        if (rev := _dict.get('_rev')) is not None:
            args['_rev'] = rev
        if (revisions := _dict.get('_revisions')) is not None:
            args['_revisions'] = Revisions.from_dict(revisions)
        if (revs_info := _dict.get('_revs_info')) is not None:
            args['_revs_info'] = [DocumentRevisionStatus.from_dict(v) for v in revs_info]
        for k, v in _dict.items():
            if k not in cls._properties:
                    if not isinstance(v, object):
                        raise ValueError('Value for additional property {} must be of type object'.format(k))
                    args[k] = v
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Document object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, '_attachments') and self._attachments is not None:
            _attachments_map = {}
            for k, v in self._attachments.items():
                if isinstance(v, dict):
                    _attachments_map[k] = v
                else:
                    _attachments_map[k] = v.to_dict()
            _dict['_attachments'] = _attachments_map
        if hasattr(self, '_conflicts') and self._conflicts is not None:
            _dict['_conflicts'] = self._conflicts
        if hasattr(self, '_deleted') and self._deleted is not None:
            _dict['_deleted'] = self._deleted
        if hasattr(self, '_deleted_conflicts') and self._deleted_conflicts is not None:
            _dict['_deleted_conflicts'] = self._deleted_conflicts
        if hasattr(self, '_id') and self._id is not None:
            _dict['_id'] = self._id
        if hasattr(self, '_local_seq') and self._local_seq is not None:
            _dict['_local_seq'] = self._local_seq
        if hasattr(self, '_rev') and self._rev is not None:
            _dict['_rev'] = self._rev
        if hasattr(self, '_revisions') and self._revisions is not None:
            if isinstance(self._revisions, dict):
                _dict['_revisions'] = self._revisions
            else:
                _dict['_revisions'] = self._revisions.to_dict()
        if hasattr(self, '_revs_info') and self._revs_info is not None:
            _revs_info_list = []
            for v in self._revs_info:
                if isinstance(v, dict):
                    _revs_info_list.append(v)
                else:
                    _revs_info_list.append(v.to_dict())
            _dict['_revs_info'] = _revs_info_list
        for k in [_k for _k in vars(self).keys() if _k not in Document._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of Document in the form of a dict."""
        _dict = {}
        for k in [_k for _k in vars(self).keys() if _k not in Document._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of Document"""
        for k in [_k for _k in vars(self).keys() if _k not in Document._properties]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in Document._properties:
                if not isinstance(v, object):
                    raise ValueError('Value for additional property {} must be of type object'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(k))

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


class DocumentResult:
    """
    Schema for the result of a document modification.

    :param str id: Schema for a document ID.
    :param str rev: (optional) Schema for a document revision identifier.
    :param bool ok: (optional) ok.
    :param str caused_by: (optional) The cause of the error (if available).
    :param str error: (optional) The name of the error.
    :param str reason: (optional) The reason the error occurred (if available).
    :param int ref: (optional) An internal error reference (if available).
    """

    def __init__(
        self,
        id: str,
        *,
        rev: Optional[str] = None,
        ok: Optional[bool] = None,
        caused_by: Optional[str] = None,
        error: Optional[str] = None,
        reason: Optional[str] = None,
        ref: Optional[int] = None,
    ) -> None:
        """
        Initialize a DocumentResult object.

        :param str id: Schema for a document ID.
        :param str rev: (optional) Schema for a document revision identifier.
        :param bool ok: (optional) ok.
        :param str caused_by: (optional) The cause of the error (if available).
        :param str error: (optional) The name of the error.
        :param str reason: (optional) The reason the error occurred (if available).
        :param int ref: (optional) An internal error reference (if available).
        """
        self.id = id
        self.rev = rev
        self.ok = ok
        self.caused_by = caused_by
        self.error = error
        self.reason = reason
        self.ref = ref

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentResult':
        """Initialize a DocumentResult object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DocumentResult JSON')
        if (rev := _dict.get('rev')) is not None:
            args['rev'] = rev
        if (ok := _dict.get('ok')) is not None:
            args['ok'] = ok
        if (caused_by := _dict.get('caused_by')) is not None:
            args['caused_by'] = caused_by
        if (error := _dict.get('error')) is not None:
            args['error'] = error
        if (reason := _dict.get('reason')) is not None:
            args['reason'] = reason
        if (ref := _dict.get('ref')) is not None:
            args['ref'] = ref
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
        if hasattr(self, 'ref') and self.ref is not None:
            _dict['ref'] = self.ref
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


class DocumentRevisionStatus:
    """
    Schema for information about revisions and their status.

    :param str rev: Schema for a document revision identifier.
    :param str status: Status of the revision. May be one of: - `available`:
          Revision is available for retrieving with rev query parameter - `missing`:
          Revision is not available - `deleted`: Revision belongs to deleted document.
    """

    def __init__(
        self,
        rev: str,
        status: str,
    ) -> None:
        """
        Initialize a DocumentRevisionStatus object.

        :param str rev: Schema for a document revision identifier.
        :param str status: Status of the revision. May be one of: - `available`:
               Revision is available for retrieving with rev query parameter - `missing`:
               Revision is not available - `deleted`: Revision belongs to deleted
               document.
        """
        self.rev = rev
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentRevisionStatus':
        """Initialize a DocumentRevisionStatus object from a json dictionary."""
        args = {}
        if (rev := _dict.get('rev')) is not None:
            args['rev'] = rev
        else:
            raise ValueError('Required property \'rev\' not present in DocumentRevisionStatus JSON')
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in DocumentRevisionStatus JSON')
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



class DocumentShardInfo:
    """
    Schema for document shard information.

    :param List[str] nodes: List of nodes serving a replica of the shard.
    :param str range: The shard range in which the document is stored.
    """

    def __init__(
        self,
        nodes: List[str],
        range: str,
    ) -> None:
        """
        Initialize a DocumentShardInfo object.

        :param List[str] nodes: List of nodes serving a replica of the shard.
        :param str range: The shard range in which the document is stored.
        """
        self.nodes = nodes
        self.range = range

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentShardInfo':
        """Initialize a DocumentShardInfo object from a json dictionary."""
        args = {}
        if (nodes := _dict.get('nodes')) is not None:
            args['nodes'] = nodes
        else:
            raise ValueError('Required property \'nodes\' not present in DocumentShardInfo JSON')
        if (range := _dict.get('range')) is not None:
            args['range'] = range
        else:
            raise ValueError('Required property \'range\' not present in DocumentShardInfo JSON')
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


class ExecutionStats:
    """
    Schema for find query execution statistics.

    :param float execution_time_ms: Time to execute the query.
    :param int results_returned: Number of results returned.
    :param int total_docs_examined: Number of documents fetched from the index.
    :param int total_keys_examined: Number of rows scanned in the index.
    :param int total_quorum_docs_examined: Number of documents fetched from the
          primary index with the specified read quorum.
    """

    def __init__(
        self,
        execution_time_ms: float,
        results_returned: int,
        total_docs_examined: int,
        total_keys_examined: int,
        total_quorum_docs_examined: int,
    ) -> None:
        """
        Initialize a ExecutionStats object.

        :param float execution_time_ms: Time to execute the query.
        :param int results_returned: Number of results returned.
        :param int total_docs_examined: Number of documents fetched from the index.
        :param int total_keys_examined: Number of rows scanned in the index.
        :param int total_quorum_docs_examined: Number of documents fetched from the
               primary index with the specified read quorum.
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
        if (execution_time_ms := _dict.get('execution_time_ms')) is not None:
            args['execution_time_ms'] = execution_time_ms
        else:
            raise ValueError('Required property \'execution_time_ms\' not present in ExecutionStats JSON')
        if (results_returned := _dict.get('results_returned')) is not None:
            args['results_returned'] = results_returned
        else:
            raise ValueError('Required property \'results_returned\' not present in ExecutionStats JSON')
        if (total_docs_examined := _dict.get('total_docs_examined')) is not None:
            args['total_docs_examined'] = total_docs_examined
        else:
            raise ValueError('Required property \'total_docs_examined\' not present in ExecutionStats JSON')
        if (total_keys_examined := _dict.get('total_keys_examined')) is not None:
            args['total_keys_examined'] = total_keys_examined
        else:
            raise ValueError('Required property \'total_keys_examined\' not present in ExecutionStats JSON')
        if (total_quorum_docs_examined := _dict.get('total_quorum_docs_examined')) is not None:
            args['total_quorum_docs_examined'] = total_quorum_docs_examined
        else:
            raise ValueError('Required property \'total_quorum_docs_examined\' not present in ExecutionStats JSON')
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


class ExplainResult:
    """
    Schema for information about the index used for a find query.

    :param bool covering: When `true`, the query is answered using the index only
          and no documents are fetched.
    :param str dbname: Schema for a database name.
    :param List[str] fields: Fields that were requested to be projected from the
          document. If no fields were requested to be projected this will be empty and all
          fields will be returned.
    :param IndexInformation index: Schema for information about an index.
    :param List[IndexCandidate] index_candidates: Schema for the list of all the
          other indexes that were not chosen for serving the query.
    :param int limit: The used maximum number of results returned.
    :param ExplainResultMrArgs mrargs: (optional) Arguments passed to the underlying
          view.
    :param ExplainResultOpts opts: Options used for the request.
    :param object partitioned: (optional) Schema for any JSON type.
    :param dict selector: JSON object describing criteria used to select documents.
          The selector specifies fields in the document, and provides an expression to
          evaluate with the field content or other data.
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
          used to combine selectors. A combination operator takes a single argument. The
          argument is either another selector, or an array of selectors.
          * Condition operators: are specific to a field, and are used to evaluate the
          value stored in that field. For instance, the basic `$eq` operator matches when
          the specified field contains a value that is equal to the supplied argument.
          It is important for query performance to use appropriate selectors:
          * Only equality operators such as `$eq`, `$gt`, `$gte`, `$lt`, and `$lte` (but
          not `$ne`) can be used as the basis of a query. You should include at least one
          of these in a selector.
          * Some operators such as `$not`, `$or`, `$in`, and `$regex` cannot be answered
          from an index. For query selectors use these operators in conjunction with
          equality operators or create and use a partial index to reduce the number of
          documents that will need to be scanned.
          See [the Cloudant
          Docs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-operators)for a list of
          all available combination and conditional operators.
          For further reference see [selector
          syntax](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-selector-syntax).
    :param List[SelectorHint] selector_hints: Schema for a list of objects with
          extra information on the selector to provide insights about its usability.
    :param int skip: Skip parameter used.
    """

    def __init__(
        self,
        covering: bool,
        dbname: str,
        fields: List[str],
        index: 'IndexInformation',
        index_candidates: List['IndexCandidate'],
        limit: int,
        opts: 'ExplainResultOpts',
        selector: dict,
        selector_hints: List['SelectorHint'],
        skip: int,
        *,
        mrargs: Optional['ExplainResultMrArgs'] = None,
        partitioned: Optional[object] = None,
    ) -> None:
        """
        Initialize a ExplainResult object.

        :param bool covering: When `true`, the query is answered using the index
               only and no documents are fetched.
        :param str dbname: Schema for a database name.
        :param List[str] fields: Fields that were requested to be projected from
               the document. If no fields were requested to be projected this will be
               empty and all fields will be returned.
        :param IndexInformation index: Schema for information about an index.
        :param List[IndexCandidate] index_candidates: Schema for the list of all
               the other indexes that were not chosen for serving the query.
        :param int limit: The used maximum number of results returned.
        :param ExplainResultOpts opts: Options used for the request.
        :param dict selector: JSON object describing criteria used to select
               documents. The selector specifies fields in the document, and provides an
               expression to evaluate with the field content or other data.
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
               are used to combine selectors. A combination operator takes a single
               argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
               It is important for query performance to use appropriate selectors:
               * Only equality operators such as `$eq`, `$gt`, `$gte`, `$lt`, and `$lte`
               (but not `$ne`) can be used as the basis of a query. You should include at
               least one of these in a selector.
               * Some operators such as `$not`, `$or`, `$in`, and `$regex` cannot be
               answered from an index. For query selectors use these operators in
               conjunction with equality operators or create and use a partial index to
               reduce the number of documents that will need to be scanned.
               See [the Cloudant
               Docs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-operators)for a
               list of all available combination and conditional operators.
               For further reference see [selector
               syntax](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-selector-syntax).
        :param List[SelectorHint] selector_hints: Schema for a list of objects with
               extra information on the selector to provide insights about its usability.
        :param int skip: Skip parameter used.
        :param ExplainResultMrArgs mrargs: (optional) Arguments passed to the
               underlying view.
        :param object partitioned: (optional) Schema for any JSON type.
        """
        self.covering = covering
        self.dbname = dbname
        self.fields = fields
        self.index = index
        self.index_candidates = index_candidates
        self.limit = limit
        self.mrargs = mrargs
        self.opts = opts
        self.partitioned = partitioned
        self.selector = selector
        self.selector_hints = selector_hints
        self.skip = skip

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ExplainResult':
        """Initialize a ExplainResult object from a json dictionary."""
        args = {}
        if (covering := _dict.get('covering')) is not None:
            args['covering'] = covering
        else:
            raise ValueError('Required property \'covering\' not present in ExplainResult JSON')
        if (dbname := _dict.get('dbname')) is not None:
            args['dbname'] = dbname
        else:
            raise ValueError('Required property \'dbname\' not present in ExplainResult JSON')
        if (fields := _dict.get('fields')) is not None:
            args['fields'] = fields
        else:
            raise ValueError('Required property \'fields\' not present in ExplainResult JSON')
        if (index := _dict.get('index')) is not None:
            args['index'] = IndexInformation.from_dict(index)
        else:
            raise ValueError('Required property \'index\' not present in ExplainResult JSON')
        if (index_candidates := _dict.get('index_candidates')) is not None:
            args['index_candidates'] = [IndexCandidate.from_dict(v) for v in index_candidates]
        else:
            raise ValueError('Required property \'index_candidates\' not present in ExplainResult JSON')
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in ExplainResult JSON')
        if (mrargs := _dict.get('mrargs')) is not None:
            args['mrargs'] = ExplainResultMrArgs.from_dict(mrargs)
        if (opts := _dict.get('opts')) is not None:
            args['opts'] = ExplainResultOpts.from_dict(opts)
        else:
            raise ValueError('Required property \'opts\' not present in ExplainResult JSON')
        if (partitioned := _dict.get('partitioned')) is not None:
            args['partitioned'] = partitioned
        if (selector := _dict.get('selector')) is not None:
            args['selector'] = selector
        else:
            raise ValueError('Required property \'selector\' not present in ExplainResult JSON')
        if (selector_hints := _dict.get('selector_hints')) is not None:
            args['selector_hints'] = [SelectorHint.from_dict(v) for v in selector_hints]
        else:
            raise ValueError('Required property \'selector_hints\' not present in ExplainResult JSON')
        if (skip := _dict.get('skip')) is not None:
            args['skip'] = skip
        else:
            raise ValueError('Required property \'skip\' not present in ExplainResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExplainResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'covering') and self.covering is not None:
            _dict['covering'] = self.covering
        if hasattr(self, 'dbname') and self.dbname is not None:
            _dict['dbname'] = self.dbname
        if hasattr(self, 'fields') and self.fields is not None:
            _dict['fields'] = self.fields
        if hasattr(self, 'index') and self.index is not None:
            if isinstance(self.index, dict):
                _dict['index'] = self.index
            else:
                _dict['index'] = self.index.to_dict()
        if hasattr(self, 'index_candidates') and self.index_candidates is not None:
            index_candidates_list = []
            for v in self.index_candidates:
                if isinstance(v, dict):
                    index_candidates_list.append(v)
                else:
                    index_candidates_list.append(v.to_dict())
            _dict['index_candidates'] = index_candidates_list
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'mrargs') and self.mrargs is not None:
            if isinstance(self.mrargs, dict):
                _dict['mrargs'] = self.mrargs
            else:
                _dict['mrargs'] = self.mrargs.to_dict()
        if hasattr(self, 'opts') and self.opts is not None:
            if isinstance(self.opts, dict):
                _dict['opts'] = self.opts
            else:
                _dict['opts'] = self.opts.to_dict()
        if hasattr(self, 'partitioned') and self.partitioned is not None:
            _dict['partitioned'] = self.partitioned
        if hasattr(self, 'selector') and self.selector is not None:
            _dict['selector'] = self.selector
        if hasattr(self, 'selector_hints') and self.selector_hints is not None:
            selector_hints_list = []
            for v in self.selector_hints:
                if isinstance(v, dict):
                    selector_hints_list.append(v)
                else:
                    selector_hints_list.append(v.to_dict())
            _dict['selector_hints'] = selector_hints_list
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


class ExplainResultMrArgs:
    """
    Arguments passed to the underlying view.

    :param object conflicts: Schema for any JSON type.
    :param str direction: Direction parameter passed to the underlying view.
    :param object end_key: Schema for any JSON type.
    :param bool include_docs: A parameter that specifies whether to include the full
          content of the documents in the response in the underlying view.
    :param str partition: Partition parameter passed to the underlying view.
    :param bool reduce: A parameter that specifies returning only documents that
          match any of the specified keys in the underlying view.
    :param bool stable: A parameter that specifies whether the view results should
          be returned form a "stable" set of shards passed to the underlying view.
    :param object start_key: (optional) Schema for any JSON type.
    :param object update: Schema for any JSON type.
    :param str view_type: The type of the underlying view.
    """

    def __init__(
        self,
        conflicts: object,
        direction: str,
        end_key: object,
        include_docs: bool,
        partition: str,
        reduce: bool,
        stable: bool,
        update: object,
        view_type: str,
        *,
        start_key: Optional[object] = None,
    ) -> None:
        """
        Initialize a ExplainResultMrArgs object.

        :param object conflicts: Schema for any JSON type.
        :param str direction: Direction parameter passed to the underlying view.
        :param object end_key: Schema for any JSON type.
        :param bool include_docs: A parameter that specifies whether to include the
               full content of the documents in the response in the underlying view.
        :param str partition: Partition parameter passed to the underlying view.
        :param bool reduce: A parameter that specifies returning only documents
               that match any of the specified keys in the underlying view.
        :param bool stable: A parameter that specifies whether the view results
               should be returned form a "stable" set of shards passed to the underlying
               view.
        :param object update: Schema for any JSON type.
        :param str view_type: The type of the underlying view.
        :param object start_key: (optional) Schema for any JSON type.
        """
        self.conflicts = conflicts
        self.direction = direction
        self.end_key = end_key
        self.include_docs = include_docs
        self.partition = partition
        self.reduce = reduce
        self.stable = stable
        self.start_key = start_key
        self.update = update
        self.view_type = view_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ExplainResultMrArgs':
        """Initialize a ExplainResultMrArgs object from a json dictionary."""
        args = {}
        if (conflicts := _dict.get('conflicts')) is not None:
            args['conflicts'] = conflicts
        else:
            raise ValueError('Required property \'conflicts\' not present in ExplainResultMrArgs JSON')
        if (direction := _dict.get('direction')) is not None:
            args['direction'] = direction
        else:
            raise ValueError('Required property \'direction\' not present in ExplainResultMrArgs JSON')
        if (end_key := _dict.get('end_key')) is not None:
            args['end_key'] = end_key
        else:
            raise ValueError('Required property \'end_key\' not present in ExplainResultMrArgs JSON')
        if (include_docs := _dict.get('include_docs')) is not None:
            args['include_docs'] = include_docs
        else:
            raise ValueError('Required property \'include_docs\' not present in ExplainResultMrArgs JSON')
        if (partition := _dict.get('partition')) is not None:
            args['partition'] = partition
        else:
            raise ValueError('Required property \'partition\' not present in ExplainResultMrArgs JSON')
        if (reduce := _dict.get('reduce')) is not None:
            args['reduce'] = reduce
        else:
            raise ValueError('Required property \'reduce\' not present in ExplainResultMrArgs JSON')
        if (stable := _dict.get('stable')) is not None:
            args['stable'] = stable
        else:
            raise ValueError('Required property \'stable\' not present in ExplainResultMrArgs JSON')
        if (start_key := _dict.get('start_key')) is not None:
            args['start_key'] = start_key
        if (update := _dict.get('update')) is not None:
            args['update'] = update
        else:
            raise ValueError('Required property \'update\' not present in ExplainResultMrArgs JSON')
        if (view_type := _dict.get('view_type')) is not None:
            args['view_type'] = view_type
        else:
            raise ValueError('Required property \'view_type\' not present in ExplainResultMrArgs JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExplainResultMrArgs object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'conflicts') and self.conflicts is not None:
            _dict['conflicts'] = self.conflicts
        if hasattr(self, 'direction') and self.direction is not None:
            _dict['direction'] = self.direction
        if hasattr(self, 'end_key') and self.end_key is not None:
            _dict['end_key'] = self.end_key
        if hasattr(self, 'include_docs') and self.include_docs is not None:
            _dict['include_docs'] = self.include_docs
        if hasattr(self, 'partition') and self.partition is not None:
            _dict['partition'] = self.partition
        if hasattr(self, 'reduce') and self.reduce is not None:
            _dict['reduce'] = self.reduce
        if hasattr(self, 'stable') and self.stable is not None:
            _dict['stable'] = self.stable
        if hasattr(self, 'start_key') and self.start_key is not None:
            _dict['start_key'] = self.start_key
        if hasattr(self, 'update') and self.update is not None:
            _dict['update'] = self.update
        if hasattr(self, 'view_type') and self.view_type is not None:
            _dict['view_type'] = self.view_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ExplainResultMrArgs object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ExplainResultMrArgs') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ExplainResultMrArgs') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DirectionEnum(str, Enum):
        """
        Direction parameter passed to the underlying view.
        """

        FWD = 'fwd'
        REV = 'rev'


    class ViewTypeEnum(str, Enum):
        """
        The type of the underlying view.
        """

        MAP = 'map'
        REDUCE = 'reduce'



class ExplainResultOpts:
    """
    Options used for the request.

    :param str bookmark: Opaque bookmark token used when paginating results.
    :param bool conflicts: Conflicts used in the request query.
    :param bool execution_stats: Execution statistics used in the request query.
    :param List[str] fields: JSON array that uses the field syntax. Use this
          parameter to specify which fields of a document must be returned. If it is
          omitted or empty, the entire document is returned.
    :param int limit: Limit used in the request query.
    :param str partition: On which database partition the request was used. If it
          was not used on a database partition, it returns with `""`.
    :param int r: The read quorum that is needed for the result.
    :param int skip: Skip used in the request query.
    :param object sort: Schema for any JSON type.
    :param bool stable: Stable used in the request query.
    :param bool stale: Deprecated: Stale used in the request query.
    :param bool update: Update used in the request query.
    :param List[str] use_index: Use index used in the request query.
    """

    def __init__(
        self,
        bookmark: str,
        conflicts: bool,
        execution_stats: bool,
        fields: List[str],
        limit: int,
        partition: str,
        r: int,
        skip: int,
        sort: object,
        stable: bool,
        stale: bool,
        update: bool,
        use_index: List[str],
    ) -> None:
        """
        Initialize a ExplainResultOpts object.

        :param str bookmark: Opaque bookmark token used when paginating results.
        :param bool conflicts: Conflicts used in the request query.
        :param bool execution_stats: Execution statistics used in the request
               query.
        :param List[str] fields: JSON array that uses the field syntax. Use this
               parameter to specify which fields of a document must be returned. If it is
               omitted or empty, the entire document is returned.
        :param int limit: Limit used in the request query.
        :param str partition: On which database partition the request was used. If
               it was not used on a database partition, it returns with `""`.
        :param int r: The read quorum that is needed for the result.
        :param int skip: Skip used in the request query.
        :param object sort: Schema for any JSON type.
        :param bool stable: Stable used in the request query.
        :param bool stale: Deprecated: Stale used in the request query.
        :param bool update: Update used in the request query.
        :param List[str] use_index: Use index used in the request query.
        """
        self.bookmark = bookmark
        self.conflicts = conflicts
        self.execution_stats = execution_stats
        self.fields = fields
        self.limit = limit
        self.partition = partition
        self.r = r
        self.skip = skip
        self.sort = sort
        self.stable = stable
        self.stale = stale
        self.update = update
        self.use_index = use_index

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ExplainResultOpts':
        """Initialize a ExplainResultOpts object from a json dictionary."""
        args = {}
        if (bookmark := _dict.get('bookmark')) is not None:
            args['bookmark'] = bookmark
        else:
            raise ValueError('Required property \'bookmark\' not present in ExplainResultOpts JSON')
        if (conflicts := _dict.get('conflicts')) is not None:
            args['conflicts'] = conflicts
        else:
            raise ValueError('Required property \'conflicts\' not present in ExplainResultOpts JSON')
        if (execution_stats := _dict.get('execution_stats')) is not None:
            args['execution_stats'] = execution_stats
        else:
            raise ValueError('Required property \'execution_stats\' not present in ExplainResultOpts JSON')
        if (fields := _dict.get('fields')) is not None:
            args['fields'] = fields
        else:
            raise ValueError('Required property \'fields\' not present in ExplainResultOpts JSON')
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in ExplainResultOpts JSON')
        if (partition := _dict.get('partition')) is not None:
            args['partition'] = partition
        else:
            raise ValueError('Required property \'partition\' not present in ExplainResultOpts JSON')
        if (r := _dict.get('r')) is not None:
            args['r'] = r
        else:
            raise ValueError('Required property \'r\' not present in ExplainResultOpts JSON')
        if (skip := _dict.get('skip')) is not None:
            args['skip'] = skip
        else:
            raise ValueError('Required property \'skip\' not present in ExplainResultOpts JSON')
        if (sort := _dict.get('sort')) is not None:
            args['sort'] = sort
        else:
            raise ValueError('Required property \'sort\' not present in ExplainResultOpts JSON')
        if (stable := _dict.get('stable')) is not None:
            args['stable'] = stable
        else:
            raise ValueError('Required property \'stable\' not present in ExplainResultOpts JSON')
        if (stale := _dict.get('stale')) is not None:
            args['stale'] = stale
        else:
            raise ValueError('Required property \'stale\' not present in ExplainResultOpts JSON')
        if (update := _dict.get('update')) is not None:
            args['update'] = update
        else:
            raise ValueError('Required property \'update\' not present in ExplainResultOpts JSON')
        if (use_index := _dict.get('use_index')) is not None:
            args['use_index'] = use_index
        else:
            raise ValueError('Required property \'use_index\' not present in ExplainResultOpts JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExplainResultOpts object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'bookmark') and self.bookmark is not None:
            _dict['bookmark'] = self.bookmark
        if hasattr(self, 'conflicts') and self.conflicts is not None:
            _dict['conflicts'] = self.conflicts
        if hasattr(self, 'execution_stats') and self.execution_stats is not None:
            _dict['execution_stats'] = self.execution_stats
        if hasattr(self, 'fields') and self.fields is not None:
            _dict['fields'] = self.fields
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'partition') and self.partition is not None:
            _dict['partition'] = self.partition
        if hasattr(self, 'r') and self.r is not None:
            _dict['r'] = self.r
        if hasattr(self, 'skip') and self.skip is not None:
            _dict['skip'] = self.skip
        if hasattr(self, 'sort') and self.sort is not None:
            _dict['sort'] = self.sort
        if hasattr(self, 'stable') and self.stable is not None:
            _dict['stable'] = self.stable
        if hasattr(self, 'stale') and self.stale is not None:
            _dict['stale'] = self.stale
        if hasattr(self, 'update') and self.update is not None:
            _dict['update'] = self.update
        if hasattr(self, 'use_index') and self.use_index is not None:
            _dict['use_index'] = self.use_index
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ExplainResultOpts object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ExplainResultOpts') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ExplainResultOpts') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FindResult:
    """
    Schema for the result of a query find operation.

    :param str bookmark: Opaque bookmark token used when paginating results.
    :param List[Document] docs: Documents matching the selector.
    :param ExecutionStats execution_stats: (optional) Schema for find query
          execution statistics.
    :param str warning: (optional) warning.
    """

    def __init__(
        self,
        bookmark: str,
        docs: List['Document'],
        *,
        execution_stats: Optional['ExecutionStats'] = None,
        warning: Optional[str] = None,
    ) -> None:
        """
        Initialize a FindResult object.

        :param str bookmark: Opaque bookmark token used when paginating results.
        :param List[Document] docs: Documents matching the selector.
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
        if (bookmark := _dict.get('bookmark')) is not None:
            args['bookmark'] = bookmark
        else:
            raise ValueError('Required property \'bookmark\' not present in FindResult JSON')
        if (docs := _dict.get('docs')) is not None:
            args['docs'] = [Document.from_dict(v) for v in docs]
        else:
            raise ValueError('Required property \'docs\' not present in FindResult JSON')
        if (execution_stats := _dict.get('execution_stats')) is not None:
            args['execution_stats'] = ExecutionStats.from_dict(execution_stats)
        if (warning := _dict.get('warning')) is not None:
            args['warning'] = warning
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
            docs_list = []
            for v in self.docs:
                if isinstance(v, dict):
                    docs_list.append(v)
                else:
                    docs_list.append(v.to_dict())
            _dict['docs'] = docs_list
        if hasattr(self, 'execution_stats') and self.execution_stats is not None:
            if isinstance(self.execution_stats, dict):
                _dict['execution_stats'] = self.execution_stats
            else:
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


class IndexAnalysis:
    """
    Schema for detailed explanation of why the specific index was excluded by the query
    planner.

    :param bool covering: When `true`, the query is answered using the index only
          and no documents are fetched.
    :param int ranking: A position of the unused index based on its potential
          relevance to the query.
    :param List[IndexAnalysisExclusionReason] reasons: A list of reasons explaining
          why index was not chosen for the query.
    :param bool usable: Indicates whether an index can still be used for the query.
    """

    def __init__(
        self,
        covering: bool,
        ranking: int,
        reasons: List['IndexAnalysisExclusionReason'],
        usable: bool,
    ) -> None:
        """
        Initialize a IndexAnalysis object.

        :param bool covering: When `true`, the query is answered using the index
               only and no documents are fetched.
        :param int ranking: A position of the unused index based on its potential
               relevance to the query.
        :param List[IndexAnalysisExclusionReason] reasons: A list of reasons
               explaining why index was not chosen for the query.
        :param bool usable: Indicates whether an index can still be used for the
               query.
        """
        self.covering = covering
        self.ranking = ranking
        self.reasons = reasons
        self.usable = usable

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IndexAnalysis':
        """Initialize a IndexAnalysis object from a json dictionary."""
        args = {}
        if (covering := _dict.get('covering')) is not None:
            args['covering'] = covering
        else:
            raise ValueError('Required property \'covering\' not present in IndexAnalysis JSON')
        if (ranking := _dict.get('ranking')) is not None:
            args['ranking'] = ranking
        else:
            raise ValueError('Required property \'ranking\' not present in IndexAnalysis JSON')
        if (reasons := _dict.get('reasons')) is not None:
            args['reasons'] = [IndexAnalysisExclusionReason.from_dict(v) for v in reasons]
        else:
            raise ValueError('Required property \'reasons\' not present in IndexAnalysis JSON')
        if (usable := _dict.get('usable')) is not None:
            args['usable'] = usable
        else:
            raise ValueError('Required property \'usable\' not present in IndexAnalysis JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IndexAnalysis object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'covering') and self.covering is not None:
            _dict['covering'] = self.covering
        if hasattr(self, 'ranking') and self.ranking is not None:
            _dict['ranking'] = self.ranking
        if hasattr(self, 'reasons') and self.reasons is not None:
            reasons_list = []
            for v in self.reasons:
                if isinstance(v, dict):
                    reasons_list.append(v)
                else:
                    reasons_list.append(v.to_dict())
            _dict['reasons'] = reasons_list
        if hasattr(self, 'usable') and self.usable is not None:
            _dict['usable'] = self.usable
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IndexAnalysis object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IndexAnalysis') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IndexAnalysis') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class IndexAnalysisExclusionReason:
    """
    A reason for index's exclusion.

    :param str name: A reason code for index's exclusion.
          The full list of possible reason codes is following:
          * alphabetically_comes_after: json
            There is another suitable index whose name comes before that of this index.
          * empty_selector: text
          "text" indexes do not support queries with empty selectors.
          * excluded_by_user: any use_index was used to manually specify the index.
          * field_mismatch: any Fields in "selector" of the query do match with the fields
          available in the index.
          * is_partial: json, text Partial indexes can be selected only manually.
          * less_overlap: json There is a better match of fields available within the
          indexes for the query.
          * needs_text_search: json The use of the $text operator requires a "text" index.
          * scope_mismatch: json The scope of the query and the index is not the same.
          * sort_order_mismatch: json, special Fields in "sort" of the query do not match
          with the fields available in the index.
          * too_many_fields: json The index has more fields than the chosen one.
          * unfavored_type: any The type of the index is not preferred.
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        """
        Initialize a IndexAnalysisExclusionReason object.

        :param str name: A reason code for index's exclusion.
               The full list of possible reason codes is following:
               * alphabetically_comes_after: json
                 There is another suitable index whose name comes before that of this
               index.
               * empty_selector: text
               "text" indexes do not support queries with empty selectors.
               * excluded_by_user: any use_index was used to manually specify the index.
               * field_mismatch: any Fields in "selector" of the query do match with the
               fields available in the index.
               * is_partial: json, text Partial indexes can be selected only manually.
               * less_overlap: json There is a better match of fields available within the
               indexes for the query.
               * needs_text_search: json The use of the $text operator requires a "text"
               index.
               * scope_mismatch: json The scope of the query and the index is not the
               same.
               * sort_order_mismatch: json, special Fields in "sort" of the query do not
               match with the fields available in the index.
               * too_many_fields: json The index has more fields than the chosen one.
               * unfavored_type: any The type of the index is not preferred.
        """
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IndexAnalysisExclusionReason':
        """Initialize a IndexAnalysisExclusionReason object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in IndexAnalysisExclusionReason JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IndexAnalysisExclusionReason object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IndexAnalysisExclusionReason object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IndexAnalysisExclusionReason') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IndexAnalysisExclusionReason') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class NameEnum(str, Enum):
        """
        A reason code for index's exclusion.
        The full list of possible reason codes is following:
        * alphabetically_comes_after: json
          There is another suitable index whose name comes before that of this index.
        * empty_selector: text
        "text" indexes do not support queries with empty selectors.
        * excluded_by_user: any use_index was used to manually specify the index.
        * field_mismatch: any Fields in "selector" of the query do match with the fields
        available in the index.
        * is_partial: json, text Partial indexes can be selected only manually.
        * less_overlap: json There is a better match of fields available within the
        indexes for the query.
        * needs_text_search: json The use of the $text operator requires a "text" index.
        * scope_mismatch: json The scope of the query and the index is not the same.
        * sort_order_mismatch: json, special Fields in "sort" of the query do not match
        with the fields available in the index.
        * too_many_fields: json The index has more fields than the chosen one.
        * unfavored_type: any The type of the index is not preferred.
        """

        ALPHABETICALLY_COMES_AFTER = 'alphabetically_comes_after'
        EMPTY_SELECTOR = 'empty_selector'
        EXCLUDED_BY_USER = 'excluded_by_user'
        FIELD_MISMATCH = 'field_mismatch'
        IS_PARTIAL = 'is_partial'
        LESS_OVERLAP = 'less_overlap'
        NEEDS_TEXT_SEARCH = 'needs_text_search'
        SCOPE_MISMATCH = 'scope_mismatch'
        SORT_ORDER_MISMATCH = 'sort_order_mismatch'
        TOO_MANY_FIELDS = 'too_many_fields'
        UNFAVORED_TYPE = 'unfavored_type'



class IndexCandidate:
    """
    Schema for an index that was not chosen for serving the query with the reason for the
    exclusion.

    :param IndexAnalysis analysis: Schema for detailed explanation of why the
          specific index was excluded by the query planner.
    :param IndexInformation index: Schema for information about an index.
    """

    def __init__(
        self,
        analysis: 'IndexAnalysis',
        index: 'IndexInformation',
    ) -> None:
        """
        Initialize a IndexCandidate object.

        :param IndexAnalysis analysis: Schema for detailed explanation of why the
               specific index was excluded by the query planner.
        :param IndexInformation index: Schema for information about an index.
        """
        self.analysis = analysis
        self.index = index

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IndexCandidate':
        """Initialize a IndexCandidate object from a json dictionary."""
        args = {}
        if (analysis := _dict.get('analysis')) is not None:
            args['analysis'] = IndexAnalysis.from_dict(analysis)
        else:
            raise ValueError('Required property \'analysis\' not present in IndexCandidate JSON')
        if (index := _dict.get('index')) is not None:
            args['index'] = IndexInformation.from_dict(index)
        else:
            raise ValueError('Required property \'index\' not present in IndexCandidate JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IndexCandidate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'analysis') and self.analysis is not None:
            if isinstance(self.analysis, dict):
                _dict['analysis'] = self.analysis
            else:
                _dict['analysis'] = self.analysis.to_dict()
        if hasattr(self, 'index') and self.index is not None:
            if isinstance(self.index, dict):
                _dict['index'] = self.index
            else:
                _dict['index'] = self.index.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IndexCandidate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IndexCandidate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IndexCandidate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class IndexDefinition:
    """
    Schema for a `json` or `text` query index definition. Indexes of type `text` have
    additional configuration properties that do not apply to `json` indexes, these are:
    * `default_analyzer` - the default text analyzer to use * `default_field` - whether to
    index the text in all document fields and what analyzer to use for that purpose.

    :param Analyzer default_analyzer: (optional) Schema for a full text search
          analyzer.
    :param IndexTextOperatorDefaultField default_field: (optional) Schema for the
          text index default field configuration. The default field is used to index the
          text of all fields within a document for use with the `$text` operator.
    :param List[IndexField] fields: List of field objects to index.  Nested fields
          are also allowed, e.g. `person.name`.
          For "json" type indexes each object is a mapping of field name to sort direction
          (asc or desc).
          For "text" type indexes each object has a `name` property of the field name and
          a `type` property of the field type (string, number, or boolean).
    :param bool index_array_lengths: (optional) Whether to scan every document for
          arrays and store the length for each array found. Set the index_array_lengths
          field to false if:
          * You do not need to know the length of an array. * You do not use the `$size`
          operator. * The documents in your database are complex, or not completely under
          your control. As a result, it is difficult to estimate the impact of the extra
          processing that is needed to determine and store the arrays lengths.
    :param dict partial_filter_selector: (optional) JSON object describing criteria
          used to select documents. The selector specifies fields in the document, and
          provides an expression to evaluate with the field content or other data.
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
          used to combine selectors. A combination operator takes a single argument. The
          argument is either another selector, or an array of selectors.
          * Condition operators: are specific to a field, and are used to evaluate the
          value stored in that field. For instance, the basic `$eq` operator matches when
          the specified field contains a value that is equal to the supplied argument.
          It is important for query performance to use appropriate selectors:
          * Only equality operators such as `$eq`, `$gt`, `$gte`, `$lt`, and `$lte` (but
          not `$ne`) can be used as the basis of a query. You should include at least one
          of these in a selector.
          * Some operators such as `$not`, `$or`, `$in`, and `$regex` cannot be answered
          from an index. For query selectors use these operators in conjunction with
          equality operators or create and use a partial index to reduce the number of
          documents that will need to be scanned.
          See [the Cloudant
          Docs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-operators)for a list of
          all available combination and conditional operators.
          For further reference see [selector
          syntax](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-selector-syntax).
    """

    def __init__(
        self,
        fields: List['IndexField'],
        *,
        default_analyzer: Optional['Analyzer'] = None,
        default_field: Optional['IndexTextOperatorDefaultField'] = None,
        index_array_lengths: Optional[bool] = None,
        partial_filter_selector: Optional[dict] = None,
    ) -> None:
        """
        Initialize a IndexDefinition object.

        :param List[IndexField] fields: List of field objects to index.  Nested
               fields are also allowed, e.g. `person.name`.
               For "json" type indexes each object is a mapping of field name to sort
               direction (asc or desc).
               For "text" type indexes each object has a `name` property of the field name
               and a `type` property of the field type (string, number, or boolean).
        :param Analyzer default_analyzer: (optional) Schema for a full text search
               analyzer.
        :param IndexTextOperatorDefaultField default_field: (optional) Schema for
               the text index default field configuration. The default field is used to
               index the text of all fields within a document for use with the `$text`
               operator.
        :param bool index_array_lengths: (optional) Whether to scan every document
               for arrays and store the length for each array found. Set the
               index_array_lengths field to false if:
               * You do not need to know the length of an array. * You do not use the
               `$size` operator. * The documents in your database are complex, or not
               completely under your control. As a result, it is difficult to estimate the
               impact of the extra processing that is needed to determine and store the
               arrays lengths.
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
               are used to combine selectors. A combination operator takes a single
               argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
               It is important for query performance to use appropriate selectors:
               * Only equality operators such as `$eq`, `$gt`, `$gte`, `$lt`, and `$lte`
               (but not `$ne`) can be used as the basis of a query. You should include at
               least one of these in a selector.
               * Some operators such as `$not`, `$or`, `$in`, and `$regex` cannot be
               answered from an index. For query selectors use these operators in
               conjunction with equality operators or create and use a partial index to
               reduce the number of documents that will need to be scanned.
               See [the Cloudant
               Docs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-operators)for a
               list of all available combination and conditional operators.
               For further reference see [selector
               syntax](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-selector-syntax).
        """
        self.default_analyzer = default_analyzer
        self.default_field = default_field
        self.fields = fields
        self.index_array_lengths = index_array_lengths
        self.partial_filter_selector = partial_filter_selector

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IndexDefinition':
        """Initialize a IndexDefinition object from a json dictionary."""
        args = {}
        if (default_analyzer := _dict.get('default_analyzer')) is not None:
            args['default_analyzer'] = Analyzer.from_dict(default_analyzer)
        if (default_field := _dict.get('default_field')) is not None:
            args['default_field'] = IndexTextOperatorDefaultField.from_dict(default_field)
        if (fields := _dict.get('fields')) is not None:
            args['fields'] = [IndexField.from_dict(v) for v in fields]
        else:
            raise ValueError('Required property \'fields\' not present in IndexDefinition JSON')
        if (index_array_lengths := _dict.get('index_array_lengths')) is not None:
            args['index_array_lengths'] = index_array_lengths
        if (partial_filter_selector := _dict.get('partial_filter_selector')) is not None:
            args['partial_filter_selector'] = partial_filter_selector
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IndexDefinition object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'default_analyzer') and self.default_analyzer is not None:
            if isinstance(self.default_analyzer, dict):
                _dict['default_analyzer'] = self.default_analyzer
            else:
                _dict['default_analyzer'] = self.default_analyzer.to_dict()
        if hasattr(self, 'default_field') and self.default_field is not None:
            if isinstance(self.default_field, dict):
                _dict['default_field'] = self.default_field
            else:
                _dict['default_field'] = self.default_field.to_dict()
        if hasattr(self, 'fields') and self.fields is not None:
            fields_list = []
            for v in self.fields:
                if isinstance(v, dict):
                    fields_list.append(v)
                else:
                    fields_list.append(v.to_dict())
            _dict['fields'] = fields_list
        if hasattr(self, 'index_array_lengths') and self.index_array_lengths is not None:
            _dict['index_array_lengths'] = self.index_array_lengths
        if hasattr(self, 'partial_filter_selector') and self.partial_filter_selector is not None:
            _dict['partial_filter_selector'] = self.partial_filter_selector
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


class IndexField:
    """
    Schema for indexed fields for use with declarative JSON query.

    :param str name: (optional) Name of the field.
    :param str type: (optional) The type of the named field.

    This type supports additional properties of type str. Schema for sort direction.
    """

    # The set of defined properties for the class
    _properties = frozenset(['name', 'type'])

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        type: Optional[str] = None,
        **kwargs: Optional[str],
    ) -> None:
        """
        Initialize a IndexField object.

        :param str name: (optional) Name of the field.
        :param str type: (optional) The type of the named field.
        :param str **kwargs: (optional) Schema for sort direction.
        """
        self.name = name
        self.type = type
        for k, v in kwargs.items():
            if k not in IndexField._properties:
                if not isinstance(v, str):
                    raise ValueError('Value for additional property {} must be of type str'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(k))

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IndexField':
        """Initialize a IndexField object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        for k, v in _dict.items():
            if k not in cls._properties:
                    if not isinstance(v, str):
                        raise ValueError('Value for additional property {} must be of type str'.format(k))
                    args[k] = v
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
        for k in [_k for _k in vars(self).keys() if _k not in IndexField._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of IndexField in the form of a dict."""
        _dict = {}
        for k in [_k for _k in vars(self).keys() if _k not in IndexField._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of IndexField"""
        for k in [_k for _k in vars(self).keys() if _k not in IndexField._properties]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in IndexField._properties:
                if not isinstance(v, str):
                    raise ValueError('Value for additional property {} must be of type str'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(k))

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



class IndexInformation:
    """
    Schema for information about an index.

    :param str ddoc: Schema for a nullable design document ID including a `_design/`
          prefix.
    :param IndexDefinition def_: Schema for a `json` or `text` query index
          definition. Indexes of type `text` have additional configuration properties that
          do not apply to `json` indexes, these are:
          * `default_analyzer` - the default text analyzer to use * `default_field` -
          whether to index the text in all document fields and what analyzer to use for
          that purpose.
    :param str name: Index name.
    :param bool partitioned: (optional) Indicates if index is partitioned.
    :param str type: Schema for the type of an index.
    """

    def __init__(
        self,
        ddoc: str,
        def_: 'IndexDefinition',
        name: str,
        type: str,
        *,
        partitioned: Optional[bool] = None,
    ) -> None:
        """
        Initialize a IndexInformation object.

        :param str ddoc: Schema for a nullable design document ID including a
               `_design/` prefix.
        :param IndexDefinition def_: Schema for a `json` or `text` query index
               definition. Indexes of type `text` have additional configuration properties
               that do not apply to `json` indexes, these are:
               * `default_analyzer` - the default text analyzer to use * `default_field` -
               whether to index the text in all document fields and what analyzer to use
               for that purpose.
        :param str name: Index name.
        :param str type: Schema for the type of an index.
        :param bool partitioned: (optional) Indicates if index is partitioned.
        """
        self.ddoc = ddoc
        self.def_ = def_
        self.name = name
        self.partitioned = partitioned
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IndexInformation':
        """Initialize a IndexInformation object from a json dictionary."""
        args = {}
        if (ddoc := _dict.get('ddoc')) is not None:
            args['ddoc'] = ddoc
        else:
            raise ValueError('Required property \'ddoc\' not present in IndexInformation JSON')
        if (def_ := _dict.get('def')) is not None:
            args['def_'] = IndexDefinition.from_dict(def_)
        else:
            raise ValueError('Required property \'def\' not present in IndexInformation JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in IndexInformation JSON')
        if (partitioned := _dict.get('partitioned')) is not None:
            args['partitioned'] = partitioned
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in IndexInformation JSON')
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
            if isinstance(self.def_, dict):
                _dict['def'] = self.def_
            else:
                _dict['def'] = self.def_.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'partitioned') and self.partitioned is not None:
            _dict['partitioned'] = self.partitioned
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



class IndexResult:
    """
    Schema for the result of creating an index.

    :param str id: Id of the design document the index was created in.
    :param str name: Name of the index created.
    :param str result: Flag to show whether the index was created or one already
          exists.
    """

    def __init__(
        self,
        id: str,
        name: str,
        result: str,
    ) -> None:
        """
        Initialize a IndexResult object.

        :param str id: Id of the design document the index was created in.
        :param str name: Name of the index created.
        :param str result: Flag to show whether the index was created or one
               already exists.
        """
        self.id = id
        self.name = name
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IndexResult':
        """Initialize a IndexResult object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in IndexResult JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in IndexResult JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = result
        else:
            raise ValueError('Required property \'result\' not present in IndexResult JSON')
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



class IndexTextOperatorDefaultField:
    """
    Schema for the text index default field configuration. The default field is used to
    index the text of all fields within a document for use with the `$text` operator.

    :param Analyzer analyzer: (optional) Schema for a full text search analyzer.
    :param bool enabled: (optional) Whether or not the default_field is enabled.
    """

    def __init__(
        self,
        *,
        analyzer: Optional['Analyzer'] = None,
        enabled: Optional[bool] = None,
    ) -> None:
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
        if (analyzer := _dict.get('analyzer')) is not None:
            args['analyzer'] = Analyzer.from_dict(analyzer)
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IndexTextOperatorDefaultField object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'analyzer') and self.analyzer is not None:
            if isinstance(self.analyzer, dict):
                _dict['analyzer'] = self.analyzer
            else:
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


class IndexesInformation:
    """
    Schema for information about the indexes in a database.

    :param int total_rows: Total number of query indexes in the database.
    :param List[IndexInformation] indexes: Indexes.
    """

    def __init__(
        self,
        total_rows: int,
        indexes: List['IndexInformation'],
    ) -> None:
        """
        Initialize a IndexesInformation object.

        :param int total_rows: Total number of query indexes in the database.
        :param List[IndexInformation] indexes: Indexes.
        """
        self.total_rows = total_rows
        self.indexes = indexes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IndexesInformation':
        """Initialize a IndexesInformation object from a json dictionary."""
        args = {}
        if (total_rows := _dict.get('total_rows')) is not None:
            args['total_rows'] = total_rows
        else:
            raise ValueError('Required property \'total_rows\' not present in IndexesInformation JSON')
        if (indexes := _dict.get('indexes')) is not None:
            args['indexes'] = [IndexInformation.from_dict(v) for v in indexes]
        else:
            raise ValueError('Required property \'indexes\' not present in IndexesInformation JSON')
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
            indexes_list = []
            for v in self.indexes:
                if isinstance(v, dict):
                    indexes_list.append(v)
                else:
                    indexes_list.append(v.to_dict())
            _dict['indexes'] = indexes_list
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


class MembershipInformation:
    """
    Schema for information about known nodes and cluster membership.

    :param List[str] all_nodes: List of nodes this node knows about, including the
          ones that are part of the cluster.
    :param List[str] cluster_nodes: All cluster nodes.
    """

    def __init__(
        self,
        all_nodes: List[str],
        cluster_nodes: List[str],
    ) -> None:
        """
        Initialize a MembershipInformation object.

        :param List[str] all_nodes: List of nodes this node knows about, including
               the ones that are part of the cluster.
        :param List[str] cluster_nodes: All cluster nodes.
        """
        self.all_nodes = all_nodes
        self.cluster_nodes = cluster_nodes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MembershipInformation':
        """Initialize a MembershipInformation object from a json dictionary."""
        args = {}
        if (all_nodes := _dict.get('all_nodes')) is not None:
            args['all_nodes'] = all_nodes
        else:
            raise ValueError('Required property \'all_nodes\' not present in MembershipInformation JSON')
        if (cluster_nodes := _dict.get('cluster_nodes')) is not None:
            args['cluster_nodes'] = cluster_nodes
        else:
            raise ValueError('Required property \'cluster_nodes\' not present in MembershipInformation JSON')
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


class Ok:
    """
    Schema for an OK result.

    :param bool ok: (optional) ok.
    """

    def __init__(
        self,
        *,
        ok: Optional[bool] = None,
    ) -> None:
        """
        Initialize a Ok object.

        :param bool ok: (optional) ok.
        """
        self.ok = ok

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Ok':
        """Initialize a Ok object from a json dictionary."""
        args = {}
        if (ok := _dict.get('ok')) is not None:
            args['ok'] = ok
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


class PartitionInformation:
    """
    Schema for information about a database partition.

    :param str db_name: Schema for a database name.
    :param int doc_count: A count of the documents in the specified database
          partition.
    :param int doc_del_count: Number of deleted documents.
    :param str partition: Schema for a partition key.
    :param PartitionInformationIndexes partitioned_indexes: (optional) Schema for
          information about the partition index count and limit in a database.
    :param PartitionInformationSizes sizes: The size of active and external data, in
          bytes.
    """

    def __init__(
        self,
        db_name: str,
        doc_count: int,
        doc_del_count: int,
        partition: str,
        sizes: 'PartitionInformationSizes',
        *,
        partitioned_indexes: Optional['PartitionInformationIndexes'] = None,
    ) -> None:
        """
        Initialize a PartitionInformation object.

        :param str db_name: Schema for a database name.
        :param int doc_count: A count of the documents in the specified database
               partition.
        :param int doc_del_count: Number of deleted documents.
        :param str partition: Schema for a partition key.
        :param PartitionInformationSizes sizes: The size of active and external
               data, in bytes.
        :param PartitionInformationIndexes partitioned_indexes: (optional) Schema
               for information about the partition index count and limit in a database.
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
        if (db_name := _dict.get('db_name')) is not None:
            args['db_name'] = db_name
        else:
            raise ValueError('Required property \'db_name\' not present in PartitionInformation JSON')
        if (doc_count := _dict.get('doc_count')) is not None:
            args['doc_count'] = doc_count
        else:
            raise ValueError('Required property \'doc_count\' not present in PartitionInformation JSON')
        if (doc_del_count := _dict.get('doc_del_count')) is not None:
            args['doc_del_count'] = doc_del_count
        else:
            raise ValueError('Required property \'doc_del_count\' not present in PartitionInformation JSON')
        if (partition := _dict.get('partition')) is not None:
            args['partition'] = partition
        else:
            raise ValueError('Required property \'partition\' not present in PartitionInformation JSON')
        if (partitioned_indexes := _dict.get('partitioned_indexes')) is not None:
            args['partitioned_indexes'] = PartitionInformationIndexes.from_dict(partitioned_indexes)
        if (sizes := _dict.get('sizes')) is not None:
            args['sizes'] = PartitionInformationSizes.from_dict(sizes)
        else:
            raise ValueError('Required property \'sizes\' not present in PartitionInformation JSON')
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
            if isinstance(self.partitioned_indexes, dict):
                _dict['partitioned_indexes'] = self.partitioned_indexes
            else:
                _dict['partitioned_indexes'] = self.partitioned_indexes.to_dict()
        if hasattr(self, 'sizes') and self.sizes is not None:
            if isinstance(self.sizes, dict):
                _dict['sizes'] = self.sizes
            else:
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


class PartitionInformationIndexes:
    """
    Schema for information about the partition index count and limit in a database.

    :param int count: (optional) Total count of the partitioned indexes.
    :param PartitionInformationIndexesIndexes indexes: (optional) The count
          breakdown of partitioned indexes.
    :param int limit: (optional) The partitioned index limit.
    """

    def __init__(
        self,
        *,
        count: Optional[int] = None,
        indexes: Optional['PartitionInformationIndexesIndexes'] = None,
        limit: Optional[int] = None,
    ) -> None:
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
        if (count := _dict.get('count')) is not None:
            args['count'] = count
        if (indexes := _dict.get('indexes')) is not None:
            args['indexes'] = PartitionInformationIndexesIndexes.from_dict(indexes)
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
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
            if isinstance(self.indexes, dict):
                _dict['indexes'] = self.indexes
            else:
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


class PartitionInformationIndexesIndexes:
    """
    The count breakdown of partitioned indexes.

    :param int search: (optional) Number of partitioned search indexes.
    :param int view: (optional) Number of partitioned view indexes.
    """

    def __init__(
        self,
        *,
        search: Optional[int] = None,
        view: Optional[int] = None,
    ) -> None:
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
        if (search := _dict.get('search')) is not None:
            args['search'] = search
        if (view := _dict.get('view')) is not None:
            args['view'] = view
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


class PartitionInformationSizes:
    """
    The size of active and external data, in bytes.

    :param int active: (optional) The size of live data inside the database, in
          bytes.
    :param int external: (optional) The uncompressed size of database contents in
          bytes.
    """

    def __init__(
        self,
        *,
        active: Optional[int] = None,
        external: Optional[int] = None,
    ) -> None:
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
        if (active := _dict.get('active')) is not None:
            args['active'] = active
        if (external := _dict.get('external')) is not None:
            args['external'] = external
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


class PartitionedIndexesDetailedInformation:
    """
    Number of partitioned indexes by type.

    :param int search: (optional) Number of partitioned indexes of search type.
    :param int view: (optional) Number of partitioned indexes of view type.
    """

    def __init__(
        self,
        *,
        search: Optional[int] = None,
        view: Optional[int] = None,
    ) -> None:
        """
        Initialize a PartitionedIndexesDetailedInformation object.

        :param int search: (optional) Number of partitioned indexes of search type.
        :param int view: (optional) Number of partitioned indexes of view type.
        """
        self.search = search
        self.view = view

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PartitionedIndexesDetailedInformation':
        """Initialize a PartitionedIndexesDetailedInformation object from a json dictionary."""
        args = {}
        if (search := _dict.get('search')) is not None:
            args['search'] = search
        if (view := _dict.get('view')) is not None:
            args['view'] = view
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PartitionedIndexesDetailedInformation object from a json dictionary."""
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
        """Return a `str` version of this PartitionedIndexesDetailedInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PartitionedIndexesDetailedInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PartitionedIndexesDetailedInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PartitionedIndexesInformation:
    """
    Information about database's partitioned indexes.

    :param int count: (optional) Total number of partitioned indexes in the
          database.
    :param PartitionedIndexesDetailedInformation indexes: (optional) Number of
          partitioned indexes by type.
    :param int limit: (optional) Maximum allowed number of partitioned indexes in
          the database.
    """

    def __init__(
        self,
        *,
        count: Optional[int] = None,
        indexes: Optional['PartitionedIndexesDetailedInformation'] = None,
        limit: Optional[int] = None,
    ) -> None:
        """
        Initialize a PartitionedIndexesInformation object.

        :param int count: (optional) Total number of partitioned indexes in the
               database.
        :param PartitionedIndexesDetailedInformation indexes: (optional) Number of
               partitioned indexes by type.
        :param int limit: (optional) Maximum allowed number of partitioned indexes
               in the database.
        """
        self.count = count
        self.indexes = indexes
        self.limit = limit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PartitionedIndexesInformation':
        """Initialize a PartitionedIndexesInformation object from a json dictionary."""
        args = {}
        if (count := _dict.get('count')) is not None:
            args['count'] = count
        if (indexes := _dict.get('indexes')) is not None:
            args['indexes'] = PartitionedIndexesDetailedInformation.from_dict(indexes)
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PartitionedIndexesInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'indexes') and self.indexes is not None:
            if isinstance(self.indexes, dict):
                _dict['indexes'] = self.indexes
            else:
                _dict['indexes'] = self.indexes.to_dict()
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PartitionedIndexesInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PartitionedIndexesInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PartitionedIndexesInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ReplicationCreateTargetParameters:
    """
    Request parameters to use during target database creation.

    :param int n: (optional) Schema for the number of replicas of a database in a
          cluster. The cluster is using the default value and it cannot be changed by the
          user.
    :param bool partitioned: (optional) Parameter to specify whether to enable
          database partitions when creating the target database.
    :param int q: (optional) Schema for the number of shards in a database. Each
          shard is a partition of the hash value range.
    """

    def __init__(
        self,
        *,
        n: Optional[int] = None,
        partitioned: Optional[bool] = None,
        q: Optional[int] = None,
    ) -> None:
        """
        Initialize a ReplicationCreateTargetParameters object.

        :param int n: (optional) Schema for the number of replicas of a database in
               a cluster. The cluster is using the default value and it cannot be changed
               by the user.
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
        if (n := _dict.get('n')) is not None:
            args['n'] = n
        if (partitioned := _dict.get('partitioned')) is not None:
            args['partitioned'] = partitioned
        if (q := _dict.get('q')) is not None:
            args['q'] = q
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


class ReplicationDatabase:
    """
    Schema for a replication source or target database.

    :param ReplicationDatabaseAuth auth: (optional) Schema for replication source or
          target database authentication.
    :param dict headers_: (optional) Replication request headers.
    :param str url: Replication database URL.
    """

    def __init__(
        self,
        url: str,
        *,
        auth: Optional['ReplicationDatabaseAuth'] = None,
        headers_: Optional[dict] = None,
    ) -> None:
        """
        Initialize a ReplicationDatabase object.

        :param str url: Replication database URL.
        :param ReplicationDatabaseAuth auth: (optional) Schema for replication
               source or target database authentication.
        :param dict headers_: (optional) Replication request headers.
        """
        self.auth = auth
        self.headers_ = headers_
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReplicationDatabase':
        """Initialize a ReplicationDatabase object from a json dictionary."""
        args = {}
        if (auth := _dict.get('auth')) is not None:
            args['auth'] = ReplicationDatabaseAuth.from_dict(auth)
        if (headers_ := _dict.get('headers')) is not None:
            args['headers_'] = headers_
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        else:
            raise ValueError('Required property \'url\' not present in ReplicationDatabase JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReplicationDatabase object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'auth') and self.auth is not None:
            if isinstance(self.auth, dict):
                _dict['auth'] = self.auth
            else:
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


class ReplicationDatabaseAuth:
    """
    Schema for replication source or target database authentication.

    :param ReplicationDatabaseAuthBasic basic: (optional) Schema for basic
          authentication of replication source or target database.
    :param ReplicationDatabaseAuthIam iam: (optional) Schema for an IAM API key for
          replication database authentication.
    """

    def __init__(
        self,
        *,
        basic: Optional['ReplicationDatabaseAuthBasic'] = None,
        iam: Optional['ReplicationDatabaseAuthIam'] = None,
    ) -> None:
        """
        Initialize a ReplicationDatabaseAuth object.

        :param ReplicationDatabaseAuthBasic basic: (optional) Schema for basic
               authentication of replication source or target database.
        :param ReplicationDatabaseAuthIam iam: (optional) Schema for an IAM API key
               for replication database authentication.
        """
        self.basic = basic
        self.iam = iam

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReplicationDatabaseAuth':
        """Initialize a ReplicationDatabaseAuth object from a json dictionary."""
        args = {}
        if (basic := _dict.get('basic')) is not None:
            args['basic'] = ReplicationDatabaseAuthBasic.from_dict(basic)
        if (iam := _dict.get('iam')) is not None:
            args['iam'] = ReplicationDatabaseAuthIam.from_dict(iam)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReplicationDatabaseAuth object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'basic') and self.basic is not None:
            if isinstance(self.basic, dict):
                _dict['basic'] = self.basic
            else:
                _dict['basic'] = self.basic.to_dict()
        if hasattr(self, 'iam') and self.iam is not None:
            if isinstance(self.iam, dict):
                _dict['iam'] = self.iam
            else:
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


class ReplicationDatabaseAuthBasic:
    """
    Schema for basic authentication of replication source or target database.

    :param str password: The password associated with the username.
    :param str username: Schema for a username.
    """

    def __init__(
        self,
        password: str,
        username: str,
    ) -> None:
        """
        Initialize a ReplicationDatabaseAuthBasic object.

        :param str password: The password associated with the username.
        :param str username: Schema for a username.
        """
        self.password = password
        self.username = username

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReplicationDatabaseAuthBasic':
        """Initialize a ReplicationDatabaseAuthBasic object from a json dictionary."""
        args = {}
        if (password := _dict.get('password')) is not None:
            args['password'] = password
        else:
            raise ValueError('Required property \'password\' not present in ReplicationDatabaseAuthBasic JSON')
        if (username := _dict.get('username')) is not None:
            args['username'] = username
        else:
            raise ValueError('Required property \'username\' not present in ReplicationDatabaseAuthBasic JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReplicationDatabaseAuthBasic object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReplicationDatabaseAuthBasic object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReplicationDatabaseAuthBasic') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReplicationDatabaseAuthBasic') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ReplicationDatabaseAuthIam:
    """
    Schema for an IAM API key for replication database authentication.

    :param str api_key: IAM API key.
    """

    def __init__(
        self,
        api_key: str,
    ) -> None:
        """
        Initialize a ReplicationDatabaseAuthIam object.

        :param str api_key: IAM API key.
        """
        self.api_key = api_key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReplicationDatabaseAuthIam':
        """Initialize a ReplicationDatabaseAuthIam object from a json dictionary."""
        args = {}
        if (api_key := _dict.get('api_key')) is not None:
            args['api_key'] = api_key
        else:
            raise ValueError('Required property \'api_key\' not present in ReplicationDatabaseAuthIam JSON')
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


class ReplicationDocument:
    """
    Schema for a replication document. Note that `selector`, `doc_ids`, and `filter` are
    incompatible with each other.

    :param dict _attachments: (optional) Schema for a map of attachment name to
          attachment metadata.
    :param List[str] _conflicts: (optional) Schema for a list of document revision
          identifiers.
    :param bool _deleted: (optional) Deletion flag. Available if document was
          removed.
    :param List[str] _deleted_conflicts: (optional) Schema for a list of document
          revision identifiers.
    :param str _id: (optional) Schema for a document ID.
    :param str _local_seq: (optional) Document's update sequence in current
          database. Available if requested with local_seq=true query parameter.
    :param str _rev: (optional) Schema for a document revision identifier.
    :param Revisions _revisions: (optional) Schema for list of revision information.
    :param List[DocumentRevisionStatus] _revs_info: (optional) Schema for a list of
          objects with information about local revisions and their status.
    :param bool cancel: (optional) Cancels the replication.
    :param int checkpoint_interval: (optional) Defines replication checkpoint
          interval in milliseconds.
    :param int connection_timeout: (optional) HTTP connection timeout per
          replication. Even for very fast/reliable networks it might need to be increased
          if a remote database is too busy.
    :param bool continuous: (optional) Configure the replication to be continuous.
    :param bool create_target: (optional) Creates the target database. Requires
          administrator privileges on target server.
    :param ReplicationCreateTargetParameters create_target_params: (optional)
          Request parameters to use during target database creation.
    :param List[str] doc_ids: (optional) Schema for a list of document IDs.
    :param str filter: (optional) The name of a filter function which is defined in
          a design document in the source database in {ddoc_id}/{filter} format. It
          determines which documents get replicated. Using the selector option provides
          performance benefits when compared with using the filter option. Use the
          selector option when possible.
    :param int http_connections: (optional) Maximum number of HTTP connections per
          replication.
    :param str owner: (optional) The replication document owner. The server sets an
          appropriate value if the field is unset when writing a replication document.
          Only administrators can modify the value to an owner other than themselves.
    :param dict query_params: (optional) Schema for a map of string key value pairs,
          such as query parameters.
    :param int retries_per_request: (optional) Number of times a replication request
          is retried. The requests are retried with a doubling exponential backoff
          starting at 0.25 seconds, with a cap at 5 minutes.
    :param dict selector: (optional) JSON object describing criteria used to select
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
          used to combine selectors. A combination operator takes a single argument. The
          argument is either another selector, or an array of selectors.
          * Condition operators: are specific to a field, and are used to evaluate the
          value stored in that field. For instance, the basic `$eq` operator matches when
          the specified field contains a value that is equal to the supplied argument.
          It is important for query performance to use appropriate selectors:
          * Only equality operators such as `$eq`, `$gt`, `$gte`, `$lt`, and `$lte` (but
          not `$ne`) can be used as the basis of a query. You should include at least one
          of these in a selector.
          * Some operators such as `$not`, `$or`, `$in`, and `$regex` cannot be answered
          from an index. For query selectors use these operators in conjunction with
          equality operators or create and use a partial index to reduce the number of
          documents that will need to be scanned.
          See [the Cloudant
          Docs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-operators)for a list of
          all available combination and conditional operators.
          For further reference see [selector
          syntax](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-selector-syntax).
    :param str since_seq: (optional) Start the replication at a specific sequence
          value.
    :param str socket_options: (optional) Replication socket options.
    :param ReplicationDatabase source: Schema for a replication source or target
          database.
    :param str source_proxy: (optional) Deprecated: This setting is forbidden in IBM
          Cloudant replication documents. This setting may be used with alternative
          replication mediators.
          Address of a (http or socks5 protocol) proxy server through which replication
          with the source database should occur.
    :param ReplicationDatabase target: Schema for a replication source or target
          database.
    :param str target_proxy: (optional) Deprecated: This setting is forbidden in IBM
          Cloudant replication documents. This setting may be used with alternative
          replication mediators.
          Address of a (http or socks5 protocol) proxy server through which replication
          with the target database should occur.
    :param bool use_bulk_get: (optional) Specify whether to use _bulk_get for
          fetching documents from the source. If unset, the server configured default will
          be used.
    :param bool use_checkpoints: (optional) Specify if checkpoints should be saved
          during replication. Using checkpoints means a replication can be efficiently
          resumed.
    :param UserContext user_ctx: (optional) Schema for the user context of a
          session.
    :param bool winning_revs_only: (optional) Replicate only the winning revisions.
          Replication with this mode discards conflicting revisions. Replication IDs and
          checkpoints generated by this mode are different to those generated by default,
          so it is possible to first replicate the winning revisions then later backfill
          remaining revisions with a regular replication job.
    :param int worker_batch_size: (optional) Controls how many documents are
          processed. After each batch a checkpoint is written so this controls how
          frequently checkpointing occurs.
    :param int worker_processes: (optional) Controls how many separate processes
          will read from the changes manager and write to the target. A higher number can
          improve throughput.

    This type supports additional properties of type object.
    """

    # The set of defined properties for the class
    _properties = frozenset(['_attachments', '_conflicts', '_deleted', '_deleted_conflicts', '_id', '_local_seq', '_rev', '_revisions', '_revs_info', 'cancel', 'checkpoint_interval', 'connection_timeout', 'continuous', 'create_target', 'create_target_params', 'doc_ids', 'filter', 'http_connections', 'owner', 'query_params', 'retries_per_request', 'selector', 'since_seq', 'socket_options', 'source', 'source_proxy', 'target', 'target_proxy', 'use_bulk_get', 'use_checkpoints', 'user_ctx', 'winning_revs_only', 'worker_batch_size', 'worker_processes'])

    def __init__(
        self,
        source: 'ReplicationDatabase',
        target: 'ReplicationDatabase',
        *,
        _attachments: Optional[dict] = None,
        _conflicts: Optional[List[str]] = None,
        _deleted: Optional[bool] = None,
        _deleted_conflicts: Optional[List[str]] = None,
        _id: Optional[str] = None,
        _local_seq: Optional[str] = None,
        _rev: Optional[str] = None,
        _revisions: Optional['Revisions'] = None,
        _revs_info: Optional[List['DocumentRevisionStatus']] = None,
        cancel: Optional[bool] = None,
        checkpoint_interval: Optional[int] = None,
        connection_timeout: Optional[int] = None,
        continuous: Optional[bool] = None,
        create_target: Optional[bool] = None,
        create_target_params: Optional['ReplicationCreateTargetParameters'] = None,
        doc_ids: Optional[List[str]] = None,
        filter: Optional[str] = None,
        http_connections: Optional[int] = None,
        owner: Optional[str] = None,
        query_params: Optional[dict] = None,
        retries_per_request: Optional[int] = None,
        selector: Optional[dict] = None,
        since_seq: Optional[str] = None,
        socket_options: Optional[str] = None,
        source_proxy: Optional[str] = None,
        target_proxy: Optional[str] = None,
        use_bulk_get: Optional[bool] = None,
        use_checkpoints: Optional[bool] = None,
        user_ctx: Optional['UserContext'] = None,
        winning_revs_only: Optional[bool] = None,
        worker_batch_size: Optional[int] = None,
        worker_processes: Optional[int] = None,
        **kwargs: Optional[object],
    ) -> None:
        """
        Initialize a ReplicationDocument object.

        :param ReplicationDatabase source: Schema for a replication source or
               target database.
        :param ReplicationDatabase target: Schema for a replication source or
               target database.
        :param dict _attachments: (optional) Schema for a map of attachment name to
               attachment metadata.
        :param List[str] _conflicts: (optional) Schema for a list of document
               revision identifiers.
        :param bool _deleted: (optional) Deletion flag. Available if document was
               removed.
        :param List[str] _deleted_conflicts: (optional) Schema for a list of
               document revision identifiers.
        :param str _id: (optional) Schema for a document ID.
        :param str _local_seq: (optional) Document's update sequence in current
               database. Available if requested with local_seq=true query parameter.
        :param str _rev: (optional) Schema for a document revision identifier.
        :param Revisions _revisions: (optional) Schema for list of revision
               information.
        :param List[DocumentRevisionStatus] _revs_info: (optional) Schema for a
               list of objects with information about local revisions and their status.
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
        :param str owner: (optional) The replication document owner. The server
               sets an appropriate value if the field is unset when writing a replication
               document. Only administrators can modify the value to an owner other than
               themselves.
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
               are used to combine selectors. A combination operator takes a single
               argument. The argument is either another selector, or an array of
               selectors.
               * Condition operators: are specific to a field, and are used to evaluate
               the value stored in that field. For instance, the basic `$eq` operator
               matches when the specified field contains a value that is equal to the
               supplied argument.
               It is important for query performance to use appropriate selectors:
               * Only equality operators such as `$eq`, `$gt`, `$gte`, `$lt`, and `$lte`
               (but not `$ne`) can be used as the basis of a query. You should include at
               least one of these in a selector.
               * Some operators such as `$not`, `$or`, `$in`, and `$regex` cannot be
               answered from an index. For query selectors use these operators in
               conjunction with equality operators or create and use a partial index to
               reduce the number of documents that will need to be scanned.
               See [the Cloudant
               Docs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-operators)for a
               list of all available combination and conditional operators.
               For further reference see [selector
               syntax](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-selector-syntax).
        :param str since_seq: (optional) Start the replication at a specific
               sequence value.
        :param str socket_options: (optional) Replication socket options.
        :param str source_proxy: (optional) Deprecated: This setting is forbidden
               in IBM Cloudant replication documents. This setting may be used with
               alternative replication mediators.
               Address of a (http or socks5 protocol) proxy server through which
               replication with the source database should occur.
        :param str target_proxy: (optional) Deprecated: This setting is forbidden
               in IBM Cloudant replication documents. This setting may be used with
               alternative replication mediators.
               Address of a (http or socks5 protocol) proxy server through which
               replication with the target database should occur.
        :param bool use_bulk_get: (optional) Specify whether to use _bulk_get for
               fetching documents from the source. If unset, the server configured default
               will be used.
        :param bool use_checkpoints: (optional) Specify if checkpoints should be
               saved during replication. Using checkpoints means a replication can be
               efficiently resumed.
        :param UserContext user_ctx: (optional) Schema for the user context of a
               session.
        :param bool winning_revs_only: (optional) Replicate only the winning
               revisions. Replication with this mode discards conflicting revisions.
               Replication IDs and checkpoints generated by this mode are different to
               those generated by default, so it is possible to first replicate the
               winning revisions then later backfill remaining revisions with a regular
               replication job.
        :param int worker_batch_size: (optional) Controls how many documents are
               processed. After each batch a checkpoint is written so this controls how
               frequently checkpointing occurs.
        :param int worker_processes: (optional) Controls how many separate
               processes will read from the changes manager and write to the target. A
               higher number can improve throughput.
        :param object **kwargs: (optional) Additional properties of type object
        """
        self._attachments = _attachments
        self._conflicts = _conflicts
        self._deleted = _deleted
        self._deleted_conflicts = _deleted_conflicts
        self._id = _id
        self._local_seq = _local_seq
        self._rev = _rev
        self._revisions = _revisions
        self._revs_info = _revs_info
        self.cancel = cancel
        self.checkpoint_interval = checkpoint_interval
        self.connection_timeout = connection_timeout
        self.continuous = continuous
        self.create_target = create_target
        self.create_target_params = create_target_params
        self.doc_ids = doc_ids
        self.filter = filter
        self.http_connections = http_connections
        self.owner = owner
        self.query_params = query_params
        self.retries_per_request = retries_per_request
        self.selector = selector
        self.since_seq = since_seq
        self.socket_options = socket_options
        self.source = source
        self.source_proxy = source_proxy
        self.target = target
        self.target_proxy = target_proxy
        self.use_bulk_get = use_bulk_get
        self.use_checkpoints = use_checkpoints
        self.user_ctx = user_ctx
        self.winning_revs_only = winning_revs_only
        self.worker_batch_size = worker_batch_size
        self.worker_processes = worker_processes
        for k, v in kwargs.items():
            if k not in ReplicationDocument._properties:
                if not isinstance(v, object):
                    raise ValueError('Value for additional property {} must be of type object'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(k))

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReplicationDocument':
        """Initialize a ReplicationDocument object from a json dictionary."""
        args = {}
        if (attachments := _dict.get('_attachments')) is not None:
            args['_attachments'] = {k: Attachment.from_dict(v) for k, v in attachments.items()}
        if (conflicts := _dict.get('_conflicts')) is not None:
            args['_conflicts'] = conflicts
        if (deleted := _dict.get('_deleted')) is not None:
            args['_deleted'] = deleted
        if (deleted_conflicts := _dict.get('_deleted_conflicts')) is not None:
            args['_deleted_conflicts'] = deleted_conflicts
        if (id := _dict.get('_id')) is not None:
            args['_id'] = id
        if (local_seq := _dict.get('_local_seq')) is not None:
            args['_local_seq'] = local_seq
        if (rev := _dict.get('_rev')) is not None:
            args['_rev'] = rev
        if (revisions := _dict.get('_revisions')) is not None:
            args['_revisions'] = Revisions.from_dict(revisions)
        if (revs_info := _dict.get('_revs_info')) is not None:
            args['_revs_info'] = [DocumentRevisionStatus.from_dict(v) for v in revs_info]
        if (cancel := _dict.get('cancel')) is not None:
            args['cancel'] = cancel
        if (checkpoint_interval := _dict.get('checkpoint_interval')) is not None:
            args['checkpoint_interval'] = checkpoint_interval
        if (connection_timeout := _dict.get('connection_timeout')) is not None:
            args['connection_timeout'] = connection_timeout
        if (continuous := _dict.get('continuous')) is not None:
            args['continuous'] = continuous
        if (create_target := _dict.get('create_target')) is not None:
            args['create_target'] = create_target
        if (create_target_params := _dict.get('create_target_params')) is not None:
            args['create_target_params'] = ReplicationCreateTargetParameters.from_dict(create_target_params)
        if (doc_ids := _dict.get('doc_ids')) is not None:
            args['doc_ids'] = doc_ids
        if (filter := _dict.get('filter')) is not None:
            args['filter'] = filter
        if (http_connections := _dict.get('http_connections')) is not None:
            args['http_connections'] = http_connections
        if (owner := _dict.get('owner')) is not None:
            args['owner'] = owner
        if (query_params := _dict.get('query_params')) is not None:
            args['query_params'] = query_params
        if (retries_per_request := _dict.get('retries_per_request')) is not None:
            args['retries_per_request'] = retries_per_request
        if (selector := _dict.get('selector')) is not None:
            args['selector'] = selector
        if (since_seq := _dict.get('since_seq')) is not None:
            args['since_seq'] = since_seq
        if (socket_options := _dict.get('socket_options')) is not None:
            args['socket_options'] = socket_options
        if (source := _dict.get('source')) is not None:
            args['source'] = ReplicationDatabase.from_dict(source)
        else:
            raise ValueError('Required property \'source\' not present in ReplicationDocument JSON')
        if (source_proxy := _dict.get('source_proxy')) is not None:
            args['source_proxy'] = source_proxy
        if (target := _dict.get('target')) is not None:
            args['target'] = ReplicationDatabase.from_dict(target)
        else:
            raise ValueError('Required property \'target\' not present in ReplicationDocument JSON')
        if (target_proxy := _dict.get('target_proxy')) is not None:
            args['target_proxy'] = target_proxy
        if (use_bulk_get := _dict.get('use_bulk_get')) is not None:
            args['use_bulk_get'] = use_bulk_get
        if (use_checkpoints := _dict.get('use_checkpoints')) is not None:
            args['use_checkpoints'] = use_checkpoints
        if (user_ctx := _dict.get('user_ctx')) is not None:
            args['user_ctx'] = UserContext.from_dict(user_ctx)
        if (winning_revs_only := _dict.get('winning_revs_only')) is not None:
            args['winning_revs_only'] = winning_revs_only
        if (worker_batch_size := _dict.get('worker_batch_size')) is not None:
            args['worker_batch_size'] = worker_batch_size
        if (worker_processes := _dict.get('worker_processes')) is not None:
            args['worker_processes'] = worker_processes
        for k, v in _dict.items():
            if k not in cls._properties:
                    if not isinstance(v, object):
                        raise ValueError('Value for additional property {} must be of type object'.format(k))
                    args[k] = v
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReplicationDocument object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, '_attachments') and self._attachments is not None:
            _attachments_map = {}
            for k, v in self._attachments.items():
                if isinstance(v, dict):
                    _attachments_map[k] = v
                else:
                    _attachments_map[k] = v.to_dict()
            _dict['_attachments'] = _attachments_map
        if hasattr(self, '_conflicts') and self._conflicts is not None:
            _dict['_conflicts'] = self._conflicts
        if hasattr(self, '_deleted') and self._deleted is not None:
            _dict['_deleted'] = self._deleted
        if hasattr(self, '_deleted_conflicts') and self._deleted_conflicts is not None:
            _dict['_deleted_conflicts'] = self._deleted_conflicts
        if hasattr(self, '_id') and self._id is not None:
            _dict['_id'] = self._id
        if hasattr(self, '_local_seq') and self._local_seq is not None:
            _dict['_local_seq'] = self._local_seq
        if hasattr(self, '_rev') and self._rev is not None:
            _dict['_rev'] = self._rev
        if hasattr(self, '_revisions') and self._revisions is not None:
            if isinstance(self._revisions, dict):
                _dict['_revisions'] = self._revisions
            else:
                _dict['_revisions'] = self._revisions.to_dict()
        if hasattr(self, '_revs_info') and self._revs_info is not None:
            _revs_info_list = []
            for v in self._revs_info:
                if isinstance(v, dict):
                    _revs_info_list.append(v)
                else:
                    _revs_info_list.append(v.to_dict())
            _dict['_revs_info'] = _revs_info_list
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
            if isinstance(self.create_target_params, dict):
                _dict['create_target_params'] = self.create_target_params
            else:
                _dict['create_target_params'] = self.create_target_params.to_dict()
        if hasattr(self, 'doc_ids') and self.doc_ids is not None:
            _dict['doc_ids'] = self.doc_ids
        if hasattr(self, 'filter') and self.filter is not None:
            _dict['filter'] = self.filter
        if hasattr(self, 'http_connections') and self.http_connections is not None:
            _dict['http_connections'] = self.http_connections
        if hasattr(self, 'owner') and self.owner is not None:
            _dict['owner'] = self.owner
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
            if isinstance(self.source, dict):
                _dict['source'] = self.source
            else:
                _dict['source'] = self.source.to_dict()
        if hasattr(self, 'source_proxy') and self.source_proxy is not None:
            _dict['source_proxy'] = self.source_proxy
        if hasattr(self, 'target') and self.target is not None:
            if isinstance(self.target, dict):
                _dict['target'] = self.target
            else:
                _dict['target'] = self.target.to_dict()
        if hasattr(self, 'target_proxy') and self.target_proxy is not None:
            _dict['target_proxy'] = self.target_proxy
        if hasattr(self, 'use_bulk_get') and self.use_bulk_get is not None:
            _dict['use_bulk_get'] = self.use_bulk_get
        if hasattr(self, 'use_checkpoints') and self.use_checkpoints is not None:
            _dict['use_checkpoints'] = self.use_checkpoints
        if hasattr(self, 'user_ctx') and self.user_ctx is not None:
            if isinstance(self.user_ctx, dict):
                _dict['user_ctx'] = self.user_ctx
            else:
                _dict['user_ctx'] = self.user_ctx.to_dict()
        if hasattr(self, 'winning_revs_only') and self.winning_revs_only is not None:
            _dict['winning_revs_only'] = self.winning_revs_only
        if hasattr(self, 'worker_batch_size') and self.worker_batch_size is not None:
            _dict['worker_batch_size'] = self.worker_batch_size
        if hasattr(self, 'worker_processes') and self.worker_processes is not None:
            _dict['worker_processes'] = self.worker_processes
        for k in [_k for _k in vars(self).keys() if _k not in ReplicationDocument._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of ReplicationDocument in the form of a dict."""
        _dict = {}
        for k in [_k for _k in vars(self).keys() if _k not in ReplicationDocument._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of ReplicationDocument"""
        for k in [_k for _k in vars(self).keys() if _k not in ReplicationDocument._properties]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in ReplicationDocument._properties:
                if not isinstance(v, object):
                    raise ValueError('Value for additional property {} must be of type object'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(k))

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


class Revisions:
    """
    Schema for list of revision information.

    :param List[str] ids: Array of valid revision IDs, in reverse order (latest
          first).
    :param int start: Prefix number for the latest revision.
    """

    def __init__(
        self,
        ids: List[str],
        start: int,
    ) -> None:
        """
        Initialize a Revisions object.

        :param List[str] ids: Array of valid revision IDs, in reverse order (latest
               first).
        :param int start: Prefix number for the latest revision.
        """
        self.ids = ids
        self.start = start

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Revisions':
        """Initialize a Revisions object from a json dictionary."""
        args = {}
        if (ids := _dict.get('ids')) is not None:
            args['ids'] = ids
        else:
            raise ValueError('Required property \'ids\' not present in Revisions JSON')
        if (start := _dict.get('start')) is not None:
            args['start'] = start
        else:
            raise ValueError('Required property \'start\' not present in Revisions JSON')
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


class RevsDiff:
    """
    Schema for information about missing revs and possible ancestors.

    :param List[str] missing: (optional) List of missing revisions.
    :param List[str] possible_ancestors: (optional) List of possible ancestor
          revisions.
    """

    def __init__(
        self,
        *,
        missing: Optional[List[str]] = None,
        possible_ancestors: Optional[List[str]] = None,
    ) -> None:
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
        if (missing := _dict.get('missing')) is not None:
            args['missing'] = missing
        if (possible_ancestors := _dict.get('possible_ancestors')) is not None:
            args['possible_ancestors'] = possible_ancestors
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


class SchedulerDocsResult:
    """
    Schema for a listing of replication scheduler documents.

    :param int total_rows: Total number of replication scheduler documents.
    :param List[SchedulerDocument] docs: Array of replication scheduler doc objects.
    """

    def __init__(
        self,
        total_rows: int,
        docs: List['SchedulerDocument'],
    ) -> None:
        """
        Initialize a SchedulerDocsResult object.

        :param int total_rows: Total number of replication scheduler documents.
        :param List[SchedulerDocument] docs: Array of replication scheduler doc
               objects.
        """
        self.total_rows = total_rows
        self.docs = docs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchedulerDocsResult':
        """Initialize a SchedulerDocsResult object from a json dictionary."""
        args = {}
        if (total_rows := _dict.get('total_rows')) is not None:
            args['total_rows'] = total_rows
        else:
            raise ValueError('Required property \'total_rows\' not present in SchedulerDocsResult JSON')
        if (docs := _dict.get('docs')) is not None:
            args['docs'] = [SchedulerDocument.from_dict(v) for v in docs]
        else:
            raise ValueError('Required property \'docs\' not present in SchedulerDocsResult JSON')
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
            docs_list = []
            for v in self.docs:
                if isinstance(v, dict):
                    docs_list.append(v)
                else:
                    docs_list.append(v.to_dict())
            _dict['docs'] = docs_list
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


class SchedulerDocument:
    """
    Schema for a replication scheduler document.

    :param str database: Database where replication document came from.
    :param str doc_id: Replication document ID.
    :param int error_count: Consecutive errors count. Indicates how many times in a
          row this replication has crashed. Replication will be retried with an
          exponential backoff based on this number. As soon as the replication succeeds
          this count is reset to 0. To can be used to get an idea why a particular
          replication is not making progress.
    :param str id: Replication ID, or null if state is completed or failed.
    :param SchedulerInfo info: Schema for scheduler document information. A JSON
          object that may contain additional information about the state. For error states
          this will contain an error field and string value.
    :param datetime last_updated: Timestamp of last state update.
    :param str node: (optional) Cluster node where the job is running.
    :param str source: (optional) Replication source.
    :param str source_proxy: (optional) Deprecated: Forbidden in IBM Cloudant
          mediated replications.
          Address of the (http or socks5 protocol) proxy server through which replication
          with the source database occurs.
    :param datetime start_time: Timestamp of when the replication was started.
    :param str state: Schema for replication state.
    :param str target: (optional) Replication target.
    :param str target_proxy: (optional) Deprecated: Forbidden in IBM Cloudant
          mediated replications.
          Address of the (http or socks5 protocol) proxy server through which replication
          with the target database occurs.
    """

    def __init__(
        self,
        database: str,
        doc_id: str,
        error_count: int,
        id: str,
        info: 'SchedulerInfo',
        last_updated: datetime,
        start_time: datetime,
        state: str,
        *,
        node: Optional[str] = None,
        source: Optional[str] = None,
        source_proxy: Optional[str] = None,
        target: Optional[str] = None,
        target_proxy: Optional[str] = None,
    ) -> None:
        """
        Initialize a SchedulerDocument object.

        :param str database: Database where replication document came from.
        :param str doc_id: Replication document ID.
        :param int error_count: Consecutive errors count. Indicates how many times
               in a row this replication has crashed. Replication will be retried with an
               exponential backoff based on this number. As soon as the replication
               succeeds this count is reset to 0. To can be used to get an idea why a
               particular replication is not making progress.
        :param str id: Replication ID, or null if state is completed or failed.
        :param SchedulerInfo info: Schema for scheduler document information. A
               JSON object that may contain additional information about the state. For
               error states this will contain an error field and string value.
        :param datetime last_updated: Timestamp of last state update.
        :param datetime start_time: Timestamp of when the replication was started.
        :param str state: Schema for replication state.
        :param str node: (optional) Cluster node where the job is running.
        :param str source: (optional) Replication source.
        :param str source_proxy: (optional) Deprecated: Forbidden in IBM Cloudant
               mediated replications.
               Address of the (http or socks5 protocol) proxy server through which
               replication with the source database occurs.
        :param str target: (optional) Replication target.
        :param str target_proxy: (optional) Deprecated: Forbidden in IBM Cloudant
               mediated replications.
               Address of the (http or socks5 protocol) proxy server through which
               replication with the target database occurs.
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
        if (database := _dict.get('database')) is not None:
            args['database'] = database
        else:
            raise ValueError('Required property \'database\' not present in SchedulerDocument JSON')
        if (doc_id := _dict.get('doc_id')) is not None:
            args['doc_id'] = doc_id
        else:
            raise ValueError('Required property \'doc_id\' not present in SchedulerDocument JSON')
        if (error_count := _dict.get('error_count')) is not None:
            args['error_count'] = error_count
        else:
            raise ValueError('Required property \'error_count\' not present in SchedulerDocument JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in SchedulerDocument JSON')
        if (info := _dict.get('info')) is not None:
            args['info'] = SchedulerInfo.from_dict(info)
        else:
            raise ValueError('Required property \'info\' not present in SchedulerDocument JSON')
        if (last_updated := _dict.get('last_updated')) is not None:
            args['last_updated'] = string_to_datetime(last_updated)
        else:
            raise ValueError('Required property \'last_updated\' not present in SchedulerDocument JSON')
        if (node := _dict.get('node')) is not None:
            args['node'] = node
        if (source := _dict.get('source')) is not None:
            args['source'] = source
        if (source_proxy := _dict.get('source_proxy')) is not None:
            args['source_proxy'] = source_proxy
        if (start_time := _dict.get('start_time')) is not None:
            args['start_time'] = string_to_datetime(start_time)
        else:
            raise ValueError('Required property \'start_time\' not present in SchedulerDocument JSON')
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        else:
            raise ValueError('Required property \'state\' not present in SchedulerDocument JSON')
        if (target := _dict.get('target')) is not None:
            args['target'] = target
        if (target_proxy := _dict.get('target_proxy')) is not None:
            args['target_proxy'] = target_proxy
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
            if isinstance(self.info, dict):
                _dict['info'] = self.info
            else:
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



class SchedulerInfo:
    """
    Schema for scheduler document information. A JSON object that may contain additional
    information about the state. For error states this will contain an error field and
    string value.

    :param int changes_pending: (optional) The count of changes not yet replicated.
    :param str checkpointed_source_seq: (optional) The source sequence id which was
          last successfully replicated.
    :param int doc_write_failures: (optional) The count of docs which failed to be
          written to the target.
    :param int docs_read: (optional) The count of docs which have been read from the
          source.
    :param int docs_written: (optional) The count of docs which have been written to
          the target.
    :param str error: (optional) Replication error message.
    :param int missing_revisions_found: (optional) The count of revisions which were
          found on the source, but missing from the target.
    :param int revisions_checked: (optional) The count of revisions which have been
          checked since this replication began.
    :param str source_seq: (optional) The last sequence number obtained from the
          source database changes feed.
    :param str through_seq: (optional) The last sequence number processed by the
          replicator.
    """

    def __init__(
        self,
        *,
        changes_pending: Optional[int] = None,
        checkpointed_source_seq: Optional[str] = None,
        doc_write_failures: Optional[int] = None,
        docs_read: Optional[int] = None,
        docs_written: Optional[int] = None,
        error: Optional[str] = None,
        missing_revisions_found: Optional[int] = None,
        revisions_checked: Optional[int] = None,
        source_seq: Optional[str] = None,
        through_seq: Optional[str] = None,
    ) -> None:
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
        if (changes_pending := _dict.get('changes_pending')) is not None:
            args['changes_pending'] = changes_pending
        if (checkpointed_source_seq := _dict.get('checkpointed_source_seq')) is not None:
            args['checkpointed_source_seq'] = checkpointed_source_seq
        if (doc_write_failures := _dict.get('doc_write_failures')) is not None:
            args['doc_write_failures'] = doc_write_failures
        if (docs_read := _dict.get('docs_read')) is not None:
            args['docs_read'] = docs_read
        if (docs_written := _dict.get('docs_written')) is not None:
            args['docs_written'] = docs_written
        if (error := _dict.get('error')) is not None:
            args['error'] = error
        if (missing_revisions_found := _dict.get('missing_revisions_found')) is not None:
            args['missing_revisions_found'] = missing_revisions_found
        if (revisions_checked := _dict.get('revisions_checked')) is not None:
            args['revisions_checked'] = revisions_checked
        if (source_seq := _dict.get('source_seq')) is not None:
            args['source_seq'] = source_seq
        if (through_seq := _dict.get('through_seq')) is not None:
            args['through_seq'] = through_seq
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


class SchedulerJob:
    """
    Schema for a replication scheduler job.

    :param str database: Replication document database.
    :param str doc_id: Replication document ID.
    :param List[SchedulerJobEvent] history: Timestamped history of events as a list
          of objects.
    :param str id: Schema for a replication job id.
    :param SchedulerInfo info: Schema for scheduler document information. A JSON
          object that may contain additional information about the state. For error states
          this will contain an error field and string value.
    :param str node: Cluster node where the job is running.
    :param str pid: Replication process ID.
    :param str source: Replication source.
    :param datetime start_time: Timestamp of when the replication was started.
    :param str target: Replication target.
    :param str user: Name of user running the process.
    """

    def __init__(
        self,
        database: str,
        doc_id: str,
        history: List['SchedulerJobEvent'],
        id: str,
        info: 'SchedulerInfo',
        node: str,
        pid: str,
        source: str,
        start_time: datetime,
        target: str,
        user: str,
    ) -> None:
        """
        Initialize a SchedulerJob object.

        :param str database: Replication document database.
        :param str doc_id: Replication document ID.
        :param List[SchedulerJobEvent] history: Timestamped history of events as a
               list of objects.
        :param str id: Schema for a replication job id.
        :param SchedulerInfo info: Schema for scheduler document information. A
               JSON object that may contain additional information about the state. For
               error states this will contain an error field and string value.
        :param str node: Cluster node where the job is running.
        :param str pid: Replication process ID.
        :param str source: Replication source.
        :param datetime start_time: Timestamp of when the replication was started.
        :param str target: Replication target.
        :param str user: Name of user running the process.
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
        if (database := _dict.get('database')) is not None:
            args['database'] = database
        else:
            raise ValueError('Required property \'database\' not present in SchedulerJob JSON')
        if (doc_id := _dict.get('doc_id')) is not None:
            args['doc_id'] = doc_id
        else:
            raise ValueError('Required property \'doc_id\' not present in SchedulerJob JSON')
        if (history := _dict.get('history')) is not None:
            args['history'] = [SchedulerJobEvent.from_dict(v) for v in history]
        else:
            raise ValueError('Required property \'history\' not present in SchedulerJob JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in SchedulerJob JSON')
        if (info := _dict.get('info')) is not None:
            args['info'] = SchedulerInfo.from_dict(info)
        else:
            raise ValueError('Required property \'info\' not present in SchedulerJob JSON')
        if (node := _dict.get('node')) is not None:
            args['node'] = node
        else:
            raise ValueError('Required property \'node\' not present in SchedulerJob JSON')
        if (pid := _dict.get('pid')) is not None:
            args['pid'] = pid
        else:
            raise ValueError('Required property \'pid\' not present in SchedulerJob JSON')
        if (source := _dict.get('source')) is not None:
            args['source'] = source
        else:
            raise ValueError('Required property \'source\' not present in SchedulerJob JSON')
        if (start_time := _dict.get('start_time')) is not None:
            args['start_time'] = string_to_datetime(start_time)
        else:
            raise ValueError('Required property \'start_time\' not present in SchedulerJob JSON')
        if (target := _dict.get('target')) is not None:
            args['target'] = target
        else:
            raise ValueError('Required property \'target\' not present in SchedulerJob JSON')
        if (user := _dict.get('user')) is not None:
            args['user'] = user
        else:
            raise ValueError('Required property \'user\' not present in SchedulerJob JSON')
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
            history_list = []
            for v in self.history:
                if isinstance(v, dict):
                    history_list.append(v)
                else:
                    history_list.append(v.to_dict())
            _dict['history'] = history_list
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'info') and self.info is not None:
            if isinstance(self.info, dict):
                _dict['info'] = self.info
            else:
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


class SchedulerJobEvent:
    """
    Schema for a replication scheduler job event.

    :param str reason: (optional) Reason for current state of event.
    :param datetime timestamp: Timestamp of the event.
    :param str type: Type of the event.
    """

    def __init__(
        self,
        timestamp: datetime,
        type: str,
        *,
        reason: Optional[str] = None,
    ) -> None:
        """
        Initialize a SchedulerJobEvent object.

        :param datetime timestamp: Timestamp of the event.
        :param str type: Type of the event.
        :param str reason: (optional) Reason for current state of event.
        """
        self.reason = reason
        self.timestamp = timestamp
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchedulerJobEvent':
        """Initialize a SchedulerJobEvent object from a json dictionary."""
        args = {}
        if (reason := _dict.get('reason')) is not None:
            args['reason'] = reason
        if (timestamp := _dict.get('timestamp')) is not None:
            args['timestamp'] = string_to_datetime(timestamp)
        else:
            raise ValueError('Required property \'timestamp\' not present in SchedulerJobEvent JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in SchedulerJobEvent JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchedulerJobEvent object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'reason') and self.reason is not None:
            _dict['reason'] = self.reason
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


class SchedulerJobsResult:
    """
    Schema for a listing of replication scheduler jobs.

    :param int total_rows: Total number of replication jobs.
    :param List[SchedulerJob] jobs: Array of replication job objects.
    """

    def __init__(
        self,
        total_rows: int,
        jobs: List['SchedulerJob'],
    ) -> None:
        """
        Initialize a SchedulerJobsResult object.

        :param int total_rows: Total number of replication jobs.
        :param List[SchedulerJob] jobs: Array of replication job objects.
        """
        self.total_rows = total_rows
        self.jobs = jobs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchedulerJobsResult':
        """Initialize a SchedulerJobsResult object from a json dictionary."""
        args = {}
        if (total_rows := _dict.get('total_rows')) is not None:
            args['total_rows'] = total_rows
        else:
            raise ValueError('Required property \'total_rows\' not present in SchedulerJobsResult JSON')
        if (jobs := _dict.get('jobs')) is not None:
            args['jobs'] = [SchedulerJob.from_dict(v) for v in jobs]
        else:
            raise ValueError('Required property \'jobs\' not present in SchedulerJobsResult JSON')
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
            jobs_list = []
            for v in self.jobs:
                if isinstance(v, dict):
                    jobs_list.append(v)
                else:
                    jobs_list.append(v.to_dict())
            _dict['jobs'] = jobs_list
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


class SearchAnalyzeResult:
    """
    Schema for the output of testing search analyzer tokenization.

    :param List[str] tokens: tokens.
    """

    def __init__(
        self,
        tokens: List[str],
    ) -> None:
        """
        Initialize a SearchAnalyzeResult object.

        :param List[str] tokens: tokens.
        """
        self.tokens = tokens

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchAnalyzeResult':
        """Initialize a SearchAnalyzeResult object from a json dictionary."""
        args = {}
        if (tokens := _dict.get('tokens')) is not None:
            args['tokens'] = tokens
        else:
            raise ValueError('Required property \'tokens\' not present in SearchAnalyzeResult JSON')
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


class SearchDiskSizeInformation:
    """
    Schema for search index disk size.

    :param str name: The name of the search index prefixed by the design document ID
          where the index is stored.
    :param SearchIndexDiskSize search_index: Schema for search index disk size.
    """

    def __init__(
        self,
        name: str,
        search_index: 'SearchIndexDiskSize',
    ) -> None:
        """
        Initialize a SearchDiskSizeInformation object.

        :param str name: The name of the search index prefixed by the design
               document ID where the index is stored.
        :param SearchIndexDiskSize search_index: Schema for search index disk size.
        """
        self.name = name
        self.search_index = search_index

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchDiskSizeInformation':
        """Initialize a SearchDiskSizeInformation object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in SearchDiskSizeInformation JSON')
        if (search_index := _dict.get('search_index')) is not None:
            args['search_index'] = SearchIndexDiskSize.from_dict(search_index)
        else:
            raise ValueError('Required property \'search_index\' not present in SearchDiskSizeInformation JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchDiskSizeInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'search_index') and self.search_index is not None:
            if isinstance(self.search_index, dict):
                _dict['search_index'] = self.search_index
            else:
                _dict['search_index'] = self.search_index.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchDiskSizeInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchDiskSizeInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchDiskSizeInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SearchIndexDefinition:
    """
    Schema for a search index definition.

    :param AnalyzerConfiguration analyzer: (optional) Schema for a search analyzer
          configuration.
    :param str index: String form of a JavaScript function that is called for each
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

    def __init__(
        self,
        index: str,
        *,
        analyzer: Optional['AnalyzerConfiguration'] = None,
    ) -> None:
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
        if (analyzer := _dict.get('analyzer')) is not None:
            args['analyzer'] = AnalyzerConfiguration.from_dict(analyzer)
        if (index := _dict.get('index')) is not None:
            args['index'] = index
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
            if isinstance(self.analyzer, dict):
                _dict['analyzer'] = self.analyzer
            else:
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


class SearchIndexDiskSize:
    """
    Schema for search index disk size.

    :param int disk_size: (optional) The size of the search index on disk.
    """

    def __init__(
        self,
        *,
        disk_size: Optional[int] = None,
    ) -> None:
        """
        Initialize a SearchIndexDiskSize object.

        :param int disk_size: (optional) The size of the search index on disk.
        """
        self.disk_size = disk_size

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchIndexDiskSize':
        """Initialize a SearchIndexDiskSize object from a json dictionary."""
        args = {}
        if (disk_size := _dict.get('disk_size')) is not None:
            args['disk_size'] = disk_size
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchIndexDiskSize object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'disk_size') and self.disk_size is not None:
            _dict['disk_size'] = self.disk_size
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchIndexDiskSize object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchIndexDiskSize') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchIndexDiskSize') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SearchIndexInfo:
    """
    Schema for metadata information about a search index.

    :param int committed_seq: The committed sequence identifier.
    :param int disk_size: The size of the search index on disk.
    :param int doc_count: The count of the number of indexed documents.
    :param int doc_del_count: The number of deleted documents.
    :param int pending_seq: The pending sequence identifier.
    :param str signature: Unique signature of the search index.
    """

    def __init__(
        self,
        committed_seq: int,
        disk_size: int,
        doc_count: int,
        doc_del_count: int,
        pending_seq: int,
        signature: str,
    ) -> None:
        """
        Initialize a SearchIndexInfo object.

        :param int committed_seq: The committed sequence identifier.
        :param int disk_size: The size of the search index on disk.
        :param int doc_count: The count of the number of indexed documents.
        :param int doc_del_count: The number of deleted documents.
        :param int pending_seq: The pending sequence identifier.
        :param str signature: Unique signature of the search index.
        """
        self.committed_seq = committed_seq
        self.disk_size = disk_size
        self.doc_count = doc_count
        self.doc_del_count = doc_del_count
        self.pending_seq = pending_seq
        self.signature = signature

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchIndexInfo':
        """Initialize a SearchIndexInfo object from a json dictionary."""
        args = {}
        if (committed_seq := _dict.get('committed_seq')) is not None:
            args['committed_seq'] = committed_seq
        else:
            raise ValueError('Required property \'committed_seq\' not present in SearchIndexInfo JSON')
        if (disk_size := _dict.get('disk_size')) is not None:
            args['disk_size'] = disk_size
        else:
            raise ValueError('Required property \'disk_size\' not present in SearchIndexInfo JSON')
        if (doc_count := _dict.get('doc_count')) is not None:
            args['doc_count'] = doc_count
        else:
            raise ValueError('Required property \'doc_count\' not present in SearchIndexInfo JSON')
        if (doc_del_count := _dict.get('doc_del_count')) is not None:
            args['doc_del_count'] = doc_del_count
        else:
            raise ValueError('Required property \'doc_del_count\' not present in SearchIndexInfo JSON')
        if (pending_seq := _dict.get('pending_seq')) is not None:
            args['pending_seq'] = pending_seq
        else:
            raise ValueError('Required property \'pending_seq\' not present in SearchIndexInfo JSON')
        if (signature := _dict.get('signature')) is not None:
            args['signature'] = signature
        else:
            raise ValueError('Required property \'signature\' not present in SearchIndexInfo JSON')
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
        if hasattr(self, 'signature') and self.signature is not None:
            _dict['signature'] = self.signature
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


class SearchInfoResult:
    """
    Schema for search index information.

    :param str name: The name of the search index prefixed by the design document ID
          where the index is stored.
    :param SearchIndexInfo search_index: Schema for metadata information about a
          search index.
    """

    def __init__(
        self,
        name: str,
        search_index: 'SearchIndexInfo',
    ) -> None:
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
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in SearchInfoResult JSON')
        if (search_index := _dict.get('search_index')) is not None:
            args['search_index'] = SearchIndexInfo.from_dict(search_index)
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
            if isinstance(self.search_index, dict):
                _dict['search_index'] = self.search_index
            else:
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


class SearchResult:
    """
    Schema for the result of a query search operation.

    :param int total_rows: Total number of rows in the index matching the search
          query. The limit may truncate the number of matches returned.
    :param str bookmark: (optional) Opaque bookmark token used when paginating
          results.
    :param str by: (optional) Grouped search matches.
    :param dict counts: (optional) The counts facet syntax returns the number of
          query results for each unique value of each named field.
    :param dict ranges: (optional) The range facet syntax reuses the standard Lucene
          syntax for ranges to return counts of results that fit into each specified
          category.
    :param List[SearchResultRow] rows: Array of row objects.
    :param List[SearchResultProperties] groups: (optional) Array of grouped search
          matches.
    """

    def __init__(
        self,
        total_rows: int,
        rows: List['SearchResultRow'],
        *,
        bookmark: Optional[str] = None,
        by: Optional[str] = None,
        counts: Optional[dict] = None,
        ranges: Optional[dict] = None,
        groups: Optional[List['SearchResultProperties']] = None,
    ) -> None:
        """
        Initialize a SearchResult object.

        :param int total_rows: Total number of rows in the index matching the
               search query. The limit may truncate the number of matches returned.
        :param List[SearchResultRow] rows: Array of row objects.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param str by: (optional) Grouped search matches.
        :param dict counts: (optional) The counts facet syntax returns the number
               of query results for each unique value of each named field.
        :param dict ranges: (optional) The range facet syntax reuses the standard
               Lucene syntax for ranges to return counts of results that fit into each
               specified category.
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
        if (total_rows := _dict.get('total_rows')) is not None:
            args['total_rows'] = total_rows
        else:
            raise ValueError('Required property \'total_rows\' not present in SearchResult JSON')
        if (bookmark := _dict.get('bookmark')) is not None:
            args['bookmark'] = bookmark
        if (by := _dict.get('by')) is not None:
            args['by'] = by
        if (counts := _dict.get('counts')) is not None:
            args['counts'] = counts
        if (ranges := _dict.get('ranges')) is not None:
            args['ranges'] = ranges
        if (rows := _dict.get('rows')) is not None:
            args['rows'] = [SearchResultRow.from_dict(v) for v in rows]
        else:
            raise ValueError('Required property \'rows\' not present in SearchResult JSON')
        if (groups := _dict.get('groups')) is not None:
            args['groups'] = [SearchResultProperties.from_dict(v) for v in groups]
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
            rows_list = []
            for v in self.rows:
                if isinstance(v, dict):
                    rows_list.append(v)
                else:
                    rows_list.append(v.to_dict())
            _dict['rows'] = rows_list
        if hasattr(self, 'groups') and self.groups is not None:
            groups_list = []
            for v in self.groups:
                if isinstance(v, dict):
                    groups_list.append(v)
                else:
                    groups_list.append(v.to_dict())
            _dict['groups'] = groups_list
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


class SearchResultProperties:
    """
    Schema for the result of a query search operation.

    :param int total_rows: Total number of rows in the index matching the search
          query. The limit may truncate the number of matches returned.
    :param str bookmark: (optional) Opaque bookmark token used when paginating
          results.
    :param str by: (optional) Grouped search matches.
    :param dict counts: (optional) The counts facet syntax returns the number of
          query results for each unique value of each named field.
    :param dict ranges: (optional) The range facet syntax reuses the standard Lucene
          syntax for ranges to return counts of results that fit into each specified
          category.
    :param List[SearchResultRow] rows: Array of row objects.
    """

    def __init__(
        self,
        total_rows: int,
        rows: List['SearchResultRow'],
        *,
        bookmark: Optional[str] = None,
        by: Optional[str] = None,
        counts: Optional[dict] = None,
        ranges: Optional[dict] = None,
    ) -> None:
        """
        Initialize a SearchResultProperties object.

        :param int total_rows: Total number of rows in the index matching the
               search query. The limit may truncate the number of matches returned.
        :param List[SearchResultRow] rows: Array of row objects.
        :param str bookmark: (optional) Opaque bookmark token used when paginating
               results.
        :param str by: (optional) Grouped search matches.
        :param dict counts: (optional) The counts facet syntax returns the number
               of query results for each unique value of each named field.
        :param dict ranges: (optional) The range facet syntax reuses the standard
               Lucene syntax for ranges to return counts of results that fit into each
               specified category.
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
        if (total_rows := _dict.get('total_rows')) is not None:
            args['total_rows'] = total_rows
        else:
            raise ValueError('Required property \'total_rows\' not present in SearchResultProperties JSON')
        if (bookmark := _dict.get('bookmark')) is not None:
            args['bookmark'] = bookmark
        if (by := _dict.get('by')) is not None:
            args['by'] = by
        if (counts := _dict.get('counts')) is not None:
            args['counts'] = counts
        if (ranges := _dict.get('ranges')) is not None:
            args['ranges'] = ranges
        if (rows := _dict.get('rows')) is not None:
            args['rows'] = [SearchResultRow.from_dict(v) for v in rows]
        else:
            raise ValueError('Required property \'rows\' not present in SearchResultProperties JSON')
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
            rows_list = []
            for v in self.rows:
                if isinstance(v, dict):
                    rows_list.append(v)
                else:
                    rows_list.append(v.to_dict())
            _dict['rows'] = rows_list
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


class SearchResultRow:
    """
    Schema for a row of the result of a query search operation.

    :param Document doc: (optional) Schema for a document.
    :param dict fields: Schema for the fields returned by a query search operation,
          a map of field name to value.
    :param dict highlights: (optional) Returns the context in which a search term
          was mentioned so that you can display more emphasized results to a user.
    :param str id: Schema for a document ID.
    """

    def __init__(
        self,
        fields: dict,
        id: str,
        *,
        doc: Optional['Document'] = None,
        highlights: Optional[dict] = None,
    ) -> None:
        """
        Initialize a SearchResultRow object.

        :param dict fields: Schema for the fields returned by a query search
               operation, a map of field name to value.
        :param str id: Schema for a document ID.
        :param Document doc: (optional) Schema for a document.
        :param dict highlights: (optional) Returns the context in which a search
               term was mentioned so that you can display more emphasized results to a
               user.
        """
        self.doc = doc
        self.fields = fields
        self.highlights = highlights
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchResultRow':
        """Initialize a SearchResultRow object from a json dictionary."""
        args = {}
        if (doc := _dict.get('doc')) is not None:
            args['doc'] = Document.from_dict(doc)
        if (fields := _dict.get('fields')) is not None:
            args['fields'] = fields
        else:
            raise ValueError('Required property \'fields\' not present in SearchResultRow JSON')
        if (highlights := _dict.get('highlights')) is not None:
            args['highlights'] = highlights
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in SearchResultRow JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchResultRow object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'doc') and self.doc is not None:
            if isinstance(self.doc, dict):
                _dict['doc'] = self.doc
            else:
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


class Security:
    """
    Schema for a security document.

    :param SecurityObject admins: (optional) Schema for names and roles to map to a
          database permission.
    :param dict cloudant: (optional) Database permissions for Cloudant users and/or
          API keys.
    :param bool couchdb_auth_only: (optional) Manage permissions using the `_users`
          database only.
    :param SecurityObject members: (optional) Schema for names and roles to map to a
          database permission.
    """

    def __init__(
        self,
        *,
        admins: Optional['SecurityObject'] = None,
        cloudant: Optional[dict] = None,
        couchdb_auth_only: Optional[bool] = None,
        members: Optional['SecurityObject'] = None,
    ) -> None:
        """
        Initialize a Security object.

        :param SecurityObject admins: (optional) Schema for names and roles to map
               to a database permission.
        :param dict cloudant: (optional) Database permissions for Cloudant users
               and/or API keys.
        :param bool couchdb_auth_only: (optional) Manage permissions using the
               `_users` database only.
        :param SecurityObject members: (optional) Schema for names and roles to map
               to a database permission.
        """
        self.admins = admins
        self.cloudant = cloudant
        self.couchdb_auth_only = couchdb_auth_only
        self.members = members

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Security':
        """Initialize a Security object from a json dictionary."""
        args = {}
        if (admins := _dict.get('admins')) is not None:
            args['admins'] = SecurityObject.from_dict(admins)
        if (cloudant := _dict.get('cloudant')) is not None:
            args['cloudant'] = cloudant
        if (couchdb_auth_only := _dict.get('couchdb_auth_only')) is not None:
            args['couchdb_auth_only'] = couchdb_auth_only
        if (members := _dict.get('members')) is not None:
            args['members'] = SecurityObject.from_dict(members)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Security object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'admins') and self.admins is not None:
            if isinstance(self.admins, dict):
                _dict['admins'] = self.admins
            else:
                _dict['admins'] = self.admins.to_dict()
        if hasattr(self, 'cloudant') and self.cloudant is not None:
            _dict['cloudant'] = self.cloudant
        if hasattr(self, 'couchdb_auth_only') and self.couchdb_auth_only is not None:
            _dict['couchdb_auth_only'] = self.couchdb_auth_only
        if hasattr(self, 'members') and self.members is not None:
            if isinstance(self.members, dict):
                _dict['members'] = self.members
            else:
                _dict['members'] = self.members.to_dict()
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



class SecurityObject:
    """
    Schema for names and roles to map to a database permission.

    :param List[str] names: (optional) List of usernames.
    :param List[str] roles: (optional) List of roles.
    """

    def __init__(
        self,
        *,
        names: Optional[List[str]] = None,
        roles: Optional[List[str]] = None,
    ) -> None:
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
        if (names := _dict.get('names')) is not None:
            args['names'] = names
        if (roles := _dict.get('roles')) is not None:
            args['roles'] = roles
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


class SelectorHint:
    """
    Schema for extra information on the selector.

    :param List[str] indexable_fields: A list of fields in the given selector that
          can be used to restrict the query.
    :param str type: A type of the index.
    :param List[str] unindexable_fields: A list of fields in the given selector that
          can't be used to restrict the query.
    """

    def __init__(
        self,
        indexable_fields: List[str],
        type: str,
        unindexable_fields: List[str],
    ) -> None:
        """
        Initialize a SelectorHint object.

        :param List[str] indexable_fields: A list of fields in the given selector
               that can be used to restrict the query.
        :param str type: A type of the index.
        :param List[str] unindexable_fields: A list of fields in the given selector
               that can't be used to restrict the query.
        """
        self.indexable_fields = indexable_fields
        self.type = type
        self.unindexable_fields = unindexable_fields

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SelectorHint':
        """Initialize a SelectorHint object from a json dictionary."""
        args = {}
        if (indexable_fields := _dict.get('indexable_fields')) is not None:
            args['indexable_fields'] = indexable_fields
        else:
            raise ValueError('Required property \'indexable_fields\' not present in SelectorHint JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in SelectorHint JSON')
        if (unindexable_fields := _dict.get('unindexable_fields')) is not None:
            args['unindexable_fields'] = unindexable_fields
        else:
            raise ValueError('Required property \'unindexable_fields\' not present in SelectorHint JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SelectorHint object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'indexable_fields') and self.indexable_fields is not None:
            _dict['indexable_fields'] = self.indexable_fields
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'unindexable_fields') and self.unindexable_fields is not None:
            _dict['unindexable_fields'] = self.unindexable_fields
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SelectorHint object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SelectorHint') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SelectorHint') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        A type of the index.
        """

        JSON = 'json'
        TEXT = 'text'



class ServerInformation:
    """
    Schema for information about the server instance.

    :param str couchdb: Welcome message.
    :param List[str] features: List of enabled optional features.
    :param List[str] features_flags: List of feature flags.
    :param ServerVendor vendor: Schema for server vendor information.
    :param str version: Apache CouchDB version.
    """

    def __init__(
        self,
        couchdb: str,
        features: List[str],
        features_flags: List[str],
        vendor: 'ServerVendor',
        version: str,
    ) -> None:
        """
        Initialize a ServerInformation object.

        :param str couchdb: Welcome message.
        :param List[str] features: List of enabled optional features.
        :param List[str] features_flags: List of feature flags.
        :param ServerVendor vendor: Schema for server vendor information.
        :param str version: Apache CouchDB version.
        """
        self.couchdb = couchdb
        self.features = features
        self.features_flags = features_flags
        self.vendor = vendor
        self.version = version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServerInformation':
        """Initialize a ServerInformation object from a json dictionary."""
        args = {}
        if (couchdb := _dict.get('couchdb')) is not None:
            args['couchdb'] = couchdb
        else:
            raise ValueError('Required property \'couchdb\' not present in ServerInformation JSON')
        if (features := _dict.get('features')) is not None:
            args['features'] = features
        else:
            raise ValueError('Required property \'features\' not present in ServerInformation JSON')
        if (features_flags := _dict.get('features_flags')) is not None:
            args['features_flags'] = features_flags
        else:
            raise ValueError('Required property \'features_flags\' not present in ServerInformation JSON')
        if (vendor := _dict.get('vendor')) is not None:
            args['vendor'] = ServerVendor.from_dict(vendor)
        else:
            raise ValueError('Required property \'vendor\' not present in ServerInformation JSON')
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        else:
            raise ValueError('Required property \'version\' not present in ServerInformation JSON')
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
        if hasattr(self, 'features_flags') and self.features_flags is not None:
            _dict['features_flags'] = self.features_flags
        if hasattr(self, 'vendor') and self.vendor is not None:
            if isinstance(self.vendor, dict):
                _dict['vendor'] = self.vendor
            else:
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


class ServerVendor:
    """
    Schema for server vendor information.

    :param str name: Vendor name.
    :param str variant: Vendor variant.
    :param str version: Vendor version.

    This type supports additional properties of type str.
    """

    # The set of defined properties for the class
    _properties = frozenset(['name', 'variant', 'version'])

    def __init__(
        self,
        name: str,
        variant: str,
        version: str,
        **kwargs: Optional[str],
    ) -> None:
        """
        Initialize a ServerVendor object.

        :param str name: Vendor name.
        :param str variant: Vendor variant.
        :param str version: Vendor version.
        :param str **kwargs: (optional) Additional properties of type str
        """
        self.name = name
        self.variant = variant
        self.version = version
        for k, v in kwargs.items():
            if k not in ServerVendor._properties:
                if not isinstance(v, str):
                    raise ValueError('Value for additional property {} must be of type str'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(k))

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServerVendor':
        """Initialize a ServerVendor object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ServerVendor JSON')
        if (variant := _dict.get('variant')) is not None:
            args['variant'] = variant
        else:
            raise ValueError('Required property \'variant\' not present in ServerVendor JSON')
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        else:
            raise ValueError('Required property \'version\' not present in ServerVendor JSON')
        for k, v in _dict.items():
            if k not in cls._properties:
                    if not isinstance(v, str):
                        raise ValueError('Value for additional property {} must be of type str'.format(k))
                    args[k] = v
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
        for k in [_k for _k in vars(self).keys() if _k not in ServerVendor._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of ServerVendor in the form of a dict."""
        _dict = {}
        for k in [_k for _k in vars(self).keys() if _k not in ServerVendor._properties]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of ServerVendor"""
        for k in [_k for _k in vars(self).keys() if _k not in ServerVendor._properties]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in ServerVendor._properties:
                if not isinstance(v, str):
                    raise ValueError('Value for additional property {} must be of type str'.format(k))
                setattr(self, k, v)
            else:
                raise ValueError('Property {} cannot be specified as an additional property'.format(k))

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

    class VariantEnum(str, Enum):
        """
        Vendor variant.
        """

        PAAS = 'paas'



class SessionAuthentication:
    """
    Schema for session authentication information.

    :param str authenticated: (optional) authenticated.
    :param str authentication_db: (optional) authentication_db.
    :param List[str] authentication_handlers: authentication_handlers.
    """

    def __init__(
        self,
        authentication_handlers: List[str],
        *,
        authenticated: Optional[str] = None,
        authentication_db: Optional[str] = None,
    ) -> None:
        """
        Initialize a SessionAuthentication object.

        :param List[str] authentication_handlers: authentication_handlers.
        :param str authenticated: (optional) authenticated.
        :param str authentication_db: (optional) authentication_db.
        """
        self.authenticated = authenticated
        self.authentication_db = authentication_db
        self.authentication_handlers = authentication_handlers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SessionAuthentication':
        """Initialize a SessionAuthentication object from a json dictionary."""
        args = {}
        if (authenticated := _dict.get('authenticated')) is not None:
            args['authenticated'] = authenticated
        if (authentication_db := _dict.get('authentication_db')) is not None:
            args['authentication_db'] = authentication_db
        if (authentication_handlers := _dict.get('authentication_handlers')) is not None:
            args['authentication_handlers'] = authentication_handlers
        else:
            raise ValueError('Required property \'authentication_handlers\' not present in SessionAuthentication JSON')
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


class SessionInformation:
    """
    Schema for information about a session.

    :param bool ok: ok.
    :param SessionAuthentication info: Schema for session authentication
          information.
    :param UserContext user_ctx: Schema for the user context of a session.
    """

    def __init__(
        self,
        ok: bool,
        info: 'SessionAuthentication',
        user_ctx: 'UserContext',
    ) -> None:
        """
        Initialize a SessionInformation object.

        :param bool ok: ok.
        :param SessionAuthentication info: Schema for session authentication
               information.
        :param UserContext user_ctx: Schema for the user context of a session.
        """
        self.ok = ok
        self.info = info
        self.user_ctx = user_ctx

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SessionInformation':
        """Initialize a SessionInformation object from a json dictionary."""
        args = {}
        if (ok := _dict.get('ok')) is not None:
            args['ok'] = ok
        else:
            raise ValueError('Required property \'ok\' not present in SessionInformation JSON')
        if (info := _dict.get('info')) is not None:
            args['info'] = SessionAuthentication.from_dict(info)
        else:
            raise ValueError('Required property \'info\' not present in SessionInformation JSON')
        if (user_ctx := _dict.get('userCtx')) is not None:
            args['user_ctx'] = UserContext.from_dict(user_ctx)
        else:
            raise ValueError('Required property \'userCtx\' not present in SessionInformation JSON')
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
            if isinstance(self.info, dict):
                _dict['info'] = self.info
            else:
                _dict['info'] = self.info.to_dict()
        if hasattr(self, 'user_ctx') and self.user_ctx is not None:
            if isinstance(self.user_ctx, dict):
                _dict['userCtx'] = self.user_ctx
            else:
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


class ShardsInformation:
    """
    Schema for a shards object that maps the hash value range for each shard to the array
    of nodes that contain a copy of that shard.

    :param dict shards: Mapping of shard hash value range to a list of nodes.
    """

    def __init__(
        self,
        shards: dict,
    ) -> None:
        """
        Initialize a ShardsInformation object.

        :param dict shards: Mapping of shard hash value range to a list of nodes.
        """
        self.shards = shards

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ShardsInformation':
        """Initialize a ShardsInformation object from a json dictionary."""
        args = {}
        if (shards := _dict.get('shards')) is not None:
            args['shards'] = shards
        else:
            raise ValueError('Required property \'shards\' not present in ShardsInformation JSON')
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


class ThroughputInformation:
    """
    Schema for detailed information about throughput capacity with breakdown by specific
    throughput requests classes.

    :param int blocks: (optional) A number of blocks of throughput units. A block
          consists of 100 reads/sec, 50 writes/sec, and 5 global queries/sec of
          provisioned throughput capacity. Not available for some plans.
    :param int query: Provisioned global queries capacity in operations per second.
    :param int read: Provisioned reads capacity in operations per second.
    :param int write: Provisioned writes capacity in operations per second.
    """

    def __init__(
        self,
        query: int,
        read: int,
        write: int,
        *,
        blocks: Optional[int] = None,
    ) -> None:
        """
        Initialize a ThroughputInformation object.

        :param int query: Provisioned global queries capacity in operations per
               second.
        :param int read: Provisioned reads capacity in operations per second.
        :param int write: Provisioned writes capacity in operations per second.
        :param int blocks: (optional) A number of blocks of throughput units. A
               block consists of 100 reads/sec, 50 writes/sec, and 5 global queries/sec of
               provisioned throughput capacity. Not available for some plans.
        """
        self.blocks = blocks
        self.query = query
        self.read = read
        self.write = write

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ThroughputInformation':
        """Initialize a ThroughputInformation object from a json dictionary."""
        args = {}
        if (blocks := _dict.get('blocks')) is not None:
            args['blocks'] = blocks
        if (query := _dict.get('query')) is not None:
            args['query'] = query
        else:
            raise ValueError('Required property \'query\' not present in ThroughputInformation JSON')
        if (read := _dict.get('read')) is not None:
            args['read'] = read
        else:
            raise ValueError('Required property \'read\' not present in ThroughputInformation JSON')
        if (write := _dict.get('write')) is not None:
            args['write'] = write
        else:
            raise ValueError('Required property \'write\' not present in ThroughputInformation JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ThroughputInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'blocks') and self.blocks is not None:
            _dict['blocks'] = self.blocks
        if hasattr(self, 'query') and self.query is not None:
            _dict['query'] = self.query
        if hasattr(self, 'read') and self.read is not None:
            _dict['read'] = self.read
        if hasattr(self, 'write') and self.write is not None:
            _dict['write'] = self.write
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ThroughputInformation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ThroughputInformation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ThroughputInformation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UpInformation:
    """
    Schema for information about the up state of the server.

    :param dict seeds: (optional) seeds.
    :param str status: status.
    """

    def __init__(
        self,
        status: str,
        *,
        seeds: Optional[dict] = None,
    ) -> None:
        """
        Initialize a UpInformation object.

        :param str status: status.
        :param dict seeds: (optional) seeds.
        """
        self.seeds = seeds
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpInformation':
        """Initialize a UpInformation object from a json dictionary."""
        args = {}
        if (seeds := _dict.get('seeds')) is not None:
            args['seeds'] = seeds
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in UpInformation JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpInformation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'seeds') and self.seeds is not None:
            _dict['seeds'] = self.seeds
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



class UpdatesPending:
    """
    Schema for an ability to tell if view is up-to-date without querying it.

    :param int minimum: Sum of shard copies with the least amount of work to do.
    :param int preferred: Sum of unique shards. This value is zero when at least one
          copy of every shard range is up-to-date and the view is able to answer a query
          without index building delays.
    :param int total: Sum of all shard copies.
    """

    def __init__(
        self,
        minimum: int,
        preferred: int,
        total: int,
    ) -> None:
        """
        Initialize a UpdatesPending object.

        :param int minimum: Sum of shard copies with the least amount of work to
               do.
        :param int preferred: Sum of unique shards. This value is zero when at
               least one copy of every shard range is up-to-date and the view is able to
               answer a query without index building delays.
        :param int total: Sum of all shard copies.
        """
        self.minimum = minimum
        self.preferred = preferred
        self.total = total

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpdatesPending':
        """Initialize a UpdatesPending object from a json dictionary."""
        args = {}
        if (minimum := _dict.get('minimum')) is not None:
            args['minimum'] = minimum
        else:
            raise ValueError('Required property \'minimum\' not present in UpdatesPending JSON')
        if (preferred := _dict.get('preferred')) is not None:
            args['preferred'] = preferred
        else:
            raise ValueError('Required property \'preferred\' not present in UpdatesPending JSON')
        if (total := _dict.get('total')) is not None:
            args['total'] = total
        else:
            raise ValueError('Required property \'total\' not present in UpdatesPending JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdatesPending object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'minimum') and self.minimum is not None:
            _dict['minimum'] = self.minimum
        if hasattr(self, 'preferred') and self.preferred is not None:
            _dict['preferred'] = self.preferred
        if hasattr(self, 'total') and self.total is not None:
            _dict['total'] = self.total
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UpdatesPending object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UpdatesPending') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpdatesPending') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UserContext:
    """
    Schema for the user context of a session.

    :param str db: (optional) Database name in the context of the provided
          operation.
    :param str name: Name of user running the process.
    :param List[str] roles: List of user roles.
    """

    def __init__(
        self,
        name: str,
        roles: List[str],
        *,
        db: Optional[str] = None,
    ) -> None:
        """
        Initialize a UserContext object.

        :param str name: Name of user running the process.
        :param List[str] roles: List of user roles.
        :param str db: (optional) Database name in the context of the provided
               operation.
        """
        self.db = db
        self.name = name
        self.roles = roles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UserContext':
        """Initialize a UserContext object from a json dictionary."""
        args = {}
        if (db := _dict.get('db')) is not None:
            args['db'] = db
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in UserContext JSON')
        if (roles := _dict.get('roles')) is not None:
            args['roles'] = roles
        else:
            raise ValueError('Required property \'roles\' not present in UserContext JSON')
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



class UuidsResult:
    """
    Schema for a set of uuids generated by the server.

    :param List[str] uuids: uuids.
    """

    def __init__(
        self,
        uuids: List[str],
    ) -> None:
        """
        Initialize a UuidsResult object.

        :param List[str] uuids: uuids.
        """
        self.uuids = uuids

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UuidsResult':
        """Initialize a UuidsResult object from a json dictionary."""
        args = {}
        if (uuids := _dict.get('uuids')) is not None:
            args['uuids'] = uuids
        else:
            raise ValueError('Required property \'uuids\' not present in UuidsResult JSON')
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


class ViewQueriesResult:
    """
    Schema for the results of a queries view operation.

    :param List[ViewResult] results: An array of result objects - one for each
          query. Each result object contains the same fields as the response to a regular
          view request.
    """

    def __init__(
        self,
        results: List['ViewResult'],
    ) -> None:
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
        if (results := _dict.get('results')) is not None:
            args['results'] = [ViewResult.from_dict(v) for v in results]
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
            results_list = []
            for v in self.results:
                if isinstance(v, dict):
                    results_list.append(v)
                else:
                    results_list.append(v.to_dict())
            _dict['results'] = results_list
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


class ViewQuery:
    """
    Schema for a query view operation.

    :param bool att_encoding_info: (optional) Parameter to specify whether to
          include the encoding information in attachment stubs if the particular
          attachment is compressed.
    :param bool attachments: (optional) Parameter to specify whether to include
          attachments bodies in a response.
    :param bool conflicts: (optional) Parameter to specify whether to include a list
          of conflicted revisions in each returned document. Active only when
          `include_docs` is `true`.
    :param bool descending: (optional) Parameter to specify whether to return the
          documents in descending by key order.
    :param bool include_docs: (optional) Parameter to specify whether to include the
          full content of the documents in the response.
    :param bool inclusive_end: (optional) Parameter to specify whether the specified
          end key should be included in the result.
    :param int limit: (optional) Parameter to specify the number of returned
          documents to limit the result to.
    :param int skip: (optional) Parameter to specify the number of records before
          starting to return the results.
    :param bool update_seq: (optional) Parameter to specify whether to include in
          the response an update_seq value indicating the sequence id of the database the
          view reflects.
    :param object end_key: (optional) Schema for any JSON type.
    :param str end_key_doc_id: (optional) Schema for a document ID.
    :param bool group: (optional) Parameter to specify whether to group reduced
          results by key. Valid only if a reduce function defined in the view. If the view
          emits key in JSON array format, then it is possible to reduce groups further
          based on the number of array elements with the `group_level` parameter.
    :param int group_level: (optional) Parameter to specify a group level to be
          used. Only applicable if the view uses keys that are JSON arrays. Implies group
          is `true`. Group level groups the reduced results by the specified number of
          array elements. If unset, results are grouped by the entire array key, returning
          a reduced value for each complete key.
    :param object key: (optional) Schema for any JSON type.
    :param List[object] keys: (optional) Parameter to specify returning only
          documents that match any of the specified keys. A JSON array of keys that match
          the key type emitted by the view function.
    :param bool reduce: (optional) Parameter to specify whether to use the reduce
          function in a map-reduce view. Default is true when a reduce function is
          defined.
          A default `reduce` view type can be disabled to behave like a `map` by setting
          `reduce=false` explicitly.
          Be aware that `include_docs=true` can only be used with `map` views.
    :param bool stable: (optional) Query parameter to specify whether use the same
          replica of  the index on each request. The default value `false` contacts all
          replicas and returns the result from the first, fastest, responder. Setting it
          to `true` when used in conjunction with `update=false`  may improve consistency
          at the expense of increased latency and decreased throughput if the selected
          replica is not the fastest of the available  replicas.
          **Note:** In general setting `true` is discouraged and is strictly not
          recommended when using `update=true`.
    :param object start_key: (optional) Schema for any JSON type.
    :param str start_key_doc_id: (optional) Schema for a document ID.
    :param str update: (optional) Parameter to specify whether or not the view in
          question should be updated prior to responding to the user.
          * `true` - Return results after the view is updated.
          * `false` - Return results without updating the view.
          * `lazy` - Return the view results without waiting for an update, but update
          them immediately after the request.
    """

    def __init__(
        self,
        *,
        att_encoding_info: Optional[bool] = None,
        attachments: Optional[bool] = None,
        conflicts: Optional[bool] = None,
        descending: Optional[bool] = None,
        include_docs: Optional[bool] = None,
        inclusive_end: Optional[bool] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        update_seq: Optional[bool] = None,
        end_key: Optional[object] = None,
        end_key_doc_id: Optional[str] = None,
        group: Optional[bool] = None,
        group_level: Optional[int] = None,
        key: Optional[object] = None,
        keys: Optional[List[object]] = None,
        reduce: Optional[bool] = None,
        stable: Optional[bool] = None,
        start_key: Optional[object] = None,
        start_key_doc_id: Optional[str] = None,
        update: Optional[str] = None,
    ) -> None:
        """
        Initialize a ViewQuery object.

        :param bool att_encoding_info: (optional) Parameter to specify whether to
               include the encoding information in attachment stubs if the particular
               attachment is compressed.
        :param bool attachments: (optional) Parameter to specify whether to include
               attachments bodies in a response.
        :param bool conflicts: (optional) Parameter to specify whether to include a
               list of conflicted revisions in each returned document. Active only when
               `include_docs` is `true`.
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
        :param object end_key: (optional) Schema for any JSON type.
        :param str end_key_doc_id: (optional) Schema for a document ID.
        :param bool group: (optional) Parameter to specify whether to group reduced
               results by key. Valid only if a reduce function defined in the view. If the
               view emits key in JSON array format, then it is possible to reduce groups
               further based on the number of array elements with the `group_level`
               parameter.
        :param int group_level: (optional) Parameter to specify a group level to be
               used. Only applicable if the view uses keys that are JSON arrays. Implies
               group is `true`. Group level groups the reduced results by the specified
               number of array elements. If unset, results are grouped by the entire array
               key, returning a reduced value for each complete key.
        :param object key: (optional) Schema for any JSON type.
        :param List[object] keys: (optional) Parameter to specify returning only
               documents that match any of the specified keys. A JSON array of keys that
               match the key type emitted by the view function.
        :param bool reduce: (optional) Parameter to specify whether to use the
               reduce function in a map-reduce view. Default is true when a reduce
               function is defined.
               A default `reduce` view type can be disabled to behave like a `map` by
               setting `reduce=false` explicitly.
               Be aware that `include_docs=true` can only be used with `map` views.
        :param bool stable: (optional) Query parameter to specify whether use the
               same replica of  the index on each request. The default value `false`
               contacts all  replicas and returns the result from the first, fastest,
               responder. Setting it to `true` when used in conjunction with
               `update=false`  may improve consistency at the expense of increased latency
               and decreased throughput if the selected replica is not the fastest of the
               available  replicas.
               **Note:** In general setting `true` is discouraged and is strictly not
               recommended when using `update=true`.
        :param object start_key: (optional) Schema for any JSON type.
        :param str start_key_doc_id: (optional) Schema for a document ID.
        :param str update: (optional) Parameter to specify whether or not the view
               in question should be updated prior to responding to the user.
               * `true` - Return results after the view is updated.
               * `false` - Return results without updating the view.
               * `lazy` - Return the view results without waiting for an update, but
               update them immediately after the request.
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
        self.end_key = end_key
        self.end_key_doc_id = end_key_doc_id
        self.group = group
        self.group_level = group_level
        self.key = key
        self.keys = keys
        self.reduce = reduce
        self.stable = stable
        self.start_key = start_key
        self.start_key_doc_id = start_key_doc_id
        self.update = update

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ViewQuery':
        """Initialize a ViewQuery object from a json dictionary."""
        args = {}
        if (att_encoding_info := _dict.get('att_encoding_info')) is not None:
            args['att_encoding_info'] = att_encoding_info
        if (attachments := _dict.get('attachments')) is not None:
            args['attachments'] = attachments
        if (conflicts := _dict.get('conflicts')) is not None:
            args['conflicts'] = conflicts
        if (descending := _dict.get('descending')) is not None:
            args['descending'] = descending
        if (include_docs := _dict.get('include_docs')) is not None:
            args['include_docs'] = include_docs
        if (inclusive_end := _dict.get('inclusive_end')) is not None:
            args['inclusive_end'] = inclusive_end
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        if (skip := _dict.get('skip')) is not None:
            args['skip'] = skip
        if (update_seq := _dict.get('update_seq')) is not None:
            args['update_seq'] = update_seq
        if (end_key := _dict.get('end_key')) is not None:
            args['end_key'] = end_key
        if (end_key_doc_id := _dict.get('end_key_doc_id')) is not None:
            args['end_key_doc_id'] = end_key_doc_id
        if (group := _dict.get('group')) is not None:
            args['group'] = group
        if (group_level := _dict.get('group_level')) is not None:
            args['group_level'] = group_level
        if (key := _dict.get('key')) is not None:
            args['key'] = key
        if (keys := _dict.get('keys')) is not None:
            args['keys'] = keys
        if (reduce := _dict.get('reduce')) is not None:
            args['reduce'] = reduce
        if (stable := _dict.get('stable')) is not None:
            args['stable'] = stable
        if (start_key := _dict.get('start_key')) is not None:
            args['start_key'] = start_key
        if (start_key_doc_id := _dict.get('start_key_doc_id')) is not None:
            args['start_key_doc_id'] = start_key_doc_id
        if (update := _dict.get('update')) is not None:
            args['update'] = update
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
        if hasattr(self, 'end_key') and self.end_key is not None:
            _dict['end_key'] = self.end_key
        if hasattr(self, 'end_key_doc_id') and self.end_key_doc_id is not None:
            _dict['end_key_doc_id'] = self.end_key_doc_id
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
        if hasattr(self, 'start_key') and self.start_key is not None:
            _dict['start_key'] = self.start_key
        if hasattr(self, 'start_key_doc_id') and self.start_key_doc_id is not None:
            _dict['start_key_doc_id'] = self.start_key_doc_id
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
        * `true` - Return results after the view is updated.
        * `false` - Return results without updating the view.
        * `lazy` - Return the view results without waiting for an update, but update them
        immediately after the request.
        """

        TRUE = 'true'
        FALSE = 'false'
        LAZY = 'lazy'



class ViewResult:
    """
    Schema for the result of a query view operation.

    :param int total_rows: (optional) Total number of rows in the view index. Note
          that if the request query narrows the view this is not the number of matching
          rows. The number of matching rows, up to the specified `limit`, is the size of
          the `rows` array.
    :param str update_seq: (optional) Current update sequence for the database.
    :param List[ViewResultRow] rows: rows.
    """

    def __init__(
        self,
        rows: List['ViewResultRow'],
        *,
        total_rows: Optional[int] = None,
        update_seq: Optional[str] = None,
    ) -> None:
        """
        Initialize a ViewResult object.

        :param List[ViewResultRow] rows: rows.
        :param int total_rows: (optional) Total number of rows in the view index.
               Note that if the request query narrows the view this is not the number of
               matching rows. The number of matching rows, up to the specified `limit`, is
               the size of the `rows` array.
        :param str update_seq: (optional) Current update sequence for the database.
        """
        self.total_rows = total_rows
        self.update_seq = update_seq
        self.rows = rows

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ViewResult':
        """Initialize a ViewResult object from a json dictionary."""
        args = {}
        if (total_rows := _dict.get('total_rows')) is not None:
            args['total_rows'] = total_rows
        if (update_seq := _dict.get('update_seq')) is not None:
            args['update_seq'] = update_seq
        if (rows := _dict.get('rows')) is not None:
            args['rows'] = [ViewResultRow.from_dict(v) for v in rows]
        else:
            raise ValueError('Required property \'rows\' not present in ViewResult JSON')
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
            rows_list = []
            for v in self.rows:
                if isinstance(v, dict):
                    rows_list.append(v)
                else:
                    rows_list.append(v.to_dict())
            _dict['rows'] = rows_list
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


class ViewResultRow:
    """
    Schema for a row of a view result.

    :param str caused_by: (optional) The cause of the error (if available).
    :param str error: (optional) The name of the error.
    :param str reason: (optional) The reason the error occurred (if available).
    :param int ref: (optional) An internal error reference (if available).
    :param Document doc: (optional) Schema for a document.
    :param str id: (optional) Schema for a document ID.
    :param object key: Schema for any JSON type.
    :param object value: Schema for any JSON type.
    """

    def __init__(
        self,
        key: object,
        value: object,
        *,
        caused_by: Optional[str] = None,
        error: Optional[str] = None,
        reason: Optional[str] = None,
        ref: Optional[int] = None,
        doc: Optional['Document'] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a ViewResultRow object.

        :param object key: Schema for any JSON type.
        :param object value: Schema for any JSON type.
        :param str caused_by: (optional) The cause of the error (if available).
        :param str error: (optional) The name of the error.
        :param str reason: (optional) The reason the error occurred (if available).
        :param int ref: (optional) An internal error reference (if available).
        :param Document doc: (optional) Schema for a document.
        :param str id: (optional) Schema for a document ID.
        """
        self.caused_by = caused_by
        self.error = error
        self.reason = reason
        self.ref = ref
        self.doc = doc
        self.id = id
        self.key = key
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ViewResultRow':
        """Initialize a ViewResultRow object from a json dictionary."""
        args = {}
        if (caused_by := _dict.get('caused_by')) is not None:
            args['caused_by'] = caused_by
        if (error := _dict.get('error')) is not None:
            args['error'] = error
        if (reason := _dict.get('reason')) is not None:
            args['reason'] = reason
        if (ref := _dict.get('ref')) is not None:
            args['ref'] = ref
        if (doc := _dict.get('doc')) is not None:
            args['doc'] = Document.from_dict(doc)
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (key := _dict.get('key')) is not None:
            args['key'] = key
        else:
            raise ValueError('Required property \'key\' not present in ViewResultRow JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        else:
            raise ValueError('Required property \'value\' not present in ViewResultRow JSON')
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
        if hasattr(self, 'ref') and self.ref is not None:
            _dict['ref'] = self.ref
        if hasattr(self, 'doc') and self.doc is not None:
            if isinstance(self.doc, dict):
                _dict['doc'] = self.doc
            else:
                _dict['doc'] = self.doc.to_dict()
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
