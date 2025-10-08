pipeline{
  agent any
  stages{
      stage('Build & Report'){
           steps{
                checkout scm
                sh 'echo "Build Stage executed Successfully..!"'
           }
      }
  }
  post{
      success{
          echo  'Build Completed and marked as successful'
      }
      failure{
          echo  'Build Failed'
      }
  }
  
}
