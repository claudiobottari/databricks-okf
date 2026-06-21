---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bfdc742201b6144e2efff059f17fb22bfaea1511deff76e5d35dc7e2de556c46
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-automl-forecasting-experiment
    - DAFE
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: Databricks AutoML Forecasting Experiment
description: The automated machine learning workflow in Databricks for forecasting tasks, supporting parameters like target_col, time_col, frequency, horizon, and identity_col.
tags:
  - databricks
  - automl
  - forecasting
timestamp: "2026-06-18T14:30:47.031Z"
---

# Databricks AutoML Forecasting Experiment

**Databricks AutoML Forecasting Experiment** is a feature of [Databricks AutoML](/concepts/databricks-automl.md) that automates the process of building time series forecasting models. It uses the `automl.forecast()` Python API to automatically train, tune, and evaluate multiple forecasting models on a given dataset, returning the best-performing model along with a summary of the experiment. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Overview

The AutoML forecasting experiment takes a time series dataset with a target column to predict, a time column, and configuration parameters such as forecast frequency and horizon. It automatically handles data preprocessing, model selection, hyperparameter tuning, and evaluation, producing a ready-to-deploy forecasting model. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Using Covariates (External Regressors)

Covariates, also known as external regressors, are additional variables outside the target time series that can improve forecasting model accuracy. For example, when forecasting hotel occupancy rates, knowing whether a date falls on a weekend can help predict customer behavior. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

To use covariates in an AutoML forecasting experiment, you must store them in a [Feature Store](/concepts/feature-store.md) table and pass them to the experiment using the `feature_store_lookups` parameter. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Feature Engineering for Covariates

Before using covariates, you typically perform feature engineering to create useful predictor variables from your data. For instance, you might compute a binary `is_weekend` feature from a date column: ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

```python
from pyspark.sql.functions import dayofweek, when

def compute_hotel_weekend_features(df):
    ''' is_weekend feature computation code returns a DataFrame with 'date' as primary key'''
    return df.select("date").withColumn(
        "is_weekend",
        when(dayofweek("date").isin(1, 2, 3, 4, 5), 0)  # Weekday
        .when(dayofweek("date").isin(6, 7), 1)  # Weekend
    )
```

### Creating the Feature Store Table

The engineered features must be stored as a Feature Store table with a primary key that matches the time column in the training data: ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

hotel_weekend_feature_table = fe.create_table(
    name='ml.default.hotel_weekend_features',
    primary_keys=['date'],
    df=hotel_weekend_feature_df,
    description='Hotel is_weekend features table'
)
```

You can also use SQL or Delta Live Tables to create and write feature tables. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Configuring the Experiment with Covariates

Pass the feature store lookups to the AutoML experiment using the `feature_store_lookups` parameter. This parameter accepts a list of dictionaries, each containing `table_name` and `lookup_key` fields: ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

```python
hotel_weekend_feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}

feature_lookups = [hotel_weekend_feature_lookup]
```

The `feature_store_lookups` parameter can contain multiple feature table lookups. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Running the Experiment

Use the `automl.forecast()` function to run the experiment. Key parameters include: ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

- `dataset`: The training DataFrame
- `target_col`: The column to predict
- `time_col`: The time column
- `frequency`: The forecast frequency (e.g., `"d"` for daily)
- `horizon`: The number of time steps to forecast
- `timeout_minutes`: Maximum experiment runtime
- `identity_col`: Optional column for grouping time series
- `feature_store_lookups`: Optional list of feature table lookups for covariates

```python
from databricks import automl

summary = automl.forecast(
    dataset=df,
    target_col="occupancy_rate",
    time_col="date",
    frequency="d",
    horizon=1,
    timeout_minutes=30,
    identity_col=None,
    feature_store_lookups=feature_lookups
)
```

## Output

The experiment returns a summary object containing the best-performing model, evaluation metrics, and metadata about the experiment run. The resulting model can be registered in [MLflow Model Registry](/concepts/mlflow-model-registry.md) and deployed for inference. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Related Concepts

- [Databricks AutoML](/concepts/databricks-automl.md) — The broader automated machine learning framework
- [Feature Store](/concepts/feature-store.md) — Centralized repository for feature tables used in covariates
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Model lifecycle management for AutoML outputs
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) — The underlying modeling task
- [AutoML Python API Reference](/concepts/automl-python-api.md) — Complete API documentation

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
