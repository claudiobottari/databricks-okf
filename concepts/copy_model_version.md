---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d4f124d0a70b8fd5dae9c1baeb99762bdfd16a2df8352a66e12ddf977ab3222
  pageDirectory: concepts
  sources:
    - migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy_model_version
    - Copy Model Version
    - Model Version
    - Model version
    - copy_model_version()
    - model version
  citations:
    - file: migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md
title: copy_model_version()
description: An MLflow API function (≥3.4.0) that copies a model version from the Workspace Model Registry to a destination Unity Catalog model, creating the destination model if it doesn't exist.
tags:
  - mlflow
  - migration
  - api
timestamp: "2026-06-19T19:35:43.804Z"
---

# `copy_model_version()`

`copy_model_version()` is an [MLflow](/concepts/mlflow.md) client method used to copy a model version from the [Databricks Workspace Model Registry](/concepts/workspace-model-registry.md) to a destination model in [Unity Catalog](/concepts/unity-catalog.md). It is part of the migration workflow that Databricks recommends for moving models from the workspace registry to Unity Catalog for improved governance, sharing, and lifecycle management. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Overview

The function accepts a source model version URI (in the form `models:/<workspace_model_name>/<version>`) and a fully qualified Unity Catalog model identifier (`catalog.schema.model_name`). If the destination Unity Catalog model does not exist, the API call creates it automatically. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Usage

To use `copy_model_version()`, the MLflow client must be ≥ 3.4.0, and the registry URI must be set to the workspace registry (`"databricks"`). A typical invocation looks like: ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

```python
import mlflow
from mlflow import MlflowClient

# Registry must be set to workspace registry
mlflow.set_registry_uri("databricks")
client = MlflowClient(registry_uri="databricks")

src_model_uri = "models:/my_wmr_model/1"
uc_migrated_copy = client.copy_model_version(
    src_model_uri,
    "mycatalog.myschema.my_uc_model"
)
```

## Signature requirements

Models in Unity Catalog require a [model signature](https://mlflow.org/docs/latest/ml/model/signatures/). If the workspace model version lacks a signature, Databricks recommends creating one. As an alternative, the environment variable `MLFLOW_SKIP_SIGNATURE_CHECK_FOR_UC_REGISTRY_MIGRATION` can be set to `"true"` to bypass the signature requirement. This environment variable works **only** with `copy_model_version()` and requires MLflow ≥ 3.4.0. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Batch migration

For migrating all versions of a workspace model to a destination Unity Catalog model, Databricks provides a ready-to-use script described in [Migrate model versions from Workspace Model Registry to Unity Catalog](/concepts/databricks-model-registry-with-unity-catalog.md). ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## See also

- [Unity Catalog](/concepts/unity-catalog.md) – The governance and catalog layer for Databricks.
- [Workspace Model Registry](/concepts/workspace-model-registry.md) – The legacy model registry that models are migrated from.
- [MLflow](/concepts/mlflow.md) – The open-source framework managing the model lifecycle.
- Model version – An immutable snapshot of a registered model.
- [Migrate workflows and models to Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md) – The full migration guide.

## Sources

- migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md](/references/migrate-workflows-and-models-to-unity-catalog-databricks-on-aws-ef30b915.md)
