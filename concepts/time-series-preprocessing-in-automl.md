---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1dcaac2fe2bcaeea92f3c7369948a9b6c6217480e6374a59bedb6f2911716296
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-series-preprocessing-in-automl
    - TSPIA
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: Time Series Preprocessing in AutoML
description: The automatic data preparation steps in Databricks Serverless Forecasting, including missing value imputation, data splitting, and one-hot encoding of categorical features.
tags:
  - preprocessing
  - time-series
  - feature-engineering
  - automl
timestamp: "2026-06-19T10:36:45.189Z"
---

# Time Series Preprocessing in AutoML

**Time Series Preprocessing in AutoML** refers to the validation, cleaning, and transformation steps that AutoML forecasting experiments apply to input time series data before model training begins. This preprocessing stage is critical for ensuring data quality and compatibility with forecasting algorithms.

## Overview

When running a serverless forecasting experiment through the Databricks Model Training UI, the preprocessing stage is the first phase executed after starting the experiment. During this stage, AutoML validates and prepares the input table by imputing missing values and splitting data into training, validation, and test sets. Automatic feature generation processing, such as one-hot encoding for categorical features, also occurs during this stage. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Key Preprocessing Steps

### Data Validation

AutoML validates that the input data meets the requirements for forecasting, including verifying that the time column is of type `timestamp` or `date` and that the data is structured appropriately for the chosen forecast frequency. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Handling Missing Time Steps

For algorithms that require regular frequency — such as Auto-ARIMA — the time series must have consistent intervals between all data points. AutoML handles missing time steps by filling in those values with the previous value (forward fill). This ensures that irregular time series are regularized before training. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Data Splitting

The data is automatically split into training, validation, and test sets to enable proper model evaluation. Users can optionally specify a custom split column with values "train", "validate", and "test" to control partitioning manually. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Feature Engineering

During preprocessing, automatic feature generation occurs. This includes:
- **One-hot encoding**: Categorical features are transformed into numerical representations.
- **Holiday region covariates**: If specified, holiday region data is prepared for use as additional features during model training. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Imputation

In addition to handling missing time steps, AutoML fills in any missing values in the time series data to ensure complete input for model training. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Post-Preprocessing Stages

After preprocessing completes, AutoML proceeds to:

1. **Tuning**: Exploring different forecasting algorithms and tuning hyperparameters.
2. **Training**: Training and evaluating the final model with selected best configurations. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Preprocessing Configuration Options

Users can influence preprocessing behavior through the following settings:

- **Forecast frequency**: Determines the granularity of time series aggregation.
- **Forecast horizon**: Defines how many time units to forecast.
- **Split column**: Optional column for custom data partitioning.
- **Weight column**: For weighting individual time series (all samples in a series must share the same weight, range [0, 10000]).
- **Time series identifier columns**: For [Multi-Series Forecasting](/concepts/multi-series-forecasting.md), columns that identify individual time series — data is grouped by these columns and each series is preprocessed independently. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Related Concepts

- [AutoML Forecasting Experiments](/concepts/automl-forecasting-experiment-stages.md)
- [Serverless Forecasting](/concepts/databricks-serverless-forecasting.md)
- Auto-ARIMA
- [Multi-Series Forecasting](/concepts/multi-series-forecasting.md)
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md)

## Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
