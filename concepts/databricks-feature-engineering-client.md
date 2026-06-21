---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 288797655b7d1c07298905b9a3464ce090419cab938eaeb96cce29f92ec6fd26
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-feature-engineering-client
    - DFEC
    - Databricks Feature Engineering
    - Databricks Feature Engineering Library
    - databricks-feature-engineering
    - databricks-feature-engineering library
    - Databricks Feature Engineering Client (databricks-feature-engineering)
    - databricks-feature-engineering-python-api
    - DFEPA
    - databricks-feature-engineering-python-client
    - DFEPC
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: Databricks Feature Engineering Client
description: Python API (FeatureEngineeringClient) for creating, managing, and storing feature tables in Unity Catalog for use in machine learning workflows.
tags:
  - databricks
  - feature-store
  - api
timestamp: "2026-06-19T22:12:06.313Z"
---

---
title: Databricks Feature Engineering Client
summary: The Python FeatureEngineeringClient API for creating and managing feature tables in Unity Catalog for use in machine learning workflows.
sources:
  - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:07:25.708Z"
updatedAt: "2026-06-19T14:07:25.708Z"
tags:
  - databricks
  - feature-store
  - python-api
  - mlops
aliases:
  - databricks-feature-engineering-client
  - DFEC
confidence: 0.85
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks Feature Engineering Client

The **Databricks Feature Engineering Client** is a Python library that provides programmatic access to create, manage, and use feature tables in the [Databricks Feature Store](/concepts/databricks-feature-store.md). It enables data scientists and engineers to register feature computations, store them in a centralized feature store, and use them for both training and inference workflows, including integration with AutoML. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Overview

The `FeatureEngineeringClient` (`databricks.feature_engineering.FeatureEngineeringClient`) allows users to create feature tables stored in [Unity Catalog](/concepts/unity-catalog.md) and use them as [covariates](/concepts/covariates-external-regressors-for-forecasting.md) (external regressors) in forecasting models. This enables the reuse of feature computations across different models and ensures consistency between training and serving. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Key Operations

### Creating Feature Tables

The primary operation for registering features is `create_table()`, which takes a DataFrame with computed features, specifies a table name and primary keys, and stores the data as a feature table in Unity Catalog. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

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

The `name` parameter specifies the fully qualified Unity Catalog table name (three-level namespace), `primary_keys` identifies the columns that uniquely identify each row, and `df` is the DataFrame containing the computed features. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Using Feature Tables with AutoML

Feature tables created with the client can be passed to AutoML forecasting experiments using the `feature_store_lookups` parameter. Each lookup specifies a `table_name` and `lookup_key` — the columns used to join the feature table with the primary training data. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

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
    feature_store_lookups=feature_lookups
)
```

Multiple feature tables can be provided in the `feature_store_lookups` list, allowing AutoML to join several covariate sources with the training data automatically. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Use Cases

### Feature Engineering with Covariates

Covariates are additional variables outside the target time series that can improve forecasting model accuracy. For example, when forecasting hotel occupancy rates, a binary `is_weekend` feature — computed from the date column — can help the model capture weekly patterns. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Feature Computation Functions

Best practice is to encapsulate feature logic in reusable functions that return DataFrames with the primary key and feature columns: ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

```python
from pyspark.sql.functions import dayofweek, when

def compute_hotel_weekend_features(df):
    """is_weekend feature computation code"""
    return df.select("date").withColumn(
        "is_weekend",
        when(dayofweek("date").isin(1, 2, 3, 4, 5), 0)  # Weekday
        .when(dayofweek("date").isin(6, 7), 1)  # Weekend
    )
```

## Alternative Approaches

While the Python `FeatureEngineeringClient` is shown in examples, users can also write and create feature tables using **SQL** or **Delta Live Tables**. See [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) for more options. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) — Using feature store tables as covariates in automated forecasting
- [Unity Catalog Feature Tables](/concepts/unity-catalog-feature-tables.md) — Storage and governance for feature tables
- [Feature Store](/concepts/feature-store.md) — Centralized repository for machine learning features
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — Process of creating features from raw data
- [Covariates](/concepts/covariates-external-regressors-for-forecasting.md) — External regressors that improve time series forecasts

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
