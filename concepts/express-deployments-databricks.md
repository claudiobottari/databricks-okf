---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 25fe67088ce0c81bcc9a69fdea784da20720e13540ff2c1ebe5314e7dda7d52f
  pageDirectory: concepts
  sources:
    - express-deployments-for-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - express-deployments-databricks
    - ED(
    - Express Deployments
    - Express deployments
    - express deployments
    - express-deployments-databricks-model-serving
    - ED(MS
    - express-deployments-for-model-serving
    - EDFMS
    - Express Deployments for Model Serving Endpoints
    - Express deployments for model serving endpoints
    - express deployments for model serving endpoints
  citations:
    - file: express-deployments-for-model-serving-endpoints-databricks-on-aws.md
title: Express Deployments (Databricks)
description: A deployment approach for Databricks model serving that accelerates endpoint creation and ensures environment consistency between training and serving by packaging model artifacts during registration.
tags:
  - databricks
  - model-serving
  - deployment
  - machine-learning
timestamp: "2026-06-19T10:27:51.272Z"
---

# Express Deployments (Databricks)

**Express deployments** (formerly called *serverless optimized deployments*) are a feature of [Model Serving](/concepts/model-serving.md) endpoints on Databricks that dramatically reduce deployment time and ensure the serving environment matches the model training environment.

## Overview

In express deployments, model artifacts and their dependencies are packaged and staged in [Serverless Notebook](/concepts/serverless-notebook-environments.md) environments during model registration. This allows endpoint creation to skip the container‑build step that is normally required at deployment time. As a result, endpoints start serving predictions much faster and the runtime environment is guaranteed to be identical to the one used during training.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

This approach contrasts with non-express (standard) deployments, where packaging happens only when the endpoint is created. In those cases, differences between the training and serving environments can arise, and the container build adds noticeable latency.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Requirements

To use express deployments, all of the following conditions must be met:

- The model must be a custom model; FMAPI (Foundation Model APIs) models are not supported.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- The model must be logged and registered from a Serverless Notebook running environment version 3 or 4. (See Serverless environment version for details.)^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- The model must be logged and registered with `mlflow>=3.1`.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- The model must be registered in [Unity Catalog](/concepts/unity-catalog.md) and served using CPU (GPU endpoints are not supported).^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- The total size of the model’s environment (dependencies and artifacts) must be ≤1 GB.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

Other standard model serving endpoint requirements also apply – see Create and manage serving endpoints – Requirements.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Using express deployments

### 1. Environment preparation

Ensure the notebook is a Serverless Notebook with client version 3 or 4 and `mlflow>=3.1`. To change the client version, follow Configure the serverless environment.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### 2. Register the model with `env_pack`

When calling `mlflow.register_model()`, pass the `env_pack` parameter with an `EnvPackConfig` object or the shorthand string `"databricks_model_serving"`.

```python
import mlflow
from mlflow.utils.env_pack import EnvPackConfig

mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack=EnvPackConfig(name="databricks_model_serving")
)
```

The shorthand `"databricks_model_serving"` is equivalent to `EnvPackConfig(name="databricks_model_serving", install_dependencies=True)`.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

The `install_dependencies` parameter (default `True`) controls whether the model’s dependencies are installed in the current environment during registration to validate that the environment is correct. Set it to `False` to skip this step.

> **Note**: Endpoints in workspaces without internet access, or endpoints with dependencies on custom libraries, may fail if `install_dependencies` is `True`. In those cases, set it to `False`.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### 3. Deploy the endpoint

After registration completes, proceed to [deploy the model in Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints) as usual. The deployment time will be noticeably shorter, and the endpoint event logs no longer show a container‑build stage.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Benefits

- **Faster deployment**: The container image is pre‑built during registration, so endpoint creation is nearly instantaneous.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- **Environment consistency**: The exact same dependencies and artifact versions that were used in the Serverless Notebook training environment are carried forward to the serving endpoint, eliminating discrepancies.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- **Simplified CI/CD**: Express deployments fit naturally into automated ML pipelines by moving the expensive packaging step to registration time, which is already part of a typical training pipeline.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Sources

- express-deployments-for-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [express-deployments-for-model-serving-endpoints-databricks-on-aws.md](/references/express-deployments-for-model-serving-endpoints-databricks-on-aws-00f4ae5c.md)
