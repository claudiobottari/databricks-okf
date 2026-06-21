---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fe11658a18b428d91308b4425ba13d25187bc4db85ade9d6d61dab8f8c0e8d6b
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - user-and-session-tracking-in-mlflow-traces
    - Session Tracking in MLflow Traces and User
    - UASTIMT
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
title: User and Session Tracking in MLflow Traces
description: Using standardized mlflow.trace.user and mlflow.trace.session metadata fields to associate traces with specific users and group traces from multi-turn conversations for behavior analysis and personalization.
tags:
  - mlflow
  - user-tracking
  - session-tracking
  - genai
timestamp: "2026-06-19T13:53:54.427Z"
---

# User and Session Tracking in MLflow Traces

**User and Session Tracking in MLflow Traces** refers to the practice of associating GenAI application traces with specific users and conversation sessions to enable behavior analysis, conversation flow tracking, and personalization insights. MLflow provides standardized metadata fields for this purpose, along with APIs to add context during trace execution.

## Overview

Tracking users and sessions in your GenAI application provides essential context for understanding user behavior, analyzing conversation flows, and improving personalization. This metadata enables powerful analytics such as user behavior analysis, multi-turn conversation tracking, personalization insights, quality per user segment, and session continuity across multiple interactions. ^[add-context-to-traces-databricks-on-aws.md]

## Standard Metadata Fields

MLflow provides two standard metadata fields for session and user tracking:

- `mlflow.trace.user` – Associates traces with specific users
- `mlflow.trace.session` – Groups traces belonging to multi-turn conversations

When you use these standard metadata fields, MLflow automatically enables filtering and grouping in the UI. Unlike tags, metadata cannot be updated once the trace is logged, making it ideal for immutable identifiers like user and session IDs. ^[add-context-to-traces-databricks-on-aws.md]

## Implementation

### Requirements

For production deployments, install the `mlflow-tracing` package:

```bash
pip install --upgrade mlflow-tracing
```

The `mlflow-tracing` package is optimized for production use with minimal dependencies and better performance characteristics. MLflow 3 is required for context tracking; MLflow 2.x is not supported due to performance limitations. ^[add-context-to-traces-databricks-on-aws.md]

### Adding User and Session Context

To add user and session metadata to traces, first trace your application (commonly using the `@mlflow.trace` decorator), then call [`mlflow.update_current_trace()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html?highlight=trace#mlflow.update_current_trace) during execution: ^[add-context-to-traces-databricks-on-aws.md]

```python
import mlflow

mlflow.update_current_trace(
    metadata={
        "mlflow.trace.user": user_id,
        "mlflow.trace.session": session_id,
    },
)
```

After your application completes and a trace is logged, `tags` are mutable, but `metadata` are immutable in the logged trace. ^[add-context-to-traces-databricks-on-aws.md]

### Accessing User and Session Metadata

To access metadata in trace logs, use the `metadata` field in the pandas DataFrame returned by `mlflow.search_traces()`, or use the [`Trace.info.trace_metadata`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo.trace_metadata) field from [`Trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace) objects. ^[add-context-to-traces-databricks-on-aws.md]

## Why Track Users and Sessions?

User and session tracking enables several categories of improvements:

1. **User behavior analysis** – Understand how different users interact with your application
2. **Conversation flow tracking** – Analyze multi-turn conversations and context retention
3. **Personalization insights** – Identify patterns to improve user-specific experiences
4. **Quality per user** – Track performance metrics across different user segments
5. **Session continuity** – Maintain context across multiple interactions

^[add-context-to-traces-databricks-on-aws.md]

## Combining with Other Context Types

Production applications typically need to track multiple pieces of context simultaneously. User and session tracking can be combined with environment and version tracking for complete traceability: ^[add-context-to-traces-databricks-on-aws.md]

```python
import mlflow
import os

mlflow.update_current_trace(
    metadata={
        "mlflow.trace.user": user_id,
        "mlflow.trace.session": session_id,
        "mlflow.source.type": os.getenv("APP_ENVIRONMENT", "development"),
    },
)
```

## Best Practices

1. **Consistent ID formats** – Use standardized formats for user and session IDs across your application
2. **Session boundaries** – Define clear rules for when sessions start and end
3. **Combine context types** – Track user, session, and environment context together for complete traceability
4. **Regular analysis** – Set up dashboards to monitor user behavior, session patterns, and version performance
5. **Immutable identifiers** – Use metadata (not tags) for user and session IDs since they should not change after logging

^[add-context-to-traces-databricks-on-aws.md]

## Related Concepts

- [Add Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) – General guide for adding metadata and tags to MLflow traces
- mlflow.search_traces() API|Search Traces Programmatically – Querying traces using `mlflow.search_traces()`
- Track Environments and Versions – Tracking deployment context alongside user and session data
- [Trace Analysis Examples](/concepts/genai-trace-analysis-and-debugging.md) – Examples of trace analytics and visualization
- Tutorial: Trace and Analyze Users and Environments – Full tutorial demonstrating user, session, and environment tracking

## Sources

- add-context-to-traces-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
