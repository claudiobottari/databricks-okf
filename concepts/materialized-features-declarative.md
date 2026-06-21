---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 62581fa0b8d43b7fac155d64cac1462aad3da5b91009dfbdc968cc8c0d1b8647
  pageDirectory: concepts
  sources:
    - materialize-declarative-features-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - materialized-features-declarative
    - MF(
  citations:
    - file: materialize-declarative-features-databricks-on-aws.md
title: Materialized Features (Declarative)
description: Precomputed feature representations in Unity Catalog produced from declarative feature definitions via Lakeflow Spark Declarative Pipelines, used for model training, batch scoring, and online serving.
tags:
  - feature-store
  - materialization
  - unity-catalog
timestamp: "2026-06-19T19:31:12.634Z"
---

# Materialized Features (Declarative)

**Materialized Features (Declarative)** refers to the process of producing feature data from declarative feature definitions stored in Unity Catalog. Databricks creates and manages Lakeflow Spark Declarative Pipelines to populate tables in Unity Catalog for model training, batch scoring, or online serving. ^[materialize-declarative-features-databricks-on-aws.md]

## Requirements

- Features must be created with the [Declarative Feature API](/concepts/declarative-feature-engineering-api.md) and stored in Unity Catalog. ^[materialize-declarative-features-databricks-on-aws.md]
- `ColumnSelection` features can be materialized to online stores. See [ColumnSelection Materialization](/concepts/columnselection-materialization.md). ^[materialize-declarative-features-databricks-on-aws.md]
- `RequestSource` features cannot be materialized because they represent data provided at inference time. ^[materialize-declarative-features-databricks-on-aws.md]

## API data structures

### `OfflineStoreConfig`

Configuration for the offline store where materialized features will be written. When `materialize_features` is called, the feature store backend creates tables using the specified prefix. Each pipeline run materializes the latest feature values according to the materialization schedule. ^[materialize-declarative-features-databricks-on-aws.md]

Fields:

- `catalog_name` – Catalog for the offline table.
- `schema_name` – Schema for the offline table.
- `table_name_prefix` – Prefix for table names. The pipeline may create multiple tables with this prefix, each updated at different cadences. ^[materialize-declarative-features-databricks-on-aws.md]

### `OnlineStoreConfig`

Configuration for the online store, which stores features used by model serving. Materialization creates Delta tables with `catalog.schema.table_name_prefix` and streams them to the Online Feature Store with the same name. ^[materialize-declarative-features-databricks-on-aws.md]

Fields:

- `catalog_name`, `schema_name`, `table_name_prefix` – Same purpose as offline config.
- `online_store_name` – Name of the existing Online Feature Store (must already exist). ^[materialize-declarative-features-databricks-on-aws.md]

### `MaterializedFeature`

Represents a declarative feature that has a precomputed representation available in Unity Catalog. There is a distinct `MaterializedFeature` for the offline table and the online table. Users typically do not instantiate this directly. ^[materialize-declarative-features-databricks-on-aws.md]

## API function calls

### `materialize_features()`

Materializes a list of declarative features into either an offline Delta table or to an [Online Feature Store](/concepts/online-feature-store.md). Features must be registered in Unity Catalog before calling this function (e.g., using `create_feature` or `register_feature`). Locally constructed, unregistered features will not work. ^[materialize-declarative-features-databricks-on-aws.md]

```python
FeatureEngineeringClient.materialize_features(
    features: List[Feature],
    offline_config: Optional[OfflineStoreConfig] = None,
    online_config: Optional[OnlineStoreConfig] = None,
    trigger: Union[CronSchedule, TableTrigger],
) -> List[MaterializedFeature]:
```

The method returns a list of `MaterializedFeature` objects. If both `OnlineStoreConfig` and `OfflineStoreConfig` are provided, two materialized features are returned per input feature (one per store type). ^[materialize-declarative-features-databricks-on-aws.md]

The `trigger` parameter controls when the materialization pipeline runs: ^[materialize-declarative-features-databricks-on-aws.md]

- **`CronSchedule`**: Runs on a fixed schedule. Required for aggregation features (`AggregationFunction`).
- **`TableTrigger`**: Runs when the upstream Delta table receives a commit. Required for `ColumnSelection` features backed by a `DeltaTableSource`.

You cannot mix `ColumnSelection` and aggregation features in a single `materialize_features` call because they require different trigger types. Issue separate calls instead. ^[materialize-declarative-features-databricks-on-aws.md]

#### Materialize to offline store

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

#### Materialize to online store

To materialize aggregation features to an online store, you must also materialize to an offline store. Both `offline_config` and `online_config` are required. The `online_store_name` must reference an existing Online Feature Store. For instructions on creating one, see [Databricks Online Feature Stores](/concepts/databricks-online-feature-store.md). `ColumnSelection` features do not require an `OfflineStoreConfig`. ^[materialize-declarative-features-databricks-on-aws.md]

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

### `list_materialized_features()`

Returns a list of all materialized features in the user's Unity Catalog [Metastore](/concepts/metastore.md). By default, a maximum of 100 features are returned. You can change this limit using the `max_results` parameter. To filter by a feature name, use the optional `feature_name` parameter. ^[materialize-declarative-features-databricks-on-aws.md]

```python
FeatureEngineeringClient.list_materialized_features(
    feature_name: Optional[str] = None,
    max_results: int = 100,
) -> List[MaterializedFeature]:
```

### `delete_materialized_feature()`

Before deleting a materialized feature, remove or update any models or feature specs that reference the feature. ^[materialize-declarative-features-databricks-on-aws.md]

The feature to pass depends on the feature type: ^[materialize-declarative-features-databricks-on-aws.md]

- **Aggregation features**: Pass the offline materialized feature. If there is an online materialized feature for the same feature, both are deleted.
- **`ColumnSelection` features**: Pass the online materialized feature. `ColumnSelection` features are materialized only to the online store, so there is no paired offline feature.

As part of materialization, features are grouped by data source and aggregation window for efficiency. The materialization pipeline, offline table, and online table are not deleted until all grouped features have been deleted. When the last materialized feature in a group is deleted, the feature store schedules the associated resources for automatic cleanup by a background process. See [#Background resource cleanup](/concepts/feature-store-resource-cleanup.md). ^[materialize-declarative-features-databricks-on-aws.md]

```python
FeatureEngineeringClient.delete_materialized_feature(
    materialized_feature: MaterializedFeature,
) -> None
```

Use `list_materialized_features()` to obtain the `materialized_feature` argument. ^[materialize-declarative-features-databricks-on-aws.md]

## `ColumnSelection` materialization

`ColumnSelection` features select the latest value of a single column per entity key without aggregation. They can only be materialized to online stores. For offline use cases (training and batch inference), `ColumnSelection` features are fetched directly from the source data at query time, so offline materialization is not needed. ^[materialize-declarative-features-databricks-on-aws.md]

### Materialization behavior

- The pipeline writes the most recent row per entity key to the online table, with no aggregation window.
- Online materialization populates the online table with the current latest value per entity key. ^[materialize-declarative-features-databricks-on-aws.md]

### Example

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
# Register before materializing
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

`ColumnSelection` features use `TableTrigger`, which runs the pipeline whenever the source Delta table receives a new commit. No `offline_config` is needed because `ColumnSelection` features are read directly from the source for offline use cases. ^[materialize-declarative-features-databricks-on-aws.md]

> `RequestSource` features cannot be materialized because they represent data provided by the caller at inference time (or extracted from the labeled DataFrame at training time). There is no source table to read from. ^[materialize-declarative-features-databricks-on-aws.md]

## Background resource cleanup

When you delete a materialized feature, Databricks removes the feature metadata immediately. The associated infrastructure (tables, pipelines, and jobs) is cleaned up asynchronously by a background process. Because multiple materialized features can share the same tables and pipelines, these shared resources are not removed until every materialized feature that references them has been deleted. When the last materialized feature sharing a set of tables is deleted, the background process automatically deletes: ^[materialize-declarative-features-databricks-on-aws.md]

- The offline Delta tables containing the materialized feature data
- The online tables, if the features were materialized to an online store
- The materialization pipeline
- The orchestration job

This background process uses a Databricks-managed system service principal to perform these cleanup actions on your behalf. No action is required from you. There may be a short delay between deleting the last materialized feature in a group and the removal of the associated tables. ^[materialize-declarative-features-databricks-on-aws.md]

## Limitations

- **Batch rolling window features** cannot be materialized. Due to high fidelity of time correctness, rolling window features for offline training or batch inference are generated on the fly for each data point. ^[materialize-declarative-features-databricks-on-aws.md]
- `ColumnSelection` features can only be materialized to online stores. ^[materialize-declarative-features-databricks-on-aws.md]
- `RequestSource` features cannot be materialized. ^[materialize-declarative-features-databricks-on-aws.md]
- Materialized features can only be deleted in the workspace in which they were created. ^[materialize-declarative-features-databricks-on-aws.md]
- For materialized aggregation features, the online materialized feature cannot be deleted directly. Delete the paired offline materialized feature, and the change propagates to both. ^[materialize-declarative-features-databricks-on-aws.md]
- For materialized aggregation features created before April 20, 2026, the materialization pipeline continues producing new feature values until all materialized features in the pipeline have been deleted, which triggers resource cleanup. To create an updated pipeline that supports per-feature delete, delete and re-materialize the feature. ^[materialize-declarative-features-databricks-on-aws.md]
- For materialized `ColumnSelection` features, the materialization pipeline continues producing new feature values until all materialized features in the pipeline have been deleted, which triggers resource cleanup. ^[materialize-declarative-features-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature API](/concepts/declarative-feature-engineering-api.md) – API for defining features declaratively in Unity Catalog.
- [Feature Engineering](/concepts/featureengineeringclient-api.md) – Overall concept of feature creation and management.
- [Online Feature Store](/concepts/online-feature-store.md) – Store for serving features in real-time.
- [Serve Declarative Features](/concepts/declarative-feature-engineering-api.md) – How to serve declarative features for inference.
- [DeltaTableSource](/concepts/deltatablesource.md) – Source for `ColumnSelection` features.
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) – Feature type that requires `CronSchedule` trigger.

## Sources

- materialize-declarative-features-databricks-on-aws.md

# Citations

1. [materialize-declarative-features-databricks-on-aws.md](/references/materialize-declarative-features-databricks-on-aws-fe7c4a29.md)
