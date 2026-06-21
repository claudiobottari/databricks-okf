---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2308e24ccb81cc3d44a9f4ed3c3a50598829e3aca0389644e471529c722e7d3d
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-protocol-upgrade-conflicts
    - DLPUC
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Delta Lake Protocol Upgrade Conflicts
description: A transaction conflict triggered when a concurrent operation upgrades the Delta Lake table protocol version, forcing other transactions to retry.
tags:
  - delta-lake
  - protocol
  - transactions
timestamp: "2026-06-19T15:02:47.472Z"
---

# Delta Lake Protocol Upgrade Conflicts

**Delta Lake Protocol Upgrade Conflicts** occur when a concurrent operation upgrades the table protocol (the Delta Lake transaction log version) while another transaction is in progress, causing the in-flight transaction to fail with a conflict error. These conflicts are a specific subclass of [Delta Lake concurrent write conflicts](/concepts/delta-lake-optimistic-concurrency-control.md).

## Overview

When a Delta table's protocol version is upgraded by one operation, any concurrent read or write transactions that were started before the upgrade will fail. This is because the protocol change alters the fundamental rules for how the table's transaction log is interpreted, making the assumptions of the in-flight transaction invalid. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Error Condition

Protocol upgrade conflicts are reported with the error condition `PROTOCOL_CHANGE`. The error message follows this pattern:

```
Transaction conflict detected, a concurrent <operation> upgraded the table protocol.
Please retry the operation.
```

^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## When Protocol Upgrades Occur

Protocol upgrades can happen automatically or manually:

- **Automatic upgrades**: Delta Lake may upgrade the protocol version when new features are enabled, such as Change Data Feed (CDC), [Deletion Vectors](/concepts/deletion-vectors.md), or [Column Mapping](/concepts/delta-table-column-mapping.md).
- **Manual upgrades**: Administrators may explicitly upgrade the protocol using `ALTER TABLE` commands or Delta Lake utility operations.

## Resolution

The recommended resolution for a `PROTOCOL_CHANGE` conflict is straightforward: **retry the operation**. Since the protocol upgrade is a one-time event, retrying the transaction after the upgrade has completed will succeed. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake concurrent write conflicts](/concepts/delta-lake-optimistic-concurrency-control.md) — The broader category of transaction conflicts in Delta Lake
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The foundation for Delta Lake's ACID guarantees
- Delta Lake protocol versioning — How Delta Lake manages protocol compatibility
- DELTA_CONCURRENT_APPEND — Error class for append conflicts
- [Optimistic concurrency control](/concepts/delta-lake-optimistic-concurrency-control.md) — The underlying mechanism that detects these conflicts

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
