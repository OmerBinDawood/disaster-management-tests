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

                // BEST RELIABLE METHOD IN JENKINS SCM JOBS
                def changeSet = currentBuild.changeSets

                def email = "unknown"

                if (changeSet != null && changeSet.size() > 0) {
                    def entries = changeSet[0].items
                    if (entries != null && entries.size() > 0) {
                        email = entries[0].authorEmail
                    }
                }

                echo "Sending email to commit author: ${email}"

                emailext (
                    to: email,
                    subject: "Jenkins CI Results - $BUILD_STATUS",
                    body: """
Hello,

Your pushed commit triggered the Jenkins pipeline.

Project: Disaster Management Tests
Build Number: $BUILD_NUMBER
Status: $BUILD_STATUS

Check details here:
$BUILD_URL

Regards,
Jenkins CI
""",
                    attachLog: true
                )
            }

            echo "Pipeline completed"
        }
    }
}