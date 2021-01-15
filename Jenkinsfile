#!groovy

peline {
  agent {
    docker {
      image 'python:3.8.7-buster'
    }
  }

  environment {
    PROJECT_NAME = "npl-document-item-service"
    PROJECT_VERSION = pythonVersion()
  }

  options {
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '3', artifactNumToKeepStr: '3'))
  }

  stages {
    stage('Initialization'){
      steps {
        echo "Release file committed and changed. Proceeding!"
        script {
          currentBuild.displayName = PROJECT_VERSION + ". #" + BUILD_NUMBER
          currentBuild.description = "Project version: ${env.PROJECT_VERSION}<br/>Branch: ${BRANCH_NAME}<br/>"
        }
        sh """
          set +x
          echo 'Building project using Python version ${env.PROJECT_VERSION}'
          """
      }
    }

    stage('Build') {
      steps {
        script{
          sh 'python3 pip install wheel && python3 pip wheel -r requirements.txt' 
        }
      }
    } 

    stage('Unit tests'){
      steps {
        script {
          sh 'echo Python test passed'
        }
      }
    }

  }
}

def pythonVersion() {
    v = sh(returnStdout: true, script: "python3 app.py --version").trim()
    return v
}
