pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Your Docker build command
                    sh 'docker build -t mohansai7777/hey-python-flask:0.0.1.RELEASE .'
                }
            }
        }

        stage('Stop and Remove Old Containers') {
            steps {
                script {
                    // Stop and remove containers with the specified name or ID
                    sh 'docker ps -q --filter "ancestor=prasanthk8/hey-python-flask:0.0.1.RELEASE" | xargs -r docker stop'
                    sh 'docker ps -a -q --filter "ancestor=prasanthk8/hey-python-flask:0.0.1.RELEASE" | xargs -r docker rm'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Your Docker run command with port 3001
                    sh 'docker container run -d -p 3001:3000 prasanthk8/hey-python-flask:0.0.1.RELEASE'
                }
            }
        }
    }
}
