---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e3f3fa46f04b6e35940e51b9e65f3f410ba186525f34c8ae4eeb2db716174fce
  pageDirectory: concepts
  sources:
    - view-training-results-with-mlflow-runs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-run
    - MLflow Run ID
    - MLflow Runs
    - MLflow Runs UI
    - MLflow runs
    - MLflow Nested Runs
    - MLflow Run Details
    - MLflow run context
    - MLflow runs|run
  citations:
    - file: view-training-results-with-mlflow-runs-databricks-on-aws.md
title: MLflow Run
description: A single execution of model code in MLflow that records parameters, metrics, tags, artifacts, and source information for experiment tracking.
tags:
  - mlflow
  - experiment-tracking
  - machine-learning
timestamp: "2026-06-19T23:25:38.516Z"
---

# [MLflow](/concepts/mlflow.md) Run

An **MLflow run** corresponds to a single execution of model code during a training experiment. Each run records information such as the notebook that launched the run, any models created by the run, model parameters and metrics saved as key-value pairs, tags for run metadata, and any artifacts (output files) created by the run.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

All [MLflow](/concepts/mlflow.md) runs are logged to the [active experiment](/concepts/mlflow-active-experiment.md) in [MLflow](/concepts/mlflow.md). If no experiment has been explicitly set as the active experiment, runs are logged to the notebook experiment by default.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Viewing Run Details

You can access a run from its experiment details page or directly from the notebook that created the run.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

From the [experiment details page](/concepts/mlflow-experiment.md), click the run name in the runs table. From the notebook, click the run name in the Experiment Runs sidebar.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

The run screen displays the run ID, the parameters used for the run, the metrics resulting from the run, and details about the run including a link to the source notebook. Artifacts saved from the run are available in the **Artifacts** tab.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

If a model is logged from a run, the model appears in the **Artifacts** tab along with code snippets illustrating how to load and use the model to make predictions on Spark and Pandas DataFrames. In [MLflow 3](/concepts/mlflow-3.md), models are now a distinct first-class object rather than being logged as run artifacts.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

### Viewing the Notebook Used for a Run

To view the version of the notebook that created a run:
- On the experiment details page, click the link in the **Source** column.
- On the run page, click the link next to **Source**.
- From the notebook, in the Experiment Runs sidebar, click the **Notebook** icon in the box for that experiment run.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Managing Runs

### Adding, Editing, and Deleting Tags

Tags are key-value pairs that can be created and used later to search for runs. To add a tag, click **Add tags** next to **Tags** on the run page's Details table. To edit or delete tags, click the pencil icon next to existing tags.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

### Renaming Runs

To rename a run, click the kebab menu at the upper right corner of the run page and select **Rename**.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

### Filtering Runs

You can search for runs in the table on the experiment details page based on parameter or metric values, or by tag.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

Query syntax examples include:

- `metrics.r2 > 0.3`
- `params.elasticNetParam = 0.5`
- `params.elasticNetParam = 0.5 AND metrics.avg_areaUnderROC > 0.3`
- `MIN(metrics.rmse) <= 1`
- `MAX(metrics.memUsage) > 0.9`
- `LATEST(metrics.memUsage) = 0 AND MIN(metrics.rmse) <= 1`

By default, metric values are filtered based on the last logged value. Using `MIN` or `MAX` lets you search for runs based on the minimum or maximum metric values. Only runs logged after August 2024 have minimum and maximum metric values.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

To search for runs by tag, use format `tags.<key>="<value>"`. Both keys and values can contain spaces; if the key includes spaces, it must be enclosed in backticks.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

You can also filter runs based on state (Active or Deleted), creation time, and datasets used through drop-down menus.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

### Downloading Runs

You can download runs from the experiment details page. Click the kebab menu and:
- Select **Download `<n>` runs** to download a CSV file containing all runs shown (up to a maximum of 100). The file contains one run per row with fields: Start Time, Duration, Run ID, Name, Source Type, Source Name, User, Status, and parameters/metrics.
- Select **Download all runs** to get a code snippet for programmatic download.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

### Deleting and Restoring Runs

Runs can be deleted from the experiment details page by selecting runs and clicking **Delete**. Deleted runs are saved for 30 days. To display deleted runs, select **Deleted** in the State field.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

Bulk deletion based on creation time is supported using `mlflow.delete_runs` API (requires Databricks Runtime 14.1 or later). For earlier runtimes, a custom client code approach is available.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

Restoration of deleted runs based on deletion time is supported using `mlflow.restore_runs` API.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Comparing Runs

You can compare runs from a single experiment or from multiple experiments. The Comparing Runs page presents information in tabular format and allows visualization of run results. For simplicity, you can hide parameters and metrics that are identical in all selected runs by toggling the **Show diff only** button.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

### Comparing Runs from a Single Experiment

On the experiment details page, select two or more runs by clicking the checkbox, then click **Compare**.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

### [Comparing Runs from Multiple Experiments](/concepts/comparing-runs-from-multiple-experiments.md)

On the experiments page, select experiments, click **Compare (n)**, then select runs and click **Compare**.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

### System Tables Comparison

[MLflow](/concepts/mlflow.md) metadata for experiments and runs is also available in system tables, where Databricks SQL and lakehouse tooling can be leveraged for analysis.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Copying Runs Between Workspaces

To import or export [MLflow](/concepts/mlflow.md) runs between Databricks workspaces, use the community-driven open-source project **MLflow Export-Import**.^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for grouping related runs
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The core logging system for runs
- [Active Experiment](/concepts/mlflow-active-experiment.md) — The experiment that receives all logged runs
- [MLflow 3](/concepts/mlflow-3.md) — Latest version with first-class model objects
- [Data Profiling](/concepts/data-profiling.md) — Statistical analysis of tables related to model runs
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Cost control for serverless [MLflow](/concepts/mlflow.md) workloads

## Sources

- view-training-results-with-mlflow-runs-databricks-on-aws.md

# Citations

1. [view-training-results-with-mlflow-runs-databricks-on-aws.md](/references/view-training-results-with-mlflow-runs-databricks-on-aws-c299681f.md)
