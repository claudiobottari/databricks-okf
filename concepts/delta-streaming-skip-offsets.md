---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d32cfbcf6525f106f6ad163e9ea4c653f6b3fe263764b8122dd21d767b0d6ac
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-streaming-skip-offsets
    - DSSO
    - DELTA_STREAMING_SKIP_OFFSETS
    - Streaming skip offsets
    - Skip Offsets
    - Skip offsets
    - skip offsets
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: Delta Streaming Skip Offsets
description: A mechanism in Databricks Delta Lake streaming that allows users to specify an offset range to skip when reading from a Delta source, enabling selective processing of data.
tags:
  - databricks
  - delta-streaming
  - streaming
  - offset-management
timestamp: "2026-06-19T18:27:02.021Z"
---

# Delta Streaming Skip Offsets

**Delta Streaming Skip Offsets** is a mechanism in Delta Lake that allows structured streaming reads to skip specific offset ranges when consuming data from a Delta source. This feature provides granular control over which portions of the transaction log are processed during streaming operations.^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Overview

When reading from a Delta table in a structured streaming workload, the stream tracks its progress using offsets that represent positions in the transaction log. The skip offsets feature allows users to specify ranges of offsets to skip, effectively telling the stream to ignore certain portions of the data. This capability can be useful for recovering from processing errors, reprocessing specific data ranges, or managing stream state.^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Error Condition: DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE

When an invalid skip offset range is provided, Databricks raises the **DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE** error. This error has SQLSTATE 42616 (class 42: syntax error or access rule violation). The general error message is:^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

```
Invalid skip offset range for Delta source range=[<startOffset>, <endOffset>). Fix this offset range and try again.
```

### Sub-conditions

The error is raised under three specific circumstances, each identified by a distinct sub-condition name.^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

#### EVENT_TIME_PRESENT

Offsets cannot have an `eventTimeMillis` value. When a skip offset range is supplied with a non-empty event time, the engine rejects it with this sub-condition.^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

#### INITIAL_SNAPSHOT

Offsets must not represent an initial snapshot. The `isInitialSnapshot` flag must be set to `false`. If a skip offset range refers to an offset that marks the beginning of the stream (such as offset 0 with no preceding data), this sub-condition is raised.^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

#### INVALID_INDEX

The offset index must equal the expected base index. The error message indicates the required base index: `Offset index must be BASE_INDEX (<baseIndex>).` This sub-condition occurs when the index of the provided offset does not match the expected base index for the skip operation.^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Resolution

A single generic resolution applies to all sub-conditions: correct the offset range and retry. The exact corrective action depends on which sub-condition is triggered:^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

- For **EVENT_TIME_PRESENT**, ensure the offset range does not include an `eventTimeMillis` value.
- For **INITIAL_SNAPSHOT**, use offsets that refer to a non-initial snapshot position.
- For **INVALID_INDEX**, adjust the offset index to match the required base index.

Databricks documentation does not provide a finer-grained remediation per sub-condition beyond the general guidance to fix the offset range.^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Related Concepts

- Delta Lake Streaming – The streaming engine that consumes Delta tables.
- Streaming Offsets – The mechanism that tracks progress in a Delta stream.
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) – The underlying Apache Spark streaming framework.
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) – The log that tracks all changes to a Delta table.
- Delta Streaming Configuration – Options for configuring Delta source streaming behavior.
- Error Classes in Databricks – The error classification system that includes this error condition.

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
