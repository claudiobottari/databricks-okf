---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 71e34681c1df56070919bc800e97839ecefed61c7df63c3cb4a962f2216f09f5
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-feature_store_lookups-parameter
    - AFP
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: AutoML feature_store_lookups Parameter
description: A configuration parameter in Databricks AutoML forecasting API that accepts a list of feature table lookups to include covariates in the experiment.
tags:
  - databricks
  - automl
  - api
timestamp: "2026-06-18T14:30:35.621Z"
---

# AutoML `feature_store_lookups` Parameter

The **`feature_store_lookups`** parameter enables AutoML forecasting experiments to incorporate covariates (also known as external regressors) from [Feature Store](/concepts/feature-store.md) tables. Covariates are additional variables outside the target time series that can improve forecasting model accuracy. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Overview

When running an AutoML forecasting experiment, the `feature_store_lookups` parameter allows you to pass one or more feature tables that contain supplementary features to join with the primary training data. This enables the forecasting model to leverage external signals that may influence the target variable. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

For example, when forecasting hotel occupancy rates, a covariate indicating whether a date falls on a weekend can help predict customer behavior more accurately than using the occupancy time series alone. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Parameter Structure

The `feature_store_lookups` parameter accepts a list of dictionaries, where each dictionary contains two required fields: ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

| Field | Description |
|-------|-------------|
| `table_name` | The fully qualified name of the feature table in Unity Catalog (e.g., `ml.default.hotel_weekend_features`) |
| `lookup_key` | A list of column names used as the join key between the feature table and the primary training data |

### Example

```python
hotel_weekend_feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}

feature_lookups = [hotel_weekend_feature_lookup]
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Multiple Feature Tables

The `feature_store_lookups` parameter can contain multiple feature table lookups, allowing you to combine covariates from different sources in a single AutoML experiment. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Usage in AutoML Experiments

Pass the `feature_store_lookups` list to the AutoML forecasting API call: ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

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

## Prerequisites

To use `feature_store_lookups`, you must first create and store your covariate data as a [Feature Store](/concepts/feature-store.md) table. Feature tables can be created using: ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

- The Python `FeatureEngineeringClient` API
- SQL commands
- Delta Live Tables

The feature table must be stored in [Unity Catalog](/concepts/unity-catalog.md) and include a primary key column that matches the lookup key used in the AutoML experiment. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) — The primary AutoML workflow that accepts `feature_store_lookups`
- [Feature Store](/concepts/feature-store.md) — The system for storing and serving feature tables
- [Covariates](/concepts/covariates-external-regressors-in-time-series-forecasting.md) — External variables that improve forecasting model accuracy
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The process of creating meaningful features from raw data
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for managing feature tables

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
