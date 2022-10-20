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

cf_params = {
    'db': 'example',  # Required: the database name.
    'limit': 100,  # Optional: return only 100 changes (including duplicates).
    'since': '3-g1AG3...'  # Optional: start from this sequence ID (e.g. with a value read from persistent storage).
}

changes_follower = ChangesFollower(
    service=client,  # Required: the Cloudant service client instance.
    error_tolerance=10000,  # Optional: suppress transient errors for at least 10 seconds before terminating.
    **cf_params  # Required: changes feed configuration options dict.
)
