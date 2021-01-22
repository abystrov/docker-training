pipeline {
    agent any

    stages {
        stage('Build images'){
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Deploy application'){
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}