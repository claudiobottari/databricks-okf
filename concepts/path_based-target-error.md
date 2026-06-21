---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 16558415cdee16ef7958544df3bf5d08c16ed8941caadd21a460f45afa78ee05
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - path_based-target-error
    - PTE
    - PATH_BASED target error
    - PATH_BASED
    - path-based access
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: PATH_BASED target error
description: A subtype of DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET indicating the target table is a path-based table (not supported for clone with history).
tags:
  - databricks
  - error-subtype
  - delta-lake
timestamp: "2026-06-18T11:51:13.609Z"
---

# PATH_BASED target error

The **PATH_BASED target error** is a specific condition of the `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` error class in Databricks. It occurs when a Delta `CLONE` operation that includes history is attempted against a target table that is defined by a storage path rather than a registered catalog table. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Error Message

When this error is raised, the following message is returned:

```
PATH_BASED target table is not supported.
```

The error belongs to SQLSTATE class `0AKDC` (Feature not supported). ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Cause

The `CLONE` command that includes full history (the `CLONE` with `HISTORY` option) requires the target to be a table registered in the [Metastore](/concepts/metastore.md) — either a [Unity Catalog](/concepts/unity-catalog.md) table or a [Hive metastore table](/concepts/hive-metastore-table-access-control.md). Path-based targets — that is, tables created or referenced using a direct storage location path such as `/mnt/bronze/my_table` or `abfss://container@storage.dfs.core.windows.net/path` — are not supported for this operation. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Context and Scope

The error is part of a broader error class that also includes `NON_DELTA` and `SESSION_TEMPORARY` target types. The `PATH_BASED` condition specifically applies when the target table is defined by a path and not by a fully qualified name within a catalog or schema. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

This error can be triggered by any `CLONE` syntax that includes history, such as:

```sql
CREATE OR REPLACE TABLE delta.`/path/to/target` CLONE source_table WITH HISTORY;
```

or

```sql
INSERT INTO `/path/to/target` CLONE source_table WITH HISTORY;
```

## Resolution

To resolve the `PATH_BASED` target error, replace the path-based target with a table registered in a catalog (e.g., `my_catalog.my_schema.my_table`). Ensure that:

- The target table exists in [Unity Catalog](/concepts/unity-catalog.md) or a Hive [Metastore](/concepts/metastore.md).
- The target table uses the [Delta Lake](/concepts/delta-lake.md) format.
- The caller has the required privileges (`CREATE`, `SELECT`, `INSERT`) on the target [Catalog and Schema](/concepts/catalog-and-schema.md).

After converting the target to a catalog-registered table, the clone with history should succeed.

## Related Concepts

- [Delta Clone](/concepts/delta-clone.md) — The Delta Lake `CLONE` operation used for incremental table copies
- [Delta Lake](/concepts/delta-lake.md) — The storage format underlying the clone feature
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) where catalog-registered tables are defined
- [External locations](/concepts/external-location.md) — Storage paths that are not registered as catalog tables
- DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET error class — The parent error class containing `PATH_BASED`, `NON_DELTA`, and `SESSION_TEMPORARY` conditions
- [Delta Sharing](/concepts/delta-sharing.md) — A related feature that may also interact with clone semantics

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)
