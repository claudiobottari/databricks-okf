---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf619bd54bf7125331b5cc138ce2189b0dc460a24e4fddcaf115f9fd9db4f891
  pageDirectory: concepts
  sources:
    - tracing-ag2-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflowag2autolog
    - MLflow Autolog
    - MLflow autolog
    - mlflow.autolog
    - mlflow.autolog()
  citations:
    - file: tracing-ag2-databricks-on-aws.md
title: mlflow.ag2.autolog()
description: A one-line API call that enables automatic tracing of all AG2 agent interactions, including tool calls, LLM calls, and message exchanges.
tags:
  - tracing
  - mlflow
  - ag2
  - observability
timestamp: "2026-06-19T23:08:00.017Z"
---

# `mlflow.ag2.autolog()`

**`mlflow.ag2.autolog()`** is an [MLflow](/concepts/mlflow.md) API that enables [Automatic Tracing](/concepts/automatic-tracing.md) and logging of AG2 (AutoGen 0.2) agent conversations. When called, it instruments AG2 agents to capture detailed trace data for each interaction, including agent messages, tool calls, and execution results. ^[tracing-ag2-databricks-on-aws.md]

## Overview

The `mlflow.ag2.autolog()` function provides a no-code-instrumentation approach for monitoring multi-agent workflows built with AG2 (formerly AutoGen 0.2). By calling this function once at the start of a script, all subsequent agent conversations — including those between [ConversableAgent](/concepts/conversableagent.md) instances — are automatically logged as [MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md). ^[tracing-ag2-databricks-on-aws.md]

## Usage

To enable [Automatic Tracing](/concepts/automatic-tracing.md), call `mlflow.ag2.autolog()` before creating any AG2 agents and initiating conversations: ^[tracing-ag2-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]

# Enable auto-tracing for AG2
[[mlflow|MLflow]].ag2.autolog()
```

After calling `autolog()`, [MLflow](/concepts/mlflow.md) captures [Traces](/concepts/traces.md) for every agent interaction. Optionally configure a [tracking URI](/concepts/mlflow-tracking-uri.md) and [MLflow Experiment](/concepts/mlflow-experiment.md) to control where [Traces](/concepts/traces.md) are stored: ^[tracing-ag2-databricks-on-aws.md]

```python
# Track to Databricks (optional if already configured)
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/ag2-tracing-demo")
```

## What Gets Traced

When `mlflow.ag2.autolog()` is enabled, [MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md) the following events for each agent conversation:

- Messages exchanged between agents (e.g., `user_proxy.initiate_chat()`)
- Tool or function calls made by agents during a conversation
- Execution results returned from registered tools
- Termination messages that end a conversation

The trace data captures the full conversation flow, enabling debugging and observability of multi-agent systems. ^[tracing-ag2-databricks-on-aws.md]

## Prerequisites

- The `autogen` package (AG2 / AutoGen 0.2) must be installed in the Python environment.
- [MLflow](/concepts/mlflow.md) must be configured with a [tracking URI](/concepts/mlflow-tracking-uri.md) to store the [Traces](/concepts/traces.md) (e.g., `"databricks"` for Databricks-hosted [MLflow](/concepts/mlflow.md), or a local or remote [MLflow Tracking](/concepts/mlflow-tracking.md) server).
- For agent models that require API keys (e.g., OpenAI models), appropriate credentials must be set in the environment. ^[tracing-ag2-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The broader [MLflow Tracing](/concepts/mlflow-tracing.md) framework for monitoring LLM and agent workflows.
- AG2 (AutoGen 0.2) — The multi-agent conversational AI framework that `mlflow.ag2.autolog()` instruments.
- [ConversableAgent](/concepts/conversableagent.md) — The base agent class in AG2 that is traced by `autolog()`.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational units for grouping related [Traces](/concepts/traces.md) and runs.
- [Tracking URI](/concepts/mlflow-tracking-uri.md) — Configuration that determines where [MLflow](/concepts/mlflow.md) logs are stored.

## Sources

- tracing-ag2-databricks-on-aws.md

# Citations

1. [tracing-ag2-databricks-on-aws.md](/references/tracing-ag2-databricks-on-aws-417b54da.md)
