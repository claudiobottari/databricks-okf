---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9fa0dd172fe63d74769f6bb5cf64df9838a9ef8d306b2727cfde6179d80bcca2
  pageDirectory: concepts
  sources:
    - data-preparation-for-forecasting-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-series-cross-validation-for-automl
    - TSCFA
  citations:
    - file: data-preparation-for-forecasting-databricks-on-aws.md
title: Time Series Cross-Validation for AutoML
description: AutoML uses chronological time series cross-validation to split forecasting data into train, validation, and test sets, incrementally extending the training dataset over time.
tags:
  - databricks
  - automl
  - forecasting
  - cross-validation
timestamp: "2026-06-19T09:43:20.153Z"
---

# Time Series Cross-Validation for AutoML

**Time Series Cross-Validation for AutoML** is the method used by AutoML forecasting experiments to split time-ordered data into training, validation, and test sets while preserving temporal order. Unlike standard cross-validation, which shuffles data randomly, time series cross-validation respects the chronological structure of the data to avoid lookahead bias.^[data-preparation-for-forecasting-databricks-on-aws.md]

## How It Works

For forecasting tasks, AutoML incrementally extends the training dataset chronologically and performs validation on subsequent time points. This process evaluates the model’s performance over different segments of time. Because the validation window always lies in the “future” relative to the training window, the resulting performance metrics reflect how the model would behave on unseen future data.^[data-preparation-for-forecasting-databricks-on-aws.md]

The number of cross-validation folds is not fixed; it depends on three characteristics of the input table:

- **Number of time series** – More time series may allow more folds.
- **Presence of covariates** – Models that use external regressors may require shorter validation windows.
- **Time series length** – Longer series can support more folds.

AutoML automatically determines the fold count based on these factors.^[data-preparation-for-forecasting-databricks-on-aws.md]

## Relationship to Train / Validation / Test Splits

AutoML is described as splitting data into three splits (train, validation, test) before applying time series cross-validation. The cross-validation is used *within* the training and validation stages to tune hyperparameters and select the best model. The final holdout test set provides an unbiased evaluation of the chosen model’s performance on entirely unseen future data.^[data-preparation-for-forecasting-databricks-on-aws.md]

## Benefits

- **Preserves temporal ordering** – No future data leaks into the training window.
- **Robust evaluation** – Tests the model across multiple time horizons.
- **Realistic performance estimates** – Mirrors how the model will be used in production (predicting future time points).^[data-preparation-for-forecasting-databricks-on-aws.md]

## Related Concepts

- AutoML
- [Forecasting](/concepts/forecast.md)
- Time Series
- [Cross-Validation](/concepts/crossvalidator.md)
- Data Preparation for Forecasting
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md)

## Sources

- data-preparation-for-forecasting-databricks-on-aws.md

# Citations

1. [data-preparation-for-forecasting-databricks-on-aws.md](/references/data-preparation-for-forecasting-databricks-on-aws-d40acbea.md)
