#!/usr/bin/env bash

set -e

# Store GIT properties in vars
GIT_COMMIT=$(git rev-parse --short HEAD)
GIT_REPO=$(git remote get-url origin)

# Use SDK version as tag from Jenkins env vars
TAG_NAME=$NEW_SDK_VERSION

# Create documentation
printf ">>>>> Generate new documentation\n"
python3 -m tox -e docs

# Clone gh-pages branch
printf ">>>>> Publishing pydoc for release build: repo=%s branch=%s build_num=%s job_name=%s\n" ${GIT_REPO} ${BRANCH_NAME} ${BUILD_NUMBER} ${JOB_NAME}
printf ">>>>> Cloning repository's gh-pages branch into directory 'gh-pages'\n"
git clone --branch=gh-pages https://github.com/IBM/cloudant-python-sdk.git gh-pages

printf ">>>>> Finished cloning...\n"

pushd gh-pages

# Create a new directory for this tag_name and copy the aggregated pydocs there, if it's a tagged release.
if [ -n "TAG_NAME" ]; then
  printf "\n>>>>> Copying aggregated pydocs to new tagged-release directory: %s\n" ${BRANCH_NAME}
  rm -rf docs/${TAG_NAME}
  mkdir -p docs/${TAG_NAME}
  cp -rf ../apidocs/* docs/${TAG_NAME}

  printf "\n>>>>> Generating gh-pages index.html...\n"
  ../scripts/pydoc/generate-index-html.sh > index.html

  # Update the 'latest' symlink to point to this directory
  pushd docs
  rm -f latest
  ln -s ./${TAG_NAME} latest
  printf "\n>>>>> Updated 'docs/latest' symlink:\n"
  ls -l latest
  popd

  printf "\n>>>>> Committing new pydoc...\n"
  git add -f .
  git commit -m "Pydoc for release ${TAG_NAME} (${GIT_COMMIT})"
  git push -f origin gh-pages

  popd

  printf "\n>>>>> Published pydoc for release build: repo=%s branch=%s build_num=%s job_name=%s\n" ${GIT_REPO} ${BRANCH_NAME} ${BUILD_NUMBER} ${JOB_NAME}
else
  printf "\n>>>>> Failed to publish pydoc for release build: TAG_NAME was empty\n"
fi
