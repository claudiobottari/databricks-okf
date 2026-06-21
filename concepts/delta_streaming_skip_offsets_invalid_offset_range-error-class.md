---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 032feabd6538be8d1b65d6a87c50998d88e164fa030f63de8facb91b1d70ed77
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_streaming_skip_offsets_invalid_offset_range-error-class
    - DEC
    - DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE Error Class
    - DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE error class
    - Delta streaming skip offsets invalid offset range error class
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE Error Class
description: A Databricks error class raised when an invalid skip offset range is specified for a Delta streaming source, with SQLSTATE 42616
tags:
  - databricks
  - error-messages
  - delta-lake
  - streaming
timestamp: "2026-06-19T10:08:13.397Z"
---

# DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE Error Class

The **DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE** error condition occurs when a [Delta Lake](/concepts/delta-lake.md) streaming source is provided with an invalid offset range to skip. The error returns with SQLSTATE **42616** (a class 42 syntax error or access rule violation) and identifies the specific sub-condition that caused the failure. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Error Message

```
Invalid skip offset range for Delta source range=[<startOffset>, <endOffset>). Fix this offset range and try again.
```

^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Sub-Error Conditions

The error class includes three sub-conditions that pinpoint the exact reason for the invalid offset range:

### EVENT_TIME_PRESENT

**Offsets cannot have event time (eventTimeMillis must be empty).** The provided offset metadata contains an `eventTimeMillis` field that is not empty, which is not allowed when skipping offsets. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

### INITIAL_SNAPSHOT

**Offsets cannot be initial snapshot offsets (isInitialSnapshot must be false).** The offset range uses an initial snapshot offset, which is not valid for skip operations. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

### INVALID_INDEX

**Offset index must be `BASE_INDEX (<baseIndex>`).** The index specified in the offset range does not match the required base index for the Delta source. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Cause

This error is raised when a [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) job attempts to skip offsets in a Delta source using an incorrectly formatted or semantically invalid offset range. The offset range may contain illegal event time metadata, use initial snapshot offsets instead of regular offsets, or refer to an index that does not match the expected base index for the Delta table.

## Resolution

1. **Check the offset range format.** Verify that the start and end offsets are valid numeric values and that the range is properly closed/open: `[<startOffset>, <endOffset>)`.
2. **Remove event time.** Ensure that `eventTimeMillis` is empty in the offset metadata.
3. **Use non-initial-snapshot offsets.** Ensure that `isInitialSnapshot` is `false` in the offset metadata.
4. **Use the correct base index.** Verify that the offset index matches the required `BASE_INDEX` value for the Delta source.

After fixing the offset range, restart the streaming query.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format for the streaming source.
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) – The streaming engine that reads from Delta tables.
- Error classes in Databricks – General framework for error classification.
- SQLSTATE – Standard SQL state codes; 42616 belongs to class 42 (syntax error or access rule violation).

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
