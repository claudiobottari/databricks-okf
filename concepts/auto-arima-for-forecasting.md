---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 305a248e16a188c60219d2cfd49d2688747893cde3825fb619814121fb8d838f
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - auto-arima-for-forecasting
    - AFF
    - AutoML for Forecasting
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
      start: 1
      end: 10
title: Auto-ARIMA for Forecasting
description: An algorithm used by Databricks AutoML that requires time series data with a regular frequency; missing time steps are filled with the previous value.
tags:
  - forecasting
  - algorithm
  - time-series
  - ARIMA
timestamp: "2026-06-18T12:23:20.027Z"
---

# Auto-ARIMA for Forecasting

**Auto-ARIMA** is an automated implementation of the ARIMA (AutoRegressive Integrated Moving Average) algorithm available through the `pmdarima` Python library. In the context of Databricks serverless forecasting, Auto-ARIMA is one of the algorithms explored by AutoML to find the best-fitting model for time-series data. ^[forecasting-serverless-with-automl-databricks-on-aws.md#L1-L10]

## Overview

Auto-ARIMA automatically selects the optimal parameters for an ARIMA model by searching over combinations of `p` (autoregressive order), `d` (differencing order), and `q` (moving average order). It balances model fit against complexity to avoid overfitting. ^[forecasting-serverless-with-automl-databricks-on-aws.md#L1-L10]

In Databricks AutoML for forecasting, Auto-ARIMA is one of several algorithms the framework evaluates during the tuning phase. The framework explores different forecasting algorithms and tunes their hyperparameters to find the best configuration for your specific time series. ^[forecasting-serverless-with-automl-databricks-on-aws.md#L1-L10]

## Requirements

To use Auto-ARIMA, the input time series must have a **regular frequency** — the interval between any two consecutive data points must be identical throughout the entire series. When this condition is met, Databricks AutoML handles missing time steps by filling in those values with the previous value (forward fill). ^[forecasting-serverless-with-automl-databricks-on-aws.md#L1-L10]

## How Auto-ARIMA Works in AutoML

### Algorithm Selection

During AutoML training, the framework evaluates Auto-ARIMA alongside other forecasting algorithms. The tuning stage performs the following: ^[forecasting-serverless-with-automl-databricks-on-aws.md#L1-L10]

1. **Preprocessing**: Validate and prepare the input table by imputing missing values and splitting data into training, validation, and test sets. Automatic feature generation (like one-hot encoding for categorical features) also occurs.
2. **Tuning**: Explore different forecasting algorithms and tune hyperparameters.
3. **Training**: Train and evaluate the final model with selected best configurations.

### Best Model Selection

The primary metric you specify (e.g., RMSE, MAE) determines which algorithm configuration is selected as the best model. Auto-ARIMA competes with other algorithms based on this metric. ^[forecasting-serverless-with-automl-databricks-on-aws.md#L1-L10]

## Configuration Options

When using Auto-ARIMA through the Databricks Model Training UI, you can configure: ^[forecasting-serverless-with-automl-databricks-on-aws.md#L1-L10]

- **Time column**: The column containing time periods (must be `timestamp` or `date` type)
- **Forecast frequency**: The time unit representing input data granularity (minutes, hours, days, months)
- **Forecast horizon**: Number of frequency units to forecast into the future
- **Time series identifier columns**: For multi-series forecasting, columns identifying individual time series
- **Training framework**: Which frameworks AutoML should explore (when Auto-ARIMA is included)

## Related Concepts

- ARIMA Models — The underlying statistical model for time series analysis
- Pmdarima — The Python library implementing Auto-ARIMA
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) — The broader field of predicting future values from temporal data
- AutoML — Automated machine learning that explores multiple algorithms including Auto-ARIMA
- [Serverless Forecasting](/concepts/databricks-serverless-forecasting.md) — Databricks' managed compute environment for running forecasting experiments
- [Classic Compute Forecasting](/concepts/classic-compute-forecasting.md) — Traditional compute environment for forecasting compared to serverless

## Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md:1-10](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
