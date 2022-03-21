# coding: utf-8

# © Copyright IBM Corporation 2022.
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

from ibmcloudant.cloudant_v1 import DesignDocument, CloudantV1, DesignDocumentOptions, SearchIndexDefinition

client = CloudantV1.new_instance()

price_index = SearchIndexDefinition(
    index='function (doc) { index("price", doc.price); }'
)

design_document_options = DesignDocumentOptions(
    partitioned=True
)

partitioned_design_doc = DesignDocument(
    indexes={'findByPrice': price_index},
    options=design_document_options
)

response = client.put_design_document(
    db='products',
    design_document=partitioned_design_doc,
    ddoc='appliances'
).get_result()

print(response)
