---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38feabd473b9a2f47da43b554e90873fb48fc4df6eaa8e02fd13c07b1cedf157
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-engineering-python-api-featureengineeringclient
    - FEPA(
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
title: Feature Engineering Python API (FeatureEngineeringClient)
description: The Python client library (databricks-feature-engineering) providing methods like write_table, read_table, get_table, create_table, drop_table, and tag management for interacting with feature tables in Unity Catalog.
tags:
  - python-api
  - feature-engineering
  - databricks
timestamp: "2026-06-19T10:30:42.273Z"
---

# Feature Engineering Python API (FeatureEngineeringClient)

The **Feature Engineering Python API (`FeatureEngineeringClient`)** is a Python client for interacting with [Feature Tables](/concepts/feature-tables.md) in [Unity Catalog](/concepts/unity-catalog.md). It provides methods for creating, reading, updating, and deleting feature tables, as well as managing feature table tags and preparing training and inference datasets.

## Overview

The `FeatureEngineeringClient` class is part of the `databricks-feature-engineering` Python package. It enables programmatic access to feature tables stored in Unity Catalog, allowing data scientists and engineers to manage the complete lifecycle of features used in machine learning workflows. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Installation

The `databricks-feature-engineering` package is pre-installed in Databricks Runtime 13.3 LTS ML and above. For non-ML Databricks Runtime versions, manual installation is required. Use the compatibility matrix to find the correct package version for your Databricks Runtime version. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

```python
%pip install databricks-feature-engineering
dbutils.library.restartPython()
```

## Initialization

Create an instance of the client to interact with feature tables:

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()
```

## Core Operations

### Writing to Feature Tables

Use `write_table` to write or merge data into a feature table. The method supports batch and streaming DataFrames.

```python
fe.write_table(
    name='ml.recommender_system.customer_features',
    df=customer_features_df,
    mode='merge'
)
```

The `mode` parameter controls how data is written. Use `'merge'` to update only specific rows based on the primary key while leaving non-matching rows unchanged. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

When using a streaming DataFrame, `write_table` returns a `StreamingQuery` object, enabling streaming feature computation pipelines. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Reading from Feature Tables

Read feature values using `read_table`:

```python
customer_features_df = fe.read_table(
    name='ml.recommender_system.customer_features'
)
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Retrieving Feature Table Metadata

Use `get_table` to fetch metadata about a feature table, including its features:

```python
ft = fe.get_table(name="ml.recommender_system.user_feature_table")
print(ft.features)
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Tag Management

The API provides methods for managing tags on feature tables. Tags are key-value pairs used to categorize and organize feature tables and features.

### Creating Tags

Tags can be set during table creation:

```python
customer_feature_table = fe.create_table(
    # ... other parameters
    tags={"tag_key_1": "tag_value_1", "tag_key_2": "tag_value_2"}
)
```

### Upserting and Deleting Tags

```python
# Update or create a tag
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

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Deleting Feature Tables

Delete a feature table using `drop_table`. This operation also drops the underlying Delta table in Unity Catalog.

```python
fe.drop_table(name="ml.recommender_system.customer_features")
```

Note that `drop_table` is not supported in Databricks Runtime 13.1 ML or below; use SQL commands instead. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Requirements

- Databricks Runtime 13.2 or above for Unity Catalog feature tables
- Unity Catalog [Metastore](/concepts/metastore.md) with Privilege Model Version 1.0
- Appropriate permissions on catalogs, schemas, and tables ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) — The underlying data structure for feature management
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for managing data assets
- [Primary Key Constraints](/concepts/primary-key-constraints-for-feature-tables.md) — Required for feature tables
- [Delta Tables](/concepts/delta-lake-table.md) — The storage format for feature tables
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) — Feature tables with time-based primary keys
- [Feature Engineering API Reference](/concepts/featureengineeringclient-api.md) — Full API documentation

## Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
