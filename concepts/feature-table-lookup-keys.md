---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4e5839d382c92c257271841bb44e6488bf224032e79478721401e8ecf4f03e44
  pageDirectory: concepts
  sources:
    - automl-feature-store-integration-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-table-lookup-keys
    - FTLK
  citations:
    - file: automl-feature-store-integration-databricks-on-aws.md
title: Feature Table Lookup Keys
description: Mechanism for joining feature tables to AutoML training datasets by mapping primary keys from feature tables to corresponding lookup key columns in the training data.
tags:
  - feature-store
  - data-joining
  - automl
timestamp: "2026-06-19T14:06:29.996Z"
---

# Feature Table Lookup Keys

**Feature Table Lookup Keys** are the columns in a training dataset that correspond to the primary keys of a feature table in [Unity Catalog](/concepts/unity-catalog.md) or the [Legacy Workspace Feature Store](/concepts/legacy-workspace-feature-store.md). When joining a feature table to a training dataset for an AutoML experiment, the lookup keys map the feature table’s primary keys to the equivalent columns in the input data, enabling automatic feature augmentation.^[automl-feature-store-integration-databricks-on-aws.md]

## Overview

During an AutoML experiment, you can optionally join one or more feature tables to the original input dataset. For each feature table, you must specify a lookup key for each primary key defined in that feature table. The lookup key must be a column that exists in the training dataset you provided for the experiment. This mechanism allows AutoML to enrich the training data with precomputed features without manual SQL joins.^[automl-feature-store-integration-databricks-on-aws.md]

## Timestamp Lookup Keys

For [Time Series Feature Tables](/concepts/time-series-feature-tables.md), an additional **timestamp lookup key** is required. This key should correspond to a timestamp column in the training dataset. It enables time-based feature lookups, ensuring that features are retrieved with the correct temporal alignment.^[automl-feature-store-integration-databricks-on-aws.md]

## Selecting Lookup Keys in the AutoML UI

When configuring an AutoML experiment in the Databricks UI:

1. Click **Join features (optional)** to open the **Join additional features** page.
2. In the **Feature Table** field, select a feature table.
3. For each **Feature table primary key**, select the corresponding lookup key from the training dataset columns.
4. For time series feature tables, select the corresponding timestamp lookup key.
5. To add more feature tables, click **Add another feature table** and repeat.

^[automl-feature-store-integration-databricks-on-aws.md]

## Using Lookup Keys with the AutoML API

To specify lookup keys programmatically, set the `feature_store_lookups` parameter in your AutoML run specification. Each entry in the list is a dictionary containing:

| Field | Description |
|-------|-------------|
| `table_name` | Fully qualified name of the feature table (e.g., `example.trip_pickup_features`). |
| `lookup_key` | List of column names from the training dataset that serve as lookup keys for the feature table’s primary keys. |

Example:

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

Note that for time series feature tables, the `lookup_key` must include the timestamp key as part of the list, matching the order of the feature table’s primary keys.^[automl-feature-store-integration-databricks-on-aws.md]

## Requirements

- Classification and regression experiments require Databricks Runtime 11.3 LTS ML and above.
- Forecasting experiments require Databricks Runtime 12.2 LTS ML and above.

^[automl-feature-store-integration-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — Centralized repository for curated features.
- AutoML — Automated machine learning on Databricks.
- [Unity Catalog](/concepts/unity-catalog.md) — Governance and metadata for feature tables.
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) — Feature tables that support temporal lookups.

## Sources

- automl-feature-store-integration-databricks-on-aws.md

# Citations

1. [automl-feature-store-integration-databricks-on-aws.md](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
