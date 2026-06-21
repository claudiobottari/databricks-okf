---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2e9b368a978a636ce73bfae93f4bd01e45991b7e2887bb0e8281ae734027ede7
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - path_based-target-table-restriction
    - PTTR
    - PATH_BASED target table restriction|PATH_BASED
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: PATH_BASED target table restriction
description: Delta clone with history does not support path-based (location-only) target tables.
tags:
  - databricks
  - delta-lake
  - clone-operation
timestamp: "2026-06-19T18:22:39.737Z"
---

# PATH_BASED Target Table Restriction

The **PATH_BASED target table restriction** is a subtype of the `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` error condition (SQLSTATE: 0AKDC) in Databricks. This error occurs when a user attempts to clone a [Delta table](/concepts/delta-lake-table.md) with history to a target table that is specified as a path rather than a metastore-registered table. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Error Details

The error class `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` defines three unsupported target table types: `NON_DELTA`, `PATH_BASED`, and `SESSION_TEMPORARY`. The `PATH_BASED` subtype specifically indicates that a path-based target table is not supported when cloning with history. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Related Conditions

- **NON_DELTA** – The target table is in a non-Delta format.
- **SESSION_TEMPORARY** – The target table is a session temporary table.

## Related Concepts

- [DELTA_CLONE](/concepts/delta-clone.md) – The CLONE operation that creates a copy of a Delta table, optionally including history.
- [Delta table](/concepts/delta-lake-table.md) – The storage format used by Delta Lake.
- Error conditions in Databricks – Overview of error classes and SQLSTATE codes.
- [Clone table with history](/concepts/delta-clone-with-history.md) – The operation of making a full copy including the transaction log.

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)
