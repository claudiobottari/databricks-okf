---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f111721b75a5ba5d252ab86bc25a66101b35b524f1c64787647fb97f5673105
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-experiment-with-feature_store_lookups
    - AEWF
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: AutoML Experiment with feature_store_lookups
description: The mechanism to pass Feature Store tables as covariates to an AutoML forecasting experiment via the feature_store_lookups parameter
tags:
  - databricks
  - automl
  - api
timestamp: "2026-06-19T09:06:54.289Z"
---

---
title: AutoML Experiment with feature_store_lookups
summary: Using the `feature_store_lookups` parameter to pass Feature Store tables as covariates (external regressors) in an AutoML forecasting experiment on Databricks.
sources:
  - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - automl
  - feature-store
  - forecasting
  - covariates
aliases:
  - automl-experiment-with-feature-store-lookups
  - automl-feature_store_lookups
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# AutoML Experiment with `feature_store_lookups`

**AutoML Experiment with `feature_store_lookups`** refers to the use of the `feature_store_lookups` parameter in Databricks AutoML forecasting experiments to incorporate covariates (also known as external regressors) from a [Feature Store](/concepts/feature-store.md). Covariates are additional variables outside the target time series that can improve forecast accuracy; for example, a binary "is_weekend" flag can help predict hotel occupancy rates. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Overview

When running an AutoML forecasting experiment, the training data typically contains only the time series target and a time column. To include external regressors, you must:

1. Create one or more feature tables in the [Feature Store](/concepts/feature-store.md) that contain the covariate data along with a primary key (usually the date/time column).
2. Pass those feature tables to AutoML via the `feature_store_lookups` parameter.
3. AutoML automatically joins the feature tables with the primary training data using the specified lookup keys.

The `feature_store_lookups` parameter accepts a list of dictionaries, each containing a `table_name` (the Unity Catalog path of the feature table) and a `lookup_key` (the column name to join on). Multiple feature tables can be included in the same list. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Prerequisites

- A [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) and a schema where the feature table will be stored.
- The feature table must be created before running the AutoML experiment. It can be created using the Python `FeatureEngineeringClient`, SQL, or Delta Live Tables. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]
- The lookup key (typically `date`) must exist as a column in both the primary training dataset and the feature table.

## Creating a Feature Store Table

Use the `FeatureEngineeringClient` to create and write a feature table containing the covariate data. The table must define at least one primary key that matches the time column in the primary dataset. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

# Example: create a feature table with an "is_weekend" column
hotel_weekend_feature_table = fe.create_table(
    name='ml.default.hotel_weekend_features',   # Unity Catalog path
    primary_keys=['date'],
    df=hotel_weekend_feature_df,
    description='Hotel is_weekend features table'
)
```

The primary key column (`'date'`) is used as the `lookup_key` when configuring the AutoML experiment. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Configuring `feature_store_lookups`

Build a list of dictionaries, each specifying the table name and lookup key: ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

```python
feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}
feature_lookups = [feature_lookup]   # can contain multiple lookups
```

The `lookup_key` must match the primary key column defined in the feature table and also exist in the primary training dataset. The lookup values can be a single column name or a list of columns for composite keys. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Running the AutoML Experiment

Pass the `feature_store_lookups` list to the `automl.forecast()` function (or other AutoML functions that support it): ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

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

During the experiment, AutoML joins the feature tables with the primary dataset using the lookup keys, making the covariate columns available to all trained models. No additional configuration (such as specifying which columns to use) is needed—AutoML automatically selects the best features from the joined data. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Best Practices

- **Use a single source of time columns.** Ensure that the date/time column in both the primary dataset and the feature table have the same type and granularity (e.g., daily, hourly).
- **Include only relevant covariates.** Feature selection is handled by AutoML, but adding many unrelated feature tables may increase experiment runtime.
- **Ownership and permissions.** You must have write access to the Unity Catalog schema where the feature table resides, and the AutoML experiment runner must have read access to that table.

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) – The main AutoML workflow for time series prediction.
- [Feature Store](/concepts/feature-store.md) – Central repository for feature tables used in machine learning.
- [Covariates in Forecasting](/concepts/covariates-in-time-series-forecasting.md) – External regressors that improve model accuracy.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer for data and AI assets.
- Automated Machine Learning (AutoML) – Overview of Databricks AutoML capabilities.

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
