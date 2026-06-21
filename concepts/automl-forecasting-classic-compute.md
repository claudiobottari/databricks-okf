---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f8a4d4cd0391590f28b602b5099b03b9afc482d5d598d62d0f1e6370b13984aa
  pageDirectory: concepts
  sources:
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-forecasting-classic-compute
    - AF(C
    - AutoML (classic compute)
    - Forecasting with AutoML (classic compute)
    - Forecasting with Classic Compute
    - forecasting with classic compute
    - automl-forecasting-databricks-classic-compute
    - AF(CC
  citations:
    - file: forecasting-with-automl-classic-compute-databricks-on-aws.md
title: AutoML Forecasting (Classic Compute)
description: Databricks AutoML's classic compute mode for automatically finding the best forecasting algorithm and hyperparameters for time-series data, requiring Databricks Runtime 10.0 ML or above.
tags:
  - automl
  - forecasting
  - databricks
  - time-series
timestamp: "2026-06-19T18:53:31.560Z"
---

# AutoML Forecasting (Classic Compute)

**AutoML Forecasting (Classic Compute)** is a feature in Databricks that automatically finds the best forecasting algorithm and hyperparameter configuration to predict future values based on time-series data. It uses user-specified compute clusters rather than serverless infrastructure. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Overview

Time series forecasting with AutoML is available for Databricks Runtime 10.0 ML and above. The classic compute experience allows users to run forecasting experiments on their own clusters, as opposed to the serverless forecasting option. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Setting Up a Forecasting Experiment

### Accessing the UI

To set up a forecasting problem using the AutoML UI:

1. In the sidebar, select **Experiments**.
2. In the **Forecasting** card, select **Start training**.

The forecasting UI defaults to serverless forecasting. To access forecasting with your own compute, select **revert back to the old experience**. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Configuring the Experiment

On the **Configure AutoML experiment page**, you specify the dataset, problem type, target column, evaluation metric, and stopping conditions. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

Key configuration fields include:

- **Compute**: Select a cluster running Databricks Runtime 10.0 ML or above.
- **Dataset**: Browse and select the table to use. The table schema appears after selection.
- **Prediction target**: Select the column the model should predict.
- **Time column**: Select the column containing time periods for the time series. Only `timestamp` or `date` type columns appear.
- **Time series identifiers**: For multi-series forecasting, select the column(s) that identify individual time series. AutoML groups data by these columns and trains a model for each series independently. If left blank, AutoML assumes a single time series.
- **Forecast horizon and frequency**: Specify the number of time periods into the future for forecasting. Enter an integer in the left box and select units in the right box.
- **Output Database** (Databricks Runtime 11.3 LTS ML and above): Specify a database to save prediction results. AutoML writes results to a table in this database.
- **Experiment name**: Displays a default name; you can change it.

^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Advanced Configurations

Open the **Advanced Configuration (optional)** section to access additional parameters:

- **Evaluation metric**: The primary metric used to score runs.
- **Excluded training frameworks** (Databricks Runtime 10.4 LTS ML and above): Exclude specific training frameworks from consideration.
- **Stopping conditions**: Default is 120 minutes for forecasting experiments. In Databricks Runtime 10.4 LTS ML and above, AutoML incorporates early stopping for classification and regression experiments.
- **Time column for data split** (Databricks Runtime 10.4 LTS ML and above): Select a time column to split data chronologically for training, validation, and testing (applies to classification and regression only).
- **Data directory**: Databricks recommends leaving this field empty to securely store the dataset as an MLflow artifact. A DBFS path can be specified, but the dataset will not inherit the AutoML experiment's access permissions.

^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Important Note on Auto-ARIMA

To use Auto-ARIMA, the time series must have a regular frequency where the interval between any two points is the same throughout the series. The frequency must match the frequency unit specified in the UI. AutoML handles missing time steps by filling in those values with the previous value. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Running and Monitoring the Experiment

To start the experiment, click **Start AutoML**. The AutoML training page appears, where you can:

- Stop the experiment at any time.
- Open the data exploration notebook.
- Monitor runs.
- Navigate to the run page for any run.

With Databricks Runtime 10.1 ML and above, AutoML displays warnings for potential dataset issues, such as unsupported column types or high cardinality columns. Click the **Warnings** tab on the training page or experiment page to see these warnings after the experiment completes. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Viewing Results

When the experiment completes, you can:

- Register and deploy a model with [MLflow](/concepts/mlflow.md).
- Select **View notebook for best model** to review and edit the notebook that created the best model.
- Select **View data exploration notebook** to open the data exploration notebook.
- Search, filter, and sort runs in the runs table.
- View details for any run, including the generated notebook saved in the **Artifacts** section of the run page.

To return to the experiment later, find it in the table on the Experiments page. Results are stored in a `databricks_automl` folder in the home folder of the user who ran the experiment. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Registering and Deploying a Model

When a run completes, the top row shows the best model based on the primary metric. To register and deploy:

1. Select the link in the **Models** column for the desired model.
2. Select **Register model** to register it to [Unity Catalog](/concepts/unity-catalog.md) or [Model Registry](/concepts/mlflow-model-registry.md). Databricks recommends registering models to Unity Catalog for the latest features.
3. After registration, deploy the model to a custom model serving endpoint.

^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Troubleshooting: Pandas Version Incompatibility

When serving a model built using AutoML with Model Serving, you may encounter the error: `No module named 'pandas.core.indexes.numeric`. This is due to an incompatible `pandas` version between AutoML and the model serving endpoint environment. To resolve:

1. Run the [add-pandas-dependency.py script](https://docs.databricks.com/aws/en/assets/files/add-pandas-dependency-4808dc9dcdfb035bdca6ebce6b86d719.py), which edits the `requirements.txt` and `conda.yaml` for your logged model to include `pandas==1.5.3`.
2. Modify the script to include the `run_id` of the [MLflow Run](/concepts/mlflow-run.md) where your model was logged.
3. Re-register the model to Unity Catalog or the model registry.
4. Try serving the new version of the MLflow model.

^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Related Concepts

- AutoML — Overview of automated machine learning on Databricks
- [Serverless Forecasting](/concepts/databricks-serverless-forecasting.md) — The alternative serverless compute option for forecasting
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for MLflow runs
- Forecasting API — Programmatic interface for forecasting experiments
- [Forecasting Data Preparation](/concepts/automl-forecasting-data-preparation.md) — Settings for preparing forecasting data
- [Covariate Forecasting](/concepts/covariates-in-time-series-forecasting.md) — Forecasting with additional predictor variables
- [Feature Store Integration](/concepts/automl-feature-store-integration.md) — Using existing feature tables to augment input datasets

## Sources

- forecasting-with-automl-classic-compute-databricks-on-aws.md

# Citations

1. [forecasting-with-automl-classic-compute-databricks-on-aws.md](/references/forecasting-with-automl-classic-compute-databricks-on-aws-20de86d0.md)
