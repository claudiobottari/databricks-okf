---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e483185306bb586a8bed7ca54a2b0c7165301c04c4b75d4542db52038929d1ba
  pageDirectory: concepts
  sources:
    - express-deployments-for-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - env_pack-parameter
  citations:
    - file: express-deployments-for-model-serving-endpoints-databricks-on-aws.md
title: env_pack Parameter
description: A parameter used with mlflow.register_model() to trigger packaging of model artifacts and the serverless notebook environment during model registration for express deployments.
tags:
  - mlflow
  - parameter
  - model-registration
timestamp: "2026-06-19T18:46:42.163Z"
---

```markdown
---
title: env_pack Parameter
summary: An MLflow parameter used during model registration to enable express deployments by packing and staging environment artifacts for accelerated endpoint deployment.
sources:
  - express-deployments-for-model-serving-endpoints-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:17:00.519Z"
updatedAt: "2026-06-18T12:17:00.519Z"
tags:
  - mlflow
  - configuration
  - databricks
aliases:
  - env_pack-parameter
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# env_pack Parameter

The **env_pack Parameter** is an argument passed to `mlflow.register_model()` that enables **express deployments** (formerly called serverless optimized deployments) for model serving endpoints. When set, it packages and stages the model artifacts together with the serverless notebook environment at registration time, allowing faster deployment and ensuring that the serving environment matches the training environment. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Usage

To use the `env_pack` parameter, register a model that was logged and registered in a [[Serverless Notebook Environments|Serverless Notebook]] with client version 3 or 4 and `mlflow>=3.1`. Pass an `EnvPackConfig` object—or its shorthand—to the `env_pack` argument of `mlflow.register_model()`: ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

```python
import mlflow
from mlflow.utils.env_pack import EnvPackConfig

mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack=EnvPackConfig(name="databricks_model_serving")
)
```

When `env_pack` is provided, the function packages the model artifacts and the serverless notebook environment during registration. This may take additional time compared to a registration without `env_pack`, but the deployment step later becomes faster because the container image is pre-built. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## EnvPackConfig

`EnvPackConfig` accepts the following fields:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `name` | `str` | required | The deployment target name. Currently must be `"databricks_model_serving"`. |
| `install_dependencies` | `bool` | `True` | If `True`, installs the model’s dependencies in the current environment to confirm that the environment is valid before packaging. |

^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### Notes on `install_dependencies`

Setting `install_dependencies=True` (the default) verifies that the environment can be reproduced. However, endpoints in workspaces without internet access, or endpoints with dependencies on custom libraries, may fail during installation. In such cases, set `install_dependencies` to `False` to skip the validation step. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Shorthand

A shorthand string `"databricks_model_serving"` can be used instead of `EnvPackConfig(...)`. This is equivalent to `EnvPackConfig(name="databricks_model_serving", install_dependencies=True)`: ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

```python
mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack="databricks_model_serving"
)
```

## Requirements for the Model

For the `env_pack` parameter to function correctly and produce an express deployment, the model must meet these additional requirements: ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

- The model must be a custom model (not a Foundation Model API model).
- The model must be logged and registered in a [[Serverless Notebook Environments|Serverless Notebook]] using client version 3 or 4.
- The model must be logged and registered with `mlflow>=3.1`.
- The model must be registered in [[Unity Catalog]] and served with CPU.
- The model’s maximum environment size must be 1 GB.

## Related Concepts

- [[Express Deployments for Model Serving|Express Deployments for Model Serving Endpoints]] – The broader feature that `env_pack` enables.
- [[Model Serving Endpoint|Model Serving Endpoints]] – The serving infrastructure where deployed models are hosted.
- MLflow Model Registration – The process of registering a model in the MLflow Model Registry.
- [[Serverless Notebook Environments|Serverless Notebooks]] – The compute environment required for models to use express deployments.

## Sources

- express-deployments-for-model-serving-endpoints-databricks-on-aws.md
```

# Citations

1. [express-deployments-for-model-serving-endpoints-databricks-on-aws.md](/references/express-deployments-for-model-serving-endpoints-databricks-on-aws-00f4ae5c.md)
