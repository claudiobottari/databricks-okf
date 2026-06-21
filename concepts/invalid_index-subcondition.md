---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a3da850fffcf7db29936d6f21fb45e3df34d66173c99b50f9ec8fd046724ee8e
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - invalid_index-subcondition
    - INVALID_INDEX subcondition
    - INVALID_INDEX Sub-Condition|INVALID_INDEX
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: INVALID_INDEX Subcondition
description: A sub-error of DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE indicating the offset index must be BASE_INDEX (<baseIndex>).
tags:
  - error-message
  - delta-lake
  - streaming
timestamp: "2026-06-18T15:22:16.596Z"
---

# INVALID_INDEX Subcondition

The **INVALID_INDEX subcondition** is one of the specific causes of the DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE Error Class|DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE error class in Databricks. This error occurs when a user attempts to specify an invalid skip offset range for a Delta source in a Structured Streaming query, and the INVALID_INDEX subcondition indicates that the offset index does not match the required base index value. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Error Context

The full error message for the parent error class is:

```
Invalid skip offset range for Delta source range=[<startOffset>, <endOffset>). Fix this offset range and try again.
```

The INVALID_INDEX subcondition produces the following additional detail:

```
Offset index must be BASE_INDEX (<baseIndex>).
```

^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Subcondition Details

When Databricks validates a custom offset range provided to a Delta streaming source, it checks that the offset index conforms to the expected `BASE_INDEX` for that source. If the provided index deviates, the INVALID_INDEX subcondition is raised. The `baseIndex` parameter in the message indicates the exact index that should have been used. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

The INVALID_INDEX subcondition is one of three possible subconditions for this error class. The other subconditions are:

- **EVENT_TIME_PRESENT** – Indicates that offsets cannot have an event time; `eventTimeMillis` must be empty.
- **INITIAL_SNAPSHOT** – Indicates that offsets cannot be initial snapshot offsets; `isInitialSnapshot` must be false.

Each subcondition helps narrow down the specific validation failure so that the user can correct the offset range accordingly. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE Error Class|Delta streaming skip offsets invalid offset range error class – The parent error class containing this subcondition.
- Structured Streaming in Databricks – The streaming framework where Delta source offset skipping is applied.
- Delta source offset configuration – How users specify custom offset ranges for Delta streaming sources.

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
