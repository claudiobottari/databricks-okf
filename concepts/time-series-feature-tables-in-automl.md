---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0799e3eb5da4e3c7d42c4532f19f1bab2abe955a01d51d3daa7ceaf98b21efcf
  pageDirectory: concepts
  sources:
    - automl-feature-store-integration-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-series-feature-tables-in-automl
    - TSFTIA
  citations:
    - file: automl-feature-store-integration-databricks-on-aws.md
title: Time Series Feature Tables in AutoML
description: For time series feature tables, AutoML requires a corresponding timestamp lookup key mapped to a timestamp column in the training dataset.
tags:
  - machine-learning
  - automl
  - time-series
  - feature-store
timestamp: "2026-06-19T17:38:22.170Z"
---

# Time Series Feature Tables in AutoML

**Time Series Feature Tables** are a specialized type of feature table in Databricks that contain time-dependent features used for machine learning experiments. When used with AutoML, these tables enable time-aware feature lookups where the feature values are joined to the training data based on both a primary key and a timestamp, ensuring that only features valid at the time of prediction are used.^[automl-feature-store-integration-databricks-on-aws.md]

## Overview

AutoML can augment the original input dataset with features from [Feature Tables](/concepts/feature-tables.md) in [Unity Catalog](/concepts/unity-catalog.md) or from the [Legacy Workspace Feature Store](/concepts/legacy-workspace-feature-store.md). Time series feature tables extend this capability by supporting temporal joins, where the lookup requires both a key column and a timestamp column. This prevents data leakage by ensuring that future feature values are not used to train on past observations.^[automl-feature-store-integration-databricks-on-aws.md]

## Requirements

- **Classification and regression experiments**: Require Databricks Runtime 11.3 LTS ML and above.^[automl-feature-store-integration-databricks-on-aws.md]
- **Forecasting experiments**: Require Databricks Runtime 12.2 LTS ML and above.^[automl-feature-store-integration-databricks-on-aws.md]

## Selecting a Time Series Feature Table in the AutoML UI

After configuring your AutoML experiment, you can join a time series feature table using the following steps:

1. Click **Join features (optional)** to open the feature joining interface.^[automl-feature-store-integration-databricks-on-aws.md]
2. On the **Join additional features** page, select a feature table in the **Feature Table** field.^[automl-feature-store-integration-databricks-on-aws.md]
3. For each **Feature table primary key**, select the corresponding lookup key. The lookup key should be a column in the training dataset you provided for your AutoML experiment.^[automl-feature-store-integration-databricks-on-aws.md]
4. For time series feature tables, select the corresponding **timestamp lookup key**. The timestamp lookup key should be a column in the training dataset you provided for your AutoML experiment, and it determines the temporal alignment between the feature table and the training data.^[automl-feature-store-integration-databricks-on-aws.md]

## Using Time Series Feature Tables with the AutoML API

To use time series feature tables programmatically, set the `feature_store_lookups` parameter in your AutoML Run Specification. Each lookup dictionary can include both key-based and timestamp-based lookup columns. The following example shows a configuration with timestamp-aware lookups:^[automl-feature-store-integration-databricks-on-aws.md]

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

In this example, `rounded_pickup_datetime` and `rounded_dropoff_datetime` function as timestamp lookup keys, ensuring that only feature values from the appropriate time window are joined to each training row.^[automl-feature-store-integration-databricks-on-aws.md]

## How Temporal Lookups Work

When AutoML performs a time series feature lookup, it matches the training data rows to feature values based on both:

- The **primary key** (e.g., `pickup_zip`), which identifies the entity.^[automl-feature-store-integration-databricks-on-aws.md]
- The **timestamp key** (e.g., `rounded_pickup_datetime`), which identifies the point in time.^[automl-feature-store-integration-databricks-on-aws.md]

The Feature Store returns the feature value that was valid at or before the timestamp specified in the lookup key. This temporal alignment is critical for producing realistic models that will perform correctly in production, where future feature values are not available at prediction time.^[automl-feature-store-integration-databricks-on-aws.md]

## Adding Multiple Feature Tables

You can join multiple time series feature tables in a single AutoML experiment. After selecting the first feature table, click **Add another feature table** and repeat the selection and lookup key configuration steps for each additional table.^[automl-feature-store-integration-databricks-on-aws.md]

## Benefits

- **Prevents data leakage**: Temporal lookups ensure that only historically available features are used during training, avoiding the use of future information.^[automl-feature-store-integration-databricks-on-aws.md]
- **Production realism**: The join mechanism mirrors how features will be served in production, where lookups happen at inference time against the current timestamp.^[automl-feature-store-integration-databricks-on-aws.md]
- **Simplified feature engineering**: Time series feature tables allow teams to pre-compute time-dependent features and reuse them across multiple experiments without recomputation.^[automl-feature-store-integration-databricks-on-aws.md]

## Related Concepts

- [Feature Tables](/concepts/feature-tables.md) — The core data structure for storing and serving features
- AutoML — Automated machine learning experiments that can use feature tables
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for managing feature tables
- [Feature Store](/concepts/feature-store.md) — The system for feature storage, discovery, and serving
- [Time Series Features](/concepts/time-series-feature-tables.md) — Feature engineering techniques for temporal data
- [Feature Lookup](/concepts/feature-lookup.md) — The mechanism for joining feature tables to training data
- AutoML Run Specification — The API configuration for AutoML experiments

## Sources

- automl-feature-store-integration-databricks-on-aws.md

# Citations

1. [automl-feature-store-integration-databricks-on-aws.md](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
