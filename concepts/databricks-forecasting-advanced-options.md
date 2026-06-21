---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0ae19859d1d03c62666858020fbe9c5c3408fde70b7e05b54e2f62eaad93eb85
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-forecasting-advanced-options
    - DFAO
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: Databricks Forecasting Advanced Options
description: Additional configuration parameters for forecasting experiments including holiday region covariates, weight columns, split columns, training framework selection, and primary metrics.
tags:
  - databricks
  - forecasting
  - configuration
timestamp: "2026-06-19T18:53:08.716Z"
---

# Databricks Forecasting Advanced Options

When creating a serverless forecasting experiment using the Databricks Model Training UI, you can configure a set of **Advanced options** that control model selection, data splitting, weighting, and other tuning parameters. These options allow you to customize the AutoML process for your time‑series data. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Available Advanced Options

The advanced options are presented after you have selected the training data, time column, forecast frequency, forecast horizon, and prediction target column. Each option is described below.

- **Experiment name** – An [MLflow Experiment](/concepts/mlflow-experiment.md) name to group the runs generated during the AutoML tuning and training stages. If left blank, Databricks creates a default name. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

- **Time series identifier columns** – For [Multi-Series Forecasting](/concepts/multi-series-forecasting.md), select one or more columns that uniquely identify individual time series. Databricks groups the data by these columns, training a separate model for each series independently. This is essential when your input table contains multiple distinct time series (e.g., sales per store, temperature per city). ^[forecasting-serverless-with-automl-databricks-on-aws.md]

- **Primary metric** – Choose the metric used to evaluate candidate models and select the best final model. Typical choices include MAE, RMSE, or MAPE. The metric determines which algorithm and hyperparameters are chosen as optimal. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

- **Training framework** – Specify which forecasting frameworks AutoML should explore. Databricks supports frameworks such as Prophet, Auto-ARIMA, and others. By selecting a subset, you can reduce experimentation time or focus on frameworks best suited to your data. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

- **Split column** – Provide a column that contains custom train/validation/test split labels. The values must be exactly `"train"`, `"validate"`, or `"test"`. This allows you to control the data partitioning manually instead of relying on the default time‑based split. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

- **Weight column** – Specify a column that assigns a weight to each time series. All samples belonging to a given time series must share the same weight. The weight value must be in the range `[0, 10000]`. Weighting influences the loss function during training, allowing you to emphasise certain series over others. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

- **Holiday region** – Select a holiday region (e.g., `"UnitedStates"`, `"India"`) to include holiday effects as covariates in model training. Databricks automatically generates holiday indicators for the chosen region, which can improve forecast accuracy when demand is affected by public holidays. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

- **Timeout** – Set a maximum duration (in minutes) for the AutoML experiment. The experiment stops when the timeout is reached, even if tuning is not complete. This prevents runaway costs and ensures that the experiment finishes within a predictable time. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Additional Considerations

When using the Auto-ARIMA algorithm, the time series must have a regular frequency (i.e., the interval between any two consecutive points must be constant). AutoML handles missing time steps by forward‑filling. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

For a full walkthrough of the serverless forecasting workflow, including requirements and result monitoring, see Serverless Forecasting with AutoML. For comparison with the classic compute forecasting approach, see the table in the serverless article.

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md)
- Time Series Forecasting on Databricks
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Prophet and Auto-ARIMA (supported frameworks)
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- [Batch Inference Notebooks](/concepts/batch-inference-on-databricks.md)

## Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
