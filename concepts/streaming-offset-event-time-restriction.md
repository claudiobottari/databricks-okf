---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5350ba66bb4ddc6389a112cd08fa25a542bc8865794ae32d77a0c59e855503fa
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-offset-event-time-restriction
    - SOETR
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: Streaming Offset Event Time Restriction
description: The constraint that streaming offsets used in Delta skip offset ranges must not contain event time (eventTimeMillis must be empty)
tags:
  - delta-lake
  - streaming
  - offsets
  - event-time
timestamp: "2026-06-19T10:08:16.922Z"
---

# Streaming Offset Event Time Restriction

**Streaming Offset Event Time Restriction** refers to the requirement that streaming offsets used in [Delta Lake](/concepts/delta-lake.md) skip‑offset ranges must have an empty event time (`eventTimeMillis` must be absent). This requirement is enforced as part of the `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE` error class and prevents event‑time metadata from being included when specifying an offset range for a Delta source. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Error Condition

When a structured streaming query attempts to process a skip‑offset range that includes event‑time information, the `EVENT_TIME_PRESENT` subtype of the error is raised with the message:

> Offsets cannot have event time (eventTimeMillis must be empty).

This indicates that the provided offset range contains a non‑empty `eventTimeMillis` field, which is not permitted. Offsets in Delta streaming are identified only by their file‑level metadata (such as version and index) and must not carry event‑time timestamps. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, ensure that the skip‑offset range specified in the streaming source configuration does not include an `eventTimeMillis` value. The range should be defined using only the allowed offset fields: the starting and ending offset identifiers (e.g., version and index), with `eventTimeMillis` omitted or set to an empty value. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Streaming Skip Offsets](/concepts/delta-streaming-skip-offsets.md) – The general mechanism for skipping a range of offsets in a Delta streaming source.
- DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE – The parent error class that includes `EVENT_TIME_PRESENT` and other validation failures.
- Structured Streaming in Databricks – Overview of streaming queries on Delta tables.
- [SQLSTATE 42616](/concepts/sqlstate-42616.md) – The associated SQL standard error code for this condition.

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
