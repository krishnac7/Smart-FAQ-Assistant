## AutoAI and WML

*Quick links :*
[Home](/README.md) - [**Step 1**](https://github.com/krishnac7/Smart-FAQ-Assistant/tree/master/Step1-Wml) - [Step 2](https://github.com/krishnac7/Smart-FAQ-Assistant/tree/master/Step2-Discovery) - [Step 3](https://github.com/krishnac7/Smart-FAQ-Assistant/tree/master/Step3-Functions) - [Step 4](https://github.com/krishnac7/Smart-FAQ-Assistant/tree/master/Step4-Assistant)
***

### Overview

In this step, you will create a simple machine learning model using AutoAI and save the model using WML(Watson Machine Learning)

### Setup an instance of Watson Studio

1.1 ) Click on Catalog

![](../Media/img/dashboard.png)

you can look at a whole list of services and offerings from ibm cloud

1.2 ) Select services tab and Filter by AI

![](../Media/img/services.png)

1.3 ) Click on Watson Studio.

 ![](../Media/img/watsonStudio.png)
 
 
1.4 ) You can leave the defaults and click on Create.Do take a minute to look at features you are getting with lite plan of the service

![](../Media/img/serviceCreation.png)


1.5 ) Once you click on Create, the service is provisioned. Click on Get Started.It opens a new tab with your watson studio dashboard

![](../Media/img/img-02.png)

1.6 ) Once you are in  watson studio dashboard, the first thing we will do is create a project  to work in.click on create a project
![](../Media/img/createProject.png)

1.7 ) Select Create an empty project.

![](../Media/img/img-03.png)

1.8 ) Give a Unique name to your project.and To add storage to your project, Click on Add.if you see the storage option prefilled, you can skip the next step

![](../Media/img/project.png)

1.9 ) It will open a new tab where you can create a new instance of object storage. you can select the lite plan and click on create
![](../Media/img/addStorage.png)

1.10 ) you can leave the defaults and click on confirm.the service name generated for you can be different

![](../Media/img/confirm.png)


1.11 ) Once the Object storage is created, you can close the tab and press refresh to see your attached storage

![](../Media/img/attachStorage.gif)

### Run and Auto-AI Experiment

1.12 ) Within project, click on 'Add to project' and choose AutoAI Experiment.

![](../Media/img/img-07.png)

1.13 ) Choose From blank and Provide a name for your experiment. then click on the 'Associate a machine learning service instance' url
![](../Media/img/autoAi.png)

1.14 ) select a lite instance and click confirm then create the service.Once the service is created go back to the Auto AI Tab and click on Reload.

![](../Media/img/createWml.gif)

1.15 ) Click on create and in the next page click pn browse and upload 'train.csv_shaped.csv' or you can also drag and rop the same file on the upload area
![](../Media/img/uploadData.png)

1.16 ) Select the predict column to be 'loan status' and click on 'Run Experiment'

![](../Media/img/runExperiment.png)

1.17 ) Then the AutoAI experiment starts running. AutoAI will create multiple pipelines.

![](../Media/img/autoAiRun.png)

to further understand how AutoAi works, please refer the [documentation](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/autoai-overview.html?context=analytics)

1.18 ) Once the process is completed, the pipelines are sorted according to the optimization metric and the most efficient pipeline is marked with a star next to it.

![](../Media/img/img-13.png)

## Save the model and create a deployment

1.19 ) You can explore the pipeline information by clicking on its name. To save this model, from the right top corner click on Save as and choose model.

![](../Media/img/img-14.png)

1.20 ) You can leave the model details as default and click on save

![](../Media/img/modelDetails.png)

 #### Note: the name generated depends on the algorithm used, sometimes it can be different from what is showed in the illustrations

1.21 ) Once the model is saved, click on View in project from the pop-up notification to open the saved model.You can always find it listed in assets tab of your project

![](../Media/img/viewModel.png)

1.22 ) once the saved model is opened,navigate to deployments tab and click on click on Add Deployment.

![](../Media/img/img-16.png)

1.23 ) Provide a name and click on Save.

![](../Media/img/deployment.png)

1.24 ) Wait for deployment status to change to Ready and click on the created deployment.

![](../Media/img/img-18.png)

1.25 ) In the deployment,navigate to Test tab and input the details and click on Predict to get the predictions from the saved model

![](../Media/img/testDeployment.png)

1.26 ) Now that the model is deployed and you have tested it out, you can switch to the implementation tab and copy the scoring End-Point url

![](../Media/img/wmlEndPoint.png)

1.27 ) We would need a couple of more credentials to access the model, to get them navigate to your [resources dashboard on IBM Cloud](https://cloud.ibm.com/resources)
1.28 ) Under services, choose your Machine learning service

![](../Media/img/resources.png)

1.29 ) Navigate to the Service Credentials tab and then create a new set of credentials

![](../Media/img/cred.png)

1.30 ) You can leave the defaults and click on add, once the new set of credentials are added, you will need to copy

```
"apikey":"<Your WML API key>"
"instance_id":"<your WML Instance Id>"
```

![](../Media/img/getCred.gif)

we suggest maintaining a single note where you copy all the required credentials as we move forward.

1.31 ) Now proceed to [Step 2](https://github.com/krishnac7/Smart-FAQ-Assistant/tree/master/Step2-Discovery)