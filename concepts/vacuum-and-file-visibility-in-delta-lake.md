---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e7e6aea024bcb34c0ea203679beb84e17f9261a835683f859ee5fa9b92bad66
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - vacuum-and-file-visibility-in-delta-lake
    - File Visibility in Delta Lake and VACUUM
    - VAFVIDL
    - DELETE and VACUUM
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: VACUUM and File Visibility in Delta Lake
description: The caveat that files not tracked by the Delta Lake transaction log are invisible to Delta Lake and can be deleted by VACUUM, meaning writes during conversion must go through Delta Lake.
tags:
  - delta-lake
  - data-integrity
  - maintenance
timestamp: "2026-06-19T14:26:23.936Z"
---

Here is the wiki page for "VACUUM and File Visibility in Delta Lake".

---

## VACUUM and File Visibility in Delta Lake

**VACUUM and File Visibility in Delta Lake** describes the relationship between the `VACUUM` command and the Delta Lake transaction log. Only files tracked by the [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) are considered visible to queries and operations. The `VACUUM` command removes files that are not tracked, freeing storage space.

### Overview

Delta Lake uses a transaction log to maintain a manifest of all valid data files in a table. This log is the source of truth for what data is currently available. Any file not listed in the transaction log is considered invisible and is a candidate for garbage collection. ^[convert-to-delta-databricks-on-aws.md]

### The `VACUUM` Command

The `VACUUM` command deletes files that are no longer referenced by the Delta Lake transaction log. This includes:

- Files that have been overwritten by newer data versions.
- Files that have been removed as part of a `DELETE`, `UPDATE`, or `MERGE` operation.
- Files that were never part of a valid Delta table state.

Running `VACUUM` is the standard mechanism for reclaiming storage space and managing the physical size of a Delta table. ^[convert-to-delta-databricks-on-aws.md]

### File Visibility

A file becomes **visible** to Delta Lake queries only when it is recorded in the transaction log. A file becomes **invisible** and subject to deletion by `VACUUM` when it is removed from the transaction log. This distinction is critical for data integrity. ^[convert-to-delta-databricks-on-aws.md]

#### Critical Safety Note

You should **avoid updating or appending data files during the conversion process** (when converting a Parquet or Iceberg table to Delta). After the table is converted, all writes must go through Delta Lake. If you modify files directly outside of Delta Lake, those modifications will not be recorded in the transaction log. As a result, `VACUUM` will treat those modified files as invisible and delete them, potentially causing data loss. ^[convert-to-delta-databricks-on-aws.md]

### Relationship with `CONVERT TO DELTA`

The `CONVERT TO DELTA` command creates a new Delta Lake transaction log that tracks existing Parquet or Iceberg files. However, any file not tracked by Delta Lake after the conversion is invisible and can be deleted when you run `VACUUM`. ^[convert-to-delta-databricks-on-aws.md]

During conversion, `CONVERT TO DELTA` collects statistics to improve query performance. If you run `CONVERT` with `NO STATISTICS`, you bypass statistics collection. After conversion, Databricks recommends using [Liquid Clustering](/concepts/liquid-clustering.md) to reorganize the data layout and generate statistics, which also affects what files are visible to queries. ^[convert-to-delta-databricks-on-aws.md]

### Best Practices

- **Always use Delta Lake APIs** for all writes after conversion. This ensures the transaction log stays up to date.
- **Run `VACUUM` regularly** to remove old, unreferenced files and manage storage costs.
- **Be cautious with shared directories.** If multiple external tables share the same underlying Parquet directory, converting one will make the others inaccessible. You must run `CONVERT` on each external table to restore access. ^[convert-to-delta-databricks-on-aws.md]

### Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The metadata store that tracks file visibility.
- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — The command that creates the transaction log.
- [Liquid Clustering](/concepts/liquid-clustering.md) — A technique for reorganizing data and generating statistics.
- [Data Retention and Garbage Collection](/concepts/delta-lake-vacuum-and-garbage-collection.md) — Practices for managing storage in Delta Lake.

### Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
