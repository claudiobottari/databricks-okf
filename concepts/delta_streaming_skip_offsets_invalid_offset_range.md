---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5677b906b743097b555c6a303a64d230af74b91ab369f9ab1e27e4a229cb5afb
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_streaming_skip_offsets_invalid_offset_range
    - DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE
description: A Databricks error class (SQLSTATE 42616) raised when a user-specified skip offset range for a Delta streaming source is invalid.
tags:
  - databricks
  - error-message
  - delta-streaming
  - streaming
timestamp: "2026-06-19T18:27:08.170Z"
---

```markdown
---
title: DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE
summary: A Databricks error condition raised when an invalid skip offset range is provided to a Delta streaming source
sources:
  - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:55:25.432Z"
updatedAt: "2026-06-19T15:07:34.301Z"
tags:
  - error-messages
  - databricks
  - delta-lake
  - streaming
aliases:
  - delta_streaming_skip_offsets_invalid_offset_range
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE

The **DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE** error occurs when a Delta Streaming source operation specifies an invalid skip offset range. The error message reports the problematic range in the format `range=[<startOffset>, <endOffset>)` and requests the user to fix the offset range and try again. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Error Details

- **SQLSTATE**: 42616 (Syntax error or access rule violation)
- **Error class**: `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE`

^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Sub‑Conditions

The error can be raised under three distinct sub‑conditions, each providing a specific reason.

### EVENT_TIME_PRESENT

**Offsets cannot have event time (eventTimeMillis must be empty).**

This sub‑condition triggers when the skip offset range includes event time information. The offsets used for skipping must not contain event timestamps. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

### INITIAL_SNAPSHOT

**Offsets cannot be initial snapshot offsets (isInitialSnapshot must be false).**

This sub‑condition occurs when the skip offset range references initial snapshot offsets. The offsets provided for skipping must not be initial snapshot offsets. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

### INVALID_INDEX

**Offset index must be `BASE_INDEX (<baseIndex>)`.**

This sub‑condition arises when the offset index does not match the expected base index for the skip operation. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Troubleshooting

When encountering this error, examine the offset range shown in the error message and ensure the following:

1. **No event time** is included in the skip offsets — remove any `eventTimeMillis` values.
2. **Initial snapshot offsets** are not used — confirm that `isInitialSnapshot` is set to `false`.
3. **Offset index matches** the expected base index for the streaming query.

Correct the offset range according to the specific sub‑condition reported, then retry the operation. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Related Concepts

- Delta Streaming – The streaming source that produces these offsets.
- [[Structured Streaming on Shared Tables|Structured Streaming]] – The underlying streaming engine in Databricks.
- Error Classes in Databricks – General documentation on Databricks error condition formatting.
- SQLSTATE Error Codes – The SQLSTATE classification system (Class 42).

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
