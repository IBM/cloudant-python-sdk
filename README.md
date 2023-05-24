[![Build Status](https://github.com/IBM/cloudant-python-sdk/actions/workflows/test.yml/badge.svg?branch=main&event=push)](https://github.com/IBM/cloudant-python-sdk/actions/workflows/test.yml)
[![Release](https://img.shields.io/github/v/release/IBM/cloudant-python-sdk?include_prereleases&sort=semver)](https://github.com/IBM/cloudant-python-sdk/releases/latest)
[![Docs](https://img.shields.io/static/v1?label=Pydoc&message=latest&color=blue)](https://ibm.github.io/cloudant-python-sdk/)

# IBM Cloudant Python SDK Version 0.4.2

IBM Cloudant Python SDK is a client library that interacts with the
[IBM Cloudant APIs](https://cloud.ibm.com/apidocs/cloudant?code=python).

Disclaimer: This library is still a 0.x release. We do consider this
library production-ready and capable, but there are still some
limitations we’re working to resolve, and refinements we want to
deliver. We are working really hard to minimise the disruption from
now until the 1.0 release, but there may still be some changes that
impact applications using this SDK. For now, be sure to pin versions
to avoid surprises.

<details>
<summary>Table of Contents</summary>

<!--
  The TOC below is generated using the `markdown-toc` node package.

      https://github.com/jonschlinkert/markdown-toc

      npx markdown-toc -i README.md
  -->

<!-- toc -->

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Authentication](#authentication)
  * [Authentication with environment variables](#authentication-with-environment-variables)
    + [IAM authentication](#iam-authentication)
    + [Session cookie authentication](#session-cookie-authentication)
    + [Basic authentication](#basic-authentication)
  * [Authentication with external configuration](#authentication-with-external-configuration)
  * [Programmatic authentication](#programmatic-authentication)
- [Using the SDK](#using-the-sdk)
  * [Request timeout configuration](#request-timeout-configuration)
  * [Code examples](#code-examples)
    + [1. Create a database and add a document](#1-create-a-database-and-add-a-document)
    + [2. Retrieve information from an existing database](#2-retrieve-information-from-an-existing-database)
    + [3. Update your previously created document](#3-update-your-previously-created-document)
    + [4. Delete your previously created document](#4-delete-your-previously-created-document)
    + [Further code examples](#further-code-examples)
  * [Error handling](#error-handling)
  * [Raw IO](#raw-io)
  * [Model classes vs dictionaries](#model-classes-vs-dictionaries)
  * [Further resources](#further-resources)
- [Questions](#questions)
- [Issues](#issues)
- [Open source at IBM](#open-source-at-ibm)
- [Contributing](#contributing)
- [License](#license)

<!-- tocstop -->

</details>

## Overview

The IBM Cloudant Python SDK allows developers to programmatically
interact with [IBM Cloudant](https://cloud.ibm.com/apidocs/cloudant)
with the help of the `ibmcloudant` package.

## Features

The purpose of this Python SDK is to wrap most of the HTTP request APIs
provided by Cloudant and supply other functions to ease the usage of Cloudant.
This SDK should make life easier for programmers to do what’s really important
to them: developing software.

Reasons why you should consider using Cloudant Python SDK in your
project:

- Supported by IBM Cloudant.
- Server compatibility with:
    - IBM Cloudant.
    - [Apache CouchDB 3.x](https://docs.couchdb.org/en/stable/) for data operations.
- Includes all the most popular and latest supported endpoints for
  applications.
- Handles the authentication.
- Familiar user experience with IBM Cloud SDKs.
- Flexibility to use either built-in models or byte-based requests and responses for documents.
- Instances of the client are unconditionally thread-safe.

## Prerequisites

- A
  [Cloudant](https://cloud.ibm.com/docs/Cloudant/getting-started.html#step-1-connect-to-your-cloudant-nosql-db-service-instance-on-ibm-cloud)
  service instance or a
  [CouchDB](https://docs.couchdb.org/en/latest/install/index.html)
  server.
- Python 3.7 or above.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "ibmcloudant>=0.4.2"
```

or

```bash
easy_install --upgrade "ibmcloudant>=0.4.2"
```

## Authentication

[service-credentials]: https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-locating-your-service-credentials
[cloud-IAM-mgmt]: https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-managing-access-for-cloudant#introduction-iam-ai
[couch-cookie-auth]: https://docs.couchdb.org/en/stable/api/server/authn.html#cookie-authentication
[cloudant-cookie-auth]: https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-work-with-your-account#cookie-authentication
[couch-basic-auth]: https://docs.couchdb.org/en/stable/api/server/authn.html#basic-authentication
[cloudant-basic-auth]: https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-work-with-your-account#basic-authentication

This library requires some of your
[Cloudant service credentials][service-credentials] to authenticate with your
account.

1. `IAM`, `COUCHDB_SESSION`, `BASIC` or `NOAUTH` **authentication type**.
    1. [*IAM authentication*](#iam-authentication) is highly recommended when your
    back-end database server is [**Cloudant**][cloud-IAM-mgmt]. This
    authentication type requires a server-generated `apikey` instead of a
    user-given password. You can create one
    [here](https://cloud.ibm.com/iam/apikeys).
    1. [*Session cookie (`COUCHDB_SESSION`) authentication*](#session-cookie-authentication)
    is recommended for [Apache CouchDB][couch-cookie-auth] or for
    [Cloudant][cloudant-cookie-auth] when IAM is unavailable. It exchanges username
    and password credentials for an `AuthSession` cookie from the `/_session`
    endpoint.
    1. [*Basic* (or legacy) *authentication*](#basic-authentication) is a fallback
    for both [Cloudant][cloudant-basic-auth] and [Apache CouchDB][couch-basic-auth]
    back-end database servers. This authentication type requires the good old
    `username` and `password` credentials.
    1. *Noauth* authentication does not require credentials. Note that this
    authentication type only works with queries against a database with read
    access for everyone.
1. The service `url`.

There are several ways to **set** these properties:

1. As [environment variables](#authentication-with-environment-variables)
1. The [programmatic approach](#programmatic-authentication)
1. With an [external credentials file](#authentication-with-external-configuration)

### Authentication with environment variables

#### IAM authentication

For Cloudant *IAM authentication*, set the following environmental variables by
replacing the `<url>` and `<apikey>` with your proper
[service credentials][service-credentials]. There is no need to set
`CLOUDANT_AUTH_TYPE` to `IAM` because it is the default.

```bash
CLOUDANT_URL=<url>
CLOUDANT_APIKEY=<apikey>
```

#### Session cookie authentication

For `COUCHDB_SESSION` authentication, set the following environmental variables
by replacing the `<url>`, `<username>` and `<password>` with your proper
[service credentials][service-credentials].

```bash
CLOUDANT_AUTH_TYPE=COUCHDB_SESSION
CLOUDANT_URL=<url>
CLOUDANT_USERNAME=<username>
CLOUDANT_PASSWORD=<password>
```

#### Basic authentication

For *Basic authentication*, set the following environmental variables by
replacing the `<url>`, `<username>` and `<password>` with your proper
[service credentials][service-credentials].

```bash
CLOUDANT_AUTH_TYPE=BASIC
CLOUDANT_URL=<url>
CLOUDANT_USERNAME=<username>
CLOUDANT_PASSWORD=<password>
```

**Note**: There are also additional [*Bearer token*](https://github.com/IBM/python-sdk-core/blob/main/Authentication.md#bearer-token-authentication), [*Container*](https://github.com/IBM/python-sdk-core/blob/main/Authentication.md#container-authentication) and [*VPC Instance*](https://github.com/IBM/python-sdk-core/blob/main/Authentication.md#vpc-instance-authentication) authentication methods. For more details, please follow the provided links.
We recommend that you use [IAM](#iam-authentication) for Cloudant and
[Session](#session-cookie-authentication) for CouchDB authentication.

### Authentication with external configuration

To use an external configuration file, the
[Cloudant API docs](https://cloud.ibm.com/apidocs/cloudant?code=python#authentication-with-external-configuration),
or the
[general SDK usage information](https://github.com/IBM/ibm-cloud-sdk-common#using-external-configuration)
will guide you.

### Programmatic authentication

To learn more about how to use programmatic authentication, see the related
documentation in the
[Cloudant API docs](https://cloud.ibm.com/apidocs/cloudant?code=python#programmatic-authentication)
or in the
[Python SDK Core document](https://github.com/IBM/python-sdk-core/blob/main/Authentication.md) about authentication.

## Using the SDK

For fundamental SDK usage information and config options, please see the common [IBM Cloud SDK](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/README.md) documentation.

### Request timeout configuration

No request timeout is defined, but a 2.5m read and a 60s connect timeout are set by default. Be sure to set a request timeout appropriate to your application usage and environment.
The [request timeout](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/README.md) section contains details on how to change the value.

**Note:** System settings may take precedence over configured timeout values.

### Code examples

The following code examples
[authenticate with the environment variables](#authentication-with-environment-variables).

#### 1. Create a database and add a document

**Note:** This example code assumes that `orders` database does not exist in your account.

This example code creates `orders` database and adds a new document "example"
into it. To connect, you must set your environment variables with
the *service url*, *authentication type* and *authentication credentials*
of your Cloudant service.

Cloudant environment variable naming starts with a *service name* prefix that identifies your service.
By default, this is `CLOUDANT`, see the settings in the
[authentication with environment variables section](#authentication-with-environment-variables).

If you would like to rename your Cloudant service from `CLOUDANT`,
you must use your defined service name as the prefix for all Cloudant related environment variables.

Once the environment variables are set, you can try out the code examples.

[embedmd]:# (test/examples/src/create_db_and_doc.py /import/ $)
```py
import logging

from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1, Document

# Set logging level to show only critical logs
logging.basicConfig(level=logging.CRITICAL)

# 1. Create a client with `CLOUDANT` default service name =============
client = CloudantV1.new_instance()

# 2. Create a database ================================================
example_db_name = "orders"

# Try to create database if it doesn't exist
try:
    put_database_result = client.put_database(
        db=example_db_name
    ).get_result()
    if put_database_result["ok"]:
        print(f'"{example_db_name}" database created.')
except ApiException as ae:
    if ae.code == 412:
        print(f'Cannot create "{example_db_name}" database, ' +
              'it already exists.')

# 3. Create a document ================================================
# Create a document object with "example" id
example_doc_id = "example"
# Setting `id` for the document is optional when "post_document"
# function is used for CREATE. When `id` is not provided the server
# will generate one for your document.
example_document: Document = Document(id=example_doc_id)

# Add "name" and "joined" fields to the document
example_document.name = "Bob Smith"
example_document.joined = "2019-01-24T10:42:59.000Z"

# Save the document in the database with "post_document" function
create_document_response = client.post_document(
    db=example_db_name,
    document=example_document
).get_result()

# =====================================================================
# Note: saving the document can also be done with the "put_document"
# function. In this case `doc_id` is required for a CREATE operation:
"""
create_document_response = client.put_document(
    db=example_db_name,
    doc_id=example_doc_id,
    document=example_document
).get_result()
"""
# =====================================================================

# Keeping track of the revision number of the document object
# is necessary for further UPDATE/DELETE operations:
example_document.rev = create_document_response["rev"]
print(f'You have created the document:\n{example_document}')
```

When you run the code, you see a result similar to the following output.

[embedmd]:# (test/examples/output/create_db_and_doc.txt)
```txt
"orders" database created.
You have created the document:
{
  "_id": "example",
  "_rev": "1-1b403633540686aa32d013fda9041a5d",
  "name": "Bob Smith",
  "joined": "2019-01-24T10:42:99.000Z"
}
```

#### 2. Retrieve information from an existing database

**Note**: This example code assumes that you have created both the `orders`
database and the `example` document by
[running the previous example code](#1-create-a-database-and-add-a-document)
successfully. Otherwise, the following error message occurs, "Cannot delete document because either 'orders'
database or 'example' document was not found."

<details>
<summary>Gather database information example</summary>

[embedmd]:# (test/examples/src/get_info_from_existing_database.py /import/ $)
```py
import json

from ibmcloudant.cloudant_v1 import CloudantV1

# 1. Create a client with `CLOUDANT` default service name ============
client = CloudantV1.new_instance()

# 2. Get server information ===========================================
server_information = client.get_server_information(
).get_result()

print(f'Server Version: {server_information["version"]}')

# 3. Get database information for "orders" ==========================
db_name = "orders"

db_information = client.get_database_information(
    db=db_name
).get_result()

# 4. Show document count in database ==================================
document_count = db_information["doc_count"]

print(f'Document count in \"{db_information["db_name"]}\" '
      f'database is {document_count}.')

# 5. Get "example" document out of the database by document id ============
document_example = client.get_document(
    db=db_name,
    doc_id="example"
).get_result()

print(f'Document retrieved from database:\n'
      f'{json.dumps(document_example, indent=2)}')
```


</details>
When you run the code, you see a result similar to the following output.

[embedmd]:# (test/examples/output/get_info_from_existing_database.txt)
```txt
Server Version: 2.1.1
Document count in "orders" database is 1.
Document retrieved from database:
{
  "_id": "example",
  "_rev": "1-1b403633540686aa32d013fda9041a5d",
  "name": "Bob Smith",
  "joined": "2019-01-24T10:42:99.000Z"
}
```

#### 3. Update your previously created document

**Note**: This example code assumes that you have created both the `orders`
database and the `example` document by
[running the previous example code](#1-create-a-database-and-add-a-document)
successfully. Otherwise, the following error message occurs, "Cannot update document because either 'orders'
database or 'example' document was not found."

<details>
<summary>Update code example</summary>

[embedmd]:# (test/examples/src/update_doc.py /import/ $)
```py
import json
import logging

from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1

# Set logging level to show only critical logs
logging.basicConfig(level=logging.CRITICAL)

# 1. Create a client with `CLOUDANT` default service name =============
client = CloudantV1.new_instance()

# 2. Update the document ==============================================
example_db_name = "orders"
example_doc_id = "example"

# Try to get the document if it previously existed in the database
try:
    document = client.get_document(
        db=example_db_name,
        doc_id=example_doc_id
    ).get_result()

    # =================================================================
    # Note: for response byte stream use:
    """
    document_as_byte_stream = client.get_document_as_stream(
        db=example_db_name,
        doc_id=example_doc_id
    ).get_result()
    """
    # =================================================================

    #  Add Bob Smith's address to the document
    document["address"] = "19 Front Street, Darlington, DL5 1TY"

    #  Remove the joined property from document object
    if "joined" in document:
        document.pop("joined")

    # Update the document in the database
    update_document_response = client.post_document(
        db=example_db_name,
        document=document
    ).get_result()

    # =================================================================
    # Note 1: for request byte stream use:
    """
    update_document_response = client.post_document(
        db=example_db_name,
        document=document_as_byte_stream
    ).get_result()
    """
    # =================================================================

    # =================================================================
    # Note 2: updating the document can also be done with the
    # "put_document" function. `doc_id` and `rev` are required for an
    # UPDATE operation, but `rev` can be provided in the document
    # object as `_rev` too:
    """
    update_document_response = client.put_document(
        db=example_db_name,
        doc_id=example_doc_id,  # doc_id is a required parameter
        rev=document["_rev"],
        document=document  # _rev in the document object CAN replace above `rev` parameter
    ).get_result()
    """
    # =================================================================

    # Keeping track of the latest revision number of the document
    # object is necessary for further UPDATE/DELETE operations:
    document["_rev"] = update_document_response["rev"]
    print(f'You have updated the document:\n' +
          json.dumps(document, indent=2))

except ApiException as ae:
    if ae.code == 404:
        print('Cannot delete document because either ' +
              f'"{example_db_name}" database or "{example_doc_id}" ' +
              'document was not found.')
```


</details>
When you run the code, you see a result similar to the following output.

[embedmd]:# (test/examples/output/update_doc.txt)
```txt
{
  "_id": "example",
  "_rev": "2-4e2178e85cffb32d38ba4e451f6ca376",
  "name": "Bob Smith",
  "address": "19 Front Street, Darlington, DL5 1TY"
}
```

#### 4. Delete your previously created document

**Note**: This example code assumes that you have created both the `orders`
database and the `example` document by
[running the previous example code](#1-create-a-database-and-add-a-document)
successfully. Otherwise, the following error message occurs, "Cannot delete document because either 'orders'
database or 'example' document was not found."

<details>
<summary>Delete code example</summary>

[embedmd]:# (test/examples/src/delete_doc.py /import/ $)
```py
import logging

from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1

# Set logging level to show only critical logs
logging.basicConfig(level=logging.CRITICAL)

# 1. Create a client with `CLOUDANT` default service name =============
client = CloudantV1.new_instance()

# 2. Delete the document ==============================================
example_db_name = "orders"
example_doc_id = "example"

# Try to get the document if it previously existed in the database
try:
    document = client.get_document(
        db=example_db_name,
        doc_id=example_doc_id
    ).get_result()

    delete_document_response = client.delete_document(
        db=example_db_name,
        doc_id=example_doc_id,  # `doc_id` is required for DELETE
        rev=document["_rev"]    # `rev` is required for DELETE
    ).get_result()

    if delete_document_response["ok"]:
        print('You have deleted the document.')

except ApiException as ae:
    if ae.code == 404:
        print('Cannot delete document because either ' +
              f'"{example_db_name}" database or "{example_doc_id}"' +
              'document was not found.')
```


</details>
When you run the code, you see the following output.

[embedmd]:# (test/examples/output/delete_doc.txt)
```txt
You have deleted the document.
```

#### Further code examples

For a complete list of code examples, see the [examples directory](examples#examples-for-python).

### Error handling

For sample code on handling errors, see
[Cloudant API docs](https://cloud.ibm.com/apidocs/cloudant?code=python#error-handling).

### Raw IO

For endpoints that read or write document content it is possible to bypass
usage of the built-in object with byte streams.

Depending on the specific SDK operation it may be possible to:
* accept a user-provided byte stream to send to the server as a request body
* return a byte stream of the server response body to the user

Request byte stream can be supplied for arguments that accept the `BinaryIO` type.
For these cases you can pass this byte stream directly to the HTTP request body.

Response byte stream is supported in functions with the suffix of `_as_stream`.
The returned byte stream allows the response body to be consumed
without triggering JSON unmarshalling that is typically performed by the SDK.

The [update document](#3-update-your-previously-created-document) section
contains examples for both request and response byte stream cases.

The API reference contains further examples of using byte streams.
They are titled "Example request as stream" and are initially collapsed.
Expand them to see examples of:

- Byte requests:
  - [Bulk modify multiple documents in a database](https://cloud.ibm.com/apidocs/cloudant?code=python#postbulkdocs)

- Byte responses:
  - [Query a list of all documents in a database](https://cloud.ibm.com/apidocs/cloudant?code=python#postalldocs)
  - [Query the database document changes feed](https://cloud.ibm.com/apidocs/cloudant?code=python#postchanges)

### Model classes vs dictionaries

This SDK supports two possible formats to define an HTTP request. One approach uses only model classes and the other only dictionaries.

<details>
<summary>Example using model class structure</summary>

[embedmd]:# (test/examples/src/model_vs_dict/put_ddoc_class.py /from/ $)
```py
from ibmcloudant.cloudant_v1 import DesignDocument, CloudantV1, DesignDocumentOptions, SearchIndexDefinition

client = CloudantV1.new_instance()

price_index = SearchIndexDefinition(
    index='function (doc) { index("price", doc.price); }'
)

design_document_options = DesignDocumentOptions(
    partitioned=True
)

partitioned_design_doc = DesignDocument(
    indexes={'findByPrice': price_index},
    options=design_document_options
)

response = client.put_design_document(
    db='products',
    design_document=partitioned_design_doc,
    ddoc='appliances'
).get_result()

print(response)
```

</details>

<details>
<summary>Same example using dictionary structure</summary>

[embedmd]:# (test/examples/src/model_vs_dict/put_ddoc_dict.py /from/ $)
```py
from ibmcloudant.cloudant_v1 import CloudantV1

client = CloudantV1.new_instance()

price_index = {
    'index': 'function (doc) { index("price", doc.price); }'
}

partitioned_design_doc = {
    'indexes': {'findByPrice': price_index},
    'options': {'partitioned': True},
}

response = client.put_design_document(
    db='products',
    design_document=partitioned_design_doc,
    ddoc='appliances'
).get_result()

print(response)
```

</details>

Since model classes and dicts are different data structures, they cannot be combined.

<details>
<summary>This solution will be invalid</summary>

[embedmd]:# (test/examples/src/model_vs_dict/put_ddoc_invalid.py /from/ $)
```py
from ibmcloudant.cloudant_v1 import CloudantV1, DesignDocument

client = CloudantV1.new_instance()

price_index = {
    'index': 'function (doc) { index("price", doc.price); }'
}

partitioned_design_doc = DesignDocument(
    indexes={'findByPrice': price_index},
    options={'partitioned': True}
)

response = client.put_design_document(
    db='products',
    design_document=partitioned_design_doc,
    ddoc='appliances'
).get_result()

print(response)
```

</details>

### Further resources

- [Cloudant API docs](https://cloud.ibm.com/apidocs/cloudant?code=python):
  API reference including usage examples for Cloudant Python SDK API.
- [Pydoc](https://ibm.github.io/cloudant-python-sdk/):
  Cloudant Python SDK API Documentation.
- [Cloudant docs](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-getting-started-with-cloudant):
  The official documentation page for Cloudant.
- [Cloudant blog](https://blog.cloudant.com/):
  Many useful articles about how to optimize Cloudant for common problems.

## Questions

If you are having difficulties using this SDK or have a question about the
IBM Cloud services, ask a question on
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues

If you encounter an issue with the project, you are welcome to submit a
[bug report](https://github.com/IBM/cloudant-python-sdk/issues).

Before you submit a bug report, search for
[similar issues](https://github.com/IBM/cloudant-python-sdk/issues?q=is%3Aissue) and review the
[KNOWN_ISSUES file](KNOWN_ISSUES.md) to verify that your issue hasn't been reported yet.

Please consult the [security policy](https://github.com/IBM/cloudant-python-sdk/security/policy) before opening security related issues.

## Open source at IBM

Find more open source projects on the [IBM GitHub](http://ibm.github.io/) page.

## Contributing

For more information, see [CONTRIBUTING](CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license. To read the full text of the license, see [LICENSE](LICENSE).
