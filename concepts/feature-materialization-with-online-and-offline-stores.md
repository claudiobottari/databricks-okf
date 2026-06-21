---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55e993f4b4a842c5a538145b5111268e6ca48a23eb3ee43ff63d033d0461364d
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-materialization-with-online-and-offline-stores
    - Offline Stores and Feature Materialization with Online
    - FMWOAOS
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Feature Materialization with Online and Offline Stores
description: The process of persisting computed features to offline stores (for batch training) or online stores (for low-latency serving) using materialize_features with scheduling triggers like CronSchedule or TableTrigger.
tags:
  - feature-engineering
  - materialization
  - serving
timestamp: "2026-06-18T15:13:04.129Z"
---

# Feature Materialization with Online and Offline Stores

**Feature Materialization with Online and Offline Stores** refers to the process of computing and persisting feature values from feature definitions into dedicated storage systems for efficient reuse in model training and serving workflows. Materialization transforms declarative feature definitions into physically stored data that can be accessed with low latency for both batch training and real-time inference. ^[declarative-features-databricks-on-aws.md]

## Overview

After defining features using the [Declarative Feature Engineering APIs](/concepts/declarative-feature-engineering-apis.md), materialization makes those features available for practical use. Without materialization, every training run or inference request would need to recompute features from source data, which is inefficient and slow. Materialization stores pre-computed feature values so they can be reused across multiple model training runs and serving requests. ^[declarative-features-databricks-on-aws.md]

The materialization workflow involves two types of storage:

- **Offline Store**: A storage system optimized for batch access, used primarily for model training and batch inference. The offline store contains historical feature values with point-in-time correctness.
- **Online Store**: A low-latency storage system designed for real-time serving, used when models need to make predictions on fresh data with minimal delay.

## Materialization Process

### Prerequisites

Features must be registered in [Unity Catalog](/concepts/unity-catalog.md) before they can be materialized. This registration is typically done using `create_feature` or `register_feature` from the `FeatureEngineeringClient`. ^[declarative-features-databricks-on-aws.md]

### Basic Materialization with Online and Offline Configs

The `materialize_features` API accepts both offline and online store configurations. Aggregation features (those using time-windowed functions like `Sum`, `Avg`, `Count`) can be materialized to both stores simultaneously. ^[declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import (
    OfflineStoreConfig, OnlineStoreConfig,
    CronSchedule, MaterializedFeaturePipelineScheduleState
)

online_config = OnlineStoreConfig(
    catalog_name="main",
    schema_name="feature_store",
    table_name_prefix="customer_features_serving",
    online_store_name="customer_features_store",
)

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

### Materialization Triggers

Different feature types support different materialization triggers: ^[declarative-features-databricks-on-aws.md]

| Trigger Type | Description | Feature Types Supported |
|---|---|---|
| `CronSchedule` | Periodic refresh based on a cron expression (e.g., hourly, daily) | Aggregation features |
| `TableTrigger` | Materialization triggered when the source table changes | Column selection features |

`ColumnSelection` features (simple column lookups without aggregation) use `TableTrigger` and only support online store configuration. ^[declarative-features-databricks-on-aws.md]

## Offline Store Usage

### Training Dataset Creation

Once features are materialized, you can use `create_training_set` with the materialized view to prepare offline batch training datasets. This provides point-in-time correct feature values for each training example. ^[declarative-features-databricks-on-aws.md]

```python
training_set = fe.create_training_set(
    df=labeled_df,
    features=[avg_feature, sum_feature],
    label="target",
)
training_set.load_df().display()
```

### Model Serving

After materializing features to an online store, models can be served using CPU model serving for real-time inference. The online store provides low-latency access to the latest feature values. ^[declarative-features-databricks-on-aws.md]

## Best Practices

### Grouping Materialization Calls

Materialize features from the same data source in a single `materialize_features` call to minimize data scans. This reduces compute costs and improves materialization performance. ^[declarative-features-databricks-on-aws.md]

### Consistent Granularity

Use the same time granularity (for example, all 1-hour or all 1-day slide durations) for features on the same data source. This enables better grouping during materialization and improves pipeline efficiency. ^[declarative-features-databricks-on-aws.md]

### Feature Type Considerations

- **Aggregation features** (using `Sum`, `Avg`, `Count`, etc. with time windows) support both offline and online materialization.
- **Column selection features** (simple column lookups) only support online store materialization.
- Aggregation features typically use `CronSchedule` triggers for periodic refresh, while column selection features use `TableTrigger` for event-driven refresh. ^[declarative-features-databricks-on-aws.md]

## Limitations

Materialization has specific limitations that vary by feature type and store configuration. For the most current list, consult the official documentation on Materialized features limitations. ^[declarative-features-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering APIs](/concepts/declarative-feature-engineering-apis.md) — The API surface for defining features before materialization
- [Train models with declarative features](/concepts/declarative-feature-limitations-and-constraints.md) — Using materialized features for model training
- Feature serving — Serving features from online stores for real-time inference
- [Unity Catalog](/concepts/unity-catalog.md) — The metadata catalog where features must be registered
- [Offline Store Config](/concepts/offlinestoreconfig.md)
- [Online Store Config](/concepts/onlinestoreconfig.md)
- [Materialization schedules](/concepts/materializedfeaturepipelineschedule.md)

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
