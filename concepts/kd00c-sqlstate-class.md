---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8394a5fe63de7f57c9b97249a9cea90ef5e6debe887abfd9b67ff317a3916446
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - kd00c-sqlstate-class
    - KSC
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: KD00C SQLSTATE Class
description: The SQLSTATE class 'KD' (Datasource-specific errors) that encompasses the DELTA_VERSIONS_NOT_CONTIGUOUS error condition in Databricks.
tags:
  - sqlstate
  - error-handling
  - databricks
timestamp: "2026-06-19T15:10:11.580Z"
---

Here is the wiki page for "KD00C SQLSTATE Class".

---

## KD00C SQLSTATE Class

The **KD00C SQLSTATE class** is a datasource-specific error class within the SQLSTATE framework, used by Databricks to signal that the [Delta Lake](/concepts/delta-lake.md) transaction log has become non-contiguous. It is one of the KD Datasource-Specific Error classes.

### Error Message

The error is raised with the following message template:

```
Versions (<versionList>) are not contiguous. A gap in the delta log between versions <startVersion> and <endVersion> was detected while trying to load version <versionToLoad>.
```

^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

### Root Cause

A **KD00C** error indicates that the Delta log contains a gap: a version number that is missing from the sequence of transaction log entries. This can happen in two main scenarios:

- **Manual file removal** – Files in the `_delta_log` directory have been deleted or moved outside of normal Delta operations, breaking the version chain. This is the most common cause across all cloud providers. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]
- **S3 eventual consistency** – On AWS, a race condition can occur when a table is deleted and immediately recreated at the same storage location. S3’s eventual consistency model may cause the new table’s log to be read before all old entries have settled, resulting in a perceived gap. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

### Remediation

Because the internal state of the Delta log is corrupted, the table cannot be read or written normally. The only supported recovery action is to **contact Databricks support** so they can repair the table and restore a contiguous log. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

### SQLSTATE Hierarchy

| Class | Sub‑class | Description |
|-------|-----------|-------------|
| KD    | DD        | Data source‑specific errors |
|       | KD00C     | Non‑contiguous Delta log versions |

### Related Concepts

- SQLSTATE – The standard 5‑character status code system used by Databricks.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer that produces the contiguous transaction log.
- [ACID Transactions](/concepts/delta-acid-transactions.md) – The guarantee that requires a contiguous log.
- [Table Repair](/concepts/delta-table-repair.md) – The process of fixing a corrupt Delta table.
- Delta Log – The directory of version‑numbered JSON files that must remain contiguous for correct reads.

### Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
