---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 26144bb1a6ec08bfc57c35edc270094f819c0bf3660efb7203d6390df89dada3
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - has_indexes-error-condition
    - HEC
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: HAS_INDEXES error condition
description: A sub-error of DELTA_CLONE_INCOMPATIBLE_SOURCE indicating the source table has indexes that must be dropped before a Delta clone operation can proceed.
tags:
  - databricks
  - delta-lake
  - error-message
  - indexes
timestamp: "2026-06-18T11:50:22.572Z"
---

# HAS_INDEXES Error Condition

The **HAS_INDEXES error condition** is a `DELTA_CLONE_INCOMPATIBLE_SOURCE` error that occurs when attempting to clone a Delta table that has indexes defined on it. The error indicates that the clone source has a valid format but contains an unsupported feature — indexes — that prevents the clone operation from completing.

## Error Message

When this error occurs, Databricks returns the following message:

```
Table `<tableName>` has indexes: `<indexNames>`. Drop the indexes before cloning.
```

^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Cause

The `HAS_INDEXES` error is raised when you attempt to clone a Delta table that has one or more indexes defined on it. Delta Lake's clone operation does not support tables with indexes, as indexes are not a feature that can be carried over to the cloned table. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Solution

To resolve this error, drop the indexes from the source table before performing the clone operation. After the indexes are removed, the clone operation can proceed. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### Example

```sql
-- Drop indexes from the source table
DROP INDEX IF EXISTS <indexName> ON <tableName>;

-- Then perform the clone operation
CREATE OR REPLACE TABLE <targetTable> CLONE <sourceTable>;
```

## Related Concepts

- DELTA_CLONE_INCOMPATIBLE_SOURCE — The parent error class for clone incompatibility issues
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and scalable metadata handling
- Clone operations — The mechanism for creating copies of Delta tables
- ICEBERG_MISSING_PARTITION_SPECS — A related error condition for Iceberg tables
- ICEBERG_UNDERGONE_PARTITION_EVOLUTION — A related error condition for Iceberg tables

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
