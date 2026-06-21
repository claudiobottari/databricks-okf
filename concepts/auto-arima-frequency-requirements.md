---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 06ae5c4f16a024c2edb1e8666b7511d539e33b1bc740959048fdfb1ada09cb69
  pageDirectory: concepts
  sources:
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - auto-arima-frequency-requirements
    - AFR
  citations:
    - file: forecasting-with-automl-classic-compute-databricks-on-aws.md
title: Auto-ARIMA Frequency Requirements
description: Constraint in AutoML forecasting requiring time series to have a regular frequency with consistent intervals between data points, matching the frequency unit specified in the UI or API.
tags:
  - arima
  - forecasting
  - time-series
  - databricks
timestamp: "2026-06-19T18:53:46.803Z"
---

# Auto-ARIMA Frequency Requirements

**Auto-ARIMA Frequency Requirements** refer to the constraints that a time series must satisfy in order for the Auto-ARIMA algorithm to be used effectively within [Databricks AutoML](/concepts/databricks-automl.md) forecasting experiments. These requirements ensure that the data has a regular, consistent temporal structure that the algorithm can model.

## Regular Frequency Requirement

To use Auto-ARIMA, the time series must have a regular frequency. This means the interval between any two consecutive data points must be the same throughout the entire time series. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Frequency Matching

The frequency of the time series must match the frequency unit specified in the AutoML API call or in the AutoML UI when configuring the forecasting experiment. For example, if the forecast horizon specifies weekly units, the time series data must have a consistent weekly spacing between observations. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Handling Missing Time Steps

AutoML handles missing time steps by filling in those values with the previous value (forward-filling). This ensures that irregular gaps in the data do not break the regular frequency requirement for Auto-ARIMA. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Configuration Context

These frequency requirements are specified when configuring the forecast horizon and frequency fields in the AutoML forecasting experiment interface. Users define the number of time periods to forecast and the units (such as days, weeks, months), and the time series data must conform to a regular interval matching that unit. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Related Concepts

- Auto-ARIMA — The automatic ARIMA algorithm subject to these frequency constraints
- Databricks AutoML Forecasting — The overall forecasting workflow that includes Auto-ARIMA
- Time Series Data Preparation — How to structure data for AutoML forecasting
- [Forecast Horizon](/concepts/forecast-frequency-and-horizon.md) — The number and units of time periods to predict

## Sources

- forecasting-with-automl-classic-compute-databricks-on-aws.md

# Citations

1. [forecasting-with-automl-classic-compute-databricks-on-aws.md](/references/forecasting-with-automl-classic-compute-databricks-on-aws-20de86d0.md)
