---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2fced776faa9c7904f44d40069e64d1acf3835387cec8bda8f8db8e7d91ccd8e
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - event_time_present-subcondition
    - EVENT_TIME_PRESENT error condition
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: EVENT_TIME_PRESENT Subcondition
description: A sub-error of DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE indicating skip offset range is invalid because the offset contains an event time (eventTimeMillis must be empty).
tags:
  - error-message
  - delta-lake
  - streaming
timestamp: "2026-06-18T15:22:19.038Z"
---

# EVENT_TIME_PRESENT Subcondition

The **EVENT_TIME_PRESENT subcondition** is one of the possible causes of the DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE error in Delta Lake streaming. It indicates that the offset range provided to a `skipOffsets` operation contains an event time (i.e., `eventTimeMillis` is non-empty) when the offset specification does not allow it. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Error Context

The full error is reported as:

```
DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE
```

This error occurs when an invalid offset range is specified for a [Delta source](/concepts/deltatablesource.md) during a streaming read. The subcondition `EVENT_TIME_PRESENT` specifically describes the violation: the offset must not carry event-time metadata. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Explanation

When using `skipOffsets` to control which offsets a streaming query processes, the offset range is defined by start and end offsets. These offsets may include optional fields such as `eventTimeMillis`. For the `EVENT_TIME_PRESENT` subcondition, the rule is:

> Offsets cannot have event time (`eventTimeMillis` must be empty). ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

In other words, if the offset range includes an event timestamp (e.g., when trying to skip offsets based on event-time boundaries), Delta Lake rejects it because the skip-offset mechanism for Delta sources does not support event-time filtering. Only logical offset indices are valid. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, ensure that the offset specification used in `skipOffsets` does not include the `eventTimeMillis` field. The offsets must be pure logical offsets without event-time markers. For example, when denoting a skip range, provide only the starting and ending index values without any event-time metadata:

```python
# Incorrect (includes eventTimeMillis):
spark.readStream.format("delta").option("skipOffsets", "...")

# Correct (only logical offsets):
```

Check the offset format expected by your streaming configuration. If you need to filter by event time, consider using a streaming watermark or a standard `WHERE` clause on the event-time column instead of `skipOffsets`. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md] (inferred from context)

## Related Concepts

- [Delta source](/concepts/deltatablesource.md)
- DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE
- INITIAL_SNAPSHOT Subcondition|INITIAL_SNAPSHOT subcondition — another subcondition of the same error
- INVALID_INDEX Subcondition|INVALID_INDEX subcondition — another subcondition of the same error
- [Streaming skip offsets](/concepts/delta-streaming-skip-offsets.md) — the feature that triggers this error

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
