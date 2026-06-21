---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e8f19f2b2735cb48667ec4b6cf94a1965f9bc12473db8c26c42831a250303a23
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_clone_with_history_unsupported_target-error-class
    - DEC
    - DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET error class
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET error class
description: A Databricks error that occurs when attempting to clone a Delta table with history to an unsupported target type.
tags:
  - databricks
  - error-message
  - delta-lake
timestamp: "2026-06-19T18:22:48.367Z"
---

```markdown
---
title: DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET error class
summary: A Databricks error class indicating that an attempt to clone a Delta table with history failed because the target table type is unsupported
sources:
  - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T15:00:00.000Z"
updatedAt: "2026-06-19T15:00:00.000Z"
tags:
  - databricks
  - delta-lake
  - error-messages
aliases:
  - delta_clone_with_history_unsupported_target-error-class
  - DEC
confidence: 1
provenanceState: extracted
inferredParagraphs: 2
---

# DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET error class

The **DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET** error class occurs when a `CLONE WITH HISTORY` operation is attempted against a target table that does not support cloning with version history. The error is assigned SQLSTATE 0AKDC, which falls under the "Feature Not Supported" category. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Error Subtypes

The error class includes three specific subtypes, each identifying a different unsupported target table type:

### NON_DELTA

The target table is not a [[Delta Lake|Delta]] format table. The error message states: "Target table of non-delta format is not supported." ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

### PATH_BASED

The target table is a path-based table (that is, a table defined directly by a storage path rather than being managed by a [[metastore|Metastore]]). The error message states: "Path-based target table is not supported." ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

### SESSION_TEMPORARY

The target table is a session temporary table, which exists only for the duration of a Spark session. The error message states: "Session temporary target table is not supported." ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Cause

A `CLONE WITH HISTORY` operation requires the target table to be a managed or external Delta table that is capable of retaining version history. The operation fails when the target is not a Delta format table, is defined only by a path (without a [[metastore|Metastore]] registration), or is a session-scoped temporary table. These table types cannot store the full history that the clone operation attempts to copy.

## Solution

Ensure the target table is a supported Delta table type. Register path-based tables in a [[metastore|Metastore]] (such as the [[Built-in Hive Metastore|Hive metastore]] or [[Unity Catalog]]) before cloning, use permanent Delta tables instead of session temporary tables, and verify that the target is in Delta format. After making these adjustments, retry the `CLONE WITH HISTORY` operation.

## Related Concepts

- Delta CLONE operation
- Delta table history and versioning
- [[Delta Lake]]
- SQLSTATE error classes

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)
