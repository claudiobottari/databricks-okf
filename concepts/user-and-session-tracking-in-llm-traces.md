---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bfd171c68970d27d5568515d4f3c8d3c52230f5d06a16ae170c9fde6ec1e1f6b
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - user-and-session-tracking-in-llm-traces
    - Session Tracking in LLM Traces and User
    - UASTILT
    - User and Session Tracking in Traces
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
title: User and Session Tracking in LLM Traces
description: Using standardized mlflow.trace.user and mlflow.trace.session metadata fields to associate traces with specific users and group them into multi-turn conversations for behavioral analytics.
tags:
  - mlflow
  - user-analytics
  - session-tracking
timestamp: "2026-06-18T10:40:11.429Z"
---

# User and Session Tracking in LLM Traces

**User and session tracking** enriches [[MLflow Trace|MLflow Traces]] with identity and conversation‑level context, enabling you to analyze user behavior, debug issues across environments, and monitor the performance of generative AI applications. By attaching standardized metadata fields to traces, you can filter, group, and compare interactions by user or session without altering your application logic. ^[add-context-to-traces-databricks-on-aws.md]

## Why Track Users and Sessions?

User and session metadata unlocks several powerful analytics capabilities:

- **User behavior analysis** – Understand how different users interact with your application.
- **Conversation flow tracking** – Analyze multi‑turn conversations and how well context is retained across turns.
- **Personalization insights** – Identify patterns that can improve user‑specific experiences.
- **Quality per user** – Track performance metrics (latency, token usage, assessment scores) across different user segments.
- **Session continuity** – Maintain context across multiple interactions within a single session.

^[add-context-to-traces-databricks-on-aws.md]

## Standard Metadata Fields

MLflow provides two reserved metadata keys for user and session tracking:

| Field | Purpose | Example |
|---|---|---|
| `mlflow.trace.user` | Associates a trace with a specific user. | `"user_1234"` or `"alice@example.com"` |
| `mlflow.trace.session` | Groups traces that belong to the same multi‑turn conversation. | `"session_abcd"` |

These fields are immutable once the trace is logged, making them ideal for permanent identifiers. When you use these standard names, MLflow automatically enables filtering and grouping of traces in the UI, and the fields are queryable via the SDK’s mlflow.search_traces()|MLflow Tracing API| search_traces function. ^[add-context-to-traces-databricks-on-aws.md]

### Adding User and Session Context

During your application’s execution, call [`mlflow.update_current_trace()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.update_current_trace) with the relevant metadata:

```python
import mlflow

mlflow.update_current_trace(
    metadata={
        "mlflow.trace.user": user_id,
        "mlflow.trace.session": session_id,
    }
)
```

After the trace is logged, the `metadata` dictionary is read‑only. Tags (such as `"query_category"`) are mutable and can be changed after logging, but they are not used for user/session grouping in the same way. ^[add-context-to-traces-databricks-on-aws.md]

## Accessing User and Session Metadata

Use the `metadata` field returned by `mlflow.search_traces()` (in the DataFrame) or the [`Trace.info.trace_metadata`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo.trace_metadata) attribute on individual [`Trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace) objects to retrieve user/session identifiers. ^[add-context-to-traces-databricks-on-aws.md]

## Best Practices

- **Use consistent ID formats** across your application (e.g., UUIDs for sessions, email or internal IDs for users).
- **Define clear session boundaries** – decide when a session starts and ends (e.g., a 30‑minute inactivity timeout or explicit logout).
- **Track user and session context together** with environment and version metadata for complete traceability. See [Add context to traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) for additional metadata fields such as `mlflow.source.type`.
- **Avoid hard‑coding metadata values**; instead, extract them from environment variables or request headers at runtime.
- **Set up dashboards** to monitor user behavior, session patterns, and quality metrics per user/segment.

^[add-context-to-traces-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace|MLflow Traces]] – The execution records that user and session metadata annotate.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The framework for capturing and analyzing traces.
- [Add context to traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) – Full guide on standard metadata fields, including environments and versions.
- [Assessments on Traces](/concepts/assessments-on-traces.md) – Quality annotations that can be filtered by user/session.
- Spans – Individual operations within a trace that inherit the parent trace’s metadata.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – Automated evaluation that can be segmented by user or session.

## Sources

- add-context-to-traces-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
