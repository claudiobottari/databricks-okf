---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c001d7b0ef39d38383aff34545e9a568ec28edc78c65acda9b7419424e0cd112
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - featureengineeringclient-python-api
    - FPA
    - Feature Engineering Python API
    - Feature Engineering Python API Reference
    - Feature Engineering Python API reference
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
title: FeatureEngineeringClient Python API
description: A Python client API (`FeatureEngineeringClient`) for creating, reading, updating, and managing feature tables in Unity Catalog, pre-installed in Databricks Runtime ML editions.
tags:
  - api
  - python
  - feature-store
timestamp: "2026-06-19T18:48:49.618Z"
---

# FeatureEngineeringClient Python API

The **FeatureEngineeringClient** is the Python client for managing [Feature Engineering](/concepts/feature-tables-in-unity-catalog.md) on Databricks. It is part of the `databricks-feature-engineering` package and provides methods to create, read, update, delete, and tag feature tables, as well as to write training sets and perform batch scoring. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Installation

The `databricks-feature-engineering` package is available on PyPI and is pre-installed in Databricks Runtime 13.3 LTS ML and above. For non-ML Databricks Runtimes, you must install it manually. Use the [compatibility matrix](https://docs.databricks.com/aws/en/release-notes/runtime/#feature-engineering-compatibility-matrix) to select the correct version for your Databricks Runtime. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

```python
%pip install databricks-feature-engineering
dbutils.library.restartPython()
```

## Requirements

- Workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md) with [Privilege Model Version 1.0](https://docs.databricks.com/aws/en/archive/unity-catalog/upgrade-privilege-model). ^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- Databricks Runtime 13.2 or above. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Core Methods

All methods are called on an instance of `FeatureEngineeringClient`:

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()
```

The following table summarizes the primary methods described in the official API documentation. Source references for each method are found in the source material.

| Method | Description |
|--------|-------------|
| `create_table()` | Creates a new feature table in Unity Catalog (with primary key and optional time series, tags). |
| `write_table()` | Writes data to a feature table; supports `mode='merge'` for upserts and streaming DataFrames. |
| `read_table()` | Reads a feature table as a Spark DataFrame. |
| `get_table()` | Returns metadata of a feature table (including list of features). |
| `set_feature_table_tag()` | Sets (upserts) a tag on a feature table. |
| `delete_feature_table_tag()` | Deletes a tag from a feature table. |
| `drop_table()` | Deletes a feature table and its underlying Delta table. |

For full parameter details, see the [Feature Engineering Python API reference](https://api-docs.databricks.com/python/feature-engineering/latest/index.html). ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Usage Examples

All examples below assume a `FeatureEngineeringClient` instance has been created as shown above.

### Create a feature table

Create a feature table in Unity Catalog by calling `create_table()` with a schema and a primary key constraint.

```python
fe.create_table(
    name="ml.recommender_system.customer_features",
    df=customer_features_df,
    primary_key="customer_id",
    description="Customer features for recommender system",
    tags={"team": "recommender", "project": "v2"}
)
```

For a time series feature table, specify the time column as part of the primary key and pass `timeseries_columns` or define it in the Delta table’s DDL. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Write (update) a feature table

Use `write_table()` to add new rows or merge updates based on the primary key. The default mode is `"merge"`, which updates existing rows and inserts new ones. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

```python
fe.write_table(
    name='ml.recommender_system.customer_features',
    df=customer_features_df,
    mode='merge'
)
```

For streaming updates, pass a streaming `DataFrame` to `write_table`. It returns a `StreamingQuery` object. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Read a feature table

```python
customer_features_df = fe.read_table(
    name='ml.recommender_system.customer_features'
)
```

### Get feature table metadata

```python
ft = fe.get_table(name="ml.recommender_system.customer_features")
print(ft.features)  # prints list of feature names and types
```

### Manage tags

```python
# Upsert a tag
fe.set_feature_table_tag(
    name="customer_feature_table",
    key="tag_key_1",
    value="new_key_value"
)

# Delete a tag
fe.delete_feature_table_tag(
    name="customer_feature_table",
    key="tag_key_2"
)
```

### Delete a feature table

```python
fe.drop_table(name="ml.recommender_system.customer_features")
```

> **Note**: `drop_table()` is not supported in Databricks Runtime 13.1 ML or below. Use SQL `DROP TABLE` instead. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Working with Existing Delta Tables and Views

Any [Delta table](/concepts/delta-lake-table.md) in Unity Catalog that has a primary key constraint can be used as a feature table without calling `create_table()`. For existing tables that lack a primary key, use `ALTER TABLE` DDL to add the constraint; after that, you can use `FeatureEngineeringClient` methods normally. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

Simple SELECT views (without JOIN, GROUP BY, or DISTINCT) can also be registered as feature tables (requires `databricks-feature-engineering` 0.7.0+ and Databricks Runtime 16.0 ML). Features from view-backed tables cannot be published to online stores. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Additional Operations

- **Training sets**: Use `create_training_set()` (not shown in source) to generate training data with automatic feature lookup.
- **Batch scoring**: Use `score_batch()` for applying features to a scoring DataFrame.

Refer to the official [Feature Engineering Python API reference](https://api-docs.databricks.com/python/feature-engineering/latest/index.html) for the complete list of methods and their signatures.

## Related Concepts

- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta tables](/concepts/delta-lake-table.md)
- [Primary key constraint](/concepts/primary-key-constraint-for-feature-tables.md)
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md)
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md)
- Databricks Runtime

## Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
