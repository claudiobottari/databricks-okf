---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 01d7338885069b8853b2dd2d857f7e0b3065eb5c1a9d904393b5f35ccdf562b4
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - base_index-offset-index-requirement
    - BOIR
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: BASE_INDEX Offset Index Requirement
description: The requirement that when an invalid offset index occurs in a Delta streaming skip offset range, the index must be of the form BASE_INDEX (baseIndex)
tags:
  - delta-lake
  - streaming
  - offsets
  - indexing
timestamp: "2026-06-19T10:08:20.621Z"
---

# BASE_INDEX Offset Index Requirement

The **BASE_INDEX Offset Index Requirement** is a validation condition in Delta Streaming that occurs when a skip-offset range specifies an offset index that is not the required base index. This requirement is enforced by the `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE` error class.

## Error Details

When the `INVALID_INDEX` subcondition is raised, the error returns the following message:

```
Offset index must be `BASE_INDEX (<baseIndex>).
```

This indicates that the offset index provided in a skip-offset range does not match the expected baseline index (`<baseIndex>`). The offset range must use the correct base index for the skip operation to succeed. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Related Error Conditions

Other subconditions of the same error class include:

- EVENT_TIME_PRESENT – Offsets cannot contain event time data (eventTimeMillis must be empty).
- INITIAL_SNAPSHOT – Offsets cannot be initial snapshot offsets (isInitialSnapshot must be false).

These all share the SQLSTATE `42616` (syntax error or access rule violation). ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Resolution

To resolve the `INVALID_INDEX` condition, ensure that the offset index in the skip range matches the required `BASE_INDEX` value. Review the offset metadata for the source stream and supply the correct base index as the starting point of the range. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Related Concepts

- Delta Streaming
- [Skip Offsets](/concepts/delta-streaming-skip-offsets.md)
- Delta Source Range Validation

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
