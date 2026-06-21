---
title: Trace concepts | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/tracing-101
ingestedAt: "2026-06-18T08:18:20.865Z"
---

Tracing is an observability technique that captures the complete execution flow of a request through your application. Unlike traditional logging that records isolated events, tracing creates a detailed map of how data flows through your systems and records every operation along the way.

GenAI applications run complex, multi-step workflows that combine multiple components such as LLMs, retrievers, tools, and agents. Tracing makes those workflows debuggable by capturing the full execution flow.

## Trace structure[​](#trace-structure "Direct link to Trace structure")

An MLflow [Trace](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace) comprises two primary objects:

1.  `Trace.info` of type [`TraceInfo`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo): Metadata describing the trace's origin, status, and execution time. `TraceInfo` also holds [tags](#tags). The tags are user-, session-, and developer-provided key-value pairs that you can use to search or filter traces.
    
2.  `Trace.data` of type [`TraceData`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceData): The actual payload containing instrumented [Span](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/span-concepts) objects that capture your application's step-by-step execution from input to output.
    

![Trace Architecture](https://docs.databricks.com/aws/en/assets/images/trace-architecture-9228f7ffed1b0e1f739a56614de23a50.png)

MLflow Traces are compatible with [OpenTelemetry specifications](https://opentelemetry.io/docs/concepts/signals/traces/), a widely adopted industry standard for observability. Traces remain interoperable with other OpenTelemetry-compatible observability tools, while MLflow extends the OpenTelemetry model with GenAI-specific structures and attributes.

### TraceInfo[​](#traceinfo "Direct link to TraceInfo")

[`TraceInfo`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo) provides lightweight metadata about the overall trace. Key fields include:

### TraceData[​](#tracedata "Direct link to TraceData")

The [`TraceData`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceData) object is a container of [Span](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/span-concepts) objects where the execution details are stored. Each span captures information about a specific operation, including:

*   Requests and responses
*   Latency measurements
*   LLM messages and tool parameters
*   Retrieved documents and context
*   Metadata and attributes

Spans form a hierarchical structure through parent-child connections, creating a tree that represents your application's execution flow.

![Span Architecture](https://docs.databricks.com/aws/en/assets/images/trace-span-a0ce1bb4698cf4ba9a5910029a8be6cf.png)

### Tags[​](#-tags "Direct link to -tags")

Tags are mutable key-value pairs attached to traces for organization and filtering. MLflow defines standard tags for common use cases:

*   `mlflow.trace.session`: Session identifier for grouping related traces
*   `mlflow.trace.user`: User identifier for tracking per-user interactions
*   `mlflow.source.name`: Entry point or script that generated the trace
*   `mlflow.source.git.commit`: Git commit hash of the source code (if applicable)
*   `mlflow.source.type`: Source type (`PROJECT`, `NOTEBOOK`, etc.)

You can also add custom tags for your specific needs. Learn more in [Add context to traces](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/add-context-to-traces) and [Attach custom tags / metadata](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/attach-tags/).

## Storage layout[​](#storage-layout "Direct link to Storage layout")

MLflow optimizes trace storage for performance and cost. To customize the storage location, attach a Unity Catalog volume when [creating an experiment](https://docs.databricks.com/aws/en/mlflow/experiments#create-expt-from-workspace). Access is then governed by [Unity Catalog volume privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference#read-volume).

`TraceInfo` is stored directly in a relational database as indexed rows, which enables fast queries for searching and filtering traces.

`TraceData` (the spans) is stored in artifact storage rather than the relational database because spans are larger. This keeps queries fast even when trace volume grows.

## Active vs. finished traces[​](#active-vs-finished-traces "Direct link to Active vs. finished traces")

An active trace is a trace that MLflow is currently writing, for example, while a [function decorated with `@mlflow.trace`](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/function-decorator) is running. After the decorated function exits, the trace is finished, but you can still annotate it with new data.

To work with active or recent traces, use these methods:

*   [`mlflow.get_active_trace_id()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.get_active_trace_id): returns the ID of the currently active trace.
*   [`mlflow.get_last_active_trace_id()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.get_last_active_trace_id): returns the ID of the most recent finished trace.

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Span concepts](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/span-concepts) — Learn about spans and how they capture individual operations.
*   [Get started: MLflow Tracing for GenAI (Databricks Notebook)](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/tracing/tracing-notebook) — Get hands-on experience with tracing in a notebook.
