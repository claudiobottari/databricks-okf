---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f87f69e79766169362aa4aabba392941de89ed3cebf0d59b37fc2bd72e696b2
  pageDirectory: concepts
  sources:
    - manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-version-promotion-across-environments
    - MVPAE
    - Model Promotion Across Environments
    - Model promotion across environments
    - Promote a Model Across Environments
    - Promote a model across environments
  citations:
    - file: manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
title: Model Version Promotion Across Environments
description: Copying model versions across registered models in Unity Catalog (e.g., staging to prod) using the copy_model_version API, combined with aliases for deployment tracking.
tags:
  - machine-learning
  - deployment
  - mlops
timestamp: "2026-06-19T19:24:43.804Z"
---

# Model Version Promotion Across Environments

**Model Version Promotion Across Environments** is the practice of moving a model version from one stage of the development pipeline to another—for example, from a staging catalog to a production catalog—so that it can serve traffic in the target environment. In [Unity Catalog](/concepts/unity-catalog.md), promotion is achieved by copying model versions between registered models in different catalogs or schemas, rather than by retraining the model in each environment.

## Overview

Databricks recommends that you deploy ML pipelines as code. This eliminates the need to promote models across environments, as all production models can be produced through automated training workflows in a production environment. However, in some cases, it may be too expensive to retrain models across environments. Instead, you can copy model versions across registered models in Unity Catalog to promote them across environments. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Required Privileges

To promote a model version by copying it, you need the following privileges:

- `USE CATALOG` on both the source and destination catalogs (e.g., `staging` and `prod`).
- `USE SCHEMA` on the source and destination schemas (e.g., `staging.ml_team` and `prod.ml_team`).
- `EXECUTE` on the source registered model (e.g., `staging.ml_team.fraud_detection`).
- Either ownership of the destination registered model or the `CREATE MODEL VERSION` privilege on it. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Promotion Using the Copy API

The promotion workflow uses the `copy_model_version` method from the MLflow Client API, available in MLflow version 2.8.0 and above. The following example copies version 1 of the `staging.ml_team.fraud_detection` model to the `prod.ml_team.fraud_detection` model, then assigns the `Champion` alias to the copied version:

```python
import mlflow
mlflow.set_registry_uri("databricks-uc")
client = mlflow.tracking.MlflowClient()

src_model_name = "staging.ml_team.fraud_detection"
src_model_version = "1"
src_model_uri = f"models:/{src_model_name}/{src_model_version}"
dst_model_name = "prod.ml_team.fraud_detection"

copied_model_version = client.copy_model_version(src_model_uri, dst_model_name)

client.set_registered_model_alias(
    name="prod.ml_team.fraud_detection",
    alias="Champion",
    version=copied_model_version.version
)
```

^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

After the model version is in the production environment, you can perform any necessary pre-deployment validation. Then, you can mark the model version for deployment using [Model Aliases](/concepts/model-aliases.md). In the example above, only users who can read from the `staging.ml_team.fraud_detection` registered model and write to the `prod.ml_team.fraud_detection` registered model can promote staging models to the production environment. The same users can also use aliases to manage which model versions are deployed within the production environment. You don't need to configure any other rules or policies to govern model promotion and deployment. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Customizing Environment Pipelines

You can customize this flow to promote the model version across multiple environments that match your setup, such as `dev`, `qa`, and `prod`. Access control is enforced as configured in each environment. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Limitations

Stages are not supported for models in Unity Catalog. Databricks recommends using the three-level namespace in Unity Catalog to express the environment a model is in, and using aliases to promote models for deployment. See [Promote a model across environments](/concepts/model-version-promotion-across-environments.md) for details. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Model Aliases](/concepts/model-aliases.md) – Mutable named references that indicate deployment status (e.g., "Champion").
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – The system for managing model versions and their lifecycle.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance platform that provides centralized access control for models.
- MLflow Client API – The Python API used to copy and manage model versions.
- copy_model_version API|Copy Model Version – The specific API operation used for promotion.
- Model Version Deployment – The process of making a model version available for serving.

## Sources

- manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md

# Citations

1. [manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md](/references/manage-model-lifecycle-in-unity-catalog-databricks-on-aws-5d1bac95.md)
