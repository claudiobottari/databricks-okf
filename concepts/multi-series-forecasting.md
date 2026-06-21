---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 67aef1c9716d19a6dfa2ca3254c5c43aafe7e82277ada022b068583d25947060
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-series-forecasting
    - Time Series Forecasting
    - Time series forecasting
    - Time-Series Forecasting
    - time series forecasting
    - time-series forecasting
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: Multi-Series Forecasting
description: A forecasting approach where data is grouped by identifier columns into multiple independent time series, and Databricks trains a separate model for each series.
tags:
  - forecasting
  - time-series
  - databricks
timestamp: "2026-06-19T18:53:00.304Z"
---

## Multi-Series Forecasting

**Multi-Series Forecasting** refers to the task of producing separate forecasts for multiple distinct time series that are stored in a single dataset. In the context of Databricks serverless forecasting with AutoML, multi-series forecasting is enabled by specifying one or more **time series identifier columns**. These columns uniquely identify each individual time series within the training data. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### How Databricks Implements Multi-Series Forecasting

When creating a forecasting experiment via the Databricks Model Training UI, you can enable multi-series forecasting by setting the **Time series identifier columns** under **Advanced options**. The platform groups the input data by the values in these columns, treating each group as an independent time series. A separate model is then trained for each series independently. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

This approach allows users to forecast, for example, sales for multiple products or demand for multiple regions in a single experiment, without needing to manually split the data or run separate experiments.

### Requirements

- The training data must be saved as a [Unity Catalog](/concepts/unity-catalog.md) table with a time column of type `timestamp` or `date`.
- For the Auto-ARIMA algorithm specifically, each individual time series must have a regular frequency (the interval between consecutive points must be identical across the series). AutoML handles missing time steps by forward-filling values. ^[forecasting-serverless-with-automl-databricks-on-aws.md]
- If the workspace has serverless egress control enabled, `pypi.org` must be added to the allowed domains for certain dependencies. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Key Settings

| Setting | Description |
|---------|-------------|
| Time column | The column containing the time periods (timestamp or date). |
| Forecast frequency | The time unit of the input data (minutes, hours, days, etc.). |
| Forecast horizon | The number of time units to forecast into the future. |
| Time series identifier columns | Columns that identify individual time series; data is grouped by these columns and a model is trained per series. |
| Primary metric | The metric used to evaluate and select the best model. |
| Training framework | Which forecasting frameworks AutoML should explore. |

### Related Concepts

- [Time Series Forecasting](/concepts/multi-series-forecasting.md)
- AutoML (Automated Machine Learning)
- [Unity Catalog](/concepts/unity-catalog.md)
- Auto-ARIMA
- Serverless Compute on Databricks

### Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
