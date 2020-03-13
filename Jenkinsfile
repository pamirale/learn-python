pipeline {
  agent any
  stages {
    stage('Install state tool') {
      steps {
        sh '''curl -q https://platform.activestate.com/dl/cli/install.sh -o install.sh
chmod +x install.sh
./install.sh -n -t $WORKSPACE || true'''
        tm '$ACTIVESTATE_API_KEY'
        sh '$WORKSPACE/state auth --token $ACTIVESTATE_API_KEY'
      }
    }

    stage('Update Project') {
      steps {
        sh '$WORKSPACE/state pull'
      }
    }

    stage('Lint') {
      steps {
        sh '$WORKSPACE/state run lints'
      }
    }

    stage('Test') {
      steps {
        sh '$WORKSPACE/state run tests'
      }
    }

  }
  environment {
    ACTIVESTATE_API_KEY = 'credentials("api-key")'
    SHELL = '/bin/bash'
  }
}