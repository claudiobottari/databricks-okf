---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6bd3cbd282af2c4166bf296ab5fe8d4b049013e16105510115290418095d5a12
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - has_indexes-sub-error
    - HAS_INDEXES error
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: HAS_INDEXES sub-error
description: A specific error under DELTA_CLONE_INCOMPATIBLE_SOURCE indicating the source table has indexes that must be dropped before cloning into Delta.
tags:
  - error
  - delta-lake
  - indexes
timestamp: "2026-06-19T15:02:19.700Z"
---

```markdown
---
title: HAS_INDEXES sub-error
summary: A sub-error of DELTA_CLONE_INCOMPATIBLE_SOURCE indicating the source table has indexes that must be dropped before cloning
sources:
  - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:17:06.235Z"
updatedAt: "2026-06-18T15:17:06.235Z"
tags:
  - databricks
  - delta-lake
  - error
aliases:
  - has_indexes-sub-error
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# HAS_INDEXES Sub-Error

**HAS_INDEXES** is a sub-error of the DELTA_CLONE_INCOMPATIBLE_SOURCE error class (SQLSTATE: 0AKDC). It occurs when attempting to clone a source table that has indexes defined on it, which are incompatible with the [[Delta Lake]] format. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Error Message

When this sub-error is triggered, Databricks returns the following message:

> Table `<tableName>` has indexes: `<indexNames>`. Drop the indexes before cloning.

The placeholders `<tableName>` and `<indexNames>` are replaced with the actual table name and a list of the indexes present on the source table. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Cause

The clone source has a valid format (e.g., Parquet or Iceberg) but includes indexes that are not supported by Delta. Delta cannot represent traditional database indexes, which prevents the clone operation from proceeding. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Solution

Drop the indexes on the source table before performing the clone operation. The error message explicitly advises: “Drop the indexes before cloning.”^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_CLONE_INCOMPATIBLE_SOURCE error class — parent error class for cloning incompatibilities.
- [[Deep Clone (Delta Lake)|Clone Table]] — the Databricks command that creates a deep copy of a source table as a Delta table.
- ICEBERG_MISSING_PARTITION_SPECS sub-error — another sub-error for Iceberg tables that have no partition specs.
- ICEBERG_UNDERGONE_PARTITION_EVOLUTION sub-error — sub-error for Iceberg tables that have undergone partition evolution.

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
