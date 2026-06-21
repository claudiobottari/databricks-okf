---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6681795ec7817793d3ea1f11c124bc2011795d31c380eb8aaba2b60d9e335a5d
  pageDirectory: concepts
  sources:
    - manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-migration-and-default-registry-behavior
    - Default Registry Behavior and Unity Catalog Migration
    - UCMADRB
  citations:
    - file: manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md
      start: 8
      end: 15
    - file: 32-35
title: Unity Catalog Migration and Default Registry Behavior
description: Guidance on when and how to use the Workspace Model Registry versus Unity Catalog for model management, including automatic routing based on workspace configuration and explicit registry URI targeting via mlflow.set_registry_uri().
tags:
  - migration
  - unity-catalog
  - databricks
  - mlflow
timestamp: "2026-06-19T19:25:55.848Z"
---

Here is the wiki page for "Unity Catalog Migration and Default Registry Behavior".

---

## Unity Catalog Migration and Default Registry Behavior

**Unity Catalog Migration and Default Registry Behavior** describes the automatic routing of model registration and loading between the [Unity Catalog](/concepts/unity-catalog.md) and the [Workspace Model Registry](/concepts/workspace-model-registry.md) on Databricks. Depending on your workspace's configuration, the default registry used by [MLflow](/concepts/mlflow.md) may change without explicit user action, affecting how models are created, loaded, and served.

### Default Registry Behavior

If your workspace's default catalog is set to a catalog in Unity Catalog (rather than `hive_metastore`), and you are either running a cluster using **Databricks Runtime 13.3 LTS or above** or using [MLflow 3](/concepts/mlflow-3.md), models are automatically created in and loaded from the workspace default catalog. This requires no additional configuration. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md:8-15]

In this scenario, the default registry URI is `databricks-uc`, meaning the MLflow Model Registry in Unity Catalog will be used. To explicitly use the Workspace Model Registry, you must call `mlflow.set_registry_uri("databricks")` at the start of your workload. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md:8-15,32-35]

### Migration from Workspace Model Registry

Databricks has disabled the Workspace Model Registry for workspaces in new accounts where the workspace's default catalog is in Unity Catalog, starting in **April 2024**. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md:8-15]

For guidance on how to upgrade from the Workspace Model Registry to Unity Catalog, see [Migrate workflows and models to Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md). ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md:8-15]

### Exceptions

A small number of workspaces where both the default catalog was configured to a catalog in Unity Catalog **prior to January 2024** and the workspace model registry was used **prior to January 2024** are exempt from this behavior. These workspaces continue to use the Workspace Model Registry by default. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md:8-15]

### Key Concepts

- [Model Registration](/concepts/unity-catalog-model-registration.md) – The process of creating a new model version in a registry.
- [Model Serving](/concepts/model-serving.md) – Exposing MLflow models as REST API endpoints.
- Model Lineage – Chronological tracking of which experiment and run produced a model.
- Model Versioning – Tracking distinct versions of a registered model.
- [Stage Transitions](/concepts/model-versioning-and-stage-transitions.md) – Moving a model version through stages like Staging, Production, and Archived.
- Webhooks – Automated triggers based on registry events.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – The component that manages model lifecycle within Unity Catalog or the Workspace Model Registry.

### Sources

- manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md

# Citations

1. [manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md:8-15](/references/manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws-666e92b6.md)
2. 32-35
