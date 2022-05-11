#!groovy

pipeline {
  agent {
    label 'sdks-executor'
  }
  options {
    skipDefaultCheckout()
  }
  parameters {
    validatingString( name: 'TARGET_VERSION',
                      defaultValue: 'NONE',
                      description: 'Tag to create after successful QA',
                      failedValidationMessage: 'Tag name must be NONE or a semantic version release or pre-release (i.e. no build metadata)',
                      regex: /NONE|${SVRE_PRE_RELEASE}/)
  }
  environment {
    GH_CREDS = credentials('gh-sdks-automation')
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
      environment {
        STAGE_ROOT = 'https://na.artifactory.swg-devops.com/artifactory/api/'
      }
      steps {
        bumpVersion(true)
        publishStaging()
        publishArtifactoryBuildInfo()
      }
      // This post stage resets the temporary version bump used to publish to staging
      post {
        always {
          sh 'git reset --hard'
        }
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

            // For standard builds attempt to run on a matching env.BRANCH_NAME branch first and if it doesn't exist
            // then fallback to TARGET_GAUGE_RELEASE_BRANCH_NAME if set or env.TARGET_GAUGE_DEFAULT_BRANCH_NAME.
            gaugeBranchName = env.BRANCH_NAME
            fallbackBranchName = env.TARGET_GAUGE_RELEASE_BRANCH_NAME ?: env.TARGET_GAUGE_DEFAULT_BRANCH_NAME

            // For release builds (tag builds or the primary branch) do the reverse and attempt to run on the
            // TARGET_GAUGE_RELEASE_BRANCH_NAME falling back to env.BRANCH_NAME or env.TAG_NAME if there is no match.
            if (env.TAG_NAME || env.BRANCH_IS_PRIMARY){
              gaugeBranchName = env.TARGET_GAUGE_RELEASE_BRANCH_NAME
              fallbackBranchName = env.TAG_NAME ?: env.BRANCH_NAME
            }
          try {
            buildResults = build job: "/${env.SDKS_GAUGE_PIPELINE_PROJECT}/${gaugeBranchName}", parameters: [
                string(name: 'SDK_RUN_LANG', value: "$libName"),
                string(name: "SDK_VERSION_${libName.toUpperCase()}", value: "$prefixedSdkVersion")]
          } catch (hudson.AbortException ae) {
            // only run build in sdks-gauge master branch if BRANCH_NAME doesn't exist
            if (ae.getMessage().contains("No item named /${env.SDKS_GAUGE_PIPELINE_PROJECT}/${gaugeBranchName} found")) {
              echo "No matching branch named '${gaugeBranchName}' in sdks-gauge, building ${fallbackBranchName} branch"
              build job: "/${env.SDKS_GAUGE_PIPELINE_PROJECT}/${fallbackBranchName}", parameters: [
                  string(name: 'SDK_RUN_LANG', value: "$libName"),
                  string(name: "SDK_VERSION_${libName.toUpperCase()}", value: "$prefixedSdkVersion")]
            } else {
              throw ae
            }
          }
        }
      }
    }
    stage('Update version and tag') {
      when {
        beforeAgent true
        allOf {
          // We only bump the version and create a tag when building master with a TARGET_VERSION
          branch 'master'
          not {
            equals expected: 'NONE', actual: "${params.TARGET_VERSION}"
          }
        }
      }
      steps {
        // bump the version
        bumpVersion(false)
        // Push the version bump and release tag
        sh 'git push --tags origin HEAD:master'
      }
    }
    stage('Publish[repository]') {
      // We publish only when building a tag that meets our semantic version release or pre-release tag format
      when {
        beforeAgent true
        allOf {
          buildingTag()
          anyOf {
            tag pattern: /${env.SVRE_PRE_RELEASE_TAG}/, comparator: "REGEXP"
          }
        }
      }
      steps {
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
def getNewVersion
// Default no-op, may be overridden
def customizePublishingInfo = {}
def publishArtifactoryBuildInfo
def artifactUrl = ''
def moduleId = ''
def buildName = ''
def buildType = ''

void defaultInit() {
  // Default to using bump2version
  bumpVersion = { isDevRelease ->
    newVersion = getNewVersion(isDevRelease, true)
    // Set an env var with the new version
    env.NEW_SDK_VERSION = newVersion
    doVersionBump(isDevRelease, newVersion)
  }

  doVersionBump = { isDevRelease, newVersion, allowDirty ->
    sh "bump2version --new-version ${newVersion} ${allowDirty ? '--allow-dirty': ''} ${isDevRelease ? '--no-commit' : '--tag --tag-message "Release {new_version}"'} patch"
  }

  getNewVersion = { isDevRelease, includeBuildMeta ->
    // Get a staging or target version and customize with lang specific requirements
    return customizeVersion(isDevRelease ? getDevVersion(includeBuildMeta) : getTargetVersion())
  }

  getTargetVersion = {
    version = ''
    if ('NONE' != params.TARGET_VERSION) {
      version = params.TARGET_VERSION
    } else {
      // If a target version is not provided default to a patch bump
      version = sh returnStdout: true, script: 'bump2version --list --dry-run patch | grep new_version=.* | cut -f2 -d='
    }
    return version.trim()
  }

  getDevVersion = { includeBuildMeta ->
    devVersion = getTargetVersion()
    if (devVersion ==~ /${env.SVRE_RELEASE}/) {
      // For a release (e.g. 1.0.0) make a -dev pre-release (e.g. 1.0.0-devTS)
      devVersion += "-dev${currentBuild.startTimeInMillis}"
    } else if (devVersion ==~ /${env.SVRE_PRE_RELEASE}/) {
      // For a pre-release (e.g. 1.0.0-b7), add .dev identifier (e.g. 1.0.0-b7.devTS)
      devVersion += ".dev${currentBuild.startTimeInMillis}"
    }
    if (includeBuildMeta) {
      // Add uniqueness and build metadata when requested to dev build versions
      devVersion += "+${commitHash}.${currentBuild.number}"
    }
    return devVersion
  }

  // Default no-op implementation to use semverFormatVersion
  customizeVersion = { semverFormatVersion ->
    semverFormatVersion
  }

  publishArtifactoryBuildInfo = {
    // create custom build name e.g. cloudant-sdks/cloudant-node-sdk/generated-branch
    buildName = "${env.JOB_NAME}"
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
    semverFormatVersion.replace('-a','a').replace('-b','b').replace('-rc', 'rc').replace('-','.')
  }
  customizePublishingInfo = {
    // Set the publishing names and types
    artifactUrl = "${STAGE_ROOT}storage/cloudant-sdks-pypi-local/ibmcloudant/${env.NEW_SDK_VERSION}"
    moduleId = "ibmcloudant-${env.NEW_SDK_VERSION}"
  }
}

void runTests() {
  sh """
    . /home/jenkins/pythonvenv/bin/activate
    python3 -m tox -e py310
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
    . /home/jenkins/pythonvenv/bin/activate
    python3 --version
    python3 setup.py sdist
    python3 -m twine upload dist/*
  """
}

void publishDocs() {
  sh './scripts/pydoc/publish-doc.sh'
}

