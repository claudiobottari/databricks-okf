---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 65ad418c7f01aa27174d925d394a406e90f1146fb5454bebcc5b91ae3e1a5b1c
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - user-and-session-tracking-with-standard-metadata-fields
    - Session Tracking with Standard Metadata Fields and User
    - UASTWSMF
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
title: User and Session Tracking with Standard Metadata Fields
description: MLflow's standard metadata fields `mlflow.trace.user` and `mlflow.trace.session` for associating traces with users and grouping multi-turn conversations
tags:
  - mlflow
  - tracing
  - users
  - sessions
timestamp: "2026-06-19T21:58:44.507Z"
---

# User and Session Tracking with Standard Metadata Fields

**User and Session Tracking with Standard Metadata Fields** refers to the practice of attaching standardized context keys—`mlflow.trace.user` and `mlflow.trace.session`—to MLflow traces in order to capture user identity and conversation grouping for production GenAI applications. These fields enable application analytics, debugging, and personalization by linking every trace to the user and session that generated it. ^[add-context-to-traces-databricks-on-aws.md]

## Why Track Users and Sessions?

User and session tracking provides several concrete benefits:

- **User behavior analysis** – Understand how different users interact with the application.
- **Conversation flow tracking** – Analyze multi-turn dialogues and context retention across turns.
- **Personalization insights** – Identify patterns to improve per‑user experiences.
- **Quality per user** – Measure performance and response quality across user segments.
- **Session continuity** – Maintain awareness of context that spans multiple interactions within the same session. ^[add-context-to-traces-databricks-on-aws.md]

## Standard Metadata Fields

MLflow defines two dedicated metadata keys for this purpose:

| Key                     | Purpose                                      |
|-------------------------|----------------------------------------------|
| `mlflow.trace.user`     | Associates a trace with a specific user.     |
| `mlflow.trace.session`  | Groups traces belonging to the same session (e.g., a multi‑turn conversation). |

When these fields are populated, MLflow’s UI automatically enables filtering and grouping by user or session, making it straightforward to examine all traces from a given user or within a particular conversation. ^[add-context-to-traces-databricks-on-aws.md]

Because these are **metadata** fields (as opposed to tags), they become immutable once the trace is logged. This immutability makes them ideal for storing identifiers that must not change after the trace is recorded. Tags, on the other hand, remain mutable and are better suited for dynamic classification (e.g., custom query categories). ^[add-context-to-traces-databricks-on-aws.md]

## Implementation

To add user and session context, trace your application functions (commonly with the `@mlflow.trace` decorator) and then call `mlflow.update_current_trace()` during execution, passing the standard metadata keys:

```python
import mlflow

mlflow.update_current_trace(
    metadata={
        "mlflow.trace.user": user_id,
        "mlflow.trace.session": session_id,
    }
)
```

Initialize `user_id` and `session_id` from your application’s authentication or session‑management layer. After the trace is logged, the metadata cannot be modified. ^[add-context-to-traces-databricks-on-aws.md]

### Requirements

- MLflow 3 is required (MLflow 2.x lacks the necessary performance and features).
- For production deployments, install the minimal‑dependency `mlflow-tracing` package:
  ```bash
  pip install --upgrade mlflow-tracing
  ``` ^[add-context-to-traces-databricks-on-aws.md]

## Best Practices

- **Consistent ID formats** – Use standardized user and session ID formats across the entire application.
- **Clear session boundaries** – Define explicit rules for when a session starts and ends (e.g., timeout, explicit logout, or user action).
- **Combine context types** – Track user, session, and environment metadata together for complete traceability.
- **Regular analysis** – Set up dashboards that monitor user behavior, session patterns, and version performance.
- **Override defaults thoughtfully** – Only override automatically populated metadata when the automatic detection does not match your needs. ^[add-context-to-traces-databricks-on-aws.md]

## Retrieving the Metadata

After traces are logged, you can access user and session information through:
- The `metadata` field of the pandas DataFrame returned by `mlflow.search_traces()`.
- The `Trace.info.trace_metadata` attribute on individual [Trace objects](/concepts/tracedata-and-span-objects.md).
- Filtering and searching in the MLflow UI, which automatically surfaces the standard user and session fields. ^[add-context-to-traces-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Overview of the tracing system.
- [Add Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) – General guide for attaching metadata and tags.
- [Trace Metadata vs Tags](/concepts/trace-metadata.md) – Immutability and mutability semantics.
- [Immutable Metadata vs Mutable Tags](/concepts/mutable-tags-vs-immutable-metadata-in-mlflow-traces.md) – Design considerations for log context.
- Session Boundaries – Defining when a session starts and ends.
- [GenAI Application Monitoring](/concepts/mlflow-genai-production-monitoring.md) – Observability for generative AI applications.
- mlflow.update_current_trace()|mlflow.update_current_trace – API reference for adding context during execution.

## Sources

- add-context-to-traces-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
