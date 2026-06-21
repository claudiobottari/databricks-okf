---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9b94d73dff4c2aede872a583ade26b4234d1fbeeaacdbea276b5e05b5d3704d1
  pageDirectory: concepts
  sources:
    - describe-history-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - describe-history
    - Table History|DESCRIBE HISTORY
  citations:
    - file: describe-history-databricks-on-aws.md
title: DESCRIBE HISTORY
description: A Delta Lake SQL command that returns provenance information (operation, user, etc.) for each write to a Delta table.
tags:
  - delta-lake
  - sql-commands
  - provenance
timestamp: "2026-06-19T18:30:42.636Z"
---

---

title: DESCRIBE HISTORY
summary: SQL command to retrieve provenance information (operation, user, etc.) for each write to a Delta table
sources:
  - describe-history-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T15:10:56.532Z"
updatedAt: "2026-06-19T15:10:56.532Z"
tags:
  - delta-lake
  - sql-command
  - provenance
aliases:
  - describe-history
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# DESCRIBE HISTORY

**DESCRIBE HISTORY** is a SQL command in Databricks that returns provenance information for each write operation performed on a Delta table. It provides a detailed audit trail of changes, including the operation type, user who performed the operation, and other metadata. ^[describe-history-databricks-on-aws.md]

## Syntax

```sql
DESCRIBE HISTORY table_name
```

^[describe-history-databricks-on-aws.md]

## Parameters

- **table_name**: Identifies an existing [Delta Table](/concepts/delta-lake-table.md). The name must not include a temporal specification or options specification. ^[describe-history-databricks-on-aws.md]

## Retention

Table history is retained for **30 days**. After this period, historical information about write operations is no longer available through this command. ^[describe-history-databricks-on-aws.md]

## Use Cases

DESCRIBE HISTORY is commonly used for:

- **Auditing**: Tracking which users made changes to a table and when.
- **Debugging**: Understanding the sequence of operations that led to the current state of a table.
- **Data lineage**: Tracing the provenance of data through write operations.
- **Rollback planning**: Identifying specific versions of a table for [time travel](/concepts/delta-lake-time-travel.md) operations.

## Related Concepts

- [Delta Table](/concepts/delta-lake-table.md) — The underlying table format that supports history tracking.
- [Time Travel](/concepts/delta-lake-time-travel.md) — The ability to query previous versions of a Delta table using the history information.
- table_changes function|table_changes — A function that returns change data feed information for a table.
- Work with Table History — Detailed documentation on managing and querying table history.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and versioning.

## Sources

- describe-history-databricks-on-aws.md

# Citations

1. [describe-history-databricks-on-aws.md](/references/describe-history-databricks-on-aws-c4aeec74.md)
