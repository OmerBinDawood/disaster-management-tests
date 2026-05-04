pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest -v'
            }
        }
    }

    post {
        always {
            echo "Tests completed"
        }
    }
}