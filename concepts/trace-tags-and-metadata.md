---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d89b6fdea119f0bc9eab1434e7b4c1d0675dda76b6549996d71e0c36f00ec4cc
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-tags-and-metadata
    - Metadata and Trace Tags
    - TTAM
    - Attach custom tags and metadata
    - Attach custom tags and metadata — Tags vs Metadata
    - Metadata vs Tags
    - Trace Tags and Attributes
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: Trace Tags and Metadata
description: "Two distinct annotation systems on traces: mutable tags (user-defined, updatable post-creation) and immutable trace_metadata (set at creation); used for environment, user ID, and other contextual information."
tags:
  - mlflow
  - tracing
  - metadata
timestamp: "2026-06-19T08:50:42.826Z"
---

# Trace Tags and Metadata

**Trace Tags and Metadata** are key-value annotations attached to MLflow [Traces](/concepts/traces.md) that provide contextual information about the execution of a GenAI agent or other traced operation. Tags and metadata serve different purposes: tags are mutable and can be updated after trace creation, while metadata is immutable and set at creation time. ^[access-trace-data-databricks-on-aws.md]

## Overview

Every MLflow [Trace](/concepts/traces.md) object contains two main components: [TraceInfo](/concepts/traceinfo.md) (metadata about the trace) and [TraceData](/concepts/tracedata.md) (the actual execution data). Tags and metadata are part of the `TraceInfo` component and allow developers to attach custom information to traces for filtering, organization, and analysis. ^[access-trace-data-databricks-on-aws.md]

## Tags

Tags are mutable key-value pairs that can be added or updated after a trace is created. They are useful for categorizing traces by environment, user, or other dynamic attributes. ^[access-trace-data-databricks-on-aws.md]

### Accessing Tags

Tags are accessed through the `trace.info.tags` property, which returns a dictionary: ^[access-trace-data-databricks-on-aws.md]

```python
# Access all tags
print("Tags:")
for key, value in trace.info.tags.items():
    print(f"  {key}: {value}")

# Access specific tags
print(f"Environment: {trace.info.tags.get('environment')}")
print(f"User ID: {trace.info.tags.get('user_id')}")
```

### Common Use Cases

- **Environment identification**: Tag traces with `environment: production`, `environment: staging`, or `environment: development` to distinguish between deployment contexts.
- **User attribution**: Attach `user_id` tags to associate traces with specific users or service principals.
- **Experiment tracking**: Tag traces with experiment names or version numbers for A/B comparison analysis.
- **Workflow categorization**: Use tags to group traces by workflow type, such as `workflow: customer_support` or `workflow: content_generation`.

## Trace Metadata

Trace metadata is an immutable set of key-value pairs that is established when the trace is created. Unlike tags, metadata cannot be modified after the trace is recorded. ^[access-trace-data-databricks-on-aws.md]

### Accessing Metadata

Metadata is accessed through the `trace.info.trace_metadata` property: ^[access-trace-data-databricks-on-aws.md]

```python
# Access all metadata
print("\nTrace metadata:")
for key, value in trace.info.trace_metadata.items():
    print(f"  {key}: {value}")

# Deprecated alias (same as trace_metadata)
print(f"Request metadata: {trace.info.request_metadata}")
```

### Common Use Cases

- **Immutable configuration**: Store configuration parameters that should not change during analysis, such as model version or system prompt hash.
- **Audit trails**: Record fixed identifiers for compliance and auditing purposes.
- **Source attribution**: Capture the originating service or pipeline that created the trace.

## Comparison: Tags vs. Metadata

| Property | Tags | Metadata |
|----------|------|----------|
| Mutability | Mutable (can be updated after creation) | Immutable (set at creation) |
| Access property | `trace.info.tags` | `trace.info.trace_metadata` |
| Deprecated alias | None | `trace.info.request_metadata` |
| Typical use | Dynamic categorization (environment, user) | Fixed configuration (model version, source) |

^[access-trace-data-databricks-on-aws.md]

## Related Concepts

- [TraceInfo](/concepts/traceinfo.md) — The metadata component of a trace that contains tags and metadata
- [TraceData](/concepts/tracedata.md) — The execution data component of a trace
- Spans — Individual operations within a trace that can also have attributes
- [Trace Assessments](/concepts/trace-assessments.md) — Evaluations attached to traces for quality scoring
- [Token Usage Tracking](/concepts/mlflow-token-usage-tracking.md) — Token consumption data stored in trace metadata
- mlflow.search_traces()|Search Traces — Filtering traces by tags and other criteria

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
