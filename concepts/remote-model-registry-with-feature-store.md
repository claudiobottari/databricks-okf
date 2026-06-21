---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e9750a14c301407183651a126e983d64c4ce5d91ae52edd08600846f666f2b11
  pageDirectory: concepts
  sources:
    - share-feature-tables-across-workspaces-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - remote-model-registry-with-feature-store
    - RMRWFS
  citations:
    - file: share-feature-tables-across-workspaces-legacy-databricks-on-aws.md
title: Remote Model Registry with Feature Store
description: Ability to specify a remote model registry URI alongside a remote feature store URI, enabling training models using local or remote feature tables and registering them in local or remote model registries.
tags:
  - databricks
  - mlops
  - model-registry
timestamp: "2026-06-19T23:05:32.478Z"
---

# Remote Model Registry with [Feature Store](/concepts/feature-store.md)

**Remote Model Registry with Feature Store** is a configuration pattern that allows you to train a model using [Feature Tables](/concepts/feature-table.md) from one workspace (the [Feature Store](/concepts/feature-store.md)) and register the model in a different workspace (the model registry), enabling cross-workspace coordination for machine learning lifecycle management.

## Overview

In a multi-workspace Databricks environment, teams may need to separate where feature data is stored from where model artifacts are registered. The [Feature Store](/concepts/feature-store.md) client supports specifying both a remote [Feature Store](/concepts/feature-store.md) and a remote model registry simultaneously, enabling a unified workflow where data sources and model destinations can be in different workspaces. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Configuration

To use both a remote [Feature Store](/concepts/feature-store.md) and a remote model registry, you specify a `feature_store_uri` and a `model_registry_uri` when instantiating the `FeatureStoreClient`. The constructor takes both URIs as separate parameters, allowing you to direct feature operations to one workspace and model registration to another. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

```python
fs = FeatureStoreClient(
    feature_store_uri=f'databricks://<scope>:<prefix>',
    model_registry_uri=f'databricks://<scope>:<prefix>'
)
```

Both URIs follow the same format: `databricks://<scope>:<prefix>`, where `<scope>` is the Databricks secret scope name and `<prefix>` is a unique identifier you created for the remote workspace. ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Workflow

Using `feature_store_uri` and `model_registry_uri`, you can:
- Train a model using any local or remote [Feature Table](/concepts/feature-table.md)
- Register the model in any local or remote model registry

The `FeatureStoreClient` methods that require a registry URI include [`log_model()`](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc) and [`create_training_set()`](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc). ^[share-feature-tables-across-workspaces-legacy-databricks-on-aws.md]

## Prerequisites

Using a remote model registry with a [Feature Store](/concepts/feature-store.md) requires:

- [Feature Store](/concepts/feature-store.md) client v0.3.6 and above.
- Both workspaces must have access to the same raw feature data (shared external Hive [Metastore](/concepts/metastore.md) and DBFS storage).
- If IP access lists are enabled, workspace IP addresses must be on access lists.

## Related Concepts

- Feature Store Client - The client object used for cross-workspace operations
- [Model Registry](/concepts/mlflow-model-registry.md) - The central registry for managing model versions across workspaces
- [Cross-workspace model sharing](/concepts/cross-workspace-feature-sharing.md) - How to share models between different Databricks workspaces
- [Feature Store URI](/concepts/feature-store.md) - The URI format for specifying remote feature stores
- Distributed model registry - Using a centralized model registry with [Feature Store](/concepts/feature-store.md)

## Sources

- share-feature-tables-across-workspaces-legacy-databricks-on-aws.md

# Citations

1. [share-feature-tables-across-workspaces-legacy-databricks-on-aws.md](/references/share-feature-tables-across-workspaces-legacy-databricks-on-aws-144855e9.md)
