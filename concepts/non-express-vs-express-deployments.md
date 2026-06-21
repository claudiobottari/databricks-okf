---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4378ecb339794df977324ff505bcfa26be7fe9ec23ef9fdf868733be2401ae89
  pageDirectory: concepts
  sources:
    - express-deployments-for-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non-express-vs-express-deployments
    - NVED
  citations:
    - file: express-deployments-for-model-serving-endpoints-databricks-on-aws.md
title: Non-Express vs Express Deployments
description: The contrast between traditional deployments (packaging artifacts at deployment time, risking environment drift) and express deployments (packaging at registration time for consistency).
tags:
  - comparison
  - deployment
  - architecture
timestamp: "2026-06-19T18:47:03.679Z"
---

# Non-Express vs Express Deployments

**Non-Express vs Express Deployments** describes two distinct approaches for packaging and deploying models on [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoints. Express deployments (previously called serverless optimized deployments) provide faster deployment times and environment consistency, while non-express deployments follow a traditional containerization approach at deployment time. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Key Differences

The fundamental distinction lies in when and how model artifacts and environments are packaged:

- **Express deployments**: Model artifacts and serverless notebook environments are packaged and staged during model registration, before deployment is initiated. This pre-packaging dramatically reduces deployment time and ensures the serving environment matches the training environment. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

- **Non-express deployments**: Model artifacts and environments are packaged into containers at deployment time. This approach may result in a serving environment that does not match the one used during model training. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Requirements for Express Deployments

To use express deployments, the following conditions must be met:

- The model must be a custom model (not an FMAPI foundation model). ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- The model must be logged and registered in a [Serverless Notebook](/concepts/serverless-notebook-environments.md) using environment version 3 or 4. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- The model must be logged and registered with `mlflow>=3.1`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- The model must be registered in [Unity Catalog](/concepts/unity-catalog.md) and served with CPU. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- The model's maximum environment size must be 1GB or less. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

Non-express deployments do not have these additional requirements beyond the standard [model serving endpoint requirements](/concepts/model-serving-endpoint.md). ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Using Express Deployments

When logging and registering a model, use a Serverless Notebook with client version 3 or 4 and `mlflow>=3.1`. During model registration, set the `env_pack` parameter to enable express deployment: ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

```python
import mlflow
from mlflow.utils.env_pack import EnvPackConfig

mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack=EnvPackConfig(name="databricks_model_serving")
)
```

The `env_pack` parameter causes the function to package and stage model artifacts along with the serverless notebook environment during registration, preparing them for deployment. This step may take additional time compared to registering without `env_pack`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### The `install_dependencies` Parameter

`EnvPackConfig` includes an `install_dependencies` parameter (defaults to `True`) that determines whether the model's dependencies are installed in the current environment to validate the environment. To skip this validation step, set `install_dependencies=False`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

Endpoints in workspaces without internet access or endpoints with dependencies on custom libraries may fail if `install_dependencies=True`. In these cases, set the parameter to `False`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

As a shorthand, you can substitute `EnvPackConfig(...)` with the string `"databricks_model_serving"`, which is equivalent to `EnvPackConfig(name="databricks_model_serving", install_dependencies=True)`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Deployment Time Differences

After registering the model with express deployment enabled, you can [deploy the model to a serving endpoint](/concepts/update-model-serving-endpoints.md). The deployment time is noticeably reduced, and the event logs no longer indicate a container build step, which is a hallmark of non-express deployments. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Comparison Summary

| Aspect | Express Deployments | Non-Express Deployments |
|--------|-------------------|------------------------|
| Packaging timing | During model registration | At deployment time |
| Deployment speed | Faster (pre-packaged) | Slower (container build at deploy) |
| Environment consistency | Matches training environment | May differ from training environment |
| Container build in logs | No | Yes |
| Additional requirements | Yes (serverless notebook, mlflow>=3.1, UC registration, CPU, ≤1GB env) | Standard model serving requirements |

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The infrastructure that hosts deployed models.
- MLflow Model Registration — The process of logging and registering models.
- [Serverless Notebooks](/concepts/serverless-notebook-environments.md) — The compute environment required for express deployments.
- [Unity Catalog](/concepts/unity-catalog.md) — Required for model registration in express deployments.

## Sources

- express-deployments-for-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [express-deployments-for-model-serving-endpoints-databricks-on-aws.md](/references/express-deployments-for-model-serving-endpoints-databricks-on-aws-00f4ae5c.md)
