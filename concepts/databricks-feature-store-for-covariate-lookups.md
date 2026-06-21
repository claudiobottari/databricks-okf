---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5659fea0dffa4dba05080b0fc11e6cae9ae39d491a36ebf788d7255914a02497
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-feature-store-for-covariate-lookups
    - DFSFCL
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: Databricks Feature Store for Covariate Lookups
description: Using Databricks Feature Engineering Client to create and store feature tables that can be joined with primary training data in AutoML experiments.
tags:
  - databricks
  - feature-store
  - machine-learning
timestamp: "2026-06-18T14:30:45.774Z"
---

# Databricks Feature Store for Covariate Lookups

**Databricks Feature Store for Covariate Lookups** refers to the mechanism by which AutoML forecasting experiments can use one or more external feature tables — stored in the [Feature Store](/concepts/feature-store.md) — as additional predictors alongside the primary training data. These external variables, called covariates or external regressors, are joined into the training dataset during an AutoML forecasting run using the `feature_store_lookups` parameter.

## Overview

Covariates are additional variables outside the target time series that can improve forecasting accuracy. For example, when predicting hotel occupancy rates, a simple binary indicator of whether a date falls on a weekend can serve as a covariate that helps the model capture recurring patterns in customer behavior. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

To use covariates with AutoML forecasting, the covariate data must be stored as a feature table in the [Feature Store](/concepts/feature-store.md). The AutoML experiment then references those feature tables using a lookup configuration, which joins the covariate features with the primary training data at the specified lookup key. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Creating the Feature Table

Feature tables are created using the [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) from the `databricks.feature_engineering` Python package. Each feature table must be defined with a primary key that matches the join key used in the `feature_store_lookups` configuration. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Example: Creating a Feature Table

The following example creates a feature table storing the `is_weekend` covariate, keyed on the `date` column:

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

Feature tables can also be created using SQL or Delta Live Tables. See [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) for additional options. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Configuring the Covariate Lookup

The `feature_store_lookups` parameter is a list of dictionaries, each containing two fields:

- **`table_name`**: The [Unity Catalog](/concepts/unity-catalog.md) three-level name of the feature table (e.g., `ml.default.hotel_weekend_features`).
- **`lookup_key`**: A list of column names in the primary training data that will be used to join the feature table. These columns must match the feature table's primary keys.

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Example: Defining a Lookup Configuration

```python
hotel_weekend_feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}

feature_lookups = [hotel_weekend_feature_lookup]
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

The `feature_store_lookups` parameter can contain multiple feature table lookups, enabling joins from several covariate tables simultaneously. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Running the AutoML Experiment

The configured lookups are passed to the `automl.forecast()` API call through the `feature_store_lookups` parameter. AutoML automatically retrieves the covariate features from the specified feature tables at inference time and includes them in model training.

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

## Benefits

- **Improved model accuracy**: Covariates provide the model with information outside the target time series, helping it capture regime changes, seasonality, or external events that affect the target variable.
- **Reusable features**: Feature tables can be shared across multiple forecasting experiments, reducing redundant feature engineering work.
- **Automated lookup**: AutoML handles the join automatically at both training and inference time.

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) — The AutoML subsystem for time-series prediction
- [Feature EngineeringClient](/concepts/featureengineeringclient-api.md) — Client for creating and managing feature tables
- [Feature Store](/concepts/feature-store.md) — Centralized repository for storing and serving features
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for feature tables
- [Covariates](/concepts/covariates-external-regressors-for-forecasting.md) — External regressors used to improve forecasting models

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
