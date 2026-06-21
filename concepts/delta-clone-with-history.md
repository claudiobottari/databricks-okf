---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 818d1ee1d2ddbf5f1791f4127c98162ea05667d5cedfad9c1621741ccb191fcc
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-clone-with-history
    - DCWH
    - CLONE WITH HISTORY
    - CLONE with history
    - Clone with History
    - Clone with history
    - Deep Clone with History
    - clone with history
    - Clone table with history
    - Clone|clone with history
  citations:
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
title: Delta Clone with History
description: A Databricks Delta Lake operation that clones a Delta table including its full version history, which has restrictions on source table types.
tags:
  - databricks
  - delta-lake
  - clone
  - data-management
timestamp: "2026-06-18T11:50:56.645Z"
---

# Delta Clone with History

**Delta Clone with History** is a Databricks operation that creates a deep clone of a [Delta table](/concepts/delta-lake-table.md) while preserving the full version history of the source table. Unlike a shallow clone that copies only metadata, a clone with history copies the underlying data files and the transaction log, allowing time travel queries on the cloned table. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE` Error Condition

When attempting to clone a table with history, the operation fails with `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE` if the source table does not meet the required characteristics. The error class has a `SQLSTATE: 0AKDC` (Feature Not Supported) and includes two specific sub-conditions. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

### `NON_DELTA`

Raised when the source table is not a Delta table. The error message is:

> Source table of `<format>` format is not supported.

Only Delta tables (the Delta Lake format) can be cloned with history. Cloning from other formats such as Parquet, CSV, or JSON is not supported. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

### `TIME_TRAVELLED_BY_TIMESTAMP`

Raised when the source table is time-travelled to a specific timestamp. The error message is:

> Source table time travelled by timestamp is not supported.

Time travel by version number (e.g., `VERSION AS OF 5`) is permitted, but using `TIMESTAMP AS OF` or `AS OF <timestamp>` is not supported for clone-with-history operations. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Resolution

- Ensure the source table is in [Delta Lake](/concepts/delta-lake.md) format.
- When specifying a historical version, use the version number instead of a timestamp. For example, use `VERSION AS OF 5` rather than `TIMESTAMP AS OF '2024-01-01'`.

## Related Concepts

- CLONE command — The SQL command used to create deep or shallow clones
- [Delta table versioning](/concepts/delta-table-versioning.md) — How Delta Lake tracks table history
- Time travel in Delta Lake — Querying previous versions of a Delta table
- Deep clone vs shallow clone — Differences between clone types

## Sources

- delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)
