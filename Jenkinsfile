pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/OmerBinDawood/disaster-management-tests.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                    python -m pytest -v
                '''
            }
        }

    }

    post {
        always {
            echo "Tests completed"
        }
    }
}