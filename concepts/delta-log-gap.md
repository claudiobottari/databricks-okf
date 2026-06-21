---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b1ab0ad1ffaff900949fbfa66c51e5e7e9de904e00705413b0312870ff0da9b2
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-log-gap
    - DLG
    - Delta Log
    - Delta log
    - DeltaLog
    - _delta_log
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: Delta log gap
description: A missing version sequence number in the Delta transaction log, often caused by manual file deletion or S3 eventual consistency issues.
tags:
  - delta-lake
  - troubleshooting
timestamp: "2026-06-19T18:29:01.076Z"
---

```markdown
---
title: Delta log gap
summary: A missing sequence of version files in the Delta transaction log that breaks the contiguity required for proper table reads.
sources:
  - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:25:06.315Z"
updatedAt: "2026-06-19T14:25:06.315Z"
tags:
  - delta-lake
  - transaction-log
  - data-integrity
aliases:
  - delta-log-gap
  - DLG
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Delta Log Gap

A **Delta log gap** is an error condition that occurs when the [[Delta Lake Transaction Log]] contains a discontinuity in its version sequence. The Delta log is a sequential record of all changes made to a Delta table, and each transaction is assigned a monotonically increasing version number. When a version is missing between two consecutive entries, the log is considered non-contiguous, and Delta Lake cannot load the table at the affected version. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Error Message

When a Delta log gap is detected, Delta Lake raises the following error:

```
DELTA_VERSIONS_NOT_CONTIGUOUS
Versions (<versionList>) are not contiguous. A gap in the delta log between versions <startVersion> and <endVersion> was detected while trying to load version <versionToLoad>.
```

^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Causes

### Manual File Removal

The most common cause of a Delta log gap is the manual deletion of Delta log files. If someone removes one or more JSON commit files from the `_delta_log` directory — for example, during cleanup or storage management — the version sequence becomes broken. Delta Lake relies on the complete, contiguous log to reconstruct table state at any given version. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

### S3 Eventual Consistency (AWS Only)

On AWS, [[S3 Eventually Consistent Model|S3 Eventual Consistency]] can cause a Delta log gap when a table is deleted and recreated at the same storage location. If the new table's log files are written before the old table's log files have fully propagated, Delta Lake may encounter a version sequence that appears non-contiguous. This is a known issue specific to AWS deployments. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Resolution

Contact Databricks support to repair the table. There is no self-service mechanism to fix a Delta log gap — only support can reconstruct the missing log entries or restore the table from a valid checkpoint. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Prevention

- Avoid manually manipulating the `_delta_log` directory. Never delete or modify Delta log files directly.
- On AWS, use proper table lifecycle management when deleting and recreating tables — consider using different storage locations or allowing sufficient time for S3 consistency before recreating a table at the same path.
- Enable Delta Lake retention policies to automate log file cleanup instead of removing files manually.

## Related Concepts

- [[Delta Lake Transaction Log]] — The core mechanism that tracks all changes to a Delta table.
- Delta Lake Checkpoints — Periodic snapshots that help reconstruct table state without replaying the entire log.
- [[Delta table versioning|Delta Lake Versioning]] — How Delta Lake assigns and tracks version numbers for each transaction.
- [[S3 Eventually Consistent Model|S3 Eventual Consistency]] — A known AWS limitation that can affect Delta Lake operations.

## Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
