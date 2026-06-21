---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7f7a63ac6ddf0e4ed736fea7c90f12b9c63c98a73b434c1d850415424ca52fc4
  pageDirectory: concepts
  sources:
    - express-deployments-for-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - express-deployments-databricks-model-serving
    - ED(MS
  citations:
    - file: express-deployments-for-model-serving-endpoints-databricks-on-aws.md
title: Express Deployments (Databricks Model Serving)
description: A deployment method for model serving endpoints that dramatically reduces deployment times by packaging and staging model artifacts during model registration in serverless notebooks.
tags:
  - machine-learning
  - deployment
  - databricks
timestamp: "2026-06-18T12:17:28.752Z"
---

# Express Deployments (Databricks Model Serving)

**Express Deployments** — formerly called *serverless optimized deployments* — is a Databricks feature that dramatically reduces the time required to deploy custom ML models to [Model Serving](/concepts/model-serving.md) endpoints. Express deployments achieve this by packaging and staging model artifacts in [Serverless Notebooks](/concepts/serverless-notebook-environments.md) environments during model registration, rather than at deployment time. This approach also ensures the serving environment is identical to the environment used during model training. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## How Express Deployments Work

In standard (non-express) deployments, model artifacts and their dependencies are packaged into containers at the moment the serving endpoint is created or updated. This process can be time-consuming, and the resulting serving environment may not perfectly match the training environment. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

Express deployments shift this work earlier in the workflow. When you register a model, the `env_pack` parameter triggers the packaging and staging of model artifacts together with the serverless notebook environment. The prepared package is stored and ready for immediate use when the endpoint is deployed, resulting in significantly faster deployment times and eliminating container build steps from the deployment logs. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Requirements

Express deployment endpoints share the same base requirements as standard model serving endpoints (see Create and Manage Serving Endpoints). In addition, the following conditions must be met: ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

- The model must be a **custom model** — not a foundation model deployed via [Foundation Model APIs (FMAPI)](/concepts/foundation-model-apis.md).
- The model must be logged and registered in a **Serverless Notebook** using environment version **3 or 4**.
- The model must be logged and registered with **`mlflow>=3.1`**.
- The model must be **registered in [Unity Catalog](/concepts/unity-catalog.md)** and served with **CPU** (GPU not supported).
- The model's maximum environment size is **1 GB**.

## Using Express Deployments

### Step 1: Configure the Serverless Environment

When logging and registering a model, use a Serverless Notebook with client version 3 or 4 and `mlflow>=3.1`. To adjust the client version of the serverless environment, see [Configure the Serverless Environment](/concepts/serverless-gpu-environment.md). ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### Step 2: Register the Model with `env_pack`

When registering a model, set the `env_pack` parameter to enable express deployment packaging: ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

```python
import mlflow
from mlflow.utils.env_pack import EnvPackConfig

mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack=EnvPackConfig(name="databricks_model_serving")
)
```

Adding the `env_pack` parameter causes the function to pack and stage the model artifacts and serverless notebook environment during model registration. This may take additional time compared to registering the model without `env_pack`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### Step 3: Deploy the Model

After registration completes, deploy the model to a serving endpoint following the standard procedure (see Create and Manage Serving Endpoints). The deployment time is noticeably reduced, and the event logs no longer indicate a container build step. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## The `EnvPackConfig` Object

`EnvPackConfig` accepts the following parameters: ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

| Parameter | Default | Description |
|-----------|---------|-------------|
| `name` | (required) | Set to `"databricks_model_serving"` to enable express deployment |
| `install_dependencies` | `True` | When `True`, the model's dependencies are installed in the current environment to confirm the environment is valid before packaging |

### Shorthand Syntax

You can substitute `EnvPackConfig(name="databricks_model_serving", install_dependencies=True)` with the shorthand string `"databricks_model_serving"` directly: ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

```python
mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack="databricks_model_serving"
)
```

## Important Notes

### Disabling Dependency Installation

If you want to skip the dependency validation step, set `install_dependencies=False`: ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

```python
EnvPackConfig(
    name="databricks_model_serving",
    install_dependencies=False
)
```

### Connectivity and Custom Dependencies

Endpoints in workspaces **without internet access** or endpoints with dependencies on **custom libraries** may fail if `install_dependencies` is set to `True`. In these cases, set `install_dependencies` to `False`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Benefits

- **Reduced deployment time** — Packaging happens during registration, not at deployment time.
- **Consistent environments** — The serving environment matches the training environment exactly.
- **Simplified deployment logs** — No container build steps appear in the event logs.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The serving infrastructure for ML models on Databricks
- [Serverless Notebooks](/concepts/serverless-notebook-environments.md) — The compute environment required for express deployments
- [Unity Catalog](/concepts/unity-catalog.md) — Required for model registration with express deployments
- MLflow Model Registration — The workflow for logging and registering models
- Create and Manage Serving Endpoints — Standard deployment procedures
- [Foundation Model APIs (FMAPI)](/concepts/foundation-model-apis.md) — Foundation model serving (not compatible with express deployments)
- [Configure the Serverless Environment](/concepts/serverless-gpu-environment.md) — Adjusting serverless client versions

## Sources

- express-deployments-for-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [express-deployments-for-model-serving-endpoints-databricks-on-aws.md](/references/express-deployments-for-model-serving-endpoints-databricks-on-aws-00f4ae5c.md)
