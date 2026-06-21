---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d838e6048d93100a2b40207b907ae742a402c5045a3f7f560527e962d9c75a92
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - event_time_present-sub-condition
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: EVENT_TIME_PRESENT sub-condition
description: A specific reason for the DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE error, indicating that offsets in the skip range must not have event time metadata (eventTimeMillis must be empty).
tags:
  - databricks
  - error-message
  - sub-condition
timestamp: "2026-06-19T18:26:59.144Z"
---

# EVENT_TIME_PRESENT Sub-Condition

**EVENT_TIME_PRESENT** is a sub-condition of the `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE` error condition in Databricks. It indicates that an offset range specified for skipping in a Delta streaming source contains event time information, which is not permitted. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Error Context

The `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE` error occurs when an invalid skip offset range `[<startOffset>, <endOffset>)` is provided for a Delta streaming source. The `EVENT_TIME_PRESENT` sub-condition specifically states that offsets in the range must not include event time data — the `eventTimeMillis` field must be empty. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Error Message

When this sub-condition is triggered, the error message appears as:

```
EVENT_TIME_PRESENT: Offsets cannot have event time (eventTimeMillis must be empty).
```

^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Related Sub-Conditions

The `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE` error class includes two other sub-conditions: ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

- INITIAL_SNAPSHOT Subcondition|INITIAL_SNAPSHOT Sub-Condition|INITIAL_SNAPSHOT — Offsets cannot be initial snapshot offsets (`isInitialSnapshot` must be false).
- INVALID_INDEX Subcondition|INVALID_INDEX Sub-Condition|INVALID_INDEX — Offset index must match the base index.

## Resolution

To resolve this error, ensure the offset range provided for skipping in your Delta streaming source query does not include event time information. The `eventTimeMillis` field in the offset specification must be empty. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Related Concepts

- Delta Streaming — The streaming source mechanism in Delta Lake.
- DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE Error Class — The parent error class containing this sub-condition.
- Structured Streaming in Databricks — The broader streaming framework.
- [SQLSTATE 42616](/concepts/sqlstate-42616.md) — The SQL standard error code associated with this condition.

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
