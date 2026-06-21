---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0affc2cbfc2241fa35cb0d64fc37f86629d1819da0f4700c5c9a36644a2d0db7
  pageDirectory: concepts
  sources:
    - mlflow-mcp-server-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-for-genai-observability
    - MTFGO
    - MLflow Tracing – GenAI Observability
    - Tracing and observability
    - trace (observability)|trace
  citations:
    - file: mlflow-mcp-server-databricks-on-aws.md
title: MLflow Tracing for GenAI Observability
description: Databricks' tracing framework for monitoring, analyzing, and debugging GenAI application behavior using MLflow
tags:
  - mlflow
  - tracing
  - genai
  - observability
timestamp: "2026-06-19T19:39:52.804Z"
---

---
title: "[MLflow Tracing](/concepts/mlflow-tracing.md) for GenAI Observability"
summary: "[MLflow Tracing](/concepts/mlflow-tracing.md) provides end-to-end observability for GenAI applications by capturing, storing, and analyzing trace data for model interactions. It includes an MCP server for programmatic trace management and supports integration with Databricks."
sources:
  - mlflow-mcp-server-databricks-on-aws.md
  - a-preview-tracking-observability-for-genai-applications.md
kind: concept
createdAt: "2026-06-18T08:17:49.893Z"
updatedAt: "2026-06-18T08:17:49.893Z"
tags:
  - mlflow
  - genai
  - observability
  - tracing
aliases:
  - mlflow-tracing-for-genai-observability
  - mlflow-tracing
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) for GenAI Observability

**MLflow Tracing for GenAI Observability** provides end-to-end observability for [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications. It captures, stores, and analyzes trace data for model interactions, helping developers and operators understand the behavior and performance of their generative AI applications. ^[mlflow-mcp-server-databricks-on-aws.md]

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) records detailed information about each invocation of a GenAI model, including inputs, outputs, and metadata. This trace data can be used for:

- Debugging and troubleshooting
- Performance analysis
- Monitoring and evaluation
- Compliance and audit

^[mlflow-mcp-server-databricks-on-aws.md]

## MLflow MCP Server

The [MLflow MCP Server](/concepts/mlflow-mcp-server.md) is a key feature for programmatic trace management. It exposes all MLflow trace management operations through the Model Context Protocol (MCP), allowing AI assistants and coding tools to interact with traces programmatically. ^[mlflow-mcp-server-databricks-on-aws.md]

The MCP server enables:

- Search and retrieval of trace data
- Analysis of trace performance and behavior
- Logging of feedback and assessments
- Management of trace tags and metadata
- Deletion of traces and assessments

^[mlflow-mcp-server-databricks-on-aws.md]

## Trace Management Operations

The MLflow MCP server supports several key operations:

- **Search Traces**: Query trace data by experiment, model, or other criteria
- **Retrieve Trace Details**: Access full input/output and metadata for specific traces
- **Log Feedback**: Add ratings, notes, or other feedback to specific traces
- **Delete Traces**: Remove specific traces and associated data

^[mlflow-mcp-server-databricks-on-aws.md]

## Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with Databricks:

- An MCP-compatible client such as [VS Code](/concepts/databricks-visual-studio-code-extension.md), Cursor, or Claude
- [MLflow](/concepts/mlflow.md) Python library version 3.5.1 or later with the `databricks` and `mcp` extras
- Databricks workspace URL and personal access token

^[mlflow-mcp-server-databricks-on-aws.md]

### Installation

```bash
pip install 'mlflow[databricks,mcp]>=3.5.1'
```

^[mlflow-mcp-server-databricks-on-aws.md]

### Configuration

For Databricks integration, configure the MCP client with:

```json
{
    "servers": {
        "mlflow-mcp": {
            "command": "uv",
            "args": ["run", "--with", "mlflow[databricks,mcp]>=3.5.1", "mlflow", "mcp", "run"],
            "env": {
                "MLFLOW_TRACKING_URI": "databricks",
                "DATABRICKS_HOST": "<your-workspace-url>",
                "DATABRICKS_TOKEN": "<your-token>"
            }
        }
    }
}
```

^[mlflow-mcp-server-databricks-on-aws.md]

## MCP Tools

The MLflow MCP server exposes the following tools to MCP clients:

- **search_traces**: Retrieve traces by experiment ID or other criteria
- **get_trace_detail**: Get full details for a specific trace
- **add_feedback**: Log feedback for a trace
- **delete_trace**: Remove a specific trace
- **delete_assessments**: Remove assessments for a trace

^[mlflow-mcp-server-databricks-on-aws.md]

### Tool Parameters

| Tool | Parameter | Description |
| --- | --- | --- |
| `search_traces` | `experiment_id` (optional) | Filter by experiment |
| `search_traces` | `request_id` (optional) | Filter by request |
| `get_trace_detail` | `trace_id` (required) | The trace to inspect |
| `add_feedback` | `trace_id`, `feedback` | Add rating/note to a trace |
| `delete_trace` | `trace_id` | Remove the trace |

^[mlflow-mcp-server-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) - The core MLflow platform
- Model Context Protocol (MCP) - The protocol for AI application interaction
- [GenAI Observability](/concepts/genai-observability.md) - The broader field of monitoring GenAI applications
- [Trace Data](/concepts/tracedata.md) - The specific data captured by traces
- Feedback Management - Managing evaluations and assessments

## Sources

- mlflow-mcp-server-databricks-on-aws.md

# Citations

1. [mlflow-mcp-server-databricks-on-aws.md](/references/mlflow-mcp-server-databricks-on-aws-8d2ac0cf.md)
