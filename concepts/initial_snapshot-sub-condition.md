---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ee73df18a3ac92d377589465f47af1b1f33cf43d0bf797cf7190d65f7f16d42a
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - initial_snapshot-sub-condition
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: INITIAL_SNAPSHOT sub-condition
description: A specific reason for the DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE error, indicating that offsets in the skip range must not be initial snapshot offsets (isInitialSnapshot must be false).
tags:
  - databricks
  - error-message
  - sub-condition
timestamp: "2026-06-19T18:27:21.745Z"
---

# INITIAL_SNAPSHOT Sub-Condition

The **INITIAL_SNAPSHOT sub-condition** is a specific error condition within the DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE Error Class|DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE error class in Databricks. It occurs when a Delta source skip offset operation attempts to use an offset that represents an initial snapshot of the streaming source, which is not permitted.

## Error Message

When this sub-condition is triggered, the system returns the following error:

```
Invalid skip offset range for Delta source range=[<startOffset>, <endOffset>). Fix this offset range and try again.
```

With the specific sub-condition message:

```
Offsets cannot be initial snapshot offsets (isInitialSnapshot must be false).
```

^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Cause

The INITIAL_SNAPSHOT sub-condition is raised when a streaming query attempts to skip offsets that are marked as initial snapshot offsets. In Delta Lake streaming, offsets can represent either:
- An initial snapshot of the source data, or
- A subsequent change data feed offset

The system requires that `isInitialSnapshot` must be set to `false` for the offsets being skipped. This means you cannot skip over offsets that represent the initial snapshot of the Delta source table. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, ensure that the offset range you are trying to skip does not include initial snapshot offsets. The offset range must contain only non-initial snapshot offsets (where `isInitialSnapshot` is `false`). ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE Error Class|DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE error class — The parent error class containing this sub-condition
- Incremental processing with Delta Lake — Streaming semantics in Delta Lake
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — The feature that generates non-snapshot offsets
- Structured Streaming on Databricks — Overview of streaming on the platform

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
