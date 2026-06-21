---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6daac68300ed6e39307c48decffc81fdb146a2c8e5964bfe95a82d4b121bf7e1
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-materialization-for-offline-and-online-serving
    - Online Serving and Feature Materialization for Offline
    - FMFOAOS
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Feature Materialization for Offline and Online Serving
description: Process of materializing defined features to offline stores for efficient batch reuse or online stores for low-latency model serving using materialize_features.
tags:
  - serving
  - materialization
  - mlops
timestamp: "2026-06-18T11:45:48.408Z"
---

# Feature Materialization for Offline and Online Serving

**Feature materialization** is the process of pre‑computing and persisting features so they can be reused efficiently in training pipelines, batch inference, and real‑time model serving. The [Declarative Feature Engineering APIs](/concepts/declarative-feature-engineering-apis.md) provide a `materialize_features` method that writes features to an offline store, an online store, or both, depending on the use case. ^[declarative-features-databricks-on-aws.md]

## Overview

After defining a feature using `create_feature` or retrieving an existing one with `get_feature`, you can call `materialize_features` to compute the feature values and store them in a purpose‑built store. Materialization avoids recomputing the same aggregations multiple times and reduces latency during serving. ^[declarative-features-databricks-on-aws.md]

### Offline materialization

Offline materialization writes features to a Delta table in Unity Catalog. This table can then be used with `create_training_set` to prepare a point‑in‑time correct training dataset, or for batch scoring. The offline store is configured with an `OfflineStoreConfig` object that specifies the target catalog, schema, and table name prefix. ^[declarative-features-databricks-on-aws.md]

### Online materialization

Online materialization writes features to an online store (e.g., a low‑latency key‑value store) so that model serving endpoints can look up the most recent feature values in real time. The online store is configured with an `OnlineStoreConfig` that names the store and the target catalog, schema, and table name prefix. After materializing features to the online store, models can be served using CPU model serving. ^[declarative-features-databricks-on-aws.md]

## Triggers

Materialization is driven by a trigger that defines when and how often the feature values should be recomputed.

### CronSchedule

Use `CronSchedule` for features defined with aggregation functions such as `Avg`, `Sum`, `Count`, or `TumblingWindow` / `SlidingWindow`. These features require periodic recomputation to keep the aggregations up to date. `CronSchedule` supports both offline and online configurations. ^[declarative-features-databricks-on-aws.md]

```python
trigger = CronSchedule(
    quartz_cron_expression="0 0 * * * ?",  # Hourly
    timezone_id="UTC",
    pipeline_schedule_state=MaterializedFeaturePipelineScheduleState.ACTIVE,
)
```

### TableTrigger

Use `TableTrigger` for features defined with a simple `ColumnSelection` function. These features represent the latest value of a column and are refreshed whenever the source Delta table is updated. `TableTrigger` supports only online configuration; offline materialization is not applicable for column‑selection features. ^[declarative-features-databricks-on-aws.md]

```python
trigger = TableTrigger()
```

## Best practices

- **Batch materialization calls.** Materialize features that originate from the same data source in a single `materialize_features` call. This reduces the number of data scans and improves performance. ^[declarative-features-databricks-on-aws.md]
- **Align window granularity.** When materializing multiple features on the same source, use the same granularity (for example, all 1‑hour or all 1‑day slide durations) so that the materialization engine can group them efficiently. ^[declarative-features-databricks-on-aws.md]
- **Separate offline and online triggers if needed.** Aggregation features can be materialized to both stores with a single `CronSchedule`. Column‑selection features are materialized online only, using `TableTrigger`.

## Limitations

Specific limitations of feature materialization are documented on the materialize_features() API|Materialize declarative features page. General limitations of the feature engineering APIs – such as supported data types, uniqueness requirements for entity and timeseries column names, and the restricted set of aggregation functions – also apply to materialized features. ^[declarative-features-databricks-on-aws.md]

## Example

The following excerpt from the quickstart shows how to materialize aggregation features to both offline and online stores, and a column‑selection feature to the online store only.

```python
# Aggregation features: materialize to offline and online stores
fe.materialize_features(
    features=[avg_feature, sum_feature],
    offline_config=OfflineStoreConfig(
        catalog_name=CATALOG_NAME,
        schema_name=SCHEMA_NAME,
        table_name_prefix="customer_features",
    ),
    online_config=online_config,
    trigger=CronSchedule(
        quartz_cron_expression="0 0 * * * ?",
        timezone_id="UTC",
        pipeline_schedule_state=MaterializedFeaturePipelineScheduleState.ACTIVE,
    ),
)

# ColumnSelection feature: materialize only to online store
fe.materialize_features(
    features=[latest_amount],
    online_config=online_config,
    trigger=TableTrigger(),
)
```

^[declarative-features-databricks-on-aws.md]

## Related concepts

- [Declarative Feature Engineering APIs](/concepts/declarative-feature-engineering-apis.md) – The API surface that provides `materialize_features`.
- materialize_features() API|Materialize declarative features – Dedicated documentation page for materialization details and limitations.
- [Feature Store](/concepts/feature-store.md) – Unity Catalog feature store that stores materialized feature definitions.
- [Offline Store](/concepts/offline-feature-store.md) – Delta table storage for training and batch inference.
- [Online Store](/concepts/online-feature-store.md) – Low‑latency storage for real‑time model serving.
- CronSchedule – Trigger for periodic materialization of aggregation features.
- TableTrigger – Trigger for incremental materialization of column‑selection features.
- [ColumnSelection](/concepts/automl-column-selection.md) – Feature function that selects the latest column value.
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) – Base class for time‑window aggregations.
- MLflow Models – Models that consume materialized features during serving.

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
