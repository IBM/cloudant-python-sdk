#!/usr/bin/env bash

set -ev

printenv | grep "^WIREMOCK_" > wiremock.env
# setup env file for gen ITs
printenv | grep "^CLOUDANT_" > cloudant_v1.env

docker start wiremock || docker run --name wiremock --rm -d -p "$WIREMOCK_PORT":8080 wiremock/wiremock:latest
timeout 120 bash -c 'while [[ "$(curl -s --location -o /dev/null -w ''%{http_code}'' ${WIREMOCK_URL}/__admin)" != "200" ]]; do sleep 2; done' || false
curl "$WIREMOCK_URL"/__admin/mappings/import -X POST -d @stubs/mappings.json
curl "$WIREMOCK_URL"/__admin/mappings/import -X POST -d @stubs/gen-its-mappings.json
echo "Wiremock started"
