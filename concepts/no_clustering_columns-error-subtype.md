---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 125bf0f46dd36adef4727ae3d02fbdbd8740fcde7130fd87636a33ced05f2fcc
  pageDirectory: concepts
  sources:
    - delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - no_clustering_columns-error-subtype
    - NES
    - NO_CLUSTERING_COLUMNS error subtype
  citations:
    - file: delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
title: NO_CLUSTERING_COLUMNS error subtype
description: A specific error raised when a command requiring clustering columns is run on a Liquid table that has no clustering columns defined.
tags:
  - delta-lake
  - error-handling
  - liquid-tables
timestamp: "2026-06-19T18:28:51.260Z"
---

# NO_CLUSTERING_COLUMNS error subtype

The **NO_CLUSTERING_COLUMNS** error is a subtype of the DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES error class (SQLSTATE: `0A000`). It occurs when a command such as `UPDATE`, `DELETE`, or `MERGE` is attempted on a [Liquid table](/concepts/liquid-tables.md) that has no clustering columns defined. Because the command requires predicates that reference clustering columns, it cannot proceed if no clustering columns exist. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Error message

The error message follows this template:

```
<command> command is not supported on Liquid tables without clustering columns.
```

For example:

```
UPDATE command is not supported on Liquid tables without clustering columns.
```

^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Cause

A Liquid table must have at least one [clustering column](/concepts/clustering-columns.md) defined for commands that evaluate predicates against clustering columns. When a table lacks any clustering columns, the engine cannot satisfy the predicate requirements of the requested command and raises `NO_CLUSTERING_COLUMNS`. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Resolution

Define one or more clustering columns on the Liquid table using a statement such as `ALTER TABLE ... CLUSTER BY`. After clustering columns are added, the command can reference them in its predicates and execute successfully.

## Related error subtypes

The `DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES` class includes three additional subtypes:

- **[NON_CLUSTERING_COLUMN](/concepts/clustering-columns.md)** – raised when a predicate references a column that is not a clustering column.
- **UNRESOLVED_COLUMN error subtype|UNRESOLVED_COLUMN** – raised when a column name in the predicate cannot be resolved among the available clustering columns.
- **UNSUPPORTED_EXPRESSION error subtype|UNSUPPORTED_EXPRESSION** – raised when the predicate contains an expression type that is not supported.

## Sources

- delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md

# Citations

1. [delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md](/references/delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws-b9f8e20f.md)
