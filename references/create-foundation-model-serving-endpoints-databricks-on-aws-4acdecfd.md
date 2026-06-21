---
title: Create foundation model serving endpoints | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/create-foundation-model-endpoints
ingestedAt: "2026-06-18T08:11:47.135Z"
---

In this article, you learn how to create model serving endpoints that deploy and serve foundation models.

[Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) supports the following models:

*   [External models](https://docs.databricks.com/aws/en/generative-ai/external-models/). These are foundation models that are hosted outside of Databricks. Endpoints that serve external models can be centrally governed and customers can establish rate limits and access control for them. Examples include foundation models like OpenAI's GPT-4 and Anthropic's Claude.

*   State-of-the-art open foundation models made available by [Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/). These models are curated foundation model architectures that support optimized inference. Base models, like Meta-Llama-3.3-70B-Instruct and GTE-Large, are available for immediate use with **pay-per-token** pricing. Production workloads, using base or fine-tuned models, can be deployed with performance guarantees using **provisioned throughput**.

Model Serving provides the following options for model serving endpoint creation:

*   The Serving UI
*   REST API
*   MLflow Deployments SDK

For creating endpoints that serve traditional ML or Python models, see [Create custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints).

## Requirements[​](#requirements "Direct link to requirements")

*   A Databricks workspace in a supported region.
    *   [Foundation Model APIs regions](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#regions)
    *   [External models regions](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#regions)
*   For creating endpoints using the MLflow Deployments SDK, you must install the MLflow Deployment client. To install it, run:

Python

    import mlflow.deploymentsclient = mlflow.deployments.get_deploy_client("databricks")

## Create a foundation model serving endpoint[​](#create-a-foundation-model-serving-endpoint "Direct link to Create a foundation model serving endpoint")

You can create an endpoint that serves fine-tuned variants of foundation models made available using Foundation Model APIs **provisioned throughput**. See [Create your provisioned throughput endpoint using the REST API](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis#provisioned-throughput-api).

For foundation models that are made available using Foundation Model APIs **pay-per-token**, Databricks automatically provides specific endpoints to access the supported models in your Databricks workspace. To access them, select the **Serving** tab in the left sidebar of the workspace. The Foundation Model APIs are located at the top of the Endpoints list view.

For querying these endpoints, see [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models).

## Create an external model serving endpoint[​](#create-an-external-model-serving-endpoint "Direct link to create-an-external-model-serving-endpoint")

The following describes how to create an endpoint that queries a foundation model made available using Databricks external models.

*   Serving UI
*   REST API
*   MLflow Deployments SDK

1.  In the **Name** field provide a name for your endpoint.
2.  In the **Served entities** section
    1.  Click into the **Entity** field to open the **Select served entity** form.
    2.  Select **Foundation models**.
    3.  In the **Select a foundation model** field, select the model provider you want to use from those listed under **External model providers**. The form dynamically updates based on your model provider selection.
    4.  Click **Confirm**.
    5.  Provide the configuration details for accessing the selected model provider. This is typically the secret that references the [personal access token](https://docs.databricks.com/aws/en/admin/access-control/tokens#enable-tokens) you want the endpoint to use to access this model.
    6.  Select the task. Available tasks are chat, completion, and embeddings.
    7.  Select the name of the external model you want to use. The list of models dynamically updates based on your task selection. See the [available external models](https://docs.databricks.com/aws/en/machine-learning/model-serving/foundation-model-overview#external-model).
3.  Click **Create**. The **Serving endpoints** page appears with **Serving endpoint state** shown as Not Ready.

![Create a model serving endpoint](https://docs.databricks.com/aws/en/assets/images/create-endpoint-eb0a4ce61321f63be092b3e0359f1c07.png)

## Update model serving endpoints[​](#update-model-serving-endpoints "Direct link to update-model-serving-endpoints")

After enabling a model endpoint, you can set the compute configuration as desired. This configuration is particularly helpful if you need additional resources for your model. Workload size and compute configuration play a key role in what resources are allocated for serving your model.

Until the new configuration is ready, the old configuration keeps serving prediction traffic. While there is an update in progress, another update cannot be made. In the Serving UI, you can cancel an in progress configuration update by selecting **Cancel update** on the top right of the endpoint's details page. This functionality is only available in the Serving UI.

When an `external_model` is present in an endpoint configuration, the served entities list can only have one served\_entity object. Existing endpoints with an `external_model` can not be updated to no longer have an `external_model`. If the endpoint is created without an `external_model`, you cannot update it to add an `external_model`.

*   REST API
*   MLflow Deployments SDK

To update your endpoint see the REST API [update configuration documentation](https://docs.databricks.com/api/workspace/servingendpoints/updateconfig) for request and response schema details.

Bash

    {  "name": "openai_endpoint",  "served_entities":  [    {      "name": "openai_chat",      "external_model":{        "name": "gpt-4",        "provider": "openai",        "task": "llm/v1/chat",        "openai_config":{          "openai_api_key": "{{secrets/my_scope/my_openai_api_key}}"        }      }    }  ]}

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [AI Gateway-enabled inference tables](https://docs.databricks.com/aws/en/ai-gateway/inference-tables)
*   [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models).
*   [External models in Model Serving](https://docs.databricks.com/aws/en/generative-ai/external-models/).
