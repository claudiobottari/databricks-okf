---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bdfe55d96ba3372a043837c00ba796345deb392e7fff651cf8d043f5c4721c3b
  pageDirectory: concepts
  sources:
    - mlflow-mcp-server-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-management-operations
    - MTMO
  citations:
    - file: mlflow-mcp-server-databricks-on-aws.md
title: MLflow Trace Management Operations
description: The set of programmatic operations exposed by the MLflow MCP server for searching, retrieving, analyzing, and managing MLflow traces
tags:
  - mlflow
  - tracing
  - api
timestamp: "2026-06-19T19:38:35.665Z"
---

# MLflow Trace Management Operations

**MLflow Trace Management Operations** refer to the set of trace lifecycle actions exposed by the [MLflow MCP (Model Context Protocol) server](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/mlflow-mcp). These operations allow AI applications and coding assistants to programmatically interact with trace data stored in Databricks without requiring direct API calls. ^[mlflow-mcp-server-databricks-on-aws.md]

## Available Operations

Through the MCP protocol, the server exposes the following trace management capabilities: ^[mlflow-mcp-server-databricks-on-aws.md]

- **Search and retrieve trace data** – Find traces by experiment ID, status, or other criteria.
- **Analyze trace performance and behavior** – Examine trace-level metrics and execution details.
- **Log feedback and assessments** – Attach ratings, comments, or evaluation scores to traces.
- **Manage trace tags and metadata** – Add, update, or remove custom tags on traces.
- **Delete traces and assessments** – Remove traces or feedback entries from the tracking store.

These operations are the same ones available through the [MLflow Tracing](/concepts/mlflow-tracing.md) API, but made accessible via natural-language or structured requests through an MCP-compatible client. ^[mlflow-mcp-server-databricks-on-aws.md]

## Prerequisites

To use the MLflow MCP server with trace management operations, you must have: ^[mlflow-mcp-server-databricks-on-aws.md]

- An MCP-compatible client such as VS Code, Cursor, or Claude Desktop.
- MLflow Python library version **3.5.1 or later** with the `databricks` and `mcp` extras installed:
  ```bash
  pip install 'mlflow[databricks,mcp]>=3.5.1'
  ```

The `databricks` extra provides authentication and connectivity to Databricks; the `mcp` extra supplies the MCP server dependencies. ^[mlflow-mcp-server-databricks-on-aws.md]

## Configuration for Databricks

To connect the MCP server to traces stored in Databricks, configure your MCP client with the following settings (example for VS Code's `.vscode/mcp.json`): ^[mlflow-mcp-server-databricks-on-aws.md]

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

Replace `<your-workspace-url>` with your Databricks workspace URL (e.g., `https://your-workspace.cloud.databricks.com`) and `<your-token>` with a personal access token. ^[mlflow-mcp-server-databricks-on-aws.md]

## Usage Examples

After configuration, an AI assistant can perform trace management operations through natural-language requests. For example: ^[mlflow-mcp-server-databricks-on-aws.md]

- *“Search for traces from experiment ID 12345”*
- *“Show me the most recent traces with errors”*
- *“Get trace details for trace ID tr-abc123”*
- *“Add feedback to trace tr-abc123 with a rating of 5”*

The assistant translates these requests into the corresponding MCP tool calls, which the MLflow MCP server executes against the Databricks trace store. ^[mlflow-mcp-server-databricks-on-aws.md]

## Related Concepts

- [MLflow MCP Server](/concepts/mlflow-mcp-server.md) – The component that exposes these operations.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying GenAI observability feature that generates and stores traces.
- Databricks – The cloud platform where traces are stored and the MCP server connects.
- Model Context Protocol (MCP) – The protocol enabling this interaction.
- [Trace Feedback](/concepts/trace-based-feedback-loop.md) – The operation for logging assessments on traces.

## Sources

- mlflow-mcp-server-databricks-on-aws.md

# Citations

1. [mlflow-mcp-server-databricks-on-aws.md](/references/mlflow-mcp-server-databricks-on-aws-8d2ac0cf.md)
