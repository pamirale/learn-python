pipeline {
  agent any
  stages {
    stage('Install state tool') {
      steps {
        sh 'env'
        sh '''curl -q https://platform.activestate.com/dl/cli/install.sh -o install.sh
chmod +x install.sh
./install.sh -n -t $WORKSPACE || true'''
      }
    }

    stage('Update Project') {
      steps {
        sh 'state pull'
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

    stage('Cleanup') {
      steps {
        sh '$WORKSPACE/state clean -f'
      }
    }

  }
  environment {
    ACTIVESTATE_API_KEY = 'credentials(\'api-key\')'
    SHELL = '/bin/bash'
    PATH = '${env.WORKSPACE}:${env.PATH}'
  }
}