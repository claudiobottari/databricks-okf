---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eb57c49fc20ebe9f1f346165e4e37b0f37f9241797300e70cc0b5111c4700e9d
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - featureengineeringclient-api
    - Feature Engineering Client
    - Feature Engineering Client API
    - Feature Engineering client
    - Feature EngineeringClient
    - FeatureEngineeringClient
    - Feature Engineering
    - Feature Engineering API Reference
    - Feature engineering
    - feature engineering
  citations:
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: FeatureEngineeringClient API
description: The Python client class for creating, writing, and managing Feature Store tables in Databricks
tags:
  - databricks
  - api
  - python
timestamp: "2026-06-19T09:06:56.947Z"
---

# FeatureEngineeringClient API

The **FeatureEngineeringClient API** is a Python API in Databricks that provides programmatic access to the [Feature Engineering](/concepts/featureengineeringclient-api.md) system. It allows users to create, manage, and interact with feature tables stored in [Unity Catalog](/concepts/unity-catalog.md), enabling feature engineering workflows for machine learning pipelines.

## Overview

The `FeatureEngineeringClient` class is the primary interface for working with feature tables programmatically. It supports creating feature tables from DataFrames, managing feature metadata, and integrating with other Databricks ML tools like AutoML. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Key Methods

### `create_table()`

The `create_table()` method creates a new feature table in Unity Catalog from a Spark DataFrame. It requires specifying the table name, primary keys, and the DataFrame containing the feature data.

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

**Parameters:**
- `name` (str): The fully qualified name of the feature table in Unity Catalog (format: `catalog.schema.table_name`).
- `primary_keys` (list): A list of column names that serve as the primary key for the feature table.
- `df` (DataFrame): The Spark DataFrame containing the feature data to be stored.
- `description` (str, optional): A human-readable description of the feature table.

## Usage with AutoML

The FeatureEngineeringClient API integrates with AutoML to provide covariates (external regressors) for forecasting models. Feature tables created with the API can be passed to AutoML experiments using the `feature_store_lookups` parameter. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Feature Store Lookups

To use feature tables as covariates in AutoML, create a lookup dictionary specifying the table name and lookup keys:

```python
hotel_weekend_feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}

feature_lookups = [hotel_weekend_feature_lookup]
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

Multiple feature table lookups can be included in a single list, allowing AutoML to join multiple covariate tables with the primary training data. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Alternative Approaches

While the Python `FeatureEngineeringClient` is the primary API for creating and writing feature tables, users can also use SQL or Delta Live Tables to create and manage feature tables in Unity Catalog. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The broader workflow of creating and managing features for machine learning.
- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) — Documentation on managing feature tables using SQL and Delta Live Tables.
- AutoML — Automated machine learning that can consume feature tables as covariates.
- [Covariates in Forecasting](/concepts/covariates-in-time-series-forecasting.md) — Using external regressors to improve time series forecasting models.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance and metadata layer for Databricks assets.

## Sources

- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
