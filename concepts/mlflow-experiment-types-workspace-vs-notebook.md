---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bd442fce38689bcfd94d497bddca4a66129db7141ad1c8bc8cc53b02c279ce9c
  pageDirectory: concepts
  sources:
    - organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-types-workspace-vs-notebook
    - METWVN
  citations:
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 1
      end: 5
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 3
      end: 4
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 14
      end: 15
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 16
      end: 17
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 6
      end: 7
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 17
      end: 18
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 19
      end: 28
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 4
      end: 5
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 32
      end: 32
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 31
      end: 31
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 3
      end: 5
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 7
      end: 8
    - file: 35-38
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 40
      end: 47
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 53
      end: 54
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 55
      end: 55
    - file: 66-67
    - file: 87-88
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 109
      end: 113
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
      start: 68
      end: 70
title: "MLflow Experiment Types: Workspace vs Notebook"
description: MLflow experiments on Databricks come in two flavors — workspace experiments (standalone, created via UI or API, not tied to a notebook) and notebook experiments (auto-created when mlflow.start_run() is called without an active experiment, bound to a specific notebook).
tags:
  - mlflow
  - experiments
  - databricks
timestamp: "2026-06-19T19:53:19.605Z"
---

# MLflow Experiment Types: Workspace vs Notebook

**MLflow Experiment Types** refer to the two ways experiments can exist in Databricks: **workspace experiments** and **notebook experiments**. Experiments serve as organizational units for MLflow runs, including agent traces, LLM application evaluations, and model training runs. Understanding the differences between these two types is essential for effectively organizing and managing your MLflow tracking workflow. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:1-5]

## Workspace Experiments

A **workspace experiment** is created from the Databricks UI or the MLflow API and is not associated with any specific notebook. Any notebook can log runs to a workspace experiment by using the experiment ID or experiment name. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:3-4]

### Creating a Workspace Experiment

You can create a workspace experiment from the workspace menu or from the Experiments page. From the workspace, navigate to the desired folder, right-click, and select **Create > MLflow experiment**. From the Experiments page, click **Experiments** or select **New > Experiment** in the sidebar. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:14-15]

When creating an experiment, you can specify an optional artifact location. If no location is specified, artifacts are stored in MLflow-managed artifact storage at `dbfs:/databricks/mlflow-tracking/<experiment-id>`. For workspaces enabled for Unity Catalog, you can store artifacts in a [Unity Catalog](/concepts/unity-catalog.md) volume by specifying a path of the form `dbfs:/Volumes/catalog_name/schema_name/volume_name/user/specified/path`. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:16-17]

You can also create workspace experiments using the MLflow API or the Databricks Terraform provider with `databricks_mlflow_experiment`. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:6-7]

### Artifact Storage Options

Databricks recommends using a [Unity Catalog](/concepts/unity-catalog.md) volume for artifact storage. Alternatives include:

- **DBFS** (`dbfs:/path/to/artifacts`)
- **S3 direct storage** (`s3://<bucket>/<path>`), though this is not recommended. Artifacts stored in S3 do not appear in the MLflow UI and must be downloaded using an object storage client.

When you store an artifact in a location other than MLflow-managed DBFS or Unity Catalog volumes, the artifact does not appear in the MLflow UI. Models stored in these locations cannot be registered in Model Registry. Upload and download file size limits are both 5GB. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:17-18]

### Special Experiment Types from the Experiments Page

From the Experiments page, you can create:

- **Foundation Model Fine-tuning** experiments (deprecated)
- **Forecasting** experiments (AutoML)
- **Classification** experiments (AutoML)
- **Regression** experiments (AutoML)
- **Custom** experiments (standard MLflow experiment)

^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:19-28]

## Notebook Experiments

A **notebook experiment** is associated with a specific notebook. Databricks automatically creates a notebook experiment when you use `mlflow.start_run()` in a notebook and no active experiment exists. The notebook experiment shares the same name and ID as its corresponding notebook. The notebook ID is the numerical identifier at the end of a notebook URL. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:4-5]

### Creating a Notebook Experiment

Notebook experiments are created automatically when you start a run without an active experiment. Alternatively, you can pass a Databricks workspace path to an existing notebook in `mlflow.set_experiment()` to create a notebook experiment for it. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:32]

Users running MLflow on compute with dedicated group access must verify the group has permission to write to the directory where the notebook lives, or use `mlflow.set_tracking_uri("<path>")` to specify a folder for MLflow to write to. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:31]

## Key Differences

| Feature | Workspace Experiment | Notebook Experiment |
|---|---|---|
| Association | Not tied to any notebook | Tied to a specific notebook |
| Creation | Manual via UI or API | Automatic when using `mlflow.start_run()` |
| Name/ID | User-defined name and ID | Same name and ID as the notebook |
| Logging | Any notebook can log to it by experiment ID or name | Only associated notebook can log runs |

^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:3-5]

## Viewing Experiments

You can view all experiments in a workspace from the sidebar under **AI/ML > Experiments**. Each experiment you have access to appears on this page. Clicking an experiment name displays its experiment details page, which lists all runs associated with the experiment. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:7-8,35-38]

For workspace experiments, you can access the experiment details page from the workspace menu. For notebook experiments, you can access it from the notebook by clicking the **Experiment** icon in the notebook's right sidebar. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:40-47]

## Managing Experiments

You can rename, delete, or manage permissions for an experiment you own from the experiments page, the experiment details page, or the workspace menu. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:53-54]

### Deletion Behavior

When you delete a notebook experiment using the API (for example, `MlflowClient.tracking.delete_experiment()`), the notebook itself is moved into the Trash folder. If you delete a workspace or notebook experiment from the UI, the associated notebook is also deleted. You cannot directly rename, delete, or manage permissions on an MLflow experiment created by a notebook in a Databricks Git folder; you must perform these actions at the Git folder level. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:55,66-67,87-88]

## Migration Between Workspaces

To copy experiments between workspaces, you can use the community-driven open source project MLflow Export-Import. This tool allows you to share experiments with other data scientists, clone experiments from other users, copy experiments from local tracking servers to Databricks workspaces, and back up mission-critical experiments and models to another Databricks workspace. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:109-113]

## Getting Experiment Information

On the experiment details page, clicking the information icon shows the path to the experiment, the experiment ID, and the artifact location. You can use the experiment ID in `mlflow.set_experiment()` to set the active experiment. From a notebook, you can copy the experiment path by clicking the path icon in the notebook's experiment sidebar. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:68-70]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — Core system for logging MLflow runs and experiments
- [MLflow Runs](/concepts/mlflow-run.md) — Individual executions logged within experiments
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance solution for managing MLflow artifact locations
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Training technique often tracked with MLflow experiments
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient training technique for large models

## Sources

- organize-training-runs-with-mlflow-experiments-databricks-on-aws.md

# Citations

1. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:1-5](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
2. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:3-4](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
3. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:14-15](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
4. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:16-17](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
5. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:6-7](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
6. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:17-18](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
7. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:19-28](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
8. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:4-5](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
9. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:32-32](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
10. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:31-31](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
11. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:3-5](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
12. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:7-8](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
13. 35-38
14. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:40-47](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
15. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:53-54](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
16. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:55-55](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
17. 66-67
18. 87-88
19. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:109-113](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
20. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md:68-70](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
