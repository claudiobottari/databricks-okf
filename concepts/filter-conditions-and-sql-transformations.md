---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1c400c768b85854dcd3778a14fce97bb00cbeed5b23753868412c2733c120f1d
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - filter-conditions-and-sql-transformations
    - SQL Transformations and Filter Conditions
    - FCAST
    - filter-conditions-and-sql-transformations-on-source-data
    - SQL Transformations on Source Data and Filter Conditions
    - FCASTOSD
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Filter Conditions and SQL Transformations
description: Mechanisms to filter source rows before aggregation (filter_condition as SQL WHERE clause) and transform columns (transformation_sql for renaming, casting, arithmetic) within DeltaTableSource, with schema_json for type safety.
tags:
  - data-preprocessing
  - feature-engineering
  - sql
timestamp: "2026-06-19T09:57:08.094Z"
---

---
title: Filter Conditions and SQL Transformations
summary: Use filter_condition and transformation_sql parameters on DeltaTableSource to filter rows and transform columns before aggregation, enabling efficient feature computation without separate views.
sources:
  - declarative-features-api-reference-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T12:00:00.000Z"
updatedAt: "2026-06-19T12:00:00.000Z"
tags:
  - feature-engineering
  - declarative-features
  - databricks
aliases:
  - filter-conditions-and-sql-transformations
  - FCST
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Filter Conditions and SQL Transformations

**Filter Conditions and SQL Transformations** refer to two optional parameters of `DeltaTableSource` in the [Declarative Feature Engineering API](/concepts/declarative-feature-engineering-api.md) that allow you to preprocess source data before computing features. `filter_condition` applies a SQL `WHERE` clause to restrict rows, while `transformation_sql` applies a `SELECT` expression to rename, cast, or derive columns. Both operate before aggregation, reducing the need for separate materialized views. ^[declarative-features-api-reference-databricks-on-aws.md]

## How They Work

Both parameters are defined on a `DeltaTableSource` instance and are applied at the source level—**before** any entity grouping or window-based aggregation occurs. When both are provided, the effective query is:

```sql
SELECT {transformation_sql} FROM {table} WHERE {filter_condition}
```

^[declarative-features-api-reference-databricks-on-aws.md]

The `timeseries_column` (specified on the `Feature` definition) must be of type `TimestampType` or `DateType`. Integer types can work but cause precision loss for time‑window aggregates. ^[declarative-features-api-reference-databricks-on-aws.md]

## `filter_condition`

The `filter_condition` parameter accepts a SQL `WHERE` clause that is evaluated **before** grouping and aggregation. This is useful when the source table contains a superset of events (for example, all transaction types) but the feature should only consider a subset (for example, only completed purchases). ^[declarative-features-api-reference-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import DeltaTableSource

high_value_transactions = DeltaTableSource(
    catalog_name="main",
    schema_name="ecommerce",
    table_name="transactions",
    filter_condition="amount > 100",
)
```

Multiple conditions can be combined with SQL logic:

```python
completed_orders_source = DeltaTableSource(
    catalog_name="main",
    schema_name="ecommerce",
    table_name="orders",
    filter_condition="status = 'completed' AND payment_method = 'credit_card'",
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

## `transformation_sql`

The `transformation_sql` parameter is a SQL `SELECT` expression (without the `SELECT` keyword) that can rename columns, cast types, or compute derived values. It supports only **row-wise** expressions—aggregation functions like `COUNT(*)` or `SUM()` are not allowed here; use `AggregationFunction` on the feature instead. Examples include renames (`user_id`, `CAST(amount AS DOUBLE) AS amount`), and derived columns (`CAST(price_cents AS DOUBLE) / 100 AS price`). ^[declarative-features-api-reference-databricks-on-aws.md]

Because the system needs to know the schema of the resulting DataFrame, you **must** provide a `schema_json` argument (in Spark `StructType` JSON format) whenever `transformation_sql` is set. The recommended way to obtain the schema is to run the transformation in a PySpark query with `LIMIT 0` and call `df.schema.json()`. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
import pyspark.sql.functions as F

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
    schema_json=df.schema.json(),
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

## Combining Both

When `filter_condition` and `transformation_sql` are both set, the system applies the `WHERE` clause **after** the transformation—i.e., the `transformation_sql` expression is placed in the `SELECT` clause, and the `filter_condition` becomes the `WHERE` clause. This allows you to filter on derived columns:

```sql
SELECT CAST(price_cents AS DOUBLE) / 100 AS price, event_time
FROM raw_events
WHERE event_type = 'purchase'
```

^[declarative-features-api-reference-databricks-on-aws.md]

## Using `from_sql()` to Create a `DeltaTableSource`

As a convenience, you can create a `DeltaTableSource` from a simple SQL query using `DeltaTableSource.from_sql()`. The method parses the query to automatically extract the table name, `transformation_sql`, and `filter_condition`. Only simple `SELECT ... FROM ... [WHERE ...]` queries are supported; joins, subqueries, CTEs, and unions are rejected. You must provide a Spark client for schema inference. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import DeltaTableSource
from databricks.ml_features._spark_client._spark_client import SparkClient

spark_client = SparkClient()
source = DeltaTableSource.from_sql(
    spark_client=spark_client,
    sql="SELECT customer_id, event_ts, amount * 2 AS doubled_amount, amount FROM main.schema.table",
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

## Previewing the Data

Use `source.to_dataframe()` to preview the data that will be used for feature computation. This is useful for iterating on `filter_condition` and `transformation_sql` until they produce the expected results. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
source.to_dataframe().display()
```

^[declarative-features-api-reference-databricks-on-aws.md]

## Related Concepts

- [DeltaTableSource](/concepts/deltatablesource.md) – The data source object that accepts these parameters.
- [Declarative Feature Engineering API](/concepts/declarative-feature-engineering-api.md) – The overall API for building features.
- Feature – The feature definition that uses a `DeltaTableSource`.
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) – How aggregation (like `Sum`, `Avg`) is combined with filter and transformation.
- RollingWindow – Time‑window type commonly used with filtered features.

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
