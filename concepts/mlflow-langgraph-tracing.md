---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 460575666af8dc2fa10955d6eada9aa62728b1e72065e75dc1b4b4d3d404fc02
  pageDirectory: concepts
  sources:
    - tracing-langgraph-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-langgraph-tracing
    - MLT
    - LangGraph Tracing
  citations:
    - file: tracing-langgraph-databricks-on-aws.md
title: MLflow LangGraph Tracing
description: Automatic capture of LangGraph agent executions as MLflow traces via the LangChain autolog integration
tags:
  - mlflow
  - tracing
  - langgraph
  - observability
timestamp: "2026-06-19T23:12:12.972Z"
---

# [MLflow](/concepts/mlflow.md) LangGraph Tracing

**MLflow LangGraph Tracing** is a feature of [MLflow Tracing](/concepts/mlflow-tracing.md) that provides automatic instrumentation for LangGraph applications, enabling developers to capture and visualize the execution of stateful, multi-actor LLM workflows. It extends [MLflow](/concepts/mlflow.md)'s existing LangChain integration to support LangGraph's graph-based execution model. ^[tracing-langgraph-databricks-on-aws.md]

## Overview

LangGraph is an open-source library for building stateful, multi-actor applications with LLMs, commonly used to create agent and multi-agent workflows. By enabling auto-tracing for LangChain through the `mlflow.langchain.autolog()` function, [MLflow](/concepts/mlflow.md) automatically captures graph execution into a trace and logs it to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-langgraph-databricks-on-aws.md]

## Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with LangGraph, you must install [MLflow](/concepts/mlflow.md) along with the relevant LangGraph and LangChain packages. For development environments, the full [MLflow](/concepts/mlflow.md) package with Databricks extras is recommended: ^[tracing-langgraph-databricks-on-aws.md]

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" langgraph langchain_core langchain_openai
```

[MLflow 3](/concepts/mlflow-3.md) is highly recommended for the best tracing experience with LangGraph, as it relies on the LangChain autologging integration. ^[tracing-langgraph-databricks-on-aws.md]

### Environment Configuration

- **Outside Databricks notebooks**: Set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables pointing to your workspace. ^[tracing-langgraph-databricks-on-aws.md]
- **Inside Databricks notebooks**: These credentials are automatically configured. ^[tracing-langgraph-databricks-on-aws.md]
- **API keys**: Configure your LLM provider API keys. For production, use [AI Gateway](/concepts/ai-gateway.md) or [Databricks secrets](/concepts/databricks-secret-scopes.md) instead of hardcoded values. ^[tracing-langgraph-databricks-on-aws.md]

## Enabling Auto-Tracing

Call `mlflow.langchain.autolog()` to enable [Automatic Tracing](/concepts/automatic-tracing.md) for LangGraph execution. On serverless compute clusters, autologging is not automatically enabled — you must explicitly call this function. ^[tracing-langgraph-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].langchain.autolog()
```

After enabling autolog, set up [MLflow Tracking](/concepts/mlflow-tracking.md) to your Databricks workspace and invoke the graph as usual: ^[tracing-langgraph-databricks-on-aws.md]

```python
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/langgraph-tracing-demo")
```

## Adding Spans Within a Node or Tool

By combining auto-tracing with [Manual Tracing APIs](/concepts/manual-tracing-apis.md), you can add child spans inside a node or tool function to obtain more granular insights. For example, within a `code_check` node that performs two different validations, you can create separate spans for each: ^[tracing-langgraph-databricks-on-aws.md]

```python
def code_check(state: GraphState):
    # ... state extraction ...
    
    # Check imports
    with [[mlflow|MLflow]].start_span(name="import_check", span_type=SpanType.TOOL) as span:
        span.set_inputs(imports)
        exec(imports)
        span.set_outputs("ok")
    
    # Check execution
    with [[mlflow|MLflow]].start_span(name="execution_check", span_type=SpanType.TOOL) as span:
        span.set_inputs(code)
        exec(code)
        span.set_outputs("ok")
    
    # ... return results ...
```

This creates child spans under the node span, recording whether each validation passes or fails, along with exception details. ^[tracing-langgraph-databricks-on-aws.md]

## Disabling Auto-Tracing

Auto-tracing for LangGraph can be disabled globally: ^[tracing-langgraph-databricks-on-aws.md]

```python
[[mlflow|MLflow]].langchain.autolog(disable=True)
# or
[[mlflow|MLflow]].autolog(disable=True)
```

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The broader tracing framework for [MLflow](/concepts/mlflow.md)
- LangChain Integration — The underlying integration that supports LangGraph tracing
- [Manual Tracing](/concepts/manual-tracing.md) — Adding custom spans for detailed instrumentation
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Where [Traces](/concepts/traces.md) are logged and organized
- [AI Gateway](/concepts/ai-gateway.md) — Secure API key management for production environments
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — Compute environment where explicit autolog enablement is required

## Sources

- tracing-langgraph-databricks-on-aws.md

# Citations

1. [tracing-langgraph-databricks-on-aws.md](/references/tracing-langgraph-databricks-on-aws-6240217a.md)
