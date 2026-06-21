---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 84edcba8babc45d52aabf6028601e47002d395a5242643bc6c18ee3123253835
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - source-transformation-and-filtering
    - Filtering and Source Transformation
    - STAF
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Source Transformation and Filtering
description: Pre-processing source data before aggregation using filter_condition (SQL WHERE clause) and transformation_sql (SQL SELECT expression) with schema_json requirement, plus a convenience from_sql() factory method.
tags:
  - feature-engineering
  - transformation
  - data-preprocessing
timestamp: "2026-06-19T18:17:39.648Z"
---

## Source Transformation and Filtering

Source transformation and filtering refers to the ability to modify and restrict the data read from a Delta table **before** feature computation in the Databricks Declarative Feature Engineering API. These operations are applied at the source level using the `DeltaTableSource` object, separate from the aggregation logic defined in the `Feature` object. This allows you to reshape raw source data without creating intermediate views or tables. ^[declarative-features-api-reference-databricks-on-aws.md]

### `filter_condition`

The `filter_condition` parameter on `DeltaTableSource` specifies a SQL `WHERE` clause that filters rows from the source table before any aggregations are performed. It works like a `WHERE` clause applied before `GROUP BY` in SQL. This is useful when the source table contains a superset of the data needed for feature computation and you want to exclude irrelevant rows early. ^[declarative-features-api-reference-databricks-on-aws.md]

Multiple conditions can be combined with logical operators such as `AND` and `OR`. For example, `filter_condition="status = 'completed' AND payment_method = 'credit_card'"` ensures only completed credit-card orders are used for subsequent aggregations. ^[declarative-features-api-reference-databricks-on-aws.md]

### `transformation_sql`

The `transformation_sql` parameter defines a SQL `SELECT` expression that is applied to the source table. Use this to rename columns, cast data types, compute derived columns (e.g., converting cents to dollars), or select a subset of columns — all without modifying the underlying table. The expression supports only row‑wise operations (column renames, casts, arithmetic). Aggregation functions like `COUNT(*)` or `SUM()` are not supported here; those belong in the feature’s `AggregationFunction`. ^[declarative-features-api-reference-databricks-on-aws.md]

When `transformation_sql` is provided, the `schema_json` parameter is **required**. This parameter must contain the schema of the resulting DataFrame in Spark StructType JSON format. You can obtain it by running a PySpark query that mirrors the transformation and calling `df.schema.json()`. ^[declarative-features-api-reference-databricks-on-aws.md]

### Combining filter and transformation

When both `filter_condition` and `transformation_sql` are set, the resulting SQL query is:

```sql
SELECT {transformation_sql} FROM {table} WHERE {filter_condition}
```

This lets you both restrict rows and reshape columns in a single source definition. The `timeseries_column` used for time windows must be of type `TimestampType` or `DateType` (integer types can cause precision loss). ^[declarative-features-api-reference-databricks-on-aws.md]

### The `from_sql()` convenience method

The `DeltaTableSource.from_sql()` method accepts a simple `SELECT ... FROM ... [WHERE ...]` query and automatically extracts the table name, `transformation_sql`, and `filter_condition`. It uses a Spark client to infer the schema. Only straightforward queries are supported; complex SQL (joins, subqueries, CTEs, unions) is rejected. For such cases, construct the `DeltaTableSource` directly with the explicit parameters. ^[declarative-features-api-reference-databricks-on-aws.md]

### Iteration and preview

Use the `to_dataframe()` method on a `DeltaTableSource` instance to preview the data that will be fed into feature computation. This is helpful for iterating on `filter_condition` and `transformation_sql` until they produce the expected output. ^[declarative-features-api-reference-databricks-on-aws.md]

### Best practices

- Apply filters as early as possible to reduce the volume of data read from the source table.
- Use `transformation_sql` to clean or normalise raw columns (e.g., currency conversion, type casting) before aggregation.
- Always provide `schema_json` when using `transformation_sql`, and derive it from a real DataFrame to avoid schema mismatches.
- The entity columns and timeseries column are specified on the `Feature` definition, not on `DeltaTableSource`; source transformation only changes how the underlying rows are read. ^[declarative-features-api-reference-databricks-on-aws.md]

## Related Concepts

- [DeltaTableSource](/concepts/deltatablesource.md) — The data source object that hosts filter and transformation parameters.
- [Declarative Feature Engineering API](/concepts/declarative-feature-engineering-api.md) — The overarching API for defining features.
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) — How transformed and filtered data is aggregated per entity.
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The broader domain of feature creation in ML pipelines.
- [Unity Catalog](/concepts/unity-catalog.md) — The catalog system where source tables reside.

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
