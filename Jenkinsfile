#!groovy

pipeline {
  agent {
    label 'sdks-executor'
  }
  options {
    skipDefaultCheckout()
  }
  environment {
    GH_CREDS = credentials('gh-sdks-automation')
    STAGE_ROOT = 'https://na.artifactory.swg-devops.com/artifactory/api/'
    buildType = ''
  }
  stages {
    stage('Checkout') {
      steps {
        script {
          defaultInit()
          applyCustomizations()
          checkoutResult = checkout scm
          commitHash = "${checkoutResult.GIT_COMMIT[0..6]}"
          sh '''
            git config --global user.email $GH_SDKS_AUTOMATION_MAIL
            git config --global user.name $GH_CREDS_USR
            git config --global credential.username $GH_CREDS_USR
            git config --global credential.helper '!f() { echo password=\$GH_CREDS_PSW; echo; }; f'
          '''
        }
      }
    }
    stage('QA') {
      steps {
        withEnv(['DOCKER_HOST=',
          'SERVER_AUTH_TYPE=basic',
          'SERVER_URL=http://127.0.0.1:5984',
          'WIREMOCK_URL=http://127.0.0.1:8080',
          'WIREMOCK_PORT=8080'
        ]) {
          withCredentials([
            usernamePassword(credentialsId: 'container-test-server',
                             usernameVariable: 'SERVER_USERNAME',
                             passwordVariable: 'SERVER_PASSWORD')
            ]) {
              sh './scripts/setup_couch.sh'
              sh './scripts/setup_wiremock.sh'
              runTests()
          }
        }
      }

      post {
        always {
          junit (
            testResults: '**/junitreports/*.xml'
          )
        }
      }
    }
    stage('Publish[staging]') {
      steps {
        bumpVersion(true)
        publishStaging()
        publishArtifactoryBuildInfo()
      }
    }
    stage('Run Gauge tests') {
      steps {
        script {
            buildResults = null
            prefixedSdkVersion = ''
            if (libName == 'go') {
              prefixedSdkVersion = "@$commitHash"
            } else if (libName == 'node') {
              prefixedSdkVersion = "@${env.NEW_SDK_VERSION}"
            } else if (libName == 'python') {
              prefixedSdkVersion = "==${env.NEW_SDK_VERSION}"
            } else if (libName == 'java') {
              prefixedSdkVersion = "${env.NEW_SDK_VERSION}"
            }
          try {
            buildResults = build job: "/${env.SDKS_GAUGE_PIPELINE_PROJECT}/${env.BRANCH_NAME}", parameters: [
                string(name: 'SDK_RUN_LANG', value: "$libName"),
                string(name: "SDK_VERSION_${libName.toUpperCase()}", value: "$prefixedSdkVersion")]
          } catch (Exception e) {
            // only run build in sdks-gauge master branch if BRANCH_NAME doesn't exist
            if (buildResults == null) {
              echo "No matching branch named '${env.BRANCH_NAME}' in sdks-gauge, building master branch"
              build job: "/${env.SDKS_GAUGE_PIPELINE_PROJECT}/master", parameters: [
                  string(name: 'SDK_RUN_LANG', value: "$libName"),
                  string(name: "SDK_VERSION_${libName.toUpperCase()}", value: "$prefixedSdkVersion")]
            }
          }
        }
      }
    }
    stage('Publish[repository]') {
      when {
        beforeAgent true
        allOf {
          // Publish master branch, but not on the version update commit after just publishing
          branch 'master'
          not {
            changelog 'Update version.*'
          }
        }
      }
      steps {
        // Throw away any temporary version changes used for stage/test
        sh 'git reset --hard'
        bumpVersion(false)
        // Push the version bump and release tag
        sh 'git push --tags origin HEAD:master'
        publishPublic()
        publishDocs()
      }
    }
  }
}

def libName
def commitHash
def bumpVersion
def customizeVersion
def prefixSdkVersion
def customizePublishingInfo
def publishArtifactoryBuildInfo
def artifactUrl = ''
def moduleId = ''
def buildName = ''
def buildType = ''

void defaultInit() {
  // Default to using bump2version
  bumpVersion = { isDevRelease ->
    newVersion = getNextVersion(isDevRelease)
    // Set an env var with the new version
    env.NEW_SDK_VERSION = newVersion
    doVersionBump(isDevRelease, newVersion)
  }

  doVersionBump = { isDevRelease, newVersion, allowDirty ->
    sh "bump2version --new-version ${newVersion} ${allowDirty ? '--allow-dirty': ''} ${isDevRelease ? '--no-commit' : '--tag --tag-message "Release {new_version}"'} patch"
  }

  getNextVersion = { isDevRelease ->
    // Identify what the next patch version is
    patchBumpedVersion = sh returnStdout: true, script: 'bump2version --list --dry-run patch | grep new_version=.* | cut -f2 -d='
    // Now the customized new version
    return getNewVersion(isDevRelease, patchBumpedVersion)
  }

  // Default no-op implementation to use semverFormatVersion
  customizeVersion = { semverFormatVersion ->
    semverFormatVersion
  }

  // Default no-op, may be overridden
  customizePublishingInfo = {}

  publishArtifactoryBuildInfo = {
    // create custom build name e.g. SDKs::cloudant-node-sdk::generated-branch
    buildName = "${env.JOB_NAME}".replaceAll('/', '::')
    buildType = 'GENERIC' // default, may be overridden
    customizePublishingInfo()
    withEnv(["LIB_NAME=${libName}",
      "TYPE=${buildType}",
      "ARTIFACT_URL=${artifactUrl}",
      "MODULE_ID=${moduleId}",
      "BUILD_NAME=${buildName}"]) {
      withCredentials([usernamePassword(credentialsId: 'artifactory', passwordVariable: 'ARTIFACTORY_APIKEY', usernameVariable: 'ARTIFACTORY_USER')]) {
        // create base build info
        rtBuildInfo (
          buildName: "${env.BUILD_NAME}",
          buildNumber: "${env.BUILD_NUMBER}",
          includeEnvPatterns: ['BRANCH_NAME'],
          maxDays: 90,
          deleteBuildArtifacts: true,
          asyncBuildRetention: true
        )
        rtPublishBuildInfo (
          buildName: "${env.BUILD_NAME}",
          buildNumber: "${env.BUILD_NUMBER}",
          serverId: 'taas-artifactory-upload'
        )
        // put build info on module/artifacts then overwrite and publish artifactory build
        sh './scripts/publish_buildinfo.sh'
      }
    }
  }
}

String getNewVersion(isDevRelease, version) {
  wipVersion = ''
  if (isDevRelease) {
    // Add uniqueness and build metadata to dev build versions
    wipVersion = "${version.trim()}-dev${currentBuild.startTimeInMillis}+${commitHash}.${currentBuild.number}"
  } else {
    wipVersion = "${version.trim()}"
  }
  // Customize with lang specific requirements
  return customizeVersion(wipVersion)
}

// Language specific implementations of the methods:
// applyCustomizations()
// runTests()
// publishStaging()
// publishPublic()
// publishDocs()
// + other customizations
void applyCustomizations() {
  libName = 'python'
  customizeVersion = { semverFormatVersion ->
    // Use a python format version
    semverFormatVersion.replace('-a','a').replace('-b','b').replace('-','.')
  }
  customizePublishingInfo = {
    // Set the publishing names and types
    artifactUrl = "${STAGE_ROOT}storage/cloudant-sdks-pypi-local/ibmcloudant/${env.NEW_SDK_VERSION}"
    moduleId = "ibmcloudant-${env.NEW_SDK_VERSION}"
  }
}

void runTests() {
  sh """
    pip3 install --upgrade pip tox
    python3 -m tox -e py36
  """
}

void publishStaging() {
  withCredentials([usernamePassword(credentialsId: 'artifactory', passwordVariable: 'TWINE_PASSWORD', usernameVariable: 'TWINE_USERNAME')]) {
    withEnv(["TWINE_REPOSITORY_URL=${env.STAGE_ROOT}pypi/cloudant-sdks-pypi-local"]) {
      publishTwine()
    }
  }
}

void publishPublic() {
  withCredentials([usernamePassword(credentialsId: 'pypi', passwordVariable: 'TWINE_PASSWORD', usernameVariable: 'TWINE_USERNAME')]) {
    publishTwine()
  }
}

void publishTwine() {
  dir('dist') {
    deleteDir()
  }
  sh """
    python3 --version
    python3 -m pip install --upgrade pip setuptools twine
    python3 setup.py sdist
    python3 -m twine upload dist/*
  """
}

void publishDocs() {
  sh './scripts/pydoc/publish-doc.sh'
}

