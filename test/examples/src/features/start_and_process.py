# © Copyright IBM Corporation 2023.
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

from ibmcloudant import ChangesFollower
from ibmcloudant.cloudant_v1 import CloudantV1

client = CloudantV1.new_instance()

# Start from a previously persisted seq
# Normally this would be read by the app from persistent storage
# e.g. previously_persisted_seq = your_app_persistence_read_func()
previously_persisted_seq = '3-g1AG3...'
changes_follower = ChangesFollower(
    service=client,
    **{'db': 'example', 'since': previously_persisted_seq})

changes_items = changes_follower.start()
for changes_item in changes_items:
    # do something with changes
    print(changes_item.id)
    for change in changes_item.changes:
        print(change.rev)
    # when change item processing is complete app can store seq
    seq = changes_item.seq
    # write seq to persistent storage for use as since if required to resume later
    # e.g. your_app_persistence_write_func(seq)
    # keep processing changes until the application is terminated or some other stop condition is reached

# Note: iterator above is blocking, code here will be unreachable
# until the iteration is stopped or another stop condition is reached.
# For long running followers careful consideration should be made of where to call stop on the iterator.
