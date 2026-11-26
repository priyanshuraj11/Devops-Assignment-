pipeline {
    agent any

    stages {
	stage('Secure Secret Management') {
    steps {
        withCredentials([
            string(credentialsId: 'lab4-api-key', variable: 'API_KEY')
        ]) {
            sh '''
                set +x
                test -n "$API_KEY"
                echo "API credential loaded securely"
                echo "Secret validation successful"
            '''
        }
    }
}
	
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .jenkins-venv
                    .jenkins-venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                sh '.jenkins-venv/bin/python -m pytest -v tests/test_unit.py'
            }
        }

        stage('Integration Tests') {
            steps {
                sh '.jenkins-venv/bin/python -m pytest -v tests/test_integration.py'
            }
        }

        stage('Deployment Gate') {
            steps {
                echo 'All tests passed. Deployment approved.'
            }
        }
    }

    post {
        success {
            echo 'Lab 4 CI/CD pipeline SUCCESS'
        }
        failure {
            echo 'Tests failed. Deployment BLOCKED.'
        }
    }
}
