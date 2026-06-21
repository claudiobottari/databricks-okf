---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 25f7a1d6f17c817cb953890260cdfe999d5ec33d72e80273a9f793e6662a6b10
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-source-streaming-offsets
    - DSSO
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: Delta Source Streaming Offsets
description: Conceptual mechanism by which Delta streaming sources track and skip processing positions via offset ranges
tags:
  - delta-lake
  - streaming
  - offsets
  - databricks
timestamp: "2026-06-19T15:07:23.029Z"
---

---
title: Delta Source Streaming Offsets
summary: An error condition raised when an invalid offset range is specified for skip offsets in a Delta source streaming query.
sources:
  - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:30:00.000Z"
updatedAt: "2026-06-20T10:30:00.000Z"
tags:
  - databricks
  - error
  - streaming
  - delta
aliases:
  - delta-streaming-skip-offsets-invalid-offset-range-error
  - DSIOIR
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Delta Source Streaming Offsets

**Delta Source Streaming Offsets** refers to the mechanism used by [Delta Lake](/concepts/delta-lake.md) in [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) queries to skip a range of already-processed offsets. The `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE` error condition is raised when the provided skip offset range is invalid for the Delta source. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Error Overview

The error is raised with SQLSTATE `42616` and the following message:

```
Invalid skip offset range for Delta source range=[<startOffset>, <endOffset>). Fix this offset range and try again.
```

^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

This error occurs when a streaming query attempts to skip offsets (e.g., via the `skipOffsets` option) but the specified range does not meet the required validity constraints. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Sub‑Conditions

The error includes three distinct sub‑conditions that provide more detail about why the offset range is invalid:

### EVENT_TIME_PRESENT

Offsets must **not** have an event time associated with them. If the offset record includes a non‑empty `eventTimeMillis` field, this sub‑condition is triggered. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

### INITIAL_SNAPSHOT

Offsets must **not** be initial snapshot offsets. The `isInitialSnapshot` flag must be `false`. Trying to skip offsets that correspond to the initial snapshot of the Delta table is not allowed. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

### INVALID_INDEX

The offset index must be exactly `BASE_INDEX` (`<baseIndex>`). If the index in the provided offset range does not match the expected base index, this sub‑condition is raised. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Context and Usage

The skip offsets feature is typically used to reprocess or ignore a section of the stream’s offset history when resuming a [Streaming Source](/concepts/delta-lake-as-a-streaming-source-and-sink.md). A valid offset range must be constructed manually only when the user is certain of the offset format. The `skipOffsets` option expects a JSON string representing a map of source ID to an offset range. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Related Concepts

- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) – The high‑level streaming API in Apache Spark.
- [Delta Lake](/concepts/delta-lake.md) – The transactional storage layer underlying the streaming source.
- Offset Management – How streaming queries track and skip processed data.
- [Streaming Source](/concepts/delta-lake-as-a-streaming-source-and-sink.md) – The abstraction for reading continuously from a data source.
- Error Classes in Databricks – The classification system for runtime errors.

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
