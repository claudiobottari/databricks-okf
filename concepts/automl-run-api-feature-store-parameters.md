---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a01b22a23a4e921e45ff305cf4d7d2cfc790d0c0fa0832fe071d9ce1a644559b
  pageDirectory: concepts
  sources:
    - automl-feature-store-integration-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-run-api-feature-store-parameters
    - ARAFSP
    - automl-api-feature_store_lookups-parameter
    - AAFP
  citations:
    - file: automl-feature-store-integration-databricks-on-aws.md
title: AutoML Run API Feature Store Parameters
description: The feature_store_lookups parameter in the AutoML run specification API that enables programmatic feature table joins
tags:
  - automl
  - api
  - feature-store
  - databricks
timestamp: "2026-06-19T22:11:21.892Z"
---

# AutoML Run API Feature Store Parameters

**AutoML Run API Feature Store Parameters** refer to the configuration options available when using the AutoML API to join feature tables from Unity Catalog or the legacy Workspace Feature Store to your training dataset. These parameters are specified through the `feature_store_lookups` argument in the AutoML run specification.

## Overview

When running AutoML experiments via the API, you can augment the original input dataset with features from existing feature tables. This integration allows AutoML to leverage pre-computed features stored in [Feature Store in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) or the [Legacy Workspace Feature Store](/concepts/legacy-workspace-feature-store.md), potentially improving model performance without requiring manual feature engineering. ^[automl-feature-store-integration-databricks-on-aws.md]

## Requirements

- Classification and regression experiments require Databricks Runtime 11.3 LTS ML and above.
- Forecasting experiments require Databricks Runtime 12.2 LTS ML and above.

^[automl-feature-store-integration-databricks-on-aws.md]

## The `feature_store_lookups` Parameter

The `feature_store_lookups` parameter accepts a list of dictionaries, where each dictionary defines a feature table to join and the corresponding lookup keys. ^[automl-feature-store-integration-databricks-on-aws.md]

### Parameter Structure

Each dictionary in the `feature_store_lookups` list contains the following fields:

| Field | Description |
|-------|-------------|
| `table_name` | The name of the feature table in Unity Catalog or the legacy Workspace Feature Store |
| `lookup_key` | A list of column names from the training dataset used to look up features from the feature table |

^[automl-feature-store-integration-databricks-on-aws.md]

### Example

```python
feature_store_lookups = [
  {
     "table_name": "example.trip_pickup_features",
     "lookup_key": ["pickup_zip", "rounded_pickup_datetime"],
  },
  {
      "table_name": "example.trip_dropoff_features",
     "lookup_key": ["dropoff_zip", "rounded_dropoff_datetime"],
  }
]
```

^[automl-feature-store-integration-databricks-on-aws.md]

## Lookup Key Configuration

For each feature table, you must specify the corresponding lookup key columns from your training dataset. The lookup key acts as the join condition between the training data and the feature table. ^[automl-feature-store-integration-databricks-on-aws.md]

### Standard Feature Tables

For standard (non-time-series) feature tables, the `lookup_key` should contain the primary key columns of the feature table. Each primary key must have a corresponding column in the training dataset. ^[automl-feature-store-integration-databricks-on-aws.md]

### Time Series Feature Tables

For [Time Series Feature Tables](/concepts/time-series-feature-tables.md), you must also provide a timestamp lookup key. The timestamp lookup key should be a column in the training dataset that corresponds to the timestamp column in the feature table. This enables AutoML to perform point-in-time lookups for time-dependent features. ^[automl-feature-store-integration-databricks-on-aws.md]

## Multiple Feature Tables

You can join multiple feature tables to your training dataset by adding multiple dictionaries to the `feature_store_lookups` list. Each feature table is joined independently using its specified lookup keys. ^[automl-feature-store-integration-databricks-on-aws.md]

## Related Concepts

- [AutoML API](/concepts/automl-python-api.md) — The programmatic interface for configuring and running AutoML experiments
- [Feature Store in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) — The Unity Catalog-based feature store for managing and serving features
- [Legacy Workspace Feature Store](/concepts/legacy-workspace-feature-store.md) — The original workspace-level feature store
- [AutoML Experiment Configuration](/concepts/automl-experiment-configuration.md) — Complete configuration options for AutoML runs
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The broader practice of creating features for machine learning

## Sources

- automl-feature-store-integration-databricks-on-aws.md

# Citations

1. [automl-feature-store-integration-databricks-on-aws.md](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
