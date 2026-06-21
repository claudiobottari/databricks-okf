---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cc808896c67585039f7d311b8a2c8d207fda0249539a668eb47562c0430dac4b
  pageDirectory: concepts
  sources:
    - materialize-declarative-features-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - materialize_features-api
    - Materialize Features
    - Materialized Feature
    - Materialized Features
    - MaterializedFeature
    - list_materialized_features() API
    - materialize_features
    - Materialize Declarative Features
    - Materialize declarative features
    - Materializing Features
  citations:
    - file: materialize-declarative-features-databricks-on-aws.md
title: materialize_features() API
description: API function that materializes a list of registered declarative features into offline Delta tables and/or an Online Feature Store, controlled by a trigger (CronSchedule or TableTrigger).
tags:
  - feature-store
  - api
  - materialization
timestamp: "2026-06-19T19:31:05.419Z"
---

# materialize_features() API

The **`materialize_features()`** method is a function in the Databricks Feature Engineering client that produces feature data from declarative feature definitions stored in Unity Catalog. Materialization creates and manages Lakeflow Spark Declarative Pipelines to populate tables for model training, batch scoring, or online serving. ^[materialize-declarative-features-databricks-on-aws.md]

## Overview

`materialize_features()` takes a list of declarative features and writes their computed values to either an offline Delta table, an Online Feature Store, or both. Features must be registered in Unity Catalog before calling this function (for example, using `create_feature` or `register_feature`). Locally constructed features that have not been registered will not work. ^[materialize-declarative-features-databricks-on-aws.md]

## Method Signature

```python
FeatureEngineeringClient.materialize_features(
    features: List[Feature],
    offline_config: Optional[OfflineStoreConfig] = None,
    online_config: Optional[OnlineStoreConfig] = None,
    trigger: Union[CronSchedule, TableTrigger],
) -> List[MaterializedFeature]:
```

^[materialize-declarative-features-databricks-on-aws.md]

## Parameters

### `features`

A list of declarative Feature objects to materialize. All features in the list must be registered in Unity Catalog. ^[materialize-declarative-features-databricks-on-aws.md]

### `offline_config`

An optional [OfflineStoreConfig](/concepts/offlinestoreconfig.md) specifying the catalog, schema, and table name prefix for the offline Delta table where materialized features will be stored. Required for aggregation features. ^[materialize-declarative-features-databricks-on-aws.md]

### `online_config`

An optional [OnlineStoreConfig](/concepts/onlinestoreconfig.md) specifying the catalog, schema, table name prefix, and online store name for serving features. Required when materializing to an online store. ^[materialize-declarative-features-databricks-on-aws.md]

### `trigger`

Controls when the materialization pipeline runs. Accepts either a `CronSchedule` or a `TableTrigger`. ^[materialize-declarative-features-databricks-on-aws.md]

- **`CronSchedule`**: Runs on a fixed schedule. Required for aggregation features (`AggregationFunction`). ^[materialize-declarative-features-databricks-on-aws.md]
- **`TableTrigger`**: Runs when the upstream Delta table receives a commit. Required for `ColumnSelection` features backed by a `DeltaTableSource`. ^[materialize-declarative-features-databricks-on-aws.md]

## Return Value

The method returns a list of MaterializedFeature objects containing metadata about when feature values are updated and the Unity Catalog tables where features are materialized. If both an `OnlineStoreConfig` and an `OfflineStoreConfig` are provided, two materialized features are returned per feature — one for each store type. ^[materialize-declarative-features-databricks-on-aws.md]

## Usage Examples

### Materialize to Offline Store

```python
from databricks.feature_engineering import FeatureEngineeringClient
from databricks.feature_engineering.entities import (
    CronSchedule, MaterializedFeaturePipelineScheduleState, OfflineStoreConfig,
)

fe = FeatureEngineeringClient()
materialized = fe.materialize_features(
    features=features,
    offline_config=OfflineStoreConfig(
        catalog_name="main",
        schema_name="feature_store",
        table_name_prefix="customer_features"
    ),
    trigger=CronSchedule(
        quartz_cron_expression="0 0 * * * ?",  # Hourly
        timezone_id="UTC",
        pipeline_schedule_state=MaterializedFeaturePipelineScheduleState.ACTIVE,
    ),
)
```

^[materialize-declarative-features-databricks-on-aws.md]

### Materialize to Online Store

To materialize aggregation features to an online store, both `offline_config` and `online_config` are required. The `online_store_name` must reference an existing Online Feature Store. ^[materialize-declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient
from databricks.feature_engineering.entities import (
    CronSchedule, MaterializedFeaturePipelineScheduleState,
    OfflineStoreConfig, OnlineStoreConfig,
)

fe = FeatureEngineeringClient()
materialized = fe.materialize_features(
    features=features,
    offline_config=OfflineStoreConfig(
        catalog_name="main",
        schema_name="feature_store",
        table_name_prefix="customer_features"
    ),
    online_config=OnlineStoreConfig(
        catalog_name="main",
        schema_name="feature_store",
        table_name_prefix="customer_features_serving",
        online_store_name="customer_features_store"
    ),
    trigger=CronSchedule(
        quartz_cron_expression="0 0 * * * ?",  # Hourly
        timezone_id="UTC",
        pipeline_schedule_state=MaterializedFeaturePipelineScheduleState.ACTIVE,
    ),
)
```

^[materialize-declarative-features-databricks-on-aws.md]

## Important Rules

- You cannot mix `ColumnSelection` and aggregation features in a single `materialize_features` call because they require different trigger types. Issue separate calls instead. ^[materialize-declarative-features-databricks-on-aws.md]
- [ColumnSelection](/concepts/automl-column-selection.md) features can only be materialized to online stores. For offline use cases (training and batch inference), they are fetched directly from the source data at query time. ^[materialize-declarative-features-databricks-on-aws.md]
- [RequestSource](/concepts/requestsource.md) features cannot be materialized because they represent data provided by the caller at inference time. ^[materialize-declarative-features-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature API](/concepts/declarative-feature-engineering-api.md) — The API used to create feature definitions before materialization
- MaterializedFeature — The object returned by `materialize_features()`
- [OfflineStoreConfig](/concepts/offlinestoreconfig.md) — Configuration for offline Delta table storage
- [OnlineStoreConfig](/concepts/onlinestoreconfig.md) — Configuration for online feature serving
- CronSchedule — Schedule-based trigger for materialization pipelines
- TableTrigger — Commit-based trigger for materialization pipelines
- list_materialized_features() API — API for listing existing materialized features
- [delete_materialized_feature() API](/concepts/deleting-materialized-features.md) — API for removing materialized features

## Sources

- materialize-declarative-features-databricks-on-aws.md

# Citations

1. [materialize-declarative-features-databricks-on-aws.md](/references/materialize-declarative-features-databricks-on-aws-fe7c4a29.md)
