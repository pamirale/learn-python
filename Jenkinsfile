pipeline {
  agent any
  stages {
    stage('Install state tool') {
      steps {
        sh '''curl -q https://platform.activestate.com/dl/cli/install.sh -o install.sh
chmod +x install.sh
./install.sh -n -t $WORKSPACE || true'''
      }
    }

    stage('Update Project') {
      steps {
        sh '$WORKSPACE/state.exe pull'
      }
    }

  }
  environment {
    ACTIVESTATE_API_KEY = 'credentials(\'api-key\')'
  }
}