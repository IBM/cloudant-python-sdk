#!/usr/bin/env bash

set -ev

printenv | grep "^WIREMOCK_" > wiremock.env

docker run --rm -d -p "$WIREMOCK_PORT":8080 rodolpheche/wiremock:2.27.1
timeout 120 bash -c 'while [[ "$(curl -s --location -o /dev/null -w ''%{http_code}'' ${WIREMOCK_URL}/__admin)" != "200" ]]; do sleep 2; done' || false
curl "$WIREMOCK_URL"/__admin/mappings/import -X POST -d @stubs/mappings.json
echo "Wiremock started"
