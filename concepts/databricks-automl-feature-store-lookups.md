---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 159f75815d34115e602ebd5e499544903d903031019cd56c43d6f32896eecac7
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-automl-feature-store-lookups
    - DAFSL
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: Databricks AutoML Feature Store Lookups
description: Mechanism to pass external feature tables as covariates to AutoML forecasting experiments via the feature_store_lookups parameter
tags:
  - databricks
  - automl
  - feature-store
timestamp: "2026-06-18T10:51:16.692Z"
---

# Databricks AutoML Feature Store Lookups

**Databricks AutoML Feature Store Lookups** allow you to improve forecasting models by incorporating covariates (external regressors) stored in [Feature Store](/concepts/feature-store.md) tables. By passing feature table references to an AutoML experiment, you can enrich your training data with additional variables outside the target time series that may improve prediction accuracy.^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Overview

Covariates are additional variables outside the target time series that can improve forecasting models. For example, if you're forecasting hotel occupancy rates, knowing whether a date falls on a weekend could help predict customer behavior. AutoML Feature Store Lookups enable you to join one or more covariate feature tables with your primary training data during an AutoML experiment.^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Requirements

To use covariates with AutoML, you must use a [Feature Store](/concepts/feature-store.md) to join one or more covariate feature tables with the primary training data. The feature tables must be stored in [Unity Catalog](/concepts/unity-catalog.md) and contain a primary key column that matches a column in your training dataset for the lookup join.^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Creating a Feature Table for Covariates

You can create feature tables using the Python `FeatureEngineeringClient`, SQL, or Delta Live Tables. The table must include a primary key column that will be used for the lookup join with your training data.^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Example: Creating a Feature Table

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

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Configuring Feature Store Lookups

Use the `feature_store_lookups` parameter to pass feature tables to AutoML. This parameter accepts a list of dictionaries, where each dictionary contains two fields:

- `table_name`: The name of the feature table in Unity Catalog.
- `lookup_key`: A list of column names used to join the feature table with the training data.

You can include multiple feature table lookups in a single AutoML experiment.^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Example: Configuring Lookups

```python
hotel_weekend_feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}

feature_lookups = [hotel_weekend_feature_lookup]
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Running an AutoML Experiment with Feature Store Lookups

Pass the `feature_store_lookups` parameter to the AutoML experiment API call. The following example demonstrates a forecasting experiment that uses feature store lookups:

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

## Best Practices

- **Use meaningful covariates**: Choose external variables that have a logical relationship with your target time series to improve model accuracy.
- **Ensure primary key alignment**: The `lookup_key` columns must match between your feature table and training dataset for successful joins.
- **Store feature tables in Unity Catalog**: Feature tables used for AutoML lookups must be registered in Unity Catalog.
- **Combine multiple lookups**: You can include several feature tables in a single experiment to incorporate diverse external signals.

## Limitations

- Feature Store Lookups are currently supported for forecasting AutoML experiments.
- The feature tables must be accessible in the same Unity Catalog [Metastore](/concepts/metastore.md) as your workspace.

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) — The forecasting experiment type that supports feature store lookups
- [Feature Store](/concepts/feature-store.md) — The system for managing and serving feature tables
- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) — How to create and manage feature tables
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for managing feature tables
- [Databricks AutoML](/concepts/databricks-automl.md) — The automated machine learning platform

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
