---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c6cf972b4d1c312bf6025d7d7e3803eaacfb0bfac633e9fc80254ce425aa71cd
  pageDirectory: concepts
  sources:
    - describe-history-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-name-restrictions-in-describe-history
    - TNRIDH
    - table_name-restrictions-for-describe-history
    - TRFDH
  citations:
    - file: describe-history-databricks-on-aws.md
title: Table Name Restrictions in DESCRIBE HISTORY
description: The table name in DESCRIBE HISTORY must not include a temporal specification or options specification.
tags:
  - delta-lake
  - sql-syntax
  - restrictions
timestamp: "2026-06-19T18:30:58.386Z"
---

# Table Name Restrictions in DESCRIBE HISTORY

**Table Name Restrictions in DESCRIBE HISTORY** refer to the constraints on the `table_name` parameter when using the `DESCRIBE HISTORY` SQL command on Databricks. The `table_name` must identify an existing [Delta table](/concepts/delta-lake-table.md) and must **not** include a temporal specification or options specification. ^[describe-history-databricks-on-aws.md]

## Syntax

```sql
DESCRIBE HISTORY table_name
```

^[describe-history-databricks-on-aws.md]

## Restrictions

The `table_name` parameter has the following restrictions:

1. **Must reference an existing Delta table**: The command only works on tables that use the Delta Lake format.
2. **No temporal specification**: The table name cannot include time-travel syntax such as `@v` or `TIMESTAMP AS OF`.
3. **No options specification**: The table name cannot include option parameters typically used in table reads or writes.

These restrictions ensure that `DESCRIBE HISTORY` returns provenance information for the table as a whole, rather than for a specific point-in-time snapshot. ^[describe-history-databricks-on-aws.md]

## Purpose

`DESCRIBE HISTORY` returns provenance information — including the operation, user, timestamp, and other metadata — for each write operation performed on a Delta table. Table history is retained for 30 days. ^[describe-history-databricks-on-aws.md]

## Related Concepts

- [DESCRIBE HISTORY](/concepts/describe-history.md) — The full command documentation
- Delta table history — Overview of table provenance and versioning
- [Delta time travel](/concepts/delta-lake-time-travel.md) — Accessing previous versions of a Delta table
- table_changes function|table_changes — A function for reading change data from Delta tables
- Table name — General rules for table name resolution in Databricks SQL

## Sources

- describe-history-databricks-on-aws.md

# Citations

1. [describe-history-databricks-on-aws.md](/references/describe-history-databricks-on-aws-c4aeec74.md)
