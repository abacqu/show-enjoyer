pipeline {
    agent { docker { image 'python:3.10' }}

    stages {
        stage('Build') {
            steps {
                sh '/usr/local/bin/python -m pip --upgrade pip'
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