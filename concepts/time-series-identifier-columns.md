---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ffc7c5b27cf054b63e0b2d9db66a1472bf0b3e6300882caff5f542596b0df416
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-series-identifier-columns
    - TSIC
    - time series identifiers
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: Time Series Identifier Columns
description: Columns that identify individual time series in multi-series forecasting; Databricks groups data by these columns and trains a separate model per series.
tags:
  - forecasting
  - multi-series
  - time-series
timestamp: "2026-06-18T12:23:22.984Z"
---

# Time Series Identifier Columns

**Time Series Identifier Columns** are columns in a dataset that uniquely identify individual time series within a multi-series forecasting problem. When used in [Databricks Model Training](/concepts/databricks-model-training.md) (forecasting with AutoML), they allow the system to distinguish and model each time series independently. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Purpose

In multi-series forecasting, a single dataset often contains multiple distinct time series — for example, sales data for several products across many stores. A time series identifier column (or a combination of columns) tells the forecasting engine which rows belong to the same series. Without such columns, the engine would treat all data as a single series, which ignores differences in patterns between series. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## How It Works

When you specify time series identifier columns during the setup of a serverless forecasting experiment, Databricks groups the input data by the unique values of those columns. Each group is treated as an independent time series. A separate model is then trained for each series, allowing the forecasting engine to capture series-specific trends, seasonality, and other patterns. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Usage in AutoML

Time series identifier columns are an optional advanced setting in the Databricks AutoML forecasting UI. They are available when creating a forecasting experiment with the **Serverless** compute mode. To use them:

1. In the **Advanced options** section of the experiment creation form, locate the **Time series identifier columns** field.
2. Select one or more columns from the training data that together form a unique key for each time series.

Common examples include `store_id`, `product_id`, `location`, or a combination such as `store_id` + `sku`.

## Example

Consider a retail dataset with columns `date`, `store`, `item`, and `sales`. To forecast the sales of each item in each store separately, you would set the identifier columns to `store` and `item`. Databricks would then train a distinct forecasting model for every combination of `store` and `item`.

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) — The automated machine learning framework for time series
- [Multi-Series Forecasting](/concepts/multi-series-forecasting.md) — Forecasting multiple related time series simultaneously
- Time series — A sequence of data points indexed in time order
- [Databricks Model Training](/concepts/databricks-model-training.md) — The platform feature that includes serverless forecasting
- Forecasting horizon — How far into the future predictions are made
- Forecast frequency — The time unit (e.g., day, month) of the input data

## Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
