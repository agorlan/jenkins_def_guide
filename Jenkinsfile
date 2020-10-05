pipeline {
    agent { docker { image 'python:3.7' } }

    stages {
        stage('1-Build') {
            steps {
                echo "Start of Stage Build"
                sh "python -m pip install -r requirements.txt"
                echo "End of Stage Build"
            }
        }
        stage('2-Test') {
            steps {
                echo "Start of Stage Test"
                sh "python -m pytest test_runner.py"
                echo "End of Stage Build"
            }
        }
        stage('3-Deploy') {
            steps {
                echo "Start of Stage Deploy"
                echo "Deploying......."
                echo "End of Stage Build"
            }
        }
   }
}