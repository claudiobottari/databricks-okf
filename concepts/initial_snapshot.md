---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 709a47cc6cbfcf6f0359130c13386bde3cea1bd2b303ce6804e62d42daaf5335
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - initial_snapshot
    - INITIAL_SNAPSHOT
    - Initial Snapshot
    - initial snapshot
    - isInitialSnapshot
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: INITIAL_SNAPSHOT
description: A sub-condition of the DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE error stating that skip offsets must not be initial snapshot offsets
tags:
  - error-messages
  - databricks
  - streaming
  - snapshots
timestamp: "2026-06-19T15:07:26.351Z"
---

# INITIAL_SNAPSHOT

The **INITIAL_SNAPSHOT** subcondition is one of the specific error conditions under the `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE` error class (SQLSTATE 42616) in Delta Streaming. It flags that the provided skip offset range contains offsets that are designated as initial snapshot offsets, which are not permitted when skipping offsets in a streaming query. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Error Message

When this subcondition fires, the error message states: "Offsets cannot be initial snapshot offsets (isInitialSnapshot must be false)." ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Cause

The error occurs because the offset range specified for skipping includes offsets that have the `isInitialSnapshot` property set to `true`. Delta streaming only allows skipping of offsets that belong to regular processed batches; initial snapshot offsets (the first read of a Delta source) cannot be skipped. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, modify the skip offset range so that it does not contain any offsets with `isInitialSnapshot = true`. The overall error message instructs: "Fix this offset range and try again." ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE – The parent error class for this subcondition.
- Delta Streaming – The streaming engine for Delta tables that processes offset ranges.
- BASE_INDEX in Delta Streaming Offsets|Offset skipping in Delta streaming – The mechanism used to skip specific offsets during stream processing.
- INITIAL_SNAPSHOT|isInitialSnapshot – The property that marks an offset as belonging to an initial snapshot.

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
