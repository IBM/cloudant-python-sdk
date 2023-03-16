#!/usr/bin/env bash

set -ev

printenv | grep "^WIREMOCK_" > wiremock.env
# setup env file for gen ITs
echo -e "CLOUDANT_AUTH_TYPE=noauth\nCLOUDANT_URL=$WIREMOCK_URL" >> cloudant_v1.env

# use image at ARTIFACTORY_DOCKER_REPO_VIRTUAL registry if set, otherwise use default registry
timeout 120 bash -c 'while [[ "$(curl -s --location -o /dev/null -w ''%{http_code}'' ${WIREMOCK_URL}/__admin)" != "200" ]]; do sleep 2; done' || false
curl "$WIREMOCK_URL"/__admin/mappings/import -X POST -d @stubs/mappings.json
curl "$WIREMOCK_URL"/__admin/mappings/import -X POST -d @stubs/gen-its-mappings.json
echo "Wiremock started"
