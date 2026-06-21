---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0ed043c69da1ebace02e611de8519eac62bda4dec11e0ee8260ebc6d2fd28d5e
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - archived-data-sampling-mechanism
    - ADSM
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Archived Data Sampling Mechanism
description: Databricks' approach to detecting restored archived files by sampling files older than the retention period; if sampled files appear restored, all archived files for the query are assumed restored.
tags:
  - databricks
  - archival
  - delta-lake
  - performance
timestamp: "2026-06-19T14:03:03.392Z"
---

# Archived Data Sampling Mechanism

The **Archived Data Sampling Mechanism** is the process Databricks uses to detect whether data files in a Delta table that were moved to archival storage (such as Amazon S3 Glacier) have been restored. When archival support is enabled, Databricks samples a subset of files older than the configured retention period to determine whether the cloud provider has made them available again, avoiding unnecessary full scans of archived files.

## Overview

Archival support in Databricks works with cloud-based lifecycle policies (e.g., S3 Glacier Deep Archive or Glacier Flexible Retrieval) to allow queries that can be answered without accessing archived files. When a query requires data from files that have been archived, Databricks must first determine whether those files have been restored to a fast-retrieval tier. The sampling mechanism provides an efficient check without requiring the system to attempt reads on every archived file. ^[archival-support-in-databricks-databricks-on-aws.md]

## How the Sampling Mechanism Works

When Databricks prepares a scan over a table with archival support enabled, it samples files older than the specified retention period that are required by the query. If the sampled files — which were presumed to be archived — are actually accessible (i.e., have been restored), Databricks assumes that **all** files for the query have been restored. The query then proceeds, and results include data from the files that were marked for archival. ^[archival-support-in-databricks-databricks-on-aws.md]

This behavior means that restoration of a small set of files can implicitly "unlock" the entire set of archived files for a given query, reducing the overhead of checking each file individually. The sampling is performed as part of the scan preparation phase.

### When Sampling Is Used

- The mechanism is engaged whenever a query would need to read data from files that are older than the `delta.timeUntilArchived` threshold.
- Sampling is also referenced in the context of `SHOW ARCHIVED FILES` and file restoration: after restoring files via cloud provider APIs, Databricks uses the same sampling logic to recognize that data is now available. ^[archival-support-in-databricks-databricks-on-aws.md]

## Limitations

Sampling does not apply to all queries. Notably, `LIMIT` queries on tables with archival support enabled **do not** trigger the sampling mechanism. This can lead to a specific error condition: if a table's archived data has been restored, most queries succeed, but a `LIMIT` query returns a `DELTA_ARCHIVED_FILES_IN_LIMIT` error. ^[archival-support-in-databricks-databricks-on-aws.md]

As stated in the source: "If a table's data is restored, most queries succeed when querying restored data, but a `LIMIT` query returns a `DELTA_ARCHIVED_FILES_IN_LIMIT` error." ^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) — The overall feature that enables cloud lifecycle policies for Delta tables
- Delta table lifecycle policies — Cloud object storage rules that transition data to archival tiers
- [SHOW ARCHIVED FILES](/concepts/show-archived-files-syntax.md) — Syntax to identify which files need restoration
- Restore archived files — Process using cloud provider APIs to make archived data available
- [delta.timeUntilArchived](/concepts/deltatimeuntilarchived.md) — Table property that defines the archival threshold

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
