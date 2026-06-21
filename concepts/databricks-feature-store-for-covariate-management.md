---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7c384e969b4ae9da9757ad9922cc933393df4ecb73797000c73f950bb9cb886b
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-feature-store-for-covariate-management
    - DFSFCM
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: Databricks Feature Store for Covariate Management
description: Using the Databricks Feature Store to store, version, and serve covariate feature tables for AutoML forecasting
tags:
  - databricks
  - feature-store
  - mlops
timestamp: "2026-06-19T09:06:53.538Z"
---

# Databricks Feature Store for Covariate Management

**Databricks Feature Store for Covariate Management** refers to the practice of using the [Feature Store](/concepts/feature-store.md) (now part of the Feature Engineering client) to store and serve covariate variables—also called external regressors—that improve the accuracy of [AutoML Forecasting](/concepts/automl-forecast.md) models. Covariates are additional time-dependent variables outside the target time series that can capture external influences, such as day-of-week effects, holidays, or weather data. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Overview

Covariate management via the Feature Store decouples feature engineering from model training. Feature-engineering logic (for example, computing `is_weekend` from a date column) is executed once and stored as a feature table in [Unity Catalog](/concepts/unity-catalog.md). The same table can then be looked up by multiple forecasting experiments, ensuring consistency and reusability. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

The primary API for creating and managing such tables is the `FeatureEngineeringClient` (formerly `FeatureStoreClient`). Tables must declare a primary key (typically the time column) so that AutoML can join them with the training data at experiment time. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## How It Works

1. **Create the time-series dataset** – Prepare a DataFrame containing at least a time column and the target column (e.g., `occupancy_rate`).
2. **Engineer covariates** – Compute additional features that depend only on the time column (e.g., day of week, holiday flag). The resulting DataFrame must contain the same time column as a primary key.
3. **Store the covariates in a Feature Store table** – Use `FeatureEngineeringClient.create_table()` (or SQL / Delta Live Tables) with the primary key set to the time column. The table can be stored in any Unity Catalog location.
4. **Pass the feature table as a lookup to AutoML** – In the `automl.forecast()` call, provide the `feature_store_lookups` parameter. Each lookup is a dictionary with `table_name` and `lookup_key` (a list of columns that match the primary key of the feature table).
5. **AutoML joins the covariates automatically** – During the experiment, AutoML retrieves the covariate values by joining the training data with the feature table on the specified lookup keys. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Example (abbreviated)

The following snippet shows the core steps for creating a weekend feature table and using it as a covariate in an AutoML forecasting experiment: ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient
from databricks import automl

# Step 2: Feature engineering
def compute_hotel_weekend_features(df):
    return df.select("date").withColumn(
        "is_weekend",
        when(dayofweek("date").isin(1,2,3,4,5), 0)
        .when(dayofweek("date").isin(6,7), 1)
    )

hotel_weekend_feature_df = compute_hotel_weekend_features(df)

# Step 3: Store in Feature Store
fe = FeatureEngineeringClient()
hotel_weekend_feature_table = fe.create_table(
    name='ml.default.hotel_weekend_features',
    primary_keys=['date'],
    df=hotel_weekend_feature_df,
    description='Hotel is_weekend features table'
)

# Step 4: Configure lookup
feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}

# Step 5: Run AutoML with covariates
summary = automl.forecast(
    dataset=df,
    target_col="occupancy_rate",
    time_col="date",
    frequency="d",
    horizon=1,
    feature_store_lookups=[feature_lookup]
)
```

## Multiple Covariate Tables

The `feature_store_lookups` parameter accepts a list of lookup dictionaries, allowing you to provide several covariate tables to a single AutoML experiment. This is useful when different feature sets are maintained independently (e.g., one table for calendar features and another for weather features). ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Alternative Creation Methods

While the Python `FeatureEngineeringClient` is demonstrated in the example, feature tables can also be created using SQL (e.g., `CREATE TABLE ... USING DELTA`) or Delta Live Tables pipelines. The Feature Store in Unity Catalog supports these methods as well. See the documentation on [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) for more options. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Benefits

- **Reusability** – Covariate tables can be shared across multiple forecasting experiments without recomputation.
- **Consistency** – The same feature logic is applied to training and serving data.
- **Governance** – Feature tables stored in Unity Catalog benefit from its access control, lineage, and discovery features.

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) – The primary consumer of covariate lookups.
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) – The Python API for managing feature tables.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer where feature tables reside.
- [Feature Store in Databricks](/concepts/online-feature-store-databricks.md) – Broader concept of feature management.
- Covariate Selection – Best practices for choosing external regressors.

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
