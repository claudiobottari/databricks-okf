---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2e91cbf2f34a6002d3e5e34ab0fb4594d1b60c6606379c99503702f2a0127bac
  pageDirectory: concepts
  sources:
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-forecasting-experiment-classic-compute
    - AFE(C
  citations:
    - file: forecasting-with-automl-classic-compute-databricks-on-aws.md
title: AutoML Forecasting Experiment (Classic Compute)
description: Setting up a time-series forecasting experiment using Databricks AutoML with user-managed compute clusters, including dataset configuration, target column selection, and launch workflow.
tags:
  - automl
  - forecasting
  - databricks
timestamp: "2026-06-19T10:38:06.436Z"
---

# AutoML Forecasting Experiment (Classic Compute)

**AutoML Forecasting Experiment (Classic Compute)** is a feature in Databricks that automates the process of finding the best forecasting algorithm and hyperparameter configuration to predict values based on time-series data. This classic compute mode runs on user-managed clusters rather than serverless infrastructure. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

Time series forecasting via AutoML is only available for Databricks Runtime 10.0 ML or above. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

---

## Setup via the UI

To set up a forecasting experiment using the AutoML UI:

1.  In the sidebar, select **Experiments**.
2.  In the **Forecasting** card, select **Start training**.

The forecasting UI defaults to [Serverless Forecasting](/concepts/databricks-serverless-forecasting.md). To access the classic compute experience, select **revert back to the old experience**. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

---

## Configure the Experiment

The **Configure AutoML experiment** page allows you to specify the dataset, problem type, target column, evaluation metric, and stopping conditions. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Compute
In the **Compute** field, select a cluster running Databricks Runtime 10.0 ML or above. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Dataset
Under **Dataset**, click **Browse** and navigate to the table you want to use. The table schema appears after selection. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Prediction Target
Click in the **Prediction target** field. A dropdown menu lists the columns from the schema. Select the column you want the model to predict. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Time Column
Click in the **Time column** field. A dropdown shows dataset columns of type `timestamp` or `date`. Select the column containing the time periods for the time series. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Time Series Identifiers
For [Multi-Series Forecasting](/concepts/multi-series-forecasting.md), select the column(s) that identify individual time series from the **Time series identifiers** dropdown. AutoML groups data by these columns as different time series and trains a model for each series independently. If left blank, AutoML assumes the dataset contains a single time series. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Forecast Horizon and Frequency
In the **Forecast horizon and frequency** fields, specify:
- Left box: The integer number of time periods to forecast.
- Right box: The units for those periods.

To use Auto-ARIMA, the time series must have a regular frequency where the interval between any two points is the same throughout the series. The frequency must match the frequency unit specified in the UI. AutoML handles missing time steps by filling in values with the previous value. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Output Database (Databricks Runtime 11.3 LTS ML and above)
To save prediction results, specify a database in the **Output Database** field. Click **Browse** and select a database. AutoML writes prediction results to a table in this database. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Experiment Name
The **Experiment name** field shows a default name. To change it, type a new name. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Additional Options
You may also:
- Specify additional configuration options.
- Use existing feature tables in Feature Store to augment the original input dataset. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

---

## Advanced Configurations

Open the **Advanced Configuration (optional)** section to access these parameters. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Evaluation Metric
The evaluation metric is the primary metric used to score runs. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Exclude Training Frameworks
In Databricks Runtime 10.4 LTS ML and above, you can exclude training frameworks from consideration. By default, AutoML trains models using frameworks listed under AutoML algorithms. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Stopping Conditions
Default stopping conditions are:
- For forecasting experiments: stop after **120 minutes**. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
- In Databricks Runtime 10.4 LTS ML and below, for classification and regression experiments: stop after 60 minutes or after completing 200 trials (whichever occurs first). For Databricks Runtime 11.0 ML and above, the number of trials is not used as a stopping condition. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
- In Databricks Runtime 10.4 LTS ML and above, for classification and regression experiments, AutoML incorporates early stopping — it stops training if the validation metric is no longer improving. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Chronological Split (Databricks Runtime 10.4 LTS ML and above)
You can select a `time column` to split data for training, validation, and testing in chronological order. This applies only to classification and regression experiments. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Data Directory
Databricks recommends leaving the **Data directory** field empty. Not populating this field triggers the default behavior of securely storing the dataset as an MLflow artifact. A DBFS path can be specified, but in that case the dataset does not inherit the AutoML experiment's access permissions. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

---

## Run and Monitor the Experiment

To start the AutoML experiment, click **Start AutoML**. The experiment begins and the AutoML training page appears. To refresh the runs table, click the refresh button. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### View Progress
From this page you can:
- Stop the experiment at any time.
- Open the data exploration notebook.
- Monitor runs.
- Navigate to the run page for any run.

With Databricks Runtime 10.1 ML and above, AutoML displays warnings for potential issues — such as unsupported column types or high cardinality columns. To see warnings, click the **Warnings** tab on the training page or experiment page after the experiment completes. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### View Results
When the experiment completes, you can:
- Register and deploy one of the models with MLflow.
- Select **View notebook for best model** to review and edit the notebook that created the best model.
- Select **View data exploration notebook** to open the data exploration notebook.
- Search, filter, and sort runs in the runs table.
- See details for any run:
  - The generated notebook for a trial run is saved in the **Artifacts** section of the run page. You can download and import this notebook if downloading artifacts is enabled by your workspace administrators.
  - To view run results, click in the **Models** column or **Start Time** column. The run page shows parameters, metrics, tags, and artifacts — including the model and code snippets for making predictions.

To return to this AutoML experiment later, find it in the table on the [Experiments page](/concepts/mlflow-experiment.md). The results — including data exploration and training notebooks — are stored in a `databricks_automl` folder in the home folder of the user who ran the experiment. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

---

## Register and Deploy a Model

Register and deploy your model using the AutoML UI. When a run completes, the top row shows the best model based on the primary metric. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

1.  Select the link in the **Models** column for the model you want to register.
2.  Select the register model button to register it to [Unity Catalog](/concepts/unity-catalog.md) or the [Model Registry](/concepts/mlflow-model-registry.md). Databricks recommends registering models to Unity Catalog for the latest features.

3.  After registration, deploy the model to a [custom model serving endpoint](/concepts/custom-model-serving-endpoint-support.md). ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### No module named 'pandas.core.indexes.numeric'

When serving a model built using AutoML with [Model Serving](/concepts/model-serving.md), you may encounter the error:
```
No module named 'pandas.core.indexes.numeric'
```
This is due to an incompatible `pandas` version between AutoML and the model serving endpoint environment. To resolve this error, run the add-pandas-dependency.py script. This script edits the `requirements.txt` and `conda.yaml` for your logged model to include the appropriate `pandas` dependency version: `pandas==1.5.3`.

1.  Modify the script to include the `run_id` of the [MLflow Run](/concepts/mlflow-run.md) where your model was logged.
2.  Re-register the model.
3.  Try serving the new version. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

---

## Next Steps

- Forecasting API
- Forecasting data preparation settings
- Forecast with covariates

---

## Sources

- forecasting-with-automl-classic-compute-databricks-on-aws.md

# Citations

1. [forecasting-with-automl-classic-compute-databricks-on-aws.md](/references/forecasting-with-automl-classic-compute-databricks-on-aws-20de86d0.md)
