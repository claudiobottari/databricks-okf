---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a7a2956d48ab553e4ef5937cc4441c57229efa0ce15811e1e38eeebb3e13e5ed
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-sources-for-features
    - DSFF
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Data Sources for Features
description: "DeltaTableSource and RequestSource define where feature data originates: Delta tables (with optional filtering and transformations) or inference-time request payloads with a defined schema."
tags:
  - feature-engineering
  - data-sources
  - databricks
timestamp: "2026-06-19T18:17:37.616Z"
---

# Data Sources for Features

**Data Sources for Features** define where and how raw data is read for declarative feature computation in [Databricks Feature Engineering](/concepts/databricks-feature-engineering-client.md). The Declarative Feature Engineering API provides two types of data sources: `DeltaTableSource` for tabular data stored in [Unity Catalog](/concepts/unity-catalog.md) and `RequestSource` for data provided at inference time. Both are used as the `source` parameter when constructing a Feature object. ^[declarative-features-api-reference-databricks-on-aws.md]

## DeltaTableSource

`DeltaTableSource` is an ephemeral Python object that specifies how features are computed from a Delta table in Unity Catalog. It does not create a new table; it describes the configuration for reading and optionally filtering or transforming the source data before aggregation. ^[declarative-features-api-reference-databricks-on-aws.md]

### Constructor

```python
from databricks.feature_engineering.entities import DeltaTableSource

source = DeltaTableSource(
    catalog_name="main",
    schema_name="analytics",
    table_name="events",
    filter_condition="event_type = 'purchase'",         # Optional SQL WHERE clause
    transformation_sql="user_id, CAST(amount AS DOUBLE) / 100 AS price, event_time",  # Optional SELECT expression
    schema_json=df.schema.json()                        # Required if transformation_sql is set
)
```

**Parameters:**
- `catalog_name`, `schema_name`, `table_name`: Identify the source Delta table in Unity Catalog.
- `filter_condition`: A SQL `WHERE` clause applied before aggregation. For example, `"status = 'completed'"`.
- `transformation_sql`: A SQL `SELECT` expression applied to the source table. Use this to rename columns, cast types, or compute derived columns. If omitted, all columns are selected (`*`).
- `schema_json`: The schema of the resulting DataFrame after transformations, in Spark StructType JSON format (from `df.schema.json()`). **Required when `transformation_sql` is provided.**

When both `filter_condition` and `transformation_sql` are set, the resulting query is equivalent to:  
`SELECT {transformation_sql} FROM {table} WHERE {filter_condition}`. ^[declarative-features-api-reference-databricks-on-aws.md]

The `timeseries_column` (specified on the `Feature` definition, not on `DeltaTableSource`) must be of type `TimestampType` or `DateType`. Integer types can work but cause loss in precision for time window aggregates. ^[declarative-features-api-reference-databricks-on-aws.md]

### Using `transformation_sql` and `schema_json`

You can derive both values from a PySpark DataFrame query. This approach is particularly useful when you need to compute derived columns or cast types:

```python
df = spark.sql("""
  SELECT user_id, CAST(amount AS DOUBLE) / 100 AS amount_dollars, event_time
  FROM main.analytics.events
  WHERE event_date >= date_sub(current_date(), 7)
  LIMIT 0
""")

source = DeltaTableSource(
    catalog_name="main",
    schema_name="analytics",
    table_name="events",
    transformation_sql="user_id, CAST(amount AS DOUBLE) / 100 AS amount_dollars, event_time",
    filter_condition="event_date >= date_sub(current_date(), 7)",
    schema_json=df.schema.json()
)
```

`transformation_sql` supports only row-wise expressions (column renames, casts, arithmetic). Aggregation functions like `COUNT(*)` or `SUM()` are not supported; use [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) on the `Feature` definition instead. ^[declarative-features-api-reference-databricks-on-aws.md]

### `DeltaTableSource.from_sql()`

As a convenience method, `from_sql()` parses a SQL query to automatically extract the table name, `transformation_sql`, and `filter_condition`. Only simple `SELECT ... FROM ... [WHERE ...]` queries are supported. Complex SQL (JOINs, subqueries, CTEs, UNIONs) is rejected.

```python
from databricks.feature_engineering.entities import DeltaTableSource
from databricks.ml_features._spark_client._spark_client import SparkClient

spark_client = SparkClient()
source = DeltaTableSource.from_sql(
    spark_client=spark_client,
    sql="SELECT customer_id, event_ts, amount * 2 AS doubled_amount FROM main.sales.transactions"
)
``` ^[declarative-features-api-reference-databricks-on-aws.md]

### Iterating with `source.to_dataframe()`

Use `source.to_dataframe()` to preview the data that will be used for feature computation. This is useful for iterating on `filter_condition` and `transformation_sql` until they produce the expected results.

```python
source = DeltaTableSource(
    catalog_name="main",
    schema_name="analytics",
    table_name="events",
    filter_condition="event_type = 'purchase'"
)
source.to_dataframe().display()
``` ^[declarative-features-api-reference-databricks-on-aws.md]

### Entities: Defining the Aggregation Level

Entity columns define the level of aggregation for your features. They are specified on the `Feature` definition (not on `DeltaTableSource`). Entities determine how data is grouped (similar to a SQL `GROUP BY`) and the primary key structure of the output.

- **Customer-level aggregation**: `entity=["user_id"]` produces one row per user.
- **Customer-store-level aggregation**: `entity=["user_id", "store_id"]` produces one row per user–store pair.

The same `DeltaTableSource` can be shared across features with different entity configurations. ^[declarative-features-api-reference-databricks-on-aws.md]

## RequestSource

`RequestSource` defines a schema for data that is provided at inference time in the request payload rather than looked up from a pre‑materialized table. During training, these columns are extracted from the labeled DataFrame passed to `create_training_set`. During model serving, the caller must include them in the HTTP request payload. ^[declarative-features-api-reference-databricks-on-aws.md]

`RequestSource` is used with [ColumnSelection](/concepts/automl-column-selection.md) to pass through values directly. It does not support aggregation functions or time windows. ^[declarative-features-api-reference-databricks-on-aws.md]

### Defining the Schema

Define the schema as a list of `FieldDefinition` objects, each specifying a name and a `ScalarDataType`:

```python
from databricks.feature_engineering.entities import (
    FieldDefinition, RequestSource, ScalarDataType
)

request_source = RequestSource(
    schema=[
        FieldDefinition(name="transaction_amount", data_type=ScalarDataType.DOUBLE),
        FieldDefinition(name="vendor_id", data_type=ScalarDataType.STRING),
        FieldDefinition(name="transaction_time", data_type=ScalarDataType.DATE),
    ]
)
``` ^[declarative-features-api-reference-databricks-on-aws.md]

### Supported Data Types

`RequestSource` supports the scalar types defined in `ScalarDataType`:
- `INTEGER`, `FLOAT`, `BOOLEAN`, `STRING`, `DOUBLE`, `LONG`, `TIMESTAMP`, `DATE`, `SHORT`

Complex types like arrays, maps, and structs are not supported. ^[declarative-features-api-reference-databricks-on-aws.md]

### Model Signature and Inference

When a model is logged using `log_model` with a training set that includes `RequestSource` features, the `RequestSource` columns are added to the [MLflow](/concepts/mlflow.md) model signature as required inputs. The serving endpoint's API schema therefore reflects which fields callers must provide at inference time. ^[declarative-features-api-reference-databricks-on-aws.md]

## Usage with Feature Definitions

Both data sources are passed as the `source` parameter to the `Feature` constructor. The `function` parameter determines whether aggregation or pass‑through is applied.

```python
from databricks.feature_engineering.entities import (
    Feature, DeltaTableSource, RequestSource,
    AggregationFunction, Sum, ColumnSelection, RollingWindow
)
from datetime import timedelta

# Aggregation feature from Delta table
delta_source = DeltaTableSource(
    catalog_name="main", schema_name="store", table_name="transactions"
)
agg_feature = Feature(
    source=delta_source,
    entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(Sum(input="amount"), RollingWindow(window_duration=timedelta(days=7)))
)

# Pass-through feature from request payload
request_source = RequestSource(
    schema=[FieldDefinition(name="session_duration", data_type=ScalarDataType.DOUBLE)]
)
request_feature = Feature(
    source=request_source,
    function=ColumnSelection("session_duration"),
    name="session_duration"
)
``` ^[declarative-features-api-reference-databricks-on-aws.md]

## Related Concepts

- Feature – The core construct that combines a data source, function, and optional entity/timeseries columns.
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) – Wraps an aggregation operator (e.g., `Sum`, `Avg`, `Count`) with a time window.
- [ColumnSelection](/concepts/automl-column-selection.md) – Pass-through function for selecting a column without aggregation.
- [Time Windows](/concepts/time-windows.md) – Rolling, tumbling, and sliding windows for time-based aggregations.
- Training and Inference with Declarative Features – Workflows that use `create_training_set`, `log_model`, and `score_batch`.
- [Filter Conditions](/concepts/entity-columns-vs-filter-conditions.md) – Using `filter_condition` to exclude rows before aggregation.

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
