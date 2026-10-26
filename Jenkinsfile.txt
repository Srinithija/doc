pipeline {
    agent any

    triggers {
        pollSCM('H/1 * * * *')
    }

    stages {
        stage('Build') {
            steps {
                bat 'docker build -t ci-cd-demo .'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker rm -f ci-cd-container || exit /b 0'
                bat 'docker run -d --name ci-cd-container -p 5000:5000 ci-cd-demo'
            }
        }
    }
}