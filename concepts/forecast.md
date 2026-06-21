---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 93e552a88839c9bfb9be45ae76a164cd9abfa532739f7b6c13f9bd19dd486071
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - forecast
    - Forecasting
    - forecasting
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: Forecast
description: The databricks.automl.forecast method configures an AutoML run for training a forecasting model with support for Auto-ARIMA.
tags:
  - auto-ml
  - forecasting
  - python-api
timestamp: "2026-06-19T17:39:06.529Z"
---

# Forecast

**Forecast** refers to the time-series forecasting capability provided by Databricks AutoML. It enables automated training of forecasting models through the `databricks.automl.forecast` method, which returns an [AutoMLSummary](/concepts/automlsummary.md) object describing the trials and results. ^[automl-python-api-reference-databricks-on-aws.md]

## Overview

The `forecast` method configures an AutoML run to train a forecasting model on a provided dataset. It accepts data as a PySpark DataFrame, pandas DataFrame, or a file path string, along with configuration parameters such as the target column, time column, frequency, and forecast horizon. ^[automl-python-api-reference-databricks-on-aws.md]

## Parameters

The method accepts several parameters, including:

- `dataset` – The input data (DataFrame or path).
- `target_col` – The column to forecast.
- `time_col` – The column representing the time stamp.
- `primary_metric` – The evaluation metric (default: `"smape"`).
- `country_code` – Country code for holiday effects (Databricks Runtime 12.0 ML and above).
- `frequency` – The frequency of the time series (default: `"D"` for daily). Must match the actual frequency of the data when using Auto-ARIMA.
- `horizon` – The number of steps to forecast ahead (default: 1).
- `identity_col` – An optional column (or list of columns) that identifies individual time series.
- `exclude_frameworks` – List of frameworks to exclude from the search.
- `feature_store_lookups` – Feature store lookups (Databricks Runtime 12.2 LTS ML and above).
- `sample_weight_col` – Sample weight column (Databricks Runtime 16.0 ML and above).
- `output_database` – Database to store the forecast output (Databricks Runtime 10.5 ML and above).
- `timeout_minutes` – Maximum duration for the AutoML run.

^[automl-python-api-reference-databricks-on-aws.md]

## Auto-ARIMA and Frequency Requirements

To use Auto-ARIMA, the time series must have a regular frequency — the interval between any two consecutive points must be consistent throughout the series. The frequency specified in the API call must match the actual frequency of the data. AutoML handles missing time steps by forward-filling with the previous value. ^[automl-python-api-reference-databricks-on-aws.md]

## Return Value

The `forecast` method returns an `AutoMLSummary` object, which provides metrics, parameters, and trial details for each trained model. The summary can be used to load individual models or import trial notebooks. ^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- AutoML – Overview of the automated machine learning functionality on Databricks.
- [AutoMLSummary](/concepts/automlsummary.md) – Object returned by AutoML methods containing trial information.
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) – Broader discipline of predicting future values based on historical data.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Runtime versions that support AutoML features.
- [Feature Store](/concepts/feature-store.md) – Used for feature lookups in forecasting runs.

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
