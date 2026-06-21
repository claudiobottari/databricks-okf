---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d719aeb4df6e992c2a0e090f8975c1ee895b20312c1e8666a245180229360a20
  pageDirectory: concepts
  sources:
    - automl-feature-store-integration-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-api-feature_store_lookups-parameter
    - AAFP
  citations:
    - file: automl-feature-store-integration-databricks-on-aws.md
title: AutoML API feature_store_lookups Parameter
description: The feature_store_lookups parameter in the AutoML run specification allows programmatic configuration of feature table joins.
tags:
  - automl
  - api
  - feature-store
timestamp: "2026-06-19T09:06:29.292Z"
---

# AutoML API `feature_store_lookups` Parameter

The **`feature_store_lookups`** parameter is an argument in the [AutoML API](/concepts/automl-python-api.md) that allows you to augment your training dataset with features from existing [Feature Tables](/concepts/feature-tables.md) in [Unity Catalog](/concepts/unity-catalog.md) or the legacy [Workspace Feature Store](/concepts/workspace-feature-store-ui.md). This parameter enables AutoML experiments to leverage pre-computed features without requiring you to manually join them into your input dataset. ^[automl-feature-store-integration-databricks-on-aws.md]

## Overview

When running an AutoML experiment via the API, you can specify one or more feature tables to join with your training data. The `feature_store_lookups` parameter accepts a list of dictionaries, where each dictionary defines a feature table to join and the lookup keys that map columns in your training dataset to the feature table's primary keys. ^[automl-feature-store-integration-databricks-on-aws.md]

## Parameter Structure

Each entry in the `feature_store_lookups` list is a dictionary with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `table_name` | string | The fully qualified name of the feature table (e.g., `"example.trip_pickup_features"`) |
| `lookup_key` | list of strings | The column names in the training dataset that correspond to the feature table's primary keys |

^[automl-feature-store-integration-databricks-on-aws.md]

## Example

The following example demonstrates how to join two feature tables to a training dataset for an AutoML experiment:

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

In this example:
- The first lookup joins the `example.trip_pickup_features` table using the `pickup_zip` and `rounded_pickup_datetime` columns from the training dataset.
- The second lookup joins the `example.trip_dropoff_features` table using the `dropoff_zip` and `rounded_dropoff_datetime` columns.

## Requirements

- **Classification and regression experiments**: Requires Databricks Runtime 11.3 LTS ML and above. ^[automl-feature-store-integration-databricks-on-aws.md]
- **Forecasting experiments**: Requires Databricks Runtime 12.2 LTS ML and above. ^[automl-feature-store-integration-databricks-on-aws.md]

## Time Series Feature Tables

For [Time Series Feature Tables](/concepts/time-series-feature-tables.md), you must also specify a timestamp lookup key in addition to the primary key. The timestamp lookup key should be a column in the training dataset that corresponds to the timestamp column in the feature table. ^[automl-feature-store-integration-databricks-on-aws.md]

## Related Concepts

- [AutoML API](/concepts/automl-python-api.md) — The API for programmatically creating AutoML experiments
- [Feature Store](/concepts/feature-store.md) — Centralized repository for feature tables
- [Unity Catalog](/concepts/unity-catalog.md) — Governance and cataloging system for data assets
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) — Legacy feature store for Databricks workspaces
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) — Feature tables that include timestamp columns for point-in-time lookups
- [AutoML Experiment Configuration](/concepts/automl-experiment-configuration.md) — Complete parameter specification for AutoML runs

## Sources

- automl-feature-store-integration-databricks-on-aws.md

# Citations

1. [automl-feature-store-integration-databricks-on-aws.md](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
