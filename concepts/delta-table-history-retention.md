---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a954406b221b54d73e66012dd805a8b9f83ab7db540b2030e243082b680f540f
  pageDirectory: concepts
  sources:
    - describe-history-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-table-history-retention
    - DTHR
  citations:
    - file: describe-history-databricks-on-aws.md
title: Delta Table History Retention
description: The period (30 days) for which Delta Lake retains write history for a table.
tags:
  - delta-lake
  - retention
  - history
timestamp: "2026-06-19T18:30:54.992Z"
---

# Delta Table History Retention

**Delta Table History Retention** refers to the period during which [Delta Lake](/concepts/delta-lake.md) retains provenance information about write operations to a table. This information includes the operation type, user, timestamp, and other metadata for each write, enabling auditing, debugging, and [time travel queries](/concepts/delta-lake-time-travel.md). ^[describe-history-databricks-on-aws.md]

## Retention Period

By default, Delta table history is retained for **30 days**. ^[describe-history-databricks-on-aws.md] After this period, historical metadata may be cleaned up and is no longer accessible through commands such as `DESCRIBE HISTORY` or `table_changes`.

## Viewing Table History

Use the `DESCRIBE HISTORY` SQL command to retrieve the provenance information for a Delta table: ^[describe-history-databricks-on-aws.md]

```sql
DESCRIBE HISTORY table_name
```

The `table_name` must identify an existing Delta table and **must not** include a temporal specification or options specification. ^[describe-history-databricks-on-aws.md] The command returns one row per write operation, including the operation (e.g., WRITE, MERGE, DELETE), the user who performed it, and a timestamp. ^[describe-history-databricks-on-aws.md]

For more details on working with table history, see Work with table history. ^[describe-history-databricks-on-aws.md]

## Related Functions

The `table_changes` function can also be used to query row-level changes for tables with [change data feed](/concepts/delta-change-data-feed-cdf.md) enabled, leveraging the same historical metadata retained by the 30-day retention policy. ^[describe-history-databricks-on-aws.md]

## Related Concepts

- [DESCRIBE HISTORY](/concepts/describe-history.md) — The SQL command to view table history.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and time travel.
- [Time Travel](/concepts/delta-lake-time-travel.md) — Querying previous versions of a Delta table.
- table_changes function|table_changes — Function for retrieving row-level changes.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — Feature that records row-level changes for downstream processing.
- Work with table history — Detailed documentation on managing table provenance.

## Sources

- describe-history-databricks-on-aws.md

# Citations

1. [describe-history-databricks-on-aws.md](/references/describe-history-databricks-on-aws-c4aeec74.md)
