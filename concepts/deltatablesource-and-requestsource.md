---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 71fbe7e64af584192a911b44fa83fb49910ce586484d8ec0f0b79221dc524569
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - deltatablesource-and-requestsource
    - RequestSource and DeltaTableSource
    - DAR
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: DeltaTableSource and RequestSource
description: "Two data source types for feature computation: DeltaTableSource reads from Unity Catalog Delta tables (with optional filtering and transformation), and RequestSource defines inference-time schema for pass-through features."
tags:
  - data-sources
  - unity-catalog
  - feature-engineering
timestamp: "2026-06-19T14:57:01.976Z"
---

---  
title: DeltaTableSource and RequestSource  
summary: "Two data source types for features: DeltaTableSource for querying Delta tables with optional filters and transformations, and RequestSource for defining schemas of inference-time request data."  
sources:  
  - declarative-features-api-reference-databricks-on-aws.md  
  - declarative-features-databricks-on-aws.md  
kind: concept  
createdAt: "2026-06-18T15:13:16.322Z"  
updatedAt: "2026-06-19T09:56:42.720Z"  
tags:  
  - data-sources  
  - feature-engineering  
  - databricks  
aliases:  
  - deltatablesource-and-requestsource  
  - RequestSource and DeltaTableSource  
  - DAR  
confidence: 0.97  
provenanceState: extracted  
inferredParagraphs: 0  
---

# DeltaTableSource and RequestSource

**DeltaTableSource** and **RequestSource** are the two primary data-source types in the [Declarative Feature Engineering APIs](/concepts/declarative-feature-engineering-apis.md). They define where feature data originates — either from a registered Delta table in [Unity Catalog](/concepts/unity-catalog.md) (DeltaTableSource) or from request-time data provided during model serving (RequestSource). ^[declarative-features-api-reference-databricks-on-aws.md]

## DeltaTableSource

`DeltaTableSource` defines a feature source backed by an existing Delta table in Unity Catalog. It is the most commonly used source for time-series aggregation features, such as rolling averages, sums, or counts over historical data. ^[declarative-features-api-reference-databricks-on-aws.md]

### Properties

A `DeltaTableSource` is an ephemeral Python object — it does not create a new table but instead specifies the configuration for reading data and computing features. It is constructed with the Unity Catalog location of the table: ^[declarative-features-api-reference-databricks-on-aws.md]

- `catalog_name` – The catalog containing the source table.
- `schema_name` – The schema (database) containing the source table.
- `table_name` – The name of the source table.

Optional parameters include `filter_condition` for applying a SQL `WHERE` clause before aggregation, `transformation_sql` for column-level transformations (renames, casts, arithmetic), and `schema_json` to describe the resulting schema when `transformation_sql` is used. ^[declarative-features-api-reference-databricks-on-aws.md]

### Usage

`DeltaTableSource` is used with `Feature` objects and supports all [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) types (e.g., `Sum`, `Avg`, `Count`) and all window types (TumblingWindow, SlidingWindow, RollingWindow). The same `DeltaTableSource` instance can be reused across multiple feature definitions. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import DeltaTableSource, Feature, AggregationFunction, Sum, RollingWindow
from datetime import timedelta

source = DeltaTableSource(
    catalog_name="main",
    schema_name="analytics",
    table_name="user_events",
)

feature = Feature(
    source=source,
    entity=["user_id"],
    timeseries_column="event_time",
    function=AggregationFunction(Sum(input="amount"), RollingWindow(window_duration=timedelta(days=7))),
)
```

### Entity columns

Entity columns define the aggregation level (similar to `GROUP BY` in SQL) and are specified on the `Feature` definition, not on `DeltaTableSource`. Different features from the same `DeltaTableSource` can use different `entity` values — for example, one feature aggregated by `user_id` and another by both `user_id` and `store_id`. ^[declarative-features-api-reference-databricks-on-aws.md]

### Filter conditions

The `filter_condition` parameter filters rows from the source table **before** aggregation, like a SQL `WHERE` clause applied before `GROUP BY`. This is useful when working with large source tables that include a superset of data, without requiring separate views. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
high_value_transactions = DeltaTableSource(
    catalog_name="main",
    schema_name="ecommerce",
    table_name="transactions",
    filter_condition="amount > 100",
)
```

### Transformation SQL

The `transformation_sql` parameter applies a SQL `SELECT` expression to the source table for renaming columns, casting types, or computing derived columns before aggregation. When `transformation_sql` is provided, the `schema_json` parameter (in Spark StructType JSON format) is required. Only row-wise expressions are supported; aggregation functions like `COUNT(*)` or `SUM()` are not supported here — use `AggregationFunction` on the feature definition instead. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
source = DeltaTableSource(
    catalog_name="main",
    schema_name="analytics",
    table_name="events",
    transformation_sql="user_id, CAST(amount AS DOUBLE) AS amount_dollars, event_time",
    filter_condition="event_type = 'purchase'",
    schema_json=df.schema.json(),
)
```

### `from_sql()` convenience method

`DeltaTableSource.from_sql()` creates a source from a simple SQL `SELECT ... FROM ... [WHERE ...]` query, automatically extracting the table name, `transformation_sql`, and `filter_condition`. Complex queries (JOINs, subqueries, CTEs, UNIONs) are not supported. ^[declarative-features-api-reference-databricks-on-aws.md]

## RequestSource

`RequestSource` defines a schema for data that is provided at inference time in the request payload rather than looked up from a pre-materialized table. During training, these columns are extracted from the labeled DataFrame passed to `create_training_set`. During model serving, the caller must include them in the HTTP request payload. ^[declarative-features-api-reference-databricks-on-aws.md]

### Schema definition

Define the schema as a list of `FieldDefinition` objects, each specifying a column name and a `ScalarDataType`: ^[declarative-features-api-reference-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import (
    FieldDefinition, RequestSource, ScalarDataType,
)

request_source = RequestSource(
    schema=[
        FieldDefinition(name="session_duration", data_type=ScalarDataType.DOUBLE),
        FieldDefinition(name="vendor_id", data_type=ScalarDataType.STRING),
    ]
)
```

### Supported data types

`RequestSource` supports only scalar types defined in `ScalarDataType`: `INTEGER`, `FLOAT`, `BOOLEAN`, `STRING`, `DOUBLE`, `LONG`, `TIMESTAMP`, `DATE`, `SHORT`. Complex types like arrays, maps, and structs are not supported. ^[declarative-features-api-reference-databricks-on-aws.md]

### Usage with ColumnSelection

`RequestSource` is used exclusively with [ColumnSelection](/concepts/automl-column-selection.md) to pass through scalar values directly. It does **not** support aggregation functions or time windows. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import ColumnSelection, Feature

request_source = RequestSource(
    schema=[
        FieldDefinition(name="session_duration", data_type=ScalarDataType.DOUBLE),
    ]
)

session_feature = Feature(
    source=request_source,
    function=ColumnSelection("session_duration"),
    name="session_duration",
)
```

### Model signature

When a model is logged using `log_model` with a training set that includes `RequestSource` features, the `RequestSource` columns are added to the MLflow model signature as required inputs. The serving endpoint's API schema reflects which fields callers must provide at inference time. ^[declarative-features-api-reference-databricks-on-aws.md]

## Comparison

| Aspect | DeltaTableSource | RequestSource |
|--------|------------------|---------------|
| Data origin | Unity Catalog Delta table | Request payload at inference |
| Supported functions | All [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) types, `ColumnSelection` | Only `ColumnSelection` |
| Time windows | Tumbling, Sliding, Rolling | Not supported |
| Data types | All types supported | Only `ScalarDataType` values |
| Entity columns | Required for aggregation | Not applicable |
| Filter conditions | Supported (`filter_condition`) | Not applicable |
| Column transformations | Supported (`transformation_sql`) | Not applicable |

## Related Concepts

- [Declarative Feature Engineering APIs](/concepts/declarative-feature-engineering-apis.md) – The overarching framework these sources belong to
- [ColumnSelection](/concepts/automl-column-selection.md) – The function type used with `RequestSource` and for pass-through features
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) – Functions (Sum, Avg, Count) that require a time-series source
- TumblingWindow, SlidingWindow, RollingWindow – Window types available for `DeltaTableSource`
- materialize_features() API|Materialize Features – Process of persisting computed features for serving
- [Train models with declarative features](/concepts/declarative-feature-limitations-and-constraints.md) – How `create_training_set` uses these sources
- Feature constructor and register_feature – API details for creating and registering features

## Sources

- declarative-features-api-reference-databricks-on-aws.md
- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
