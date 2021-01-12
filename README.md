<!--
  The example codes and outputs below are generated using the `embedmd` go
  package.

      https://github.com/campoy/embedmd

  You should regenerate the example codes after making any changes to
  examples in the test/examples/ folder.

      embedmd -w README.md
  -->

[![Build Status](https://travis-ci.com/IBM/cloudant-python-sdk.svg?branch=master)](https://travis-ci.com/IBM/cloudant-python-sdk)
[![Release](https://img.shields.io/github/v/release/IBM/cloudant-python-sdk?include_prereleases&sort=semver)](https://github.com/IBM/cloudant-python-sdk/releases/latest)

# IBM Cloudant Python SDK Version 0.0.29

Python client library to interact with the
[IBM Cloudant APIs](https://cloud.ibm.com/apidocs/cloudant?code=python).

Disclaimer: this SDK is being released initially as a **pre-release** version.
Changes might occur which impact applications that use this SDK.

<details>
<summary>Table of Contents</summary>

<!--
  The TOC below is generated using the `markdown-toc` node package.

      https://github.com/jonschlinkert/markdown-toc

  You should regenerate the TOC after making changes to this file.

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
  * [Code examples](#code-examples)
    + [1. Retrieve information from an existing database](#1-retrieve-information-from-an-existing-database)
    + [2. Create your own database and add a document](#2-create-your-own-database-and-add-a-document)
    + [3. Update your previously created document](#3-update-your-previously-created-document)
    + [4. Delete your previously created document](#4-delete-your-previously-created-document)
  * [Error handling](#error-handling)
  * [Raw IO](#raw-io)
  * [Further resources](#further-resources)
- [Questions](#questions)
- [Issues](#issues)
- [Open source @ IBM](#open-source--ibm)
- [Contributing](#contributing)
- [License](#license)

<!-- tocstop -->

</details>

## Overview

The IBM Cloudant Python SDK allows developers to programmatically
interact with IBM [Cloudant](https://cloud.ibm.com/apidocs/cloudant)
with the help of the `ibmcloudant` package.

## Features

The purpose of this Python SDK is to wrap most of the HTTP request APIs
provided by Cloudant and supply other functions to ease the usage of Cloudant.
This SDK should make life easier for programmers to do what’s really important
for them: develop.

Reasons why you should consider using Cloudant Python SDK in your
project:

- Supported by IBM Cloudant.
- Server compatibility with:
    - IBM Cloudant "Classic"
    - [Cloudant "Standard on Transaction Engine"](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-overview-te) for APIs compatible with Cloudant "Classic" (see the [Feature Parity page](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-overview-te#feature-parity-between-ibm-cloudant-on-the-transaction-engine-vs-classic-architecture) for further details).
    - [Apache CouchDB 3.x](https://docs.couchdb.org/en/stable/) for data operations
- Includes all the most popular and latest supported endpoints for
  applications.
- Handles the authentication.
- Familiar user experience of IBM Cloud SDKs.
- Flexibility to use either built-in models or byte-based requests and responses for documents.
- Instances of the client are unconditionally thread-safe.

## Prerequisites

- A
  [Cloudant](https://cloud.ibm.com/docs/Cloudant/getting-started.html#step-1-connect-to-your-cloudant-nosql-db-service-instance-on-ibm-cloud)
  service instance or a
  [CouchDB](https://docs.couchdb.org/en/latest/install/index.html)
  server.
- Python 3.5.3 or above.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "ibmcloudant>=0.0.29"
```

or

```bash
easy_install --upgrade "ibmcloudant>=0.0.29"
```

## Authentication

[service-credentials]: https://cloud.ibm.com/docs/Cloudant?topic=cloudant-creating-an-ibm-cloudant-instance-on-ibm-cloud#locating-your-service-credentials
[cloud-IAM-mgmt]: https://cloud.ibm.com/docs/Cloudant?topic=cloudant-ibm-cloud-identity-and-access-management-iam-
[couch-cookie-auth]: https://docs.couchdb.org/en/stable/api/server/authn.html#cookie-authentication
[cloudant-cookie-auth]: https://cloud.ibm.com/docs/Cloudant?topic=cloudant-authentication#cookie-authentication
[couch-basic-auth]: https://docs.couchdb.org/en/stable/api/server/authn.html#basic-authentication
[cloudant-basic-auth]: https://cloud.ibm.com/docs/services/Cloudant/api?topic=cloudant-authentication#basic-authentication

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
    1. *Noauth* authentication does not need any credentials. Note that this
    authentication type will only work for queries against a database with read
    access for everyone.
1. The service `url`.

There are several ways to **set** these properties:

1. As [environment variables](#authentication-with-environment-variables)
1. The [programmatic approach](#programmatic-authentication)
1. With an [external credentials file](#authentication-with-external-configuration)

### Authentication with environment variables

#### IAM authentication

For Cloudant *IAM authentication* set the following environmental variables by
replacing `<url>` and `<apikey>` with your proper
[service credentials][service-credentials]. There is no need to set
`CLOUDANT_AUTH_TYPE` to `IAM` because it is the default.

```bash
CLOUDANT_URL=<url>
CLOUDANT_APIKEY=<apikey>
```

#### Session cookie authentication

For `COUCHDB_SESSION` authentication set the following environmental variables
by replacing `<url>`, `<username>` and `<password>` with your proper
[service credentials][service-credentials].

```bash
CLOUDANT_AUTH_TYPE=COUCHDB_SESSION
CLOUDANT_URL=<url>
CLOUDANT_USERNAME=<username>
CLOUDANT_PASSWORD=<password>
```

#### Basic authentication

For *Basic authentication* set the following environmental variables by
replacing `<url>`, `<username>` and `<password>` with your proper
[service credentials][service-credentials].

```bash
CLOUDANT_AUTH_TYPE=BASIC
CLOUDANT_URL=<url>
CLOUDANT_USERNAME=<username>
CLOUDANT_PASSWORD=<password>
```

**Note**: We recommend using [IAM](#iam-authentication) for Cloudant and
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
[Python SDK Core document about authentication](https://github.com/IBM/python-sdk-core/blob/master/Authentication.md).

## Using the SDK

For general IBM Cloud SDK usage information, please see
[IBM Cloud SDK Common](https://github.com/IBM/ibm-cloud-sdk-common/blob/master/README.md).

### Code examples

The code examples below will follow the
[authentication with environment variables](#authenticate-with-environment-variables).

#### 1. Retrieve information from an existing database

**Note:** this example code assumes that `animaldb` database does not exist in your account.

This example code gathers some information about an existing database hosted on
the https://examples.cloudant.com/ service `url`. To do this, you need to
extend your environment variables with the *service url* and *authentication
type* to use `NOAUTH` authentication while reaching the `animaldb` database.
This step is necessary for the SDK to distinguish the `EXAMPLES` custom service
name from the default service name which is `CLOUDANT`.

```bash
EXAMPLES_URL=https://examples.cloudant.com
EXAMPLES_AUTH_TYPE=NOAUTH
```

Once the environment variables are set, you can try out the code examples.

[embedmd]:# (test/examples/src/get_info_from_existing_database.py)
```py
import json

from ibmcloudant.cloudant_v1 import CloudantV1

# 1. Create a Cloudant client with "EXAMPLES" service name ============
client = CloudantV1.new_instance(service_name="EXAMPLES")

# 2. Get server information ===========================================
server_information = client.get_server_information(
).get_result()

print(f'Server Version: {server_information["version"]}')

# 3. Get database information for "animaldb" ==========================
db_name = "animaldb"

db_information = client.get_database_information(
    db=db_name
).get_result()

# 4. Show document count in database ==================================
document_count = db_information["doc_count"]

print(f'Document count in \"{db_information["db_name"]}\" '
      f'database is {document_count}.')

# 5. Get zebra document out of the database by document id ============
document_about_zebra = client.get_document(
    db=db_name,
    doc_id="zebra"
).get_result()

print(f'Document retrieved from database:\n'
      f'{json.dumps(document_about_zebra, indent=2)}')
```

The result of the code is similar to the following output.

[embedmd]:# (test/examples/output/get_info_from_existing_database.txt)
```txt
Server Version: 2.1.1
Document count in "animaldb" database is 11.
Document retrieved from database:
{
  "_id": "zebra",
  "_rev": "3-750dac460a6cc41e6999f8943b8e603e",
  "wiki_page": "http://en.wikipedia.org/wiki/Plains_zebra",
  "min_length": 2,
  "max_length": 2.5,
  "min_weight": 175,
  "max_weight": 387,
  "class": "mammal",
  "diet": "herbivore"
}
```

#### 2. Create your own database and add a document

**Note:** this example code assumes that `orders` database does not exist in your account.

Now comes the exciting part of creating your own `orders` database and adding
a document about *Bob Smith* with your own [IAM](#iam-authentication) or
[Basic](#basic-authentication) service credentials.

<details>
<summary>Create code example</summary>

[embedmd]:# (test/examples/src/create_db_and_doc.py)
```py
import logging

from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1, Document

# Set logging level to show only critical logs
logging.basicConfig(level=logging.CRITICAL)

# 1. Create a client with `CLOUDANT` default service name ============
client = CloudantV1.new_instance()

# 2. Create a database ===============================================
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

# 3. Create a document ===============================================
# Create a document object with "example" id
example_doc_id = "example"
example_document: Document = Document(id=example_doc_id)

# Add "name" and "joined" fields to the document
example_document.name = "Bob Smith"
example_document.joined = "2019-01-24T10:42:99.000Z"

# Save the document in the database
create_document_response = client.post_document(
    db=example_db_name,
    document=example_document
).get_result()

# Keep track of the revision number from the `example` document object
example_document.rev = create_document_response["rev"]
print(f'You have created the document:\n{example_document}')
```


</details>
The result of the code is similar to the following output.

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

#### 3. Update your previously created document

**Note**: this example code assumes that you have created both the `orders`
database and the `example` document by
[running this previous example code](#2-create-your-own-database-and-add-a-document)
successfully, otherwise you get the `Cannot update document because either "orders"
database or "example" document was not found.` message.

<details>
<summary>Update code example</summary>

[embedmd]:# (test/examples/src/update_doc.py)
```py
import json
import logging

from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1

# Set logging level to show only critical logs
logging.basicConfig(level=logging.CRITICAL)

# 1. Create a client with `CLOUDANT` default service name ============
client = CloudantV1.new_instance()

# 2. Update the document =============================================
example_db_name = "orders"
example_doc_id = "example"

# Try to get the document if it previously existed in the database
try:
    document = client.get_document(
        db=example_db_name,
        doc_id=example_doc_id
    ).get_result()

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

    # Keep track with the revision number of the document object:
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
The result of the code is similar to the following output.

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

**Note**: this example code assumes that you have created both the `orders`
database and the `example` document by
[running this previous example code](#2-create-your-own-database-and-add-a-document)
successfully, otherwise you get the `Cannot delete document because either "orders"
database or "example" document was not found.` message.

<details>
<summary>Delete code example</summary>

[embedmd]:# (test/examples/src/delete_doc.py)
```py
import logging

from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1

# Set logging level to show only critical logs
logging.basicConfig(level=logging.CRITICAL)

# 1. Create a client with `CLOUDANT` default service name ============
client = CloudantV1.new_instance()

# 2. Delete the document =============================================
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
        doc_id=example_doc_id,
        rev=document["_rev"]
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
The result of the code is the following output.

[embedmd]:# (test/examples/output/delete_doc.txt)
```txt
You have deleted the document.
```

### Error handling

For sample code on handling errors, please see
[Cloudant API docs](https://cloud.ibm.com/apidocs/cloudant?code=python#error-handling).

### Raw IO

For endpoints that read or write document content it is possible to bypass
usage of the built-in models and send or receive a bytes response.
For examples of using byte streams, see the API reference documentation
("Example request as a stream" section).

- [Bulk modify multiple documents in a database](https://cloud.ibm.com/apidocs/cloudant?code=python#postbulkdocs)
- [Query a list of all documents in a database](https://cloud.ibm.com/apidocs/cloudant?code=python#postalldocs)
- [Query the database document changes feed](https://cloud.ibm.com/apidocs/cloudant?code=python#postchanges)

### Further resources

- [Cloudant API docs](https://cloud.ibm.com/apidocs/cloudant?code=python):
  API examples for Cloudant Python SDK.
- [Cloudant docs](https://cloud.ibm.com/docs/services/Cloudant?topic=cloudant-overview#overview):
  The official documentation page for Cloudant.
- [Cloudant Learning Center](https://developer.ibm.com/clouddataservices/docs/compose/cloudant/):
  The official learning center with several useful videos which help you to use
  Cloudant successfully.
- [Cloudant blog](https://blog.cloudant.com/):
  Many useful articles how to optimize Cloudant for common problems.

## Questions

If you are having difficulties using this SDK or have a question about the
IBM Cloud services, please ask a question on
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues

If you encounter an issue with the project, you are welcome to submit a
[bug report](https://github.com/IBM/cloudant-python-sdk/issues).
Before that, please search for similar issues. It's possible that someone
has already reported the problem.

## Open source @ IBM

Find more open source projects on the [IBM Github Page](http://ibm.github.io/).

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](LICENSE).
