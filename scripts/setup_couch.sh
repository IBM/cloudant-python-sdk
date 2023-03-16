#!/usr/bin/env bash

set -ev

printenv | grep "^SERVER_" >> cloudant_v1.env
# if you change the image version please regenerate example output captures
# use image at ARTIFACTORY_DOCKER_REPO_VIRTUAL registry if set, otherwise use default registry

# shellcheck disable=SC2016
timeout 120 bash -c 'while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' ${SERVER_URL}/_up)" != "200" ]]; do sleep 5; done' || false
curl -XPUT -u "$SERVER_USERNAME":"$SERVER_PASSWORD" "$SERVER_URL"/_users
curl -XPUT -u "$SERVER_USERNAME":"$SERVER_PASSWORD" "$SERVER_URL"/stores
curl -XPOST -u "$SERVER_USERNAME":"$SERVER_PASSWORD" -H "Content-type: application/json" -d '{}' "$SERVER_URL"/stores
