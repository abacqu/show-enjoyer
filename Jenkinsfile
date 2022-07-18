pipeline {
    agent { docker { image 'python:3' }}

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                sh 'python tests.py'
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}