---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ceb7ecdb538ce6642e4adca3727280dbd3876f37e1cc07768edb93353e7fca5b
  pageDirectory: concepts
  sources:
    - delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - skipchangecommits-for-source-table-changes
    - SFSTC
  citations:
    - file: delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md
title: skipChangeCommits for Source Table Changes
description: Option to ignore transactions that delete or modify existing records in a Delta source table, processing only appends during streaming reads
tags:
  - delta-lake
  - streaming
  - structured-streaming
  - change-handling
timestamp: "2026-06-19T15:00:00.162Z"
---

# skipChangeCommits for Source Table Changes

The `skipChangeCommits` option is a configuration parameter for Spark Structured Streaming readers that read from [Delta Lake](/concepts/delta-lake.md) tables as a streaming source. When enabled, the streaming query ignores all commits that delete, update, or otherwise modify existing data in the source table, processing only new **append** transactions. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Purpose and Usage

Setting `skipChangeCommits` to `true` is the recommended approach for most streaming workloads that do not require full [change data feed](/concepts/delta-change-data-feed-cdf.md) (CDF) functionality. It allows a stream to continue running even when the source Delta table undergoes `UPDATE`, `DELETE`, `MERGE INTO`, or `OVERWRITE` operations, without failing or re-emitting modified rows. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

**Python example:**

```python
(spark.readStream
  .option("skipChangeCommits", "true")
  .table("source_table"))
```

**Scala example:**

```scala
spark.readStream
  .option("skipChangeCommits", "true")
  .table("source_table")
```

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Important Considerations

- **Schema changes cause failure:** If the schema of a [Delta Lake Table](/concepts/delta-lake-table.md) changes after the streaming read begins, the query fails. For most schema changes, restarting the stream resolves the mismatch. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- **Non‑additive schema evolution:** In Databricks Runtime 12.2 LTS and below, you cannot stream from a [Delta Lake Table](/concepts/delta-lake-table.md) with column mapping enabled that has undergone non‑additive schema evolution (renaming or dropping columns). ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- **Retention window:** Because no new data is read from skipped commits, the stream must run at least once within the source table’s retention window (7‑day file retention and 30‑day log retention by default) to avoid `DELTA_FILE_NOT_FOUND_DETAILED` errors. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Legacy Options

`skipChangeCommits` supersedes two earlier options:

| Option | Behaviour | Runtime support |
|--------|-----------|-----------------|
| `ignoreDeletes` | Handles only transactions that delete data at **partition boundaries** (full partition drops). Non‑partition deletes still cause the stream to fail. | Legacy; use `skipChangeCommits` instead unless deletes are always full partition drops. |
| `ignoreChanges` | Re‑emits rewritten data files after modifications (`UPDATE`, `MERGE INTO`, `DELETE` within partitions, `OVERWRITE`). Unchanged rows are often emitted alongside new rows, so downstream consumers must handle potential duplicates. Deletes are not propagated. | Databricks Runtime 11.3 LTS and lower only. In 12.2 LTS and above, `skipChangeCommits` replaces it. |

^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

`skipChangeCommits` provides a cleaner model: it **entirely ignores** file‑changing operations rather than re‑emitting modified data. To propagate modifications to downstream tables, you must implement separate logic (for example, by using [change data feed](/concepts/delta-change-data-feed-cdf.md)). ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Example: GDPR Delete Scenario

Suppose a table `user_events` is partitioned by `date` and you need to delete records for a specific `user_email` due to GDPR. With `skipChangeCommits` enabled, the stream continues to process only new appends and ignores the delete operation. Similarly, an `UPDATE` that rewrites a data file is skipped. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Recommendations

- Use `skipChangeCommits` for workloads that do not need to propagate updates or deletions downstream. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- If you need to react to all change types (inserts, updates, deletes), use [Delta Lake change data feed](/concepts/delta-lake-change-data-feed-cdf.md) instead. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]
- If you are certain that deletes are always full partition drops, `ignoreDeletes` may still be used, but `skipChangeCommits` is simpler and safer. ^[delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md]

## Related Concepts

- [Delta Lake table streaming reads and writes](/concepts/delta-lake-as-a-streaming-source-and-sink.md)
- Spark Structured Streaming
- [Change data feed](/concepts/delta-change-data-feed-cdf.md)
- ignoreDeletes for Delta Lake streaming
- ignoreChanges for Delta Lake streaming
- Delta Lake retention windows

## Sources

- delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md

# Citations

1. [delta-lake-table-streaming-reads-and-writes-databricks-on-aws.md](/references/delta-lake-table-streaming-reads-and-writes-databricks-on-aws-cb1a6ce2.md)
