---
title: Express deployments for model serving endpoints | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/express-deployments
ingestedAt: "2026-06-18T08:11:55.099Z"
---

This article describes how to use express deployments on your [model serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) endpoints. Express deployments dramatically lower deployment times and keep the model serving environment the same as the model training environment.

note

Express deployments were previously called serverless optimized deployments.

## What are express deployments?[​](#what-are-express-deployments "Direct link to What are express deployments?")

Express deployments take advantage of packaging and staging model artifacts in serverless notebook environments during model registration, resulting in accelerated endpoint deployment and consistent environments between training and serving.

This differs from non-express deployments, where model artifacts and environments are packaged into containers at deployment time. In such cases, the serving environment may not match the one used during model training.

## Requirements[​](#requirements "Direct link to Requirements")

Express deployment endpoints have the same requirements as model serving endpoint (see [Requirements](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints#requirement)). In addition:

*   The model must be a custom model (not [FMAPI](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis))
*   The model must be logged and registered in a [Serverless Notebook](https://docs.databricks.com/aws/en/compute/serverless/notebooks) using [version](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/) 3 or 4
*   The model must be logged and registered with `mlflow>=3.1`
*   The model must be registered in UC and served with CPU
*   The model's max environment size is 1GB

## Using express deployments[​](#using-express-deployments "Direct link to Using express deployments")

When logging and registering a model, use a Serverless Notebook with client 3 or 4 and `mlflow>=3.1`.

To adjust the client version of the serverless environment, see [Configure the serverless environment](https://docs.databricks.com/aws/en/compute/serverless/dependencies).

Then, when registering a model, set the `env_pack` parameter with the desired values.

Python

    import mlflowfrom mlflow.utils.env_pack import EnvPackConfigmlflow.register_model(    model_info.model_uri,    model_name,    env_pack=EnvPackConfig(name="databricks_model_serving"))

Adding in the `env_pack` parameter will make the function pack and stage the model artifacts and serverless notebook environment during model registration to prepare it for usage during deployment. This may take additional time compared to registering the model without `env_pack`.

`EnvPackConfig` has a parameter `install_dependencies` (`True` by default) that determines whether the model's dependencies are installed in the current environment to confirm the environment is valid. If you'd like to skip that step, set the value to `False`.

note

Endpoints in workspaces without internet access or endpoints with dependencies on custom libraries may fail if `install_dependencies` is set to `True`. In these cases, set `install_dependencies` to `False`.

You can also substitute `EnvPackConfig(...)` with `"databricks_model_serving"` as a shorthand. This is equivalent to `EnvPackConfig(name="databricks_model_serving", install_dependencies = True)`.

After registering the model is finished, you can [deploy the model in model serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints). Notice that the deployment time is reduced and the event logs no longer indicate container build.
