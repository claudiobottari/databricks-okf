---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 47b57c51ee669b47b98679a9fbbc565645297d6eaacf93bb9e68afcfc88d7197
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-series-forecasting-with-time-series-identifiers
    - MFWTSI
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: Multi-Series Forecasting with Time Series Identifiers
description: The ability to forecast multiple independent time series simultaneously by designating columns that identify each series, with a model trained per series.
tags:
  - forecasting
  - time-series
  - multi-series
timestamp: "2026-06-19T10:37:05.373Z"
---

# Multi-Series Forecasting with Time Series Identifiers

**Multi-Series Forecasting with Time Series Identifiers** is a technique in which a forecasting model is trained on multiple independent time series within a single dataset, using designated columns to group observations into separate series. Each series is modeled independently, enabling the simultaneous generation of forecasts for many related time sequences.

## Overview

In many real-world forecasting scenarios, the input data contains not one but many distinct time series. For example, sales data may include separate series for each product, store, or region. To handle this, the forecasting framework must identify which column(s) define the boundaries between individual time series. These are called **time series identifier columns**. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## How It Works

When performing multi-series forecasting, the user specifies one or more columns as **time series identifier columns** during experiment setup. The system then groups the data by these columns, treating each unique combination as a separate time series. Each series is processed independently during model training and evaluation. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Specification in the UI

In the Databricks Model Training UI, the **Time series identifier columns** option is found under **Advanced options** when creating a forecasting experiment. The user selects the column(s) that identify the individual time series. Databricks groups the data by these columns as different time series and trains a model for each series independently. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Example

Consider a dataset containing sales data for multiple products across several stores:

| Date | Product | Store | Sales |
|------|---------|-------|-------|
| 2024-01-01 | Widget A | Store 1 | 100 |
| 2024-01-01 | Widget B | Store 1 | 150 |
| 2024-01-02 | Widget A | Store 1 | 110 |

If **Product** and **Store** are selected as time series identifier columns, the system creates separate forecasting models for each unique (Product, Store) combination. Each series is treated independently with its own training and evaluation. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Use Cases

- **Retail forecasting**: Predicting sales for multiple products across multiple store locations, with each product-store combination as a separate series.
- **Demand planning**: Forecasting demand for different product categories or SKUs.
- **Energy load forecasting**: Predicting energy consumption for multiple buildings or zones.
- **Inventory management**: Forecasting stock levels for individual items across warehouses.

## Requirements

- The training data must contain a **time series column** of type `timestamp` or `date`.
- The data must be saved as a [Unity Catalog](/concepts/unity-catalog.md) table.
- Time series identifier columns can be any data type that meaningfully distinguishes series. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Related Concepts

- [Multi-Series Forecasting](/concepts/multi-series-forecasting.md) – The general approach of forecasting multiple related time series.
- Forecasting with AutoML – The broader framework for automated time series forecasting.
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) – The fundamental concept of predicting future values based on historical patterns.
- [Forecast Horizon](/concepts/forecast-frequency-and-horizon.md) – The number of time steps to predict into the future.
- Forecast Frequency – The time unit representing the input data's granularity.
- Auto-ARIMA – An algorithm that requires regular frequency in time series data.

## Best Practices

- **Choose meaningful identifiers**: Select columns that naturally define distinct forecasting scenarios (e.g., product IDs, store codes, region labels).
- **Ensure consistent frequency**: For algorithms like Auto-ARIMA, each individual time series must have a regular frequency with consistent intervals between points. Missing time steps are handled by filling with previous values.
- **Balance series independence**: While each series is trained independently, they share the same overall forecasting framework and hyperparameter tuning process.

## Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
