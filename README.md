[![Build Status](https://github.com/IBM/cloudant-python-sdk/actions/workflows/test.yml/badge.svg?branch=main&event=push)](https://github.com/IBM/cloudant-python-sdk/actions/workflows/test.yml)
[![Release](https://img.shields.io/github/v/release/IBM/cloudant-python-sdk?include_prereleases&sort=semver)](https://github.com/IBM/cloudant-python-sdk/releases/latest)
[![Docs](https://img.shields.io/static/v1?label=Pydoc&message=latest&color=blue)](https://ibm.github.io/cloudant-python-sdk/)

# IBM Cloudant Python SDK Version 0.10.6

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

<!-- toc -->
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Using the SDK](#using-the-sdk)
  * [Authentication](#authentication)
  * [Automatic retries](#automatic-retries)
  * [Request timeout configuration](#request-timeout-configuration)
  * [Code examples](#code-examples)
  * [Error handling](#error-handling)
  * [Raw IO](#raw-io)
  * [Model classes vs dictionaries](#model-classes-vs-dictionaries)
  * [Further resources](#further-resources)
- [Questions](#questions)
- [Issues](#issues)
- [Versioning and LTS support](#versioning-and-lts-support)
- [Open source at IBM](#open-source-at-ibm)
- [Contributing](#contributing)
- [License](#license)

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
- Built-in [Changes feed follower](./docs/Changes_Follower.md)
- Built-in [Pagination](./docs/Pagination.md) (beta)
- Instances of the client are unconditionally thread-safe.

## Prerequisites

- A
  [Cloudant](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-getting-started-with-cloudant)
  service instance or a
  [CouchDB](https://docs.couchdb.org/en/latest/install/index.html)
  server.
- Python 3.9 or above.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "ibmcloudant>=0.10.6"
```

or

```bash
easy_install --upgrade "ibmcloudant>=0.10.6"
```

## Using the SDK

For fundamental SDK usage information and config options, please see the common [IBM Cloud SDK](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/README.md) documentation.

This library requires configuration with a service URL and
[Cloudant service credentials][service-credentials] to authenticate with your
account.

There are several ways to **set** these authentication properties:

1. As [environment variables](./docs/Authentication.md#authentication-with-environment-variables)
2. The [programmatic approach](./docs/Authentication.md#programmatic-authentication)
3. With an [external credentials file](./docs/Authentication.md#authentication-with-external-configuration)

The following section describes the different authentication types and provides environment variable examples.
Examples for other configuration methods are available by following the provided links.

### Authentication

Consult the [authentication document](./docs/Authentication.md)
for comprehensive details of all the available authentication methods and how to configure them with environment settings
or programmatically.

Quick start for Cloudant with an IAM API key:
```sh
CLOUDANT_URL=https://~replaceWithYourUniqueHost~.cloudantnosqldb.appdomain.cloud # use your own Cloudant public or private URL # use your own Cloudant public or private URL
CLOUDANT_APIKEY=a1b2c3d4e5f6f1g4h7j3k6l9m2p5q8s1t4v7x0z3 # use your own IAM API key
```

Quick start for Apache CouchDB with a username/password session:
```sh
CLOUDANT_AUTH_TYPE=COUCHDB_SESSION
CLOUDANT_URL=http://~replaceWithYourUniqueHost~.example:5984 # use your CouchDB URL
CLOUDANT_USERNAME=username # replace with your username
CLOUDANT_PASSWORD=password # replace with your password
```

### Automatic retries

The SDK supports a generalized retry feature that can automatically retry on common errors.

The [automatic retries](https://github.com/IBM/ibm-cloud-sdk-common#automatic-retries) section has details on how to enable the retries with default values and customize the retries programmatically or with external configuration.

### Request timeout configuration

No request timeout is defined, but a 2.5m read and a 60s connect timeout are set by default. Be sure to set a request timeout appropriate to your application usage and environment.
The [request timeout](https://github.com/IBM/ibm-cloud-sdk-common#configuring-request-timeouts) section contains details on how to change the value.

**Note:** System settings may take precedence over configured timeout values.

### Code examples

Quick start example to list all databases (assumes environment variable [authentication](#authentication)):

```py
# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_all_dbs().get_result()

print(response)
```

[More tutorial examples](./docs/Examples.md) for creating a database
and document create, read, update and delete operations.

For a complete list of code examples, see the [examples directory](https://github.com/IBM/cloudant-python-sdk/tree/v0.10.6/examples#examples-for-python).

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

The [update document](./docs/Examples.md#3-update-your-previously-created-document) section
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

- [Cloudant Python SDK feature docs](./docs)
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
[KNOWN_ISSUES file](https://github.com/IBM/cloudant-python-sdk/tree/v0.10.6/KNOWN_ISSUES.md) to verify that your issue hasn't been reported yet.

Please consult the [security policy](https://github.com/IBM/cloudant-python-sdk/security/policy) before opening security related issues.

## Versioning and LTS support

This SDK follows semantic versioning with respect to the definition of user facing APIs.
This means under some circumstances breaking changes may occur within a major or minor version
of the SDK related to changes in supported language platforms.

The SDK is supported on the available LTS releases of the language platform.
The LTS language versions are listed in the prerequisites:
* [LTS versions currently supported by the SDK](https://github.com/IBM/cloudant-python-sdk/#prerequisites)
* [LTS versions for this release of the SDK](#prerequisites)

Incompatible changes from new language versions are not added to the SDK
until they are available in the minimum supported language version.

When language LTS versions move out of support the following will happen:
* Existing SDK releases will continue to run on obsolete language versions, but will no longer be supported.
* The minimum language version supported by the SDK will be updated to the next available LTS.
* New language features may be added in subsequent SDK releases that will cause breaking changes
  if the new releases of the SDK are used with older, now unsupported, language levels.

## Open source at IBM

Find more open source projects on the [IBM GitHub](http://ibm.github.io/) page.

## Contributing

For more information, see [CONTRIBUTING](https://github.com/IBM/cloudant-python-sdk/tree/v0.10.6/CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license. To read the full text of the license, see [LICENSE](https://github.com/IBM/cloudant-python-sdk/tree/v0.10.6/LICENSE).
