---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cafe953bbaee4b5e0e14c9f20fde78be87f6df3a504e7203c7fc54a41e382a52
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - has_indexes-delta-clone-sub-error
    - H(CS
    - HAS_INDEXES (Delta Clone sub-error)
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: HAS_INDEXES (Delta Clone sub-error)
description: A specific DELTA_CLONE_INCOMPATIBLE_SOURCE sub-error indicating the source table has indexes that must be dropped before cloning.
tags:
  - error-message
  - delta-lake
  - indexes
timestamp: "2026-06-19T10:02:29.980Z"
---

# HAS_INDEXES (Delta Clone sub-error)

**HAS_INDEXES** is a sub-error of the `DELTA_CLONE_INCOMPATIBLE_SOURCE` error class that occurs when attempting to clone a table that has indexes defined on it. The clone operation fails because Delta Lake does not support cloning tables with existing indexes.

## Error Message

When this error occurs, the following message is returned:

```
Table <tableName> has indexes: <indexNames>. Drop the indexes before cloning.
```

^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Cause

The clone source table has a valid format and is otherwise compatible with Delta Lake, but it contains indexes that are not supported in the target Delta table. Delta Lake's clone operation requires the source table to be free of indexes before cloning can proceed. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Solution

To resolve this error, drop the indexes from the source table before attempting the clone operation. The exact command for dropping indexes depends on the source table format:

- For tables with indexes, use the appropriate `DROP INDEX` syntax for the source table's format.
- After dropping all indexes, retry the `CLONE` operation.

## Related Concepts

- DELTA_CLONE_INCOMPATIBLE_SOURCE — The parent error class for clone compatibility issues
- [Delta Lake Clone](/concepts/delta-clone.md) — The operation used to create a copy of a Delta table
- ICEBERG_MISSING_PARTITION_SPECS — Related sub-error for Iceberg tables without partition specs
- ICEBERG_UNDERGONE_PARTITION_EVOLUTION — Related sub-error for Iceberg tables with partition evolution

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
