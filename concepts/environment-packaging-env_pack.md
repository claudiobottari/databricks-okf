---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5237b62b7bba6e80b632fc4979af80dc3c3da9e705813354625d6228c8f9431f
  pageDirectory: concepts
  sources:
    - express-deployments-for-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - environment-packaging-env_pack
    - EP(
  citations:
    - file: express-deployments-for-model-serving-endpoints-databricks-on-aws.md
title: Environment Packaging (env_pack)
description: A mechanism in MLflow's register_model function that packages and stages model artifacts along with the serverless notebook environment during model registration, enabling express deployments.
tags:
  - mlflow
  - model-registration
  - databricks
  - deployment
timestamp: "2026-06-19T10:28:08.457Z"
---

# Environment Packaging (env_pack)

**Environment Packaging (env_pack)** is a feature in MLflow that enables packaging and staging of model artifacts and their serving environment during model registration, rather than at deployment time. This approach powers [express deployments for model serving endpoints](/concepts/express-deployments-for-model-serving.md) by decoupling the environment preparation step from endpoint creation.

## Overview

When a model is registered with `env_pack`, the system packages the model artifacts and the [serverless notebook](/concepts/serverless-notebook-environments.md) environment at registration time. This differs from non-express deployments, where model artifacts and environments are packaged into containers at deployment time. By packaging the environment upfront, the serving environment is guaranteed to match the one used during model training.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Prerequisites

For `env_pack` to function, the following requirements must be met:

- The model must be a custom model (not an FMAPI foundational model)
- The model must be logged and registered in a [serverless notebook](/concepts/serverless-notebook-environments.md) using environment version 3 or 4
- The model must be logged and registered with `mlflow>=3.1`
- The model must be registered in [Unity Catalog](/concepts/unity-catalog.md) and served with CPU
- The model's maximum environment size is 1GB

^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Usage

To use `env_pack` when registering a model, set the `env_pack` parameter in `mlflow.register_model()`:^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

```python
import mlflow
from mlflow.utils.env_pack import EnvPackConfig

mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack=EnvPackConfig(name="databricks_model_serving")
)
```

### EnvPackConfig Parameters

`EnvPackConfig` has the following parameters:

- **name**: Specifies the packaging configuration. The shorthand `"databricks_model_serving"` can be used as a substitute for `EnvPackConfig(name="databricks_model_serving", install_dependencies=True)`.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- **install_dependencies** (default `True`): Determines whether the model's dependencies are installed in the current environment to confirm the environment is valid. If set to `False`, the dependency installation step is skipped.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Considerations

- Adding `env_pack` may take additional time during model registration compared to registering without it.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- Endpoints in workspaces without internet access, or endpoints with dependencies on custom libraries, may fail if `install_dependencies` is set to `True`. In these cases, set `install_dependencies` to `False`.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Benefits

After registration with `env_pack` completes, deployment times are reduced and the event logs no longer indicate container build steps, as the environment is already prepared.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Express deployments for model serving endpoints](/concepts/express-deployments-for-model-serving.md)
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md)
- [Serverless Notebook Environments](/concepts/serverless-notebook-environments.md)
- MLflow model registration
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- express-deployments-for-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [express-deployments-for-model-serving-endpoints-databricks-on-aws.md](/references/express-deployments-for-model-serving-endpoints-databricks-on-aws-00f4ae5c.md)
