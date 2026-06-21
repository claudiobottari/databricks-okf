---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0d308e90f553563592e6e200650d8ee5c2f5de669800edba85f237dc3b05b741
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_deep_clone_streaming_table_error
    - DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR
    - DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR error class
    - DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR#REQUIRES_WITH_HISTORY
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR
description: An error class in Databricks that occurs when attempting to deep clone a streaming table, with multiple specific sub-error conditions.
tags:
  - error
  - databricks
  - delta-lake
  - streaming
timestamp: "2026-06-19T18:24:14.290Z"
---

```markdown
---
title: DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR
summary: Databricks error class raised when attempting to deep clone a Delta streaming table, with five distinct sub-reasons.
sources:
  - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:52:44.240Z"
updatedAt: "2026-06-19T15:03:46.134Z"
tags:
  - error
  - delta-lake
  - streaming-tables
  - databricks
aliases:
  - delta_deep_clone_streaming_table_error
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR

The `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` error class occurs when a `DEEP CLONE` operation fails on a Delta Streaming Table. The error has a SQLSTATE of `0A000` (feature not supported). The error message is "Deep clone of streaming table failed:" followed by a specific sub‑reason. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Sub‑errors

The error class includes five distinct sub‑error conditions, each describing a different reason why the deep clone failed.

### LOCATION_NOT_SUPPORTED

Specifying a `LOCATION` clause is not supported when deep cloning a streaming table. The cloned streaming table must use [[Managed Storage in Unity Catalog|Managed Storage]]. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### OLD_ARCHITECTURE_NOT_SUPPORTED

Only streaming tables that use the default publishing mode are supported. Streaming tables using an older architecture cannot be deep cloned. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### REQUIRES_WITH_HISTORY

The `WITH HISTORY` clause is required for deep cloning a streaming table. The correct syntax is:

```sql
CREATE TABLE ... DEEP CLONE ... WITH HISTORY
```

Omitting `WITH HISTORY` causes this sub‑error. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### SCHEDULED_TABLE_NOT_SUPPORTED

Scheduled streaming tables are not supported for deep clone. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### TIME_TRAVEL_NOT_SUPPORTED

[[Delta Lake Time Travel|Time Travel]] (specifying a version or timestamp) is not supported for deep clone of a streaming table. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Concepts

- Delta Streaming Table — The table type that triggers this error when deep cloned incorrectly.
- [[Deep Clone]] — The `DEEP CLONE` operation used to create an independent copy of a Delta table.
- [[Managed Storage in Unity Catalog|Managed Storage]] — Storage location managed by Unity Catalog or the [[metastore|Metastore]]; external location is not allowed for this operation.
- Delta Lake SQL Reference — For correct syntax of `CREATE TABLE ... DEEP CLONE ... WITH HISTORY`.
- [[Delta Lake Time Travel|Time Travel]] — A Delta Lake feature that allows querying previous versions of a table, which is not supported for streaming table deep clones.

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
