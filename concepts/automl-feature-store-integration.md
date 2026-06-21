---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e28b89bb222a7d0eeb7ae1a5b7e3338462b3357cf9cbfb7093fbd61455d06751
  pageDirectory: concepts
  sources:
    - automl-feature-store-integration-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-feature-store-integration
    - AFSI
    - Feature Store Integration
    - Feature Store integration
    - Feature Store Integration with AutoML
    - Feature Store integration for AutoML
  citations:
    - file: automl-feature-store-integration-databricks-on-aws.md
title: AutoML Feature Store Integration
description: How Databricks AutoML can augment input datasets with features from Unity Catalog or legacy Workspace Feature Store tables
tags:
  - automl
  - feature-store
  - databricks
  - machine-learning
timestamp: "2026-06-19T22:11:22.784Z"
---

# AutoML Feature Store Integration

**AutoML Feature Store Integration** allows AutoML to augment the original input dataset with features from existing feature tables. These feature tables can reside in [Unity Catalog](/concepts/unity-catalog.md) or in the legacy [Workspace Feature Store](/concepts/workspace-feature-store-ui.md). By joining pre-computed features during training, you can enrich your training data without manually merging tables. ^[automl-feature-store-integration-databricks-on-aws.md]

## Requirements

- Classification and regression experiments require **Databricks Runtime 11.3 LTS ML** or above. ^[automl-feature-store-integration-databricks-on-aws.md]
- Forecasting experiments require **Databricks Runtime 12.2 LTS ML** or above. ^[automl-feature-store-integration-databricks-on-aws.md]

## Select a Feature Table Using the AutoML UI

After configuring your AutoML experiment, you can add feature tables through the UI. Click **Join features (optional)**, then on the **Join additional features** page select a feature table in the **Feature Table** field. For each **Feature table primary key**, select the corresponding lookup key from the training dataset. For [Time Series Feature Tables](/concepts/time-series-feature-tables.md), also select the corresponding timestamp lookup key. You can add multiple feature tables by clicking **Add another feature table** and repeating these steps. ^[automl-feature-store-integration-databricks-on-aws.md]

## Use Feature Tables with the AutoML API

To use feature tables programmatically, set the `feature_store_lookups` parameter in your AutoML run specification. Each lookup entry specifies the `table_name`, `lookup_key` (the columns used to join), and optionally a timestamp lookup key for time series tables. ^[automl-feature-store-integration-databricks-on-aws.md]

Example Python configuration:

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

Databricks provides a notebook titled **AutoML experiment using feature tables** that demonstrates how to join feature tables to your training dataset for use with AutoML. ^[automl-feature-store-integration-databricks-on-aws.md]

## Related Concepts

- AutoML – Automated machine learning on Databricks
- [Feature Store](/concepts/feature-store.md) – Centralized feature management for ML
- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer for feature tables
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) – Feature tables with temporal keys
- [AutoML API](/concepts/automl-python-api.md) – Programmatic interface for AutoML experiments

## Sources

- automl-feature-store-integration-databricks-on-aws.md

# Citations

1. [automl-feature-store-integration-databricks-on-aws.md](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
