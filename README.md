# Overview

Udacity Project #2 Building a CI/CD Pipeline

Steps:

1. Set up Azure Cloud Shell - Creating ssh keys, copying repository into Azure and running your Makefile in a virtual environment
2. Configure GitHub Actions - Spin up azure web app and configure yaml pipeline in GitHub actions
3. Enable Continuous Delivery via Azure Devops - upload flask starter code to repo, create an azure pipeline and ensure prediction works

## Project Plan

<TODO: Project Plan

* A link to a [Trello](https://trello.com/b/mgbM0QV5/udacity-project-2) board for the project
* A link to a [spreadsheet](https://docs.google.com/spreadsheets/d/1V2cy8WjRHUGpVEoUbSiUSh5qYBpkyyxbSuYpjcarDEg/edit#gid=1348135932) that includes the original and final project plan.

## Instructions

* Architectural Diagrams

![CI Diagram](Images\ci-diagram.png)
![Azure Cloud Shell Diagram](Images\azure-cloud-shell.png)
![CD Diagram](Images\cd-diagram.png)

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


