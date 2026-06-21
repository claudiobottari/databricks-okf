---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5f53bd6d3c3cdc36174a989db6b3a1854309aae91640551dd80242f4efecbaa2
  pageDirectory: concepts
  sources:
    - materialize-declarative-features-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - columnselection-materialization
  citations:
    - file: materialize-declarative-features-databricks-on-aws.md
title: ColumnSelection Materialization
description: Declarative features that select the latest single-column value per entity key without aggregation; can only materialize to online stores (not offline).
tags:
  - feature-store
  - ColumnSelection
  - online-serving
timestamp: "2026-06-19T19:31:21.327Z"
---

## ColumnSelection Materialization

**ColumnSelection Materialization** is the process of precomputing and storing [ColumnSelection](/concepts/automl-column-selection.md) features — which select the latest value of a single column per entity key without aggregation — into an online feature store for low-latency serving. Unlike aggregation features, `ColumnSelection` features are not materialized to an offline store; they are fetched directly from the source Delta table at query time for training and batch inference. ^[materialize-declarative-features-databricks-on-aws.md]

### Overview

`ColumnSelection` features are defined using the declarative feature API and must be registered in Unity Catalog before materialization. They can only be materialized to an online store (via an `OnlineStoreConfig`), and no `OfflineStoreConfig` is required. Materialization is triggered by a `TableTrigger`, which runs the pipeline whenever the source Delta table receives a new commit. ^[materialize-declarative-features-databricks-on-aws.md]

Because `ColumnSelection` features do not involve aggregation, they have no aggregation window. The materialization pipeline writes the most recent row per entity key to the online table, providing the current latest value. ^[materialize-declarative-features-databricks-on-aws.md]

### Materialization Behavior

- The pipeline reads the source [DeltaTableSource](/concepts/deltatablesource.md) and extracts the latest value of the selected column for each entity key, ordered by the specified timeseries column.
- Online materialization populates the online table with these latest values, overwriting previous entries for the same key.
- `ColumnSelection` features use `TableTrigger`, not `CronSchedule`, because they are incrementally updated on source table commits. ^[materialize-declarative-features-databricks-on-aws.md]

### Example

The following example demonstrates materializing a `ColumnSelection` feature to an online store:

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

^[materialize-declarative-features-databricks-on-aws.md]

### Managing Materialized `ColumnSelection` Features

- **Listing**: Use `list_materialized_features()` to retrieve all materialized features, optionally filtering by `feature_name`.
- **Deleting**: Pass the online `MaterializedFeature` object to `delete_materialized_feature()`. Because `ColumnSelection` features are only materialized online, there is no paired offline materialized feature to delete separately. Deleting the online materialized feature removes the feature metadata; associated infrastructure (tables, pipelines, jobs) is cleaned up asynchronously after all features sharing those resources have been deleted. ^[materialize-declarative-features-databricks-on-aws.md]

### Limitations

- `ColumnSelection` features can only be materialized to online stores; offline materialization is not supported. ^[materialize-declarative-features-databricks-on-aws.md]
- They cannot be materialized together with aggregation features in a single `materialize_features()` call because the two types require different trigger types (`TableTrigger` vs. `CronSchedule`). ^[materialize-declarative-features-databricks-on-aws.md]
- `RequestSource` features cannot be materialized at all, as they represent data provided at inference time. ^[materialize-declarative-features-databricks-on-aws.md]

### Related Concepts

- [Declarative Feature APIs](/concepts/declarative-feature-engineering-apis.md) – API for defining features stored in Unity Catalog.
- [Online Feature Store](/concepts/online-feature-store.md) – The serving store where materialized features are written.
- [DeltaTableSource](/concepts/deltatablesource.md) – A source specification for a Delta table.
- TableTrigger – Trigger type that runs materialization on source table commits.
- Aggregation Materialization – Materialization of features that use aggregation functions.
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) – The Python client used for materialization operations.

### Sources

- materialize-declarative-features-databricks-on-aws.md

# Citations

1. [materialize-declarative-features-databricks-on-aws.md](/references/materialize-declarative-features-databricks-on-aws-fe7c4a29.md)
