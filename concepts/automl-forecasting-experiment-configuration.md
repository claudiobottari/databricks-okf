---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 51f9e6cb4bb2e3d88c966b3cb1ee854fc079486352801b85e1ff40d2ffe1d920
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-forecasting-experiment-configuration
    - AFEC
    - Forecast experiment configuration
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: AutoML Forecasting Experiment Configuration
description: Configuring and launching an automated forecasting experiment in Databricks AutoML with parameters for target column, time column, frequency, horizon, and timeout.
tags:
  - automl
  - forecasting
  - databricks
timestamp: "2026-06-19T22:11:49.663Z"
---

# AutoML Forecasting Experiment Configuration

**AutoML Forecasting Experiment Configuration** refers to the setup and parameters used when running an AutoML forecasting experiment on Databricks, particularly the mechanism for incorporating [covariates](/concepts/covariates-external-regressors-in-time-series-forecasting.md) (external regressors) via [Feature Store](/concepts/feature-store.md) lookups. The configuration allows users to join additional feature tables to the primary training data, improving forecast accuracy by including external factors that influence the target time series. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Overview

Covariates are variables outside the target time series that can improve forecasting models. For example, when forecasting hotel occupancy rates, knowing whether a date falls on a weekend can help predict customer behavior. Databricks AutoML supports passing these external covariates through a Feature Store lookup mechanism, which joins one or more feature tables with the primary training dataset at experiment execution time. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Prerequisites

To use covariates in an AutoML forecasting experiment, you must:

- Create a [Feature Store](/concepts/feature-store.md) table containing the covariate features, with a primary key that matches a column in the training dataset (commonly the time column or an identity column).
- Use the `FeatureEngineeringClient` (or SQL, Delta Live Tables) to create and write the feature table in [Unity Catalog](/concepts/unity-catalog.md).
- Ensure the primary key column in the feature table corresponds to a lookup key in the training data that can be used for joins. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Configuration Steps

### 1. Create the Feature Table

The covariate data must be stored as a Unity Catalog-managed feature table. For example, a table of weekend indicators for each date is created with `'date'` as the primary key:

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()
hotel_weekend_feature_table = fe.create_table(
    name='ml.default.hotel_weekend_features',  # change to desired location
    primary_keys=['date'],
    df=hotel_weekend_feature_df,
    description='Hotel is_weekend features table'
)
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### 2. Define the Feature Store Lookup

The `feature_store_lookups` parameter in the AutoML forecasting call is a list of dictionaries. Each dictionary specifies the `table_name` and `lookup_key` columns for a feature table to be joined:

```python
hotel_weekend_feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}
feature_lookups = [hotel_weekend_feature_lookup]
```

Multiple feature tables can be included in the list, enabling the use of several covariate sources simultaneously. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### 3. Run the AutoML Forecasting Experiment

Pass the `feature_store_lookups` parameter to `automl.forecast()`:

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

AutoML automatically joins the feature tables using the specified lookup keys before training forecasting models. The resulting experiment incorporates the external regressors as additional features. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Example Walkthrough

The source example uses randomly generated daily hotel occupancy data for January 2024 to predict February 1. The covariate is a binary `is_weekend` feature computed from the date column. After creating the feature table and configuring the lookup, AutoML runs a forecasting experiment with a horizon of 1 day and a 30-minute timeout. No identity column is used in this case. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Related Concepts

- AutoML – Automated machine learning service on Databricks.
- [Feature Store](/concepts/feature-store.md) – Centralized repository for feature tables used in machine learning.
- Covariates (External Regressors) – Additional variables that can improve time series forecasts.
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) – The overarching task AutoML addresses.
- [Unity Catalog](/concepts/unity-catalog.md) – Data governance platform for managing feature tables.
- [Feature Engineering](/concepts/featureengineeringclient-api.md) – Process of creating features from raw data.

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
