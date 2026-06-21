---
title: View training results with MLflow runs | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow/runs
ingestedAt: "2026-06-18T08:14:15.606Z"
---

This article describes how to use MLflow runs to view and analyze the results of a model training experiment, and how to manage and organize runs. For more information about MLflow experiments, see [Organize training runs with MLflow experiments](https://docs.databricks.com/aws/en/mlflow/experiments).

An MLflow _run_ corresponds to a single execution of model code. Each run records information such as the notebook that launched the run, any models created by the run, model parameters and metrics saved as key-value pairs, tags for run metadata, and any artifacts, or output files, created by the run.

All MLflow runs are logged to the [active experiment](https://docs.databricks.com/aws/en/mlflow/tracking#where-mlflow-runs-are-logged). If you have not explicitly set an experiment as the active experiment, runs are logged to the notebook experiment.

## View run details[​](#view-run-details "Direct link to View run details")

You can access a run either from its experiment details page or directly from the notebook that created the run.

From the [experiment details page](https://docs.databricks.com/aws/en/mlflow/experiments#experiment-page), click the run name in the runs table.

![Open experiment run from experiment details page.](https://docs.databricks.com/aws/en/assets/images/open-run-from-runs-table-d4823f90f62f30494e5148dc243e45ab.png)

From the notebook, click the run name in the Experiment Runs sidebar.

![Open experiment run from notebook.](https://docs.databricks.com/aws/en/assets/images/open-run-from-notebook-564ed9303aecc466153ca6fdb369de71.png)

The [run screen](#run-details-screen) shows the run ID, the parameters used for the run, the metrics resulting from the run, and details about the run including a link to the source notebook. Artifacts saved from the run are available in the **Artifacts** tab.

![View run](https://docs.databricks.com/aws/en/assets/images/quick-start-nb-run-3512267e9c81cb9f94c5e009c8c693a4.png)

### Code snippets for prediction[​](#code-snippets-for-prediction "Direct link to Code snippets for prediction")

If you log a model from a run, the model appears in the **Artifacts** tab, along with code snippets illustrating how to load and use the model to make predictions on Spark and Pandas DataFrames. In [MLflow 3](https://docs.databricks.com/aws/en/mlflow/mlflow-3-install), models are now their distinct first-class object rather than being logged as run artifact. For more information, see [Get started with MLflow 3 for models](https://docs.databricks.com/aws/en/mlflow/mlflow-3-install).

![predict code snippets](https://docs.databricks.com/aws/en/assets/images/model-snippets-71c5265418f96f2b5291263ef229c901.png)

### View the notebook used for a run[​](#view-the-notebook-used-for-a-run "Direct link to View the notebook used for a run")

To view the [version of the notebook](https://docs.databricks.com/aws/en/notebooks/notebook-version-history) that created a run:

*   On the experiment details page, click the link in the **Source** column.
*   On the run page, click the link next to **Source**.
*   From the notebook, in the Experiment Runs sidebar, click the **Notebook** icon ![Notebook Version Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAaCAYAAABVX2cEAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAE6ADAAQAAAABAAAAGgAAAAAtfzLXAAABwklEQVQ4EWP8DwQMVAJMVDIHbMwIMYwFPcyuvP/C8PnnXxRhXnZmBh1BHhQxbBxG9Nh0XHiYQVZcAK72268/DB+//mCQBBo22UmTgZ8Nw364Wqwyizx04QqOvfjIcOLFB4bnX38xpOy8zDDHXRengUTHZre1KoOCEA9D7r7rcIvQGUQZduHFJ4b+i48YpHjYGV4AwxTkWmwAqzeRFWoLcTMYSPAxwDIKGytuLVhlHn/5wVB95DbYTDs5IYYiA3m4+W7ywgz8OAzEahgfMMYyDOQY+KBJAmT4CaBXP/3+w+AmK8Qgy8MBNxyZgTXMHgOTwrV3X8Bpa8ejt2BX/mf4zyDNzQ5mr7rzEtkMBBuUzpCBw4JDYO6Hn7//g3Ds9ktg/qPP3/+DMAiAxGBssACUwOoykFWgxHn13Vdw4IP4j7/8BGMQ20dFjGEn0MXoAMMwYWBKB+WCj8CU33fqHsOxR+/AbFlgstj9+C0DKLuBAChcMQCyM9HZMK+CaBi4/O4zTm9iMR5hH8iroJgsBKZ6a2CSAIGjD98ypABjGluMYmR0hFGoLFiqByViXJmdaMNQjcbOw4gA7MqIEx01jLhwQlYFAPAEGa+z/P8jAAAAAElFTkSuQmCC) in the box for that Experiment Run.

The version of the notebook associated with the run appears in the main window with a highlight bar showing the date and time of the run.

### Add a tag to a run[​](#add-a-tag-to-a-run "Direct link to Add a tag to a run")

Tags are key-value pairs that you can create and use later to [search for runs](#filter-runs).

1.  In the **Details** table on the [run page](#run-details-screen), click **Add tags** next to **Tags**.
    
    ![Tag button on Details page](https://docs.databricks.com/aws/en/assets/images/tags-open-2b92892f2d6833c4fac51ed029b0ae39.png)
    
2.  The Add/Edit tags dialog opens. In the **Key** field, enter a name for the key, and click **Add tag**.
    
    ![Add a tag.](https://docs.databricks.com/aws/en/assets/images/tag-add-e7a0a94c7df96101259d3f82deb415fc.png)
    
3.  In the **Value** field, enter the value for the tag.
    
4.  Click the plus sign to save the key-value pair you just entered.
    
    ![Plus sign to save key-value pair.](https://docs.databricks.com/aws/en/assets/images/save-tag-46acb16b79fdaa4e2136120312a5e5f7.png)
    
5.  To add additional tags, repeat steps 2 through 4.
    
6.  When you are done, click **Save tags**.
    

### Edit or delete a tag for a run[​](#edit-or-delete-a-tag-for-a-run "Direct link to Edit or delete a tag for a run")

1.  In the **Details** table on the [run page](#run-details-screen), click ![Pencil icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xMy40ODc0IDEuNTEyNTZDMTIuODA0IDAuODI5MTQ2IDExLjY5NiAwLjgyOTE0NSAxMS4wMTI2IDEuNTEyNTZMMS4yMTk2NyAxMS4zMDU1QzEuMDc5MDIgMTEuNDQ2MSAxIDExLjYzNjkgMSAxMS44MzU4VjE0LjMzNThDMSAxNC43NSAxLjMzNTc5IDE1LjA4NTggMS43NSAxNS4wODU4SDQuMjVDNC40NDg5MSAxNS4wODU4IDQuNjM5NjggMTUuMDA2OCA0Ljc4MDMzIDE0Ljg2NjFMMTQuNTczMiA1LjA3MzIyQzE1LjI1NjYgNC4zODk4MSAxNS4yNTY2IDMuMjgxNzcgMTQuNTczMiAyLjU5ODM1TDEzLjQ4NzQgMS41MTI1NlpNMTIuMDczMiAyLjU3MzIyQzEyLjE3MDkgMi40NzU1OSAxMi4zMjkxIDIuNDc1NTkgMTIuNDI2OCAyLjU3MzIyTDEzLjUxMjYgMy42NTkwMUMxMy42MTAyIDMuNzU2NjQgMTMuNjEwMiAzLjkxNDkzIDEzLjUxMjYgNC4wMTI1NkwxMiA1LjUyNTEzTDEwLjU2MDcgNC4wODU3OUwxMi4wNzMyIDIuNTczMjJaTTkuNSA1LjE0NjQ1TDIuNSAxMi4xNDY0VjEzLjU4NThIMy45MzkzNEwxMC45MzkzIDYuNTg1NzlMOS41IDUuMTQ2NDVaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) next to the existing tags.
    
    ![tag table](https://docs.databricks.com/aws/en/assets/images/existing-tags-open-13c732d3590f13fe8c0eb69b19f09937.png)
    
2.  The Add/Edit tags dialog opens.
    
    1.  To delete a tag, click the X on that tag.
        
        ![Delete a tag.](https://docs.databricks.com/aws/en/assets/images/delete-tag-bbbf797ca49fc213a14050ad89bba9a6.png)
        
    2.  To edit a tag, select the key from the drop-down menu, and edit the value in the **Value** field. Click the plus sign to save your change.
        
        ![Edit a tag.](https://docs.databricks.com/aws/en/assets/images/edit-tag-38b2751593f92d6d25926b4f545990ce.png)
        
3.  When you are done, click **Save tags**.
    

## Rename run[​](#rename-run "Direct link to Rename run")

To rename a run, click the kebab menu ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) at the upper right corner of the run page (next to the **Permissions** button) and select **Rename**.

![Rename a run from the run page.](https://docs.databricks.com/aws/en/assets/images/rename-run-c94bde4c43e4a3be54168645ce5dbbd7.png)

## Select columns to display[​](#select-columns-to-display "Direct link to Select columns to display")

To control the columns displayed in the runs table on the experiment details page, click **Columns** and select from the drop-down menu.

## Filter runs[​](#filter-runs "Direct link to filter-runs")

You can search for runs in the table on the experiment details page based on parameter or metric values. You can also search for runs by tag.

*   To search for runs that match an expression containing parameter and metric values, enter a query in the search field and press Enter. Some query syntax examples are:
    
    `metrics.r2 > 0.3`
    
    `params.elasticNetParam = 0.5`
    
    `params.elasticNetParam = 0.5 AND metrics.avg_areaUnderROC > 0.3`
    
    `MIN(metrics.rmse) <= 1`
    
    `MAX(metrics.memUsage) > 0.9`
    
    `LATEST(metrics.memUsage) = 0 AND MIN(metrics.rmse) <= 1`
    
    By default, metric values are filtered based on the last logged value. Using `MIN` or `MAX` lets you search for runs based on the minimum or maximum metric values, respectively. Only runs logged after August 2024 have minimum and maximum metric values.
    
*   To search for runs by tag, enter tags in the format: `tags.<key>="<value>"`. String values must be enclosed in quotes as shown.
    
    `tags.estimator_name="RandomForestRegressor"`
    
    `tags.color="blue" AND tags.size=5`
    
    Both keys and values can contain spaces. If the key includes spaces, you must enclose it in backticks as shown.
    
        tags.`my custom tag` = "my value"
    

You can also filter runs based on their state (Active or Deleted), when the run was created, and what datasets were used. To do this, make your selections from the **Time created**, **State**, or **Datasets** drop-down menus respectively.

![Filter runs](https://docs.databricks.com/aws/en/assets/images/quick-start-nb-experiment-4738b3f9a806bff5043de7497d29d62a.png)

## Download runs[​](#download-runs "Direct link to Download runs")

You can download runs from the Experiment details page as follows:

1.  Click ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) to open the kebab menu.
    
    ![Kebab menu with download options on Experiments page.](https://docs.databricks.com/aws/en/assets/images/download-runs-f60b5fd156b503f0114d2a1fd96f992b.png)
    
2.  To download a file in CSV format containing all runs shown (up to a maximum of 100), select **Download `<n>` runs**. MLflow creates and downloads a file with one run per row, containing the following fields for each run:
    
        Start Time, Duration, Run ID, Name, Source Type, Source Name, User, Status, <parameter1>, <parameter2>, ..., <metric1>, <metric2>, ...
    
3.  If you want to download more than 100 runs or want to download runs programmatically, select **Download all runs**. A dialog opens showing a code snippet that you can copy or open in a notebook. After you run this code in a notebook cell, select **Download all rows** from the cell output.
    

## Delete runs[​](#delete-runs "Direct link to Delete runs")

You can delete runs from the experiment details page following these steps:

1.  In the experiment, select one or more runs by clicking in the checkbox to the left of the run.
2.  Click **Delete**.
3.  If the run is a parent run, decide whether you also want to delete descendant runs. This option is selected by default.
4.  Click **Delete** to confirm. Deleted runs are saved for 30 days. To display deleted runs, select **Deleted** in the State field.

### Bulk delete runs based on the creation time[​](#bulk-delete-runs-based-on-the-creation-time "Direct link to bulk-delete-runs-based-on-the-creation-time")

You can use Python to bulk delete runs of an experiment that were created prior to or at a UNIX timestamp. Using Databricks Runtime 14.1 or later, you can call the `mlflow.delete_runs` API to delete runs and return the number of runs deleted.

The following are the `mlflow.delete_runs` parameters:

*   `experiment_id`: The ID of the experiment containing the runs to delete.
*   `max_timestamp_millis`: The maximum creation timestamp in milliseconds since the UNIX epoch for deleting runs. Only runs created prior to or at this timestamp are deleted.
*   `max_runs`: Optional. A positive integer that indicates the maximum number of runs to delete. The maximum allowed value for max\_runs is 10000. If not specified, `max_runs` defaults to 10000.

Python

    import mlflow# Replace <experiment_id>, <max_timestamp_ms>, and <max_runs> with your values.runs_deleted = mlflow.delete_runs(  experiment_id=<experiment_id>,  max_timestamp_millis=<max_timestamp_ms>,  max_runs=<max_runs>)# Example:runs_deleted = mlflow.delete_runs(  experiment_id="4183847697906956",  max_timestamp_millis=1711990504000,  max_runs=10)

Using Databricks Runtime 13.3 LTS or earlier, you can run the following client code in a Databricks Notebook.

Python

    from typing import Optionaldef delete_runs(experiment_id: str,                max_timestamp_millis: int,                max_runs: Optional[int] = None) -> int:    """    Bulk delete runs in an experiment that were created prior to or at the specified timestamp.    Deletes at most max_runs per request.    :param experiment_id: The ID of the experiment containing the runs to delete.    :param max_timestamp_millis: The maximum creation timestamp in milliseconds                                 since the UNIX epoch for deleting runs. Only runs                                 created prior to or at this timestamp are deleted.    :param max_runs: Optional. A positive integer indicating the maximum number                     of runs to delete. The maximum allowed value for max_runs                     is 10000. If not specified, max_runs defaults to 10000.    :return: The number of runs deleted.    """    from mlflow.utils.databricks_utils import get_databricks_host_creds    from mlflow.utils.request_utils import augmented_raise_for_status    from mlflow.utils.rest_utils import http_request    json_body = {"experiment_id": experiment_id, "max_timestamp_millis": max_timestamp_millis}    if max_runs is not None:        json_body["max_runs"] = max_runs    response = http_request(        host_creds=get_databricks_host_creds(),        endpoint="/api/2.0/mlflow/databricks/runs/delete-runs",        method="POST",        json=json_body,    )    augmented_raise_for_status(response)    return response.json()["runs_deleted"]

See the Databricks Experiments API documentation for parameters and return value specifications for [deleting runs based on creation time](https://docs.databricks.com/api/workspace/experiments/deleteruns).

## Restore runs[​](#restore-runs "Direct link to Restore runs")

You can restore previously deleted runs from the UI as follows:

1.  On the **Experiment** page, in the **State** field, select **Deleted** to display deleted runs.
2.  Select one or more runs by clicking in the checkbox to the left of the run.
3.  Click **Restore**.
4.  Click **Restore** to confirm. The restored runs now appear when you select **Active** in the State field.

### Bulk restore runs based on the deletion time[​](#bulk-restore-runs-based-on-the-deletion-time "Direct link to bulk-restore-runs-based-on-the-deletion-time")

You can also use Python to bulk restore runs of an experiment that were deleted at or after a UNIX timestamp. Using Databricks Runtime 14.1 or later, you can call the `mlflow.restore_runs` API to restore runs and return the number of restored runs.

The following are the `mlflow.restore_runs` parameters:

*   `experiment_id`: The ID of the experiment containing the runs to restore.
*   `min_timestamp_millis`: The minimum deletion timestamp in milliseconds since the UNIX epoch for restoring runs. Only runs deleted at or after this timestamp are restored.
*   `max_runs`: Optional. A positive integer that indicates the maximum number of runs to restore. The maximum allowed value for max\_runs is 10000. If not specified, max\_runs defaults to 10000.

Python

    import mlflow# Replace <experiment_id>, <min_timestamp_ms>, and <max_runs> with your values.runs_restored = mlflow.restore_runs(  experiment_id=<experiment_id>,  min_timestamp_millis=<min_timestamp_ms>,  max_runs=<max_runs>)# Example:runs_restored = mlflow.restore_runs(  experiment_id="4183847697906956",  min_timestamp_millis=1711990504000,  max_runs=10)

Using Databricks Runtime 13.3 LTS or earlier, you can run the following client code in a Databricks Notebook.

Python

    from typing import Optionaldef restore_runs(experiment_id: str,                 min_timestamp_millis: int,                 max_runs: Optional[int] = None) -> int:    """    Bulk restore runs in an experiment that were deleted at or after the specified timestamp.    Restores at most max_runs per request.    :param experiment_id: The ID of the experiment containing the runs to restore.    :param min_timestamp_millis: The minimum deletion timestamp in milliseconds                                 since the UNIX epoch for restoring runs. Only runs                                 deleted at or after this timestamp are restored.    :param max_runs: Optional. A positive integer indicating the maximum number                     of runs to restore. The maximum allowed value for max_runs                     is 10000. If not specified, max_runs defaults to 10000.    :return: The number of runs restored.    """    from mlflow.utils.databricks_utils import get_databricks_host_creds    from mlflow.utils.request_utils import augmented_raise_for_status    from mlflow.utils.rest_utils import http_request    json_body = {"experiment_id": experiment_id, "min_timestamp_millis": min_timestamp_millis}    if max_runs is not None:        json_body["max_runs"] = max_runs    response = http_request(        host_creds=get_databricks_host_creds(),        endpoint="/api/2.0/mlflow/databricks/runs/restore-runs",        method="POST",        json=json_body,    )    augmented_raise_for_status(response)    return response.json()["runs_restored"]

See the Databricks Experiments API documentation for parameters and return value specifications for [restoring runs based on deletion time](https://docs.databricks.com/api/workspace/experiments/restoreruns).

## Compare runs[​](#compare-runs "Direct link to compare-runs")

You can compare runs from a single experiment or from multiple experiments. The **Comparing Runs** page presents information about the selected runs in tabular format. You can also create visualizations of run results and tables of run information, run parameters, and metrics. See [Compare MLflow runs and models using graphs and charts](https://docs.databricks.com/aws/en/mlflow/visualize-runs).

The **Parameters** and **Metrics** tables display the run parameters and metrics from all selected runs. The columns in these tables are identified by the **Run details** table immediately above. For simplicity, you can hide parameters and metrics that are identical in all selected runs by toggling ![Show diff only button](data:image/png;base64,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).

![compare runs page tables](https://docs.databricks.com/aws/en/assets/images/mlflow-run-comparison-table-679629ac4bc7d03b07476fa599d549de.png)

### Compare runs from a single experiment[​](#compare-runs-from-a-single-experiment "Direct link to Compare runs from a single experiment")

1.  On the [experiment details page](https://docs.databricks.com/aws/en/mlflow/experiments), select two or more runs by clicking in the checkbox to the left of the run, or select all runs by checking the box at the top of the column.
2.  Click **Compare**. The Comparing `<N>` Runs screen appears.

### Compare runs from multiple experiments[​](#compare-runs-from-multiple-experiments "Direct link to compare-runs-from-multiple-experiments")

1.  On the [experiments page](https://docs.databricks.com/aws/en/mlflow/experiments), select the experiments you want to compare by clicking in the box at the left of the experiment name.
2.  Click **Compare (n)** (**n** is the number of experiments you selected). A screen appears showing all of the runs from the experiments you selected.
3.  Select two or more runs by clicking in the checkbox to the left of the run, or select all runs by checking the box at the top of the column.
4.  Click **Compare**. The Comparing `<N>` Runs screen appears.

### Compare runs using system tables[​](#compare-runs-using-system-tables "Direct link to compare-runs-using-system-tables")

MLflow metadata for experiments and runs is also available in system tables, where you can leverage [Databricks SQL](https://docs.databricks.com/aws/en/sql/) and all the lakehouse tooling Databricks offers to analyze your experiment data. For more details, see [MLflow system tables reference](https://docs.databricks.com/aws/en/admin/system-tables/mlflow).

## Copy runs between workspaces[​](#copy-runs-between-workspaces "Direct link to Copy runs between workspaces")

To import or export MLflow runs to or from your Databricks workspace, you can use the community-driven open source project [MLflow Export-Import](https://github.com/mlflow/mlflow-export-import#why-use-mlflow-export-import).
