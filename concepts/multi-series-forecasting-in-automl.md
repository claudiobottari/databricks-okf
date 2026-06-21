---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7abbff5bd2f69727d81ef9e2495ac1d33e34f693d293edab192befc3f0111e62
  pageDirectory: concepts
  sources:
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-series-forecasting-in-automl
    - MFIA
    - Time Series Forecasting with AutoML
  citations:
    - file: forecasting-with-automl-classic-compute-databricks-on-aws.md
title: Multi-Series Forecasting in AutoML
description: Technique in Databricks AutoML where time series identifiers group data into multiple independent time series, with each series trained independently.
tags:
  - forecasting
  - time-series
  - databricks
timestamp: "2026-06-19T18:53:36.444Z"
---

# Multi-Series Forecasting in AutoML

**Multi-Series Forecasting in AutoML** allows you to forecast multiple independent time series within a single AutoML experiment. By designating one or more **time series identifier columns**, AutoML groups the dataset into separate time series, trains a forecasting model for each group independently, and produces predictions for each series. This feature is available in the classic compute AutoML experience (Databricks Runtime 10.0 ML and above). ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Configuring Multi-Series Forecasting

In the AutoML UI, multi-series forecasting is set up during experiment configuration:

1. Open the **Configure AutoML experiment** page.
2. Select a cluster running Databricks Runtime 10.0 ML or above.
3. Choose your dataset and set the **Prediction target** column.
4. Set the **Time column** that contains the time periods.
5. In the **Time series identifiers** drop-down, select one or more columns that identify the individual time series. AutoML groups the data by these columns, treating each unique combination as a separate time series. If left blank, AutoML assumes the dataset contains a single time series. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
6. Specify the **Forecast horizon** (number of periods) and **Frequency** (units such as days, weeks, months).

The forecasting UI in Databricks defaults to [serverless forecasting](/concepts/databricks-serverless-forecasting.md). To use the classic compute experience described here, select **revert back to the old experience**. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## How It Works

AutoML groups the input data by the selected time series identifier columns, creating a distinct training set for each series. For each group, AutoML independently trains and evaluates a forecasting model, selecting the best algorithm and hyperparameters. The result is a set of models — one per time series — each producing predictions for the specified forecast horizon. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Related Concepts

- AutoML — Automated machine learning for classification, regression, and forecasting
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) — The general problem of predicting future values based on historical data
- [Forecast Horizon](/concepts/forecast-frequency-and-horizon.md) — The number of time periods into the future to predict
- Forecasting with Covariates — Using external predictors in forecasting experiments
- [Serverless Forecasting](/concepts/databricks-serverless-forecasting.md) — The default forecasting experience on Databricks

## Sources

- forecasting-with-automl-classic-compute-databricks-on-aws.md

# Citations

1. [forecasting-with-automl-classic-compute-databricks-on-aws.md](/references/forecasting-with-automl-classic-compute-databricks-on-aws-20de86d0.md)
