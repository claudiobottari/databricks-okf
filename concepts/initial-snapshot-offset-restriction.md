---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0ddd6be4441916575b487f6010bdb0db7131f625a30ec00164737bbf7716a712
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - initial-snapshot-offset-restriction
    - ISOR
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: Initial Snapshot Offset Restriction
description: The constraint that offsets used in Delta skip offset ranges cannot be initial snapshot offsets (isInitialSnapshot must be false)
tags:
  - delta-lake
  - streaming
  - offsets
  - snapshots
timestamp: "2026-06-19T10:08:26.146Z"
---

# Initial Snapshot Offset Restriction

**Initial Snapshot Offset Restriction** refers to the error condition `INITIAL_SNAPSHOT` within the `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE` error class. It occurs when a streaming query attempts to use an offset range that includes an offset marked as an initial snapshot offset, which is not permitted. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Error Details

The error is raised with [SQLSTATE: 42616](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-42-syntax-error-or-access-rule-violation) and reports the specific sub-error `INITIAL_SNAPSHOT`. The full message is:

```
Invalid skip offset range for Delta source range=[<startOffset>, <endOffset>). Fix this offset range and try again.
```

The `INITIAL_SNAPSHOT` variant adds the explanation:

> Offsets cannot be initial snapshot offsets (isInitialSnapshot must be false).

^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Cause

The `DELTA_STREAMING_SKIP_OFFSETS` functionality allows a streaming read to skip a range of offsets in a Delta source. When providing a skip offset range, each offset must have certain metadata properties. The `INITIAL_SNAPSHOT` error indicates that one of the offsets in the range has the `isInitialSnapshot` flag set to `true`. Initial snapshot offsets represent the starting state of a Delta table (the snapshot at the time the stream begins); they cannot be used in a skip offset range because they do not correspond to a specific change (transaction) in the change data feed. Only offsets that represent actual changes (i.e., non‑snapshot offsets) are valid for skipping. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Resolution

To resolve the error, ensure that all offsets in the specified range have `isInitialSnapshot` set to `false`. The guidance in the error message is to fix the offset range and try again. In practice, this means constructing the skip offset range using only offsets that correspond to actual Delta transaction versions (commits), not the initial snapshot offset. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Related Concepts

- [DELTA_STREAMING_SKIP_OFFSETS](/concepts/delta-streaming-skip-offsets.md) – The feature for skipping offsets in a Delta streaming source.
- Delta Streaming – Streaming reads from Delta tables using change data feed.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – The mechanism that provides row-level changes for Delta tables.
- Streaming Offset Management – How Databricks tracks and manages streaming offsets.
- [SQLSTATE 42616](/concepts/sqlstate-42616.md) – The SQL state code for this error class (syntax error or access rule violation).

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
