---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2d482df0de53b9cec4273d71d40d4d7301b7bbd48d88d48ef5f7826f0009947b
  pageDirectory: concepts
  sources:
    - mlflow-mcp-server-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mcp-client-configuration-for-databricks
    - MCCFD
  citations:
    - file: mlflow-mcp-server-databricks-on-aws.md
title: MCP Client Configuration for Databricks
description: Configuration patterns for connecting MCP-compatible clients (VS Code, Cursor, Claude Desktop) to the MLflow MCP server with Databricks authentication
tags:
  - mcp
  - databricks
  - configuration
timestamp: "2026-06-19T19:38:36.273Z"
---

# MCP Client Configuration for Databricks

**MCP Client Configuration for Databricks** describes how to set up an MCP‑compatible client (such as VS Code, Cursor, or Claude Desktop) to use the [MLflow MCP Server](/concepts/mlflow-mcp-server.md) for interacting with traces stored in a Databricks workspace. The MLflow MCP server exposes trace management operations via the Model Context Protocol, enabling AI coding assistants to search, retrieve, analyze, and manage trace data programmatically. ^[mlflow-mcp-server-databricks-on-aws.md]

## Prerequisites

Before configuring the client, ensure the following are in place:

- An MCP‑compatible client, such as VS Code, Cursor, or Claude Desktop. ^[mlflow-mcp-server-databricks-on-aws.md]
- MLflow Python library version 3.5.1 or later, installed with both the `databricks` and `mcp` extras. The `databricks` extra provides Databricks authentication and connectivity, and the `mcp` extra supplies the MCP server dependencies. The recommended installation command is:
  ```bash
  pip install 'mlflow[databricks,mcp]>=3.5.1'
  ```
  ^[mlflow-mcp-server-databricks-on-aws.md]

## Configuration Steps

To use the MLflow MCP server with traces in Databricks, add a server definition to your MCP client’s configuration file. The exact file location and format vary by client:

- **VS Code**: `.vscode/mcp.json` in your project.
- **Cursor** and **Claude Desktop**: consult the client’s own MCP settings documentation (the source provides VS Code as the example). ^[mlflow-mcp-server-databricks-on-aws.md]

Below is a sample configuration for VS Code that uses `uv` to run the MLflow MCP server:

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

Replace `<your-workspace-url>` with your actual Databricks workspace URL (for example, `https://your-workspace.cloud.databricks.com`) and `<your-token>` with a valid [Databricks personal access token](/concepts/databricks-personal-access-token-pat-authentication.md). ^[mlflow-mcp-server-databricks-on-aws.md]

## Usage

Once configured, your AI assistant can issue natural‑language commands to interact with Databricks traces. Example queries include:

- “Search for traces from experiment ID 12345”
- “Show me the most recent traces with errors”
- “Get trace details for trace ID tr‑abc123”
- “Add feedback to trace tr‑abc123 with a rating of 5”

^[mlflow-mcp-server-databricks-on-aws.md]

For a full list of available tools and operations, refer to the open source MLflow MCP server documentation.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – GenAI observability on Databricks.
- Model Context Protocol (MCP) – The protocol underlying this integration.
- [Databricks personal access token](/concepts/databricks-personal-access-token-pat-authentication.md) – Required authentication credential.
- [MLflow experiments](/concepts/mlflow-experiment.md) – Organizational unit for runs and traces.

## Sources

- mlflow-mcp-server-databricks-on-aws.md

# Citations

1. [mlflow-mcp-server-databricks-on-aws.md](/references/mlflow-mcp-server-databricks-on-aws-8d2ac0cf.md)
