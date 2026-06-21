---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dab5153a62ed60629b5fbe71f92ba10da9ae9896f10ec27bbcdb601c64998265
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store-lookups-in-automl
    - FSLIA
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: Feature Store Lookups in AutoML
description: The mechanism for passing Databricks Feature Store tables as covariates to AutoML forecasting experiments using the feature_store_lookups parameter.
tags:
  - databricks
  - automl
  - feature-store
  - mlops
timestamp: "2026-06-19T14:07:18.452Z"
---

# Feature Store Lookups in AutoML

**Feature Store Lookups in AutoML** refers to the mechanism that allows AutoML experiments to reference and join feature tables from the [Feature Store](/concepts/feature-store.md) (Databricks Feature Engineering) as additional input variables during model training. This capability is particularly important for forecasting tasks, where external covariates — variables outside the target time series — can significantly improve prediction accuracy.

## Overview

Feature Store lookups enable AutoML to incorporate pre-computed feature tables alongside the primary training dataset. By specifying one or more feature tables through the `feature_store_lookups` parameter, AutoML automatically joins the feature data with the training data at runtime using defined lookup keys. This allows models to leverage curated, reusable features without manually merging datasets before starting the experiment. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Covariates in Forecasting

Covariates — also known as external regressors — are additional variables outside the target time series that can improve forecasting models. For example, when forecasting hotel occupancy rates, knowing whether a date falls on a weekend can help predict customer behavior. Feature Store lookups make it straightforward to supply such covariates to an AutoML forecasting experiment. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Requirements

To use covariates with AutoML, you must use the Databricks Feature Store to host one or more covariate feature tables. AutoML then joins these feature tables with the primary training data during the experiment. Feature tables must be stored in [Unity Catalog](/concepts/unity-catalog.md) and defined with appropriate primary keys that match the lookup keys used in the experiment configuration. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Configuration

### Creating a Feature Table

Feature tables can be created using the Python `FeatureEngineeringClient`, SQL, or Delta Live Tables. Each table must specify primary keys that serve as join keys for the lookup. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

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

### Defining Feature Store Lookups

The `feature_store_lookups` parameter accepts a list of dictionaries, where each dictionary contains two required fields: `table_name` (the fully qualified name of the feature table in Unity Catalog) and `lookup_key` (a list of column names used to join the feature table with the training data). Multiple feature table lookups can be specified in a single experiment. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

```python
hotel_weekend_feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}

feature_lookups = [hotel_weekend_feature_lookup]
```

### Running an AutoML Experiment with Lookups

Pass the configured `feature_lookups` to the AutoML experiment API call. AutoML automatically joins the specified feature tables with the training dataset during the experiment. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

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

## Supported Use Cases

While the example above focuses on forecasting, Feature Store lookups can potentially be applied to other AutoML problem types (classification, regression) where external feature tables improve model quality. The primary documented use case is forecasting with covariates. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Best Practices

- **Align primary keys with lookup keys.** Ensure that the primary keys defined in the feature table match the columns used as `lookup_key` in the AutoML configuration.
- **Store features in Unity Catalog.** Feature tables must be registered in Unity Catalog for AutoML to access them during lookups.
- **Use consistent time granularity.** For forecasting, ensure that the time column in the training data aligns with the lookup key (e.g., both use dates at daily granularity).
- **Pre-compute reusable features.** Feature Store lookups are most beneficial when features are computed once and reused across multiple experiments, promoting consistency and reducing duplication.

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) — Time series forecasting with automated model selection
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) — Python API for creating and managing feature tables
- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) — Storage and governance for feature tables
- [Covariates and External Regressors](/concepts/covariates-external-regressors-for-forecasting.md) — Additional variables used in forecasting models
- [AutoML Python API Reference](/concepts/automl-python-api.md) — Full documentation for AutoML parameters and configuration

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
