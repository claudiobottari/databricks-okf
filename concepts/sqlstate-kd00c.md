---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f631dfefe83fc4efb7b16444327e00e893b948a4d5693b46abf127d9a8233010
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sqlstate-kd00c
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: SQLSTATE KD00C
description: The SQL state class KD00C used for Datasource-specific errors in Databricks, under which the DELTA_VERSIONS_NOT_CONTIGUOUS error falls.
tags:
  - sqlstate
  - error-codes
  - databricks
timestamp: "2026-06-19T10:11:14.911Z"
---

Here is the wiki page for "SQLSTATE KD00C", written based solely on the provided source material.

---

## SQLSTATE KD00C

**SQLSTATE KD00C** is a Databricks error condition indicating that the Delta Lake transaction log is missing intermediate commit versions. The error occurs when the Delta log versions are not contiguous, meaning there is a gap between expected commit versions.

## Error Message

The error presents with the following message:

```
Versions (<versionList>) are not contiguous. A gap in the delta log between versions <startVersion> and <endVersion> was detected while trying to load version <versionToLoad>.
```

^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## SQLSTATE Class

KD00C belongs to the SQLSTATE class **KD**, which covers datasource-specific errors. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Causes

### AWS

On AWS, this error can occur when:

- Files have been manually removed from the Delta log.
- Amazon S3 eventual consistency causes this issue when a Delta table is deleted and recreated at the same location. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

### Azure and Generic

On Azure, as well as in generic (cloud-agnostic) environments, the error occurs when files have been manually removed from the Delta log. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Resolution

Contact Databricks support to repair the table in all cases (AWS, Azure, and generic). ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that uses a transaction log (Delta log) to track changes.
- Delta Log — The ordered commit log that records all changes to a Delta table.
- Delta Table Maintenance — Best practices for keeping Delta tables healthy and avoiding log corruption.
- [S3 Eventual Consistency](/concepts/s3-eventually-consistent-model.md) — A property of Amazon S3 that can cause read-after-write inconsistencies.
- SQLSTATE Error Classes — The Databricks error classification system for datasource-specific errors.

## Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
