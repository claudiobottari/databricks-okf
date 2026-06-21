---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 16a313574f24904f086d89058716f0941125441da3a98a96320e6314425bf49b
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-feature-store-lookups-parameter
    - AFSLP
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: AutoML Feature Store Lookups Parameter
description: The feature_store_lookups parameter in Databricks AutoML that links one or more Feature Store tables (keyed by lookup_key) as covariates in a forecasting experiment.
tags:
  - databricks
  - automl
  - api
timestamp: "2026-06-19T17:38:41.521Z"
---

# AutoML Feature Store Lookups Parameter

The **AutoML Feature Store Lookups Parameter** (`feature_store_lookups`) is a configuration option passed to AutoML experiment calls (such as `automl.forecast()`) that enables the use of [Feature Store](/concepts/feature-store.md) tables as external covariates (also known as external regressors) for forecasting models. Covariates are additional variables outside the target time series that can improve model accuracy — for example, a binary `is_weekend` feature when predicting hotel occupancy rates. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Parameter Structure

`feature_store_lookups` accepts a list of dictionary objects, where each dictionary contains exactly two fields:

- **`table_name`** (string) – The fully qualified name of a Feature Store table in [Unity Catalog](/concepts/unity-catalog.md) (e.g., `ml.default.hotel_weekend_features`). The table must be registered in Feature Store and contain the covariate features.
- **`lookup_key`** (list of strings) – The column names used to join the feature table with the primary training dataset. Typically this is the time column or another primary key column (e.g., `["date"]`).

Multiple feature table lookups can be listed in the same call, allowing the model to use features from several different covariate tables simultaneously. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Usage in an AutoML Experiment

The parameter is passed directly to the [AutoML Python API](/concepts/automl-python-api.md) when starting a forecast experiment. The following example shows how to define a lookup for a weekend‑features table and then run an experiment:

```python
from databricks import automl

# Define a single feature store lookup
feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}
feature_lookups = [feature_lookup]

# Run AutoML forecasting with the lookup
summary = automl.forecast(
    dataset=df,
    target_col="occupancy_rate",
    time_col="date",
    frequency="d",
    horizon=1,
    timeout_minutes=30,
    feature_store_lookups=feature_lookups
)
```

AutoML automatically joins the feature store tables at training and inference time, using the lookup key columns to align rows. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Requirements

- The covariate features must be stored in a [Feature Store](/concepts/feature-store.md) table, which can be created using the `FeatureEngineeringClient`, SQL, or Delta Live Tables.
- The lookup key columns must exist in both the feature store table and the primary training DataFrame.
- The feature store table should be registered in Unity Catalog (as shown in the example). ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) – The overall workflow for time‑series forecasting with AutoML.
- Covariates (External Regressors) – Additional predictors that can improve forecast accuracy.
- [Feature Engineering on Databricks](/concepts/feature-engineering-on-databricks.md) – Techniques for creating and transforming features before storing them in Feature Store.
- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) – How to register and manage feature tables for use in AutoML and other ML workloads.

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
