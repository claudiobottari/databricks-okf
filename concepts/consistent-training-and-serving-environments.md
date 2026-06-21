---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4bded1c2f874224defd88bb219abb152170f86a4f38ebb318144c649cf549eba
  pageDirectory: concepts
  sources:
    - express-deployments-for-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - consistent-training-and-serving-environments
    - Serving Environments and Consistent Training
    - CTASE
  citations:
    - file: express-deployments-for-model-serving-endpoints-databricks-on-aws.md
title: Consistent Training and Serving Environments
description: A key benefit of express deployments where the model serving environment matches the training environment, avoiding divergence issues common in non-express deployments.
tags:
  - machine-learning
  - mlops
  - databricks
timestamp: "2026-06-18T12:17:13.146Z"
---

# Consistent Training and Serving Environments

**Consistent Training and Serving Environments** refers to the practice of ensuring that the runtime environment used during model training matches the environment used during model deployment and serving. This consistency helps guarantee that model behavior remains stable when transitioning from development to production, reducing the risk of unexpected failures or performance degradation caused by environmental differences.

## Overview

Machine learning models are typically trained in a specific environment with particular software dependencies, library versions, and hardware configurations. When these models are deployed to a serving endpoint, inconsistencies between the training and serving environments can lead to issues such as dependency conflicts, runtime errors, or divergent model outputs. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

Maintaining consistent environments is a key goal of the MLflow model management lifecycle, and Databricks supports this through features like [Express deployments](/concepts/express-deployments-databricks.md) (also known as serverless optimized deployments), which package the model's training environment alongside the model artifacts during registration to ensure that the same environment is used at serving time. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## How Consistency is Achieved

### Environment Packaging

During model registration, if the `env_pack` parameter is set (for example, using `EnvPackConfig(name="databricks_model_serving")`), the model's training environment is captured and staged for deployment. This includes all dependencies, library versions, and runtime configurations used during training. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

```python
import mlflow
from mlflow.utils.env_pack import EnvPackConfig

mlflow.register_model(
    model_info.model_uri,
    model_name,
    env_pack=EnvPackConfig(name="databricks_model_serving")
)
```

The `install_dependencies` parameter (default `True`) determines whether the model's dependencies are installed in the current environment during registration to validate that the environment is usable. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### Serverless Notebook Environments

Consistency relies on the model being logged and registered in a [Serverless Notebook](/concepts/serverless-notebook-environments.md) environment with client version 3 or 4 and `mlflow>=3.1`. These environments are designed to be reproducible and consistent across training and serving phases. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Benefits

- **Reduced deployment time**: Since the environment is already packaged during registration, deployment does not require building a new container from scratch.
- **Elimination of runtime errors**: Environmental mismatches (e.g., missing or conflicting dependencies) are avoided.
- **Predictable model behavior**: The model runs in the same conditions under which it was validated during training. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Requirements

- The model must be a custom model (not using [Foundation Model APIs](/concepts/foundation-model-apis.md)).
- The model must be logged and registered using [Serverless Notebook](/concepts/serverless-notebook-environments.md) with client version 3 or 4.
- The model must be registered with `mlflow>=3.1`.
- The model must be registered in [Unity Catalog](/concepts/unity-catalog.md) and served with CPU.
- The model's maximum environment size is 1 GB. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Express Deployments](/concepts/express-deployments-databricks.md) – The mechanism that packages training environments for serving
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – The endpoints where consistent environments are deployed
- [Serverless Notebook](/concepts/serverless-notebook-environments.md) – The environment that provides the runtime for model training
- MLflow Model Registration – The process that packages environment and model artifacts
- Dependency Management – Ensuring library versions match between environments

## Sources

- express-deployments-for-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [express-deployments-for-model-serving-endpoints-databricks-on-aws.md](/references/express-deployments-for-model-serving-endpoints-databricks-on-aws-00f4ae5c.md)
