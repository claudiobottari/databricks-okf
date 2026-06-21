---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b03895d5dfa4f0a4b980983e43f20ea82eb921d07b06bfc004b1e0956bd75c2f
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sampling-based-restoration-detection
    - SRD
    - sampling-based-restored-data-detection
    - SRDD
    - RDD
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Sampling-based restoration detection
description: Databricks samples files presumed to be archived to detect if they have been restored, and if so, assumes all files are restored for that query.
tags:
  - delta-lake
  - archival
  - sampling
timestamp: "2026-06-19T17:34:56.225Z"
---

# Sampling-based Restoration Detection

**Sampling-based restoration detection** is a mechanism used by Databricks to determine whether archived files in a Delta table with [archival support](/concepts/archival-support-in-databricks.md) have been restored to a fast retrieval storage tier. When a query requires scanning files that are presumed to be archived, Databricks samples a subset of those files to check whether they are still in archival storage or have been restored. ^[archival-support-in-databricks-databricks-on-aws.md]

## How It Works

When Databricks prepares a scan over a table with archival support enabled, it samples files older than the specified retention period that are required by the query. The system checks whether these sampled files have been restored from archival storage. If the results indicate that the sampled files — which were presumed to be archived — have been restored, Databricks assumes that all files for the query have been restored and proceeds to process the query. The results then include data from the files that had been marked for archival. ^[archival-support-in-databricks-databricks-on-aws.md]

This sampling approach avoids the overhead of checking every single archived file before running a query, but it introduces an assumption that restored files are restored in bulk rather than individually.

## Relationship to `SHOW ARCHIVED FILES`

The `SHOW ARCHIVED FILES` command returns URIs for archived files as a Spark DataFrame, helping users identify which files must be restored. After restoring those files using cloud provider APIs (such as S3 restore object APIs), archival support automatically recognizes the restored files. The sampling mechanism then detects the restored state when subsequent queries are run. ^[archival-support-in-databricks-databricks-on-aws.md]

## Limitations on Sampling

Sampling-based restoration detection does **not** apply to all queries. In particular:

- **`LIMIT` queries** do not trigger sampling for restored data. If a table's data has been restored, most queries succeed when querying restored data, but a `LIMIT` query returns a `DELTA_ARCHIVED_FILES_IN_LIMIT` error. This is because the system cannot determine how many unarchived rows exist to satisfy the `LIMIT` clause without potentially scanning archived files. ^[archival-support-in-databricks-databricks-on-aws.md]

Users who encounter the error `Not enough files to satisfy LIMIT` should lower the `LIMIT` clause to find enough unarchived rows to meet the specified limit. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) — The broader feature that enables cloud-based lifecycle policies for Delta tables
- [Delta Lake](/concepts/delta-lake.md) — The storage format that supports archival with `timeUntilArchived` table properties
- Cloud lifecycle policies — The underlying cloud object storage policies that govern file archival
- S3 Glacier Deep Archive and S3 Glacier Flexible Retrieval — Supported archival storage tiers

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
