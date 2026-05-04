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
                // Get email of last commit author (dynamic sender)
                def email = sh(script: "git log -1 --pretty=%ae", returnStdout: true).trim()

                echo "Sending results to: ${email}"

                emailext (
                    to: email,
                    subject: "Jenkins CI Results - Disaster Tests",
                    body: """
Hello,

Your Selenium test pipeline has completed.

Project: Disaster Management Tests
Status: Completed (check Jenkins console for pass/fail details)

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