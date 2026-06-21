---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 426f008be1442126b064e80e4d6ff52703260229f668d5dc72a03feece3ed237
  pageDirectory: concepts
  sources:
    - describe-history-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-table-history-retention
    - DLTHR
    - Delta Lake table history and data retention
    - Managing Delta Lake table history
  citations:
    - file: describe-history-databricks-on-aws.md
title: Delta Lake table history retention
description: Delta Lake retains table history metadata for 30 days by default
tags:
  - delta-lake
  - retention
  - governance
timestamp: "2026-06-19T15:11:05.624Z"
---

# [Delta Lake Table](/concepts/delta-lake-table.md) History Retention

**Delta Lake table history retention** refers to the default 30‑day preservation period for provenance information recorded for every write operation on a [Delta Lake](/concepts/delta-lake.md) table. This history enables auditing, debugging, and time‑travel queries and is accessible through the [DESCRIBE HISTORY](/concepts/describe-history.md) SQL command. ^[describe-history-databricks-on-aws.md]

## Overview

When a write operation (e.g., `INSERT`, `UPDATE`, `DELETE`, `MERGE`) is performed on a Delta table, Delta Lake automatically stores metadata about the operation. This metadata includes the operation type, the user who performed it, the timestamp, and other operational details. The accumulated records form the table’s history. ^[describe-history-databricks-on-aws.md]

## Retention Period

By default, table history is retained for **30 days**. After this period, records of older write operations may be automatically purged and are no longer available through `DESCRIBE HISTORY`. The source material does not describe a mechanism to change this retention period. ^[describe-history-databricks-on-aws.md]

## Viewing Table History

Use the `DESCRIBE HISTORY` statement to view the retained history for a specific Delta table. The command returns one row per write operation, sorted with the most recent operation first. ^[describe-history-databricks-on-aws.md]

```sql
DESCRIBE HISTORY table_name;
```

The table name must not include a temporal specification or options specification. ^[describe-history-databricks-on-aws.md]

## Related Concepts

- [DESCRIBE HISTORY](/concepts/describe-history.md) — The SQL command that exposes table history.
- Work with table history — Detailed guidance on using history information.
- table_changes function|table_changes — A function for retrieving row‑level changes.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions, history, and time travel.

## Sources

- describe-history-databricks-on-aws.md

# Citations

1. [describe-history-databricks-on-aws.md](/references/describe-history-databricks-on-aws-c4aeec74.md)
