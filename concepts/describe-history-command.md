---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4685a4caf93e2bcae165e3aa4c230362732b92d9564b7fc672db1bf418a3a206
  pageDirectory: concepts
  sources:
    - restore-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - describe-history-command
    - DHC
  citations:
    - file: restore-databricks-on-aws.md
title: DESCRIBE HISTORY Command
description: Command used to retrieve the version history of a Delta table, enabling selection of a specific version for restore
tags:
  - delta-lake
  - sql-command
  - history
timestamp: "2026-06-19T20:14:29.248Z"
---

# DESCRIBE HISTORY Command

**`DESCRIBE HISTORY`** is a [Delta Lake](/concepts/delta-lake.md) SQL command that returns a list of version numbers for a [Delta table](/concepts/delta-lake-table.md). The command is commonly used to retrieve version identifiers needed for RESTORE operations, where a specific version (obtained from `DESCRIBE HISTORY`) can be used with `RESTORE TABLE ... TO VERSION AS OF`. ^[restore-databricks-on-aws.md]

## Usage

Although the source material does not specify the full syntax, the command is invoked as a SQL statement against an existing Delta table. For example:

```sql
DESCRIBE HISTORY employee
```

This returns a set of version numbers and associated metadata (timestamps, operation types, etc.) for each write to the table. ^[restore-databricks-on-aws.md]

## Related Commands

- [RESTORE Command](/concepts/restore-table-command.md) – Uses version numbers from `DESCRIBE HISTORY` to restore a table to a previous state.
- [Delta table](/concepts/delta-lake-table.md) – The table type that maintains a transaction log enabling history queries.

## Sources

- restore-databricks-on-aws.md

# Citations

1. [restore-databricks-on-aws.md](/references/restore-databricks-on-aws-b92cad28.md)
