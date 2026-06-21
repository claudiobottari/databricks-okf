---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f1e1b7aaecbf36992c728da2fae9ac477494f097850989e74d86f5b54805fd84
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_versions_not_contiguous-error
    - DELTA_VERSIONS_NOT_CONTIGUOUS
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: DELTA_VERSIONS_NOT_CONTIGUOUS error
description: A Databricks Delta Lake error that occurs when versions in the delta transaction log are not sequential, indicating a gap in the log.
tags:
  - databricks
  - delta-lake
  - error-message
timestamp: "2026-06-19T18:28:55.016Z"
---

---

title: DELTA_VERSIONS_NOT_CONTIGUOUS Error
summary: A Databricks error indicating that Delta Lake transaction log versions are not sequential, with a gap detected between two version numbers.
sources:
  - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:25:15.247Z"
updatedAt: "2026-06-19T15:09:46.250Z"
tags:
  - delta-lake
  - error-handling
  - databricks
aliases:
  - delta_versions_not_contiguous-error
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# DELTA_VERSIONS_NOT_CONTIGUOUS Error

The **DELTA_VERSIONS_NOT_CONTIGUOUS** error is raised by Delta Lake when the transaction log of a Delta table contains a gap between consecutive version numbers. The Delta Lake protocol requires that every commit produces a strictly increasing, contiguous sequence of JSON files (e.g., `000000.json`, `000001.json`, `000002.json`) in the `_delta_log/` directory. If any file is missing, the engine cannot reconstruct the full history of the table and fails with this error. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Error Message

When the error is thrown, the engine returns the following pattern:

```
Versions (<versionList>) are not contiguous. A gap in the delta log between
versions <startVersion> and <endVersion> was detected while trying to load
version <versionToLoad>.
```

The error's SQL state is `KD00C` (a datasource-specific error class under the KD SQLSTATE class). ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Causes

The root causes differ slightly depending on the deployment environment.

| Environment | Cause(s) |
|-------------|----------|
| **AWS**     | Files have been manually removed from the Delta log directory, or Amazon S3 eventual consistency can produce a gap when a table is deleted and then recreated at the same location. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md] |
| **Azure**   | Files have been manually removed from the Delta log directory. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md] |
| **Generic** | Files have been manually removed from the Delta log directory. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md] |

In all cases, the most common trigger is accidental or external deletion of intermediate Delta log files. On AWS, S3 eventual consistency can also introduce temporary gaps when a table is dropped and immediately recreated at the same S3 path (the new table's log may appear before the old table's log has fully replicated). ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Resolution

Databricks support must be contacted to repair the affected table. The error cannot be resolved by the user through standard Delta Lake commands. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The storage layer that uses the transaction log to provide ACID transactions.
- Delta Log – The `_delta_log/` directory containing commit JSON files that record all changes.
- [S3 Eventual Consistency](/concepts/s3-eventually-consistent-model.md) – A property of Amazon S3 that can cause transient listing inconsistencies.
- SQLSTATE – Error classification system used by Databricks (class KD covers datasource-specific errors).

## Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
