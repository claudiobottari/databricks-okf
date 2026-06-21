---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d9fee589b2465921b24f7ef1cea981606731a86b96eb01eae82ac7a811e702f7
  pageDirectory: concepts
  sources:
    - express-deployments-for-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-notebook-environment-for-model-registration
    - SNEFMR
  citations:
    - file: express-deployments-for-model-serving-endpoints-databricks-on-aws.md
title: Serverless Notebook Environment for Model Registration
description: The requirement that models must be logged and registered in Databricks Serverless Notebooks (client version 3 or 4) to use express deployments.
tags:
  - databricks
  - notebooks
  - serverless
timestamp: "2026-06-18T12:17:06.164Z"
---

# Serverless Notebook Environment for Model Registration

**Serverless Notebook Environment for Model Registration** refers to the packaging and staging of model artifacts and their dependencies within a [Serverless Notebook](/concepts/serverless-notebook-environments.md) compute environment at the time of model registration. This approach enables accelerated model serving endpoint deployment and ensures consistency between the training environment and the serving environment. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Overview

When a model is registered from a serverless notebook environment, the model artifacts and environment dependencies can be packaged and staged during registration rather than at deployment time. In traditional deployments, model artifacts and environments are packaged into containers at deployment time, which can lead to environment mismatches between training and serving. Express deployments — which require a serverless notebook environment during registration — eliminate this inconsistency by packaging the environment at the point of model registration. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Requirements

To use the serverless notebook environment for model registration, the following requirements must be met: ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

- The model must be a custom model (not using the [Foundation Model APIs (FMAPI)](/concepts/foundation-model-apis.md))
- The model must be logged and registered in a Serverless Notebook using environment version 3 or 4
- The model must be logged and registered with `mlflow>=3.1`
- The model must be registered in [Unity Catalog](/concepts/unity-catalog.md) and served with CPU
- The model's maximum environment size must be 1GB or less

These requirements apply in addition to the standard Model Serving Endpoint requirements. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Enabling Express Deployment During Registration

When logging and registering a model, use a Serverless Notebook with environment client version 3 or 4 and `mlflow>=3.1`. To adjust the client version of the serverless environment, see Configure the serverless environment. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

When registering a model, set the `env_pack` parameter to enable packaging and staging: ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

```python
import mlflow
from mlflow.utils.env_pack import EnvPackConfig

mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack=EnvPackConfig(name="databricks_model_serving"),
)
```

Adding the `env_pack` parameter instructs MLflow to pack and stage the model artifacts and serverless notebook environment during model registration, preparing them for use during deployment. This may take additional time compared to registering the model without `env_pack`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### The `install_dependencies` Parameter

`EnvPackConfig` has a parameter `install_dependencies` (defaults to `True`) that determines whether the model's dependencies are installed in the current environment to confirm the environment is valid. If you want to skip this validation step, set the value to `False`: ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

```python
env_pack=EnvPackConfig(
    name="databricks_model_serving",
    install_dependencies=False,
)
```

Endpoints in workspaces without internet access or endpoints with dependencies on custom libraries may fail if `install_dependencies` is set to `True`. In these cases, set `install_dependencies` to `False`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### Shorthand Notation

You can substitute `EnvPackConfig(...)` with the string `"databricks_model_serving"` as a shorthand. This is equivalent to `EnvPackConfig(name="databricks_model_serving", install_dependencies=True)`: ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

```python
mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack="databricks_model_serving",
)
```

## Benefits

### Accelerated Deployment

After the model is registered with the serverless notebook environment packaged, deployment to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) is significantly faster. The event logs no longer indicate a container build step, as the environment is already prepared. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### Consistent Environments

Because the environment is captured during training (within the serverless notebook) and packaged at registration time, the serving environment is guaranteed to match the training environment. This eliminates discrepancies caused by separate container builds at deployment time. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Express Deployments for Model Serving](/concepts/express-deployments-for-model-serving.md) — The deployment approach enabled by serverless notebook environment packaging
- MLflow Models — The model format used with serverless notebook registration
- [Unity Catalog](/concepts/unity-catalog.md) — Required catalog for models using express deployment
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — The serving infrastructure that benefits from pre-packaged environments
- [Serverless Notebook](/concepts/serverless-notebook-environments.md) — The compute environment where model training and registration occur

## Sources

- express-deployments-for-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [express-deployments-for-model-serving-endpoints-databricks-on-aws.md](/references/express-deployments-for-model-serving-endpoints-databricks-on-aws-00f4ae5c.md)
