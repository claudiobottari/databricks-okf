---
title: Configure access to resources from model serving endpoints | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving
ingestedAt: "2026-06-18T08:12:50.642Z"
---

This article describes how to configure access to external and private resources from model serving endpoints. Model Serving supports plain text environment variables and secrets-based environment variables using Databricks [secrets](https://docs.databricks.com/aws/en/security/secrets/#secrets).

## Requirements[​](#requirements "Direct link to Requirements")

For secrets-based environment variables,

*   The endpoint creator must have READ access to the Databricks secrets being referenced in the configs.
*   You must store credentials like your API key or other tokens as a Databricks secret.

## Add plain text environment variables[​](#add-plain-text-environment-variables "Direct link to add-plain-text-environment-variables")

Use plain text environment variables to set variables that don't need to be hidden. You can set variables in the Serving UI, the REST API or the SDK when you create or update an endpoint.

*   Serving UI
*   REST API
*   WorkspaceClient SDK
*   MLflow Deployments SDK

From the Serving UI, you can add an environment variable in **Advanced configurations**:

![Create a model serving endpoint](https://docs.databricks.com/aws/en/assets/images/add-env-variable-ad2b102e19093f57131762b347fa0972.png)

## Log feature lookup DataFrames to inference tables[​](#-log-feature-lookup-dataframes-to-inference-tables "Direct link to -log-feature-lookup-dataframes-to-inference-tables")

If you have inference tables enabled on your endpoint, you can log your [automatic feature lookup data frame](https://docs.databricks.com/aws/en/machine-learning/feature-store/automatic-feature-lookup) to that inference table using `ENABLE_FEATURE_TRACING`. This requires MLflow 2.14.0 or above.

Set `ENABLE_FEATURE_TRACING` as an environment variable in the Serving UI, REST API or SDK when you create or update an endpoint.

*   Serving UI
*   REST API
*   WorkspaceClient SDK
*   MLflow Deployments SDK

1.  In **Advanced configurations**, select \*\* + Add environment variables\*\*.
2.  Type `ENABLE_FEATURE_TRACING` as the environment name.
3.  In the field to the right type `true`.

![Create a model serving endpoint](https://docs.databricks.com/aws/en/assets/images/add-env-variable-ad2b102e19093f57131762b347fa0972.png)

## Add secrets-based environment variables[​](#add-secrets-based-environment-variables "Direct link to add-secrets-based-environment-variables")

You can securely store credentials using Databricks secrets and reference those secrets in model serving using a secrets-based environment variables. This allows credentials to be fetched from model serving endpoints at serving time.

For example, you can pass credentials to call OpenAI and other external model endpoints or access external data storage locations directly from model serving.

Databricks recommends this feature for deploying [OpenAI](https://mlflow.org/docs/latest/python_api/openai/index.html) and [LangChain](https://mlflow.org/docs/latest/python_api/mlflow.langchain.html) MLflow model flavors to serving. It is also applicable to other SaaS models requiring credentials with the understanding that the access pattern is based on using environment variables and API keys and tokens.

### Step 1: Create a secret scope[​](#step-1-create-a-secret-scope "Direct link to Step 1: Create a secret scope")

During model serving, the secrets are retrieved from Databricks secrets by the secret scope and key. These get assigned to the secret environment variable names that can be used inside the model.

First, create a secret scope. See [Manage secret scopes](https://docs.databricks.com/aws/en/security/secrets/#scopes).

The following are CLI commands:

Bash

    databricks secrets create-scope my_secret_scope

You can then add your secret to a desired secret scope and key as shown below:

Bash

    databricks secrets put-secret my_secret_scope my_secret_key

The secret information and the name of the environment variable can then be passed to your endpoint configuration during endpoint creation or as an update to the configuration of an existing endpoint.

### Step 2: Add secret scopes to endpoint configuration[​](#step-2-add-secret-scopes-to-endpoint-configuration "Direct link to Step 2: Add secret scopes to endpoint configuration")

You can add the secret scope to an environment variable and pass that variable to your endpoint during endpoint creation or configuration updates. See [Create custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints).

*   Serving UI
*   REST API
*   WorkspaceClient SDK
*   MLflow Deployments SDK

From the Serving UI, you can add an environment variable in **Advanced configurations**. The secrets based environment variable must be provided using the following syntax: `{{secrets/scope/key}}`. Otherwise, the environment variable is considered a plain text environment variable.

![Create a model serving endpoint](https://docs.databricks.com/aws/en/assets/images/add-env-variable-ad2b102e19093f57131762b347fa0972.png)

After the endpoint is created or updated, model serving automatically fetches the secret key from the Databricks secrets scope and populates the environment variable for your model inference code to use.

## Notebook example[​](#notebook-example "Direct link to Notebook example")

See the following notebook for an example of how to configure an OpenAI API key for a LangChain Retrieval QA Chain deployed behind the model serving endpoints with secret-based environment variables.

#### Configure access to resources from model serving endpoints notebook

## Additional resource[​](#additional-resource "Direct link to Additional resource")

*   [Add an instance profile to a model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/add-model-serving-instance-profile)
