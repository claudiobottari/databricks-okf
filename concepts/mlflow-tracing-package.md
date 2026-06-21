---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c436d4d7cb80c8ace8a1ff361fa04b41b145bc339db679140f44251eee0ffee0
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-package
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
    - file: trace-agents-deployed-outside-of-databricks-databricks-on-aws.md
title: mlflow-tracing Package
description: Production-optimized Python package for MLflow tracing with minimal dependencies and better performance, requiring MLflow 3
tags:
  - mlflow
  - tracing
  - installation
  - production
timestamp: "2026-06-19T21:59:21.993Z"
---

# mlflow-tracing Package

The **`mlflow-tracing` package** is a lightweight, production-optimized Python package for deploying [MLflow Tracing](/concepts/mlflow-tracing.md) capabilities in generative AI applications. It provides the core functionality for instrumenting, capturing, and analyzing traces with minimal dependencies and better performance characteristics compared to the full MLflow package.^[add-context-to-traces-databricks-on-aws.md]

## Overview

The `mlflow-tracing` package is designed for production environments where performance, reliability, and minimal footprint are essential. It offers a streamlined alternative to the full MLflow package when tracing is the primary feature needed.^[add-context-to-traces-databricks-on-aws.md]

## Installation

Install the `mlflow-tracing` package using pip:

```bash
pip install --upgrade mlflow-tracing
```

^[add-context-to-traces-databricks-on-aws.md]

For production deployments of agents outside of Databricks, the `mlflow-tracing` package is the recommended installation option.^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Key Characteristics

The package is optimized for production use with the following characteristics:^[add-context-to-traces-databricks-on-aws.md]

- **Minimal dependencies** — A smaller dependency footprint compared to the full MLflow package.
- **Better performance** — Optimized for production workloads with reduced overhead.
- **MLflow 3 required** — The package requires MLflow 3 for context tracking; MLflow 2.x is not supported due to performance limitations and missing features essential for production use.

## Features

The `mlflow-tracing` package supports the full set of tracing capabilities, including:^[add-context-to-traces-databricks-on-aws.md]

### Context Metadata

Add standardized context metadata to traces using fields such as:
- `mlflow.trace.user` — Associates traces with specific users.
- `mlflow.trace.session` — Groups traces belonging to multi-turn conversations.
- `mlflow.source.type` — Tracks execution environment (development, staging, production).

The package also supports custom metadata keys for application-specific context like application version, deployment ID, region, and feature flags.

### Trace Tags

Tags are mutable after trace logging and are useful for metadata that may change, such as query categories or classification labels.

### Automatic Metadata Population

The package automatically populates certain standard metadata fields based on the execution environment. You can override any automatically populated metadata fields using `mlflow.update_current_trace()`.

## Usage

### Adding Context to Traces

The primary API for adding context during application execution is `mlflow.update_current_trace()`:

```python
import mlflow

mlflow.update_current_trace(
    metadata={
        "mlflow.trace.user": user_id,
        "mlflow.trace.session": session_id,
    },
    tags={
        "query_category": "chat",
    },
)
```

^[add-context-to-traces-databricks-on-aws.md]

### Accessing Metadata and Tags

After traces are logged, access metadata and tags through:
- The `metadata` and `tags` fields in the pandas DataFrame returned by `mlflow.search_traces()`.
- The `Trace.info.trace_metadata` and `Trace.info.tags` fields from `Trace` objects.

### Production Tracing for External Deployments

For agents deployed outside of Databricks, configure the following environment variables to connect to your Databricks workspace:^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

```bash
export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
export DATABRICKS_TOKEN="your-databricks-token"
export MLFLOW_TRACKING_URI=databricks
export MLFLOW_EXPERIMENT_NAME="/Shared/production-genai-app"
```

## Best Practices

When using the `mlflow-tracing` package in production:^[add-context-to-traces-databricks-on-aws.md]

- **Use consistent ID formats** for user and session IDs across your application.
- **Define clear session boundaries** for when sessions start and end.
- **Populate metadata from environment variables** rather than hard-coding values.
- **Combine context types** — track user, session, and environment context together for complete traceability.
- **Override defaults thoughtfully** — only override automatically populated metadata when necessary.

## Related Concepts

- [[MLflow Trace|MLflow Traces]] — The execution records that the package captures.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The broader framework for capturing and analyzing traces.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Long-term trace storage and automated quality assessment.
- [Add Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) — Detailed guide on adding metadata and tags.
- Trace Agents Deployed Outside of Databricks — Deploying tracing for external applications.

## Sources

- add-context-to-traces-databricks-on-aws.md
- trace-agents-deployed-outside-of-databricks-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
2. [trace-agents-deployed-outside-of-databricks-databricks-on-aws.md](/references/trace-agents-deployed-outside-of-databricks-databricks-on-aws-afaae7ad.md)
