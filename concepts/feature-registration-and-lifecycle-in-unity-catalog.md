---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bad10a672856f0c3976e7ae1f3b0be1a12a14cbdf83baeb00e661d87c3e1e644
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-registration-and-lifecycle-in-unity-catalog
    - Lifecycle in Unity Catalog and Feature Registration
    - FRALIUC
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Feature Registration and Lifecycle in Unity Catalog
description: Process of persisting locally-defined Feature objects into Unity Catalog using register_feature or create_feature, enabling governance, discoverability, and reuse across teams.
tags:
  - feature-engineering
  - unity-catalog
  - governance
  - databricks
timestamp: "2026-06-19T09:57:40.035Z"
---

# Feature Registration and Lifecycle in Unity Catalog

**Feature Registration and Lifecycle in Unity Catalog** refers to the process of defining, persisting, materializing, and serving features using the Declarative Feature Engineering APIs. These APIs allow you to create features from Delta table sources and request-time data, register them as Unity Catalog objects, and manage their lifecycle through materialization to offline and online stores for training and serving. ^[declarative-features-databricks-on-aws.md]

## Overview

The Declarative Feature Engineering APIs provide two main workflows for registering features: using `create_feature` for a one-step define‑and‑register operation, or constructing a `Feature` object locally and later persisting it with `register_feature`. Once registered, features can be materialized to offline stores for batch inference or online stores for low‑latency serving, and they can be used directly in model training via `create_training_set`. ^[declarative-features-databricks-on-aws.md]

## Requirements

To use the declarative APIs, you need:
- A classic compute cluster running Databricks Runtime 17.0 ML or above.
- The custom Python package installed: `%pip install databricks-feature-engineering>=0.15.0` (followed by `dbutils.library.restartPython()`).

^[declarative-features-databricks-on-aws.md]

## Registration Methods

### One‑step: `create_feature`
Define and register a feature in Unity Catalog simultaneously. You specify the source (as a `DeltaTableSource`), entity columns, timeseries column, computation function, and the target catalog/schema/name. The feature is immediately available. ^[declarative-features-databricks-on-aws.md]

```python
latest_amount = fe.create_feature(
    source=source,
    function=ColumnSelection("amount"),
    entity=["user_id"],
    timeseries_column="transaction_time",
    catalog_name=CATALOG_NAME,
    schema_name=SCHEMA_NAME,
    name="latest_amount",
)
```

### Two‑step: Local construction then `register_feature`
Build a `Feature` object locally using the `Feature` class, optionally explore it with `compute_features`, and then persist it to Unity Catalog later. This is useful during iterative development. ^[declarative-features-databricks-on-aws.md]

```python
avg_feature = Feature(
    source=source,
    entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(Avg(input="amount"), TumblingWindow(window_duration=timedelta(days=30))),
    name="avg_transaction_30d",
)
avg_feature = fe.register_feature(
    feature=avg_feature,
    catalog_name=CATALOG_NAME,
    schema_name=SCHEMA_NAME,
)
```

## Lifecycle Phases

### 1. Training Set Creation
After registration, features can be combined with a labeled DataFrame using `create_training_set` to produce a point‑in‑time correct training dataset. This works for both registered and unregistered local features. ^[declarative-features-databricks-on-aws.md]

```python
training_set = fe.create_training_set(
    df=labeled_df,
    features=[avg_feature, sum_feature],
    label="target",
)
training_set.load_df().display()
```

### 2. Model Logging and Serving
When training a model with MLflow, use `fe.log_model()` to capture the feature‑to‑model lineage. The logged model automatically references the registered features, enabling consistent inference. ^[declarative-features-databricks-on-aws.md]

```python
fe.log_model(
    model=model,
    artifact_path="recommendation_model",
    flavor=mlflow.sklearn,
    training_set=training_set,
    registered_model_name=f"{CATALOG_NAME}.{SCHEMA_NAME}.recommendation_model",
)
```

### 3. Feature Materialization
Materialization makes features available for serving. You can materialize to an **offline store** (for batch scoring) and/or an **online store** (for real‑time serving). The trigger can be a `CronSchedule` (time‑based) for aggregation features, or a `TableTrigger` (change‑based) for column‑selection features. ^[declarative-features-databricks-on-aws.md]

```python
# Aggregation features with CronSchedule
fe.materialize_features(
    features=[avg_feature, sum_feature],
    offline_config=OfflineStoreConfig(
        catalog_name=CATALOG_NAME,
        schema_name=SCHEMA_NAME,
        table_name_prefix="customer_features",
    ),
    online_config=OnlineStoreConfig(
        catalog_name=CATALOG_NAME,
        schema_name=SCHEMA_NAME,
        table_name_prefix="customer_features_serving",
        online_store_name="customer_features_store",
    ),
    trigger=CronSchedule(
        quartz_cron_expression="0 0 * * * ?",  # Hourly
        timezone_id="UTC",
        pipeline_schedule_state=MaterializedFeaturePipelineScheduleState.ACTIVE,
    ),
)

# ColumnSelection features with TableTrigger
fe.materialize_features(
    features=[latest_amount],
    online_config=online_config,
    trigger=TableTrigger(),
)
```

The `MaterializedFeaturePipelineScheduleState` can be set to `ACTIVE` or `PAUSED`, controlling whether the materialization pipeline runs on the defined schedule. ^[declarative-features-databricks-on-aws.md]

### 4. Batch Inference
Use `score_batch()` to run batch inference with materialized features. The API automatically retrieves features from the offline store. ^[declarative-features-databricks-on-aws.md]

## Feature Lifecycle Management

- **Registration in Unity Catalog** makes features discoverable and reusable across workspaces and teams, with full lineage tracking.
- **Materialization** persists computed feature values, improving performance and enabling low‑latency serving.
- **Pipeline scheduling** (via `CronSchedule`) automates refreshes; pausing the schedule stops updates while preserving the materialized data.
- **Offline vs. Online stores** separate batch and real‑time workloads; online stores support model serving with CPU endpoints.

## Best Practices

### Feature naming
Use descriptive, consistent names for business‑critical features. During development, auto‑generated names (based on source and function) can be used to quickly iterate. ^[declarative-features-databricks-on-aws.md]

### Time windows
Align windows with business cycles (daily, weekly). Shorter windows capture recent trends but may be noisy; longer windows smooth variability. Start with sliding windows for most use cases. Tumbling and sliding windows scale better than rolling windows. ^[declarative-features-databricks-on-aws.md]

### Performance
Materialize features from the same data source in a single `materialize_features` call to minimize data scans. Use consistent granularity (e.g., 1‑hour slide durations) across features on the same source to enable efficient grouping. ^[declarative-features-databricks-on-aws.md]

### Entity vs. filter conditions
Use different `entity` definitions when you need different aggregation levels (e.g., customer‑level vs. customer‑merchant). Use `filter_condition` on the `DeltaTableSource` when you need to filter rows at the same aggregation level (e.g., only high‑value transactions). ^[declarative-features-databricks-on-aws.md]

## Limitations

- Entity and timeseries column names must match between the training dataset and feature definitions when using `create_training_set`.
- The label column in the training dataset must not exist in any source table used for feature definitions.
- Only a limited list of UDAFs (user‑defined aggregate functions) is supported in `create_feature`.
- Entity columns cannot be of type `DATE` or `TIMESTAMP`.
- `RequestSource` supports only scalar data types; complex types (arrays, maps, structs) are not supported.
- `RequestSource` does not support aggregation functions or time windows – only `ColumnSelection`.
- Entity column names, timeseries column names, and request feature column names must be globally unique across all sources in a training set or serving endpoint.

^[declarative-features-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering APIs](/concepts/declarative-feature-engineering-apis.md)
- materialize_features() API|Materialize Declarative Features
- Online Store for Feature Serving
- [Offline Store for Batch Inference](/concepts/offlinestoreconfig.md)
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md)
- Unity Catalog Objects
- [Point-in-time correctness](/concepts/point-in-time-correctness.md)

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
