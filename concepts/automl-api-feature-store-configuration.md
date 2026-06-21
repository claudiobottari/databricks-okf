---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2475a42e786995ecce3c401f1a6c2e3488569d226a50ad10223fb95e88bcb25e
  pageDirectory: concepts
  sources:
    - automl-feature-store-integration-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-api-feature-store-configuration
    - AAFSC
  citations:
    - file: automl-feature-store-integration-databricks-on-aws.md
title: AutoML API Feature Store Configuration
description: The AutoML API accepts a `feature_store_lookups` parameter, a list of dictionaries specifying table names and lookup keys to join feature tables to the training dataset.
tags:
  - machine-learning
  - automl
  - api
  - databricks
timestamp: "2026-06-19T17:38:46.871Z"
---

# AutoML API Feature Store Configuration

**AutoML API Feature Store Configuration** allows you to programmatically augment the original input dataset of an AutoML experiment with features from existing feature tables. These feature tables can be stored in [Unity Catalog](/concepts/unity-catalog.md) or in the [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) (legacy). ^[automl-feature-store-integration-databricks-on-aws.md]

## Requirements

- **Classification and regression experiments** require Databricks Runtime 11.3 LTS ML and above. ^[automl-feature-store-integration-databricks-on-aws.md]
- **Forecasting experiments** require Databricks Runtime 12.2 LTS ML and above. ^[automl-feature-store-integration-databricks-on-aws.md]

## API Configuration

To use existing feature tables programmatically, set the `feature_store_lookups` parameter in your AutoML run specification. The parameter accepts a list of dictionaries, each containing the feature table name and the lookup keys to join on. ^[automl-feature-store-integration-databricks-on-aws.md]

### Parameter Structure

Each dictionary in the `feature_store_lookups` list must include: ^[automl-feature-store-integration-databricks-on-aws.md]

- **`table_name`**: The fully qualified name of a feature table (e.g., `"example.trip_pickup_features"`).
- **`lookup_key`**: A list of column names in the training dataset that map to the feature table's primary keys. For [Time Series Feature Tables](/concepts/time-series-feature-tables.md), the lookup key must include the timestamp column.

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

## UI Configuration (Alternative)

After configuring your AutoML experiment in the UI, you can also add feature tables interactively: ^[automl-feature-store-integration-databricks-on-aws.md]

1. Click **Join features (optional)**.
2. On the **Join additional features** page, select a feature table in the **Feature Table** field.
3. For each **Feature table primary key**, select the corresponding lookup key. The lookup key must be a column in the training dataset you provided for the experiment.
4. For time series feature tables, select the corresponding timestamp lookup key. The timestamp lookup key must also be a column in the training dataset.
5. To add more feature tables, click **Add another feature table** and repeat the steps.

## Related Concepts

- [Feature Store](/concepts/feature-store.md) – Central repository for curated features
- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer for data and AI assets
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) – Legacy feature store scoped to a workspace
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) – Feature tables that include a timestamp dimension
- AutoML – Automated machine learning experiments in Databricks
- [AutoML Regression API](/concepts/automl-regress-api.md) – API for running regression experiments with feature store support
- [AutoML Classification API](/concepts/automl-classification-classify.md) – API for running classification experiments with feature store support
- [AutoML Forecasting API](/concepts/automl-forecast-api.md) – API for running forecasting experiments with feature store support

## Sources

- automl-feature-store-integration-databricks-on-aws.md

# Citations

1. [automl-feature-store-integration-databricks-on-aws.md](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
