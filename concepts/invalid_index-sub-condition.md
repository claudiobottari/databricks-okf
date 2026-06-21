---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 615ac7ef0ba2ff9103ec7b5871fffeaef0e90e26b39a7d09ecc780865300db00
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - invalid_index-sub-condition
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: INVALID_INDEX sub-condition
description: A specific reason for the DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE error, indicating that the offset index must match the expected BASE_INDEX value.
tags:
  - databricks
  - error-message
  - sub-condition
timestamp: "2026-06-19T18:27:06.184Z"
---

# INVALID_INDEX sub-condition

The **INVALID_INDEX sub-condition** is a specific error variant under the `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE` error class in Databricks. It indicates that the offset index provided in a skip offset range for a Delta source does not match the expected base index.

## Error Message

```
Offset index must be BASE_INDEX (<baseIndex>).
```

The `<baseIndex>` placeholder is replaced with the actual base index that the offset must conform to.

## Context

This sub-condition occurs when using the [skip offsets](/concepts/delta-streaming-skip-offsets.md) feature in a Delta Lake streaming source. The skip offsets mechanism allows users to define a range of offsets to skip during streaming reads. The offset range is specified as `[<startOffset>, <endOffset>)`. When the `INVALID_INDEX` sub-condition fires, it means that the index value within one of the offsets (most likely the start or end offset) is not equal to the required `BASE_INDEX` for that stream. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

The `BASE_INDEX` typically refers to the foundational offset index from which the streaming source begins its offset numbering. Offsets for a particular stream share a common base index, and any offset supplied in a skip range must reference that same base. If an offset from a different stream or a differently numbered sequence is used, the `INVALID_INDEX` sub-condition is raised.

## Related Sub-conditions

The `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE` error class has two other sub-conditions:

- **EVENT_TIME_PRESENT**: Offsets must not contain event time metadata (`eventTimeMillis` must be empty).
- **INITIAL_SNAPSHOT**: Offsets must not be initial snapshot offsets (`isInitialSnapshot` must be false).

These sub-conditions, together with `INVALID_INDEX`, cover common validation failures for skip offset arguments. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Resolution

To resolve the `INVALID_INDEX` sub-condition, ensure that the offset index in the skip range matches the `BASE_INDEX` expected by the Delta streaming source. This may involve:

1. Checking the actual base index of the stream (e.g., by inspecting the stream metadata or the latest committed offset).
2. Adjusting the offset range so that its index aligns with the base index.
3. Verifying that the offset references the correct streaming query and checkpoint location.

If the error persists, consult the [Delta Streaming Skip Offsets](/concepts/delta-streaming-skip-offsets.md) documentation or use the streaming query's offset metadata to determine the correct base index.

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
