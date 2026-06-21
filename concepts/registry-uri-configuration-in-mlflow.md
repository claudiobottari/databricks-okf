---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0dfb7b69f68c2cab73798990e342426820766c1888589631d3c42daf5ccda18d
  pageDirectory: concepts
  sources:
    - migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - registry-uri-configuration-in-mlflow
    - RUCIM
  citations:
    - file: migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md
title: Registry URI Configuration in MLflow
description: The mechanism of setting the MLflow registry URI to 'databricks' (workspace) or 'databricks-uc' (Unity Catalog) to target different model registries
tags:
  - databricks
  - mlflow
  - configuration
timestamp: "2026-06-19T19:33:53.136Z"
---

# Registry URI Configuration in MLflow

**Registry URI Configuration in MLflow** refers to the setting that determines which model registry backend an MLflow client connects to when performing operations such as registering models, creating model versions, or querying existing model versions. The registry URI is specified via the `registry_uri` parameter when creating an `MlflowClient` instance.

## Overview

MLflow supports multiple model registry backends. The registry URI tells the client which backend to use. Two common registry URIs are:

- `"databricks"` — connects to the **Workspace Model Registry** (the legacy registry that lives within a Databricks workspace).
- `"databricks-uc"` — connects to the **Unity Catalog** registry (the newer, cross-workspace catalog-backed registry).

^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

## Usage

When creating an `MlflowClient`, you pass the `registry_uri` parameter to specify the target registry:

```python
from mlflow import MlflowClient

# Connect to the Workspace Model Registry
workspace_client = MlflowClient(registry_uri="databricks")

# Connect to Unity Catalog
uc_client = MlflowClient(registry_uri="databricks-uc")
```

^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

## Migration Context

The registry URI is a critical configuration when migrating model versions from the Workspace Model Registry to Unity Catalog. During migration, you typically create two clients — one for each registry — and use them to copy model versions from the source (workspace) to the destination (Unity Catalog). ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

For example, the following pattern is used in migration scripts:

```python
workspace_client = MlflowClient(registry_uri="databricks")
uc_client = MlflowClient(registry_uri="databricks-uc")
```

The workspace client reads model versions from the source, and the Unity Catalog client writes them to the destination. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- MlflowClient — The primary client class for interacting with MLflow registries.
- [Workspace Model Registry](/concepts/workspace-model-registry.md) — The legacy model registry within a Databricks workspace.
- [Unity Catalog](/concepts/unity-catalog.md) — The cross-workspace catalog and governance system for data and AI assets.
- Model Version Migration — The process of copying model versions between registries.
- [Model Registry](/concepts/mlflow-model-registry.md) — The central component for managing the lifecycle of MLflow models.

## Sources

- migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md](/references/migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws-d3e98aed.md)
