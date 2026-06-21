---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6230f8bdfee48638badc0f758143661f14f13a6f01fb3b735afac5f611a148cb
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - event_time_present
    - EVENT_TIME_PRESENT
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: EVENT_TIME_PRESENT
description: A sub-condition of the DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE error stating that skip offsets must not contain event timestamps
tags:
  - error-messages
  - databricks
  - streaming
  - event-time
timestamp: "2026-06-19T15:07:21.133Z"
---

# EVENT_TIME_PRESENT

**EVENT_TIME_PRESENT** is a specific sub-condition of the DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE error class (SQLSTATE 42616) in Databricks. It occurs when a user provides an offset that includes an event time (`eventTimeMillis` is non-empty) within a Delta streaming skip operation, which is not allowed by the system. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Error Context

When you attempt to skip offsets in a Delta Streaming source, you must supply a valid offset range `[<startOffset>, <endOffset>)`. Each offset in that range must satisfy several constraints, one of which is that event time metadata must be absent. If any offset contains a non-empty `eventTimeMillis`, the **EVENT_TIME_PRESENT** condition is triggered and the operation fails with a `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE` error. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, ensure that the offsets you provide for skipping do not include event time information. Specifically, the `eventTimeMillis` field in your offset specification must be empty or omitted for every offset in the range. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

You can review the exact offset range you passed and remove the event time from each offset entry before retrying the operation.

## Related Concepts

- DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE – The parent error class that includes this condition along with `INITIAL_SNAPSHOT` and `INVALID_INDEX`.
- Delta Streaming – The streaming engine on Delta Lake.
- Offset Management in Delta Streaming – How offsets are used to control progress in streaming queries.
- [SQLSTATE 42616](/concepts/sqlstate-42616.md) – The SQL standard error code for syntax or access rule violations.

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
