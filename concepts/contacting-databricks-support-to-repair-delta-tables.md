---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3fc62a35ff862d80d2a44ace89faccc8c5195659605838eab18b6af47bc601bb
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - contacting-databricks-support-to-repair-delta-tables
    - CDSTRDT
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: Contacting Databricks support to repair Delta tables
description: Databricks recommends contacting their support team to repair tables affected by the DELTA_VERSIONS_NOT_CONTIGUOUS error.
tags:
  - databricks
  - operations
  - support
timestamp: "2026-06-18T11:58:05.243Z"
---

# Contacting Databricks Support to Repair Delta Tables

When a [Delta table](/concepts/delta-lake-table.md) becomes corrupted—for example, due to missing or removed log files—Databricks support can repair the table by restoring the Delta log to a consistent state. The most common scenario that triggers this intervention is the `DELTA_VERSIONS_NOT_CONTIGUOUS` error. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## The DELTA_VERSIONS_NOT_CONTIGUOUS Error

This error occurs when the Delta log contains a gap between two consecutive versions. The error message states: "Versions are not contiguous. A gap in the delta log between versions `<startVersion>` and `<endVersion>` was detected while trying to load version `<versionToLoad>`." ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

### Causes

The gap can happen for two reasons: ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

* **Manual file deletion** — Files inside the `_delta_log` directory have been removed accidentally or intentionally, breaking the chain of transaction log entries.
* **S3 eventual consistency (AWS only)** — When a Delta table is deleted and recreated at the same storage location, the old and new logs can temporarily overlap or create inconsistencies due to AWS S3's eventual consistency model.

### Recommended Action

For both AWS and Azure environments, the only supported remedy is to contact Databricks Support. Databricks can inspect the table's metadata and repair the Delta log to restore a contiguous version history. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## How to Contact Databricks Support

When you reach out to Databricks support, provide the following information to speed up the investigation: ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

* The full error message, including the version numbers mentioned.
* The table location (path or catalog/schema/table name).
* Whether the table was recently deleted and recreated.
* Any known manual operations on the `_delta_log` directory.

Support will use internal tools to validate the table state and attempt repair. Note that in some cases, data loss may be unavoidable if the missing log versions cannot be recovered.

## Preventing Delta Table Corruption

To avoid needing a repair, follow these best practices: ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

* Never manually delete or modify files in the `_delta_log` directory.
* Use Delta vacuum and Optimize commands correctly—vacuum removes unreferenced data files, not log files.
* On AWS, avoid deleting and re‑creating a Delta table at the same location. Instead, use `DROP TABLE` and `CREATE TABLE` with a different path, or use `REPLACE TABLE` where supported.
* Enable [Delta Table History Retention](/concepts/delta-table-history-retention.md) with a reasonable threshold so old logs are automatically retained.

## Related Concepts

* [Delta table](/concepts/delta-lake-table.md) — The core storage format that relies on a transaction log.
* Delta log — The `_delta_log` directory that contains all transactional metadata.
* Delta table corruption — Other forms of corruption and recovery options.
* Databricks Support — The official support channel for repair requests.
* [S3 eventual consistency](/concepts/s3-eventually-consistent-model.md) — Cloud storage behavior that can cause log gaps on AWS.

## Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
