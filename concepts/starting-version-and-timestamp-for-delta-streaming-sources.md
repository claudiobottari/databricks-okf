---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0271ddac5f1707ed5edd2ac88488704da90b89d991687277c24a7d5615fe2f20
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - starting-version-and-timestamp-for-delta-streaming-sources
    - timestamp for Delta streaming sources and Starting version
    - SVATFDSS
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: Starting version and timestamp for Delta streaming sources
description: Options (startingVersion, startingTimestamp) to control the starting point of Delta streaming reads without processing the entire table history.
tags:
  - streaming
  - delta-lake
  - configuration
timestamp: "2026-06-19T10:00:53.256Z"
---

# Starting version and timestamp for Delta streaming sources

**Starting version and timestamp for Delta streaming sources** refers to the optional configuration settings `startingVersion` and `startingTimestamp` that allow a Spark Structured Streaming query to begin reading from a [Delta Lake](/concepts/delta-lake.md) table at a commit other than the latest available version. By default, a streaming source starts with the most recent snapshot of the table and processes all future changes. Databricks recommends using the default starting point for most streaming workloads. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## `startingVersion`

The `startingVersion` option specifies the [Delta Lake Table](/concepts/delta-lake-table.md) version (commit number) from which to begin reading. All table changes committed **at or after** the given version are processed by the stream. If the specified version has already been cleaned up by the table's retention mechanisms, the stream fails to start. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

To find available commit versions, run `DESCRIBE HISTORY` on the table and examine the `version` column. As a special value, you can set `startingVersion` to `"latest"` to read only the most recent changes (i.e., the stream skips any existing data and processes only new commits after the query begins). ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## `startingTimestamp`

The `startingTimestamp` option specifies a point in time from which to start reading. All table changes committed **at or after** the given timestamp are read by the stream. If the timestamp precedes the earliest table commit, the stream begins with the earliest available version. The value accepts either:

- A timestamp string, for example `"2019-01-01T00:00:00.000Z"`.
- A date string, for example `"2019-01-01"`. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Important considerations

- **Mutual exclusivity**: You cannot set both `startingVersion` and `startingTimestamp` at the same time. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- **New queries only**: These options apply **only** when a streaming query first starts. Once the query has progressed and its checkpoint has recorded the state, the settings are ignored. To change the starting point of an already‑running stream, you must delete the checkpoint and restart. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- **Schema is the latest**: The schema used for the streaming source is always the **latest schema** of the [Delta Lake Table](/concepts/delta-lake-table.md), regardless of the starting version or timestamp. You must ensure no incompatible schema changes (e.g., column removal or type change) have occurred between the chosen starting point and the latest schema. Otherwise, the stream may return incorrect results. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- **Retention windows**: A streaming query must run at least once within the source table’s retention windows. The default windows are 7 days for data files removed by `VACUUM` and 30 days for the transaction log (`logRetentionDuration`). If the stream falls behind these windows, it fails with `DELTA_FILE_NOT_FOUND_DETAILED` and must be reset with a full refresh. Do **not** set `spark.sql.files.ignoreMissingFiles` to `true` as a workaround, because it silently produces incorrect results. If a stream’s schedule cannot keep up, increase the source table’s retention instead. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Example usage

The following Scala examples demonstrate how to use the options: ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

```scala
// Read changes starting from table version 5
spark.readStream
  .option("startingVersion", "5")
  .table("user_events")

// Read changes starting from a specific date
spark.readStream
  .option("startingTimestamp", "2018-10-18")
  .table("user_events")
```

## Related concepts

- Streaming checkpointing – How Structured Streaming stores progress and why checkpoint deletion is needed to reapply `startingVersion` or `startingTimestamp`.
- [Delta Lake Time Travel](/concepts/delta-lake-time-travel.md) – The `DESCRIBE HISTORY` command and table versioning.
- [VACUUM for Delta Lake](/concepts/delta-lake.md) – Retention of data files and transaction logs that affect which starting versions are available.
- Structured Streaming triggers – Options such as `Trigger.AvailableNow` that can be combined with starting‑point settings.
- [Delta Lake table history and data retention](/concepts/delta-lake-table-history-retention.md) – Configuring `logRetentionDuration` and `deletedFileRetentionDuration`.

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
