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

            // safer GitHub commit email extraction
            def email = sh(
                script: "git log -1 --pretty=format:'%ae'",
                returnStdout: true
            ).trim()

            echo "Sending email to: ${email}"

            emailext (
                to: email,
                subject: "Jenkins CI Results - Disaster Tests #${env.BUILD_NUMBER}",
                body: """
    Hello,

    Pipeline completed.

    Project: Disaster Management Tests
    Build Status: ${currentBuild.currentResult}

    Check details: ${env.BUILD_URL}

    Regards,
    CI Pipeline
    """,
                    attachLog: true
                )
            }

            echo "Pipeline completed"
        }
    }
}