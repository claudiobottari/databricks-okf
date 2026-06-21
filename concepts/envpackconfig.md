---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 00a2fc2184d6d62e6f5c35aeae2b3fa272dbcc31d17cfc712c19f05b90ca1f7a
  pageDirectory: concepts
  sources:
    - express-deployments-for-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - envpackconfig
  citations:
    - file: express-deployments-for-model-serving-endpoints-databricks-on-aws.md
title: EnvPackConfig
description: A configuration class with an install_dependencies parameter that controls whether model dependencies are installed during the env_pack process to validate the environment.
tags:
  - configuration
  - mlflow
  - dependencies
timestamp: "2026-06-19T18:46:47.741Z"
---

# EnvPackConfig

**EnvPackConfig** is a configuration class in the MLflow Python SDK used to control environment packaging for [Express Deployments for Model Serving Endpoints](/concepts/express-deployments-databricks.md). It is passed as the `env_pack` parameter to `mlflow.register_model()` to trigger packaging and staging of model artifacts and the serverless notebook environment during model registration, enabling accelerated endpoint deployment and consistent environments between training and serving.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Overview

When `mlflow.register_model()` is called with `EnvPackConfig`, the function packages and stages the model artifacts along with the serverless notebook environment during model registration, preparing them for deployment. This reduces deployment time and eliminates the container build step that would otherwise occur at deployment time, avoiding possible mismatches between training and serving environments.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

The class is part of the `mlflow.utils.env_pack` module.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Parameters

### `name` (required)

Specifies the type of express deployment. For Databricks model serving, the value must be `"databricks_model_serving"`.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### `install_dependencies` (optional, default `True`)

A boolean parameter that determines whether the model's dependencies are installed in the current environment to confirm the environment is valid before deployment.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

Setting this value to `False` skips the validation step. This is useful in workspaces without internet access or endpoints with dependencies on custom libraries, where attempting to install dependencies may fail.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Usage

### Basic Usage

```python
import mlflow
from mlflow.utils.env_pack import EnvPackConfig

mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack=EnvPackConfig(name="databricks_model_serving")
)
```

^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### Skipping Dependency Validation

```python
mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack=EnvPackConfig(
        name="databricks_model_serving",
        install_dependencies=False
    )
)
```

^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### Shorthand Usage

As an alternative to explicitly creating an `EnvPackConfig` instance, the string `"databricks_model_serving"` can be passed directly as the `env_pack` parameter. This shorthand is equivalent to `EnvPackConfig(name="databricks_model_serving", install_dependencies=True)`.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

```python
mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack="databricks_model_serving"
)
```

## Effect on Model Registration

Adding the `env_pack` parameter causes `mlflow.register_model()` to package and stage model artifacts and the serverless notebook environment during model registration. This may take additional time compared to registering the model without `env_pack`, but it reduces deployment time and eliminates the container build step during endpoint creation.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Express Deployments for Model Serving Endpoints](/concepts/express-deployments-databricks.md) — The deployment acceleration feature that EnvPackConfig enables.
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The serving infrastructure that hosts deployed models.
- [Serverless Notebook Environments](/concepts/serverless-notebook-environments.md) — The compute environment required for express deployments.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — A separate serving option for foundation models (not compatible with express deployments).

## Sources

- express-deployments-for-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [express-deployments-for-model-serving-endpoints-databricks-on-aws.md](/references/express-deployments-for-model-serving-endpoints-databricks-on-aws-00f4ae5c.md)
