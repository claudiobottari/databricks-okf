---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e95348308ba8f62ac2a0f3d004202c61bb916e413378afb1f3e2ae0d8189c697
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-streaming-retention-window-and-failure-handling
    - failure handling and Delta Lake streaming retention window
    - DLSRWAFH
    - Delta Lake Source Retention Windows
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
    - file: delta-lake-table-streaming-reads-and-databricks-on-aws.md
title: Delta Lake streaming retention window and failure handling
description: Streaming queries from Delta tables must run within the VACUUM retention window (7 days for data files, 30 days for transaction logs) or they fail with DELTA_FILE_NOT_FOUND_DETAILED.
tags:
  - streaming
  - delta-lake
  - error-handling
timestamp: "2026-06-19T10:00:27.894Z"
---

# Delta Lake Streaming Retention Window and Failure Handling

**Delta Lake streaming retention window and failure handling** refers to the time limits within which streaming queries must process data from a Delta Lake source, and the strategies for recovering when those limits are exceeded. Delta Lake uses retention windows to manage data files and transaction log entries; if a streaming query falls behind these windows, it will fail and require manual intervention. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Retention Windows

Delta Lake has two default retention windows that directly affect streaming reads:

| Retention policy | Default duration | Purpose |
|------------------|------------------|---------|
| `VACUUM`-removed data files | 7 days | Data files no longer referenced by the table’s current version are physically deleted. |
| Transaction log (`logRetentionDuration`) | 30 days | Old transaction log entries (commits) are cleaned up, making earlier table versions unavailable for time travel. |

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

A streaming query that reads from a [Delta Lake Table](/concepts/delta-lake-table.md) must run at least once within the source table’s retention window. If the query falls behind these windows (for example, because it was stopped for a long period), it can no longer access the required data files or log entries. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Failure Modes

### `DELTA_FILE_NOT_FOUND_DETAILED`

When a streaming query cannot find data files or transaction log entries that it needs to process, it fails with the error `DELTA_FILE_NOT_FOUND_DETAILED`. This occurs when:

- The query has been idle longer than the data file retention window (7 days by default), so `VACUUM` has removed the underlying files.
- The query has been idle longer than the transaction log retention window (30 days by default), so log entries needed to reconstruct the table state are gone.

In either case, the stream must be reset with a full refresh. ^[delta-lake-table-streaming-reads-and-databricks-on-aws.md]

### Unavailable Starting Version or Timestamp

When using the `startingVersion` or `startingTimestamp` options to set an initial read point, the stream fails to start if the requested version or timestamp is no longer available (e.g., because the transaction log has been cleaned up). ^[delta-lake-table-streaming-reads-and-databricks-on-aws.md]

### Transaction Log Cleanup During Active Streaming

Even during active streaming, if the source table’s `logRetentionDuration` setting causes old transaction logs to be cleaned up, the streaming query will fail to prevent data loss. This is the default behavior (`failOnDataLoss=true`). ^[delta-lake-table-streaming-reads-and-databricks-on-aws.md]

## Handling Failures

### Recommended: Increase Source Table Retention

If a streaming query’s schedule cannot keep up with the default retention windows, the recommended fix is to increase the retention settings on the source [Delta Lake Table](/concepts/delta-lake-table.md). This gives the stream more time to catch up before the data or logs are removed. ^[delta-lake-table-streaming-reads-and-databricks-on-aws.md]

### Full Refresh

When a stream has fallen behind and fails with `DELTA_FILE_NOT_FOUND_DETAILED`, the only recovery option is to perform a **full refresh**: delete the streaming checkpoint and output table, then restart the stream from the beginning. This causes all data in the source table to be reprocessed. ^[delta-lake-table-streaming-reads-and-databricks-on-aws.md]

### `failOnDataLoss` Option

By default, if the transaction log cleans up entries that the streaming query still needs, the query fails with `failOnDataLoss=true`. You can set `failOnDataLoss` to `false` to ignore the lost data and continue processing from the latest available state. This should be used with caution because it can lead to silent data loss. ^[delta-lake-table-streaming-reads-and-databricks-on-aws.md]

### Do NOT Use `spark.sql.files.ignoreMissingFiles`

Setting `spark.sql.files.ignoreMissingFiles` to `true` is **not** a valid workaround for retention‑related failures. This configuration silently produces incorrect results and must never be used to bypass a missing‑file error. ^[delta-lake-table-streaming-reads-and-databricks-on-aws.md]

## Best Practices

- **Monitor stream backlog.** Use streaming query metrics such as `numBytesOutstanding` and `numFilesOutstanding` to detect when a stream is falling behind the retention window. ^[delta-lake-table-streaming-reads-and-databricks-on-aws.md]
- **Plan for downtime.** If a stream must be stopped for longer than the retention window, plan to perform a full refresh upon restart, or increase the retention window beforehand.
- **Increase retention proactively.** For streams with known long idle periods (e.g., nightly batch schedules), increase `logRetentionDuration` and the `VACUUM` retention threshold on the source table.
- **Avoid `failOnDataLoss=false` except in controlled circumstances.** Only disable the fail‑on‑data‑loss guard if you fully accept that some data may be skipped.
- **Use `skipChangeCommits` to avoid re‑processing modifications.** While not directly about retention, using `skipChangeCommits` reduces the number of files the stream must read, which can help the stream keep up. ^[delta-lake-table-streaming-reads-and-databricks-on-aws.md]

## Related Concepts

- Delta Lake VACUUM – The operation that physically removes old data files.
- Time Travel in Delta Lake – Reading previous table versions, which depends on transaction log retention.
- Structured Streaming Checkpoints – The mechanism that tracks stream progress; deleted checkpoints force a full refresh.
- Streaming Query Metrics – Using `numBytesOutstanding` to monitor backlog.
- [skipChangeCommits](/concepts/skipchangecommits.md) – Option to ignore data modification operations in a streaming source.

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
2. delta-lake-table-streaming-reads-and-databricks-on-aws.md
