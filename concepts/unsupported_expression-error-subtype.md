---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d0f7d979683bca191118d6fd0b756b2dca7d83f5a7a99b7e35d7760ff778ac1a
  pageDirectory: concepts
  sources:
    - delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unsupported_expression-error-subtype
    - UES
    - UNSUPPORTED_EXPRESSION error subtype
    - UNSUPPORTED_EXPRESSION
  citations:
    - file: delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md
title: UNSUPPORTED_EXPRESSION error subtype
description: A specific error raised when an unsupported expression is used in a predicate for a command on a Liquid table.
tags:
  - delta-lake
  - error-handling
  - liquid-tables
timestamp: "2026-06-19T18:28:50.197Z"
---

#UNSUPPORTED_EXPRESSION Error Subtype

The **UNSUPPORTED_EXPRESSION** error subtype is a specific condition within the DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES error class (SQLSTATE `0A000`, Feature Not Supported). It is raised when a command executed on a [Liquid table](/concepts/liquid-tables.md) contains a predicate expression that the command does not support. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Error Message

When this error occurs, the following message is returned:

```
Unsupported expression: <expression>.
```

The `<expression>` placeholder is replaced with the actual unsupported predicate expression that caused the failure. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Cause

The error indicates that the provided predicate expression (for example, in a `WHERE` clause or other predicate context) is not valid for the specific command being run against a Liquid table. The command’s predicate logic can only use expressions that the Liquid table’s execution engine supports. ^[delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md]

## Related Subtypes

The DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES error class includes several other subtypes that identify specific constraint violations:

- [NON_CLUSTERING_COLUMN](/concepts/clustering-columns.md) – The predicate references a column that is not a clustering column.
- [NO_CLUSTERING_COLUMNS](/concepts/clustering-columns.md) – The command is run on a Liquid table that has no clustering columns.
- UNRESOLVED_COLUMN error subtype|UNRESOLVED_COLUMN – The predicate column cannot be resolved against the available clustering columns.

## Related Concepts

- [Liquid tables](/concepts/liquid-tables.md) – The Delta Lake feature where [Clustering columns](/concepts/clustering-columns.md) are used for data layout.
- Delta Lake error classes – The classification system for Delta Lake runtime errors.
- SQLSTATE 0A000 – Class for feature not supported errors.

## Sources

- delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md

# Citations

1. [delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws.md](/references/delta_unsupported_clustering_column_predicates-error-condition-databricks-on-aws-b9f8e20f.md)
