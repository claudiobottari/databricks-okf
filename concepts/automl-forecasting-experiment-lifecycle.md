---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 50bcaa9558824bbee5a38f80ec7d00b8fde0f3a4e4415cbbb42a8adabe806b58
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-forecasting-experiment-lifecycle
    - AFEL
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: AutoML Forecasting Experiment Lifecycle
description: "The three-stage pipeline of a Databricks forecasting experiment: Preprocessing (validation, imputation, feature engineering), Tuning (algorithm selection and hyperparameter search), and Training (final model training and registration)."
tags:
  - machine-learning
  - automl
  - pipeline
  - databricks
timestamp: "2026-06-19T18:52:54.392Z"
---

# AutoML Forecasting Experiment Lifecycle

The **AutoML Forecasting Experiment Lifecycle** describes the stages and steps involved in running a serverless forecasting experiment using the Databricks Model Training UI. Databricks Model Training simplifies forecasting of time-series data by automatically selecting the best algorithm and hyperparameters, running on fully-managed compute resources. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Requirements

Training data must have a time series column and be saved as a Unity Catalog table. If the workspace has serverless egress control enabled, `pypi.org` must be added to the **Allowed domains** list to allow AutoML to install necessary packages. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Creating a Forecasting Experiment with the UI

To create an experiment, go to the Databricks landing page and click **Experiments** in the sidebar. In the **Forecasting** tile, select **Start training**. The user then configures the experiment by specifying:

- **Training data** from a Unity Catalog table.
- **Time column** (must be `timestamp` or `date`) and **Forecast frequency** (e.g., minutes, hours, days, months).
- **Forecast horizon** (number of future time units to predict).
- **Prediction target column**.
- Optionally, a **Prediction data path** (Unity Catalog table) to store forecasts, and a **Model registration** Unity Catalog location and name.

Advanced options include setting an MLflow experiment name, time series identifier columns for multi-series forecasting, primary metric, training framework, split column (with values `"train"`, `"validate"`, `"test"`), weight column (range [0,10000]), holiday region as a covariate, and a maximum timeout duration. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Lifecycle Stages

Once the experiment is launched by clicking **Start training**, it proceeds through three sequential stages: ^[forecasting-serverless-with-automl-databricks-on-aws.md]

1. **Preprocessing:** The system validates and prepares the input table by imputing missing values and splitting data into training, validation, and test sets. Automatic feature generation, such as one-hot encoding for categorical features, also occurs during this stage. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

2. **Tuning:** AutoML explores different forecasting algorithms and tunes hyperparameters to find the best performing configuration. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

3. **Training:** The final model is trained and evaluated with the selected best configuration. If a Unity Catalog registration path was specified, the model is registered in Unity Catalog. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

During all stages, users can monitor the experiment from the training page, stop the experiment at any time, view individual runs, and navigate to each run's page. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Viewing Results and Using the Best Model

After training completes, the prediction results are stored in the specified Delta table, and the best model is registered to Unity Catalog. From the experiments page, the user can take any of the following next steps:

- **View predictions** to examine the forecasting results table.
- **Batch inference notebook** to open an auto-generated notebook for batch inferencing using the best model.
- **Create serving endpoint** to deploy the best model to a Model Serving endpoint.

^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Related Concepts

- AutoML – Automated machine learning for model selection and tuning.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) for managing data tables and registered models.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for tracking runs and results.
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) – The general domain of predicting future values from historical data.
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – The process of finding optimal model parameters.

## Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
