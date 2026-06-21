---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 93b27dc56e5fb4941eb37c25d309f497e5941deb0cf5729f1895e019b9e4c373
  pageDirectory: concepts
  sources:
    - automl-feature-store-integration-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store-lookup-keys
    - FSLK
    - Feature Store Lookup
  citations:
    - file: automl-feature-store-integration-databricks-on-aws.md
      start: 7
      end: 9
    - file: automl-feature-store-integration-databricks-on-aws.md
      start: 11
      end: 14
    - file: automl-feature-store-integration-databricks-on-aws.md
      start: 16
      end: 39
    - file: automl-feature-store-integration-databricks-on-aws.md
      start: 41
      end: 51
title: Feature Store Lookup Keys
description: The mechanism for joining feature tables to training datasets by mapping feature table primary keys to columns in the training dataset
tags:
  - feature-store
  - data-joining
  - automl
timestamp: "2026-06-19T22:11:03.810Z"
---

```yaml
---
title: Feature Store Lookup Keys
summary: Columns in a training dataset that map to the primary keys of a feature table, enabling AutoML to join additional features during an experiment.
sources:
  - automl-feature-store-integration-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:30:03.502Z"
updatedAt: "2026-06-18T14:30:03.502Z"
tags:
  - machine-learning
  - feature-store
  - automl
aliases:
  - feature-store-lookup-keys
  - FSLK
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Feature Store Lookup Keys

**Feature Store Lookup Keys** are columns in a training dataset that correspond to the primary keys of a [[Feature Store]] feature table. AutoML uses these lookup keys to join additional features from the specified feature table into the original input dataset during an experiment. ^[automl-feature-store-integration-databricks-on-aws.md#L7-L9]

## Requirements

- Classification and regression experiments: Databricks Runtime 11.3 LTS ML and above.
- Forecasting experiments: Databricks Runtime 12.2 LTS ML and above.

The training dataset must contain columns with names and types that exactly match the lookup keys expected by the selected feature tables. ^[automl-feature-store-integration-databricks-on-aws.md#L11-L14]

## Configuring Lookup Keys in the AutoML UI

To join feature tables using the AutoML UI:

1. After configuring the experiment, click **Join features (optional)**.
2. On the **Join additional features** page, select a feature table from the **Feature Table** field.
3. For each **Feature table primary key**, select the corresponding lookup key from a dropdown that lists columns in the training dataset.
4. For [[time series feature tables]], select the corresponding **timestamp lookup key** from a similar dropdown. This timestamp key must be a column in the training dataset that maps to the timestamp column of the time series feature table.
5. To add more feature tables, click **Add another feature table** and repeat. ^[automl-feature-store-integration-databricks-on-aws.md#L16-L39]

## Configuring Lookup Keys in the AutoML API

Use the `feature_store_lookups` parameter in the AutoML run specification. Each entry is a dictionary with a `table_name` and a `lookup_key` list. For time series feature tables, include a `timestamp_lookup_key` field.

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

^[automl-feature-store-integration-databricks-on-aws.md#L41-L51]

## Related Concepts

- AutoML – Automated machine learning on Databricks
- [[Feature Store]] – Central repository for curated features
- [[Time Series Feature Tables]] – Feature tables with a temporal dimension requiring timestamp lookup keys
- [[Unity Catalog]] – Governance layer for feature tables
- [[Workspace Feature Store UI|Workspace Feature Store]] – Legacy feature store within a workspace

## Sources

- automl-feature-store-integration-databricks-on-aws.md
```

# Citations

1. [automl-feature-store-integration-databricks-on-aws.md:7-9](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
2. [automl-feature-store-integration-databricks-on-aws.md:11-14](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
3. [automl-feature-store-integration-databricks-on-aws.md:16-39](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
4. [automl-feature-store-integration-databricks-on-aws.md:41-51](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
