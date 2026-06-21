---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 20ed35fcb6b340392de1e8bcf4631ab69abf0ce66d7735075fb3136cc55a0b1b
  pageDirectory: concepts
  sources:
    - express-deployments-for-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - express-deployment-requirements-and-constraints
    - Constraints and Express Deployment Requirements
    - EDRAC
  citations:
    - file: express-deployments-for-model-serving-endpoints-databricks-on-aws.md
title: Express Deployment Requirements and Constraints
description: The set of conditions necessary for express deployments including UC model registry, CPU serving, custom models (not FMAPI), max 1GB environment size, mlflow>=3.1, and serverless notebooks.
tags:
  - requirements
  - constraints
  - model-serving
timestamp: "2026-06-19T18:47:20.657Z"
---

# Express Deployment Requirements and Constraints

**Express Deployment** (previously called serverless optimized deployments) is a Databricks model serving feature that packages and stages model artifacts in serverless notebook environments during model registration, resulting in accelerated endpoint deployment and consistent environments between training and serving. Unlike non-express deployments, where model artifacts and environments are packaged into containers at deployment time, express deployments ensure the serving environment matches the one used during model training. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Requirements

Express deployment endpoints share the same base requirements as standard [model serving endpoints](/concepts/model-serving-endpoint.md), with the following additional constraints: ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### Model Type

- The model must be a **custom model** (not FMAPI). ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### Environment and Registration

- The model must be logged and registered in a [Serverless Notebook](/concepts/serverless-notebook-environments.md) using environment version 3 or 4. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- The model must be logged and registered with `mlflow>=3.1`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- The model must be registered in [Unity Catalog](/concepts/unity-catalog.md) and served with CPU. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### Environment Size Limit

- The model's maximum environment size is **1 GB**. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Using Express Deployments

When logging and registering a model, use a Serverless Notebook with client version 3 or 4 and `mlflow>=3.1`. To adjust the client version of the serverless environment, see Configure the serverless environment. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### Registering with `env_pack`

When registering a model, set the `env_pack` parameter with the desired values: ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

```python
import mlflow
from mlflow.utils.env_pack import EnvPackConfig

mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack=EnvPackConfig(name="databricks_model_serving")
)
```

Adding the `env_pack` parameter causes the function to pack and stage the model artifacts and serverless notebook environment during model registration to prepare it for usage during deployment. This may take additional time compared to registering the model without `env_pack`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### The `install_dependencies` Parameter

`EnvPackConfig` has a parameter `install_dependencies` (default: `True`) that determines whether the model's dependencies are installed in the current environment to confirm the environment is valid. If you'd like to skip that step, set the value to `False`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

> **Important:** Endpoints in workspaces without internet access or endpoints with dependencies on custom libraries may fail if `install_dependencies` is set to `True`. In these cases, set `install_dependencies` to `False`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

You can also substitute `EnvPackConfig(...)` with `"databricks_model_serving"` as a shorthand. This is equivalent to `EnvPackConfig(name="databricks_model_serving", install_dependencies = True)`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Deployment

After registering the model, you can [deploy the model in model serving](/concepts/mlflow-model-serving-and-deployment.md). Notice that the deployment time is reduced and the event logs no longer indicate container build. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model serving endpoints](/concepts/model-serving-endpoint.md)
- [Serverless Notebook](/concepts/serverless-notebook-environments.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- FMAPI
- Configure the serverless environment

## Sources

- express-deployments-for-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [express-deployments-for-model-serving-endpoints-databricks-on-aws.md](/references/express-deployments-for-model-serving-endpoints-databricks-on-aws-00f4ae5c.md)
