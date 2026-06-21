---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 34c8eb5a22a46db719e77824fc5d593dfe78f57d9ad9e47da7133cae837746f0
  pageDirectory: concepts
  sources:
    - express-deployments-for-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - express-deployments-for-model-serving
    - EDFMS
    - Express Deployments for Model Serving Endpoints
    - Express deployments for model serving endpoints
    - express deployments for model serving endpoints
  citations:
    - file: express-deployments-for-model-serving-endpoints-databricks-on-aws.md
title: Express Deployments for Model Serving
description: A Databricks feature that packages and stages model artifacts during model registration to dramatically reduce endpoint deployment times and maintain environment consistency between training and serving.
tags:
  - machine-learning
  - model-serving
  - deployment
timestamp: "2026-06-19T18:46:29.781Z"
---

# Express Deployments for Model Serving

**Express Deployments** (previously called *serverless optimized deployments*) are a feature of [Model Serving](/concepts/model-serving.md) on Databricks that dramatically reduce model deployment time and ensure the serving environment matches the training environment. They achieve this by packaging and staging model artifacts in [Serverless Notebook](/concepts/serverless-notebook-environments.md) environments during model registration, rather than at deployment time. This contrasts with non-express deployments, where artifacts and environments are packaged into containers at deployment time, potentially causing discrepancies between training and serving environments. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Requirements

Express deployment endpoints have the same general requirements as any model serving endpoint. Additionally, the following conditions must be met:

- The model must be a custom model (not a [Foundation Model APIs](/concepts/foundation-model-apis.md) model). ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- The model must be logged and registered from a Serverless Notebook using environment client version 3 or 4. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- The model must be logged and registered with `mlflow>=3.1`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- The model must be registered in [Unity Catalog](/concepts/unity-catalog.md) and served with CPU only. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- The model's maximum environment size is 1 GB. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Usage

To use express deployments, register the model with the `env_pack` parameter set to the appropriate configuration. The following Python example demonstrates the process: ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

```python
import mlflow
from mlflow.utils.env_pack import EnvPackConfig

mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack=EnvPackConfig(name="databricks_model_serving")
)
```

Passing `env_pack` makes the function pack and stage the model artifacts and Serverless Notebook environment during registration, preparing them for deployment. This may take additional time compared to registering a model without `env_pack`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

`EnvPackConfig` accepts a parameter `install_dependencies` (default `True`) that determines whether the model's dependencies are installed in the current environment to confirm the environment is valid. To skip this validation step, set `install_dependencies` to `False`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

You can also use the shorthand string `"databricks_model_serving"` in place of `EnvPackConfig(name="databricks_model_serving", install_dependencies=True)`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Important Notes

- Endpoints in workspaces **without internet access** or endpoints with dependencies on **custom libraries** may fail if `install_dependencies` is set to `True`. In such cases, set `install_dependencies` to `False`. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]
- After registering the model with express deployment support, you can deploy it to a serving endpoint as usual. The deployment time is reduced, and the endpoint event logs no longer indicate a container build, confirming that express deployment was used. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md)
- [Serverless Notebook](/concepts/serverless-notebook-environments.md)
- [MLflow](/concepts/mlflow.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Serving Endpoint
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md)

## Sources

- express-deployments-for-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [express-deployments-for-model-serving-endpoints-databricks-on-aws.md](/references/express-deployments-for-model-serving-endpoints-databricks-on-aws-00f4ae5c.md)
