pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

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
            script {
                def email = "default-recipient@example.com"

                echo "Build completed successfully"

                emailext (
                    to: email,
                    subject: "Jenkins CI Results - Disaster Tests - Build #${env.BUILD_NUMBER}",
                    body: """
Hello,

Your pipeline has completed.

Project: Disaster Management Tests
Build Status: ${currentBuild.currentResult}

Check logs: ${env.BUILD_URL}

Regards,
Jenkins CI
""",
                    attachLog: true
                )
            }
        }
    }
}