---
title: Organize training runs with MLflow experiments | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow/experiments
ingestedAt: "2026-06-18T08:14:00.264Z"
---

Experiments are units of organization for your MLflow runs, including agent traces, LLM application evaluations, and [model training runs](https://docs.databricks.com/aws/en/mlflow/runs). There are two types of experiments: workspace and notebook.

*   You can create a workspace experiment from the Databricks UI or the MLflow API. Workspace experiments are not associated with any notebook, and any notebook can log a run to these experiments by using the experiment ID or the experiment name.
*   A notebook experiment is associated with a specific notebook. Databricks automatically creates a notebook experiment if there is no active experiment when you start a run using [mlflow.start\_run()](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.start_run).

To see all of the experiments in a workspace that you have access to, in the sidebar, under **AI/ML**, click **Experiments**.

![Experiments page](https://docs.databricks.com/aws/en/assets/images/experiments-page-982bbf32c5a22bf2892492573c84678a.png)

## Create workspace experiment[​](#create-workspace-experiment "Direct link to create-workspace-experiment")

This section describes how to create a workspace experiment using the Databricks UI. You can create a workspace experiment directly [from the workspace](#create-expt-from-workspace) or [from the Experiments page](#create-expt-from-expts-page).

You can also use the [MLflow API](https://mlflow.org/docs/latest/index.html), or the [Databricks Terraform provider](https://docs.databricks.com/aws/en/dev-tools/terraform/) with [databricks\_mlflow\_experiment](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/mlflow_experiment).

For instructions on logging runs to workspace experiments, see [Log runs and models to an experiment](https://docs.databricks.com/aws/en/mlflow/tracking#mlflow-recording-runs).

### Create experiment from the workspace[​](#create-experiment-from-the-workspace "Direct link to create-experiment-from-the-workspace")

1.  Click ![Workspace Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAHqADAAQAAAABAAAAHgAAAADKQTcFAAAA3UlEQVRIDWNUsHT6zzAAgGkA7ARbOWox3UJ+wIKaBZ8X7x/bi0+aoNyl6zcZkourGd58eI+hlqY+1tNUZ5jb24phKUgAr49hOhStnMFMWAjA+DB5bLQwvwDDme1rGUCWYwM08/Hbjx+w2QcXw+pjmM9gqtD5MHFKaJr5mJCjsFoMikPkeETnEzKUGHmsFhOjkVI1A2bxaOICRx16YkLnUxq/IP0DFscDZvFo4hr6iQtULeIDWOMYXQN67YTOR1ePzAe1QrABmqZqWNMHm8WMoz0JbMFCCzGaxjE+BwMA4fU485n7fpkAAAAASUVORK5CYII=) **Workspace** in the sidebar.
    
2.  Navigate to the folder in which you want to create the experiment.
    
3.  Right-click on the folder and select **Create > MLflow experiment**.
    
4.  In the Create MLflow Experiment dialog, enter a name for the experiment and an optional artifact location. If you do not specify an artifact location, artifacts are stored in MLflow-managed artifact storage: `dbfs:/databricks/mlflow-tracking/<experiment-id>`.
    
    For workspaces enabled for Unity Catalog, you can also store artifacts in a Unity Catalog volume. To store artifacts in your own cloud storage, create a Unity Catalog external volume.
    
    To store artifacts in a Unity Catalog volume, specify a volume path of the form `dbfs:/Volumes/catalog_name/schema_name/volume_name/user/specified/path` as your MLflow experiment artifact location, either in the UI or as shown in the following code:
    
    Python
    
        import mlflow # Storing artifacts in a volume requires MLflow 2.15.0 or aboveEXP_NAME = "/Users/first.last@databricks.com/my_experiment_name"CATALOG = "my_catalog"SCHEMA = "my_schema"VOLUME = "my_volume"ARTIFACT_PATH = f"dbfs:/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}" # can be a managed or external volumemlflow.set_tracking_uri("databricks")mlflow.set_registry_uri("databricks-uc")if mlflow.get_experiment_by_name(EXP_NAME) is None:    mlflow.create_experiment(name=EXP_NAME, artifact_location=ARTIFACT_PATH)mlflow.set_experiment(EXP_NAME)
    
    If your workspace is not enabled for Unity Catalog, or you do not have access to MLflow 2.15.0 or above, specify a path in this format: `dbfs:/path/to/artifacts`.
    
    Databricks recommends using a Unity Catalog volume for artifact storage. If neither a Unity Catalog volume nor DBFS is a suitable option, you can also store artifacts directly to S3 (not recommended). To store artifacts in S3, specify a URI of the form `s3://<bucket>/<path>`. MLflow obtains credentials to access S3 from your cluster's [instance profile](https://docs.databricks.com/aws/en/archive/storage/tutorial-s3-instance-profile). Artifacts stored in S3 do not appear in the MLflow UI; you must download them using an object storage client.
    
    The upload and download file size limits are both 5GB.
    
    note
    
    When you store an artifact in a location other than MLflow-managed DBFS (default) or Unity Catalog volumes, the artifact does not appear in the MLflow UI. Models stored in locations other than these cannot be registered in Model Registry.
    
5.  Click **Create**. The experiment details page for the new experiment appears.
    
6.  To log runs to this experiment, call `mlflow.set_experiment()` with the experiment path. To display the experiment path, click the information icon ![information icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAFKADAAQAAAABAAAAFAAAAACy3fD9AAABF0lEQVQ4Ec2SPRIBQRCFh3IPClX2FjJCbkAqlYhlXICUEyBDxCmsqvV3kuUb1XTNmC2BwAvofd3zZrpf59IHzA+R/6GWlfp/wUJWy/HpalbbvYmTmy2LqkVTK5dMu1kPHgsKjqdzK4SICB3PzwtQC4risovFepd2+8P0kFzcVCq50WTm5SCMy8oB/gXE+puLQhd6LtMWLeqWpG0ZXFQp2Rrm68ITxAAGryGmaI74E+8JUsgrNbQZwruXCu8J0t43kNG4tZ5gq1G3rbCDAjj9ouXmuZuak1rPZZxlJXBROyuOi8OfctTk+Hmpq4BX4KJeatIYATfodVT1OwwKUoIosxI3EaJ91iaETMHQoSzeMyWr+Jvc/wveAcuVOvV05H7lAAAAAElFTkSuQmCC) to the right of the experiment name. See [Log runs and models to an experiment](https://docs.databricks.com/aws/en/mlflow/tracking#mlflow-recording-runs) for details and an example notebook.
    

### Create experiment from the Experiments page[​](#create-experiment-from-the-experiments-page "Direct link to create-experiment-from-the-experiments-page")

To create a foundation model fine-tuning, AutoML, or custom experiment, click **Experiments** or select **New > Experiment** in the left sidebar.

At the top of the page, select one of the following options to configure an experiment:

*   **Foundation Model Fine-tuning**. The **Foundation Model Fine-tuning** dialog appears. For details, see [Create a training run using the Foundation Model Fine-tuning UI (deprecated)](https://docs.databricks.com/aws/en/large-language-models/foundation-model-training/ui).
*   **Forecasting**. The **Configure Forecasting experiment** dialog appears. For details, see [Configure the AutoML experiment](https://docs.databricks.com/aws/en/machine-learning/automl/forecasting#configure).
*   **Classification**. The **Configure Classification experiment** dialog appears. For details, see [Set up classification experiment with the UI](https://docs.databricks.com/aws/en/machine-learning/automl/classification#setup).
*   **Regression**. The **Configure Classification experiment** dialog appears. For details, see [Set up regression experiment with the UI](https://docs.databricks.com/aws/en/machine-learning/automl/regression#setup).
*   **Custom**. The **Create MLflow Experiment** dialog appears. For details, see Step 4 in [Create experiment from the workspace](#create-expt-from-workspace).

## Create notebook experiment[​](#create-notebook-experiment "Direct link to create-notebook-experiment")

When you use the [mlflow.start\_run() command](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.start_run) in a notebook, the run logs metrics and parameters to the active experiment. If no experiment is active, Databricks creates a notebook experiment. A notebook experiment shares the same name and ID as its corresponding notebook. The notebook ID is the numerical identifier at the end of a [Notebook URL and ID](https://docs.databricks.com/aws/en/workspace/workspace-details#workspace-notebook-url).

note

Users running MLflow on compute with [dedicated group access](https://docs.databricks.com/aws/en/compute/group-access) must verify the group has permission to write to the directory where the notebook lives, or use `mlflow.set_tracking_uri("<path>")` to specify a folder for MLflow to write to.

Alternatively, you can pass a Databricks workspace path to an existing notebook in [mlflow.set\_experiment()](https://www.mlflow.org/docs/latest/python_api/mlflow.html?highlight=set_experiment#mlflow.set_experiment) to create a notebook experiment for it.

For instructions on logging runs to notebook experiments, see [Log runs and models to an experiment](https://docs.databricks.com/aws/en/mlflow/tracking#mlflow-recording-runs).

note

If you delete a notebook experiment using the API (for example, `MlflowClient.tracking.delete_experiment()` in Python), the notebook itself is moved into the Trash folder.

## View experiments[​](#view-experiments "Direct link to view-experiments")

Each experiment that you have access to appears on the experiments page. From this page, you can view any experiment. Click on an experiment name to display the experiment details page.

Additional ways to access the experiment details page:

*   You can access the experiment details page for a workspace experiment from the workspace menu.
*   You can access the experiment details page for a notebook experiment from the notebook.

To search for experiments, type text in the **Filter experiments** field and press **Enter** or click the magnifying glass icon. The experiment list changes to show only those experiments that contain the search text in the **Name** or **Location** columns.

For advanced usage, you can enter a search query for `` tags.`mlflow.note.content` `` to search based on the **Description** column. For further details on syntax, see [Search Experiments](https://mlflow.org/docs/latest/ml/search/search-experiments/). Please note that unlike searching for **Name** or **Location**, searching through tags requires you to manually construct the search query with an identifier and comparator. It will not directly return all results that contain the search text.

Click the name of any experiment in the table to display its experiment details page:

![View experiment](https://docs.databricks.com/aws/en/assets/images/quick-start-nb-experiment-4738b3f9a806bff5043de7497d29d62a.png)

The experiment details page lists all runs associated with the experiment. From the table, you can open the run page for any run associated with the experiment by clicking its **Run Name**. The **Source** column gives you access to the notebook version that created the run. You can also search and [filter](https://docs.databricks.com/aws/en/mlflow/runs#filter-runs) runs by metrics or parameter settings.

### View workspace experiment[​](#view-workspace-experiment "Direct link to view-workspace-experiment")

1.  Click ![Workspace Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAHqADAAQAAAABAAAAHgAAAADKQTcFAAAA3UlEQVRIDWNUsHT6zzAAgGkA7ARbOWox3UJ+wIKaBZ8X7x/bi0+aoNyl6zcZkourGd58eI+hlqY+1tNUZ5jb24phKUgAr49hOhStnMFMWAjA+DB5bLQwvwDDme1rGUCWYwM08/Hbjx+w2QcXw+pjmM9gqtD5MHFKaJr5mJCjsFoMikPkeETnEzKUGHmsFhOjkVI1A2bxaOICRx16YkLnUxq/IP0DFscDZvFo4hr6iQtULeIDWOMYXQN67YTOR1ePzAe1QrABmqZqWNMHm8WMoz0JbMFCCzGaxjE+BwMA4fU485n7fpkAAAAASUVORK5CYII=) **Workspace** in the sidebar.
2.  Go to the folder containing the experiment.
3.  Click the experiment name.

### View notebook experiment[​](#view-notebook-experiment "Direct link to view-notebook-experiment")

In the notebook's right sidebar, click the **Experiment** icon ![Experiment icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAVCAYAAACpF6WWAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAFaADAAQAAAABAAAAFQAAAAAIGxIOAAABUUlEQVQ4EWP8DwQMVAZMVDYPbBxNDGUh5NL04jqGe4+eoChTkpNhmNnbhCKGzCFoKMhAYz0tBgMdDbC+C1duMJy9dA3ZDAw2QUNBOkAGRgT6wDUTMpQmYTpMDP0HzRdMjIzw8ISx8eUZvN4/eeYC2DBREWG4oTD2qfOX4GLoDEZc2XTf4RMMnVPmMPz7948hOtiXgYOdFaz3x49fDEvXbWFgYmJiqMhLYXC0tkA3kwHDUJCXFyxfx7B8/VYMxdgEQBbGhwcwMCIFEQPIpchgzaYd/11CEv9Pmr3o/9+/f5GlUNggud5pc8Fq123ZhSKHYWhoYv7/lr5pKIrwcRq7J/+PTC9GUYKRo8TFhRkePXnOsGL9Fmy+xRB78uwlg7iIEIo4RpjeuHWXoWvqXIbHz16gKMTFkZeWZCjNTWFQV1aEK8EwFC5DAQNvOiXX3KFjKAAbsvOWj3bmtQAAAABJRU5ErkJggg==).

The Experiment Runs sidebar appears and shows a summary of each run associated with the notebook experiment, including run parameters and metrics. At the top of the sidebar is the name of the experiment that the notebook most recently logged runs to (either a notebook experiment or a workspace experiment).

![View run parameters and metrics](https://docs.databricks.com/aws/en/assets/images/mlflow-notebook-revision-bb9ffd483a940486a363e5871b55f7d3.png)

From the sidebar, you can navigate to the experiment details page or directly to a run.

*   To view the experiment, click ![External Link](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAXCAYAAAARIY8tAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAGKADAAQAAAABAAAAFwAAAABgZeJ8AAAA8ElEQVRIDWP8DwQMNARMNDQbbDTNLWAh1wfKxdswtN7t9cIQw2pB1LQTDCfvvsNQDBKAGZLnrgqWP3nnLU61IAVYLQAZbq4sxGCuIgw2BBuR76bKMHHXbbyG47QAJAEyHGQILgAyfNLO2wwwn4DY2ABZkYxsOD5HgC0E5QN0oFS09f+EnbfQhcF8kDg+eXRNJPkAFDewYCHocmh4kWQBKOKXZVmgxA0ouLAlWVh8kGQBSBPIElIAyRaQYjhI7dC3AGtOBnkNVARMBDEIAJA6fACrBaCIBCVJXOURuoH4Ip4RlDHQNVCTP/QjedQHBNMDAL0aoP7asXF1AAAAAElFTkSuQmCC) at the far right, next to **Experiment Runs**.
*   To display a [run](https://docs.databricks.com/aws/en/mlflow/runs), click the name of the run.

## Manage experiments[​](#manage-experiments "Direct link to Manage experiments")

You can rename, delete, or manage permissions for an experiment you own from the experiments page, the [experiment details page](#experiment-page), or the workspace menu.

note

You cannot directly rename, delete, or manage permissions on an MLflow experiment that was created by a notebook in a Databricks Git folder. You must perform these actions at the Git folder level.

### Rename experiment[​](#rename-experiment "Direct link to Rename experiment")

You can rename an experiment that you own from the [**Experiments** page](#experiment-page) or from the experiment details page for that experiment.

*   On the **Experiments** page, click the kebab menu ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) in the rightmost column and then click **Rename**.

![Rename from the Experiments page.](https://docs.databricks.com/aws/en/assets/images/expts-page-change-permission-736f0ea10742672b6693d95e105199ab.png)

*   On the experiment details page, click the kebab menu ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) next to **Permissions** and then click **Rename**.

![Rename from the experiment details page.](https://docs.databricks.com/aws/en/assets/images/expt-page-kebab-270fc13781d89ffe0ab53163df6e1848.png)

You can rename a workspace experiment from the workspace. Right-click the experiment name and then click **Rename**.

### Get experiment ID and path to experiment[​](#get-experiment-id-and-path-to-experiment "Direct link to get-experiment-id-and-path-to-experiment")

On the experiment details page, you can get the path to a notebook experiment by clicking the information icon ![information icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAFKADAAQAAAABAAAAFAAAAACy3fD9AAABF0lEQVQ4Ec2SPRIBQRCFh3IPClX2FjJCbkAqlYhlXICUEyBDxCmsqvV3kuUb1XTNmC2BwAvofd3zZrpf59IHzA+R/6GWlfp/wUJWy/HpalbbvYmTmy2LqkVTK5dMu1kPHgsKjqdzK4SICB3PzwtQC4risovFepd2+8P0kFzcVCq50WTm5SCMy8oB/gXE+puLQhd6LtMWLeqWpG0ZXFQp2Rrm68ITxAAGryGmaI74E+8JUsgrNbQZwruXCu8J0t43kNG4tZ5gq1G3rbCDAjj9ouXmuZuak1rPZZxlJXBROyuOi8OfctTk+Hmpq4BX4KJeatIYATfodVT1OwwKUoIosxI3EaJ91iaETMHQoSzeMyWr+Jvc/wveAcuVOvV05H7lAAAAAElFTkSuQmCC) to the right of the experiment name. A pop-up note appears that shows the path to the experiment, the experiment ID, and the artifact location. You can use the experiment ID in the MLflow command `set_experiment` to set the active MLflow experiment.

![Experiment name icon](https://docs.databricks.com/aws/en/assets/images/get-experiment-path-eeff100bddf07e213082f11eb4a07f76.png)

From a notebook, you can copy the full path of the experiment by clicking ![Path icon.](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAHKADAAQAAAABAAAAHAAAAABkvfSiAAAAzUlEQVRIDWP8DwQMdARMdLQLbNWohVQP8eEfpCy4wqxz+kKGG3ce4pIGi2uoyDOUZ8bjVYMuidNCkGUgA9WVFND1gPk37z0g6CBsGnFaCFIMsizA3R6bPoYNOxnIspDuiQavD5G9hitOE4ub4MqIiVOiLaRWnBJtIcgb1IjTwRWHoKQPSo3UBDiDFJQAQPFGKPOT6hicFqKXIMipkVRLkNUPrjhEdhmIjS9OQXLEAJxBiq6ZmDgFqSEEGEcbUYSCiFR5uqfSUQtJjSKC6gGwl0oAR4OWnAAAAABJRU5ErkJggg==) in the notebook's experiment sidebar.

![Experiment path icon in notebook sidebar.](https://docs.databricks.com/aws/en/assets/images/get-experiment-name-00b973b42b67491e8fcf3ff074911cda.png)

### Delete notebook experiment[​](#delete-notebook-experiment "Direct link to Delete notebook experiment")

Notebook experiments are part of the notebook and cannot be deleted separately. When you [delete a notebook](https://docs.databricks.com/aws/en/notebooks/notebooks-manage#delete-a-notebook), the associated notebook experiment is deleted. When you delete a notebook experiment using the UI, the notebook is also deleted.

To delete notebook experiments using the API, use the [Workspace API](https://docs.databricks.com/api/workspace/introduction) to ensure both the notebook and experiment are deleted from the workspace.

### Delete a workspace or notebook experiment[​](#delete-a-workspace-or-notebook-experiment "Direct link to Delete a workspace or notebook experiment")

You can delete an experiment that you own from the [experiments page](#experiment-page) or from the experiment details page.

important

When you delete a notebook experiment, the notebook is also deleted.

*   On the **Experiments** page, click the kebab menu ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) in the rightmost column and then click **Delete**.

![Delete from experiments page.](https://docs.databricks.com/aws/en/assets/images/expts-page-change-permission-736f0ea10742672b6693d95e105199ab.png)

*   On the experiment details page, click the kebab menu ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) next to **Permissions** and then click **Delete**.

![Delete from experiment details page.](https://docs.databricks.com/aws/en/assets/images/expt-page-kebab-270fc13781d89ffe0ab53163df6e1848.png)

You can delete a workspace experiment from the workspace. Right-click the experiment name and then click **Move to Trash**.

### Change permissions for an experiment[​](#change-permissions-for-an-experiment "Direct link to change-permissions-for-an-experiment")

To change permissions for an experiment from the [experiment details page](#experiment-page), click **Permissions**.

![Experiment details page permissions menu](https://docs.databricks.com/aws/en/assets/images/expt-permission-1943b7275556ce8f16211124dab1d4e1.png)

You can change permissions for an experiment that you own from the [**Experiments** page](#experiment-page). Click the kebab menu ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) in the rightmost column and then click **Permissions**.

![Change permissions from the Experiments page.](https://docs.databricks.com/aws/en/assets/images/expts-page-change-permission-736f0ea10742672b6693d95e105199ab.png)

For information on experiment permission levels, see [MLflow experiment ACLs](https://docs.databricks.com/aws/en/security/auth/access-control/#experiments).

## Copy experiments between workspaces[​](#copy-experiments-between-workspaces "Direct link to Copy experiments between workspaces")

To migrate MLflow experiments between workspaces, you can use the community-driven open source project [MLflow Export-Import](https://github.com/mlflow/mlflow-export-import#why-use-mlflow-export-import).

With these tools, you can:

*   Share and collaborate with other data scientists in the same or another tracking server. For example, you can clone an experiment from another user into your workspace.
*   Copy MLflow experiments and runs from your local tracking server to your Databricks workspace.
*   Back up mission critical experiments and models to another Databricks workspace.
