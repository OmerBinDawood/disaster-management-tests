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
            def email = ""

            try {
                email = sh(script: "git log -1 --pretty=%ae", returnStdout: true).trim()
            } catch (Exception e) {
                email = "default-email@example.com"
            }

            echo "Sending results to: ${email}"

            emailext (
                to: email,
                subject: "Jenkins CI Results - Disaster Tests (${currentBuild.result})",
                body: """
    Hello,

    Build Status: ${currentBuild.result}

    Project: Disaster Management Tests
    Build URL: ${env.BUILD_URL}

    Check logs for full details.

    Regards,
    Jenkins CI System
    """,
                    attachLog: true
                )
            }

            echo "Docker tests completed"
        }
    }
}