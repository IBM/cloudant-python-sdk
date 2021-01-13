#!/bin/sh -e

# based on https://odoepner.wordpress.com/2012/02/17/shell-script-to-generate-simple-index-html/

echo '<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>IBM Cloudant SDK for Python</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
</head>
<body>
<div class="container">
    <div class="page-header">
        <h1>IBM Cloudant Python SDK Documentation</h1>
    </div>

    <p><a href="https://cloud.ibm.com/apidocs/cloudant?code=python">Cloudant API Docs</a>
        | <a href="https://github.com/IBM/cloudant-python-sdk">GitHub</a>
    </p>

    <p>Pydoc by release:</p>
    <ul><li><a href="docs/latest">Latest</a></li>'
ls docs | grep --invert-match index.html | grep -v latest | sed 's/^.*/<li><a href="docs\/&">&<\/a><\/li>/'
echo '    </ul>
</div>
</body>
</html>'
