---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 47773e27a1ed004ef3a1e25caa4d976f05f2409e6dd28bf632a0d6a355e32b8b
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
    - train-models-with-feature-tables-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - views-as-feature-tables
    - VAFT
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
    - file: train-models-with-feature-tables-databricks-on-aws.md
title: Views as Feature Tables
description: Simple SELECT views over a single Delta table can serve as feature tables for offline training/evaluation but cannot be published to online stores or served.
tags:
  - views
  - feature-store
  - offline-training
timestamp: "2026-06-18T12:19:32.904Z"
---

# Views as Feature Tables

In Unity Catalog, a simple SELECT view can serve as a feature table, allowing you to use subsets of data from an existing Delta table for model training and inference without duplicating the underlying data. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Overview

A view in Unity Catalog that is backed by a single Delta table with a primary key constraint can be used as a feature table in conjunction with [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md). This capability enables you to create a logical subset of features from a larger feature table, filtering or limiting the data while maintaining the same primary key structure. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Requirements

To use a view as a feature table, you must use `databricks-feature-engineering` version 0.7.0 or above, which is built into Databricks Runtime 16.0 ML. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## View Definition Constraints

A simple SELECT view is defined as a view created from a single Delta table in Unity Catalog that can be used as a feature table, and whose primary keys are selected without JOIN, GROUP BY, or DISTINCT clauses. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

Acceptable keywords in the SQL statement are: SELECT, FROM, WHERE, ORDER BY, LIMIT, and OFFSET. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

The view must include the primary key columns from the source table in its SELECT statement. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Creating a View as a Feature Table

The following example creates a view that selects a subset of rows and columns from a larger feature table, including the primary key columns `cid` and `dt`:

```sql
CREATE OR REPLACE VIEW ml.recommender_system.customer_features AS
SELECT cid, dt, pid, rating
FROM ml.recommender_system.customer_table
WHERE rating > 3
```

This view, backed by a single Delta table, can then be used as a feature table in `FeatureEngineeringClient.create_training_set` calls. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Using a View in Training Sets

When creating a training set using a view as a feature table, use `FeatureLookup` with the `timestamp_lookup_key` parameter to specify the time-based key from the view. The following example demonstrates creating a training set from a view where the source table has primary keys `cid` and `dt`, and `dt` is a time series column: ^[train-models-with-feature-tables-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookup

feature_lookups = [
    FeatureLookup(
        table_name='ml.recommender_system.customer_features',
        feature_names=['pid', 'rating'],
        lookup_key=['cid'],
        timestamp_lookup_key='dt'
    ),
]

fe = FeatureEngineeringClient()
training_set = fe.create_training_set(
    df=training_df,
    feature_lookups=feature_lookups,
    label='label'
)
```

## Limitations

Feature tables backed by views have the following limitations: ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

- They do not appear in the Features UI.
- They cannot be published to online stores.
- Features from these tables and models based on these features cannot be served.

## Use Cases

Views as feature tables are useful for: ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

- Offline model training and evaluation
- Creating filtered subsets of features for specific use cases
- Reducing the feature space for particular model training scenarios
- Creating data subsets without duplicating the underlying Delta table

## Related Concepts

- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) — The parent concept for feature tables in Unity Catalog
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) — The Python client for creating and managing feature tables
- [Feature Lookups](/concepts/featurelookup.md) — The mechanism for specifying features from feature tables
- Training Sets — The datasets created from feature lookups
- [Primary Key Constraints](/concepts/primary-key-constraints-for-feature-tables.md) — The constraint required for feature tables

## Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md
- train-models-with-feature-tables-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
2. [train-models-with-feature-tables-databricks-on-aws.md](/references/train-models-with-feature-tables-databricks-on-aws-a4118a38.md)
