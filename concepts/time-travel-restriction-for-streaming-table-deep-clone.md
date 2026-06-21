---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ffee800d62d43b87a007d68a0a3683842ba27e67cbeb496d1f3c4ee6576ba6c0
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-travel-restriction-for-streaming-table-deep-clone
    - TTRFSTDC
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: Time Travel Restriction for Streaming Table Deep Clone
description: Time travel (e.g., VERSION AS OF, TIMESTAMP AS OF) is not supported when deep cloning a streaming table
tags:
  - delta-lake
  - streaming-tables
  - time-travel
  - deep-clone
timestamp: "2026-06-19T15:04:16.139Z"
---

# Time Travel Restriction for Streaming Table Deep Clone

**Time Travel Restriction for Streaming Table Deep Clone** is a limitation in Databricks that prevents the use of [Time Travel](/concepts/delta-lake-time-travel.md) features when performing a deep clone operation on Streaming Tables.

## Overview

When attempting to deep clone a streaming table, time travel is not supported. This restriction applies to any deep clone operation that specifies a time travel option, such as `AS OF` or a specific version or timestamp. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Error Condition

The restriction is enforced through the `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` error class, with the specific error subtype `TIME_TRAVEL_NOT_SUPPORTED`. When triggered, this error indicates that the deep clone operation cannot be completed because time travel is not supported for streaming table deep clones. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### Error Message

The error is accompanied by a generic message stating: "Deep clone of streaming table failed" along with the specific reason: "Time travel is not supported for streaming table deep clone." ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Affected Operations

The restriction specifically applies to:
- `CREATE OR REPLACE TABLE ... DEEP CLONE` statements that include time travel specifications (e.g., `AS OF TIMESTAMP` or `AS OF VERSION`)
- Deep clone operations that attempt to clone a streaming table from a historical state
- Any other deep clone variant that incorporates time travel on streaming tables

## Context and Limitations

The time travel restriction is part of a broader set of limitations for streaming table deep clones. Other related restrictions include:

- LOCATION_NOT_SUPPORTED|Location Not Supported for Streaming Table Deep Clone – Specifying a `LOCATION` is not supported
- OLD_ARCHITECTURE_NOT_SUPPORTED|Old Architecture Not Supported – Only streaming tables using the default publishing mode are supported
- [WITH HISTORY Requirement](/concepts/with-history-requirement-for-deep-clone-of-streaming-tables.md) – The `WITH HISTORY` clause is required for streaming table deep clones
- SCHEDULED_TABLE_NOT_SUPPORTED|Scheduled Tables Not Supported – Scheduled streaming tables cannot be deep cloned

## Related Concepts

- [Delta Lake Deep Clone](/concepts/delta-table-cloning.md) – The general deep clone operation for Delta tables
- [Streaming tables in Databricks](/concepts/streaming-tables-in-databricks.md) – Overview of streaming table capabilities and limitations
- [Delta Lake Time Travel](/concepts/delta-lake-time-travel.md) – Time travel features available for non-streaming Delta tables
- Delta Lake Error Classes – Error handling for Delta Lake operations
- SQLSTATE 0A000 – The SQLSTATE code associated with feature not supported errors

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
