---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ec38da2688333163b692dc548659047cf80b8c1978ea0f88c711414dc7a774bd
  pageDirectory: concepts
  sources:
    - tracing-anthropic-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-prerequisites-and-setup-for-anthropic
    - Setup for Anthropic and MLflow Tracing Prerequisites
    - MTPASFA
  citations:
    - file: tracing-anthropic-databricks-on-aws.md
title: MLflow Tracing Prerequisites and Setup for Anthropic
description: Required environment setup including MLflow version (>=3.1 recommended), Anthropic SDK installation, Databricks environment variables, and API key configuration for the Anthropic tracing integration
tags:
  - mlflow
  - tracing
  - anthropic
  - setup
  - databricks
timestamp: "2026-06-19T23:10:10.018Z"
---



# [MLflow Tracing](/concepts/mlflow-tracing.md) Prerequisites and Setup for Anthropic

**MLflow Tracing** provides automatic trace capture for Anthropic LLM (large language model) invocations. When auto-tracing is enabled via `mlflow.anthropic.autolog()`, [MLflow](/concepts/mlflow.md) records nested [Traces](/concepts/traces.md) and logs them to the active [MLflow Experiment](/concepts/mlflow-experiment.md) upon each call to the Anthropic Python SDK. ^[tracing-anthropic-databricks-on-aws.md]

## Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with Anthropic, you must install both [MLflow](/concepts/mlflow.md) and the Anthropic SDK. Two installation paths are available depending on your environment.

### Development Environment

For development work, install the full [MLflow](/concepts/mlflow.md) package with Databricks extras and the `anthropic` library:

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" anthropic
```

The full `mlflow[databricks]` package includes all features for local development and experimentation on Databricks. [MLflow 3](/concepts/mlflow-3.md) is strongly recommended for the best tracing experience with Anthropic. ^[tracing-anthropic-databricks-on-aws.md]

### Production Environment

For production use, install [MLflow](/concepts/mlflow.md) and the Anthropic SDK using the same command above. The `mlflow[databricks]` extras package provides the complete set of features needed for production tracing on Databricks. ^[tracing-anthropic-databricks-on-aws.md]

## Environment Configuration

Before running tracing examples, configure your environment with the appropriate credentials.

### For Users Outside Databricks Notebooks

Set your Databricks workspace environment variables:

```bash
export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
export DATABRICKS_TOKEN="your-personal-access-token"
```

### For Users Inside Databricks Notebooks

These credentials are automatically set for you. No manual configuration is needed. ^[tracing-anthropic-databricks-on-aws.md]

### API Key Configuration

Ensure your Anthropic API key is configured. For production use, it is recommended to use [AI Gateway](/concepts/ai-gateway.md) or [Databricks secrets](/concepts/databricks-secret-scopes.md) instead of environment variables for secure API key management:

```bash
export ANTHROPIC_API_KEY="your-anthropic-api-key"
```

On serverless compute clusters, autologging is **not** automatically enabled — you must explicitly call `mlflow.anthropic.autolog()` to activate tracing. ^[tracing-anthropic-databricks-on-aws.md]

## Supported APIs

[MLflow Tracing](/concepts/mlflow-tracing.md) supports [Automatic Tracing](/concepts/automatic-tracing.md) for the following Anthropic APIs:

| API | Support |
|-----|---------|
| Synchronous `messages.create` | Traced |
| Async `messages.create` | Traced (added in [MLflow](/concepts/mlflow.md) 2.21.0) |
| Other synchronous text interactions | Traced |
| Async APIs | Not traced |
| Multi-modal inputs | Full inputs not recorded |

To request support for additional APIs, open a [feature request](https://github.com/[MLflow](/concepts/mlflow.md)/[MLflow](/concepts/mlflow.md)/issues) on GitHub. ^[tracing-anthropic-databricks-on-aws.md]

## Capabilities

When auto-tracing is enabled, [MLflow](/concepts/mlflow.md) automatically captures the following information from Anthropic calls:

- Prompts and completion responses
- Latencies
- Model name
- Additional metadata (e.g., `temperature`, `max_tokens`) if specified
- Function calling if returned in the response
- Any exception raised

[MLflow](/concepts/mlflow.md) also supports tracing tool calling responses from Anthropic models — tool functions can be annotated with the `@mlflow.trace` decorator to create a span for tool execution. ^[tracing-anthropic-databricks-on-aws.md]

## Disabling Auto-Tracing

Auto-tracing for Anthropic can be disabled globally by calling:

```python
[[mlflow|MLflow]].anthropic.autolog(disable=True)
# or
[[mlflow|MLflow]].autolog(disable=True)
```

^[tracing-anthropic-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Anthropic SDK
- [MLflow Experiment](/concepts/mlflow-experiment.md)
- Serverless Compute
- [AI Gateway](/concepts/ai-gateway.md)
- Span Type
- [Tool Calling](/concepts/llm-function-calling.md)

## Sources

- tracing-anthropic-databricks-on-aws.md

# Citations

1. [tracing-anthropic-databricks-on-aws.md](/references/tracing-anthropic-databricks-on-aws-085cde5b.md)
