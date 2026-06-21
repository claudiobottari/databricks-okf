---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 673a348a6405ca9e3d9b314261b2f78e9a3139a3e9912146e9440a59cb503009
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment
    - MLflow Experiment UI
    - MLflow Experiments
    - MLflow Experiments UI
    - MLflow experiment ACLs
    - MLflow experiment UI
    - MLflow experiment page
    - MLflow experiments
    - Read MLflow experiments
    - Experiment
    - Experiment UI
    - Experiments
    - Experiments page
    - MLflow Experiments|MLflow Experiment
    - MLflow Experiments|MLflow experiment
    - MLflow Experiments|experiment
    - MLflow Experiments|experiment page
    - MLflow experiment management
    - MLflow experiments | experiment
    - MLflow experiments|MLflow experiment
    - MLflow experiments|MLflow experiment page
    - MLflow experiments|experiment
    - experiment
    - experiment details page
  citations:
    - file: concepts-data-model-databricks-on-aws.md
    - file: track-model-development-using-mlflow-databricks-on-aws.md
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: MLflow Experiment
description: A named container that organizes and groups all artifacts related to a single GenAI application, including traces, evaluation runs, app versions, prompts, and quality assessments.
tags:
  - mlflow
  - data-model
  - genai
timestamp: "2026-06-19T14:23:21.462Z"
---

# MLflow Experiment

An **MLflow Experiment** is a named container that organizes and groups together all artifacts related to a single application, whether for traditional machine learning or generative AI. ^[concepts-data-model-databricks-on-aws.md] In the GenAI context, an experiment serves as a project folder that contains every trace, evaluation run, app version, prompt, and quality assessment from throughout an app's lifecycle. ^[concepts-data-model-databricks-on-aws.md]

Experiments are the core organizational entity in the [MLflow Tracking](/concepts/mlflow-tracking.md) system. They allow you to compare and filter runs to understand how a model performs and how its performance depends on parameter settings, input data, and other factors. ^[track-model-development-using-mlflow-databricks-on-aws.md]

## Data Model Structure

Experiments contain the following categories of data for GenAI applications ^[concepts-data-model-databricks-on-aws.md]:

- **Observability data**: [Traces](/concepts/traces.md) (app execution logs) with attached [Assessments](/concepts/assessments.md) (quality measurements)
- **Evaluation data**: [Evaluation Datasets](/concepts/evaluation-datasets.md) (curated test cases) and [Evaluation Runs](/concepts/evaluation-runs.md) (results of quality evaluation)
- **Human labeling data**: [Labeling Sessions](/concepts/labeling-sessions.md) (queues of traces for human review) and [Labeling Schemas](/concepts/labeling-schemas.md) (structured questions for labelers)
- **Application versioning data**: [Logged Models](/concepts/logged-models.md) (app version snapshots) and [Prompts](/concepts/prompt-versioning.md) (LLM prompt templates)

MLflow only requires you to use traces; all other aspects of the data model are optional but highly recommended. ^[concepts-data-model-databricks-on-aws.md]

## Types of Experiments

There are two types of experiments in Databricks: **workspace experiments** and **notebook experiments**. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Workspace Experiment

A workspace experiment is created from the Databricks UI or the MLflow API and is not associated with any particular notebook. Any notebook can log a run to a workspace experiment by using the experiment ID or name. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Notebook Experiment

A notebook experiment is associated with a specific notebook. Databricks automatically creates a notebook experiment if there is no active experiment when you start a run using `mlflow.start_run()`. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md] A notebook experiment shares the same name and ID as its corresponding notebook; the notebook ID is the numerical identifier at the end of a notebook URL. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

If you delete a notebook experiment using the API (for example, `MlflowClient.tracking.delete_experiment()`), the notebook itself is moved to the Trash folder. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Creating an Experiment

### Creating a Workspace Experiment from the UI

You can create a workspace experiment directly from the workspace or from the Experiments page. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

To create from the workspace ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]:
1. Click **Workspace** in the sidebar.
2. Navigate to the folder where you want the experiment.
3. Right-click the folder and select **Create > MLflow experiment**.
4. Enter a name and optional artifact location. If no location is given, artifacts are stored in MLflow-managed storage (`dbfs:/databricks/mlflow-tracking/<experiment-id>`). For Unity Catalog–enabled workspaces, you can store artifacts in a Unity Catalog volume by specifying a path like `dbfs:/Volumes/catalog_name/schema_name/volume_name/user/specified/path`. If neither Unity Catalog nor DBFS is suitable, you can use an S3 URI (`s3://<bucket>/<path>`), though artifacts stored in S3 do not appear in the MLflow UI. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]
5. Click **Create**. The experiment details page appears.

To create from the Experiments page ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]:
- Click **Experiments** in the sidebar, then click **New > Experiment**.
- Choose one of: **Foundation Model Fine-tuning**, **Forecasting**, **Classification**, **Regression**, or **Custom**. The **Custom** option opens the same dialog as creating from the workspace.

### Creating a Workspace Experiment via the API

```python
import mlflow

EXP_NAME = "/Users/first.last@databricks.com/my_experiment_name"
ARTIFACT_PATH = "dbfs:/Volumes/my_catalog/my_schema/my_volume"

mlflow.set_tracking_uri("databricks")
mlflow.set_registry_uri("databricks-uc")
if mlflow.get_experiment_by_name(EXP_NAME) is None:
    mlflow.create_experiment(name=EXP_NAME, artifact_location=ARTIFACT_PATH)
mlflow.set_experiment(EXP_NAME)
```

^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

You can also create experiments using the Databricks Terraform provider with the `databricks_mlflow_experiment` resource. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Creating a Notebook Experiment

When you use `mlflow.start_run()` in a notebook without an active experiment, Databricks automatically creates a notebook experiment. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md] Alternatively, you can pass a Databricks workspace path to an existing notebook in `mlflow.set_experiment()` to create a notebook experiment for it. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Viewing Experiments

All experiments you have access to appear on the **Experiments** page (sidebar → **AI/ML** → **Experiments**). Click an experiment name to view its details page, which lists all runs associated with the experiment. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Viewing a Workspace Experiment

From **Workspace**, navigate to the folder containing the experiment and click the experiment name. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Viewing a Notebook Experiment

In the notebook's right sidebar, click the **Experiment** icon. The Experiment Runs sidebar shows a summary of each run (parameters and metrics). At the top is the name of the experiment the notebook most recently logged to. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md] From there, you can navigate to the full experiment details page or directly to a run. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Getting Experiment ID and Path

On the experiment details page, click the information icon (circled "i") next to the experiment name. A pop-up shows the path, experiment ID, and artifact location. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md] In a notebook's sidebar, you can also copy the full path by clicking the Path icon. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Managing Experiments

You can rename, delete, or change permissions for an experiment you own from the Experiments page, the experiment details page, or the workspace menu. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md] Experiments created by a notebook in a Databricks Git folder cannot be directly renamed, deleted, or have permissions changed; those actions must be performed at the Git folder level. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Renaming

- On the **Experiments** page, click the kebab menu (three vertical dots) in the rightmost column and select **Rename**. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]
- On the experiment details page, click the kebab menu next to **Permissions** and select **Rename**. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]
- From the workspace, right-click the experiment name and click **Rename**. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Deleting

- **Notebook experiments** cannot be deleted separately from the notebook. Deleting a notebook experiment via the UI also deletes the notebook. To delete both using the API, use the Workspace API. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]
- **Workspace or notebook experiments** can be deleted from the Experiments page (kebab menu → **Delete**) or from the experiment details page (kebab menu → **Delete**). ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md] From the workspace, right-click and select **Move to Trash**. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

### Changing Permissions

From the experiment details page, click **Permissions** to open the permissions dialog. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md] You can also change permissions from the Experiments page (kebab menu → **Permissions**). ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md] For information on experiment permission levels, see MLflow experiment ACLs. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Logging Runs to an Experiment

By default, runs are logged to the notebook experiment when training in a notebook. To log runs to a workspace experiment, call `mlflow.set_experiment(experiment_name)` with the experiment path. ^[track-model-development-using-mlflow-databricks-on-aws.md] MLflow can automatically log training code (autologging) or you can use the logging API for fine-grained control over which parameters, metrics, and artifacts are logged. ^[track-model-development-using-mlflow-databricks-on-aws.md]

## Serverless Budget Policy

Starting with the 403 PERMISSION_DENIED Serverless Budget Policy Error, experiments support assigning a serverless budget policy to control which policy MLflow uses for serverless workloads such as scheduled scorers, synthetic evaluation set generation, and agent evaluation. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

To set a budget policy on an experiment ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]:

1. Open the MLflow experiment.
2. In the experiment **Details** panel, set the **Budget policy** to a policy you have access to use.

Or via the API using `mlflow.set_experiment_tag()` ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]:

```python
import mlflow

mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

## Resource Limits

Starting March 27, 2024, MLflow imposes quota limits on the number of total runs per experiment. If you hit this quota, delete runs you no longer need using the delete runs API. If you require an increase, contact your Databricks account team. ^[track-model-development-using-mlflow-databricks-on-aws.md]

## Copying Experiments Between Workspaces

To migrate MLflow experiments between workspaces, you can use the community-driven open source project [MLflow Export-Import](https://github.com/mlflow/mlflow-export-import). This tool enables you to share experiments with other users, clone experiments from a local tracking server to a Databricks workspace, or back up mission-critical experiments. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## MLflow Experiment UI

The MLflow experiment UI provides visual access to many elements of the data model. Using the UI, you can do the following ^[concepts-data-model-databricks-on-aws.md]:

- Search for and view traces.
- Review feedback and expectations.
- View and analyze evaluation results.
- Manage evaluation datasets.
- Manage versions and prompts.

## Related Concepts

- [MLflow Runs](/concepts/mlflow-run.md) — Single executions of model code logged to an experiment.
- [MLflow Logged Models](/concepts/mlflow-loggedmodel.md) — Versioned model snapshots associated with runs.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Execution logs (traces) stored in experiments for GenAI apps.
- [Evaluation Runs](/concepts/evaluation-runs.md) — Results of systematic quality evaluation, stored as runs in an experiment.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Policy that can be assigned to an experiment to control serverless workload costs.
- [Traces](/concepts/traces.md) — Complete execution logs of GenAI applications.
- [Assessments](/concepts/assessments.md) — Quality measurements attached to traces.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Curated collections of test cases for systematic testing.
- [Prompts](/concepts/prompt-versioning.md) — Version-controlled templates for LLM prompts.
- 403 PERMISSION_DENIED Serverless Budget Policy Error — Error that occurs when no budget policy is available.

## Sources

- concepts-data-model-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
- organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
- track-model-development-using-mlflow-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
2. [track-model-development-using-mlflow-databricks-on-aws.md](/references/track-model-development-using-mlflow-databricks-on-aws-fe722724.md)
3. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
4. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
