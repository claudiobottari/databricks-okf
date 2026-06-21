---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f72577ffc9bd8ddcbe659c3c88b74a06e196f9f33fd65ab3b34d9a7d3ec4e7c3
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - whole-table-operation-conflicts-in-delta-lake
    - WTOCIDL
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Whole Table Operation Conflicts in Delta Lake
description: Conflicts arising when a transaction reads or replaces the entire table while another concurrent operation modifies it, including sub-types WHOLE_TABLE_READ and WHOLE_TABLE_REPLACE.
tags:
  - delta-lake
  - concurrency
  - transaction-conflicts
timestamp: "2026-06-18T11:51:47.560Z"
---

# Whole Table Operation Conflicts in Delta Lake

**Whole Table Operation Conflicts** are a category of transaction conflicts in [Delta Lake](/concepts/delta-lake.md) that occur when a transaction attempts to scan or replace the entire content of a table while a concurrent write operation modifies the same table. These conflicts are surfaced as specific subconditions of the DELTA_CONCURRENT_APPEND error class (`SQLSTATE: 2D521`).

## Overview

In Delta Lake’s optimistic concurrency model, concurrent transactions are detected and resolved automatically through row-level conflict detection. When a transaction’s predicate or operation scope covers the entire table — for example, a full table scan or a full table overwrite — it conflicts with any concurrent modification that changes the table’s data. Delta Lake raises a `DELTA_CONCURRENT_APPEND` error with one of two whole‑table subtypes, each suggesting a different recovery action. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## WHOLE_TABLE_READ

The **WHOLE_TABLE_READ** subcondition occurs when a transaction attempts to read the entire table, but a concurrent operation has added or modified data since the transaction’s snapshot was taken.

> This transaction attempted to read the entire table, conflicting with the concurrent modification. Consider adding filters to your query to narrow the data scope or retrying the operation. Refer to `<docLink>` for more information.

^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Cause

A read transaction that scans an entire table (e.g., a `SELECT *` without a partition filter, or an aggregate over all rows) conflicts with any concurrent write that changes the table. Delta Lake cannot guarantee a consistent read of the full table if another transaction modifies it in parallel.

### Resolution

- **Add filter predicates** to the query to scope the read to a subset of the data (such as by partition column or a WHERE clause). This reduces the chance of conflict with concurrent writes.
- **Retry the operation**: if the conflicting write completes, the read can be re‑executed against the new snapshot.
- Use Delta Lake read modes such as `ignoreChanges` or time travel if the application can tolerate a stale snapshot.

## WHOLE_TABLE_REPLACE

The **WHOLE_TABLE_REPLACE** subcondition occurs when a concurrent operation replaces all data in the table (e.g., an `OVERWRITE` or `INSERT OVERWRITE` without a partition), conflicting with the current transaction.

> The concurrent operation replaced all data in the table. Please retry the operation. Refer to `<docLink>` for more information.

^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Cause

A concurrent write that truncates and replaces the entire table — for example, a `DELETE` without a filter, or a `CREATE OR REPLACE TABLE` — invalidates the snapshot being used by the current transaction. Any subsequent operation that reads or writes the table will see the conflict.

### Resolution

- **Retry the operation** after the conflicting write completes. The retry will start with the new table snapshot.
- Avoid full‑table overwrites in concurrent workflows when other transactions may be reading or writing the same table. Consider using partition‑level overwrites instead.

## Relationship to Other Conflict Types

Whole‑table conflicts are one of several subconditions within the `DELTA_CONCURRENT_APPEND` error class. Other subconditions include:

- **ROW_LEVEL_CHANGES** – the concurrent operation modified the same rows.
- **WITH_PARTITION_HINT** – the conflict occurred within a specific partition.
- **ALLOTTED_TIME_EXCEEDED** – row‑level conflict resolution timed out.
- **PROTOCOL_CHANGE** – the table protocol was upgraded concurrently.

See Delta Lake Transaction Conflicts for a complete list.

## Best Practices for Avoiding Whole Table Conflicts

- Use partition columns in queries to limit the scope of reads and writes.
- Prefer `INSERT OVERWRITE` with partition specifications instead of unpartitioned overwrites.
- Use Delta Live Tables or [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) to manage incremental updates rather than batch overwrites.
- Monitor [Delta Lake transaction history](/concepts/delta-lake-transaction-log.md) to detect patterns of frequent full‑table scans or overwrites.

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
