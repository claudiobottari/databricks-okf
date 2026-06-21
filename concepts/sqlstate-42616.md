---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0e5363827fca8a181c0246fb703f2773351da80e3f40e5044c8cd0706fe118da
  pageDirectory: concepts
  sources:
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sqlstate-42616
  citations:
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: SQLSTATE 42616
description: A SQL standard error code in Class 42 (Syntax Error or Access Rule Violation) used by the DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE error condition in Databricks.
tags:
  - databricks
  - sqlstate
  - error-code
  - sql
timestamp: "2026-06-19T18:27:23.728Z"
---

```markdown
---
title: SQLSTATE 42616
summary: A SQL state error (class 42) that occurs when a Delta Streaming operation specifies an invalid offset skip range. The error condition is `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE`.
sources:
  - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
kind: concept
tags:
  - delta-streaming
  - error
  - sqlstate
---

# SQLSTATE 42616

**SQLSTATE 42616** is an error code in class 42 (Syntax Error or Access Rule Violation) that is raised when a Delta Streaming source is given a skip‑offset range that fails validation. The associated error condition is `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE`. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Error Message

The error displays the following message:

```
Invalid skip offset range for Delta source range=[<startOffset>, <endOffset>). Fix this offset range and try again.
```

^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Sub‑Conditions

Three sub‑conditions provide more specific context about why the offset range is invalid. Each sub‑condition has its own message and interpretation.

### EVENT_TIME_PRESENT

**Message:** `Offsets cannot have event time (eventTimeMillis must be empty).`

This sub‑condition occurs when the skip‑offset range includes event time metadata (`eventTimeMillis`). The field must be empty in the skip‑offset specification. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

### INITIAL_SNAPSHOT

**Message:** `Offsets cannot be initial snapshot offsets (isInitialSnapshot must be false).`

This sub‑condition occurs when the skip‑offset range references the initial snapshot offset. The `isInitialSnapshot` flag must be set to `false`. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

### INVALID_INDEX

**Message:** `Offset index must be BASE_INDEX (<baseIndex>).`

This sub‑condition occurs when the offset index in the skip range does not match the expected base index of the streaming source. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Cause

The error is triggered when a user‑specified offset range provided to a Delta Streaming source violates validation rules. The specific violation is identified by one of the three sub‑conditions described above. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Resolution

To resolve the error, adjust the skip‑offset range according to the sub‑condition that fired:

- For **EVENT_TIME_PRESENT**, ensure that `eventTimeMillis` is empty.
- For **INITIAL_SNAPSHOT**, set `isInitialSnapshot` to `false`.
- For **INVALID_INDEX**, change the offset index to match the required `BASE_INDEX` value.

After fixing the range, retry the streaming operation. ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

## Related Concepts

- Delta Streaming
- Class 42 Syntax Error or Access Rule Violation
- Delta Source Offsets

## Sources

- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
