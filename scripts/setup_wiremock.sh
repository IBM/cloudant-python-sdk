#!/usr/bin/env bash

set -ev

printenv | grep "^WIREMOCK_" > wiremock.env

# use image at ARTIFACTORY_DOCKER_REPO_VIRTUAL registry if set, otherwise use default registry
docker start wiremock || docker run --name wiremock --rm -d -p "$WIREMOCK_PORT":8080 ${ARTIFACTORY_DOCKER_REPO_VIRTUAL:+${ARTIFACTORY_DOCKER_REPO_VIRTUAL}/}wiremock/wiremock:latest
timeout 120 bash -c 'while [[ "$(curl -s --location -o /dev/null -w ''%{http_code}'' ${WIREMOCK_URL}/__admin)" != "200" ]]; do sleep 2; done' || false
curl "$WIREMOCK_URL"/__admin/mappings/import -X POST -d @stubs/mappings.json
echo "Wiremock started"
