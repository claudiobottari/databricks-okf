---
title: Forecasting with AutoML (classic compute) | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/automl/forecasting
ingestedAt: "2026-06-18T08:09:32.048Z"
---

Use AutoML to automatically finding the best forecasting algorithm and hyperparameter configuration to predict values based on time-series data.

Time series forecasting is only available for Databricks Runtime 10.0 ML or above.

## Set up forecasting experiment with the UI[​](#set-up-forecasting-experiment-with-the-ui "Direct link to Set up forecasting experiment with the UI")

You can set up a forecasting problem using the AutoML UI with the following steps:

1.  In the sidebar, select **Experiments**.
2.  In the **Forecasting** card, select **Start training**.

The forecasting UI defaults to [serverless forecasting](https://docs.databricks.com/aws/en/machine-learning/train-model/serverless-forecasting). To access forecasting with your own compute, select **revert back to the old experience**.

## Configure the AutoML experiment[​](#configure-the-automl-experiment "Direct link to configure-the-automl-experiment")

1.  The **Configure AutoML experiment page** displays. On this page, you configure the AutoML process, specifying the dataset, problem type, target or label column to predict, metric to use to evaluate and score the experiment runs, and stopping conditions.
    
2.  In the **Compute** field, select a cluster running Databricks Runtime 10.0 ML or above.
    
3.  Under **Dataset**, click **Browse**. Navigate to the table you want to use and click **Select**. The table schema appears.
    
4.  Click in the **Prediction target** field. A dropdown menu appears, listing the columns shown in the schema. Select the column you want the model to predict.
    
5.  Click in the **Time column** field. A drop-down appears showing the dataset columns that are of type `timestamp` or `date`. Select the column containing the time periods for the time series.
    
6.  For multi-series forecasting, select the column(s) that identify the individual time series from the **Time series identifiers** drop-down. AutoML groups the data by these columns as different time series and trains a model for each series independently. If you leave this field blank, AutoML assumes that the dataset contains a single time series.
    
7.  In the **Forecast horizon and frequency** fields, specify the number of time periods into the future for which AutoML should calculate forecasted values. In the left box, enter the integer number of periods to forecast. In the right box, select the units.
    
    note
    
    To use Auto-ARIMA, the time series must have a regular frequency where the interval between any two points must be the same throughout the time series. The frequency must match the frequency unit specified in the API call or in the AutoML UI. AutoML handles missing time steps by filling in those values with the previous value.
    
8.  In Databricks Runtime 11.3 LTS ML and above, you can save prediction results. To do so, specify a database in the **Output Database** field. Click **Browse** and select a database from the dialog. AutoML writes the prediction results to a table in this database.
    
9.  The **Experiment name** field shows the default name. To change it, type the new name in the field.
    

You can also:

*   Specify [additional configuration options](#advanced-config).
*   Use [existing feature tables in Feature Store to augment the original input dataset](https://docs.databricks.com/aws/en/machine-learning/automl/feature-store-integration).

## Advanced configurations[​](#advanced-configurations "Direct link to advanced-configurations")

Open the **Advanced Configuration (optional)** section to access these parameters.

*   The evaluation metric is the [primary metric](https://docs.databricks.com/aws/en/machine-learning/automl/automl-api-reference) used to score the runs.
*   In Databricks Runtime 10.4 LTS ML and above, you can exclude training frameworks from consideration. By default, AutoML trains models using frameworks listed under [AutoML algorithms](https://docs.databricks.com/aws/en/machine-learning/automl/#automl-algorithm).
*   You can edit the stopping conditions. Default stopping conditions are:
    *   For forecasting experiments, stop after 120 minutes.
    *   In Databricks Runtime 10.4 LTS ML and below, for classification and regression experiments, stop after 60 minutes or after completing 200 trials, whichever happens first. For Databricks Runtime 11.0 ML and above, the number of trials is not used as a stopping condition.
    *   In Databricks Runtime 10.4 LTS ML and above, for classification and regression experiments, AutoML incorporates early stopping; it stops training and tuning models if the validation metric is no longer improving.
*   In Databricks Runtime 10.4 LTS ML and above, you can select a `time column` to split the data for training, validation, and testing in chronological order (applies only to [classification](https://docs.databricks.com/aws/en/machine-learning/automl/classification-data-prep#control-automl-split) and [regression](https://docs.databricks.com/aws/en/machine-learning/automl/regression-data-prep#control-automl-split)).
*   Databricks recommends leaving the **Data directory** field empty. Not populating this field triggers the default behavior of securely storing the dataset as an MLflow artifact. A [DBFS](https://docs.databricks.com/aws/en/dbfs/) path can be specified, but in this case, the dataset does not inherit the AutoML experiment's access permissions.

## Run the experiment and monitor the results[​](#run-the-experiment-and-monitor-the-results "Direct link to Run the experiment and monitor the results")

To start the AutoML experiment, click **Start AutoML**. The experiment starts to run, and the AutoML training page appears. To refresh the runs table, click ![Refresh button](data:image/png;base64,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).

### View experiment progress[​](#view-experiment-progress "Direct link to View experiment progress")

From this page, you can:

*   Stop the experiment at any time.
*   Open the data exploration notebook.
*   Monitor runs.
*   Navigate to the run page for any run.

With Databricks Runtime 10.1 ML and above, AutoML displays warnings for potential issues with the dataset, such as unsupported column types or high cardinality columns.

note

Databricks does its best to indicate potential errors or issues. However, this may not be comprehensive and may not capture the issues or errors you may be searching for.

To see any warnings for the dataset, click the **Warnings** tab on the training page or the experiment page after the experiment completes.

![AutoML warnings](https://docs.databricks.com/aws/en/assets/images/automl-alerts-3b3174dee68bf42059085aecad29b49d.png)

### View results[​](#view-results "Direct link to View results")

When the experiment completes, you can:

*   [Register and deploy](#register-deploy-automl-ui) one of the models with MLflow.
*   Select **View notebook for best model** to review and edit the notebook that created the best model.
*   Select **View data exploration notebook** to open the data exploration notebook.
*   Search, filter, and sort the runs in the runs table.
*   See details for any run:
    *   The generated notebook containing source code for a trial run can be found by clicking into the MLflow run. The notebook is saved in the **Artifacts** section of the run page. You can download this notebook and import it into the workspace, if downloading artifacts is enabled by your workspace administrators.
    *   To view the run results, click in the **Models** column or the **Start Time** column. The run page appears, showing information about the trial run (such as parameters, metrics, and tags) and artifacts created by the run, including the model. This page also includes code snippets that you can use to make predictions with the model.

To return to this AutoML experiment later, find it in the table on the [Experiments page](https://docs.databricks.com/aws/en/mlflow/experiments). The results of each AutoML experiment, including the data exploration and training notebooks, are stored in a `databricks_automl` folder in the [home folder](https://docs.databricks.com/aws/en/workspace/workspace-browser#home-folder) of the user who ran the experiment.

## Register and deploy a model[​](#register-and-deploy-a-model "Direct link to register-and-deploy-a-model")

Register and deploy your model using the AutoML UI. When a run completes, the top row shows the best model based on the primary metric.

1.  Select the link in the **Models** column for the model you want to register.
2.  Select ![register model button](data:image/png;base64,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) to register it to Unity Catalog or [Model Registry](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/).
    
    note
    
    Databricks recommends you register models to Unity Catalog for the latest features.
    
3.  After registration, you can deploy the model to a [custom model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints).

### No module named 'pandas.core.indexes.numeric[​](#no-module-named-pandascoreindexesnumeric "Direct link to No module named 'pandas.core.indexes.numeric")

When serving a model built using AutoML with Model Serving, you may get the error: `No module named 'pandas.core.indexes.numeric`.

This is due to an incompatible `pandas` version between AutoML and the model serving endpoint environment. You can resolve this error by running the [add-pandas-dependency.py script](https://docs.databricks.com/aws/en/assets/files/add-pandas-dependency-4808dc9dcdfb035bdca6ebce6b86d719.py). The script edits the `requirements.txt` and `conda.yaml` for your logged model to include the appropriate `pandas` dependency version: `pandas==1.5.3`

1.  Modify the script to include the `run_id` of the MLflow run where your model was logged.
2.  Re-register the model to Unity Catalog or the model registry.
3.  Try serving the new version of the MLflow model.

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Forecasting API](https://docs.databricks.com/aws/en/machine-learning/automl/forecasting-train-api)
*   [Forecasting data preparation settings](https://docs.databricks.com/aws/en/machine-learning/automl/forecasting-data-prep)
*   [Forecast with covariates](https://docs.databricks.com/aws/en/machine-learning/automl/automl-covariate-forecast)
