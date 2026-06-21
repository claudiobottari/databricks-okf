---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c68aa6c83b8ad09c2fca7e302212da7b0143671644140208d557c2143878192b
  pageDirectory: concepts
  sources:
    - describe-history-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-table-history-operations
    - DTHO
  citations:
    - file: describe-history-databricks-on-aws.md
title: Databricks table history operations
description: Broader topic covering how to work with Delta table history, including DESCRIBE HISTORY and related tools, documented separately in the Databricks guide.
tags:
  - delta-lake
  - history
  - operations
timestamp: "2026-06-18T15:27:18.100Z"
---



# Databricks table history operations

**Databricks table history operations** refers to the ability to query and retrieve provenance information for each write operation performed on a Delta table. This feature is part of the [Delta Lake](/concepts/delta-lake.md) transaction log and enables users to audit changes, track data lineage, and understand how a table evolved over time.

## Overview

The `DESCRIBE HISTORY` command returns metadata about every operation that has modified a Delta table, including details such as which operation was performed, who executed it, and when it occurred. This provenance information is retained for **30 days** by default.^[describe-history-databricks-on-aws.md]

## Syntax

```sql
DESCRIBE HISTORY table_name
```

The `table_name` parameter must identify an existing Delta table. The name must not include a temporal specification or options specification.^[describe-history-databricks-on-aws.md]

## Usage

`DESCRIBE HISTORY` returns provenance information for each write operation to a Delta table. Use this command to:

- Audit data modifications
- Track data lineage and evolution
- Recover from unintended changes
- Understand operation timing and execution details

The output includes:

- **Timestamp** when the operation occurred
- **Operation type** (e.g., WRITE, MERGE, UPDATE, DELETE, TRUNCATE)
- **Operation parameters** specific to each write
- **User** who performed the operation
- **Isolation level** used during the operation (e.g., `SnapshotIsolation`, `Serializable`)
- **Operation metrics** providing additional metadata about the operation's impact (e.g., number of files added, records read/written)

## Related concepts

- table_changes function|Table changes – The `table_changes` function for reading changes
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) – The underlying mechanism that stores operation history
- Work with table history – Extended guidance on using table history
- [Time travel queries](/concepts/delta-lake-time-travel.md) – Querying previous versions of a Delta table

## Sources

- describe-history-databricks-on-aws.md

# Citations

1. [describe-history-databricks-on-aws.md](/references/describe-history-databricks-on-aws-c4aeec74.md)
