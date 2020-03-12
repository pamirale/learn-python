pipeline {
  agent any
  stages {
    stage('Install state tool') {
      steps {
        sh '''sh\'\'\'
curl -q https://platform.activestate.com/dl/cli/install.sh -o install.sh
chmod +x install.sh
./install.sh -n -t $WORKSPACE || true
\'\'\''''
      }
    }

    stage('Update Project') {
      steps {
        sh 'sh \'state pull\''
      }
    }

  }
  environment {
    SHELL = 'bin/bash'
    PATH = '${env.WORKSPACE}:${env.PATH}'
    ACTIVESTATE_API_KEY = 'credentials(\'api-key\')'
  }
}