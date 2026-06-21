---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 458e8fb955257d1dfbc45c4e63a191c391886d543cab21ffdae0f6434c514553
  pageDirectory: concepts
  sources:
    - delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non_clustering_column-error-subtype
    - NES
    - NON_CLUSTERING_COLUMN error subtype
  citations:
    - file: delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
title: NON_CLUSTERING_COLUMN error subtype
description: A specific error within DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES raised when a predicate references a column that is not a clustering column.
tags:
  - delta-lake
  - error-handling
  - liquid-tables
timestamp: "2026-06-19T18:29:19.986Z"
---

#NON_CLUSTERING_COLUMN error subtype

**NON_CLUSTERING_COLUMN** is an error subtype of the DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES error class (SQLSTATE 0A000). It occurs when a command is executed on a [Liquid table](/concepts/liquid-tables.md) and the predicate references a column that is **not** a [clustering column](/concepts/clustering-columns.md), while the command requires that only clustering columns be used in the predicate. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Error Message

The error message takes the following form:

```
<command> predicate references non-clustering column '<columnName>'. Only the clustering columns may be referenced when <command> is run on a Liquid table: [<columnList>].
```

Where:

- `<command>` – the specific command being executed (e.g., `DELETE`, `MERGE`, `UPDATE`).
- `<columnName>` – the non-clustering column referenced in the predicate.
- `<columnList>` – the list of allowed clustering columns for the Liquid table.

^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Cause

Liquid tables impose a restriction that certain commands can only filter rows using predicates that involve clustering columns. If a predicate includes a column that is not designated as a clustering column, the engine raises this error. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Solution

Modify the command predicate to reference only columns that appear in the `<columnList>` provided in the error message (the clustering columns of the table). Alternatively, if the operation does not need to be restricted to clustering columns, consider restructuring the query or altering the table’s clustering configuration. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES error class – The parent error class containing this and other related subtypes.
- [Liquid tables](/concepts/liquid-tables.md) – The table type that enforces clustering column predicate restrictions.
- [Clustering columns](/concepts/clustering-columns.md) – Columns used for data distribution and query optimization in Liquid tables.
- [NO_CLUSTERING_COLUMNS](/concepts/clustering-columns.md) – Another subtype, raised when the table has no clustering columns at all.
- UNRESOLVED_COLUMN error subtype|UNRESOLVED_COLUMN – Error when a column name cannot be resolved among the clustering columns.
- UNSUPPORTED_EXPRESSION error subtype|UNSUPPORTED_EXPRESSION – Error for unsupported predicate expressions.

## Sources

- delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md

# Citations

1. [delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md](/references/delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws-b9f8e20f.md)
