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
changes_follower = ChangesFollower(
    service=client,
    **{'db': 'example'})
changes_items = changes_follower.start()

for changes_item in changes_items:
    # Option 1: call stop after some condition
    # Note that since the iterator is blocking at least one item
    # must be returned from it to reach to this point.
    # Additional changes may be processed before the iterator stops.
    changes_follower.stop()

# Option 2: call stop method when you want to end the continuous loop from
# outside the iterator.  For example, you've put the changes follower in a
# separate thread and need to call stop on the main thread.
# Note: in this context the call must be made from a different thread because
# code immediately following the iterator is unreachable until the iterator
# has stopped.
changes_follower.stop()
