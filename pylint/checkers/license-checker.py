#!/usr/bin/env python
# coding: utf-8

# © Copyright IBM Corporation 2020.
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

from pylint.interfaces import IRawChecker, HIGH
from pylint.checkers import BaseChecker

LICENSE_HEADER = """
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
""".strip().split("\n")


class LicenseChecker(BaseChecker):
    """
    Check for license header
    """

    __implements__ = IRawChecker

    name = 'license-checker'
    msgs = {'E9903': ('Include or fix license header in file',
                      'file-no-license',
                      'Your file has no license or it needs to be fixed'),
            }
    options = ()

    def process_module(self, node):
        i = 0
        with node.stream() as stream:
            for (lineno, raw_actual_line) in enumerate(stream):
                actual_line = raw_actual_line.decode("utf-8").strip()
                if actual_line == '':
                    continue
                if actual_line[0] != '#' and i != len(LICENSE_HEADER):
                    self.add_message('file-no-license', line=lineno, confidence=HIGH)
                    break
                if i < len(LICENSE_HEADER) and actual_line == LICENSE_HEADER[i]:
                    i += 1
                    continue


def register(linter):
    linter.register_checker(LicenseChecker(linter))
