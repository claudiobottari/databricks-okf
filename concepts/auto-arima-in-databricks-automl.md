---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c7eeb0eee77a4563941387e06afc7105a4c86c933808c588ec35fb85441e84c5
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - auto-arima-in-databricks-automl
    - AIDA
    - Auto-ARIMA algorithm
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: Auto-ARIMA in Databricks AutoML
description: An algorithm option for forecasting that requires regularly-spaced time series data; Databricks AutoML handles missing time steps by forward-filling with the previous value.
tags:
  - algorithm
  - forecasting
  - time-series
  - automl
timestamp: "2026-06-19T18:52:58.310Z"
---

# Auto-ARIMA in Databricks AutoML

**Auto-ARIMA** is a forecasting algorithm available in Databricks AutoML for time series prediction tasks. It is based on the [pmdarima](https://alkaline-ml.com/pmdarima/) library and is automatically considered by AutoML when performing serverless forecasting experiments.

## Overview

Auto-ARIMA automates the process of selecting optimal (p, d, q) parameters for an ARIMA (AutoRegressive Integrated Moving Average) model. In Databricks AutoML, it is one of the algorithms that the training framework evaluates during the tuning stage to find the best forecasting model for your time series data. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Requirements

To use the Auto-ARIMA algorithm, the time series data must have a **regular frequency**, where the interval between any two consecutive time points must be the same throughout the entire time series. AutoML handles missing time steps by filling in those values with the previous value (forward fill). ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Integration with AutoML

During a serverless forecasting experiment, Databricks AutoML goes through several stages:

1. **Preprocessing**: Validates and prepares the input table by imputing missing values and splitting data into training, validation, and test sets. Automatic feature generation, such as one-hot encoding for categorical features, also occurs during this stage.
2. **Tuning**: Explores different forecasting algorithms (including Auto-ARIMA) and tunes hyperparameters.
3. **Training**: Trains and evaluates the final model with the selected best configurations.

Auto-ARIMA is considered alongside other algorithms during the tuning stage as part of the selected [Training Framework](/concepts/horovod-distributed-training-framework.md). ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Configuration

To enable Auto-ARIMA in a forecasting experiment:

1. Navigate to **Experiments** in the Databricks sidebar.
2. Select **Start training** in the **Forecasting** tile.
3. Configure your training data, including the **Time column**, **Forecast frequency**, and **Forecast horizon**.
4. In **Advanced options**, select the **Training framework** that includes Auto-ARIMA as an option.

The forecast frequency must match the regular frequency required by Auto-ARIMA (e.g., minutes, hours, days, months). ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Related Concepts

- ARIMA Models – The statistical modeling approach that Auto-ARIMA automates
- [Serverless Forecasting](/concepts/databricks-serverless-forecasting.md) – The compute infrastructure for running AutoML forecasting experiments
- Time Series Analysis – The broader field of analyzing time-ordered data
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – The process of finding optimal model parameters
- [Training Framework](/concepts/horovod-distributed-training-framework.md) – The set of algorithms AutoML explores during experiments

## Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
