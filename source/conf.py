# Copyright IBM Corporation 2021.
# SPDX-License-Identifier: Apache-2.0

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
print(os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'Cloudant Python SDK'
copyright = 'Copyright IBM Corp. 2021, 2023.'
author = '@IBM/cloudant-sdks'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'autodoc2',
    'myst_parser',
    'sphinx_rtd_theme',
]

myst_enable_extensions = ['colon_fence', 'fieldlist']

autodoc2_packages = [
    {
        'path': '../ibmcloudant',
        'exclude_files': [
            'common.py',
            'version.py',
            'cloudant_base_service.py',
            'couchdb_session_get_authenticator_patch.py',
            'couchdb_session_token_manager.py'
        ]
    }
]

autodoc2_sort_names = True

autodoc2_index_template = None

autodoc2_hidden_objects = ['dunder', 'private', 'inherited']

autodoc2_docstring_parser_regexes = [
    (r'.*', 'myst'),
]

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['apidocs/ibmcloudant/ibmcloudant.rst']

# -- Patch generated rst -----------------------------------------------------

file_path = '../ibmcloudant/cloudant_v1.py'
print(f'[patching] file {file_path}')
# read source file
with open(file_path, 'r') as file:
    lines = file.readlines()
# patch broken markup
codeblock = False
for i in range(len(lines)):
    # replace class vars to :param: for better rendering
    if ':attr ' in lines[i]:
        lines[i] = lines[i].replace(':attr', ':param')
    # replace note with tip admonition
    if '### Note' in lines[i]:
        lines[i] = '        :::{tip}\n'
        codeblock = True
    if codeblock and lines[i] == '\n':
        lines[i] = '        :::\n\n'
        codeblock = False
# write back
with open(file_path, 'w') as file:
    file.writelines(lines)

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# Sort members by type
autodoc_member_order = 'groupwise'
