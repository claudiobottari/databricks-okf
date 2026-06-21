---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 168c0334f35286dc5892431df4021b384bc08dd50083a8b6f865be4439cb7dbe
  pageDirectory: concepts
  sources:
    - manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-model-registry-unity-catalog
    - MMR(C
  citations:
    - file: manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
title: MLflow Model Registry (Unity Catalog)
description: Databricks' hosted version of the open-source MLflow Model Registry, integrated with Unity Catalog, using the 'databricks-uc' registry URI and three-level naming (catalog.schema.model).
tags:
  - machine-learning
  - mlflow
  - model-registry
timestamp: "2026-06-19T19:25:06.107Z"
---

# MLflow Model Registry (Unity Catalog)

The **MLflow Model Registry (Unity Catalog)** is a hosted, Unity Catalog–native version of the MLflow Model Registry provided by Databricks. It extends Unity Catalog's governance capabilities — centralised access control, auditing, lineage, and cross-workspace discovery — to machine learning models, and is compatible with the open‑source MLflow Python client. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

MLflow 3 introduces significant enhancements, including the ability for models to directly capture parameters and metrics and make them available across all workspaces and experiments. The default registry URI in MLflow 3 is `databricks-uc`, meaning the Model Registry in Unity Catalog is used automatically. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Overview

Models are registered under a three‑level namespace: `<catalog>.<schema>.<model_name>`. This structure ties each model to a specific [Catalog and Schema](/concepts/catalog-and-schema.md), inheriting Unity Catalog’s access‑control policies. The registry supports version management, aliases (mutable, named references to versions), tags, descriptions, and lineage tracking. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

For workspaces where Unity Catalog is not enabled, Databricks provides a separate [Workspace Model Registry](/concepts/workspace-model-registry.md).

## Requirements

- Unity Catalog must be enabled in the workspace. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]
- Compute resources must have access to Unity Catalog; for ML workloads the access mode must be **Dedicated** (single user). With Databricks Runtime 15.4 LTS ML and above, dedicated group access mode is also supported. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]
- To create new registered models, you need `USE CATALOG`, `USE SCHEMA`, and `CREATE MODEL` (or `CREATE FUNCTION`) privileges on the enclosing [Catalog and Schema](/concepts/catalog-and-schema.md).
- New model versions must have a model signature. Signatures can be automatically inferred using an input example (MLflow 2.5.0+) or via Databricks autologging. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Setup

Support for models in Unity Catalog is included in Databricks Runtime 13.2 ML and above. On older runtimes (11.3 LTS ML+), install the latest MLflow Python client:

```python
%pip install --upgrade "mlflow-skinny[databricks]"
dbutils.library.restartPython()
```

If the workspace’s default catalog is not in Unity Catalog, configure the MLflow client to use Unity Catalog:

```python
import mlflow
mlflow.set_registry_uri("databricks-uc")
```

If the workspace’s default catalog is already a Unity Catalog catalog (and the cluster runs Databricks Runtime 13.3 LTS+ or MLflow 3), this step is not needed. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Registering Models

You can register models through the Python API, autologging, or the UI. All registration calls must use the three‑level name (e.g., `"prod.ml_team.iris_model"`).

- **Using autologging** (MLflow 2.x): `mlflow.register_model(logged_model.model_uri, "catalog.schema.model_name")`
- **With an automatically inferred signature**: supply an `input_example` in the `log_model` call. The model is automatically registered if `registered_model_name` is provided.
- **Using the UI**: from an experiment run page, click **Register model**, select **Unity Catalog**, and pick a destination model. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

Model versions without a signature have limitations (no input enforcement, no auto‑generated input examples for Model Serving, and requirement to provide a schema when used with AI functions). Signatures can be added or updated later via MLflow documentation. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Model Aliases

Aliases are mutable, named references to a specific model version. They are used to indicate deployment status (e.g., `"Champion"`, `"Staging"`). You can set, reassign, and delete aliases using the MLflow Client API or Catalog Explorer. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

```python
client = MlflowClient()
client.set_registered_model_alias("prod.ml_team.iris_model", "Champion", 1)
client.get_model_version_by_alias("prod.ml_team.iris_model", "Champion")
client.delete_registered_model_alias("prod.ml_team.iris_model", "Champion")
```

Aliases allow batch inference and model serving endpoints to reference a version by alias, decoupling deployment from version numbers. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Loading Models for Inference

Load models by alias or version number:

```python
# By alias
model_uri = "models:/prod.ml_team.iris_model@Champion"
champion = mlflow.pyfunc.load_model(model_uri)
champion.predict(test_x)

# By version number
model_uri = "models:/prod.ml_team.iris_model/1"
version_1 = mlflow.pyfunc.load_model(model_uri)
```

Models in Unity Catalog can be accessed from any workspace attached to the same [Metastore](/concepts/metastore.md), provided the user has the necessary privileges (`EXECUTE` on the model, plus `USE CATALOG` and `USE SCHEMA`). ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Data Lineage

Lineage from a model version to its upstream training datasets is automatically captured when `mlflow.log_input` is used to log a Unity Catalog table. Lineage information is visible on the model version page in Catalog Explorer under the **Lineage** tab, and can be explored as a directed graph. Feature store APIs also capture lineage automatically. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Access Control

In Unity Catalog, registered models are a subtype of the `FUNCTION` securable object. Permissions are managed with `GRANT ON FUNCTION` or via Catalog Explorer. REST API calls use `securable_type = "FUNCTION"`. To share write access, the model owner must grant ownership to a group containing collaborators. Models can be shared across regions or accounts using OpenSharing (Databricks‑to‑Databricks). ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Managing Models in the UI (Catalog Explorer)

To view models, navigate to Catalog Explorer, select a schema, and click a model under **Models**. The model details page shows all versions and allows you to:

- Set, update, or remove aliases.
- View version metadata and (in MLflow 3) parameters and metrics.
- View lineage.
- Add descriptions (including AI‑generated comments for registered models).
- Delete a model or individual versions.
- Copy a model version to another registered model.
- Edit tags. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Renaming, Copying, and Deleting

- **Rename**: use `client.rename_registered_model("<full-three-level-name>", "<new-model-name>")`. Only the model name (last part) is changed.
- **Copy model version**: use `client.copy_model_version("models:/source/version", "destination.model")` or the Copy button on the version page.
- **Delete**: delete a version with `client.delete_model_version(name, version)` or the entire model with `client.delete_registered_model(name)`. Deletion is irreversible. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Tags and Descriptions

- **Tags**: key‑value pairs on registered models or versions. Set and delete with `set_registered_model_tag`, `delete_registered_model_tag`, `set_model_version_tag`, `delete_model_version_tag`. Tags must meet platform‑wide constraints.
- **Descriptions**: free‑text descriptions can be added via the UI or API (`update_registered_model`, `update_model_version`). Registered models support AI‑generated comments. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Listing and Searching Models

List all registered models with `mlflow.search_registered_models()`. Search for versions of a specific model with `mlflow.search_model_versions("name='catalog.schema.model'")`. Note that some search‑API features are not supported (see Limitations). ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Promoting Models Across Environments

Model versions can be copied between registered models in different catalogs (e.g., `staging` to `prod`). After copying, aliases can be assigned to mark the version for deployment. This workflow uses the `copy_model_version` API and enforces access control through Unity Catalog privileges on source and destination models. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Limitations

- Stages are not supported; use the three‑level namespace and aliases instead.
- Webhooks are not supported.
- The `order_by` parameter and tag‑based filters are not supported in `search_model_versions` and `search_registered_models`. Only exact‑equality filters are allowed.
- Searching registered models by name in the filter string is not supported; use `get_registered_model` instead.
- Email notifications, comment discussion threads, and activity logs are not available. Audit logs provide an alternative.
- `search_registered_models` may return stale results for OpenSharing models; use the Databricks CLI or SDK to list models. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Downloading Model Files (Advanced)

For debugging, model files can be downloaded using `mlflow.artifacts.download_artifacts`. Normal loading should be done via `mlflow.pyfunc.load_model` or flavor‑specific loaders. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow](/concepts/mlflow.md)
- [MLflow Model Registry (Workspace)](/concepts/mlflow-model-registry.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Model Signature](/concepts/model-signatures-in-unity-catalog.md)
- [Feature Governance and Lineage](/concepts/feature-governance-and-lineage.md)
- [Model Serving](/concepts/model-serving.md)
- [MLflow 3](/concepts/mlflow-3.md)

## Sources

- manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md

# Citations

1. [manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md](/references/manage-model-lifecycle-in-unity-catalog-databricks-on-aws-5d1bac95.md)
