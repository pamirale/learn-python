pipeline {
  agent any
  stages {
    stage('Install State Tool') {
      steps {
        sh '''curl -q https://platform.activestate.com/dl/cli/install.sh -o install.sh
chmod +x install.sh
./install.sh -n -t $WORKSPACE || true'''
      }
    }

    stage('Authenticate with Platform') {
      steps {
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
    SHELL = '/bin/bash'
    ACTIVESTATE_API_KEY = credentials('api-key')
  }
}