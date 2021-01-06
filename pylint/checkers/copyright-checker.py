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

import re

from pylint.interfaces import IRawChecker, HIGH
from pylint.checkers import BaseChecker


class CopyrightChecker(BaseChecker):
    """
    Check for copyright
    """

    __implements__ = IRawChecker

    name = 'copyright-checker'
    msgs = {'E9902': ('Include or fix copyright in file',
                      'file-no-copyright',
                      'Your file has no copyright or it needs to be fixed'),
            }
    options = ()

    def process_module(self, node):
        ibm_copyright_regex = r'^# © Copyright IBM Corporation 20\d\d(?:, 20\d\d)?\.$'
        with node.stream() as stream:
            # get actual file line by line
            for (lineno, raw_actual_line) in enumerate(stream):
                actual_line = raw_actual_line.decode("utf-8").strip()
                if actual_line == '':
                    continue
                if actual_line[0] != '#':
                    self.add_message('file-no-copyright', line=lineno, confidence=HIGH)
                    break
                if re.match(ibm_copyright_regex, actual_line):
                    break


def register(linter):
    linter.register_checker(CopyrightChecker(linter))
