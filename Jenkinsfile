pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Sap-04-Learner/fapi-jenkins.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("fapi-jenkins:latest")
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    docker.image("fapi-jenkins:latest").run("-p 5000:5000")
                }
            }
        }
    }
}