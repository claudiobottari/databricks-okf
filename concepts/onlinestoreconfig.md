---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 848c6034ee1b7ca45c28828ca2d2034800f46dd651e90d24f870993b2683cfb5
  pageDirectory: concepts
  sources:
    - materialize-declarative-features-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - onlinestoreconfig
    - Online Store Config
    - online store spec
    - online store specification
  citations:
    - file: materialize-declarative-features-databricks-on-aws.md
title: OnlineStoreConfig
description: Configuration for the online feature store used by model serving, creating Delta tables streamed to an Online Feature Store with the same name prefix.
tags:
  - feature-store
  - configuration
  - online-store
timestamp: "2026-06-19T19:31:04.094Z"
---

# OnlineStoreConfig

**OnlineStoreConfig** is a configuration class in the Databricks Feature Engineering API that specifies the target online store where materialized features are written for model serving. It is used with the `materialize_features()` method to stream feature data to an online feature store for low-latency inference. ^[materialize-declarative-features-databricks-on-aws.md]

## Overview

The `OnlineStoreConfig` defines the Unity Catalog location and online store name for materialized features. When `materialize_features()` is called with an `OnlineStoreConfig`, the feature store backend creates Delta tables at the specified `catalog.schema.table_name_prefix` path and streams those tables to the Online Feature Store under the same name. ^[materialize-declarative-features-databricks-on-aws.md]

## API Structure

The `OnlineStoreConfig` class is imported from `databricks.feature_engineering.entities` and accepts the following parameters: ^[materialize-declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import OnlineStoreConfig

online_store = OnlineStoreConfig(
    catalog_name="main",
    schema_name="feature_store",
    table_name_prefix="customer_features_serving",
    online_store_name="customer_features_store"
)
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `catalog_name` | `str` | Catalog name for the online table where materialized features will be stored |
| `schema_name` | `str` | Schema name for the online table |
| `table_name_prefix` | `str` | Table name prefix for the online table. The pipeline may create multiple tables with this prefix, each updated at different cadences |
| `online_store_name` | `str` | Name of the existing Online Feature Store to stream data to |

^[materialize-declarative-features-databricks-on-aws.md]

## Usage with `materialize_features()`

The `OnlineStoreConfig` is passed to the `materialize_features()` method of the `FeatureEngineeringClient`. When both an `OnlineStoreConfig` and an `OfflineStoreConfig` are provided, two materialized features are returned per input feature — one for each store type. ^[materialize-declarative-features-databricks-on-aws.md]

### Materializing Aggregation Features to Online Store

For aggregation features (those using `AggregationFunction`), materialization to an online store requires also materializing to an offline store. Both `offline_config` and `online_config` must be provided. The `online_store_name` must reference an existing Online Feature Store. ^[materialize-declarative-features-databricks-on-aws.md]

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
        quartz_cron_expression="0 0 * * * ?",
        timezone_id="UTC",
        pipeline_schedule_state=MaterializedFeaturePipelineScheduleState.ACTIVE,
    ),
)
```

### Materializing ColumnSelection Features to Online Store

`ColumnSelection` features can be materialized directly to an online store without requiring an `OfflineStoreConfig`. These features select the latest value of a single column per entity key without aggregation. ^[materialize-declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient
from databricks.feature_engineering.entities import (
    DeltaTableSource, Feature, ColumnSelection, TableTrigger, OnlineStoreConfig,
)

fe = FeatureEngineeringClient()

delta_source = DeltaTableSource(
    catalog_name="catalog",
    schema_name="schema",
    table_name="transactions",
)

amount_feature = Feature(
    source=delta_source,
    function=ColumnSelection("amount"),
    entity=["user_id"],
    timeseries_column="transaction_time",
    name="latest_transaction_amount",
)

amount_feature = fe.register_feature(
    feature=amount_feature,
    catalog_name="catalog",
    schema_name="schema",
)

mfs = fe.materialize_features(
    features=[amount_feature],
    online_config=OnlineStoreConfig(
        catalog_name="catalog",
        schema_name="feats_online",
        table_name_prefix="txn_",
        online_store_name="lb_usw2"
    ),
    trigger=TableTrigger(),
)
```

`ColumnSelection` features use `TableTrigger`, which runs the pipeline whenever the source Delta table receives a new commit. No `offline_config` is needed because `ColumnSelection` features are read directly from the source for offline use cases (training and batch inference). ^[materialize-declarative-features-databricks-on-aws.md]

## Requirements

- The `online_store_name` must reference an existing Online Feature Store. For instructions on creating one, see [Databricks Online Feature Stores](/concepts/databricks-online-feature-store.md). ^[materialize-declarative-features-databricks-on-aws.md]
- Features must be created with the declarative feature API and stored in Unity Catalog before materialization. ^[materialize-declarative-features-databricks-on-aws.md]

## Limitations

- `RequestSource` features cannot be materialized because they represent data provided at inference time. ^[materialize-declarative-features-databricks-on-aws.md]
- For materialized aggregation features, the online materialized feature cannot be deleted directly. Delete the paired offline materialized feature, and the change propagates to both. ^[materialize-declarative-features-databricks-on-aws.md]

## Related Concepts

- [OfflineStoreConfig](/concepts/offlinestoreconfig.md) — Configuration for the offline store where materialized features are written for training and batch scoring
- MaterializedFeature — Represents a declarative feature that has been precomputed and stored in Unity Catalog
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) — The API client used to materialize features
- [Declarative Feature APIs](/concepts/declarative-feature-engineering-apis.md) — The API for creating feature definitions stored in Unity Catalog
- [Databricks Online Feature Stores](/concepts/databricks-online-feature-store.md) — The service that provides low-latency feature serving for model inference

## Sources

- materialize-declarative-features-databricks-on-aws.md

# Citations

1. [materialize-declarative-features-databricks-on-aws.md](/references/materialize-declarative-features-databricks-on-aws-fe7c4a29.md)
