---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e9cc0a22eacb5608c626eb7d35ea9b23fb0a39f1f6051a89983d7066a0c790e
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-feature-store-lookups
    - AFSL
    - automl-feature-store-lookups-parameter
    - AFSLP
    - automl-feature_store_lookups-parameter
    - AFP
    - databricks-automl-feature-store-lookups
    - DAFSL
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: AutoML Feature Store Lookups
description: A mechanism in Databricks AutoML to pass external feature tables as covariates to forecasting experiments using the feature_store_lookups parameter.
tags:
  - automl
  - databricks
  - feature-store
timestamp: "2026-06-19T22:11:49.419Z"
---

# AutoML Feature Store Lookups

**AutoML Feature Store Lookups** is a feature in Databricks AutoML that allows you to enrich forecasting models with additional variables stored in [Feature Store](/concepts/feature-store.md) tables, also known as covariates or external regressors. By incorporating feature store lookups, you can improve model accuracy by providing the algorithm with relevant external information that the target time series alone may not capture. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Overview

Covariates are variables outside the target time series that can improve forecasting predictions. For example, when forecasting hotel occupancy rates, knowing whether a date falls on a weekend can help predict customer behavior more accurately than using the historical occupancy series alone. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

To use covariates with AutoML, you must register the covariate data as a [Feature Store](/concepts/feature-store.md) table and then pass it to the AutoML experiment through the `feature_store_lookups` parameter. AutoML automatically joins the feature tables with the primary training data during model training. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Feature Store Table Requirements

Covariate feature tables must be stored in [Unity Catalog](/concepts/unity-catalog.md) and must include a primary key column that matches a column in the training dataset used for joining. The primary key is typically a time-related column such as `date`. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

Feature tables can be created using:
- The Python `FeatureEngineeringClient` from the `databricks.feature_engineering` library
- SQL statements
- Delta Live Tables

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Configuration

The `feature_store_lookups` parameter accepts a list of dictionaries, where each dictionary contains two fields:

- `table_name`: The Unity Catalog name of the feature table (e.g., `ml.default.hotel_weekend_features`)
- `lookup_key`: A list of column names used to join the feature table with the training dataset (e.g., `["date"]`)

You can pass multiple feature table lookups in a single AutoML experiment, enabling the use of several covariate tables simultaneously. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Example Usage

The following code demonstrates the complete workflow for using feature store lookups in an AutoML forecasting experiment:

1. **Create and register feature tables:**

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

2. **Configure the lookups and run AutoML:**

```python
from databricks import automl

hotel_weekend_feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}

feature_lookups = [hotel_weekend_feature_lookup]

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

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — Centralized repository for storing and serving features
- [AutoML Forecasting](/concepts/automl-forecast.md) — Automated time series forecasting on Databricks
- [Covariates in Time Series](/concepts/covariates-in-time-series-forecasting.md) — External regressors used to improve forecasting accuracy
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — Process of creating features from raw data
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for managing data assets including feature tables

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
