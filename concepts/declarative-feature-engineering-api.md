---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d7a56fdfc172c086fa2777a975c485193223387aff55e23976e0c25cae118d4
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - declarative-feature-engineering-api
    - DFEA
    - Declarative Feature Engineering
    - Declarative Feature API
    - Declarative Features
    - Declarative features API reference
    - Serve Declarative Features
    - SlidingWindow (declarative features)
    - declarative features
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Declarative Feature Engineering API
description: A Python-based API for defining, registering, and using machine learning features declaratively (vs. imperatively) with Unity Catalog on Databricks.
tags:
  - feature-engineering
  - api-reference
  - databricks
timestamp: "2026-06-19T18:17:23.876Z"
---

# Declarative Feature Engineering API

The **Declarative Feature Engineering API** is a Python API in [Databricks Feature Engineering](/concepts/databricks-feature-engineering-client.md) that allows you to define, register, and use machine learning features in [Unity Catalog](/concepts/unity-catalog.md) by declaring what data to use and how to transform it, rather than writing custom Spark pipelines for feature computation. You specify the source data, the aggregation or column selection logic, and the time window, and the system automatically computes [point-in-time correct features](/concepts/point-in-time-feature-joins.md) for training and inference. ^[declarative-features-api-reference-databricks-on-aws.md]

## Core API: Feature Definition and Registration

### `Feature` Constructor and `register_feature()`

The recommended workflow is to construct a `Feature` object locally and then persist it to Unity Catalog using `register_feature()`. This two-step approach allows you to experiment with features — including creating training sets — before registering them. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
Feature(
    source: DataSource,                                    # Required: DeltaTableSource or RequestSource
    function: Union[AggregationFunction, ColumnSelection], # Required: aggregation or column selection
    entity: Optional[List[str]] = None,                    # Required for aggregation: entity columns
    timeseries_column: Optional[str] = None,               # Required for aggregation: timestamp column
    name: Optional[str] = None,                            # Optional: feature name (auto-generated if omitted)
    description: Optional[str] = None                      # Optional: feature description
)
```

`FeatureEngineeringClient.register_feature()` registers a locally constructed `Feature` in Unity Catalog. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
FeatureEngineeringClient.register_feature(
    feature: Feature,       # Required: a Feature instance (not already registered)
    catalog_name: str,      # Required: Unity Catalog catalog name
    schema_name: str,       # Required: Unity Catalog schema name
) -> Feature
```

### `create_feature()`

`FeatureEngineeringClient.create_feature()` validates, constructs, and immediately registers a feature in Unity Catalog in a single step. Use this when you do not need to experiment with the feature locally first. ^[declarative-features-api-reference-databricks-on-aws.md]

### `delete_feature()`

`FeatureEngineeringClient.delete_feature()` deletes a feature from Unity Catalog by its fully qualified name (`<catalog>.<schema>.<feature_name>`). Before deleting a feature, remove or update any models or [feature specs](/concepts/featurespec.md) that reference it. If the feature has been materialized, delete the materialized feature first. ^[declarative-features-api-reference-databricks-on-aws.md]

## Supported Functions

### Aggregation Functions

Aggregation functions are wrapped in an `AggregationFunction` together with a [time window](/concepts/time-windows.md). Each function takes an `input` parameter specifying the source column to aggregate. The API supports operators like `Sum`, `Avg`, `ApproxCountDistinct`, and `Count`. ^[declarative-features-api-reference-databricks-on-aws.md]

### `ColumnSelection` (Pass-Through)

`ColumnSelection` selects a single column from a source without applying any aggregation. It is wrapped directly in the `function` parameter (not inside `AggregationFunction`). Use it with:

* **`DeltaTableSource`**: returns the latest value per entity key via a [point-in-time join](/concepts/point-in-time-joins.md) (no lookback window).
* **`RequestSource`**: passes through the value provided at inference time (or extracted from the labeled DataFrame at training time).

The return type is inferred from the source schema. ^[declarative-features-api-reference-databricks-on-aws.md]

## Features with Filter Conditions

The `filter_condition` parameter on `DeltaTableSource` lets you filter rows from the source table **before** computing aggregations. It functions as a SQL `WHERE` clause applied prior to grouping and aggregating data, similar to a SQL `WHERE` clause applied before `GROUP BY`. This is useful for working with large source tables that include a superset of data needed for feature computation, minimizing the need for separate views. ^[declarative-features-api-reference-databricks-on-aws.md]

## Data Sources

### `DeltaTableSource`

`DeltaTableSource` is an ephemeral Python object that defines how features are computed from a source Delta table. It does not create a new table. It specifies the catalog, schema, and table name, plus optional `filter_condition` and `transformation_sql` (a SQL `SELECT` expression applied before aggregation, e.g., for column renaming or casting). When `transformation_sql` is provided, the `schema_json` parameter (Spark StructType JSON format) is required. ^[declarative-features-api-reference-databricks-on-aws.md]

A convenience method `DeltaTableSource.from_sql()` parses a simple `SELECT ... FROM ... [WHERE ...]` query to automatically extract the table, transformation SQL, and filter condition. Complex SQL (JOINs, subqueries, CTEs, UNIONs) is rejected. ^[declarative-features-api-reference-databricks-on-aws.md]

Entity columns define the aggregation level (like a `GROUP BY`) and are specified on the `Feature` definition, not on the source. ^[declarative-features-api-reference-databricks-on-aws.md]

### `RequestSource`

`RequestSource` defines a schema for data provided at inference time in the request payload rather than looked up from a pre-materialized table. It is used exclusively with `ColumnSelection` (no aggregation). The schema is a list of `FieldDefinition` objects, each with a name and `ScalarDataType` (e.g., `INTEGER`, `STRING`, `DOUBLE`). Complex types such as arrays, maps, and structs are not supported. When a model is logged with a training set that includes `RequestSource` features, those columns become required inputs in the MLflow model signature. ^[declarative-features-api-reference-databricks-on-aws.md]

## Time Windows

Declarative Feature Engineering supports three window types for time‑based aggregation:

### Rolling Window
`RollingWindow` (previously named `ContinuousWindow`) is a fixed-length lookback window from the evaluation time. Features at time `T` aggregate events from `[T − window_duration − delay, T − delay)`. A rolling window is up‑to‑date and commonly used with streaming data. An optional `delay` accounts for data ingestion delays. ^[declarative-features-api-reference-databricks-on-aws.md]

### Tumbling Window
`TumblingWindow` is a pre‑determined, fixed‑length, non‑overlapping window that partitions time. Each event contributes to exactly one window. Features at time `t` aggregate data from windows ending at or before `t` (exclusive). Windows start at the Unix epoch. ^[declarative-features-api-reference-databricks-on-aws.md]

### Sliding Window
`SlidingWindow` is a fixed‑length window that advances by a slide interval, producing overlapping windows. Each event can contribute to multiple windows. Features at time `t` aggregate data from windows ending at or before `t` (exclusive). ^[declarative-features-api-reference-databricks-on-aws.md]

## Training and Inference API

* **`create_training_set()`** – Creates a training dataset with [point-in-time correct](/concepts/point-in-time-correctness.md) feature computation, given a labeled DataFrame and a list of `Feature` objects.
* **`log_model()`** – Logs a model with feature metadata for lineage tracking and automatic feature lookup during inference.
* **`score_batch()`** – Performs offline batch inference with automatic feature lookup using the feature metadata stored with the model. The input DataFrame must contain the entity and timeseries columns used during training. ^[declarative-features-api-reference-databricks-on-aws.md]

## Materialization Triggers

Triggers control when a materialization pipeline runs.

* **`CronSchedule`** – For aggregation features (`AggregationFunction`). Uses a Quartz cron expression for scheduled runs.
* **`TableTrigger`** – For `ColumnSelection` features backed by a `DeltaTableSource`. Runs whenever the upstream Delta table receives a new commit.

You cannot mix `ColumnSelection` and aggregation features in a single `materialize_features` call because they require different trigger types. Issue separate calls instead. ^[declarative-features-api-reference-databricks-on-aws.md]

## Auto-Generated Feature Names

When `name` is omitted, a name is automatically generated following the pattern `{column}_{function}_{window}`, for example `price_avg_rolling_1h` or `transaction_count_rolling_30d_1d`. ^[declarative-features-api-reference-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) – The underlying system for managing and serving features
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer where features are registered
- MLflow Models – Models logged with feature metadata for automatic inference
- [Point-in-time Joins](/concepts/point-in-time-joins.md) – The technique ensuring temporal consistency between training and inference
- materialize_features() API|Materialized Features – Pre-computed feature values for low-latency serving
- [Time Window Aggregation](/concepts/time-windows-for-aggregation.md) – The mechanism for computing window-based features

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
