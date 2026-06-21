---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 239e05fb225b3e890bd11b25826739400d7dc16a5816b890c2003c0a95be6bff
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - filter-conditions-and-sql-transformations-on-source-data
    - SQL Transformations on Source Data and Filter Conditions
    - FCASTOSD
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Filter Conditions and SQL Transformations on Source Data
description: Mechanisms to filter rows (filter_condition) and transform columns (transformation_sql) at the DeltaTableSource level before aggregation, supporting row-wise operations like casts and arithmetic.
tags:
  - data-transformation
  - filtering
  - sql
timestamp: "2026-06-19T14:57:15.154Z"
---

## Filter Conditions and SQL Transformations on Source Data

**Filter Conditions and SQL Transformations on Source Data** let you preprocess a Delta source table before computing [Declarative Feature Engineering|declarative features](/concepts/declarative-feature-engineering-apis.md) using the `DeltaTableSource` object from the `FeatureEngineeringClient` API. By specifying a SQL filter and/or a SQL column transformation, you can reduce the volume of data fed into aggregations and adjust column names and types without creating separate views or intermediate tables. ^[declarative-features-api-reference-databricks-on-aws.md]

### Filter Conditions

A filter condition is a SQL `WHERE` clause that is applied to the source Delta table **before** any grouping or aggregation takes place. It is specified via the `filter_condition` parameter of a `DeltaTableSource`. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
high_value_source = DeltaTableSource(
    catalog_name="main",
    schema_name="ecommerce",
    table_name="transactions",
    filter_condition="amount > 100",  # Only rows where amount exceeds 100
)
```

The filter behaves like a `WHERE` clause in SQL: rows that do not satisfy the condition are excluded from feature computation. The aggregation granularity is still defined by the `entity` columns on the `Feature` definition, not by the filter. ^[declarative-features-api-reference-databricks-on-aws.md]

Multiple conditions can be combined using SQL operators (e.g., `AND`, `OR`):

```python
filter_condition="status = 'completed' AND payment_method = 'credit_card'"
```

### SQL Transformations

A SQL transformation is a `SELECT` expression that renames columns, casts types, or computes derived columns **before** aggregation. It is specified via the `transformation_sql` parameter of a `DeltaTableSource`. When `transformation_sql` is provided, the system does not use the default `SELECT *`; instead it uses only the columns and expressions listed. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
source = DeltaTableSource(
    catalog_name="main",
    schema_name="analytics",
    table_name="raw_events",
    transformation_sql="user_id, CAST(price_cents AS DOUBLE) / 100 AS price, event_time",
    schema_json=spark.sql(
        "SELECT user_id, CAST(price_cents AS DOUBLE) / 100 AS price, event_time "
        "FROM main.analytics.raw_events LIMIT 0"
    ).schema.json(),
)
```

Because the transformation changes the shape of the source data, **`schema_json` is mandatory** when `transformation_sql` is set. The schema must be provided as a Spark StructType JSON string (obtainable from `df.schema.json()`). ^[declarative-features-api-reference-databricks-on-aws.md]

#### Supported Expressions

Only **row-wise** expressions are supported in `transformation_sql` – column renames, casts, arithmetic, string operations, etc. Aggregation functions like `COUNT(*)` or `SUM()` are **not** allowed; use `AggregationFunction` on the feature definition instead. ^[declarative-features-api-reference-databricks-on-aws.md]

### Combined Usage

When both `filter_condition` and `transformation_sql` are set on the same `DeltaTableSource`, the effective query is:

```
SELECT {transformation_sql} FROM {table} WHERE {filter_condition}
```

This allows you to filter rows **and** reshape columns in a single source definition. ^[declarative-features-api-reference-databricks-on-aws.md]

### The `from_sql()` Convenience Method

`DeltaTableSource.from_sql()` automatically extracts the `table_name`, `transformation_sql`, and `filter_condition` from a simple SQL query. Only queries of the form `SELECT ... FROM ... [WHERE ...]` are supported; JOINs, subqueries, CTEs, and UNIONs are rejected. The method requires a Spark client to infer the output schema. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
source = DeltaTableSource.from_sql(
    spark_client=spark_client,
    sql="SELECT customer_id, event_ts, amount * 2 AS doubled_amount "
        "FROM main.schema.table WHERE status = 'active'",
)
```

### Important Considerations

- **Filtering vs. Granularity**: `filter_condition` filters rows before the `GROUP BY` that corresponds to the entity columns. It does not change the aggregation level (which is determined solely by the `entity` list on the `Feature`). ^[declarative-features-api-reference-databricks-on-aws.md]
- **Schema Requirement**: When using `transformation_sql`, you must provide `schema_json` describing the resulting columns and types. Omitting it raises a validation error. ^[declarative-features-api-reference-databricks-on-aws.md]
- **No Aggregation in Transformations**: Only scalar, row-level expressions are allowed in `transformation_sql`. All aggregation logic must be placed on the `Feature` definition using the appropriate `AggregationFunction`. ^[declarative-features-api-reference-databricks-on-aws.md]
- **Timestamp Columns**: The `timeseries_column` specified on the `Feature` must be of type `TimestampType` or `DateType`. Integer timestamps can work but may cause precision loss for time‑window aggregates. ^[declarative-features-api-reference-databricks-on-aws.md]

### Related Concepts

- [DeltaTableSource](/concepts/deltatablesource.md) – The source object that holds `filter_condition` and `transformation_sql`.
- [Declarative Feature Engineering API](/concepts/declarative-feature-engineering-api.md) – Overview of the API used to define features in Unity Catalog.
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) – How to define the aggregate operations that consume the preprocessed source data.
- [RequestSource](/concepts/requestsource.md) – An alternative source for inference‑time features, which does not support filters or transformations.
- Training and Inference with Declarative Features – How to use `create_training_set`, `log_model`, and `score_batch` with preprocessed features.

### Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
