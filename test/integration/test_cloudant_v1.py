# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2024.
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
Integration Tests for CloudantV1
"""

from ibm_cloud_sdk_core import *
import io
import os
import pytest
from ibmcloudant.cloudant_v1 import *

# Config file name
config_file = 'cloudant_v1.env'


class TestCloudantV1:
    """
    Integration Test Class for CloudantV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.cloudant_service = CloudantV1.new_instance(
            )
            assert cls.cloudant_service is not None

            cls.config = read_external_sources(CloudantV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.cloudant_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_server_information(self):
        response = self.cloudant_service.get_server_information()

        assert response.get_status_code() == 200
        server_information = response.get_result()
        assert server_information is not None

    @needscredentials
    def test_get_membership_information(self):
        response = self.cloudant_service.get_membership_information()

        assert response.get_status_code() == 200
        membership_information = response.get_result()
        assert membership_information is not None

    @needscredentials
    def test_get_uuids(self):
        response = self.cloudant_service.get_uuids(
            count=1,
        )

        assert response.get_status_code() == 200
        uuids_result = response.get_result()
        assert uuids_result is not None

    @needscredentials
    def test_get_capacity_throughput_information(self):
        response = self.cloudant_service.get_capacity_throughput_information()

        assert response.get_status_code() == 200
        capacity_throughput_information = response.get_result()
        assert capacity_throughput_information is not None

    @needscredentials
    def test_put_capacity_throughput_configuration(self):
        response = self.cloudant_service.put_capacity_throughput_configuration(
            blocks=10,
        )

        assert response.get_status_code() == 200
        capacity_throughput_information = response.get_result()
        assert capacity_throughput_information is not None

    @needscredentials
    def test_get_db_updates(self):
        response = self.cloudant_service.get_db_updates(
            descending=False,
            feed='normal',
            heartbeat=0,
            limit=0,
            timeout=60000,
            since='0',
        )

        assert response.get_status_code() == 200
        db_updates = response.get_result()
        assert db_updates is not None

    @needscredentials
    def test_post_changes(self):
        response = self.cloudant_service.post_changes(
            db='testString',
            doc_ids=['0007741142412418284'],
            fields=['testString'],
            selector={'anyKey': 'anyValue'},
            last_event_id='testString',
            att_encoding_info=False,
            attachments=False,
            conflicts=False,
            descending=False,
            feed='normal',
            filter='testString',
            heartbeat=0,
            include_docs=False,
            limit=0,
            seq_interval=1,
            since='0',
            style='main_only',
            timeout=60000,
            view='testString',
        )

        assert response.get_status_code() == 200
        changes_result = response.get_result()
        assert changes_result is not None

    @needscredentials
    def test_post_changes_as_stream(self):
        response = self.cloudant_service.post_changes_as_stream(
            db='testString',
            doc_ids=['0007741142412418284'],
            fields=['testString'],
            selector={'anyKey': 'anyValue'},
            last_event_id='testString',
            att_encoding_info=False,
            attachments=False,
            conflicts=False,
            descending=False,
            feed='normal',
            filter='testString',
            heartbeat=0,
            include_docs=False,
            limit=0,
            seq_interval=1,
            since='0',
            style='main_only',
            timeout=60000,
            view='testString',
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_head_database(self):
        response = self.cloudant_service.head_database(
            db='testString',
        )

        assert response.get_status_code() == 200

    @needscredentials
    def test_get_all_dbs(self):
        response = self.cloudant_service.get_all_dbs(
            descending=False,
            end_key='testString',
            limit=0,
            skip=0,
            start_key='testString',
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_post_dbs_info(self):
        response = self.cloudant_service.post_dbs_info(
            keys=['products', 'users', 'orders'],
        )

        assert response.get_status_code() == 200
        list_dbs_info_result = response.get_result()
        assert list_dbs_info_result is not None

    @needscredentials
    def test_get_database_information(self):
        response = self.cloudant_service.get_database_information(
            db='testString',
        )

        assert response.get_status_code() == 200
        database_information = response.get_result()
        assert database_information is not None

    @needscredentials
    def test_put_database(self):
        response = self.cloudant_service.put_database(
            db='testString',
            partitioned=False,
            q=26,
        )

        assert response.get_status_code() == 201
        ok = response.get_result()
        assert ok is not None

    @needscredentials
    def test_head_document(self):
        response = self.cloudant_service.head_document(
            db='testString',
            doc_id='testString',
            if_none_match='testString',
            latest=False,
            rev='testString',
        )

        assert response.get_status_code() == 200

    @needscredentials
    def test_post_document(self):
        # Construct a dict representation of a Attachment model
        attachment_model = {
            'content_type': 'testString',
            'data': 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4=',
            'digest': 'testString',
            'encoded_length': 0,
            'encoding': 'testString',
            'follows': True,
            'length': 0,
            'revpos': 1,
            'stub': True,
        }
        # Construct a dict representation of a Revisions model
        revisions_model = {
            'ids': ['testString'],
            'start': 1,
        }
        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {
            'rev': 'testString',
            'status': 'available',
        }
        # Construct a dict representation of a Document model
        document_model = {
            '_attachments': {'key1': attachment_model},
            '_conflicts': ['testString'],
            '_deleted': True,
            '_deleted_conflicts': ['testString'],
            '_id': 'exampleid',
            '_local_seq': 'testString',
            '_rev': 'testString',
            '_revisions': revisions_model,
            '_revs_info': [document_revision_status_model],
            'brand': 'Foo',
            'colours': '["red","green","black","blue"]',
            'description': 'Slim Colourful Design Electronic Cooking Appliance for ...',
            'image': 'assets/img/0gmsnghhew.jpg',
            'keywords': '["Foo","Scales","Weight","Digital","Kitchen"]',
            'name': 'Digital Kitchen Scales',
            'price': '14.99',
            'productid': '1000042',
            'taxonomy': '["Home","Kitchen","Small Appliances"]',
            'type': 'product',
        }

        response = self.cloudant_service.post_document(
            db='testString',
            document=document_model,
            content_type='application/json',
            batch='ok',
        )

        assert response.get_status_code() == 201
        document_result = response.get_result()
        assert document_result is not None

    @needscredentials
    def test_post_all_docs(self):
        response = self.cloudant_service.post_all_docs(
            db='testString',
            att_encoding_info=False,
            attachments=False,
            conflicts=False,
            descending=False,
            include_docs=False,
            inclusive_end=True,
            limit=10,
            skip=0,
            update_seq=False,
            end_key='testString',
            key='testString',
            keys=['testString'],
            start_key='0007741142412418284',
        )

        assert response.get_status_code() == 200
        all_docs_result = response.get_result()
        assert all_docs_result is not None

    @needscredentials
    def test_post_all_docs_as_stream(self):
        response = self.cloudant_service.post_all_docs_as_stream(
            db='testString',
            att_encoding_info=False,
            attachments=False,
            conflicts=False,
            descending=False,
            include_docs=False,
            inclusive_end=True,
            limit=10,
            skip=0,
            update_seq=False,
            end_key='testString',
            key='testString',
            keys=['testString'],
            start_key='0007741142412418284',
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_post_all_docs_queries(self):
        # Construct a dict representation of a AllDocsQuery model
        all_docs_query_model = {
            'att_encoding_info': False,
            'attachments': False,
            'conflicts': False,
            'descending': False,
            'include_docs': False,
            'inclusive_end': True,
            'limit': 0,
            'skip': 0,
            'update_seq': False,
            'end_key': 'testString',
            'key': 'testString',
            'keys': ['small-appliances:1000042', 'small-appliances:1000043'],
            'start_key': 'testString',
        }

        response = self.cloudant_service.post_all_docs_queries(
            db='testString',
            queries=[all_docs_query_model],
        )

        assert response.get_status_code() == 200
        all_docs_queries_result = response.get_result()
        assert all_docs_queries_result is not None

    @needscredentials
    def test_post_all_docs_queries_as_stream(self):
        # Construct a dict representation of a AllDocsQuery model
        all_docs_query_model = {
            'att_encoding_info': False,
            'attachments': False,
            'conflicts': False,
            'descending': False,
            'include_docs': False,
            'inclusive_end': True,
            'limit': 0,
            'skip': 0,
            'update_seq': False,
            'end_key': 'testString',
            'key': 'testString',
            'keys': ['small-appliances:1000042', 'small-appliances:1000043'],
            'start_key': 'testString',
        }

        response = self.cloudant_service.post_all_docs_queries_as_stream(
            db='testString',
            queries=[all_docs_query_model],
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_post_bulk_docs(self):
        # Construct a dict representation of a Attachment model
        attachment_model = {
            'content_type': 'testString',
            'data': 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4=',
            'digest': 'testString',
            'encoded_length': 0,
            'encoding': 'testString',
            'follows': True,
            'length': 0,
            'revpos': 1,
            'stub': True,
        }
        # Construct a dict representation of a Revisions model
        revisions_model = {
            'ids': ['testString'],
            'start': 1,
        }
        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {
            'rev': 'testString',
            'status': 'available',
        }
        # Construct a dict representation of a Document model
        document_model = {
            '_attachments': {'key1': attachment_model},
            '_conflicts': ['testString'],
            '_deleted': True,
            '_deleted_conflicts': ['testString'],
            '_id': '0007241142412418284',
            '_local_seq': 'testString',
            '_rev': 'testString',
            '_revisions': revisions_model,
            '_revs_info': [document_revision_status_model],
            'date': '2019-01-28T10:44:22.000Z',
            'eventType': 'addedToBasket',
            'productId': '1000042',
            'type': 'event',
            'userid': 'abc123',
        }
        # Construct a dict representation of a BulkDocs model
        bulk_docs_model = {
            'docs': [document_model],
            'new_edits': True,
        }

        response = self.cloudant_service.post_bulk_docs(
            db='testString',
            bulk_docs=bulk_docs_model,
        )

        assert response.get_status_code() == 201
        list_document_result = response.get_result()
        assert list_document_result is not None

    @needscredentials
    def test_post_bulk_get(self):
        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {
            'atts_since': ['1-99b02e08da151943c2dcb40090160bb8'],
            'id': 'order00067',
            'rev': '3-917fa2381192822767f010b95b45325b',
        }

        response = self.cloudant_service.post_bulk_get(
            db='testString',
            docs=[bulk_get_query_document_model],
            attachments=False,
            att_encoding_info=False,
            latest=False,
            revs=False,
        )

        assert response.get_status_code() == 200
        bulk_get_result = response.get_result()
        assert bulk_get_result is not None

    @needscredentials
    def test_post_bulk_get_as_mixed(self):
        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {
            'atts_since': ['1-99b02e08da151943c2dcb40090160bb8'],
            'id': 'order00067',
            'rev': '3-917fa2381192822767f010b95b45325b',
        }

        response = self.cloudant_service.post_bulk_get_as_mixed(
            db='testString',
            docs=[bulk_get_query_document_model],
            attachments=False,
            att_encoding_info=False,
            latest=False,
            revs=False,
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_post_bulk_get_as_related(self):
        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {
            'atts_since': ['1-99b02e08da151943c2dcb40090160bb8'],
            'id': 'order00067',
            'rev': '3-917fa2381192822767f010b95b45325b',
        }

        response = self.cloudant_service.post_bulk_get_as_related(
            db='testString',
            docs=[bulk_get_query_document_model],
            attachments=False,
            att_encoding_info=False,
            latest=False,
            revs=False,
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_post_bulk_get_as_stream(self):
        # Construct a dict representation of a BulkGetQueryDocument model
        bulk_get_query_document_model = {
            'atts_since': ['1-99b02e08da151943c2dcb40090160bb8'],
            'id': 'order00067',
            'rev': '3-917fa2381192822767f010b95b45325b',
        }

        response = self.cloudant_service.post_bulk_get_as_stream(
            db='testString',
            docs=[bulk_get_query_document_model],
            attachments=False,
            att_encoding_info=False,
            latest=False,
            revs=False,
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_get_document(self):
        response = self.cloudant_service.get_document(
            db='testString',
            doc_id='testString',
            if_none_match='testString',
            attachments=False,
            att_encoding_info=False,
            conflicts=False,
            deleted_conflicts=False,
            latest=False,
            local_seq=False,
            meta=False,
            rev='testString',
            revs=False,
            revs_info=False,
        )

        assert response.get_status_code() == 200
        document = response.get_result()
        assert document is not None

    @needscredentials
    def test_get_document_as_mixed(self):
        response = self.cloudant_service.get_document_as_mixed(
            db='testString',
            doc_id='testString',
            if_none_match='testString',
            attachments=False,
            att_encoding_info=False,
            conflicts=False,
            deleted_conflicts=False,
            latest=False,
            local_seq=False,
            meta=False,
            rev='testString',
            revs=False,
            revs_info=False,
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_get_document_as_related(self):
        response = self.cloudant_service.get_document_as_related(
            db='testString',
            doc_id='testString',
            if_none_match='testString',
            attachments=False,
            att_encoding_info=False,
            conflicts=False,
            deleted_conflicts=False,
            latest=False,
            local_seq=False,
            meta=False,
            rev='testString',
            revs=False,
            revs_info=False,
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_get_document_as_stream(self):
        response = self.cloudant_service.get_document_as_stream(
            db='testString',
            doc_id='testString',
            if_none_match='testString',
            attachments=False,
            att_encoding_info=False,
            conflicts=False,
            deleted_conflicts=False,
            latest=False,
            local_seq=False,
            meta=False,
            rev='testString',
            revs=False,
            revs_info=False,
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_put_document(self):
        # Construct a dict representation of a Attachment model
        attachment_model = {
            'content_type': 'testString',
            'data': 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4=',
            'digest': 'testString',
            'encoded_length': 0,
            'encoding': 'testString',
            'follows': True,
            'length': 0,
            'revpos': 1,
            'stub': True,
        }
        # Construct a dict representation of a Revisions model
        revisions_model = {
            'ids': ['testString'],
            'start': 1,
        }
        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {
            'rev': 'testString',
            'status': 'available',
        }
        # Construct a dict representation of a Document model
        document_model = {
            '_attachments': {'key1': attachment_model},
            '_conflicts': ['testString'],
            '_deleted': True,
            '_deleted_conflicts': ['testString'],
            '_id': 'exampleid',
            '_local_seq': 'testString',
            '_rev': 'testString',
            '_revisions': revisions_model,
            '_revs_info': [document_revision_status_model],
            'brand': 'Foo',
            'colours': '["red","green","black","blue"]',
            'description': 'Slim Colourful Design Electronic Cooking Appliance for ...',
            'image': 'assets/img/0gmsnghhew.jpg',
            'keywords': '["Foo","Scales","Weight","Digital","Kitchen"]',
            'name': 'Digital Kitchen Scales',
            'price': '14.99',
            'productid': '1000042',
            'taxonomy': '["Home","Kitchen","Small Appliances"]',
            'type': 'product',
        }

        response = self.cloudant_service.put_document(
            db='testString',
            doc_id='testString',
            document=document_model,
            content_type='application/json',
            if_match='testString',
            batch='ok',
            new_edits=False,
            rev='testString',
        )

        assert response.get_status_code() == 201
        document_result = response.get_result()
        assert document_result is not None

    @needscredentials
    def test_head_design_document(self):
        response = self.cloudant_service.head_design_document(
            db='testString',
            ddoc='testString',
            if_none_match='testString',
        )

        assert response.get_status_code() == 200

    @needscredentials
    def test_get_design_document(self):
        response = self.cloudant_service.get_design_document(
            db='testString',
            ddoc='testString',
            if_none_match='testString',
            attachments=False,
            att_encoding_info=False,
            conflicts=False,
            deleted_conflicts=False,
            latest=False,
            local_seq=False,
            meta=False,
            rev='testString',
            revs=False,
            revs_info=False,
        )

        assert response.get_status_code() == 200
        design_document = response.get_result()
        assert design_document is not None

    @needscredentials
    def test_put_design_document(self):
        # Construct a dict representation of a Attachment model
        attachment_model = {
            'content_type': 'testString',
            'data': 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4=',
            'digest': 'testString',
            'encoded_length': 0,
            'encoding': 'testString',
            'follows': True,
            'length': 0,
            'revpos': 1,
            'stub': True,
        }
        # Construct a dict representation of a Revisions model
        revisions_model = {
            'ids': ['testString'],
            'start': 1,
        }
        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {
            'rev': 'testString',
            'status': 'available',
        }
        # Construct a dict representation of a Analyzer model
        analyzer_model = {
            'name': 'classic',
            'stopwords': ['testString'],
        }
        # Construct a dict representation of a AnalyzerConfiguration model
        analyzer_configuration_model = {
            'name': 'standard',
            'stopwords': ['testString'],
            'fields': {'key1': analyzer_model},
        }
        # Construct a dict representation of a SearchIndexDefinition model
        search_index_definition_model = {
            'analyzer': analyzer_configuration_model,
            'index': 'function (doc) {\n  index("price", doc.price);\n}',
        }
        # Construct a dict representation of a DesignDocumentOptions model
        design_document_options_model = {
            'partitioned': True,
        }
        # Construct a dict representation of a DesignDocumentViewsMapReduce model
        design_document_views_map_reduce_model = {
            'map': 'function(doc) { \n  emit(doc.productid, [doc.brand, doc.name, doc.description]) \n}',
            'reduce': 'testString',
        }
        # Construct a dict representation of a DesignDocument model
        design_document_model = {
            '_attachments': {'key1': attachment_model},
            '_conflicts': ['testString'],
            '_deleted': True,
            '_deleted_conflicts': ['testString'],
            '_id': '_design/appliances',
            '_local_seq': 'testString',
            '_rev': '8-7e2537e5989294471061e0cfd7292725',
            '_revisions': revisions_model,
            '_revs_info': [document_revision_status_model],
            'autoupdate': True,
            'filters': {'key1': 'testString'},
            'indexes': {'findByPrice': search_index_definition_model},
            'language': 'javascript',
            'options': design_document_options_model,
            'validate_doc_update': 'testString',
            'views': {'byApplianceProdId': design_document_views_map_reduce_model},
            'foo': 'testString',
        }

        response = self.cloudant_service.put_design_document(
            db='testString',
            ddoc='testString',
            design_document=design_document_model,
            if_match='testString',
            batch='ok',
            new_edits=False,
            rev='testString',
        )

        assert response.get_status_code() == 201
        document_result = response.get_result()
        assert document_result is not None

    @needscredentials
    def test_get_design_document_information(self):
        response = self.cloudant_service.get_design_document_information(
            db='testString',
            ddoc='testString',
        )

        assert response.get_status_code() == 200
        design_document_information = response.get_result()
        assert design_document_information is not None

    @needscredentials
    def test_post_design_docs(self):
        response = self.cloudant_service.post_design_docs(
            db='testString',
            att_encoding_info=False,
            attachments=False,
            conflicts=False,
            descending=False,
            include_docs=False,
            inclusive_end=True,
            limit=10,
            skip=0,
            update_seq=False,
            end_key='testString',
            key='testString',
            keys=['testString'],
            start_key='0007741142412418284',
        )

        assert response.get_status_code() == 200
        all_docs_result = response.get_result()
        assert all_docs_result is not None

    @needscredentials
    def test_post_design_docs_queries(self):
        # Construct a dict representation of a AllDocsQuery model
        all_docs_query_model = {
            'att_encoding_info': False,
            'attachments': False,
            'conflicts': False,
            'descending': False,
            'include_docs': False,
            'inclusive_end': True,
            'limit': 0,
            'skip': 0,
            'update_seq': False,
            'end_key': 'testString',
            'key': 'testString',
            'keys': ['small-appliances:1000042', 'small-appliances:1000043'],
            'start_key': 'testString',
        }

        response = self.cloudant_service.post_design_docs_queries(
            db='testString',
            queries=[all_docs_query_model],
            accept='application/json',
        )

        assert response.get_status_code() == 200
        all_docs_queries_result = response.get_result()
        assert all_docs_queries_result is not None

    @needscredentials
    def test_post_view(self):
        response = self.cloudant_service.post_view(
            db='testString',
            ddoc='testString',
            view='testString',
            att_encoding_info=False,
            attachments=False,
            conflicts=False,
            descending=False,
            include_docs=True,
            inclusive_end=True,
            limit=10,
            skip=0,
            update_seq=False,
            end_key='testString',
            end_key_doc_id='testString',
            group=False,
            group_level=1,
            key='testString',
            keys=['examplekey'],
            reduce=True,
            stable=False,
            start_key='testString',
            start_key_doc_id='testString',
            update='true',
        )

        assert response.get_status_code() == 200
        view_result = response.get_result()
        assert view_result is not None

    @needscredentials
    def test_post_view_as_stream(self):
        response = self.cloudant_service.post_view_as_stream(
            db='testString',
            ddoc='testString',
            view='testString',
            att_encoding_info=False,
            attachments=False,
            conflicts=False,
            descending=False,
            include_docs=True,
            inclusive_end=True,
            limit=10,
            skip=0,
            update_seq=False,
            end_key='testString',
            end_key_doc_id='testString',
            group=False,
            group_level=1,
            key='testString',
            keys=['examplekey'],
            reduce=True,
            stable=False,
            start_key='testString',
            start_key_doc_id='testString',
            update='true',
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_post_view_queries(self):
        # Construct a dict representation of a ViewQuery model
        view_query_model = {
            'att_encoding_info': False,
            'attachments': False,
            'conflicts': False,
            'descending': False,
            'include_docs': True,
            'inclusive_end': True,
            'limit': 5,
            'skip': 0,
            'update_seq': False,
            'end_key': 'testString',
            'end_key_doc_id': 'testString',
            'group': False,
            'group_level': 1,
            'key': 'testString',
            'keys': ['testString'],
            'reduce': True,
            'stable': False,
            'start_key': 'testString',
            'start_key_doc_id': 'testString',
            'update': 'true',
        }

        response = self.cloudant_service.post_view_queries(
            db='testString',
            ddoc='testString',
            view='testString',
            queries=[view_query_model],
        )

        assert response.get_status_code() == 200
        view_queries_result = response.get_result()
        assert view_queries_result is not None

    @needscredentials
    def test_post_view_queries_as_stream(self):
        # Construct a dict representation of a ViewQuery model
        view_query_model = {
            'att_encoding_info': False,
            'attachments': False,
            'conflicts': False,
            'descending': False,
            'include_docs': True,
            'inclusive_end': True,
            'limit': 5,
            'skip': 0,
            'update_seq': False,
            'end_key': 'testString',
            'end_key_doc_id': 'testString',
            'group': False,
            'group_level': 1,
            'key': 'testString',
            'keys': ['testString'],
            'reduce': True,
            'stable': False,
            'start_key': 'testString',
            'start_key_doc_id': 'testString',
            'update': 'true',
        }

        response = self.cloudant_service.post_view_queries_as_stream(
            db='testString',
            ddoc='testString',
            view='testString',
            queries=[view_query_model],
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_get_partition_information(self):
        response = self.cloudant_service.get_partition_information(
            db='testString',
            partition_key='testString',
        )

        assert response.get_status_code() == 200
        partition_information = response.get_result()
        assert partition_information is not None

    @needscredentials
    def test_post_partition_all_docs(self):
        response = self.cloudant_service.post_partition_all_docs(
            db='testString',
            partition_key='testString',
            att_encoding_info=False,
            attachments=False,
            conflicts=False,
            descending=False,
            include_docs=False,
            inclusive_end=True,
            limit=10,
            skip=0,
            update_seq=False,
            end_key='testString',
            key='testString',
            keys=['testString'],
            start_key='0007741142412418284',
        )

        assert response.get_status_code() == 200
        all_docs_result = response.get_result()
        assert all_docs_result is not None

    @needscredentials
    def test_post_partition_all_docs_as_stream(self):
        response = self.cloudant_service.post_partition_all_docs_as_stream(
            db='testString',
            partition_key='testString',
            att_encoding_info=False,
            attachments=False,
            conflicts=False,
            descending=False,
            include_docs=False,
            inclusive_end=True,
            limit=10,
            skip=0,
            update_seq=False,
            end_key='testString',
            key='testString',
            keys=['testString'],
            start_key='0007741142412418284',
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_post_partition_search(self):
        response = self.cloudant_service.post_partition_search(
            db='testString',
            partition_key='testString',
            ddoc='testString',
            index='testString',
            query='name:Jane* AND active:True',
            bookmark='testString',
            highlight_fields=['testString'],
            highlight_number=1,
            highlight_post_tag='</em>',
            highlight_pre_tag='<em>',
            highlight_size=100,
            include_docs=False,
            include_fields=['testString'],
            limit=3,
            sort=['testString'],
            stale='ok',
        )

        assert response.get_status_code() == 200
        search_result = response.get_result()
        assert search_result is not None

    @needscredentials
    def test_post_partition_search_as_stream(self):
        response = self.cloudant_service.post_partition_search_as_stream(
            db='testString',
            partition_key='testString',
            ddoc='testString',
            index='testString',
            query='name:Jane* AND active:True',
            bookmark='testString',
            highlight_fields=['testString'],
            highlight_number=1,
            highlight_post_tag='</em>',
            highlight_pre_tag='<em>',
            highlight_size=100,
            include_docs=False,
            include_fields=['testString'],
            limit=3,
            sort=['testString'],
            stale='ok',
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_post_partition_view(self):
        response = self.cloudant_service.post_partition_view(
            db='testString',
            partition_key='testString',
            ddoc='testString',
            view='testString',
            att_encoding_info=False,
            attachments=False,
            conflicts=False,
            descending=False,
            include_docs=True,
            inclusive_end=True,
            limit=10,
            skip=0,
            update_seq=False,
            end_key='testString',
            end_key_doc_id='testString',
            group=False,
            group_level=1,
            key='testString',
            keys=['examplekey'],
            reduce=True,
            start_key='testString',
            start_key_doc_id='testString',
            update='true',
        )

        assert response.get_status_code() == 200
        view_result = response.get_result()
        assert view_result is not None

    @needscredentials
    def test_post_partition_view_as_stream(self):
        response = self.cloudant_service.post_partition_view_as_stream(
            db='testString',
            partition_key='testString',
            ddoc='testString',
            view='testString',
            att_encoding_info=False,
            attachments=False,
            conflicts=False,
            descending=False,
            include_docs=True,
            inclusive_end=True,
            limit=10,
            skip=0,
            update_seq=False,
            end_key='testString',
            end_key_doc_id='testString',
            group=False,
            group_level=1,
            key='testString',
            keys=['examplekey'],
            reduce=True,
            start_key='testString',
            start_key_doc_id='testString',
            update='true',
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_post_partition_explain(self):
        response = self.cloudant_service.post_partition_explain(
            db='testString',
            partition_key='testString',
            selector={'type': {'$eq': 'product'}},
            bookmark='testString',
            conflicts=True,
            execution_stats=True,
            fields=['productid', 'name', 'description'],
            limit=25,
            skip=0,
            sort=[{'key1': 'asc'}],
            stable=True,
            update='true',
            use_index=['testString'],
        )

        assert response.get_status_code() == 200
        explain_result = response.get_result()
        assert explain_result is not None

    @needscredentials
    def test_post_partition_find(self):
        response = self.cloudant_service.post_partition_find(
            db='testString',
            partition_key='testString',
            selector={'type': {'$eq': 'product'}},
            bookmark='testString',
            conflicts=True,
            execution_stats=True,
            fields=['productid', 'name', 'description'],
            limit=25,
            skip=0,
            sort=[{'key1': 'asc'}],
            stable=True,
            update='true',
            use_index=['testString'],
        )

        assert response.get_status_code() == 200
        find_result = response.get_result()
        assert find_result is not None

    @needscredentials
    def test_post_partition_find_as_stream(self):
        response = self.cloudant_service.post_partition_find_as_stream(
            db='testString',
            partition_key='testString',
            selector={'type': {'$eq': 'product'}},
            bookmark='testString',
            conflicts=True,
            execution_stats=True,
            fields=['productid', 'name', 'description'],
            limit=25,
            skip=0,
            sort=[{'key1': 'asc'}],
            stable=True,
            update='true',
            use_index=['testString'],
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_post_explain(self):
        response = self.cloudant_service.post_explain(
            db='testString',
            selector={'email_verified': {'$eq': True}},
            bookmark='testString',
            conflicts=True,
            execution_stats=True,
            fields=['_id', 'type', 'name', 'email'],
            limit=3,
            skip=0,
            sort=[{'key1': 'asc'}],
            stable=True,
            update='true',
            use_index=['testString'],
            r=1,
        )

        assert response.get_status_code() == 200
        explain_result = response.get_result()
        assert explain_result is not None

    @needscredentials
    def test_post_find(self):
        response = self.cloudant_service.post_find(
            db='testString',
            selector={'email_verified': {'$eq': True}},
            bookmark='testString',
            conflicts=True,
            execution_stats=True,
            fields=['_id', 'type', 'name', 'email'],
            limit=3,
            skip=0,
            sort=[{'key1': 'asc'}],
            stable=True,
            update='true',
            use_index=['testString'],
            r=1,
        )

        assert response.get_status_code() == 200
        find_result = response.get_result()
        assert find_result is not None

    @needscredentials
    def test_post_find_as_stream(self):
        response = self.cloudant_service.post_find_as_stream(
            db='testString',
            selector={'email_verified': {'$eq': True}},
            bookmark='testString',
            conflicts=True,
            execution_stats=True,
            fields=['_id', 'type', 'name', 'email'],
            limit=3,
            skip=0,
            sort=[{'key1': 'asc'}],
            stable=True,
            update='true',
            use_index=['testString'],
            r=1,
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_get_indexes_information(self):
        response = self.cloudant_service.get_indexes_information(
            db='testString',
        )

        assert response.get_status_code() == 200
        indexes_information = response.get_result()
        assert indexes_information is not None

    @needscredentials
    def test_post_index(self):
        # Construct a dict representation of a Analyzer model
        analyzer_model = {
            'name': 'classic',
            'stopwords': ['testString'],
        }
        # Construct a dict representation of a IndexTextOperatorDefaultField model
        index_text_operator_default_field_model = {
            'analyzer': analyzer_model,
            'enabled': True,
        }
        # Construct a dict representation of a IndexField model
        index_field_model = {
            'name': 'asc',
            'type': 'boolean',
            'foo': 'asc',
        }
        # Construct a dict representation of a IndexDefinition model
        index_definition_model = {
            'default_analyzer': analyzer_model,
            'default_field': index_text_operator_default_field_model,
            'fields': [index_field_model],
            'index_array_lengths': True,
            'partial_filter_selector': {'anyKey': 'anyValue'},
        }

        response = self.cloudant_service.post_index(
            db='testString',
            index=index_definition_model,
            ddoc='json-index',
            name='getUserByName',
            partitioned=True,
            type='json',
        )

        assert response.get_status_code() == 200
        index_result = response.get_result()
        assert index_result is not None

    @needscredentials
    def test_post_search_analyze(self):
        response = self.cloudant_service.post_search_analyze(
            analyzer='english',
            text='running is fun',
        )

        assert response.get_status_code() == 200
        search_analyze_result = response.get_result()
        assert search_analyze_result is not None

    @needscredentials
    def test_post_search(self):
        response = self.cloudant_service.post_search(
            db='testString',
            ddoc='testString',
            index='testString',
            query='name:Jane* AND active:True',
            bookmark='testString',
            highlight_fields=['testString'],
            highlight_number=1,
            highlight_post_tag='</em>',
            highlight_pre_tag='<em>',
            highlight_size=100,
            include_docs=False,
            include_fields=['testString'],
            limit=3,
            sort=['testString'],
            stale='ok',
            counts=['testString'],
            drilldown=[['testString']],
            group_field='testString',
            group_limit=1,
            group_sort=['testString'],
            ranges={'key1': {'key1': {'key1': 'testString'}}},
        )

        assert response.get_status_code() == 200
        search_result = response.get_result()
        assert search_result is not None

    @needscredentials
    def test_post_search_as_stream(self):
        response = self.cloudant_service.post_search_as_stream(
            db='testString',
            ddoc='testString',
            index='testString',
            query='name:Jane* AND active:True',
            bookmark='testString',
            highlight_fields=['testString'],
            highlight_number=1,
            highlight_post_tag='</em>',
            highlight_pre_tag='<em>',
            highlight_size=100,
            include_docs=False,
            include_fields=['testString'],
            limit=3,
            sort=['testString'],
            stale='ok',
            counts=['testString'],
            drilldown=[['testString']],
            group_field='testString',
            group_limit=1,
            group_sort=['testString'],
            ranges={'key1': {'key1': {'key1': 'testString'}}},
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_get_search_info(self):
        response = self.cloudant_service.get_search_info(
            db='testString',
            ddoc='testString',
            index='testString',
        )

        assert response.get_status_code() == 200
        search_info_result = response.get_result()
        assert search_info_result is not None

    @needscredentials
    def test_head_replication_document(self):
        response = self.cloudant_service.head_replication_document(
            doc_id='testString',
            if_none_match='testString',
        )

        assert response.get_status_code() == 200

    @needscredentials
    def test_head_scheduler_document(self):
        response = self.cloudant_service.head_scheduler_document(
            doc_id='testString',
        )

        assert response.get_status_code() == 200

    @needscredentials
    def test_head_scheduler_job(self):
        response = self.cloudant_service.head_scheduler_job(
            job_id='testString',
        )

        assert response.get_status_code() == 200

    @needscredentials
    def test_get_replication_document(self):
        response = self.cloudant_service.get_replication_document(
            doc_id='testString',
            if_none_match='testString',
            attachments=False,
            att_encoding_info=False,
            conflicts=False,
            deleted_conflicts=False,
            latest=False,
            local_seq=False,
            meta=False,
            rev='testString',
            revs=False,
            revs_info=False,
        )

        assert response.get_status_code() == 200
        replication_document = response.get_result()
        assert replication_document is not None

    @needscredentials
    def test_put_replication_document(self):
        # Construct a dict representation of a Attachment model
        attachment_model = {
            'content_type': 'testString',
            'data': 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4=',
            'digest': 'testString',
            'encoded_length': 0,
            'encoding': 'testString',
            'follows': True,
            'length': 0,
            'revpos': 1,
            'stub': True,
        }
        # Construct a dict representation of a Revisions model
        revisions_model = {
            'ids': ['testString'],
            'start': 1,
        }
        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {
            'rev': 'testString',
            'status': 'available',
        }
        # Construct a dict representation of a ReplicationCreateTargetParameters model
        replication_create_target_parameters_model = {
            'n': 3,
            'partitioned': False,
            'q': 1,
        }
        # Construct a dict representation of a ReplicationDatabaseAuthBasic model
        replication_database_auth_basic_model = {
            'password': 'testString',
            'username': 'testString',
        }
        # Construct a dict representation of a ReplicationDatabaseAuthIam model
        replication_database_auth_iam_model = {
            'api_key': 'testString',
        }
        # Construct a dict representation of a ReplicationDatabaseAuth model
        replication_database_auth_model = {
            'basic': replication_database_auth_basic_model,
            'iam': replication_database_auth_iam_model,
        }
        # Construct a dict representation of a ReplicationDatabase model
        replication_database_model = {
            'auth': replication_database_auth_model,
            'headers': {'key1': 'testString'},
            'url': 'https://my-source-instance.cloudantnosqldb.appdomain.cloud.example/animaldb',
        }
        # Construct a dict representation of a UserContext model
        user_context_model = {
            'db': 'testString',
            'name': 'john',
            'roles': ['_replicator'],
        }
        # Construct a dict representation of a ReplicationDocument model
        replication_document_model = {
            '_attachments': {'key1': attachment_model},
            '_conflicts': ['testString'],
            '_deleted': True,
            '_deleted_conflicts': ['testString'],
            '_id': 'testString',
            '_local_seq': 'testString',
            '_rev': 'testString',
            '_revisions': revisions_model,
            '_revs_info': [document_revision_status_model],
            'cancel': False,
            'checkpoint_interval': 4500,
            'connection_timeout': 15000,
            'continuous': True,
            'create_target': True,
            'create_target_params': replication_create_target_parameters_model,
            'doc_ids': ['badger', 'lemur', 'llama'],
            'filter': 'ddoc/my_filter',
            'http_connections': 10,
            'owner': 'testString',
            'query_params': {'key1': 'testString'},
            'retries_per_request': 3,
            'selector': {'_id': {'$regex': 'docid'}},
            'since_seq': '34-g1AAAAGjeJzLYWBgYMlgTmGQT0lKzi9KdU',
            'socket_options': '[{keepalive, true}, {nodelay, false}]',
            'source': replication_database_model,
            'source_proxy': 'testString',
            'target': replication_database_model,
            'target_proxy': 'testString',
            'use_bulk_get': True,
            'use_checkpoints': False,
            'user_ctx': user_context_model,
            'winning_revs_only': False,
            'worker_batch_size': 400,
            'worker_processes': 3,
            'foo': 'testString',
        }

        response = self.cloudant_service.put_replication_document(
            doc_id='testString',
            replication_document=replication_document_model,
            if_match='testString',
            batch='ok',
            new_edits=False,
            rev='testString',
        )

        assert response.get_status_code() == 201
        document_result = response.get_result()
        assert document_result is not None

    @needscredentials
    def test_get_scheduler_docs(self):
        response = self.cloudant_service.get_scheduler_docs(
            limit=0,
            skip=0,
            states=['initializing'],
        )

        assert response.get_status_code() == 200
        scheduler_docs_result = response.get_result()
        assert scheduler_docs_result is not None

    @needscredentials
    def test_get_scheduler_document(self):
        response = self.cloudant_service.get_scheduler_document(
            doc_id='testString',
        )

        assert response.get_status_code() == 200
        scheduler_document = response.get_result()
        assert scheduler_document is not None

    @needscredentials
    def test_get_scheduler_jobs(self):
        response = self.cloudant_service.get_scheduler_jobs(
            limit=25,
            skip=0,
        )

        assert response.get_status_code() == 200
        scheduler_jobs_result = response.get_result()
        assert scheduler_jobs_result is not None

    @needscredentials
    def test_get_scheduler_job(self):
        response = self.cloudant_service.get_scheduler_job(
            job_id='testString',
        )

        assert response.get_status_code() == 200
        scheduler_job = response.get_result()
        assert scheduler_job is not None

    @needscredentials
    def test_get_session_information(self):
        response = self.cloudant_service.get_session_information()

        assert response.get_status_code() == 200
        session_information = response.get_result()
        assert session_information is not None

    @needscredentials
    def test_get_security(self):
        response = self.cloudant_service.get_security(
            db='testString',
        )

        assert response.get_status_code() == 200
        security = response.get_result()
        assert security is not None

    @needscredentials
    def test_put_security(self):
        # Construct a dict representation of a SecurityObject model
        security_object_model = {
            'names': ['superuser'],
            'roles': ['admins'],
        }

        response = self.cloudant_service.put_security(
            db='testString',
            admins=security_object_model,
            members=security_object_model,
            cloudant={'key1': ['_reader']},
            couchdb_auth_only=True,
        )

        assert response.get_status_code() == 200
        ok = response.get_result()
        assert ok is not None

    @needscredentials
    def test_post_api_keys(self):
        response = self.cloudant_service.post_api_keys()

        assert response.get_status_code() == 201
        api_keys_result = response.get_result()
        assert api_keys_result is not None

    @needscredentials
    def test_put_cloudant_security_configuration(self):
        # Construct a dict representation of a SecurityObject model
        security_object_model = {
            'names': ['testString'],
            'roles': ['testString'],
        }

        response = self.cloudant_service.put_cloudant_security_configuration(
            db='testString',
            cloudant={'antsellseadespecteposene': ['_reader', '_writer', '_admin'], 'garbados': ['_reader', '_writer'], 'nobody': ['_reader']},
            admins=security_object_model,
            members=security_object_model,
            couchdb_auth_only=True,
        )

        assert response.get_status_code() == 200
        ok = response.get_result()
        assert ok is not None

    @needscredentials
    def test_get_cors_information(self):
        response = self.cloudant_service.get_cors_information()

        assert response.get_status_code() == 200
        cors_information = response.get_result()
        assert cors_information is not None

    @needscredentials
    def test_put_cors_configuration(self):
        response = self.cloudant_service.put_cors_configuration(
            origins=['https://example.com', 'https://www.example.com'],
            allow_credentials=True,
            enable_cors=True,
        )

        assert response.get_status_code() == 200
        ok = response.get_result()
        assert ok is not None

    @needscredentials
    def test_head_attachment(self):
        response = self.cloudant_service.head_attachment(
            db='testString',
            doc_id='testString',
            attachment_name='testString',
            if_match='testString',
            if_none_match='testString',
            rev='testString',
        )

        assert response.get_status_code() == 200

    @needscredentials
    def test_get_attachment(self):
        response = self.cloudant_service.get_attachment(
            db='testString',
            doc_id='testString',
            attachment_name='testString',
            if_match='testString',
            if_none_match='testString',
            range='testString',
            rev='testString',
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_put_attachment(self):
        response = self.cloudant_service.put_attachment(
            db='testString',
            doc_id='testString',
            attachment_name='testString',
            attachment=io.BytesIO(b'This is a mock file.').getvalue(),
            content_type='application/octet-stream',
            if_match='testString',
            rev='testString',
        )

        assert response.get_status_code() == 201
        document_result = response.get_result()
        assert document_result is not None

    @needscredentials
    def test_head_local_document(self):
        response = self.cloudant_service.head_local_document(
            db='testString',
            doc_id='testString',
            if_none_match='testString',
        )

        assert response.get_status_code() == 200

    @needscredentials
    def test_get_local_document(self):
        response = self.cloudant_service.get_local_document(
            db='testString',
            doc_id='testString',
            accept='application/json',
            if_none_match='testString',
            attachments=False,
            att_encoding_info=False,
            local_seq=False,
        )

        assert response.get_status_code() == 200
        document = response.get_result()
        assert document is not None

    @needscredentials
    def test_put_local_document(self):
        # Construct a dict representation of a Attachment model
        attachment_model = {
            'content_type': 'testString',
            'data': 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4=',
            'digest': 'testString',
            'encoded_length': 0,
            'encoding': 'testString',
            'follows': True,
            'length': 0,
            'revpos': 1,
            'stub': True,
        }
        # Construct a dict representation of a Revisions model
        revisions_model = {
            'ids': ['testString'],
            'start': 1,
        }
        # Construct a dict representation of a DocumentRevisionStatus model
        document_revision_status_model = {
            'rev': 'testString',
            'status': 'available',
        }
        # Construct a dict representation of a Document model
        document_model = {
            '_attachments': {'key1': attachment_model},
            '_conflicts': ['testString'],
            '_deleted': True,
            '_deleted_conflicts': ['testString'],
            '_id': 'exampleid',
            '_local_seq': 'testString',
            '_rev': 'testString',
            '_revisions': revisions_model,
            '_revs_info': [document_revision_status_model],
            'brand': 'Foo',
            'colours': '["red","green","black","blue"]',
            'description': 'Slim Colourful Design Electronic Cooking Appliance for ...',
            'image': 'assets/img/0gmsnghhew.jpg',
            'keywords': '["Foo","Scales","Weight","Digital","Kitchen"]',
            'name': 'Digital Kitchen Scales',
            'price': '14.99',
            'productid': '1000042',
            'taxonomy': '["Home","Kitchen","Small Appliances"]',
            'type': 'product',
        }

        response = self.cloudant_service.put_local_document(
            db='testString',
            doc_id='testString',
            document=document_model,
            content_type='application/json',
            batch='ok',
        )

        assert response.get_status_code() == 201
        document_result = response.get_result()
        assert document_result is not None

    @needscredentials
    def test_post_revs_diff(self):
        response = self.cloudant_service.post_revs_diff(
            db='testString',
            document_revisions={'key1': ['testString']},
        )

        assert response.get_status_code() == 200
        dict = response.get_result()
        assert dict is not None

    @needscredentials
    def test_get_shards_information(self):
        response = self.cloudant_service.get_shards_information(
            db='testString',
        )

        assert response.get_status_code() == 200
        shards_information = response.get_result()
        assert shards_information is not None

    @needscredentials
    def test_get_document_shards_info(self):
        response = self.cloudant_service.get_document_shards_info(
            db='testString',
            doc_id='testString',
        )

        assert response.get_status_code() == 200
        document_shard_info = response.get_result()
        assert document_shard_info is not None

    @needscredentials
    def test_head_up_information(self):
        response = self.cloudant_service.head_up_information()

        assert response.get_status_code() == 200

    @needscredentials
    def test_get_active_tasks(self):
        response = self.cloudant_service.get_active_tasks()

        assert response.get_status_code() == 200
        list_active_task = response.get_result()
        assert list_active_task is not None

    @needscredentials
    def test_get_up_information(self):
        response = self.cloudant_service.get_up_information()

        assert response.get_status_code() == 200
        up_information = response.get_result()
        assert up_information is not None

    @needscredentials
    def test_get_activity_tracker_events(self):
        response = self.cloudant_service.get_activity_tracker_events()

        assert response.get_status_code() == 200
        activity_tracker_events = response.get_result()
        assert activity_tracker_events is not None

    @needscredentials
    def test_post_activity_tracker_events(self):
        response = self.cloudant_service.post_activity_tracker_events(
            types=['management', 'data'],
        )

        assert response.get_status_code() == 200
        ok = response.get_result()
        assert ok is not None

    @needscredentials
    def test_get_current_throughput_information(self):
        response = self.cloudant_service.get_current_throughput_information()

        assert response.get_status_code() == 200
        current_throughput_information = response.get_result()
        assert current_throughput_information is not None

    @needscredentials
    def test_delete_database(self):
        response = self.cloudant_service.delete_database(
            db='testString',
        )

        assert response.get_status_code() == 200
        ok = response.get_result()
        assert ok is not None

    @needscredentials
    def test_delete_document(self):
        response = self.cloudant_service.delete_document(
            db='testString',
            doc_id='testString',
            if_match='testString',
            batch='ok',
            rev='testString',
        )

        assert response.get_status_code() == 200
        document_result = response.get_result()
        assert document_result is not None

    @needscredentials
    def test_delete_design_document(self):
        response = self.cloudant_service.delete_design_document(
            db='testString',
            ddoc='testString',
            if_match='testString',
            batch='ok',
            rev='testString',
        )

        assert response.get_status_code() == 200
        document_result = response.get_result()
        assert document_result is not None

    @needscredentials
    def test_delete_index(self):
        response = self.cloudant_service.delete_index(
            db='testString',
            ddoc='testString',
            type='json',
            index='testString',
        )

        assert response.get_status_code() == 200
        ok = response.get_result()
        assert ok is not None

    @needscredentials
    def test_delete_replication_document(self):
        response = self.cloudant_service.delete_replication_document(
            doc_id='testString',
            if_match='testString',
            batch='ok',
            rev='testString',
        )

        assert response.get_status_code() == 200
        document_result = response.get_result()
        assert document_result is not None

    @needscredentials
    def test_delete_attachment(self):
        response = self.cloudant_service.delete_attachment(
            db='testString',
            doc_id='testString',
            attachment_name='testString',
            if_match='testString',
            rev='testString',
            batch='ok',
        )

        assert response.get_status_code() == 200
        document_result = response.get_result()
        assert document_result is not None

    @needscredentials
    def test_delete_local_document(self):
        response = self.cloudant_service.delete_local_document(
            db='testString',
            doc_id='testString',
            batch='ok',
        )

        assert response.get_status_code() == 200
        document_result = response.get_result()
        assert document_result is not None
