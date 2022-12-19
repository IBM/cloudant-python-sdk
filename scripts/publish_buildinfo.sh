#!/usr/bin/env bash

set -ev
file="/tmp/build.json"
tmpfile="/tmp/build.json.tmp"
printf "Current values set:\n Module ID: $MODULE_ID\nBuild name: $BUILD_NAME\nBuild URL: $BUILD_URL\nBuild timestamp: $BUILD_TIMESTAMP\nBuild number: $BUILD_NUMBER\n"
printf "Artifactory URL: $ARTIFACT_URL\n"
ARTIFACTS=$(curl -H "Authorization: Bearer $ARTIFACTORY_CREDS_PSW" "$ARTIFACT_URL")
HAS_CHILDREN_RESULT=$(echo $ARTIFACTS | jq 'has("children")')
# if 'children' array exists then grab all aritfact uris, else grab parent uri
if [[ "$HAS_CHILDREN_RESULT" == "false" ]]; then
  ARTIFACTS_URI=$(echo $ARTIFACTS | jq -r '.uri' | sed 's:.*/:/:')
else
  ARTIFACTS_URI=$(echo $ARTIFACTS | jq -r '.children[] | .uri')
fi

if [[ -z $ARTIFACTS_URI || -z $MODULE_ID || -z $BUILD_NAME || -z $BUILD_URL || -z $BUILD_TIMESTAMP || -z $BUILD_NUMBER ]]; then
  printf "one or more variables are undefined.  Check printed statement above."
  exit 1
fi

# create new (or write over existing) build.json file
echo -n "" > $file
# get current published build
CURRENT_BUILD=$(curl -H "Authorization: Bearer $ARTIFACTORY_CREDS_PSW" "$STAGE_ROOT"build/"$BUILD_NAME"/"$BUILD_NUMBER")
echo $CURRENT_BUILD
CURRENT_BUILD_INFO=$(echo "$CURRENT_BUILD" | jq -r '.buildInfo')
echo $CURRENT_BUILD_INFO | tee $file

# put build name, number, and url on published artifacts
URL_WITH_PROPS="$ARTIFACT_URL?properties=build.name=$BUILD_NAME;build.number=$BUILD_NUMBER;build.url=$BUILD_URL"
curl -i -X PUT -H "Authorization: Bearer $ARTIFACTORY_CREDS_PSW" "$URL_WITH_PROPS"

# add artifact type and module id to build info file
jq --arg type "$TYPE" '.type = $type' $file > $tmpfile && mv $tmpfile $file
jq --arg id "$MODULE_ID" '.modules[0].id = $id' $file > $tmpfile && mv $tmpfile $file

# get md5 and sha1 from each artifact and add to build info file
for artifact in $ARTIFACTS_URI; do
  # node does not have 'children' artifacts
  if [[ "$HAS_CHILDREN_RESULT" == "false" ]]; then
    ARTIFACT_INFO_URL="$ARTIFACT_URL"
  else
    ARTIFACT_INFO_URL="$ARTIFACT_URL$artifact"
  fi
  GET_ARTIFACT=$(curl -H "Authorization: Bearer $ARTIFACTORY_CREDS_PSW" $ARTIFACT_INFO_URL | jq -r .checksums)
  MD5=$(echo $GET_ARTIFACT | jq -r .md5)
  SHA1=$(echo $GET_ARTIFACT | jq -r .sha1)
  NAME="${artifact#*/}"
  jq --arg name "$NAME" --arg md5 "$MD5" --arg sha1 "$SHA1" '.modules[0].artifacts += [{"name": $name, "md5": $md5, "sha1": $sha1}]' $file > $tmpfile && mv $tmpfile $file
done

if jq empty $file 2>/dev/null; then
  echo "JSON in $file is valid"
else
  echo "JSON in $file is invalid"
  exit 1
fi

curl -i -X PUT -H "Authorization: Bearer $ARTIFACTORY_CREDS_PSW" -H "Content-Type: application/json"  "$STAGE_ROOT"build  --upload-file $file
