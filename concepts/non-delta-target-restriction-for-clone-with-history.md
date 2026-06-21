---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a9eedb43d2f55a41e288662b05ac94f3dc5d0eb4b531cc36181027491550c56a
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non-delta-target-restriction-for-clone-with-history
    - NTRFCWH
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: Non-Delta target restriction for clone with history
description: Cloning a Delta table with history to a non-Delta format target table is not supported in Databricks.
tags:
  - databricks
  - delta-lake
  - restrictions
timestamp: "2026-06-18T15:17:27.139Z"
---

# Non-Delta target restriction for clone with history

**Non-Delta target restriction for clone with history** is an error condition that occurs when attempting to use the `CLONE WITH HISTORY` operation on a target table that is not a [Delta table](/concepts/delta-lake-table.md). The operation requires the target to be a Delta table to preserve the full history of changes during the clone operation.

## Error Overview

The `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` error is raised when the target table for a clone with history operation does not meet the required format. The error has a SQLSTATE of `0AKDC`, which falls under the "Feature not supported" class. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Error Subtypes

The error condition includes three specific subtypes, each describing a different unsupported target scenario:

### NON_DELTA

The `NON_DELTA` subtype occurs when the target table is not a Delta format table. Only [Delta Lake](/concepts/delta-lake.md) tables support the history preservation feature during clone operations. Attempting to clone with history to a non-Delta target will result in this error. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

### PATH_BASED

The `PATH_BASED` subtype occurs when the target is a path-based table. Path-based tables do not support clone with history operations. The target must be a managed or external table registered in the [Hive metastore](/concepts/built-in-hive-metastore.md) or [Unity Catalog](/concepts/unity-catalog.md). ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

### SESSION_TEMPORARY

The `SESSION_TEMPORARY` subtype occurs when the target is a session temporary table. Session temporary tables exist only for the duration of a session and cannot serve as targets for clone with history operations. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, ensure the target table meets the following requirements:

- The target must be a [Delta table](/concepts/delta-lake-table.md) format
- The target must be a registered table (not path-based)
- The target must be a permanent table (not session temporary)

Consider using a regular `CLONE` operation (without history) if you need to clone to a non-Delta target, or create a Delta table as the target before performing the clone with history operation.

## Related Concepts

- [Delta Lake clone](/concepts/delta-clone.md) — The clone operation for creating copies of Delta tables
- [Delta table](/concepts/delta-lake-table.md) — The table format required for clone with history
- [Unity Catalog](/concepts/unity-catalog.md) — Table registration and management
- [Hive metastore](/concepts/built-in-hive-metastore.md) — Legacy table metadata storage

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)
