---
title: Migrate to Model Serving | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/migrate-model-serving
ingestedAt: "2026-06-18T08:12:04.896Z"
---

This article demonstrates how to enable Model Serving in your workspace and switch your models to the [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) experience built on serverless compute.

important

Starting August 22, 2025, customers will no longer be able to create new serving endpoints using the Legacy MLflow Model Serving experience. On September 15, 2025, the legacy experience will reach end of life and all existing endpoints using this service can no longer be used.

## Requirements[​](#requirements "Direct link to Requirements")

*   Registered model in the MLflow Model Registry.
*   Permissions on the registered models as described in the [access control guide](https://docs.databricks.com/aws/en/security/auth/access-control/#serving-endpoints).
*   [Enable serverless compute on your workspace](https://docs.databricks.com/aws/en/machine-learning/model-serving/#serverless).

## Significant changes[​](#significant-changes "Direct link to Significant changes")

*   In Model Serving, the format of the request to the endpoint and the response from the endpoint are slightly different from Legacy MLflow Model Serving. See [Scoring a model endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints#score) for details on the new format protocol.
*   In Model Serving, the endpoint URL includes `serving-endpoints` instead of `model`.
*   Model Serving includes full support for [managing resources with API workflows](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints).
*   Model Serving is production-ready and backed by the Databricks SLA.

## Identify serving endpoints that use Legacy MLflow Model Serving[​](#identify-serving-endpoints-that-use-legacy-mlflow-model-serving "Direct link to Identify serving endpoints that use Legacy MLflow Model Serving")

To identify model serving endpoints that use Legacy MLflow Model Serving:

1.  Navigate to the **Models** UI in your workspace.
2.  Select the **Workspace Model Registry** filter.
3.  Select the **Legacy serving enabled only** filter.

## Migrate Legacy MLflow Model Serving served models to Model Serving[​](#migrate-legacy-mlflow-model-serving-served-models-to-model-serving "Direct link to Migrate Legacy MLflow Model Serving served models to Model Serving")

You can create a Model Serving endpoint and flexibly transition model serving workflows without disabling [Legacy MLflow Model Serving](https://docs.databricks.com/aws/en/archive/legacy-model-serving/model-serving).

The following steps show how to accomplish this with the UI. For each model on which you have Legacy MLflow Model Serving enabled:

1.  Register your model to Unity Catalog.
2.  Navigate to **Serving endpoints** on the sidebar of your machine learning workspace.
3.  Follow the workflow described in [Create custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints) on how to create a serving endpoint with your model.
4.  Transition your application to use the new URL provided by the serving endpoint to query the model, along with the new scoring format.
5.  When your models are transitioned over, you can navigate to **Models** on the sidebar of your machine learning workspace.
6.  Select the model for which you want to disable Legacy MLflow Model Serving.
7.  On the **Serving** tab, select **Stop**.
8.  A message appears to confirm. Select **Stop Serving**.

## Migrate deployed model versions to Model Serving[​](#migrate-deployed-model-versions-to-model-serving "Direct link to Migrate deployed model versions to Model Serving")

In previous versions of the Model Serving functionality, the serving endpoint was created based on the stage of the registered model version: `Staging` or `Production`. To migrate your served models from that experience, you can replicate that behavior in the new Model Serving experience.

This section demonstrates how to create separate model serving endpoints for `Staging` model versions and `Production` model versions. The following steps show how to accomplish this with the serving endpoints API for each of your served models.

In the example, the registered model name `modelA` has version 1 in the model stage `Production` and version 2 in the model stage `Staging`.

1.  Create two endpoints for your registered model, one for `Staging` model versions and another for `Production` model versions.
    
    For `Staging` model versions:
    
    Bash
    
        POST /api/2.0/serving-endpoints  {     "name":"modelA-Staging"     "config":     {        "served_entities":        [           {              "entity_name":"model-A",              "entity_version":"2",  // Staging Model Version              "workload_size":"Small",              "scale_to_zero_enabled":true           },        ],     },  }
    
    For `Production` model versions:
    
    Bash
    
        POST /api/2.0/serving-endpoints  {     "name":"modelA-Production"     "config":     {        "served_entities":        [           {              "entity_name":"model-A",              "entity_version":"1",   // Production Model Version              "workload_size":"Small",              "scale_to_zero_enabled":true           },        ],     },  }
    
2.  Verify the status of the endpoints.
    
    For Staging endpoint: `GET /api/2.0/serving-endpoints/modelA-Staging`
    
    For Production endpoint: `GET /api/2.0/serving-endpoints/modelA-Production`
    
3.  Once the endpoints are ready, query the endpoint using:
    
    For Staging endpoint: `POST /serving-endpoints/modelA-Staging/invocations`
    
    For Production endpoint: `POST /serving-endpoints/modelA-Production/invocations`
    
4.  Update the endpoint based on model version transitions.
    
    In the scenario where a new model version 3 is created, you can have the model version 2 transition to `Production`, while model version 3 can transition to `Staging` and model version 1 is `Archived`. These changes can be reflected in separate model serving endpoints as follows:
    
    For the `Staging` endpoint, update the endpoint to use the new model version in `Staging`.
    
    Bash
    
        PUT /api/2.0/serving-endpoints/modelA-Staging/config{   "served_entities":   [      {         "entity_name":"model-A",         "entity_version":"3",  // New Staging model version         "workload_size":"Small",         "scale_to_zero_enabled":true      },   ],}
    
    For `Production` endpoint, update the endpoint to use the new model version in `Production`.
    
    Bash
    
        PUT /api/2.0/serving-endpoints/modelA-Production/config{   "served_entities":   [      {         "entity_name":"model-A",         "entity_version":"2",  // New Production model version         "workload_size":"Small",         "scale_to_zero_enabled":true      },   ],}
    

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Create Model Serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints)
