pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t disaster-tests .'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                sh 'docker run --rm disaster-tests'
            }
        }
    }

    post {
        always {
            echo "Docker tests completed"
        }
    }
}