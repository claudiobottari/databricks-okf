---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 156e1c6cf67df8c3572261d3832bb50e9e5cf46b5c7126c49bb2cc7895e67b0c
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unsupported-delta-clone-targets
    - UDCT
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: Unsupported Delta Clone Targets
description: "The three categories of target tables that cannot receive a Delta clone with history: non-Delta tables, path-based tables, and session temporary tables."
tags:
  - databricks
  - delta-lake
  - limitations
timestamp: "2026-06-19T15:02:25.749Z"
---

# Unsupported Delta Clone Targets

**Unsupported Delta Clone Targets** refers to specific target table types that are not permitted when performing a `CLONE` operation with history (i.e., `CLONE WITH HISTORY`) in [Delta Lake](/concepts/delta-lake.md). When a clone operation targets one of these unsupported formats, Databricks raises the `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` error condition (SQLSTATE: 0AKDC). ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Error Condition

The error is classified under SQLSTATE class `0A` (Feature Not Supported). It occurs solely during clone operations that include history. Three distinct target types trigger this error:

### NON_DELTA

Target table of non-Delta format is not supported. The clone target must be a [Delta Lake](/concepts/delta-lake.md) table; cloning with history into a non-Delta table (e.g., Parquet, CSV, JSON) is rejected. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

### PATH_BASED

Path-based target table is not supported. When the target is specified as a file path rather than a registered table in the [Hive metastore](/concepts/built-in-hive-metastore.md) or [Unity Catalog](/concepts/unity-catalog.md), the operation fails. Only metastore-registered tables can be the target of a clone with history. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

### SESSION_TEMPORARY

Session temporary target table is not supported. Temporary views or temporary tables that exist only for the duration of a session cannot serve as the target for a clone with history. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Usage Context

The error applies to both SQL and API-based clone operations, such as `CREATE OR REPLACE TABLE ... CLONE ... WITH HISTORY` or the `delta.clone()` DataFrame method. The restriction exists because history metadata (including transaction log, versioning, and time travel information) cannot be reliably maintained in non-Delta, path-based, or temporary targets. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Resolution

Ensure the clone target is a registered Delta table in the [Metastore](/concepts/metastore.md) (or Unity Catalog). Avoid using file paths, temporary tables, or non-Delta formats as targets for clone operations that include history. For shallow clones without history, different target restrictions apply. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Clone](/concepts/delta-clone.md)
- [Delta Lake](/concepts/delta-lake.md)
- [Hive metastore](/concepts/built-in-hive-metastore.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [SQLSTATE class 0A (Feature not supported)](/concepts/sqlstate-class-0a-feature-not-supported.md)
- Time Travel in Delta Lake

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)
