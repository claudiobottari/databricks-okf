---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cee4ec62b1eeeaf5d4735532425af15fa710787cb3c8795f58e0f928ac4ef4c5
  pageDirectory: concepts
  sources:
    - delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - clustering-columns
    - NON_CLUSTERING_COLUMN
    - NO_CLUSTERING_COLUMNS
    - clustering column
    - Entity Columns
  citations:
    - file: delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
title: Clustering columns
description: Designated columns in a Liquid table used for data organization; certain commands on Liquid tables may only reference clustering columns in their predicates.
tags:
  - delta-lake
  - clustering
  - liquid-tables
timestamp: "2026-06-19T18:28:37.997Z"
---

```markdown
---
title: Clustering columns
summary: Columns designated for physical data clustering in Databricks Liquid tables, which are the only columns allowed in certain command predicates.
sources:
  - delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:10:21.319Z"
updatedAt: "2026-06-19T10:10:21.319Z"
tags:
  - databricks
  - delta-lake
  - data-organization
  - liquid-tables
aliases:
  - clustering-columns
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Clustering columns

**Clustering columns** are the columns designated to physically co-locate data in [[Delta Lake]] [[Liquid tables]] on Databricks. When a Liquid table defines clustering columns, certain data modification commands impose restrictions on which columns can appear in their predicates.

## Overview

Clustering columns control how data is stored and organized within a Liquid table. This physical clustering affects the performance of operations that depend on predicate filtering. The system enforces that only clustering columns may be referenced in the predicate of commands such as `UPDATE`, `DELETE`, and `MERGE` when they are run on a Liquid table. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Restrictions

### Non-clustering column predicates

If a command predicate references a column that is not a clustering column, the operation fails with the `NON_CLUSTERING_COLUMN` error condition. The error message reports the column name and lists the available clustering columns that may be used. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

### Missing clustering columns

If a Liquid table is created without any clustering columns, commands that require clustering support (such as `UPDATE`, `DELETE`, or `MERGE`) are not allowed. The `NO_CLUSTERING_COLUMNS` error indicates that the command is unsupported on a Liquid table that lacks clustering columns. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

### Unresolved columns

If a predicate references a column name that cannot be resolved among the defined clustering columns, the `UNRESOLVED_COLUMN` error is raised. The error message lists the available clustering columns that the predicate could have referenced. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

### Unsupported expressions

Certain expressions used in predicates against clustering columns are not accepted. The `UNSUPPORTED_EXPRESSION` error is raised when such an expression is encountered. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Related concepts

- [[Liquid tables]] – The table type that supports clustering columns.
- [[Delta Lake]] – The storage layer that implements Liquid tables and clustering.
- Delta table commands – Data modification commands (UPDATE, DELETE, MERGE) affected by clustering column restrictions.

## Sources

- delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md](/references/delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws-b9f8e20f.md)
