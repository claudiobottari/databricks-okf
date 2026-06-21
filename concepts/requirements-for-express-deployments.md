---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 872fb3c58fc4e2dca2328cea1051ba5f7690ae93c0a9d4769c5d478dc784ea49
  pageDirectory: concepts
  sources:
    - express-deployments-for-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - requirements-for-express-deployments
    - RFED
  citations:
    - file: express-deployments-for-model-serving-endpoints-databricks-on-aws.md
title: Requirements for Express Deployments
description: "Specific conditions that must be met for express deployments: custom models only, serverless notebook registration, mlflow>=3.1, UC registration, CPU serving, and max 1GB environment size."
tags:
  - requirements
  - databricks
  - deployment
timestamp: "2026-06-18T12:17:26.964Z"
---

# Requirements for Express Deployments

**Express deployments** (formerly called serverless optimized deployments) are a feature of [Model Serving](/concepts/model-serving.md) that dramatically lower deployment times and keep the model serving environment identical to the model training environment. This is achieved by packaging and staging model artifacts in [Serverless Notebook Notebooks](/concepts/serverless-notebook-environments.md) during model registration, rather than building containers at deployment time. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

Express deployments differ from non-express deployments, where model artifacts and environments are packaged into containers at deployment time, which may result in a serving environment that does not match the one used during model training. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Overview of Requirements

Express deployment endpoints have the same requirements as standard model serving endpoints (see [Model Serving Endpoint Requirements](/concepts/model-serving-endpoint.md)). In addition, the following specific requirements must be met. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Model Requirements

- **Custom model only.** The model must be a custom model, not an FMAPI (Foundation Model APIs) model. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- **CPU serving only.** The model must be served with CPU. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- **Max environment size of 1GB.** The model's environment size must not exceed 1GB. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Registration Requirements

- **Registered in Unity Catalog.** The model must be registered in [Unity Catalog](/concepts/unity-catalog.md). ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- **Logged and registered in a Serverless Notebook.** The model must be logged and registered in a [Serverless Notebook](/concepts/serverless-notebook-environments.md) using serverless environment version 3 or 4. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- **MLflow version.** The model must be logged and registered with `mlflow>=3.1`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- **Use the `env_pack` parameter.** When registering the model, you must set the `env_pack` parameter to either `EnvPackConfig(name="databricks_model_serving")` or its shorthand `"databricks_model_serving"`. This packages and stages the model artifacts and serverless notebook environment during model registration to prepare it for usage during deployment. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

```python
import mlflow
from mlflow.utils.env_pack import EnvPackConfig

mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack=EnvPackConfig(name="databricks_model_serving")
)
```

Adding the `env_pack` parameter may take additional time compared to registering the model without it. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Dependency Installation Requirements

The `EnvPackConfig` has a parameter `install_dependencies` that is `True` by default. This parameter determines whether the model's dependencies are installed in the current environment to confirm the environment is valid. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### Internet Access and Custom Libraries

Endpoints in workspaces without internet access or endpoints with dependencies on custom libraries may fail if `install_dependencies` is set to `True`. In these cases, set `install_dependencies` to `False`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

```python
mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack=EnvPackConfig(name="databricks_model_serving", install_dependencies=False)
)
```

The shorthand `"databricks_model_serving"` is equivalent to `EnvPackConfig(name="databricks_model_serving", install_dependencies=True)`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Summary Table

| Requirement | Specification |
|-------------|---------------|
| Model type | Custom model (not FMAPI) |
| Registration target | Unity Catalog |
| Compute | CPU only |
| Max environment size | 1 GB |
| Notebook environment | Serverless Notebook, client version 3 or 4 |
| MLflow version | `mlflow>=3.1` |
| Registration parameter | `env_pack` must be set |

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The serving platform for MLflow models
- [Serverless Notebook Environments](/concepts/serverless-notebook-environments.md) — The runtime environment for model training
- [Model Serving Endpoint Requirements](/concepts/model-serving-endpoint.md) — Base requirements for all serving endpoints
- [Unity Catalog](/concepts/unity-catalog.md) — Required for registered models
- [FMAPI Foundation Model APIs](/concepts/foundation-model-apis.md) — Not supported for express deployments

## Sources

- express-deployments-for-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [express-deployments-for-model-serving-endpoints-databricks-on-aws.md](/references/express-deployments-for-model-serving-endpoints-databricks-on-aws-00f4ae5c.md)
