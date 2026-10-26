pipeline {
    agent any

    triggers {
        pollSCM('H/1 * * * *')
    }

    stages {
        stage('Build') {
            steps {
                bat '"C:\\Users\\SRINITHIJA\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t ci-cd-demo .'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                bat '"C:\\Users\\SRINITHIJA\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" rm -f ci-cd-container || exit /b 0'
                bat '"C:\\Users\\SRINITHIJA\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run -d --name ci-cd-container -p 5000:5000 ci-cd-demo'
            }
        }
    }
}