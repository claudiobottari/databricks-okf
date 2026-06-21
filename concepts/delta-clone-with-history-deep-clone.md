---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0a50ff02743c983bd7a92604443ed2e7f1c1b4f980425374057628a2bdeb3a9c
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-clone-with-history-deep-clone
    - DCWH(C
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: Delta Clone with History (Deep Clone)
description: A Databricks operation that creates a deep copy of a Delta table including its full commit history, as opposed to a shallow clone.
tags:
  - databricks
  - delta-lake
  - data-management
timestamp: "2026-06-19T15:02:17.733Z"
---

# Delta Clone with History (Deep Clone)

**Delta Clone with History (Deep Clone)** is a Databricks operation that creates a full deep copy of a [Delta Table](/concepts/delta-lake-table.md) along with its complete history, including all previous versions and metadata. This contrasts with a shallow clone, which does not copy the data files or history. The deep clone with history is useful for creating independent replicas for testing, archival, or disaster recovery.

## Error Condition: `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET`

When a `CLONE` command with `DEEP CLONE` history targeting an unsupported table format fails, Databricks raises the error condition `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET`. This error is classified under SQLSTATE `0AKDC` (Feature not supported). ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

### Unsupported Target Types

The error message includes a specific reason string that identifies the type of unsupported target:

- **`NON_DELTA`** – The target table is not a Delta table. Deep clone with history is only supported when both source and target are Delta tables. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]
- **`PATH_BASED`** – The target is a path-based table (i.e., a table created using `USING DELTA LOCATION 'path'` without a [Metastore](/concepts/metastore.md) catalog). Deep clone with history requires a [Unity Catalog](/concepts/unity-catalog.md) managed table or a Hive [Metastore](/concepts/metastore.md) table, not a bare path reference. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]
- **`SESSION_TEMPORARY`** – The target is a session temporary view or table. Temporary tables cannot be targets of a deep clone with history because they do not persist beyond the session. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

### Resolution

To resolve this error, ensure the target table is a persisted Delta table in a [Metastore](/concepts/metastore.md) (catalog or Hive) and is not a temporary view. Use `CREATE TABLE` to define a permanent Delta target before executing the deep clone with history. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Table](/concepts/delta-lake-table.md)
- [Clone Table](/concepts/deep-clone.md)
- [Deep Clone](/concepts/deep-clone.md)
- [Shallow Clone](/concepts/shallow-clone.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- SQLSTATE Error Classes
- [Delta Lake](/concepts/delta-lake.md)

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)
