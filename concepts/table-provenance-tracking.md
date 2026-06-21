---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3f0aa32cab9fdafc2de3e85d52ecd6baa4952e1abcded20555c3cbb3eb765343
  pageDirectory: concepts
  sources:
    - describe-history-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-provenance-tracking
    - TPT
    - table-provenance-tracking-in-delta-lake
    - TPTIDL
  citations:
    - file: describe-history-databricks-on-aws.md
title: Table provenance tracking
description: Delta Lake tracks metadata for each write operation including the operation type, user, and other provenance information.
tags:
  - delta-lake
  - provenance
  - audit
timestamp: "2026-06-18T12:00:01.164Z"
---

# Table Provenance Tracking

**Table provenance tracking** refers to the ability to view the history of operations performed on a Delta table, including details about when each change occurred, who made it, and what type of operation was executed. This capability is essential for auditing data lineage, debugging unintended changes, and understanding the evolution of a table over time. ^[describe-history-databricks-on-aws.md]

## Overview

Databricks maintains a history log for every [Delta table](/concepts/delta-lake-table.md) that records information about each write operation. This log provides a detailed audit trail of the table's provenance, capturing metadata about every change, including the operation type, the user who performed it, and the timestamp of the operation. ^[describe-history-databricks-on-aws.md]

By default, table history is retained for **30 days**. After this period, older history entries may no longer be available. ^[describe-history-databricks-on-aws.md]

## Viewing Table History with DESCRIBE HISTORY

The primary SQL command for table provenance tracking is `DESCRIBE HISTORY`. This command returns provenance information for each write operation on a table. ^[describe-history-databricks-on-aws.md]

### Syntax

```sql
DESCRIBE HISTORY table_name
```

The `table_name` parameter must identify an existing Delta table. The name must not include a temporal specification or options specification. ^[describe-history-databricks-on-aws.md]

### Output

The `DESCRIBE HISTORY` command returns a result set with the following columns for each write operation:

| Column Name | Description |
|-------------|-------------|
| `version` | The version number of the table after the operation |
| `timestamp` | When the operation was committed |
| `userId` | The identifier of the user who performed the operation |
| `userName` | The name of the user who performed the operation |
| `operation` | The type of operation (e.g., WRITE, DELETE, MERGE, UPDATE) |
| `operationParameters` | Parameters specific to the operation |
| `job` | Information about the job that ran the operation (if applicable) |
| `notebook` | Information about the notebook that ran the operation (if applicable) |
| `clusterId` | The cluster where the operation was executed |
| `readVersion` | The version of the table that was read before writing |
| `isolationLevel` | The isolation level used for the operation |
| `isBlindAppend` | Whether the operation appended data without reading existing data |
| `operationMetrics` | Metrics about the operation (e.g., number of files added, number of rows affected) |
| `userMetadata` | Optional user-specified metadata |

^[describe-history-databricks-on-aws.md]

## Use Cases

### Auditing Data Changes

Table provenance tracking allows data engineers and administrators to audit who made changes to a table and when. This is critical for [data governance](/concepts/ai-governance.md) and compliance with regulatory requirements. ^[describe-history-databricks-on-aws.md]

### Debugging Data Issues

When unexpected data quality issues arise, table history can help identify which operation introduced the problem and who was responsible. Teams can inspect the `operationParameters` and `operationMetrics` columns to understand the scope of each change. ^[describe-history-databricks-on-aws.md]

### Understanding Table Evolution

By reviewing the sequence of operations on a table, teams can understand how the table has evolved over time, including schema changes, data loads, and cleanup operations. ^[describe-history-databricks-on-aws.md]

### Enabling Time Travel

Table history provides the foundation for [Delta Time Travel](/concepts/delta-lake-time-travel.md), which allows querying historical versions of a table. The version numbers returned by `DESCRIBE HISTORY` can be used with time travel queries to access previous states of the data. ^[describe-history-databricks-on-aws.md]

## Limitations

- History is retained for **30 days** only. Operations older than 30 days are not available via `DESCRIBE HISTORY`. ^[describe-history-databricks-on-aws.md]
- The command only returns information about write operations. Read operations are not tracked in the table history. ^[describe-history-databricks-on-aws.md]
- The table name must not include temporal specifications or options specifications. ^[describe-history-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and versioned data
- [Delta Time Travel](/concepts/delta-lake-time-travel.md) — Querying historical versions of a Delta table using version numbers or timestamps
- table_changes function|table_changes Function — A SQL function that returns changes made to a Delta table by specifying a starting version
- [Data Lineage](/concepts/data-lineage.md) — Broader concept of tracking data through its lifecycle, including transformations and dependencies
- Audit Logging for Unity Catalog — Higher-level audit logging for governance operations in Unity Catalog

## Sources

- describe-history-databricks-on-aws.md

# Citations

1. [describe-history-databricks-on-aws.md](/references/describe-history-databricks-on-aws-c4aeec74.md)
