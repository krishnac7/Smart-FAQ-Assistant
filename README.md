# Smart FAQ Assistant


## Overview
In this tutorial, we will be creating a smart assistant that can answer user questions basing on a pdf file that is provided as input and can also can query a machine learning model for prediction. 

## Pre-reqisites:
1) IBM Cloud Account
2) Watson Studio
3) Watson Machine Learning service
4) Watson Discovery service
5) IBM Cloud Functions
6) Watson Assistant


## Creating IBM Cloud Account:
* Create your account at [cloud.ibm.com/registration](https://cloud.ibm.com/registration)
* You will get a confirmation email to the provided email address

Once we have created our IBM Cloud account and logged into it, we will be creating the next set of services as 4 discreate steps.


### [Step 1](https://github.com/krishnac7/Smart-FAQ-Assistant/tree/master/Step1-Wml)
Create a Machine learning model on Watson Studio using AutoAI and deploy it to Watson Machine Learning service.

### [Step 2](https://github.com/krishnac7/Smart-FAQ-Assistant/tree/master/Step2-Discovery)
Create a collection on Watson Discovery, load documents and use smart document understanding to better process the documents.

### [Step 3](https://github.com/krishnac7/Smart-FAQ-Assistant/tree/master/Step3-Functions)
Create a cloud function that can talk to discovery service or watson machine learning service as per requirement.

### [Step 4](https://github.com/krishnac7/Smart-FAQ-Assistant/tree/master/Step4-Assistant)
In this step we create a watson assistance instance and train it to respond to basic user queries.Then we integrate the above configured services into one assistant using Cloud functions.
