pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'py -m venv .venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '.venv\\Scripts\\python -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python -m pip install -r requirements.txt'
                bat '.venv\\Scripts\\python -m playwright install chromium'
            }
        }

        stage('Clean Previous Reports') {
            steps {
                bat 'if exist reports\\allure-results rmdir /s /q reports\\allure-results'
            }
        }

        stage('Register Test Account') {
            steps {
                bat '.venv\\Scripts\\python -m pytest tests/regression/test_register.py --headless'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\python -m pytest --headless --ignore=tests/regression/test_register.py'
            }
        }
    }

    post {
        always {
            script {
                if (fileExists('reports/allure-results')) {
                    allure includeProperties: false, results: [[path: 'reports/allure-results']]
                } else {
                    echo 'Allure results were not created; skipping report generation.'
                }
            }
            archiveArtifacts artifacts: 'reports/html/**, reports/allure-results/**, reports/evidence/**, reports/logs/**', allowEmptyArchive: true
        }
    }
}
