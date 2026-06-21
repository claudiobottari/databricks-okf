---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3514fed6697359ccc284f87c5877a73a978b135c7839b4d2d5a5f0a70e1e1337
  pageDirectory: concepts
  sources:
    - manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-tags-in-unity-catalog
    - MTIUC
    - Tags in Unity Catalog
  citations:
    - file: manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
title: Model Tags in Unity Catalog
description: Key-value pairs applied to registered models and model versions for labeling and categorization, managed via MLflow Client API or Catalog Explorer.
tags:
  - machine-learning
  - metadata
  - unity-catalog
timestamp: "2026-06-19T19:25:41.888Z"
---

# Model Tags in Unity Catalog

**Model Tags in Unity Catalog** are key-value pairs that you can associate with both registered models and individual model versions, enabling you to label and categorize them by function, status, or any other attribute relevant to your ML workflow. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Overview

Tags provide a flexible way to organize and identify models without relying on naming conventions or directory structures. For example, you could apply a tag with key `"task"` and value `"question-answering"` to registered models intended for question-answering tasks. At the model version level, you could tag versions undergoing pre-deployment validation with `validation_status:pending` and those cleared for deployment with `validation_status:approved`. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

Both registered model tags and model version tags must meet the platform-wide Unity Catalog tag constraints. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Permissions Required

To manage tags on a registered model or model version, you must be the owner of the registered model or have the `APPLY TAG` privilege on it. You also need `USE SCHEMA` and `USE CATALOG` privileges on the schema and catalog containing the model. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Managing Tags in the UI

You can set and delete tags using Catalog Explorer. See Apply tags to Unity Catalog securable objects for detailed instructions on using the UI. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Managing Tags Using the MLflow Client API

### Setting and Deleting Registered Model Tags

Use the `set_registered_model_tag()` and `delete_registered_model_tag()` methods from the MLflow Client API: ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

```python
from mlflow import MlflowClient

client = MlflowClient()

# Set registered model tag
client.set_registered_model_tag("prod.ml_team.iris_model", "task", "classification")

# Delete registered model tag
client.delete_registered_model_tag("prod.ml_team.iris_model", "task")
```

### Setting and Deleting Model Version Tags

Use the `set_model_version_tag()` and `delete_model_version_tag()` methods: ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

```python
from mlflow import MlflowClient

client = MlflowClient()

# Set model version tag
client.set_model_version_tag("prod.ml_team.iris_model", "1", "validation_status", "approved")

# Delete model version tag
client.delete_model_version_tag("prod.ml_team.iris_model", "1", "validation_status")
```

## Use Cases

- **Functional categorization**: Tag models by the type of task they perform (e.g., `task:classification`, `task:question-answering`). ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]
- **Deployment status tracking**: Use tags to indicate a model version's readiness for deployment (e.g., `validation_status:pending`, `validation_status:approved`). ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]
- **Environment management**: Identify which environment a model version belongs to alongside the three-level namespace and [Model Aliases](/concepts/model-aliases.md). ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Model Aliases in Unity Catalog](/concepts/models-in-unity-catalog.md) — An alternative method for marking model versions for deployment
- Unity Catalog Tag Constraints — Platform-wide constraints that tags must satisfy
- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md) — The securable objects hierarchy that includes registered models
- MLflow Client API — The API used for programmatic tag management
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI for viewing and managing Unity Catalog objects
- [Registered Models in Unity Catalog](/concepts/models-in-unity-catalog.md) — The broader model management lifecycle
- [Model Versions in Unity Catalog](/concepts/models-in-unity-catalog.md) — Individual iterations of a registered model

## Sources

- manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md

# Citations

1. [manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md](/references/manage-model-lifecycle-in-unity-catalog-databricks-on-aws-5d1bac95.md)
