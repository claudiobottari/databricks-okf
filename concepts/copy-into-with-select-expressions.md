---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c965a21ff3a378acdaf0be62c5e4ff1b583fbfed620a32e2d466f15556c1f921
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-with-select-expressions
    - CIWSE
  citations:
    - file: copy-into-databricks-on-aws.md
title: COPY INTO with SELECT Expressions
description: The ability to specify SELECT expressions including window operations and global aggregates when loading source data into a Delta table
tags:
  - databricks
  - sql
  - etl
timestamp: "2026-06-19T09:25:40.166Z"
---

---
title: COPY INTO with SELECT Expressions
summary: Using SQL SELECT expressions inside the COPY INTO statement to transform data before loading into a Delta table, including window operations and global aggregates.
sources:
  - copy-into-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:18:43.797Z"
updatedAt: "2026-06-18T08:18:43.797Z"
tags:
  - sql
  - data-ingestion
  - delta-lake
aliases:
  - copy-into-select-expressions
  - CISE
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# COPY INTO with SELECT Expressions

**COPY INTO with SELECT Expressions** is a variant of the [COPY INTO](/concepts/copy-into-command.md) command that allows you to transform source data using arbitrary SQL expressions before loading it into a [Delta table](/concepts/delta-lake-table.md). This feature enables in-flight data manipulation such as column renaming, type casting, computed columns, and even window functions, reducing the need for separate staging or transformation steps. ^[copy-into-databricks-on-aws.md]

## Syntax

The `SELECT` clause is placed inside parentheses after the `FROM` keyword in the `COPY INTO` statement:

```sql
COPY INTO target_table
  FROM (
    SELECT expression_list
    FROM source_clause
  )
  FILEFORMAT = data_source
  [ ... other options ... ]
```

Where `expression_list` is one or more column expressions, and `source_clause` specifies the file location (with optional credentials). ^[copy-into-databricks-on-aws.md]

## Capabilities

The expressions in the `SELECT` list can include any construct supported by standard SQL `SELECT` statements. This includes:

- **Column references and aliases** – Select and rename specific columns from the source files.
- **Computed columns** – Apply functions, arithmetic, or string manipulations.
- **Window operations** – Use `ROW_NUMBER()`, `LAG()`, `LEAD()`, and other window functions to compute values based on partitions of the data. ^[copy-into-databricks-on-aws.md]
- **Aggregate functions** – Only as **global aggregates** (applied over the entire dataset). `GROUP BY` is **not** allowed in this context. For example, you can compute `SUM(amount)` or `AVG(price)` over all rows in the source. ^[copy-into-databricks-on-aws.md]

## Limitations

- **Aggregation without grouping** – You can use aggregation expressions only for global aggregates; you **cannot** `GROUP BY` on columns. This means that window-based aggregations (e.g., `SUM() OVER (PARTITION BY ...)`) are also not allowed because they implicitly involve grouping. ^[copy-into-databricks-on-aws.md]
- **No `GROUP BY` clause** – The `SELECT` list is applied to the entire source as a single batch; any aggregation must be over all rows.

## Use Cases

- **Clean data on ingestion** – Filter out unwanted columns or transform data types before writing to the Delta table.
- **Enrich with row numbers or ranks** – Use window functions to add sequential identifiers or rank values before loading.
- **Compute summary statistics** – Calculate global aggregates like total sales or average temperature and store them alongside raw data (e.g., as a constant column).

## Related Concepts

- [COPY INTO](/concepts/copy-into-command.md) – The base command for incremental, idempotent data loading.
- [Delta table](/concepts/delta-lake-table.md) – The target storage format for COPY INTO.
- SQL SELECT – The standard SQL statement that forms the basis of the expression list.
- Window functions – Advanced analytics functions usable in the SELECT expressions.
- Aggregate functions – Functions like `SUM`, `AVG`, `COUNT` allowed only as global aggregates.

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
