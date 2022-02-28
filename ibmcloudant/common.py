# coding: utf-8

# © Copyright IBM Corporation 2020, 2022.
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
Common module
"""
import platform
from .version import __version__

SDK_ANALYTICS_HEADER = 'X-IBMCloud-SDK-Analytics'
USER_AGENT_HEADER = 'User-Agent'
SDK_NAME = 'cloudant-python-sdk'


def get_system_info():  # pylint: disable=missing-docstring
    return f'python.version={platform.python_version()}; ' \
           f'python.vendor={platform.python_implementation()}; ' \
           f'os.name={platform.system()}; ' \
           f'os.version={platform.release()}; ' \
           f'os.arch={platform.machine()}; lang=python;'


def get_user_agent():  # pylint: disable=missing-docstring
    return user_agent


def get_sdk_analytics(service_name, service_version, operation_id):  # pylint: disable=missing-docstring
    return 'service_name={0};service_version={1};operation_id={2}'.format(
        service_name, service_version, operation_id)


user_agent = f'{SDK_NAME}/{__version__} ({get_system_info()})'


def get_sdk_headers(service_name, service_version, operation_id):  # pylint: disable=missing-docstring
    headers = {}
    headers[SDK_ANALYTICS_HEADER] = get_sdk_analytics(service_name, service_version, operation_id)
    headers[USER_AGENT_HEADER] = get_user_agent()
    return headers
