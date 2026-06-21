---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 02d047706b84082f0042084259c669d1edff3f0cad084a3384f8b568b80f530e
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-engineering-for-time-series-forecasting
    - FEFTSF
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: Feature Engineering for Time Series Forecasting
description: Creating derived features from date/time columns — such as is_weekend binary flags using dayofweek — to improve forecasting model accuracy.
tags:
  - feature-engineering
  - time-series
  - databricks
timestamp: "2026-06-19T17:38:55.893Z"
---

# Feature Engineering for Time Series Forecasting

**Feature engineering for time series forecasting** involves creating predictive variables (features) from raw temporal data to improve model accuracy. A common technique is to derive features from date‑time information, such as day of week, month, or holiday indicators. These engineered features often act as **covariates** (also called external regressors) — additional variables outside the target time series that can help the model capture recurring patterns and external influences. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Creating Features from Date/Time

A simple yet powerful example is a binary `is_weekend` feature. Using the day‑of‑week information, one can label each observation as a weekday (0) or weekend (1). For instance, with PySpark:

```python
from pyspark.sql.functions import dayofweek, when

def compute_weekend_features(df):
    return df.select("date").withColumn(
        "is_weekend",
        when(dayofweek("date").isin(1, 2, 3, 4, 5), 0)  # Weekday
        .when(dayofweek("date").isin(6, 7), 1)           # Weekend
    )
```

This feature can be stored and later used as a covariate in a [Time Series Forecasting](/concepts/multi-series-forecasting.md) model. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Storing Features in a Feature Store

To reuse engineered features across experiments, they should be stored in a [Feature Store](/concepts/feature-store.md). Using the [Databricks Feature Engineering Client](/concepts/databricks-feature-engineering-client.md), you can create a feature table with a primary key (typically the timestamp column) and write the computed features to it. For example:

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()
fe.create_table(
    name='ml.default.weekend_features',   # adjust to your catalog/schema
    primary_keys=['date'],
    df=weekend_feature_df,
    description='Weekend indicator features'
)
```

The feature table can then be referenced in downstream modelling tasks. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Using Covariates in AutoML Forecasting

When running an AutoML forecasting experiment, you can supply the engineered covariates via the `feature_store_lookups` parameter. This parameter accepts a list of dictionaries, each specifying a feature table name and the lookup keys (columns used to join the covariate table to the training data). For example:

```python
feature_lookup = {
    "table_name": "ml.default.weekend_features",
    "lookup_key": ["date"]
}
feature_store_lookups = [feature_lookup]
```

Pass this list to the `automl.forecast()` function:

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
    feature_store_lookups=feature_store_lookups
)
```

AutoML will automatically join the covariate table with the primary training data, enabling the model to learn from both the target series and the engineered features. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Additional Feature Engineering Techniques

Beyond date/time indicators, common time series features include:

- **Lag features**: Previous values of the target variable at specified offsets
- **Rolling window statistics**: Moving averages, standard deviations, or other aggregates over a sliding window
- **Differencing**: The change between consecutive observations
- **Fourier transforms**: Capturing cyclical patterns at various frequencies
- **Holiday indicators**: Binary features for known holidays or special events
- **Time since event**: The number of periods since a particular event occurred

These features help models capture Temporal Dependencies and Seasonal Patterns in the data.

## Related Concepts

- [External Regressors / Covariates](/concepts/covariates-external-regressors-for-forecasting.md)
- [Time Series Forecasting](/concepts/multi-series-forecasting.md)
- [Databricks AutoML](/concepts/databricks-automl.md)
- PySpark Feature Engineering
- [Feature Store](/concepts/feature-store.md)
- Lag Features
- Rolling Window Features
- Seasonal Decomposition

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
