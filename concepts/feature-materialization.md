---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 11d12077630c56142f232f58f5e4a1d53fd8f066fe6331bddcdc837db1abcb9e
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-materialization
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Feature Materialization
description: The process of persisting computed features to offline or online stores for efficient reuse in training and serving
tags:
  - feature-engineering
  - serving
  - mlops
timestamp: "2026-06-19T18:18:03.426Z"
---

```yaml
---
title: Feature Materialization
summary: The process of computing and persisting declaratively defined features to offline or online stores for efficient reuse in model training and real‑time serving.
sources:
  - declarative-features-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:57:19.449Z"
updatedAt: "2026-06-19T09:57:19.449Z"
tags:
  - feature-engineering
  - ml-serving
  - databricks
aliases:
  - feature-materialization
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Feature Materialization

**Feature Materialization** is the process of computing and persisting declaratively defined features to offline or online storage for efficient reuse in model training and real‑time serving. After defining features with `create_feature` or retrieving them with `get_feature`, you can call `materialize_features` to pre‑compute the feature values and store them in a materialized view. This avoids recomputing features on demand and enables low‑latency serving.^[declarative-features-databricks-on-aws.md]

## Workflow

### Prerequisites
Before calling `materialize_features`, features must be registered in [[Unity Catalog]]. Features defined locally using the `Feature` class must first be persisted using `register_feature` or `create_feature`.^[declarative-features-databricks-on-aws.md]

### Configuration
The `materialize_features` API accepts store configurations that determine where the features are persisted:

```python
from databricks.feature_engineering.entities import (
    CronSchedule, OfflineStoreConfig, OnlineStoreConfig,
    MaterializedFeaturePipelineScheduleState, TableTrigger
)

online_config = OnlineStoreConfig(
    catalog_name="main",
    schema_name="feature_store",
    table_name_prefix="customer_features_serving",
    online_store_name="customer_features_store",
)
```
^[declarative-features-databricks-on-aws.md]

### Materializing Aggregation Features
Aggregation features (using functions such as `Sum`, `Avg`, or `Count` with time windows) support both offline and online store configurations. They require a `CronSchedule` trigger to define the materialization cadence:

```python
fe.materialize_features(
    features=[avg_feature, sum_feature],
    offline_config=OfflineStoreConfig(
        catalog_name="main",
        schema_name="feature_store",
        table_name_prefix="customer_features",
    ),
    online_config=online_config,
    trigger=CronSchedule(
        quartz_cron_expression="0 0 * * * ?",  # Hourly
        timezone_id="UTC",
        pipeline_schedule_state=MaterializedFeaturePipelineScheduleState.ACTIVE,
    ),
)
```
^[declarative-features-databricks-on-aws.md]

### Materializing Column Selection Features
Column selection features (created with the `ColumnSelection` function) use a `TableTrigger` instead of a `CronSchedule`. These features support only online store configuration:

```python
fe.materialize_features(
    features=[latest_amount],
    online_config=online_config,
    trigger=TableTrigger(),
)
```
^[declarative-features-databricks-on-aws.md]

## Store Types

### Offline Store
The offline store persists computed features to [[Delta Lake Table|Delta tables]] in Unity Catalog for batch use cases such as training dataset preparation. After materialization, you can use `create_training_set` with the materialized view to prepare an offline batch training dataset.^[declarative-features-databricks-on-aws.md]

### Online Store
The online store persists features for low‑latency serving applications. Features are stored in a dedicated online store (for example, a key‑value store) for real‑time inference. After materializing features, you can serve models using CPU model serving.^[declarative-features-databricks-on-aws.md]

## Triggers

Materialization can be triggered in two ways:

| Trigger Type | Description | Used With |
|---|---|---|
| `CronSchedule` | Scheduled pipeline based on a Quartz cron expression | Aggregation features (Sum, Avg, Count, etc.) |
| `TableTrigger` | Triggered when the source table is updated | Column selection features |

The `CronSchedule` includes a `pipeline_schedule_state` parameter that can be set to `ACTIVE` or `PAUSED` to control whether the scheduled pipeline runs.^[declarative-features-databricks-on-aws.md]

## Best Practices

- **Group features from the same data source** in a single `materialize_features` call to minimize data scans and reduce compute costs.^[declarative-features-databricks-on-aws.md]
- **Use consistent granularity** (for example, all 1‑hour or all 1‑day slide durations) for features on the same data source. This enables better grouping during materialization and improves pipeline efficiency.^[declarative-features-databricks-on-aws.md]

## Limitations

For materialization‑specific limitations, see the [materialized features documentation](https://docs.databricks.com/aws/en/machine-learning/feature-store/materialized-features#limitations).^[declarative-features-databricks-on-aws.md]

## Related Concepts

- [[Declarative Feature Engineering APIs]] — APIs for defining and computing features
- [[Feature Store]] — Central repository for feature definitions and values
- Model Training with Declarative Features — Using materialized features for training
- [[Online Feature Serving]] — Serving pre‑computed features for real‑time inference
- [[Unity Catalog]] — Governance and storage layer for feature metadata

## Sources

- declarative-features-databricks-on-aws.md
```

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
