# © Copyright IBM Corporation 2025. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from ibmcloudant import Pager, Pagination, PagerType
from ibmcloudant.cloudant_v1 import CloudantV1

# Initialize service
service = CloudantV1.new_instance()

# Setup options
opts = {
    'db': 'events',  # example database name
    'limit': 50,  # limit option sets the page size
    'partition_key': 'ns1HJS13AMkK',  # query only this partition
    'fields': ['productId', 'eventType', 'date'],  # return these fields
    'selector': {'userId': 'abc123'}  # select documents with "userId" field equal to "abc123"
}

# Create pagination
pagination = Pagination.new_pagination(
    service, PagerType.POST_PARTITION_FIND, **opts)
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

# Option: use pager next page
# For retrieving one page at a time with a method call.
pager: Pager = pagination.pager()
if pager.has_next():
    page = pager.get_next()
    # Do something with page

# Option: use pager all results
# For retrieving all result rows in a single list
# Note: all result rows may be very large!
# Preferably use iterables instead of get_all for memory efficiency with large result sets.
all_pager: Pager = pagination.pager()
all_rows = all_pager.get_all()
for page in all_rows:
    # Do something with row
    pass
