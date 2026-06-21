---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 702049955cede644bf04b497bece449e993ad0e8b92fd6ae4631353352c49255
  pageDirectory: concepts
  sources:
    - organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - creating-mlflow-experiments-on-databricks
    - CMEOD
    - Create an MLflow Experiment|Create an MLflow experiment
  citations:
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
title: Creating MLflow Experiments on Databricks
description: Experiments can be created via the Databricks workspace UI, the Experiments page (with presets for Foundation Model Fine-tuning, AutoML forecasting/classification/regression, or Custom), the MLflow API, or the Databricks Terraform provider.
tags:
  - mlflow
  - experiments
  - creation
  - databricks
timestamp: "2026-06-19T19:53:35.505Z"
---

# Creating MLflow Experiments on Databricks

**MLflow Experiments** are the primary unit of organization for MLflow runs, including agent traces, LLM application evaluations, and model training runs. On Databricks, you can create experiments in two ways: workspace experiments and notebook experiments. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Types of MLflow Experiments

There are two types of experiments on Databricks:

- **Workspace experiments** – Created from the Databricks UI or the MLflow API. They are not associated with any notebook, and any notebook can log runs to them using the experiment ID or name. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]
- **Notebook experiments** – Automatically created when you start a run using `mlflow.start_run()` and no active experiment exists. A notebook experiment shares the same name and ID as its corresponding notebook. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Create Workspace Experiment

You can create a workspace experiment from the Databricks workspace, the Experiments page, or using the MLflow API or Terraform provider. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Create from the Workspace

1. Click **Workspace** in the sidebar.
2. Navigate to the folder where you want to create the experiment.
3. Right-click the folder and select **Create > MLflow experiment**.
4. In the dialog, enter a name and an optional artifact location. If not specified, artifacts are stored in MLflow-managed DBFS: `dbfs:/databricks/mlflow-tracking/<experiment-id>`. For Unity Catalog enabled workspaces, you can store artifacts in a Unity Catalog volume by specifying a path like `dbfs:/Volumes/catalog_name/schema_name/volume_name/user/specified/path`. You can also store artifacts directly to S3 (not recommended). ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]
5. Click **Create**. To log runs to this experiment, call `mlflow.set_experiment()` with the experiment path. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Create from the Experiments Page

Click **Experiments** in the left sidebar and select **New > Experiment**. Then choose one of:

- **Foundation Model Fine-tuning** – Opens the Fine-tuning dialog.
- **Forecasting** – Opens the AutoML forecasting configuration.
- **Classification** – Opens the classification configuration.
- **Regression** – Opens the regression configuration.
- **Custom** – Opens the standard Create MLflow Experiment dialog (same as from workspace). ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Create Using the MLflow API

You can also create an experiment using Python:

```python
import mlflow
mlflow.create_experiment(name=EXP_NAME, artifact_location=ARTIFACT_PATH)
```

The artifact location can be a Unity Catalog volume, DBFS path, or S3 URI. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Create Notebook Experiment

When you call `mlflow.start_run()` in a notebook and no experiment is active, Databricks automatically creates a notebook experiment. The experiment shares the same name and ID as the notebook. Alternatively, you can pass a Databricks workspace path to an existing notebook in `mlflow.set_experiment()` to create a notebook experiment for it. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## View Experiments

All experiments you have access to appear on the **Experiments** page. Click an experiment name to see its details page, which lists all associated runs. You can search experiments by name or location, or by using the `tags.\`mlflow.note.content\`` tag for description search. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

To view experiment details:
- **Workspace experiment** – Navigate to the folder in Workspace and click the experiment name.
- **Notebook experiment** – Open the notebook and click the Experiment icon in the right sidebar. The sidebar shows run summaries and allows navigation to the experiment details page. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Manage Experiments

You can rename, delete, or change permissions for experiments you own via the Experiments page, the experiment details page, or the workspace menu. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

- **Rename** – Click the kebab menu on the Experiments page or experiment details page and select **Rename**.
- **Delete** – Click the kebab menu and select **Delete**. Deleting a notebook experiment also deletes its associated notebook.
- **Change permissions** – Click **Permissions** on the experiment details page, or use the kebab menu on the Experiments page. Permission levels are defined by MLflow experiment ACLs. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Copy Experiments Between Workspaces

To migrate MLflow experiments between workspaces, use the community-driven open source project [MLflow Export-Import](https://github.com/mlflow/mlflow-export-import). It allows sharing, cloning, backing up experiments and runs across tracking servers or Databricks workspaces. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Related Concepts

- [MLflow runs](/concepts/mlflow-run.md) – The unit of execution recorded under an experiment.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – API for logging parameters, metrics, and artifacts.
- [Unity Catalog](/concepts/unity-catalog.md) – Governs artifact storage locations.
- Workspace objects – How experiments are stored in the Databricks workspace.

## Sources

- organize-training-runs-with-mlflow-experiments-databricks-on-aws.md

# Citations

1. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
