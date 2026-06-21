---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c606a0abd3ad3e9d350ac7e2bdf5c2c8e7fed82297fd1c84542fb40d0d22a946
  pageDirectory: concepts
  sources:
    - describe-history-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - describe-history-syntax-constraints
    - DHSC
  citations:
    - file: describe-history-databricks-on-aws.md
title: DESCRIBE HISTORY syntax constraints
description: The table name used with DESCRIBE HISTORY must not include a temporal specification or options specification
tags:
  - delta-lake
  - sql-command
  - constraints
timestamp: "2026-06-19T15:11:10.596Z"
---

# DESCRIBE HISTORY syntax constraints

**DESCRIBE HISTORY** is a Delta Lake SQL statement that returns provenance information about each write to a Delta table, including the operation type, user, and timestamp. ^[describe-history-databricks-on-aws.md]

## Syntax

```sql
DESCRIBE HISTORY table_name
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| **table_name** | Identifies an existing [Delta Table](/concepts/delta-lake-table.md). The name must **not** include a [Temporal Specification|temporal specification](/concepts/temporal-specification-restriction-on-describe-history.md) or Options Specification|options specification. ^[describe-history-databricks-on-aws.md] |

The constraint on `table_name` is the primary syntactic restriction: the identifier must be a plain table reference without any time-travel (e.g., `@v1` or `TIMESTAMP AS OF`) or option clauses (e.g., `OPTIONS(...)`). This ensures the command operates on the full history of the table rather than a point-in-time view.

## Additional characteristics

- The command returns a row for each write operation, including the operation, user, and other metadata. ^[describe-history-databricks-on-aws.md]
- Table history is retained for 30 days. ^[describe-history-databricks-on-aws.md]

## Related concepts

- DESCRIBE DETAIL – Returns metadata about a Delta table’s current state.
- table_changes function|table_changes – A table-valued function that returns changes made to a Delta table over a range of versions.
- Work with table history – Detailed guidance on querying and managing table history.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer underlying these commands.

## Sources

- describe-history-databricks-on-aws.md

# Citations

1. [describe-history-databricks-on-aws.md](/references/describe-history-databricks-on-aws-c4aeec74.md)
