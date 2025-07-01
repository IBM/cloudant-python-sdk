# © Copyright IBM Corporation 2025. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from ibmcloudant import Pager, Pagination, PagerType
from ibmcloudant.cloudant_v1 import CloudantV1

# Initialize service
service = CloudantV1.new_instance()

# Setup options
opts = {
    'db': 'shoppers',  # example database name
    'limit': 50,  # limit option sets the page size
    'ddoc': 'allUsers',  # use the allUsers design document
    'index': 'activeUsers',  # search in this index
    'query': 'name:Jane* AND active:True'  # Lucene search query
}

# Create pagination
pagination = Pagination.new_pagination(
    service, PagerType.POST_SEARCH, **opts)
# pagination can be reused without side-effects as a factory for iterables or pagers
# options are fixed at pagination creation time

# Option: iterate pages
# Ideal for using a for loop with each page.
# Each call to pages() returns a fresh iterator that can be traversed once.
for page in pagination.pages():
    # Do something with page
    pass

# Option: iterate rows
# Ideal for using a for loop with each row.
# Each call to rows() returns a fresh iterator that can be traversed once.
for row in pagination.rows():
    # Do something with row
    pass

# For retrieving one page at a time with a method call.
pager: Pager = pagination.pager()
if pager.get_next():
    page = pager.get_next()
    # Do something with page

all_pager: Pager = pagination.pager()
all_rows = all_pager.get_all()
for page in all_rows:
    # Do something with row
    pass
