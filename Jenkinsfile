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
  }
  stages {
    stage('Checkout') {
      steps {
        script {
          defaultInit()
          applyCustomizations()
          checkoutResult = checkout scm
          commitHash = "${checkoutResult.GIT_COMMIT[0..6]}"
          sh """
            git config user.email '71659186+cloudant-sdks-automation@users.noreply.github.com'
            git config user.name 'cloudant-sdks-automation'
            git config credential.username '${env.GH_CREDS_USR}'
            git config credential.helper '!f() { echo password=\$GH_CREDS_PSW; echo; }; f'
          """
        }
      }
    }
    stage('QA') {
      steps {
        withEnv(['DOCKER_HOST=',
          'SERVER_AUTH_TYPE=basic',
          'SERVER_URL=http://127.0.0.1:5984',
          'SERVER_USERNAME=admin',
          'SERVER_PASSWORD=password',
          'WIREMOCK_URL=http://127.0.0.1:8080',
          'WIREMOCK_PORT=8080'
        ]) {
          sh './scripts/setup_couch.sh'
          sh './scripts/setup_wiremock.sh'
          runTests()
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
      }
    }
  }
}

def libName
def commitHash
def bumpVersion
def customizeVersion

void defaultInit() {
  // Default to using bump2version
  bumpVersion = { isDevRelease ->
    newVersion = getNextVersion(isDevRelease)
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
// + other customizations
void applyCustomizations() {
  libName = 'python'
  customizeVersion = { semverFormatVersion ->
    // Use a python format version
    semverFormatVersion.replace('-a','a').replace('-b','b').replace('-','.')
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

