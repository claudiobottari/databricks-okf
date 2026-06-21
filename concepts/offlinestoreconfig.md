---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4295d178cbc2927f960da9a2dd1eb4d3685eb03874cc981130822e58b07bacd7
  pageDirectory: concepts
  sources:
    - materialize-declarative-features-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - offlinestoreconfig
    - Offline Store Config
    - Offline Store for Batch Inference
  citations:
    - file: materialize-declarative-features-databricks-on-aws.md
title: OfflineStoreConfig
description: Configuration specifying the Unity Catalog catalog, schema, and table name prefix where materialized features are stored as Delta tables for offline use (training, batch scoring).
tags:
  - feature-store
  - configuration
  - offline-store
timestamp: "2026-06-19T19:31:05.268Z"
---

---
title: OfflineStoreConfig
summary: Configuration for the offline Delta table where materialized declarative features are stored in Unity Catalog.
sources:
  - materialize-declarative-features-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:26:53.977Z"
updatedAt: "2026-06-18T12:26:53.977Z"
tags:
  - databricks
  - feature-engineering
  - offline-store
  - materialization
aliases:
  - offline-store-config
  - offline-store-configuration
confidence: 0.99
provenanceState: extracted
inferredParagraphs: 0
---

# OfflineStoreConfig

**OfflineStoreConfig** is a configuration object used in the Databricks [Feature Engineering](/concepts/featureengineeringclient-api.md) client to specify the Unity Catalog location where materialized declarative features are written as Delta tables. When `materialize_features()` is called with an `offline_config`, the feature store creates tables in the specified [Catalog and Schema](/concepts/catalog-and-schema.md) using the given table name prefix. Each pipeline run materializes the latest feature values into these tables according to the materialization schedule. ^[materialize-declarative-features-databricks-on-aws.md]

## Fields

The `OfflineStoreConfig` class has three required parameters:

| Field | Type | Description |
|-------|------|-------------|
| `catalog_name` | `str` | The Unity Catalog catalog name where the offline table will be stored. |
| `schema_name` | `str` | The schema name within the catalog for the offline table. |
| `table_name_prefix` | `str` | The prefix used for the table name. The pipeline may create multiple tables with this prefix, each updated at different cadences. |

^[materialize-declarative-features-databricks-on-aws.md]

### Example

```python
from databricks.feature_engineering.entities import OfflineStoreConfig

offline_store = OfflineStoreConfig(
    catalog_name="main",
    schema_name="feature_store",
    table_name_prefix="customer_features"
)
```

^[materialize-declarative-features-databricks-on-aws.md]

## Usage in `materialize_features()`

The `OfflineStoreConfig` is passed as the `offline_config` parameter of the `FeatureEngineeringClient.materialize_features()` method. It is required when materializing **aggregation features** (those using `AggregationFunction`). For aggregation features, an offline table must be created before features can be served to an online store; both `offline_config` and `online_config` are then needed together. ^[materialize-declarative-features-databricks-on-aws.md]

In contrast, [ColumnSelection](/concepts/automl-column-selection.md) features cannot be materialized offline — they are read directly from the source Delta table at training or batch inference time — so `ColumnSelection` features do not require an `OfflineStoreConfig`. Similarly, [RequestSource](/concepts/requestsource.md) features cannot be materialized at all. ^[materialize-declarative-features-databricks-on-aws.md]

The `trigger` parameter of `materialize_features()` controls when the materialization pipeline runs. For aggregation features, a `CronSchedule` trigger is required; for `ColumnSelection` features, a `TableTrigger` is required. ^[materialize-declarative-features-databricks-on-aws.md]

## Related Concepts

- [OnlineStoreConfig](/concepts/onlinestoreconfig.md) – Configuration for the online feature store used by model serving.
- MaterializedFeature – Represents a declarative feature that has been materialized, with separate instances for offline and online stores.
- materialize_features() API|Materialize Features – The process of producing precomputed feature tables from declarative feature definitions.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) that stores the materialized feature tables.
- [Feature Engineering](/concepts/featureengineeringclient-api.md) – The broader API used to create, register, and materialize features.

## Sources

- materialize-declarative-features-databricks-on-aws.md

# Citations

1. [materialize-declarative-features-databricks-on-aws.md](/references/materialize-declarative-features-databricks-on-aws-fe7c4a29.md)
