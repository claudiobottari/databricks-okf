---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9b0573c33ac9d079d70a127ea71128a04da4ac7ae2cafdc6fea6aa9e738f1488
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-feature-store-for-covariates
    - DFSFC
    - databricks-feature-store-for-covariate-management
    - DFSFCM
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: Databricks Feature Store for Covariates
description: Using Databricks Feature Store (FeatureEngineeringClient) to register covariate feature tables that can be joined with primary training data for AutoML forecasting.
tags:
  - databricks
  - feature-store
  - mlops
timestamp: "2026-06-19T17:38:40.487Z"
---

# Databricks Feature Store for Covariates

**Databricks Feature Store for Covariates** refers to the use of [Feature Store](/concepts/feature-store.md) tables to supply external regressors (covariates) to AutoML forecasting models. Covariates are additional variables outside the target time series that can improve forecast accuracy — for example, a binary `is_weekend` flag when predicting hotel occupancy. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## How It Works

To use covariates with AutoML forecasting, you must store one or more covariate feature tables in a Feature Store and then join them with the primary training data via the `feature_store_lookups` parameter in the AutoML API. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

The typical workflow is:

1. **Create the training data** – a time-series dataset containing the target column and at least a date/time column.
2. **Engineer covariate features** – compute additional columns (e.g., `is_weekend`, holidays, weather data) from the date column or external sources.
3. **Store the covariates in a Feature Store table** – the table must have a primary key (usually the date column) that matches the join key in the training data.
4. **Pass the Feature Store lookups to AutoML** – the `feature_store_lookups` parameter tells AutoML which tables to join and on which keys.
5. **Run the AutoML experiment** – AutoML automatically joins the feature tables during training and inference.

This approach allows AutoML to access rich external signals without requiring you to manually merge tables beforehand. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Creating a Covariate Feature Table

You can create a covariate Feature Store table using the `FeatureEngineeringClient` (Python API), SQL, or Delta Live Tables. The table must define a primary key that matches the join key in your training data. For example, for a hotel occupancy forecast, you could create a table with primary key `date` and a column `is_weekend`: ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

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

## Configuring the AutoML Experiment

When calling `automl.forecast()`, add the `feature_store_lookups` parameter. This parameter is a list of dictionaries, each containing `table_name` (the Unity Catalog path of the feature table) and `lookup_key` (the columns to join on). You can include multiple covariate tables. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

Example:

```python
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

## Benefits

- **Improved forecast accuracy** – external regressors capture patterns not visible in the target series alone.
- **Reusability** – feature tables can be reused across multiple experiments and models.
- **Simplified pipeline** – AutoML handles the join automatically; no manual merging is needed.
- **Multi-table support** – you can supply multiple covariate tables in a single experiment.

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md)
- [Feature Store](/concepts/feature-store.md)
- Covariates (External Regressors)
- [Feature Engineering](/concepts/featureengineeringclient-api.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Time Series Forecasting](/concepts/multi-series-forecasting.md)
- [AutoML Python API Reference](/concepts/automl-python-api.md)

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
