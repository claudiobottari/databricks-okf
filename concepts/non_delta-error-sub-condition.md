---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ecde8ad6f25ebc7e7aa65138e5bde333c1a5a3140038afc62d7d72b8d438eb24
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non_delta-error-sub-condition
    - NES
  citations:
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
title: NON_DELTA error sub-condition
description: A specific error sub-condition under DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE, raised when the source table is not a Delta format table.
tags:
  - databricks
  - error-messages
  - delta-lake
  - clone
timestamp: "2026-06-18T11:50:53.480Z"
---

# NON_DELTA error sub-condition

The **NON_DELTA** error sub-condition occurs under the parent error class `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE`. It is raised when a `CLONE WITH HISTORY` operation targets a source table that is not a Delta table. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Error Details

The error message is:

> Source table of `<format>` format is not supported.

The placeholder `<format>` indicates the actual format of the source table (for example, Parquet, CSV, Avro, or JSON), which is unsupported for cloning with history. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Cause

`CLONE WITH HISTORY` creates a deep clone of a [Delta table](/concepts/delta-lake-table.md) that preserves the full version history of the source. This operation requires the source table to be a Delta table. If the source is in any other format (e.g., Parquet, ORC, or a non-Delta Lake table), the `NON_DELTA` sub-condition is thrown. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, confirm that the source table is a Delta table. If the source is not in Delta format, consider:

- Converting the source to Delta format using `CONVERT TO DELTA`.
- Using a regular `CLONE` (without the `WITH HISTORY` option), which does not require a Delta source but creates a shallow clone without version history.

Note that these workarounds are not explicitly provided in the source material and are general best practices for Databricks Delta Lake.

## Related Concepts

- DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class
- [Delta Clone](/concepts/delta-clone.md)
- [CLONE WITH HISTORY](/concepts/delta-clone-with-history.md)
- [Delta table](/concepts/delta-lake-table.md)
- [Deep Clone](/concepts/deep-clone.md)
- [Shallow Clone](/concepts/shallow-clone.md)

## Sources

- delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)
