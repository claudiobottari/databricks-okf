---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 14aba5a43a1b82c66c7ad90e1fe5c34302b2344c828e09aff8a59b4c6e0f0dd5
  pageDirectory: concepts
  sources:
    - automl-feature-store-integration-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-lookup-keys
    - FLK
    - lookup_key
  citations:
    - file: automl-feature-store-integration-databricks-on-aws.md
title: Feature Lookup Keys
description: When joining a feature table to an AutoML training dataset, each feature table primary key must be mapped to a corresponding lookup key column in the training dataset.
tags:
  - machine-learning
  - automl
  - feature-engineering
timestamp: "2026-06-19T17:38:28.516Z"
---

```markdown
---
title: Feature Lookup Keys
summary: Mechanism for joining feature tables to AutoML training datasets by mapping feature table primary keys to corresponding columns in the training data.
sources:
  - automl-feature-store-integration-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:50:38.647Z"
updatedAt: "2026-06-18T10:50:38.647Z"
tags:
  - feature-store
  - data-engineering
  - automl
aliases:
  - feature-lookup-keys
  - FLK
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Feature Lookup Keys

**Feature lookup keys** are columns in a training dataset that serve as the join keys to retrieve features from a [[Feature Store]] table. When AutoML augments an input dataset with features from feature tables, each feature table’s primary key must be mapped to a lookup key column in the training dataset.^[automl-feature-store-integration-databricks-on-aws.md]

## Role in AutoML experiments

AutoML can enrich a training dataset by joining it with features stored in [[feature tables in Unity Catalog]] or the legacy [[Workspace Feature Store UI|Workspace Feature Store]]. To perform this join, you must specify a lookup key for each feature table: the lookup key is the column in the training dataset that corresponds to the feature table’s primary key. For [[time series feature tables]], an additional timestamp lookup key is required — a column in the training dataset that matches the feature table’s timestamp column.^[automl-feature-store-integration-databricks-on-aws.md]

## Using lookup keys in the AutoML UI

After configuring an AutoML experiment:

1. Click **Join features (optional)**.
2. On the **Join additional features** page, select a feature table.
3. For each **Feature table primary key**, select the corresponding lookup key from the training dataset.
4. For time series feature tables, also select the corresponding **timestamp lookup key**.
5. To add more feature tables, click **Add another feature table** and repeat.^[automl-feature-store-integration-databricks-on-aws.md]

## Using lookup keys in the AutoML API

When using the AutoML run specification, set the `feature_store_lookups` parameter. Each entry is a dictionary containing:

- `"table_name"` – the fully qualified name of the feature table.
- `"lookup_key"` – a list of column names in the training dataset that act as lookup keys.

Example:

```python
feature_store_lookups = [
  {
     "table_name": "example.trip_pickup_features",
     "lookup_key": ["pickup_zip", "rounded_pickup_datetime"]
  },
  {
      "table_name": "example.trip_dropoff_features",
      "lookup_key": ["dropoff_zip", "rounded_dropoff_datetime"]
  }
]
```

^[automl-feature-store-integration-databricks-on-aws.md]

## Requirements

- Classification and regression experiments require Databricks Runtime 11.3 LTS ML and above.
- Forecasting experiments require Databricks Runtime 12.2 LTS ML and above.^[automl-feature-store-integration-databricks-on-aws.md]

## Related concepts

- AutoML — Automated machine learning on Databricks
- [[Feature Store]] — Centralized repository for feature tables
- [[Feature Tables]] — Tables that store curated features
- [[Time Series Feature Tables]] — Feature tables that include timestamp columns for point-in-time joins
- AutoML run specification — API parameters for configuring AutoML experiments

## Sources

- automl-feature-store-integration-databricks-on-aws.md
```

# Citations

1. [automl-feature-store-integration-databricks-on-aws.md](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
