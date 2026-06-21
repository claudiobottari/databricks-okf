---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cd3309ca9eba4418f837d5345df4a06dd8d6b6775bb02e0fcfde8ad64db1c81a
  pageDirectory: concepts
  sources:
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - auto-arima-and-regular-frequency-requirement
    - Regular Frequency Requirement and Auto-ARIMA
    - AARFR
  citations:
    - file: forecasting-with-automl-classic-compute-databricks-on-aws.md
title: Auto-ARIMA and Regular Frequency Requirement
description: Requirement that time series data must have a regular, consistent frequency for Auto-ARIMA, with AutoML automatically filling in missing time steps using forward fill.
tags:
  - arima
  - forecasting
  - time-series
timestamp: "2026-06-19T10:37:14.563Z"
---

# Auto-ARIMA and Regular Frequency Requirement

**Auto-ARIMA** is a forecasting algorithm available in Databricks AutoML that automatically selects the best ARIMA (AutoRegressive Integrated Moving Average) model for time-series data. To use Auto-ARIMA, the time series must have a **regular frequency**, meaning the interval between any two consecutive data points must be consistent throughout the entire series. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Frequency Requirement

The frequency of the time series must match the frequency unit specified in the AutoML experiment configuration (either in the UI or API call). This ensures the model can properly interpret the temporal structure of the data and make accurate forecasts. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Handling Irregular Frequencies

If the input time series has missing time steps or irregular intervals, AutoML handles these gaps by filling in missing values with the previous known value. This imputation step ensures that the resulting series meets the regular frequency requirement before Auto-ARIMA is applied. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Configuration

When setting up a forecasting experiment, users configure the **Forecast horizon and frequency** by specifying:

- The integer number of time periods to forecast
- The time units for those periods (e.g., days, weeks, months)

These values must align with the natural frequency of the data. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Related Concepts

- [Forecasting with AutoML (classic compute)](/concepts/automl-forecasting-classic-compute.md) — The overall forecasting workflow in Databricks AutoML
- Time series data preparation — Preprocessing steps for time-series forecasting
- AutoML algorithms — Other algorithms used in AutoML experiments
- ARIMA model — Statistical model underlying Auto-ARIMA

## Sources

- forecasting-with-automl-classic-compute-databricks-on-aws.md

# Citations

1. [forecasting-with-automl-classic-compute-databricks-on-aws.md](/references/forecasting-with-automl-classic-compute-databricks-on-aws-20de86d0.md)
