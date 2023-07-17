# Overview

Udacity Project #2 Building a CI/CD Pipeline

Steps:

1. Set up Azure Cloud Shell - Creating ssh keys, copying repository into Azure and running your Makefile in a virtual environment
2. Configure GitHub Actions - Spin up azure web app and configure yaml pipeline in GitHub actions
3. Enable Continuous Delivery via Azure Devops - upload flask starter code to repo, create an azure pipeline and ensure prediction works

## Project Plan

* A link to a [Trello](https://trello.com/b/mgbM0QV5/udacity-project-2) board for the project
* A link to a [spreadsheet](https://docs.google.com/spreadsheets/d/1V2cy8WjRHUGpVEoUbSiUSh5qYBpkyyxbSuYpjcarDEg/edit#gid=1348135932) that includes the original and final project plan.

## Instructions

### Architectural Diagrams

![CI Diagram](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/ci-diagram.png)
With this setup, code is able to be tested automatically with Github Actions.

![Azure Cloud Shell Diagram](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/azure-cloud-shell.png)
Link GitHub repository with the cloned repository in Azure.

![CD Diagram](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/cd-diagram.png)
When a change event is pushed to GitHub, it will kick off Azure Pipelines which will deploy the changed to your Azure Web App.

### CI Setup

1. Log into Azure with credentials.
2. Open a Bash terminal and click on Advanced settings to setup a storage account and file share.
3. Within the Bash terminal create ssh keys. 
   1. `ssh-keygen -t rsa`
   2. `cat /home/udacity/.ssh/.id_rsa.pub` (The folder name will output from the step above.)
   3. Copy `ssh key`
4. Go to your GitHub Account
   1. Click on your profile picture
   2. Click Settings
   3. Click SSH and GPG Keys
   4. Click New SSH Key and paste value from above.
5. Within your Azure Bash terminal, clone your repo from GitHub via ssh.
   1. `git clone git@github.com:lmnicholls/flask-ml-service.git`
   2. ![Repo in Azure](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/ProjectInAzureCloudShell.png)
6. Create a virtual environment in your Azure Bash terminal.
   1. `python3 -m venv ~/.myrepo`
   2. Run `source ~/.myrepo/bin/activate` to start your virtual environment
   3. Cd into your repo and install dependencies by running `make all`
   4. ![Passing make all](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/MakeAllPassingTests1.png)
   5. ![Passing make all](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/MakeAllPassingTests2.png)
   6. ![Passing make all](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/MakeAllPassingTests3.png)
   7. ![Passing make all](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/MakeAllPassingTests4.png)

### Configure GitHub Actions

1. In your Github repository, enable GitHub Actions.
![Github Actions](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/NichollsP2_Screenshot_GitHubActions.png)
![Github Actions](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/GitHubActionsPassingTests.png)
![Github Actions](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/GitHubActionsPassingTests2.png)

### Deploy Azure Web App

1. Within your virtual environment, spin up an Azure Web App by running the following command:
   1. `az webapp up --name nichollsflaskapp --resource-group Azuredevops --runtime "PYTHON|3.7"`
   ![Deployed Azure Web App](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/AzureWebApp.png)
2. Navigate to the web app and in the left hand menu select Deployment Center to link your web app to your GitHub Repo
   ![Azure Web App Linked to GitHub Repo](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/AzureWebAppDeploymentCenter.png)
3. Update your `make_predict_azure_app.sh` file to include your web app url.
4. Confirm a succesful prediction from the flask app:
   ![Prediction](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/BashPrediction.png)
5. Check the logs from your web app using the `az webapp log tail` command.
   ![Azure Logs](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/AzureLogs.png)

## CD Setup

1. Login to Azure Devops and create a new project.
2. Create a new pipeline.
   1. Select GitHub and your repo.
   2. Select existing yaml file and copy the relative path to azure-pipelines.yml.
3. In Azure Devops, create a new service connection.
   1. Within the project, select Project Settings.
   2. Select Service Connections
   3. New Service Connection
   ![ServiceConnection](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/AzureServiceConnection.png)
   4. Update the service connection name in your azure-pipelines.yaml file.
4. If you are running this through a Udacity Cloud Lab Environment, you will need to set up an agent.
   1. Create a Personal Access Token (PAT) in Azure Devops.
   ![Azure PAT](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/AzurePAT.png)
   2. Be sure to copy the Personal Access Token (PAT) for later use when you are creating your agent.
5. If you have a windows machine, you will need to set up a virtual machine running ubuntu.
   1. In your Azure Resource Group, create an Ubuntu Virtual Machine.
   ![Azure VM](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/AzureVM.png)
   2. Click Connect at the top and open a Bash Shell.
   3. Be sure to install all necessary applications on your VM using `sudo apt install update`
      1. Install git, python, make, unzip and zip.
   4. Follow the steps within the SSH tab to connect to your VM.
   ![Connect to VM](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/AzureConnectToVM.png)

6. Set up an Agent Pool.
   1. In Azure Devops Project, select Project Settings.
   2. Select Agent Pools.
   3. Click on Default Agent Pool.
   4. Select New Agent.
   5. Click Linux and follow the steps to get it up and running. This will enable you to run your pipeline.
   ![Agent Pool](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/AzureAgentPool.png)
7. Run your pipeline manually or by pushing a change to your repo.
   ![Pipeline](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/AzurePipelines.png)
   * Every time you make a change to your repository on the main branch, it will start the pipeline to enable CD.

### Load Test App

1. In a Bash shell within Azure, cd into your repo and run your python app using `Python app.py`
2. Within your virtual environment, install locust using `pip3 install locust`.
   1. Run the locust file from within your repo using `locust -f locustfile.py --web-port 8079`.
   2. Within the Bash shell, click on the Web Preview button and configure to port 8079. Configure settings and click Start swarming.
   ![Locust](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/Locust.png)
   3. In the Python app.py Bash shell you will see the hits to your web app.
3. Results will look something like this:
![Locust Results](https://raw.githubusercontent.com/lmnicholls/flask-ml-service/main/Images/../../../../../../Images/LocustfileTest.png)

## Enhancements

Enhancements could include an improved azure web app UI and additional end points to test.

## Demo

Link to [Demo](https://share.vidyard.com/watch/Ph3x3BYjRV8b2HnA4Gjwap?)
