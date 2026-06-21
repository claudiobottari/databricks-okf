---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f6f474db4435a98acde712e3efcf57ddf1c2cbe7e7f1bfd4e8a9e304bee08cf9
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - old_architecture_not_supported-sub-error
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: OLD_ARCHITECTURE_NOT_SUPPORTED sub-error
description: Sub-error indicating that only streaming tables using the default publishing mode are supported for deep clone; legacy architectures are rejected.
tags:
  - error-messages
  - streaming-tables
  - publishing-mode
timestamp: "2026-06-19T10:04:51.259Z"
---

# OLD_ARCHITECTURE_NOT_SUPPORTED Sub-Error

The **OLD_ARCHITECTURE_NOT_SUPPORTED** sub-error occurs when attempting to perform a `DEEP CLONE` on a streaming table that does not use the **default publishing mode**. Only streaming tables configured with the default publishing mode are eligible for deep clone operations. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Parent Error

This sub-error is part of the DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR error class, which is raised when a deep clone of a streaming table fails.

## Error Message

When the error is triggered, the full error message reads:

```
Deep clone of streaming table failed: OLD_ARCHITECTURE_NOT_SUPPORTED
```

## Cause

The deep clone operation on a streaming table requires the table to be using the **default publishing mode**. Streaming tables that have been configured with a non-default publishing mode – for example, an explicit publishing mode set via Delta Live Tables – trigger this error because the deep clone mechanism cannot handle the non-default architecture. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Solution

To resolve this error, ensure that the target streaming table uses the default publishing mode. If the streaming table was created with a different publishing mode, consider either:

- Recreating the streaming table using the default publishing mode, or
- Choosing an alternative method to copy or clone the data that is compatible with the non-default publishing mode.

For more details on streaming table publishing modes, see the related documentation on streaming table architecture and Delta Live Tables publication settings.

## Related Concepts

- DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR — The parent error class.
- [Deep Clone](/concepts/deep-clone.md) — The operation that failed.
- Streaming table — The object type involved.
- [Default publishing mode](/concepts/streaming-table-default-publishing-mode-requirement.md) — The required configuration for deep clone support.
- Delta Live Tables — The framework used to define streaming table publishing modes.
- LOCATION_NOT_SUPPORTED sub-error — Another sub-error of the same parent class.
- REQUIRES_WITH_HISTORY sub-error — Another sub-error that recommends using `WITH HISTORY`.

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
