---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 21abb9b0e8c7b23c35743a7eaa43bbad11cf00f39d3ad19b729660213d791681
  pageDirectory: concepts
  sources:
    - view-training-results-with-mlflow-runs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-run-lifecycle-management
    - MRLM
  citations:
    - file: view-training-results-with-mlflow-runs-databricks-on-aws.md
title: MLflow Run Lifecycle Management
description: Operations for managing MLflow runs including renaming, deleting (with bulk deletion by creation time), restoring (with bulk restore by deletion time), and a 30-day retention period for deleted runs.
tags:
  - mlflow
  - experiment-tracking
  - lifecycle-management
timestamp: "2026-06-19T23:25:36.331Z"
---

# [MLflow Run](/concepts/mlflow-run.md) Lifecycle Management

An **MLflow run** corresponds to a single execution of model code. Each run records information such as the notebook that launched the run, any models created by the run, model parameters and metrics saved as key-value pairs, tags for run metadata, and any artifacts (output files) created by the run. All [MLflow](/concepts/mlflow.md) runs are logged to the [active experiment](/concepts/mlflow-active-experiment.md); if no experiment has been explicitly set as active, runs are logged to the notebook experiment. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Viewing Run Details

You can access a run either from its experiment details page or directly from the notebook that created it. On the run screen you see the run ID, parameters, metrics, and details including a link to the source notebook. Artifacts saved from the run are available in the **Artifacts** tab.

If a model is logged from a run, the model appears in the **Artifacts** tab together with code snippets illustrating how to load and use the model for predictions on Spark and Pandas DataFrames. (In [MLflow 3](/concepts/mlflow-3.md), models are distinct first-class objects rather than run artifacts.) ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

To view the version of the notebook that created a run, click the link in the **Source** column on the experiment page, or click the source link on the run page, or from the notebook itself use the **Notebook** icon in the Experiment Runs sidebar. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Managing Runs

### Tags

Tags are key-value pairs used to store custom metadata and can later be used to search for runs.

- **Add a tag:** On the run page, in the **Details** table, click **Add tags** next to **Tags**. Enter a key and value in the dialog and save.
- **Edit or delete a tag:** On the run page, click the pencil icon next to the existing tags. Delete a tag by clicking the X on that tag, or edit its value. Save when done.

### Rename a Run

On the run page, click the kebab menu (upper right, next to **Permissions**) and select **Rename**. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Filtering Runs

On the experiment details page, you can filter runs by entering a query expression in the search field. Queries can compare parameter or metric values, use aggregate functions (`MIN`, `MAX`, `LATEST`), and filter by tag keys and values. For example:

- `metrics.r2 > 0.3`
- `params.elasticNetParam = 0.5 AND metrics.avg_areaUnderROC > 0.3`
- `tags.estimator_name="RandomForestRegressor"`

By default, metric values are filtered based on the last logged value. Using `MIN` or `MAX` lets you search by minimum or maximum metric values (only for runs logged after August 2024). You can also filter by run state (**Active** or **Deleted**), creation time, or used datasets using the drop‑down menus. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Downloading Runs

On the experiment details page, click the kebab menu and choose **Download `<n>` runs** to download a CSV file containing up to 100 runs, with columns for start time, duration, run ID, name, source type, source name, user, status, parameters, and metrics.

To download more than 100 runs or to download programmatically, select **Download all runs**. A dialog provides a code snippet that can be copied or opened in a notebook. After running the code, select **Download all rows** from the cell output. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Deleting Runs

You can delete runs from the experiment details page:

1. Select one or more runs by checking the box to their left.
2. Click **Delete**.
3. If the run is a parent run, choose whether to also delete descendant runs (selected by default).
4. Confirm deletion. Deleted runs are saved for 30 days. To display deleted runs, select **Deleted** in the **State** field. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

### Bulk Delete Based on Creation Time

Using Databricks Runtime 14.1 or later, call the `mlflow.delete_runs` API:

- `experiment_id`: ID of the experiment.
- `max_timestamp_millis`: Maximum creation timestamp (UNIX epoch ms); only runs created at or before this time are deleted.
- `max_runs`: (Optional) Maximum number of runs to delete (default 10000, max 10000).

For earlier Databricks Runtime versions, a client code snippet using `http_request` is provided in the source documentation. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Restoring Runs

To restore previously deleted runs from the UI:

1. On the experiment page, set **State** to **Deleted**.
2. Select one or more runs.
3. Click **Restore** and confirm. Restored runs appear when **Active** is selected. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

### Bulk Restore Based on Deletion Time

Using Databricks Runtime 14.1 or later, call the `mlflow.restore_runs` API:

- `experiment_id`: ID of the experiment.
- `min_timestamp_millis`: Minimum deletion timestamp (UNIX epoch ms); only runs deleted at or after this time are restored.
- `max_runs`: (Optional) Maximum number of runs to restore (default 10000, max 10000).

For earlier versions, a client code snippet is provided in the source documentation. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Comparing Runs

You can compare runs from a single experiment or from multiple experiments. The **Comparing Runs** page presents the selected runs in tabular format, with parameters and metrics tables. You can also create visualizations of run results (see Compare MLflow runs and models using graphs and charts).

- **Single experiment:** On the experiment details page, select two or more runs and click **Compare**.
- **Multiple experiments:** On the experiments page, select the experiments, click **Compare (n)**, then select runs from the resulting combined table and click **Compare**.

The **Parameters** and **Metrics** tables show data from all selected runs. You can toggle **Show diff only** to hide parameters and metrics that are identical across runs. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

[MLflow](/concepts/mlflow.md) metadata for experiments and runs is also available in [system tables](/concepts/mlflow-system-tables.md), where you can use Databricks SQL and lakehouse tooling to analyze experiment data. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Copying Runs Between Workspaces

To import or export [MLflow](/concepts/mlflow.md) runs to or from your Databricks workspace, use the community‑driven open source project MLflow Export-Import. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [Active Experiment](/concepts/mlflow-active-experiment.md)
- [MLflow 3](/concepts/mlflow-3.md)
- MLflow Export-Import
- System Tables (MLflow)

## Sources

- view-training-results-with-mlflow-runs-databricks-on-aws.md

# Citations

1. [view-training-results-with-mlflow-runs-databricks-on-aws.md](/references/view-training-results-with-mlflow-runs-databricks-on-aws-c299681f.md)
