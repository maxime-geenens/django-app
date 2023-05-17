#!groovy
pipeline {
    agent any
    environment {
        VERSION = '0.1.0'
        APP_NAME = 'Django-app'
    }
    stages {
        stage('Init') {
            steps {
                echo "This is build number $BUILD_NUMBER of $APP_NAME"

                sh '''
                    git version
                    docker version
                '''
            }
        }
        stage('Build') {
            environment {
                LOG_LEVEL = 'INFO'
            }
            steps {
                echo "Building version : ${VERSION}"
                echo "Log level : ${LOG_LEVEL}..."
                sh 'docker compose up -d'
            }
        }
        stage('Unit Test') {
            agent {
                docker { image 'python:3.10' }
            }
            steps {
                echo "Testing version ${VERSION}..."
                echo 'testing...'
            }
        }
        stage('Deploy') {
            input {
                message 'Deploy?'
                ok 'Do it!'
                parameters {
                    string(name: 'TARGET_ENVIRONMENT', defaultValue: 'DEV',\
                    description: 'Target deployment environment')
                }
            }
            steps {
                echo "Deploying release ${VERSION} to environment ${TARGET_ENVIRONMENT}"
            }
        }
    }
    post {
        always {
            echo 'Prints whether deploy happened or not, success or failure'
        }
    }
}
