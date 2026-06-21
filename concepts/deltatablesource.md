---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03cf7f72bca2ed3833624ec5d3c4777d5ec384f089ae600fc1f84226133cbb37
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deltatablesource
    - Delta Table Sources
    - Data source
    - Delta Table Streaming Source
    - Delta source
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: DeltaTableSource
description: An ephemeral Python object defining how features are computed from a Delta table in Unity Catalog; supports filter_condition, transformation_sql, schema_json, and helper methods like from_sql() and to_dataframe().
tags:
  - data-source
  - delta-table
  - feature-engineering
timestamp: "2026-06-18T15:11:59.067Z"
---

---
title: DeltaTableSource
summary: An ephemeral Python object that defines how features are computed from a Delta table in Unity Catalog, supporting filter conditions and SQL transformations
sources:
  - declarative-features-api-reference-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:44:58.588Z"
updatedAt: "2026-06-18T11:44:58.588Z"
tags:
  - data-source
  - feature-engineering
  - delta-lake
  - databricks
aliases:
  - deltatablesource
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# DeltaTableSource

**DeltaTableSource** is an ephemeral Python object in the Databricks Declarative Feature Engineering API that defines how features are computed from a source Delta table. It does not create a new table; instead, it specifies the configuration for reading data and applying aggregations or column selections during both training and inference. ^[declarative-features-api-reference-databricks-on-aws.md]

## Parameters

DeltaTableSource accepts the following parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `catalog_name` | `str` | Yes | Unity Catalog catalog name |
| `schema_name` | `str` | Yes | Unity Catalog schema name |
| `table_name` | `str` | Yes | Delta table name |
| `filter_condition` | `Optional[str]` | No | SQL `WHERE` clause applied **before** aggregation. Example: `"status = 'completed'"` |
| `transformation_sql` | `Optional[str]` | No | SQL `SELECT` expression for column renaming, casting, or deriving columns. Example: `"user_id, CAST(amount AS DOUBLE) AS amount, event_time"`. If omitted, all columns are selected (`*`). |
| `schema_json` | `Optional[str]` | No | Schema of the resulting DataFrame after transformations, in Spark StructType JSON format (from `df.schema.json()`). **Required if `transformation_sql` is provided.** |

^[declarative-features-api-reference-databricks-on-aws.md]

When both `filter_condition` and `transformation_sql` are set, the resulting query is: `SELECT {transformation_sql} FROM {table} WHERE {filter_condition}`. ^[declarative-features-api-reference-databricks-on-aws.md]

## Methods

### `from_sql()`

A convenience class method for creating a `DeltaTableSource` from a simple SQL query. The method parses the query to automatically extract the table name, `transformation_sql`, and `filter_condition`. Only `SELECT ... FROM ... [WHERE ...]` queries are supported; complex SQL (JOINs, subqueries, CTEs, UNIONs) is rejected. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
DeltaTableSource.from_sql(
    sql: str,
    spark_client
) -> DeltaTableSource
```

### `to_dataframe()`

Use `source.to_dataframe()` to preview the data that will be used for feature computation. This is useful for iterating on `filter_condition` and `transformation_sql` until they produce the expected results. ^[declarative-features-api-reference-databricks-on-aws.md]

## Notes on Usage

- The `timeseries_column` and `entity` columns are specified on the Feature definition, not on `DeltaTableSource`. The timeseries column must be of type `TimestampType` or `DateType` for time window aggregations. ^[declarative-features-api-reference-databricks-on-aws.md]
- `transformation_sql` supports only row-wise expressions (column renames, casts, arithmetic). Aggregate functions like `COUNT(*)` or `SUM()` are not supported inside `transformation_sql`; use [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) on the feature definition instead. ^[declarative-features-api-reference-databricks-on-aws.md]
- `filter_condition` filters rows **before** aggregation, acting like a SQL `WHERE` clause applied before `GROUP BY`. It does not change the granularity, which is always defined by `entity` on the feature definition. ^[declarative-features-api-reference-databricks-on-aws.md]

## Related Concepts

- Feature — The object that uses a DeltaTableSource as its source
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) — Wraps operators like `Sum`, `Avg`, `Count` together with a time window
- [ColumnSelection](/concepts/automl-column-selection.md) — Pass-through feature without aggregation
- [RequestSource](/concepts/requestsource.md) — Data source for inference-time inputs
- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) — The overall framework

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
