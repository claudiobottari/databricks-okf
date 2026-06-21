---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0ab9a2550b9cf1a7db44937dc37347528ed2e8854f1fd1cf83ef6d25083b568e
  pageDirectory: concepts
  sources:
    - migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alias-based-model-lifecycle-in-unity-catalog
    - AMLIUC
    - Manage model lifecycle in Unity Catalog
  citations:
    - file: migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md
title: Alias-based model lifecycle in Unity Catalog
description: Replacement for fixed stages (Staging, Production, etc.) in the Workspace Model Registry — up to 10 custom, reassignable aliases can be used to reference specific model versions.
tags:
  - machine-learning
  - unity-catalog
  - mlops
timestamp: "2026-06-19T19:36:01.475Z"
---

# Alias-based Model Lifecycle in Unity Catalog

**Alias-based model lifecycle in Unity Catalog** replaces the fixed-stage system of the Workspace Model Registry with a flexible, alias-driven approach for managing model version transitions. Instead of four predefined stages (e.g., `Staging`, `Production`), Unity Catalog allows you to create up to 10 custom, reassignable aliases per model.

## Overview

When you migrate models from the [Workspace Model Registry](/concepts/workspace-model-registry.md) to [Unity Catalog](/concepts/unity-catalog.md), the concept of stages is replaced by aliases and tags. Aliases are used for calling a specific model version, while tags are used for labeling models. This design provides greater flexibility in managing the model lifecycle and accommodates more complicated workflows than the fixed-stage system. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Aliases vs. Stages

The Workspace Model Registry used four fixed stages (`None`, `Staging`, `Production`, `Archived`) to track model lifecycle. In Unity Catalog:

- **Aliases** replace stages for calling models. You can create up to 10 custom, reassignable aliases per model, such as `"Production"`, `"Staging"`, `"Canary"`, or any other name. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]
- **Tags** replace stage labels for labeling model versions. You can use tags like `"Production"`, `"Staging"`, or `"Archived"`, and any other custom labels you prefer. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

### Key Differences

A critical distinction from the Workspace Model Registry is that in Unity Catalog, an alias is assigned to a **unique model version**. In the Workspace Model Registry, multiple model versions could be in the same stage, and the latest version was called when referenced. In Unity Catalog, an alias points to exactly one version, providing unambiguous version references. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Lifecycle Management with Deployment Jobs

While the Workspace Model Registry tracked model lifecycle through stages with human approval for transition requests, Unity Catalog manages model version lifecycle through [MLflow 3 Deployment Jobs](/concepts/mlflow-3-deployment-jobs.md). Each task in a deployment job corresponds to a stage. Deployment jobs allow you to customize the model lifecycle and accommodate more complicated workflows, while still supporting human approvals. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

A deployment job can be configured to automatically trigger whenever a new model version is created, automating the evaluation, approval, and deployment workflow. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

### Aliases and Deployment Jobs

When creating a deployment job, aliases can be defined at each task to control which model version is promoted. The deployment job manages the lifecycle of model versions across aliases, replacing the manual stage-transition workflow from the Workspace Model Registry. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Migrating Stages to Aliases and Tags

For simple migration of Workspace Model Registry stages to Unity Catalog:

1. **Use alias names** directly as `"Production"` and `"Staging"` or other preferred names. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]
2. **Use tags** to label model versions as `"Production"`, `"Staging"`, or `"Archived"`. Tags support any custom labels. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

### Tag Limitations

In Catalog Explorer, you can use tags only to search for models, not model versions. The MLflow client does not support searching for models by Unity Catalog tags. Unity Catalog also allows at most 50 tags per object. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Permissions in the Alias-based Model Lifecycle

Instead of Workspace Model Registry permissions, Unity Catalog uses account-level [Unity Catalog permissions](/concepts/unity-catalog-permissions-model.md) with a unified permission model. All actions require `USE CATALOG` and `USE SCHEMA` privileges in addition to model-specific privileges. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for models and data assets.
- [MLflow 3 Deployment Jobs](/concepts/mlflow-3-deployment-jobs.md) — Automation for model lifecycle management.
- [Workspace Model Registry](/concepts/workspace-model-registry.md) — The legacy model registry being migrated from.
- [Model Aliases in Unity Catalog](/concepts/models-in-unity-catalog.md) — Custom, reassignable references to model versions.
- [Model Tags in Unity Catalog](/concepts/model-tags-in-unity-catalog.md) — Labels for searching and organizing models.
- [Unity Catalog Permissions](/concepts/unity-catalog-permissions-model.md) — The permission model governing model access.

## Sources

- migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md](/references/migrate-workflows-and-models-to-unity-catalog-databricks-on-aws-ef30b915.md)
