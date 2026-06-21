---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: af321de6f244d38676abc2ee3d8aa6143bdd2bd87f6aebe19ee30f30717bdb29
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - base_index-offset-reference
    - BOR
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: BASE_INDEX Offset Reference
description: A requirement that Delta streaming skip offset indices must be expressed as BASE_INDEX, a specific reference format for identifying offsets in a Delta source stream.
tags:
  - delta-lake
  - streaming
  - offsets
  - indexing
timestamp: "2026-06-18T11:55:40.997Z"
---

# BASE_INDEX Offset Reference

The **BASE_INDEX offset reference** describes the expected format of the `baseIndex` parameter in [Delta Streaming Skip Offsets](/concepts/delta-streaming-skip-offsets.md) when using the `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE` error condition. The error includes a sub-condition `INVALID_INDEX` that indicates the provided offset index does not match the required `BASE_INDEX` value. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Error Context

The `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE` error (SQLSTATE: 42616) occurs when an invalid skip offset range is specified for a Delta source. The error message format is:

```
Invalid skip offset range for Delta source range=[<startOffset>, <endOffset>).
Fix this offset range and try again.
```

^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

### INVALID_INDEX Sub-Condition

Under the `INVALID_INDEX` sub-condition, the error explicitly states:

```
Offset index must be `BASE_INDEX (<baseIndex>)`.
```

This means that when constructing a skip offset range for a Delta streaming source, the offset index value must conform to the `BASE_INDEX` format, which is expected to be an integer (or numeric identifier) provided in parentheses after the literal `BASE_INDEX`. The error indicates that a caller supplied an offset index that does not match the expected `BASE_INDEX` form for that particular streaming query. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Usage

The `BASE_INDEX` offset reference is part of the internal offset metadata used by [Delta Lake](/concepts/delta-lake.md) structured streaming to track progress. When manually skipping or adjusting offsets (for example, to reprocess a batch), the offset index must exactly match the `BASE_INDEX` value that the streaming source expects. Supplying an incorrect index triggers the `INVALID_INDEX` sub-error. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Resolution

To resolve the `INVALID_INDEX` error:

1. Identify the correct `baseIndex` value for the streaming query by inspecting the persisted offset metadata (e.g., from the checkpoint).
2. Ensure that any manual offset range specification uses the exact `BASE_INDEX (<baseIndex>)` format (where `<baseIndex>` is the correct integer value).
3. Avoid modifying offset indices unless fully understood; typically, offset management should be left to the Delta streaming engine. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Related Concepts

- Delta Streaming
- Delta Lake checkpointing
- Structured Streaming offsets
- Error messages in Databricks

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
