pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'git@github.com:StakeTake/ci-cd-docker-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 my-app'
            }
        }
    }
}
