---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2df6858e86c0bb4a167e72fbfaeba6a523d806d6f4366d52a64a9c9d8b26c5d1
  pageDirectory: concepts
  sources:
    - manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md
    - migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md
    - workspace-model-registry-example-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - workspace-model-registry
    - WMR
    - Workspace Model Registry (legacy)
    - Workspace Registry
    - Databricks Workspace Model Registry
  citations:
    - file: manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md
    - file: workspace-model-registry-example-databricks-on-aws.md
    - file: migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md
title: Workspace Model Registry
description: A Databricks-hosted, legacy version of the MLflow Model Registry for managing the full lifecycle of ML models, providing model lineage, versioning, stage transitions, webhooks, and email notifications.
tags:
  - machine-learning
  - model-registry
  - databricks
  - mlflow
timestamp: "2026-06-19T19:25:07.443Z"
---

# Workspace Model Registry

The **Workspace Model Registry** is a Databricks-provided, hosted version of the MLflow Model Registry. It enables teams to manage the full lifecycle of machine learning models within a single Databricks workspace. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

> **Note:** Databricks recommends using [Models in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/) for new projects. Workspace Model Registry is considered legacy and will be deprecated in the future. If your workspace is enabled for Unity Catalog, do not use the procedures on this page; instead use [Models in Unity Catalog](/concepts/models-in-unity-catalog.md). For guidance on migration, see Migrate workflow and models to Unity Catalog. Starting April 2024, Workspace Model Registry is disabled for new accounts whose workspace default catalog is in Unity Catalog. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md, workspace-model-registry-example-databricks-on-aws.md]

If your workspace default catalog is in Unity Catalog (rather than `hive_metastore`) and you are running Databricks Runtime 13.3 LTS or above or using MLflow 3, models are automatically created in and loaded from the workspace default catalog. To explicitly target the Workspace Model Registry in that scenario, run `mlflow.set_registry_uri("databricks")` at the start of your workload. Workspaces that had both a default catalog in Unity Catalog and used the Workspace Model Registry prior to January 2024 are exempt and continue to use the Workspace Model Registry by default. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Key Features

The Workspace Model Registry provides: ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

- Chronological model lineage (which MLflow experiment and run produced the model at a given time)
- [Model Serving](/concepts/model-serving.md) for real-time inference
- Model versioning with stage transitions (None, Staging, Production, Archived)
- Webhooks to automatically trigger actions based on registry events
- Email notifications of model events
- Descriptive annotations and comments on models and versions

## Creating or Registering a Model

### Using the UI

You can register a model from an [MLflow Run](/concepts/mlflow-run.md) or create a new empty model and assign a logged model to it. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

To register an existing logged model:
1. Open the [MLflow Run](/concepts/mlflow-run.md) from the notebook's Experiment Runs sidebar.
2. In the Artifacts section, click the model directory and click **Register Model**.
3. Choose to create a new model or select an existing one, then click **Register**.

To create a new empty model:
1. On the registered models page, click **Create Model**, enter a name, and create.
2. Then register a logged model to it as above.

### Using the API

- Use `mlflow.<model-flavor>.log_model(..., registered_model_name="<name>")` during an experiment to log and register in one step. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]
- Use `mlflow.register_model("runs:/<run-id>/<artifact-path>", "<name>")` after experiments complete.
- Use `MlflowClient().create_registered_model("<name>")` to create a new empty model (fails if name exists).

## Stage Transitions

Each model version has a stage: **None**, **Staging**, **Production**, or **Archived**. Users with appropriate permissions can transition directly; otherwise, they can request a transition for approval. Multiple versions can share the same stage. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

In the UI, click the **Stage** button on the model version page and select the target stage. Optionally, when transitioning to Production, you can choose to transition existing Production versions to Archived.

Using the API:
```python
client = MlflowClient()
client.transition_model_version_stage(
    name="<model-name>",
    version=<version>,
    stage="Production"
)
```
Accepted stage values: `"Staging"`, `"staging"`, `"Archived"`, `"archived"`, `"Production"`, `"production"`, `"None"`, `"none"`. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Permissions

Model permissions are set at the registered model level (versions inherit permissions). Permission levels include CAN READ, CAN EDIT, CAN MANAGE, etc. Workspace admins and CAN MANAGE users can set registry-wide default permissions from the Models page. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Annotations

### Descriptions, Comments, and Tags

- **Descriptions**: Add to models or versions to provide context (e.g., problem overview, methodology).
- **Comments**: Add to model versions for ongoing discussion.
- **Tags**: Key-value pairs to customize metadata and enable search.

Use the UI Edit buttons or API methods like `client.update_registered_model()`, `client.update_model_version()`, `client.set_registered_model_tag()`, and `client.set_model_version_tag()`. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Searching for Models

In the UI, use the search box on the registered models page. You can search by name or by tag using format `tags.<key>=<value>`, including the `AND` operator for multiple tags. Only models for which you have at least CAN READ permission are returned. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

Using the API:
```python
import mlflow
for m in mlflow.search_registered_models("tags.`<key>`='<value>'"):
    print(dict(m))
```
Also `mlflow.search_model_versions("name='<model-name>'")` to list version details. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Deleting Models and Model Versions

Deletion is permanent and cannot be undone. You can only delete models and model versions that are in the **None** or **Archived** stage. To delete a model with versions in Staging or Production, first transition them to None or Archived. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

In the UI, use the kebab menu on the model version or model page. Using the API:
```python
client.delete_model_version(name="<model-name>", version=<version>)
client.delete_registered_model(name="<model-name>")
```

## Notifications and Webhooks

You can configure email notifications per registered model (all activity, activity on versions you follow, or muted). Notifications are triggered for new versions, stage transitions, transition requests, and comments. Users are auto-subscribed when they comment, transition, or request a transition. Maximum daily email limits apply. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

Webhooks allow listening for events to trigger CI/CD or notifications to tools like Slack. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Quota Limits

Starting May 2024, the Workspace Model Registry imposes quota limits on the total number of registered models and model versions per workspace. See Resource limits. If exceeded, delete unneeded models/versions or adjust retention strategy. Contact your account team for limit increases. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Sharing Across Workspaces and Migration

To share models across workspaces, Databricks recommends using [Models in Unity Catalog](/concepts/models-in-unity-catalog.md) for centralized governance, cross-workspace access, lineage, and audit logging. If using the workspace model registry, you can share models across multiple workspaces with additional setup, such as remote workspace model registry. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

To migrate model versions from Workspace Model Registry to Unity Catalog, you can use the MLflow Client API `copy_model_version()` to copy versions while preserving version numbers. A placeholder model approach can ensure version numbering aligns between the two registries. ^[migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md]

## Example Usage

A complete example demonstrates forecasting wind farm power output: training a Keras neural network, registering the model as `power-forecasting-model`, adding descriptions, transitioning to Production, then loading the model for predictions. Later, a scikit-learn random forest is registered as a new version, transitioned through Staging to Production, and the application code automatically uses the latest Production version. Finally, versions are archived and deleted. The example notebook is available. ^[workspace-model-registry-example-databricks-on-aws.md]

## Related Concepts

- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Model Serving](/concepts/model-serving.md)
- Webhooks
- [Models in Unity Catalog](/concepts/models-in-unity-catalog.md)
- Migrate workflow and models to Unity Catalog

## Sources

- manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md
- migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md
- workspace-model-registry-example-databricks-on-aws.md

# Citations

1. [manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md](/references/manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws-666e92b6.md)
2. [workspace-model-registry-example-databricks-on-aws.md](/references/workspace-model-registry-example-databricks-on-aws-fa952b3f.md)
3. [migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws.md](/references/migrate-model-versions-from-workspace-model-registry-to-unity-catalog-databricks-on-aws-d3e98aed.md)
