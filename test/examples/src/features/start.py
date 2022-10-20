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

from collections.abc import Iterable

from ibmcloudant import ChangesFollower
from ibmcloudant.cloudant_v1 import CloudantV1, ChangesResultItem

client = CloudantV1.new_instance()

changes_follower = ChangesFollower(
    service=client,
    **{'db': 'example'})

changes_items: Iterable[ChangesResultItem] = changes_follower.start()
# Note: iterable will not do anything until it is iterated
# Create a for loop to iterate over the flow of changes
# for changes_item in changes_items: ...
