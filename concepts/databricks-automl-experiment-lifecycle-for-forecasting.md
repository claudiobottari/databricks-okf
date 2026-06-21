---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9e9557a2ad7a41c75987f10fd602f4fbaadab9b6a2bc6aa7ef334166d3a5b962
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-automl-experiment-lifecycle-for-forecasting
    - DAELFF
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: Databricks AutoML Experiment Lifecycle for Forecasting
description: The three-stage pipeline (Preprocessing, Tuning, Training) that Databricks Serverless Forecasting follows when running an AutoML experiment.
tags:
  - databricks
  - automl
  - pipeline
  - workflow
timestamp: "2026-06-19T10:36:40.828Z"
---

# Databricks AutoML Experiment Lifecycle for Forecasting

**Databricks AutoML Experiment Lifecycle for Forecasting** describes the end-to-end process of running a serverless forecasting experiment using the Databricks Model Training UI. The lifecycle automates data preparation, algorithm selection, hyperparameter tuning, and model registration, all on fully managed compute resources. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Requirements

To start an AutoML forecasting experiment, you must have training data saved as a [Unity Catalog](/concepts/unity-catalog.md) table that contains a time-series column of type `timestamp` or `date`. If the workspace has serverless egress control enabled, `pypi.org` must be added to the allowed domains list to permit package installation. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Creating a Forecasting Experiment with the UI

The experiment is created through the Databricks landing page by clicking **Experiments** in the sidebar, then selecting **Start training** in the **Forecasting** tile. The required configuration includes:

- **Training data**: A Unity Catalog table.
- **Time column**: The timestamp or date column for the time series.
- **Forecast frequency**: The time unit (e.g., minutes, days, months) that determines granularity.
- **Forecast horizon**: The number of frequency units to forecast into the future.
- **Prediction target column**: The numeric column to predict.
- **Prediction data path** (optional): A Unity Catalog table to store output forecasts.
- **Model registration location**: The Unity Catalog path to register the best model.

Optional advanced settings include experiment name, time-series identifier columns (for multi-series forecasting), primary metric, training framework, split column, weight column, holiday region, and timeout. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

When using the Auto-ARIMA algorithm, the time series must have a regular frequency (constant interval between points). AutoML handles missing time steps by filling them with the previous value. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Experiment Stages

Once the experiment is started, the AutoML system progresses through three sequential stages, each with distinct responsibilities. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### 1. Preprocessing

During preprocessing, the input table is validated and prepared. Missing values are imputed, and the data is split into training, validation, and test sets. Automatic feature generation (such as one-hot encoding for categorical features) is also performed in this stage. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### 2. Tuning

The tuning stage explores different forecasting algorithms and tunes their hyperparameters to find optimal configurations. AutoML evaluates multiple algorithms from the chosen training framework. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### 3. Training

The final model is trained using the best configuration identified during tuning. If a Unity Catalog path was specified, the model is registered automatically. Evaluation metrics are computed against the test set. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Monitoring and Control

From the experiment training page, you can stop the experiment at any time, monitor individual runs, and navigate to the run page for any completed run. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Viewing Results and Using the Best Model

After training completes, the prediction results are stored in the specified Delta table and the best model is registered to [Unity Catalog](/concepts/unity-catalog.md). From the experiment page, you can:

- Select **View predictions** to see the forecasting results table.
- Select **Batch inference notebook** to open an auto-generated notebook for batch inference using the best model.
- Select **Create serving endpoint** to deploy the best model to a [Model Serving](/concepts/model-serving.md) endpoint. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Serverless Forecasting vs. Classic Compute Forecasting

Serverless forecasting differs from [forecasting with classic compute](/concepts/automl-forecasting-classic-compute.md) primarily in the compute model and infrastructure management. The source material provides a summary table comparing the two approaches. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for tracking runs and parameters.
- [Unity Catalog](/concepts/unity-catalog.md) — Required for source data and model registration.
- Auto-ARIMA — A supported algorithm that requires regular frequency.
- [Model Serving](/concepts/model-serving.md) — Deployment target for the best model.
- Batch Inference — Automated notebook for applying the model to new data.
- [Forecasting with Classic Compute](/concepts/automl-forecasting-classic-compute.md) — Alternative approach using traditional compute clusters.

## Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
