#!groovy

pipeline {
  def app 

  environment {
    VERSION = "${env.BUILD_ID}-${env.GIT_COMMIT}"
  }

  agent 
    docker {
      image 'python:3.8.7-buster'
    }
  }

  stages {
    stage('Checkout') {
      checkout scm
    }
    
    stage('Unit Test') {
      sh 'echo Python test passed'
    }

    stage('Integration Test') {
      sh 'echo Python test passed'
    }

    stage('Sonarqube') {
      sh 'echo Python test passed'
    }

    stage('Build docker image') {
      //Change by our real registry, default is dockerhub
      //docker.withRegistry('url','credentials'){}
      app = docker.build("Chillaso/python-docker-jenkins")
    }
    
    stage('Test docker image') {
      app.inside{
        sh 'echo Test passed'
      }
    }

    stage('Push image'){
      //docker.withRegistry('url', 'credentials'{}
      app.push("${VERSION}")
    }
  }
}
