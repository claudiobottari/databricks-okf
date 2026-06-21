---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f9990ce0814afd2a4a5ae286bc1fb74da083b5ffe5eda90f973efc0b60313e18
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - featureengineeringclient-for-covariate-tables
    - FFCT
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: FeatureEngineeringClient for Covariate Tables
description: Databricks API client used to create and register feature tables with a primary key (e.g., date) for use as covariates in AutoML
tags:
  - databricks
  - API
  - feature-store
timestamp: "2026-06-18T10:51:15.572Z"
---

# FeatureEngineeringClient for Covariate Tables

The `FeatureEngineeringClient` is a Python SDK client that enables you to create, manage, and store [Feature Tables](/concepts/feature-table.md) in [Unity Catalog](/concepts/unity-catalog.md) for use as covariates (external regressors) in AutoML forecasting experiments. Covariates are additional variables outside the target time series that can improve forecasting model accuracy. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Overview

When building forecasting models, covariates such as day-of-week indicators, holiday flags, or weather data can provide predictive signal beyond the target time series alone. The `FeatureEngineeringClient` allows you to compute these features, store them in Unity Catalog as feature tables, and then reference them in AutoML forecasting experiments using the `feature_store_lookups` parameter. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Creating a Covariate Feature Table

To use covariates in AutoML forecasting, you must store feature data in a [Unity Catalog](/concepts/unity-catalog.md) feature table using the `FeatureEngineeringClient`. The feature table must include a primary key column that matches a column in your training data — typically the date or time column used for forecasting. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Example: Weekend Feature Engineering

The following example demonstrates feature engineering a binary `is_weekend` indicator from a date column and storing it as a feature table:

```python
from databricks.feature_engineering import FeatureEngineeringClient
from pyspark.sql.functions import dayofweek, when

def compute_hotel_weekend_features(df):
    """Returns a DataFrame with 'date' as primary key and 'is_weekend' feature."""
    return df.select("date").withColumn(
        "is_weekend",
        when(dayofweek("date").isin(1, 2, 3, 4, 5), 0)  # Weekday
        .when(dayofweek("date").isin(6, 7), 1)           # Weekend
    )

hotel_weekend_feature_df = compute_hotel_weekend_features(df)

fe = FeatureEngineeringClient()
hotel_weekend_feature_table = fe.create_table(
    name='ml.default.hotel_weekend_features',
    primary_keys=['date'],
    df=hotel_weekend_feature_df,
    description='Hotel is_weekend features table'
)
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

You can also use SQL or Delta Live Tables to write and create feature tables. See [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) for more options. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Using Covariate Tables in AutoML Forecasting

Once your covariate feature table is created, you pass it to the AutoML forecasting experiment using the `feature_store_lookups` parameter. This parameter accepts a list of dictionaries, each containing two fields:

- `table_name`: The fully qualified name of the feature table in Unity Catalog.
- `lookup_key`: A list of column names used to join the feature table to the training data.

### Example: Configuring Feature Store Lookups

```python
hotel_weekend_feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}
feature_lookups = [hotel_weekend_feature_lookup]
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

You can include multiple feature table lookups in the list, enabling complex feature compositions from different sources. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Example: Running an AutoML Forecast with Covariates

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

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Key Considerations

- The feature table's primary key must match a column in your training dataset — typically the time column for forecasting use cases. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- Feature tables used as covariates must be stored in Unity Catalog. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- The `feature_store_lookups` parameter can reference multiple feature tables, allowing you to combine different covariate sources. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- Feature engineering is performed separately from the AutoML experiment, giving you full control over feature computation logic. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) — The automated machine learning workflow for time series prediction
- [Feature Store](/concepts/feature-store.md) — The centralized repository for feature tables in Databricks
- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) — Documentation on creating and managing feature tables
- Covariates (External Regressors) — The statistical concept of auxiliary time series variables
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for managing data and AI assets
- [MLflow](/concepts/mlflow.md) — Tracking and logging framework for machine learning experiments

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
