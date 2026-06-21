---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bdd356b7b0bfdeb75bdc9b3d752c544428fc6b7ba946dfaa15e0e32cae1f9b14
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-table-default-publishing-mode-requirement
    - STDPMR
    - Default publishing mode
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: Streaming Table Default Publishing Mode Requirement
description: Only streaming tables using the default publishing mode can be deep cloned; older architectures are not supported
tags:
  - delta-lake
  - streaming-tables
  - publishing-mode
  - databricks
timestamp: "2026-06-19T15:03:57.835Z"
---

## Streaming Table Default Publishing Mode Requirement

The **Streaming Table Default Publishing Mode Requirement** is a constraint that applies when performing a deep clone operation on a [Delta Lake](/concepts/delta-lake.md) streaming table. If the streaming table does not use the default publishing mode, the deep clone fails with the error `OLD_ARCHITECTURE_NOT_SUPPORTED`. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### Context

The deep clone operation on a streaming table can raise the error `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR`. One of its sub‑conditions is `OLD_ARCHITECTURE_NOT_SUPPORTED`, which reports: “Only streaming tables using the default publishing mode are supported.” This means that if the streaming table was created with a non‑default output mode (for example, `update` or `complete` instead of the default `append`), the deep clone is not allowed. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### Related Sub‑Conditions of the Same Error

The deep clone error also includes several other restrictions that apply to streaming tables: ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

- **`LOCATION_NOT_SUPPORTED`** – Specifying a custom `LOCATION` is not supported; the cloned streaming table uses managed storage.
- **`REQUIRES_WITH_HISTORY`** – The deep clone command must include `WITH HISTORY`.
- **`SCHEDULED_TABLE_NOT_SUPPORTED`** – Scheduled streaming tables cannot be deep cloned.
- **`TIME_TRAVEL_NOT_SUPPORTED`** – Time travel is not supported for streaming table deep clones.

### Usage Note

When deep cloning a streaming table, ensure that the source table was created with the default publishing mode (typically `append`). If the table used a different mode, the operation will fail with `OLD_ARCHITECTURE_NOT_SUPPORTED`, and the user must either change the source table’s mode or use an alternative cloning approach.

### Related Concepts

- Delta Live Tables – Often used to define streaming tables and their publishing modes.
- [Deep Clone](/concepts/deep-clone.md) – A operation that copies a table’s data and metadata.
- Streaming Table – A table that continuously ingests data from a streaming source.
- Error Handling – General guidance for diagnosing and resolving Delta Lake errors.
- SQLSTATE 0A000 – The feature‑not‑supported SQL state associated with this error.

### Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
