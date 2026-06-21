---
title: "Tutorial: Deploy and query a custom model | Databricks on AWS"
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-intro
ingestedAt: "2026-06-18T08:12:12.031Z"
---

This article provides the basic steps for deploying and querying a custom model, that is a traditional ML model, using Model Serving. The model must be registered in Unity Catalog or in the workspace model registry.

To learn about serving and deploying generative AI models instead, see the following articles:

*   [External Models](https://docs.databricks.com/aws/en/generative-ai/tutorials/external-models-tutorial)
*   [Foundation Model API](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models)

## Step 1: Log the model[​](#step-1-log-the-model "Direct link to Step 1: Log the model")

There are different ways to log your model for model serving:

The following example shows how to log your MLflow model using the `transformer` flavor and specify parameters you need for your model.

Python

    with mlflow.start_run():    model_info = mlflow.transformers.log_model(        transformers_model=text_generation_pipeline,        artifact_path="my_sentence_generator",        inference_config=inference_config,        registered_model_name='gpt2',        input_example=input_example,        signature=signature    )

After your model is logged be sure to check that your model is registered in either [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/) or the MLflow [Model Registry](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/).

## Step 2: Create endpoint using the Serving UI[​](#step-2-create-endpoint-using-the-serving-ui "Direct link to Step 2: Create endpoint using the Serving UI")

After your registered model is logged and you are ready to serve it, you can create a model serving endpoint using the **Serving** UI.

1.  Click **Serving** in the sidebar to display the **Serving** UI.
    
2.  Click **Create serving endpoint**.
    
    ![Model serving pane in Databricks UI](https://docs.databricks.com/aws/en/assets/images/serving-pane-ea28c77158ce07121e7c86bd9aa897ac.png)
    
3.  In the **Name** field, provide a name for your endpoint.
    
4.  In the **Served entities** section
    
    1.  Click into the **Entity** field to open the **Select served entity** form.
    2.  Select the type of model you want to serve. The form dynamically updates based on your selection.
    3.  Select which model and model version you want to serve.
    4.  Select the percentage of traffic to route to your served model.
    5.  Select what size compute to use.
    6.  Under **Compute Scale-out**, select the size of the compute scale out that corresponds with the number of requests this served model can process at the same time. This number should be roughly equal to QPS x model execution time.
        1.  Available sizes are **Small** for 0-4 requests, **Medium** 8-16 requests, and **Large** for 16-64 requests.
    7.  Specify if the endpoint should scale to zero when not in use.
5.  Click **Create**. The **Serving endpoints** page appears with **Serving endpoint state** shown as Not Ready.
    
    ![Create a model serving endpoint](https://docs.databricks.com/aws/en/assets/images/create-endpoint-eb0a4ce61321f63be092b3e0359f1c07.png)
    

If you prefer to create an endpoint programmatically with the Databricks Serving API, see [Create custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints).

## Step 3: Query the endpoint[​](#step-3-query-the-endpoint "Direct link to Step 3: Query the endpoint")

The easiest and fastest way to test and send scoring requests to your served model is to use the **Serving** UI.

1.  From the **Serving endpoint** page, select **Query endpoint**.
    
2.  Insert the model input data in JSON format and click **Send Request**. If the model has been logged with an input example, click **Show Example** to load the input example.
    
    Python
    
           {   "inputs" : ["Hello, I'm a language model,"],   "params" : {"max_new_tokens": 10, "temperature": 1}   }
    

To send scoring requests, construct a JSON with one of the supported keys and a JSON object corresponding to the input format. See [Query serving endpoints for custom models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-custom-model-endpoints) for supported formats and guidance on how to send scoring requests using the API.

If you plan to access your serving endpoint outside of the Databricks Serving UI, you need a `DATABRICKS_API_TOKEN`.

## Example notebooks[​](#example-notebooks "Direct link to Example notebooks")

See the following notebook for serving a MLflow `transformers` model with Model Serving.

#### Deploy a Hugging Face transformers model notebook

See the following notebook for serving a MLflow `pyfunc` model with Model Serving. For additional details on customizing your model deployments, see [Deploy Python code with Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/deploy-custom-python-code).

#### Deploy a MLflow pyfunc model notebook
