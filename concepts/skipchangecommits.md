---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 97a200ed7dda8737b6f7d4d2bff25b91ae26bb9177bd54a0402c016518e9ec92
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - skipchangecommits
    - skipchangecommits-for-handling-source-table-modifications
    - SFHSTM
    - skipchangecommits-for-source-table-changes
    - SFSTC
    - skipchangecommits-for-streaming-sources
    - SFSS
    - Skip Change Commits for Delta Streaming
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: skipChangeCommits
description: Option to ignore data modification transactions (UPDATE, DELETE, MERGE, OVERWRITE) in a Delta Lake streaming source, processing only appends.
tags:
  - structured-streaming
  - delta-lake
  - configuration
timestamp: "2026-06-19T18:20:55.553Z"
---

# skipChangeCommits

**skipChangeCommits** is a configuration option for Spark Structured Streaming when reading from [Delta Lake](/concepts/delta-lake.md) tables as a streaming source. When enabled, it allows the streaming query to ignore transactions that modify or delete existing records, processing only append operations. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Overview

When a streaming query reads from a [Delta Lake Table](/concepts/delta-lake-table.md), it processes new records as new table versions commit to the source. By default, Structured Streaming only accepts append inputs and throws an error if any upstream modifications (such as `UPDATE`, `DELETE`, `MERGE INTO`, or `OVERWRITE`) occur on the source table. The `skipChangeCommits` option provides a mechanism to bypass this restriction by ignoring file-changing operations entirely. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Behavior

With `skipChangeCommits` enabled, rewritten data files in the source table due to data modification operations are ignored. This means:
- Deletes are not propagated downstream
- Updates to existing records are not reflected
- Overwrite operations are disregarded

The stream continues processing only new append data, and unchanged rows are not re-emitted. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Usage

To enable `skipChangeCommits` on a streaming source:

```python
(spark.readStream
  .option("skipChangeCommits", "true")
  .table("source_table"))
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Recommended for Most Workloads

Databricks recommends using `skipChangeCommits` for most workloads that do not use [Change Data Feed](/concepts/delta-change-data-feed-cdf.md). It is the preferred option over legacy alternatives because it provides cleaner behavior by disregarding any data modification operations. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Version History

- **Databricks Runtime 12.2 LTS and above**: `skipChangeCommits` is the standard option
- **Databricks Runtime 11.3 LTS and lower**: Only `ignoreChanges` is supported as a legacy option ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Comparison with Legacy Options

| Option | Behavior | Recommended Use |
|--------|----------|-----------------|
| `skipChangeCommits` | Ignores all file-changing operations; only processes appends | Most workloads |
| `ignoreChanges` | Re-emits rewritten data files (including unchanged rows); handles only duplicates | Legacy, replaced by `skipChangeCommits` in DBR 12.2+ |
| `ignoreDeletes` | Only handles partition-level deletes | Legacy, limited to full partition drops |

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Important Considerations

- If the schema of a [Delta Lake Table](/concepts/delta-lake-table.md) changes after a streaming read begins, the query fails. Most schema mismatches can be resolved by restarting the stream. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- For workloads that need to process all types of changes (inserts, updates, and deletes), use [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) instead of `skipChangeCommits`. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- The streaming query must run at least once within the source table's retention window (7 days for `VACUUM`-removed files, 30 days for transaction log). ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- Delta Lake streaming
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md)
- ignoreChanges
- ignoreDeletes
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md)

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
