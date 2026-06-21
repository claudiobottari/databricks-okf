---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b840a6894f7ff40725f44335717016d651ef3a9c04ced767e39a2ae33506f604
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-user-and-session-tracking
    - Session Tracking and MLflow User
    - MUAST
    - User and Session Tracking
    - User and session tracking
    - Track Users and Sessions
    - Track users and sessions
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
title: MLflow User and Session Tracking
description: Standardized metadata fields mlflow.trace.user and mlflow.trace.session for associating traces with specific users and grouping traces into multi-turn conversations.
tags:
  - mlflow
  - tracing
  - user-analytics
timestamp: "2026-06-19T08:52:21.975Z"
---

# MLflow User and Session Tracking

**MLflow User and Session Tracking** refers to the practice of associating GenAI application traces with specific users and conversation sessions by using standard metadata fields in MLflow. This enables analytics such as user behavior analysis, multi-turn conversation flow tracking, personalization insights, quality per user, and session continuity.^[add-context-to-traces-databricks-on-aws.md]

## Standard Metadata Fields

MLflow provides two reserved metadata fields for session and user tracking:^[add-context-to-traces-databricks-on-aws.md]

| Field | Purpose | Mutability after logging |
|-------|---------|--------------------------|
| `mlflow.trace.user` | Associates traces with a specific user identifier | Immutable |
| `mlflow.trace.session` | Groups traces belonging to multi-turn conversations | Immutable |

When these standard fields are used, the MLflow UI automatically enables filtering and grouping by user or session. Unlike tags, metadata values cannot be updated once a trace is logged, making them suitable for immutable identifiers like user and session IDs.^[add-context-to-traces-databricks-on-aws.md]

## Implementation

User and session context is added during application execution by calling [`mlflow.update_current_trace()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.update_current_trace) with a `metadata` dictionary containing the standard fields. This call must be made while a trace is active (after tracing has been started via decorators or manual instrumentation).^[add-context-to-traces-databricks-on-aws.md]

```python
import mlflow

mlflow.update_current_trace(
    metadata={
        "mlflow.trace.user": user_id,
        "mlflow.trace.session": session_id,
    }
)
```

### Requirements

- MLflow 3 is required; MLflow 2.x is not supported for context tracking due to performance limitations.^[add-context-to-traces-databricks-on-aws.md]
- For production deployments, install the `mlflow-tracing` package.^[add-context-to-traces-databricks-on-aws.md]

### Accessing User and Session Data

After traces are logged, the stored metadata can be retrieved via:
- `mlflow.search_traces()` – returns a pandas DataFrame whose `metadata` field contains the user and session IDs.
- `Trace.info.trace_metadata` – a [`TraceInfo`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo) attribute.
- `Trace.info.tags` – for mutable tags (user/session metadata is immutable).^[add-context-to-traces-databricks-on-aws.md]

## Why Track Users and Sessions?

User and session tracking in GenAI applications enables:^[add-context-to-traces-databricks-on-aws.md]

1. **User behavior analysis** – understand how different users interact with the application.
2. **Conversation flow tracking** – analyze multi-turn conversations and context retention.
3. **Personalization insights** – identify patterns to improve user‑specific experiences.
4. **Quality per user** – track performance metrics across different user segments.
5. **Session continuity** – maintain context across multiple interactions within a session.

## Best Practices

- **Consistent ID formats** – use standardized formats for user and session IDs across the application.^[add-context-to-traces-databricks-on-aws.md]
- **Session boundaries** – define clear rules for when a session starts and ends.^[add-context-to-traces-databricks-on-aws.md]
- **Combine context types** – track user, session, and environment context together for complete traceability.^[add-context-to-traces-databricks-on-aws.md]
- **Regular analysis** – set up dashboards to monitor user behavior, session patterns, and version performance.^[add-context-to-traces-databricks-on-aws.md]

## Related Concepts

- [Add context to traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) – broader topic covering environment, version, and custom metadata.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – the underlying tracing framework.
- mlflow.search_traces()|mlflow.search_traces – programmatic retrieval of trace metadata.
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – applying user/session tracking in deployed systems.

## Sources

- add-context-to-traces-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
