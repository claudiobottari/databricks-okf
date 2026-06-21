---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f85ec248ac95c882f0dcbb811d13eb3833cd341eb589c14ea93f18c11aa036ee
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-construction-and-registration-workflows
    - Registration Workflows and Feature Construction
    - FCARW
    - Feature Constructor and registration
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Feature Construction and Registration Workflows
description: "Two complementary approaches to creating features: two-step (local Feature construction + register_feature) for experimentation, and single-step (create_feature) for direct registration in Unity Catalog."
tags:
  - feature-engineering
  - workflow
  - api
timestamp: "2026-06-19T18:17:24.245Z"
---

# Feature Construction and Registration Workflows

**Feature Construction and Registration Workflows** refer to the two primary approaches for defining, validating, and persisting features in Databricks Feature Engineering: the two-step local construction workflow and the single-step direct registration workflow. Both workflows ultimately register features in [Unity Catalog](/concepts/unity-catalog.md) for use in training and inference.

## Two-Step Workflow: Local Construction with `register_feature()`

The recommended approach is to construct a `Feature` object locally and use `register_feature()` to persist it to Unity Catalog. This two-step workflow lets you experiment with features — including calling `create_training_set()` — before registering them. ^[declarative-features-api-reference-databricks-on-aws.md]

### Step 1: Construct a `Feature` Object

The `Feature` constructor accepts a data source, a function (aggregation or column selection), and optional parameters for entity columns, timestamp columns, name, and description. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import Feature, DeltaTableSource, AggregationFunction, Sum, RollingWindow
from datetime import timedelta

feature = Feature(
    source=DeltaTableSource(catalog_name="main", schema_name="store", table_name="transactions"),
    entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(Sum(input="amount"), RollingWindow(window_duration=timedelta(days=7))),
)
```

### Step 2: Register in Unity Catalog

After constructing and validating the feature locally, call `register_feature()` to persist it. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
fe = FeatureEngineeringClient()
registered_feature = fe.register_feature(
    feature=feature,
    catalog_name="main",
    schema_name="store",
)
```

## Single-Step Workflow: `create_feature()`

The `create_feature()` method validates, constructs, and immediately registers a feature in Unity Catalog in a single step. Use this when you do not need to experiment with the feature locally first. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
fe.create_feature(
    source=DeltaTableSource(catalog_name="main", schema_name="store", table_name="transactions"),
    function=AggregationFunction(Sum(input="amount"), RollingWindow(window_duration=timedelta(days=7))),
    catalog_name="main",
    schema_name="store",
    entity=["user_id"],
    timeseries_column="transaction_time",
)
```

## Feature Deletion

The `delete_feature()` method removes a feature from Unity Catalog by its fully qualified name. Before deleting a feature, remove or update any models or feature specs that reference it. If the feature has been materialized, delete the materialized feature first. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
fe.delete_feature(full_name="main.store.amount_sum_rolling_7d")
```

## Data Sources

### `DeltaTableSource`

`DeltaTableSource` is an ephemeral Python object used to define how features are computed from a source table. It does not create a new table. It specifies the configuration for reading data and aggregating features. ^[declarative-features-api-reference-databricks-on-aws.md]

Key parameters include:
- `catalog_name`, `schema_name`, `table_name`: Identify the source Delta table in Unity Catalog
- `filter_condition`: A SQL `WHERE` clause applied before aggregation
- `transformation_sql`: A SQL `SELECT` expression for column transformations (row-wise only)
- `schema_json`: Required if `transformation_sql` is set; specifies the schema of the resulting DataFrame

The `from_sql()` convenience method creates a `DeltaTableSource` from a SQL query, automatically extracting the table name, `transformation_sql`, and `filter_condition`. Only simple `SELECT ... FROM ... [WHERE ...]` queries are supported. ^[declarative-features-api-reference-databricks-on-aws.md]

### `RequestSource`

`RequestSource` defines a schema for data provided at inference time in the request payload rather than looked up from a pre-materialized table. During training, these columns are extracted from the labeled DataFrame passed to `create_training_set`. During model serving, the caller must include them in the HTTP request payload. ^[declarative-features-api-reference-databricks-on-aws.md]

`RequestSource` is used with `ColumnSelection` only and does not support aggregation functions or time windows. Supported data types include `INTEGER`, `FLOAT`, `BOOLEAN`, `STRING`, `DOUBLE`, `LONG`, `TIMESTAMP`, `DATE`, and `SHORT`. ^[declarative-features-api-reference-databricks-on-aws.md]

## Feature Functions

### Aggregation Functions

Aggregation functions are wrapped in an `AggregationFunction` together with a time window. Each function takes an `input` parameter specifying the source column to aggregate. Supported functions include `Sum`, `Avg`, `Count`, `ApproxCountDistinct`, and others. ^[declarative-features-api-reference-databricks-on-aws.md]

### `ColumnSelection` (Pass-Through)

`ColumnSelection` selects a single column from a source without applying any aggregation. It is wrapped directly in the `function` parameter (not inside `AggregationFunction`). With `DeltaTableSource`, it returns the latest value per entity key via a point-in-time join. With `RequestSource`, it passes through the value provided at inference time. ^[declarative-features-api-reference-databricks-on-aws.md]

## Time Windows

Declarative Feature Engineering APIs support three window types for time window-based aggregations:

- **Rolling windows**: Look back from the event time with explicit duration and optional delay. Useful for real-time aggregates over streaming data.
- **Tumbling windows**: Fixed, non-overlapping time windows. Each data point belongs to exactly one window.
- **Sliding windows**: Overlapping, rolling time windows with a configurable slide interval.

^[declarative-features-api-reference-databricks-on-aws.md]

## Filter Conditions

The `filter_condition` parameter on `DeltaTableSource` allows filtering rows from the source table before computing aggregations. This functions as a SQL `WHERE` clause applied prior to grouping and aggregating data. Filters are useful when working with large source tables that include a superset of data needed for feature computation. ^[declarative-features-api-reference-databricks-on-aws.md]

## Auto-Generated Names

When `name` is omitted, a feature name is automatically generated following the pattern `{column}_{function}_{window}`. For example, `price_avg_rolling_1h` or `transaction_count_rolling_30d_1d`. ^[declarative-features-api-reference-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering API](/concepts/declarative-feature-engineering-api.md) — The full API reference for feature construction
- [Unity Catalog](/concepts/unity-catalog.md) — The catalog system where features are registered
- materialize_features() API|Materialized Features — Features that are pre-computed and stored for low-latency serving
- Training and Inference with Declarative Features — Using registered features for model training and scoring
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) — The client class providing registration and management methods

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
