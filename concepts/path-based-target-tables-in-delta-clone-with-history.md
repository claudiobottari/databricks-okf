---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 309ee33a5f16b9c2ac72c9f10798c7a8f9759a3e4b48a380dc6792f774feb778
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - path-based-target-tables-in-delta-clone-with-history
    - PTTIDCWH
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: Path-based target tables in Delta Clone with History
description: An error sub-condition (PATH_BASED) where the target table for a Delta Clone with History operation is path-based rather than metastore-registered
tags:
  - databricks
  - delta-lake
  - error-messages
timestamp: "2026-06-19T10:03:08.251Z"
---

# Path-based target tables in Delta Clone with History

**Path-based target tables in Delta Clone with History** refers to a restriction in Databricks where the `CREATE OR REPLACE TABLE ... CLONE ... WITH HISTORY` operation does not support cloning with history to tables referenced by a path in the Unity Catalog [Metastore](/concepts/metastore.md). When a user attempts to perform a `DEEP CLONE` with history to a path-based table, Databricks raises a `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` error with the `PATH_BASED` subcondition. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Overview

The [Delta Clone](/concepts/delta-clone.md) operation allows users to create a copy of a Delta table. The `DEEP CLONE` variant copies both data and metadata, and the `WITH HISTORY` option preserves the table's version history. However, this operation is not supported when the target table is specified by a path (e.g., `/path/to/table`) rather than by a fully qualified table name in the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Error Details

When a user attempts to clone with history to a path-based target table, Databricks raises the following error:

- **SQLSTATE**: `0AKDC`
- **Error class**: `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET`
- **Subcondition**: `PATH_BASED`
- **Message**: "Path-based target table is not supported."

^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

This error is distinct from other unsupported target scenarios in the same error class:

| Subcondition | Description |
|--------------|-------------|
| `NON_DELTA` | Target table is not a Delta format table |
| `PATH_BASED` | Target is specified by a filesystem path |
| `SESSION_TEMPORARY` | Target is a session-scoped temporary table |

^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Affected Operations

The restriction applies to `CREATE OR REPLACE TABLE ... CLONE ... WITH HISTORY` statements where the target table is referenced by a path. This includes both:

- Direct path references (e.g., `delta.`/path/to/table``)
- External locations referenced by path

## Workaround

To clone a Delta table with history, use a fully qualified table name in Unity Catalog as the target instead of a path-based reference. For example:

```sql
-- This will fail with PATH_BASED error
CREATE OR REPLACE TABLE delta.`/path/to/target` 
DEEP CLONE source_table WITH HISTORY;

-- This works — use a Unity Catalog table name
CREATE OR REPLACE TABLE catalog.schema.target_table 
DEEP CLONE source_table WITH HISTORY;
```

For path-based targets that do not require history, use a shallow clone (`SHALLOW CLONE`) or a deep clone without the `WITH HISTORY` clause.

## Related Concepts

- [Delta Clone](/concepts/delta-clone.md) — The cloning operation for Delta tables
- DEEP CLONE vs SHALLOW CLONE — Differences between clone types
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) for managing table references
- Path-based tables in Unity Catalog — How path references work
- DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET — The full error class documentation
- Delta Lake table management — General Delta table operations

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)
