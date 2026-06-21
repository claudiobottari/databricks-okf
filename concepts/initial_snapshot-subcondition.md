---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 21c46a9cbad5e9d3d8a654ef0e0511b4b94ffc9155a58f63e94a993701fbada4
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - initial_snapshot-subcondition
    - INITIAL_SNAPSHOT error condition
    - INITIAL_SNAPSHOT subcondition
    - INITIAL_SNAPSHOT Sub-Condition|INITIAL_SNAPSHOT
    - Process Initial Snapshot Without Dropping Data
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: INITIAL_SNAPSHOT Subcondition
description: A sub-error of DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE indicating skip offset range is invalid because the offsets are initial snapshot offsets (isInitialSnapshot must be false).
tags:
  - error-message
  - delta-lake
  - streaming
timestamp: "2026-06-18T15:22:12.538Z"
---

# INITIAL_SNAPSHOT Subcondition

The **INITIAL_SNAPSHOT subcondition** is one of the possible causes of the DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE Error Class|DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE error class (SQLSTATE 42616). It indicates that the offset range specified for a [Delta Lake](/concepts/delta-lake.md) streaming source includes offsets that correspond to the initial snapshot of the table, which is not permitted for skip operations. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Cause

The error occurs when a user attempts to skip a range of offsets in a Delta streaming source, and the range contains offsets from the initial snapshot. Initial snapshot offsets are special markers that represent the state of the table at the start of the stream before any new data arrives. The streaming engine requires that `isInitialSnapshot` must be `false` for any offset being skipped. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Error Message

When this subcondition is triggered, the error message reports:

```
Offsets cannot be initial snapshot offsets (isInitialSnapshot must be false).
```

## Resolution

Adjust the offset range so that it does not include any offsets from the initial snapshot. Ensure that the `startOffset` and `endOffset` parameters of the skip range have `isInitialSnapshot = false`. For further guidance, refer to the documentation for the parent error class.

## Related Concepts

- DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE Error Class|DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE error class
- [SQLSTATE 42616](/concepts/sqlstate-42616.md)
- Delta Lake streaming – How streaming reads work with Delta sources
- Offset management in Delta streaming – Skipping and managing offsets

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
