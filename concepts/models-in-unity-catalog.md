---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d446f61fe1f754e36a8c2ad11cd7d63726adfee51369479f717b05751b31f5fc
  pageDirectory: concepts
  sources:
    - manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
    - migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md
    - share-models-across-workspaces-databricks-on-aws.md
    - workspace-model-registry-example-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - models-in-unity-catalog
    - MIUC
    - Model Aliases in Unity Catalog
    - Model Versions in Unity Catalog
    - Foundation Models in Unity Catalog
    - MLflow Models in Unity Catalog
    - Registered Models in Unity Catalog
    - Registered model (Unity Catalog)
    - registered model in Unity Catalog
  citations:
    - file: manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
    - file: workspace-model-registry-example-databricks-on-aws.md
    - file: share-models-across-workspaces-databricks-on-aws.md
    - file: migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md
title: Models in Unity Catalog
description: Databricks' integration of MLflow Model Registry with Unity Catalog for centralized model management, access control, auditing, and lineage.
tags:
  - machine-learning
  - model-registry
  - unity-catalog
timestamp: "2026-06-19T19:24:21.079Z"
---

# Models in Unity Catalog

Models in Unity Catalog is Databricks' hosted version of the MLflow Model Registry integrated with Unity Catalog. It extends Unity Catalog's governance capabilities to machine learning models, providing centralized access control, auditing, lineage tracking, and model discovery across workspaces.^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Overview

Models in Unity Catalog is compatible with the open-source MLflow Python client and serves as the recommended approach for managing the full lifecycle of ML models on Databricks. It replaces the older Workspace Model Registry, which will be deprecated in the future.^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md, workspace-model-registry-example-databricks-on-aws.md]

For an overview of Model Registry concepts, see [MLflow on Databricks](/concepts/mlflow-on-databricks.md).

## Key Benefits

Models in Unity Catalog provides several advantages over the workspace model registry:

- **Centralized access control** using Unity Catalog's unified permission model
- **Auditing** through Unity Catalog audit logs
- **Lineage tracking** from models to upstream datasets
- **Model sharing and discovery** across workspaces
- **Cross-workspace access** — models can be accessed from any workspace attached to the same [Metastore](/concepts/metastore.md)

^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md, share-models-across-workspaces-databricks-on-aws.md]

## Requirements

To use Models in Unity Catalog, the following requirements must be met:

- Unity Catalog must be enabled in the workspace. See Get started using Unity Catalog.
- Compute resources must have access to Unity Catalog, with an access mode of **Dedicated** (formerly single user). Databricks Runtime 15.4 LTS ML and above also supports [dedicated group access mode](/concepts/dedicated-access-mode-for-ml-compute.md).
- To create new registered models, the following privileges are required:
  - `USE SCHEMA` and `USE CATALOG` privileges on the schema and its enclosing catalog
  - `CREATE MODEL` or `CREATE FUNCTION` privilege on the schema

For Databricks on AWS GovCloud, the environment variable `MLFLOW_USE_DATABRICKS_SDK_MODEL_ARTIFACTS_REPO_FOR_UC` must be set to `True`.^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Model Namespace

Models in Unity Catalog use a three-level naming convention in the format `<catalog>.<schema>.<model>`. This replaces the simple model names used in the workspace model registry.^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Training and Registering Models

### Register a Model

Models can be registered using the MLflow Client API `register_model()` method, passing the three-level model name:

```python
import mlflow

mlflow.set_registry_uri("databricks-uc")
mlflow.register_model(model_uri, "catalog.schema.model_name")
```

^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

### Model Signature Requirement

All new ML model versions in Unity Catalog must include a model signature. Model versions without signatures have limitations, including:
- No automatic input enforcement at inference
- No schema auto-generation when using [AI Functions](/concepts/ai-functions.md)
- No auto-generated input examples with [Model Serving](/concepts/model-serving.md)

Signatures can be provided through [Databricks Autologging](/concepts/databricks-autologging.md), input examples, or explicit specification.^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

### Register via the UI

From an experiment run page, click **Register model**, select **Unity Catalog**, choose a destination model from the dropdown, and click **Register**.^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Model Aliases

Model aliases replace the stage-based system (None, Staging, Production, Archived) used in the workspace model registry. Aliases are mutable, named references assigned to a particular model version. Up to 10 custom aliases can be created per model.^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md, migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

Common use cases include assigning a "Champion" alias to the production model version and updating it as new versions are promoted.

### Setting Aliases

```python
from mlflow import MlflowClient

client = MlflowClient()
client.set_registered_model_alias("catalog.schema.model", "Champion", 1)
```

### Loading Models by Alias

```python
import mlflow.pyfunc

model_uri = "models:/catalog.schema.model@Champion"
model = mlflow.pyfunc.load_model(model_uri)
```

^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Access Control

In Unity Catalog, registered models are a subtype of the `FUNCTION` securable object. Permissions are granted using `GRANT ON FUNCTION` SQL commands or through Catalog Explorer. All actions require `USE CATALOG` and `USE SCHEMA` privileges on the enclosing [Catalog and Schema](/concepts/catalog-and-schema.md).

Key permissions include:
- `EXECUTE` — Load and use a model version
- `CREATE MODEL VERSION` — Create new versions under a registered model
- Ownership — Full control, including deletion

Programmatic permission management is available through the Grants REST API with `securable_type` set to `"FUNCTION"`.^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Data Lineage

When training a model on a Unity Catalog table, lineage can be tracked from the model to its upstream datasets using `mlflow.log_input()`. This saves input table information with the [MLflow Run](/concepts/mlflow-run.md) that generated the model. Lineage information is automatically saved when registering the model to Unity Catalog and is visible in the **Lineage** tab on the model version page in Catalog Explorer.

Data lineage is also automatically captured for models logged using [feature store APIs](/concepts/feature-store.md).^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Managing Models

### Viewing Models

Models can be viewed and managed using Catalog Explorer. Navigate to a [Catalog and Schema](/concepts/catalog-and-schema.md) — if the schema contains models, they appear in the tree under **Models**. Clicking a model displays its details page with a list of model versions.^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

### Tags

Tags are key-value pairs that can be associated with registered models and model versions for labeling and categorization. Up to 50 tags are allowed per object. Tags are set using MLflow client APIs or through the Catalog Explorer UI.

```python
client.set_registered_model_tag("catalog.schema.model", "task", "classification")
```

^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

### Descriptions

Text descriptions can be added to both registered models and model versions. AI-generated comments are also available for models.

```python
client.update_registered_model(
    name="catalog.schema.model",
    description="This model forecasts power output."
)
```

^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

### Renaming Models

```python
client.rename_registered_model("catalog.schema.model", "new_model_name")
```

Note that only the model name (without catalog or schema) can be changed.^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

### Copying Model Versions

Model versions can be copied between registered models in Unity Catalog, which enables promotion across environments such as `staging` to `prod`.

```python
client.copy_model_version(
    "models:/staging.schema.model/1",
    "prod.schema.model"
)
```

^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

### Deleting Models

Model versions and entire registered models can be deleted using the UI or API. Deletion is permanent and cannot be undone.

```python
client.delete_model_version(name="catalog.schema.model", version=1)
client.delete_registered_model(name="catalog.schema.model")
```

^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Listing and Searching Models

```python
mlflow.search_registered_models()
mlflow.search_model_versions("name='catalog.schema.model'")
```

Note that search API support has some limitations — the `order_by` parameter and tag-based filters are not supported for Unity Catalog models.^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Cross-Workspace Access

Models in Unity Catalog can be accessed from any workspace attached to the same [Metastore](/concepts/metastore.md), provided the user has appropriate privileges. To share models with users in other regions or accounts, use the OpenSharing Databricks-to-Databricks sharing flow.^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Migrating from Workspace Model Registry

Databricks recommends migrating models from the Workspace Model Registry to Unity Catalog. Key differences include:

| Workspace Registry | Unity Catalog |
|---|---|
| Stages (None, Staging, Production, Archived) | Aliases (up to 10 custom) and tags |
| Workspace-level permissions | Account-level Unity Catalog permissions |
| Email notifications | Deployment job notifications |

Model versions can be migrated using `copy_model_version()` with MLflow client version 3.4.0 or above.^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Limitations

- Stages (from the workspace model registry) are not supported — use aliases and the three-level namespace instead.
- Webhooks are not supported — use model event job triggers (in Private Preview) as an alternative.
- Some search API fields and operators are not supported, including `order_by` and tag-based filters.
- Email notifications and comment discussion threads are not supported.
- The activity log is not supported — use audit logs instead.
- `search_registered_models` may return stale results for models shared through OpenSharing.

^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [MLflow on Databricks](/concepts/mlflow-on-databricks.md)
- [Workspace Model Registry](/concepts/workspace-model-registry.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow 3](/concepts/mlflow-3.md)
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- [Model Serving](/concepts/model-serving.md)
- [Feature Governance and Lineage](/concepts/feature-governance-and-lineage.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- Audit logs

## Sources

- manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
- migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md
- share-models-across-workspaces-databricks-on-aws.md
- workspace-model-registry-example-databricks-on-aws.md

# Citations

1. [manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md](/references/manage-model-lifecycle-in-unity-catalog-databricks-on-aws-5d1bac95.md)
2. [workspace-model-registry-example-databricks-on-aws.md](/references/workspace-model-registry-example-databricks-on-aws-fa952b3f.md)
3. [share-models-across-workspaces-databricks-on-aws.md](/references/share-models-across-workspaces-databricks-on-aws-bd976522.md)
4. [migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md](/references/migrate-workflows-and-models-to-unity-catalog-databricks-on-aws-ef30b915.md)
