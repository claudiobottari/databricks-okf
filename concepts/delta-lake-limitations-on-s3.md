---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6f3d2f5cb483fa79e6f17c131028f33752070de28f89d189b8cc397d0c90202e
  pageDirectory: concepts
  sources:
    - migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-limitations-on-s3
    - DLLOS
  citations:
    - file: migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md
title: Delta Lake Limitations on S3
description: Warning against simultaneously modifying the same Delta table stored on S3 from multiple workspaces or systems due to concurrency limitations.
tags:
  - delta-lake
  - s3
  - limitations
timestamp: "2026-06-19T19:32:20.581Z"
---

# Delta Lake Limitations on S3

**Delta Lake limitations on S3** refer to known constraints when using [Delta Lake](/concepts/delta-lake.md) tables stored on Amazon S3. The primary limitation documented by Databricks is that simultaneously modifying data in the same Delta table stored in S3 from multiple workspaces or data systems is not recommended. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Background

Delta Lake is the underlying format for the Databricks Lakehouse and is built on top of Parquet. While Databricks optimizes many lakehouse features around Delta Lake and provides native connectors, concurrent writes from separate workspaces or external data systems to the same Delta table on S3 can lead to consistency issues. Databricks advises against this practice and provides a dedicated external resource for further details. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- Amazon S3 – The object store commonly used with Delta Lake.
- Databricks Lakehouse – The architecture that relies on Delta Lake.
- [Parquet to Delta Lake Migration](/concepts/parquet-to-delta-lake-migration.md) – Considerations when converting Parquet data lakes.
- [Delta Sharing](/concepts/delta-sharing.md) – Sharing data stored in Delta Lake with external clients.

## Sources

- migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md

# Citations

1. [migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md](/references/migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws-01ccec95.md)
