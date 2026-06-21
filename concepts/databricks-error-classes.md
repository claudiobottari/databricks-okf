---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 658448fd41d96030a8c01b4c611c4797ac728cb41d6c9e3287861b3930e82e44
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
    - delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-error-classes
    - DEC
    - Databricks Error Messages
    - Databricks error messages
    - Delta error classes
    - Error classes
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
    - file: delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md
title: Databricks Error Classes
description: A system in Databricks that organizes error conditions into classes and sub-conditions, each with specific SQLSTATE codes and resolution guidance.
tags:
  - databricks
  - error-messages
  - architecture
timestamp: "2026-06-19T15:02:36.365Z"
---

# Databricks Error Classes

**Databricks Error Classes** are a structured categorization system for runtime errors in Databricks. Each error class has a unique name (e.g., `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET`), a SQLSTATE code, and one or more sub‑conditions that describe the specific failure mode. This design lets users quickly identify the root cause and find targeted guidance for remediation.

## Structure

An error class consists of three layers: ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md, delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

- **Error class name** — a descriptive identifier, written in `UPPER_SNAKE_CASE` (e.g., `DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE`).
- **SQLSTATE** — a five‑character code (e.g., `0AKDC` or `42616`) that groups the error by general category (e.g., “Feature Not Supported”, “Syntax Error or Access Rule Violation”).
- **Sub‑conditions** — one or more named variants (e.g., `NON_DELTA`, `PATH_BASED`, `SESSION_TEMPORARY`) that refine the error message. Each sub‑condition includes its own explanation and, in many cases, a resolution hint.

## Examples

### DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET

This error occurs when an attempt to clone a Delta table with history targets a table that does not support versioned clones. The SQLSTATE is `0AKDC` (Class 0A – Feature Not Supported). ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

Sub‑conditions:

| Sub‑condition | Explanation |
|---------------|-------------|
| `NON_DELTA` | The target table is of a non‑Delta format. |
| `PATH_BASED` | A path‑based target table is not supported. |
| `SESSION_TEMPORARY` | A session‑temporary target table is not supported. |

### DELTA_STREAMING_SKIP_OFFSETS_INVALID_OFFSET_RANGE

This error is raised when a streaming skip offset range is invalid for a Delta source. The SQLSTATE is `42616` (Class 42 – Syntax Error or Access Rule Violation). ^[delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

Sub‑conditions:

| Sub‑condition | Explanation |
|---------------|-------------|
| `EVENT_TIME_PRESENT` | The offset includes an event time, which is not allowed. |
| `INITIAL_SNAPSHOT` | The offset refers to an initial snapshot offset, which is not permitted. |
| `INVALID_INDEX` | The offset index does not match the required base index. |

## Using Error Classes

When an error occurs, Databricks returns the error class name and sub‑condition. Users can: ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md, delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md]

1. Look up the error class in the documentation to see the full list of sub‑conditions.
2. Identify the sub‑condition from the error message (e.g., `NON_DELTA`).
3. Apply the resolution steps suggested for that sub‑condition.

Error classes are defined for many areas of the product, including [Delta Sharing](/concepts/delta-sharing.md), [Delta Lake](/concepts/delta-lake.md) operations, and streaming pipelines.

## Related Concepts

- SQLSTATE — Standard codes that accompany Databricks error classes.
- [Delta Sharing](/concepts/delta-sharing.md) — A data‑sharing protocol with its own set of error classes.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that generates many of the error classes.
- Troubleshooting Databricks Workflows — General approach for diagnosing errors.

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
- delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)
2. [delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws.md](/references/delta_streaming_skip_offsets_invalid_offset_range-error-condition-databricks-on-aws-1b391d37.md)
