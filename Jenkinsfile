pipeline {
    agent any

    environment {
        IMAGE = 'muying11/counter-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & unit tests') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -q -r app/requirements.txt pytest
                    cd app && python -m pytest -v --junitxml=report.xml
                '''
            }
            post {
                always {
                    junit 'app/report.xml'
                }
            }
        }

        stage('Build Docker image') {
            steps {
                sh "docker build -t ${IMAGE}:${BUILD_NUMBER} -t ${IMAGE}:latest app"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub',
                                                  usernameVariable: 'HUB_USER',
                                                  passwordVariable: 'HUB_TOKEN')]) {
                    sh '''
                        echo "$HUB_TOKEN" | docker login -u "$HUB_USER" --password-stdin
                        docker push ${IMAGE}:${BUILD_NUMBER}
                        docker push ${IMAGE}:latest
                    '''
                }
            }
        }
    }

    post {
        always {
            sh 'docker logout || true'
        }
    }
}
