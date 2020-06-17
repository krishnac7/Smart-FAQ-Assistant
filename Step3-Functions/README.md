## Functions

*Quick links :*
[Home](/README.md) - [Step 1](https://github.com/krishnac7/Smart-FAQ-Assistant/tree/master/Step1-Wml) - [Step 2](https://github.com/krishnac7/Smart-FAQ-Assistant/tree/master/Step2-Discovery) - [**Step 3**](https://github.com/krishnac7/Smart-FAQ-Assistant/tree/master/Step3-Functions) - [Step 4](https://github.com/krishnac7/Smart-FAQ-Assistant/tree/master/Step4-Assistant)
***


### Overview

In this, you will create an action using cloud functions that will parse the data fetched from Watson Discovery and Watson Machine Learning.

### Create an action in Functions

1. From the navigation menu, click on Functions.

![](../Media/imgf/img-01.png)

2. Select Actions.

![](../Media/imgf/img-02.png)

3. Provide a name to your action and change the runtime to python 3.7.

![](../Media/imgf/img-03.png)

4. Paste the code provided in this repo.

![](../Media/imgf/img-04.png)

5. Go to parameters, click on Add parameter and provide the following parametes that are copied from discovery and watson machine learning.

![](../Media/imgf/img-05.png)

6. Go to endpoints, click on "Enable as web Action" copy the url that is generated in this step.

![](../Media/imgf/img-06.png)
