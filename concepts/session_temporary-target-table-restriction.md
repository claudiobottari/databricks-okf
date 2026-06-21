---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2b362960f146a7cdb93cc10f8fd73ca5ab38ddd14d966e7c7ccf586de34003a4
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - session_temporary-target-table-restriction
    - STTR
    - SESSION_TEMPORARY target table restriction|SESSION_TEMPORARY
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: SESSION_TEMPORARY target table restriction
description: Delta clone with history does not support session-scoped temporary target tables.
tags:
  - databricks
  - delta-lake
  - clone-operation
timestamp: "2026-06-19T18:22:52.018Z"
---

# SESSION_TEMPORARY Target Table Restriction

The **SESSION_TEMPORARY target table restriction** is an error condition that prevents using session temporary tables as the target for a [Deep Clone](/concepts/deep-clone.md) operation with history in [Delta Lake](/concepts/delta-lake.md). When attempting to clone a Delta table into a session temporary target table, the operation fails with the `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` error. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Error Details

The full error class is `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET`, with the subtype `SESSION_TEMPORARY`. The associated SQLSTATE is `0AKDC`, which falls under the "Feature not supported" class of SQL states. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

### Error Message

When this restriction is encountered, the error message states:

```
Session temporary target table is not supported.
```

^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Related Unsupported Target Types

The `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` error condition includes three categories of unsupported target tables:

| Error Subtype | Description |
|---|---|
| `NON_DELTA` | Target table of non-Delta format is not supported |
| `PATH_BASED` | Path-based target table is not supported |
| `SESSION_TEMPORARY` | Session temporary target table is not supported |

All three subtypes result in the same error class being raised. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Reason for Restriction

Session temporary tables in Databricks SQL have a limited lifespan — they exist only within the scope of a single session and are automatically dropped when the session ends. Because [Deep Clone with History](/concepts/delta-clone-with-history.md) operations are designed to create durable, independently managed copies of Delta tables that preserve the full commit history, session temporary tables are incompatible as targets. The history preservation and long-term persistence requirements of a deep clone conflict with the ephemeral nature of session-scoped temporary views. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Workarounds

To clone a Delta table with history, use one of the supported target table types instead of a session temporary table:

- **Managed Delta tables** — Tables registered in the [Hive metastore](/concepts/built-in-hive-metastore.md) or [Unity Catalog](/concepts/unity-catalog.md)
- **External Delta tables** — Tables backed by an external storage location

After cloning into a persistent table, you can create a session temporary view pointing to the cloned table if temporary access is needed for downstream operations. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Related Concepts

- [Deep Clone](/concepts/deep-clone.md) — The operation type affected by this restriction
- [Delta Lake](/concepts/delta-lake.md) — The storage format used by clone operations
- Session Temporary Tables — The unsupported target type
- [Delta Clone with History](/concepts/delta-clone-with-history.md) — The specific clone variant that preserves commit history
- [SQLSTATE 0AKDC](/concepts/sqlstate-0akdc.md) — The SQL standard state code for this error condition

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)
