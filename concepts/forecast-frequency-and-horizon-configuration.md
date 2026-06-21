---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 02a7537606914b7bb6ac416f10f8e65d0938b75097429d714b50ae86c779c843
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - forecast-frequency-and-horizon-configuration
    - Horizon Configuration and Forecast Frequency
    - FFAHC
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: Forecast Frequency and Horizon Configuration
description: "Key parameters for defining a forecasting problem: forecast frequency (granularity like hours/days/months) and forecast horizon (number of future time units to predict)."
tags:
  - forecasting
  - time-series
  - parameters
timestamp: "2026-06-19T18:52:58.660Z"
---

# Forecast Frequency and Horizon Configuration

**Forecast Frequency and Horizon Configuration** refers to the two fundamental parameters that define the temporal scope and granularity of a forecasting model in Databricks AutoML. These settings determine both the time unit of the input data and how far into the future predictions are made.

## Overview

When creating a forecasting experiment using the Databricks Model Training UI, you must configure the forecast frequency and forecast horizon. Together, these parameters define both the time units and the number of time units to forecast. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Forecast Frequency

The **forecast frequency** is the time unit that represents your input data's frequency. This determines the granularity of your time series. Available options include minutes, hours, days, months, and other standard time units. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

The frequency selection must match the interval between consecutive time points in your training data. For the Auto-ARIMA algorithm to work correctly, the time series must have a regular frequency where the interval between any two points is the same throughout the entire series. AutoML handles missing time steps by filling in those values with the previous value. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Forecast Horizon

The **forecast horizon** specifies how many units of the selected frequency to forecast into the future. For example, if the forecast frequency is set to "days" and the forecast horizon is set to 30, the model will predict values for the next 30 days. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Configuration in the UI

To configure these parameters when creating a forecasting experiment:

1. Select the **Training data** from a Unity Catalog table.
2. Choose the **Time column** containing the time periods (must be of type `timestamp` or `date`).
3. Set the **Forecast frequency** to match your input data's time unit.
4. Set the **Forecast horizon** to the desired number of time units to predict.

^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Relationship Between Parameters

The forecast frequency and forecast horizon work together to define the complete forecasting scope. The frequency establishes the base time unit, while the horizon determines how many of those units to project forward. Together, they control both the resolution and the extent of the forecast output. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Related Concepts

- Serverless Forecasting with AutoML — The overall process for running forecasting experiments
- Auto-ARIMA — A forecasting algorithm that requires regular frequency data
- Time Series Analysis — The broader field of analyzing time-ordered data points
- [Data Profiling](/concepts/data-profiling.md) — Statistical analysis of input data before forecasting
- Model Training UI — The interface for configuring forecasting experiments

## Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
