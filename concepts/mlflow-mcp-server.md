---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1900b8f1b73cf5a55f2177bc621dfcc3587ff028db7affee4fbc99608283ff0d
  pageDirectory: concepts
  sources:
    - mlflow-mcp-server-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-mcp-server
    - MMS
    - MCP Servers
    - MCP servers
  citations:
    - file: mlflow-mcp-server-databricks-on-aws.md
title: MLflow MCP Server
description: An MCP (Model Context Protocol) server that exposes MLflow trace management operations to AI applications and coding assistants
tags:
  - mlflow
  - mcp
  - tracing
  - databricks
timestamp: "2026-06-19T19:38:32.677Z"
---

Here is the wiki page for "MLflow MCP Server".

---

## MLflow MCP Server

The **MLflow MCP (Model Context Protocol) Server** is a service that exposes all [MLflow](/concepts/mlflow.md) trace management operations through the standardized Model Context Protocol. It enables AI-powered applications and coding assistants to programmatically search, analyze, and manage [[MLflow Trace|MLflow Traces]] stored in Databricks. ^[mlflow-mcp-server-databricks-on-aws.md]

### Overview

The MLflow MCP server allows AI assistants to interact with trace data through natural language or programmatic commands. Supported operations include searching and retrieving trace data, analyzing trace performance and behavior, logging feedback and assessments, and managing trace tags, metadata, and deletions. ^[mlflow-mcp-server-databricks-on-aws.md]

The server is built on the open source Model Context Protocol and requires an MCP-compatible client such as VS Code, Cursor, or Claude Desktop. ^[mlflow-mcp-server-databricks-on-aws.md]

### Prerequisites

To use the MLflow MCP server, you need:

- An MCP-compatible client (VS Code, Cursor, or Claude Desktop).
- MLflow Python library version **3.5.1 or later** installed with both the `databricks` and `mcp` extras. The `mcp` extra provides the MCP server dependencies, and the `databricks` extra provides Databricks authentication and connectivity. ^[mlflow-mcp-server-databricks-on-aws.md]

Installation command:

```bash
pip install 'mlflow[databricks,mcp]>=3.5.1'
```

### Configuration for Databricks

To use the MLflow MCP server with traces stored in Databricks, configure your MCP client with the following environment variables and command settings. Below is an example configuration for VS Code, which can be adapted for Cursor or Claude Desktop with minimal changes. ^[mlflow-mcp-server-databricks-on-aws.md]

#### VS Code Configuration

Add the following to `.vscode/mcp.json` in your project:

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

Replace `<your-workspace-url>` with your Databricks workspace URL (e.g., `https://your-workspace.cloud.databricks.com`) and `<your-token>` with your personal access token. ^[mlflow-mcp-server-databricks-on-aws.md]

### Usage

After configuring the MCP server, your AI assistant can interact with traces stored in Databricks. Example queries you can make include:

- "Search for traces from experiment ID 12345"
- "Show me the most recent traces with errors"
- "Get trace details for trace ID tr-abc123"
- "Add feedback to trace tr-abc123 with a rating of 5" ^[mlflow-mcp-server-databricks-on-aws.md]

### Available Tools

The MLflow MCP server exposes all standard MLflow trace management operations through the MCP protocol, including:

- Search and retrieve trace data
- Analyze trace performance and behavior
- Log feedback and assessments
- Manage trace tags and metadata
- Delete traces and assessments ^[mlflow-mcp-server-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing – GenAI Observability](/concepts/mlflow-tracing-for-genai-observability.md) – The broader tracing framework on Databricks.
- Model Context Protocol (MCP) – The underlying protocol standard.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Organizational units for MLflow runs and traces.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – Controls for managing MLflow serverless workload costs.
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) – Monitoring model predictions via trace data.

### Sources

- mlflow-mcp-server-databricks-on-aws.md

# Citations

1. [mlflow-mcp-server-databricks-on-aws.md](/references/mlflow-mcp-server-databricks-on-aws-8d2ac0cf.md)
