---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d942752ad9797f21b24a9ec7aae3f9060e4742908ecabfb7f8bfd5165da13cc1
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - base_index-in-delta-streaming-offsets
    - BIDSO
    - Offset skipping in Delta streaming
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: BASE_INDEX in Delta Streaming Offsets
description: A required offset index format for Delta streaming skip offsets, validated as part of the INVALID_INDEX subcondition of the DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE error.
tags:
  - delta-lake
  - streaming
  - offset-management
timestamp: "2026-06-18T15:22:38.861Z"
---

# BASE_INDEX in Delta Streaming Offsets

**BASE_INDEX** is a required offset index type used in skip offset ranges for Delta source streaming. When the `INVALID_INDEX` subtype of the `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE` error occurs, the error message specifies that the offset index must be `BASE_INDEX (<baseIndex>)`. This indicates that the offset range provided does not use a valid base index, which is necessary for proper offset skipping behavior. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Error Context

The `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE` error (SQLSTATE: 42616) is raised when an invalid skip offset range is specified for a Delta source. The error message follows the pattern:

```
Invalid skip offset range for Delta source range=[<startOffset>, <endOffset>). Fix this offset range and try again.
```

The error includes three possible sub-conditions:

- `EVENT_TIME_PRESENT` – Offsets cannot contain event time (`eventTimeMillis` must be empty).
- `INITIAL_SNAPSHOT` – Offsets cannot be initial snapshot offsets (`isInitialSnapshot` must be false).
- `INVALID_INDEX` – The offset index must be `BASE_INDEX (<baseIndex>`).

The `INVALID_INDEX` subtype specifically requires that the offset index used in the range be a `BASE_INDEX` with a valid base index value. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Understanding BASE_INDEX

In Delta streaming offsets, a `BASE_INDEX` serves as a fundamental identifier for the streaming position. It is distinct from other offset representations such as event-time-based offsets or initial snapshot offsets. When constructing a skip offset range (e.g., for resuming a stream from a specific point), the offsets must reference a `BASE_INDEX` rather than a different type. The exact `<baseIndex>` value depends on the streaming source's internal indexing scheme.

## Resolution

To resolve the `INVALID_INDEX` sub-error, ensure that both the start and end offsets in the skip range use a `BASE_INDEX` type. If you are manually specifying offsets (e.g., through checkpoint manipulation or custom streaming logic), adjust them to conform to the required format. The following general steps apply:

1. Retrieve the correct base index from the Delta streaming source (e.g., from a valid checkpoint or source state).
2. Replace any non-base indices (such as initial snapshot offsets or event-time offsets) with the appropriate `BASE_INDEX`.
3. Re-submit the skip offset range.

If you are using a streaming framework (such as [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md)), avoid manually overriding offsets unless you fully understand the required format. Refer to the [Delta Lake](/concepts/delta-lake.md) documentation on streaming offset management for details.

## Related Concepts

- Delta Lake streaming – The underlying technology for streaming from Delta tables.
- [Skip offsets](/concepts/delta-streaming-skip-offsets.md) – A mechanism to skip a range of offsets during stream restarts.
- Streaming checkpoint management – How offsets are stored and restored in streaming applications.
- EVENT_TIME_PRESENT Subcondition|EVENT_TIME_PRESENT error condition – Another subtype of the same error, involving event-time offsets.
- INITIAL_SNAPSHOT Subcondition|INITIAL_SNAPSHOT error condition – Subtype involving snapshot offsets.

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
