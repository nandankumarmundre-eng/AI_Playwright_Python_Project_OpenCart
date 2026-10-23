pipeline {
    agent any

    options {
        timestamps()
    }

    parameters {
        choice(name: 'browser', choices: ['chromium', 'firefox', 'webkit'], description: 'Browser engine')
        choice(name: 'testgroups', choices: ['sanity', 'regression', 'sanity or regression', 'sanity and regression', 'smoke', 'e2e'], description: 'Pytest marker expression for the main test run')
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
                bat ".venv\\Scripts\\python -m playwright install ${params.browser}"
            }
        }

        stage('Clean Previous Reports') {
            steps {
                bat 'if exist reports\\allure-results rmdir /s /q reports\\allure-results'
            }
        }

        stage('Register Test Account') {
            steps {
                bat ".venv\\Scripts\\python -m pytest tests/regression/test_register.py --headless --browser ${params.browser}"
            }
        }

        stage('Run Tests') {
            steps {
                bat ".venv\\Scripts\\python -m pytest --headless --browser ${params.browser} -m \"${params.testgroups}\" --ignore=tests/regression/test_register.py"
            }
        }
    }

    post {
        always {
            script {
                if (fileExists('reports/allure-results')) {
                    allure commandline: 'allurereport', includeProperties: false, results: [[path: 'reports/allure-results']]
                } else {
                    echo 'Allure results were not created; skipping report generation.'
                }
            }
            archiveArtifacts artifacts: 'reports/html/**, reports/allure-results/**, reports/evidence/**, reports/logs/**', allowEmptyArchive: true
        }
    }
}
