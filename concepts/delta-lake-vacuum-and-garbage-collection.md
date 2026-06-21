---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 94483df05c648bad18514a451f263f96bb3649b865cddfd3b2c914e186f416bc
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-vacuum-and-garbage-collection
    - Garbage Collection and Delta Lake VACUUM
    - DLVAGC
    - Delta Lake garbage collection
    - Garbage Collection in Delta Lake
    - Data Retention and Garbage Collection
    - delta-lake-vacuum-and-garbage-collection-on-s3
    - garbage collection on S3 and Delta Lake VACUUM
    - DLVAGCOS
    - delta-lake-vacuum-and-s3-garbage-collection
    - S3 Garbage Collection and Delta Lake VACUUM
    - DLVASGC
    - delta-lake-vacuum-and-s3-versioning-interaction
    - S3 Versioning Interaction and Delta Lake VACUUM
    - DLVASVI
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Delta Lake VACUUM and Garbage Collection
description: Delta Lake's VACUUM command permanently deletes data files and transaction logs; enabling S3 bucket versioning causes S3 to retain these files, undermining Delta's own garbage collection.
tags:
  - delta-lake
  - s3
  - garbage-collection
timestamp: "2026-06-18T15:15:19.021Z"
---

---
title: Delta Lake VACUUM and Garbage Collection
summary: Delta Lake's built-in garbage collection mechanism for reclaiming storage and the VACUUM command for permanently deleting old data files.
sources:
  - delta-lake-limitations-on-s3-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:05:05.503Z"
updatedAt: "2026-06-18T08:05:05.503Z"
tags:
  - delta-lake
  - data-management
  - storage
aliases:
  - delta-lake-vacuum-and-garbage-collection
  - dl-vacuum-gc
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

## Overview

Delta Lake manages its own versioning and garbage collection independently of the underlying storage system. This includes automatic cleanup of transaction logs during regular table operations and the `VACUUM` command for permanently deleting old data files. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## VACUUM Command

The `VACUUM` command is Delta Lake's mechanism for garbage collection. It permanently deletes data files that are no longer referenced by the Delta transaction log and are older than a configurable retention threshold. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Interaction with S3 Bucket Versioning

Databricks recommends that you not enable S3 bucket versioning for buckets that store Delta Lake data, including Unity Catalog managed tables. When bucket versioning is enabled, S3 retains old copies of files that Delta Lake considers deleted — including data files that `VACUUM` would permanently remove and transaction logs cleaned up during regular operations. This can lead to unnecessary storage accumulation and potential performance degradation. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

If you must use bucket versioning, Databricks recommends:
- Retaining only three versions
- Implementing a lifecycle management policy that retains versions for 7 days or less
- Notifying Databricks support that bucket versioning is enabled if you encounter performance slowdowns on versioned buckets ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- VACUUM — The command for permanently deleting old data files
- [S3 Bucket Versioning](/concepts/s3-bucket-versioning-and-delta-lake.md) — How S3 versioning interacts with Delta Lake garbage collection
- [Unity Catalog](/concepts/unity-catalog.md) — Managed tables that are subject to these limitations
- [Transaction Log](/concepts/delta-transaction-log.md) — The log of all changes to a Delta table
- Data Retention — Configuring how long old data files are kept
- Delta Cleanup — Automatic cleanup during regular operations

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
