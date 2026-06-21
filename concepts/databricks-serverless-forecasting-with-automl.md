---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d39987396b48277cbcec93aed812879f04d46bf585b7d275429bd13f20389bc
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-serverless-forecasting-with-automl
    - DSFWA
    - Serverless Forecasting with AutoML
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: Databricks Serverless Forecasting with AutoML
description: A UI-driven feature in Databricks that automates time series forecasting by selecting optimal algorithms and hyperparameters on fully-managed compute resources.
tags:
  - databricks
  - forecasting
  - automl
  - time-series
timestamp: "2026-06-19T10:36:29.306Z"
---

Here is the wiki page for "Databricks Serverless Forecasting with AutoML", written entirely based on the provided source material.

---

## Databricks Serverless Forecasting with AutoML

**Databricks Serverless Forecasting with AutoML** simplifies forecasting time-series data by automatically selecting the best algorithm and hyperparameters, all while running on fully-managed compute resources. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Requirements

To run a serverless forecasting experiment, the training data must have a time series column and be saved as a [Unity Catalog](/concepts/unity-catalog.md) table. If the workspace has serverless egress control enabled, `pypi.org` must be added to the "Allowed domains" list. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Creating a Forecasting Experiment with the UI

To create a new experiment using the Databricks Model Training UI:

1. Navigate to the **Experiments** page from the sidebar and click **Start training** in the **Forecasting** tile.
2. Select the **Training data** from accessible Unity Catalog tables.
3. Configure the time series by setting the **Time column** (must be `timestamp` or `date` type), the **Forecast frequency** (the time unit of the input data, e.g., minutes, hours, days), and the **Forecast horizon** (how many units to forecast into the future).
4. Select a **Prediction target column** that the model will predict.
5. Optionally, specify a Unity Catalog table **Prediction data path** to store output forecasts.
6. Select a **Model registration** Unity Catalog location and name.
7. If desired, configure **Advanced options**, including: an alternative experiment name, time series identifier columns for multi-series forecasting, a primary metric, the training framework to explore, a split column for custom data splits, a weight column for weighting time series, a holiday region for covariates, and a timeout for the experiment duration. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

To use the [Auto-ARIMA algorithm](/concepts/auto-arima-in-databricks-automl.md), the time series must have a regular frequency with constant intervals between all data points. AutoML handles missing time steps by filling in those values with the previous value. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Running and Monitoring the Experiment

After clicking **Start training**, the experiment progresses through three stages:

1. **Preprocessing**: Validates and prepares the input table by imputing missing values and splitting data into training, validation, and test sets. Automatic feature generation (e.g., one-hot encoding) also occurs here.
2. **Tuning**: Explores different forecasting algorithms and tunes hyperparameters.
3. **Training**: Trains and evaluates the final model with the best configurations. The model is registered in Unity Catalog if a path was specified.

Users can stop the experiment at any time, monitor runs, and navigate to individual run pages. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Viewing Results and Using the Best Model

After training completes, prediction results are stored in the specified Delta table, and the best model is registered to Unity Catalog. From the experiments page, users can:

- **View predictions** to see the forecasting results table.
- **Batch inference notebook** to open an auto-generated notebook for batch inferencing.
- **Create serving endpoint** to deploy the best model to a [Model Serving](/concepts/model-serving.md) endpoint. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Serverless vs. Classic Compute Forecasting

The primary difference between serverless forecasting and forecasting with classic compute is that serverless forecasting runs on fully-managed compute resources, eliminating the need to provision and manage clusters. For a detailed comparison, see the documentation on [forecasting with classic compute](/concepts/automl-forecasting-classic-compute.md). ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Related Concepts

- AutoML
- [Unity Catalog](/concepts/unity-catalog.md)
- [Model Serving](/concepts/model-serving.md)
- [Time Series Forecasting](/concepts/multi-series-forecasting.md)
- [Databricks Model Training](/concepts/databricks-model-training.md)

### Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
