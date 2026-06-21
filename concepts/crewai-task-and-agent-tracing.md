---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f71ad1ed0e918eb500ef8392feec8be979dd98ccd33e6251fcbf068a94c95d8
  pageDirectory: concepts
  sources:
    - tracing-crewai-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - crewai-task-and-agent-tracing
    - Agent Tracing and CrewAI Task
    - CTAAT
    - agent tracing for AI agents
  citations:
    - file: tracing-crewai-databricks-on-aws.md
title: CrewAI Task and Agent Tracing
description: MLflow captures nested traces for CrewAI tasks, agents, LLM calls, memory ops, and exceptions
tags:
  - crewai
  - tracing
  - observability
  - mlflow
timestamp: "2026-06-19T23:10:09.839Z"
---

# CrewAI Task and Agent Tracing

**CrewAI Task and Agent Tracing** is an [MLflow Tracing](/concepts/mlflow-tracing.md) integration that automatically captures detailed execution [Traces](/concepts/traces.md) for CrewAI multi-agent workflows, including task assignments, LLM calls, memory operations, and performance metrics.

## Overview

CrewAI is an open-source framework for orchestrating role-playing, autonomous AI agents. By enabling auto-tracing through the `mlflow.crewai.autolog()` function, [MLflow](/concepts/mlflow.md) captures nested [Traces](/concepts/traces.md) for CrewAI workflow execution and logs them to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-crewai-databricks-on-aws.md]

On [serverless compute clusters](/concepts/serverless-gpu-compute-databricks.md), [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks is not automatically enabled. Users must explicitly call the appropriate `mlflow.<library>.autolog()` function for each integration they want to trace. ^[tracing-crewai-databricks-on-aws.md]

## Captured Information

[MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md) automatically capture the following information about CrewAI agents and tasks:

- Tasks and the Agent that executes each task
- Every [Large Language Model (LLM)](/concepts/large-language-models-llms-on-databricks.md) call, including input prompts, completion responses, and various metadata
- Memory load and write operations
- Latency of each operation
- Any exceptions that are raised

^[tracing-crewai-databricks-on-aws.md]

## Current Limitations

- [MLflow](/concepts/mlflow.md) CrewAI integration currently only supports tracing for **synchronous task execution**
- Asynchronous task and kickoff are not supported at this time

^[tracing-crewai-databricks-on-aws.md]

## Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with CrewAI, install [MLflow](/concepts/mlflow.md) version 3 or later and the `crewai` library (which includes `crewai_tools`):

```
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" crewai
```

^[tracing-crewai-databricks-on-aws.md]

### Environment Configuration

Configure environment variables for your Databricks workspace and LLM provider API keys:

```bash
# Databricks credentials (for users outside Databricks notebooks)
export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
export DATABRICKS_TOKEN="your-personal-access-token"

# LLM provider API keys
export OPENAI_API_KEY="your-openai-api-key"
export SERPER_API_KEY="your-serper-api-key"
```

^[tracing-crewai-databricks-on-aws.md]

For production use, use [AI Gateway](/concepts/ai-gateway.md) or Databricks Secrets instead of hardcoded environment variables for API key management. ^[tracing-crewai-databricks-on-aws.md]

## Enabling Auto-Tracing

Enable auto-tracing globally and optionally create an [MLflow Experiment](/concepts/mlflow-experiment.md) to organize [Traces](/concepts/traces.md):

```python
import [[mlflow|MLflow]]
import os

# Turn on auto tracing
[[mlflow|MLflow]].crewai.autolog()

# Set up [[mlflow-tracking|MLflow Tracking]] to Databricks
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/crewai-demo")
```

^[tracing-crewai-databricks-on-aws.md]

After enabling autologging, [Traces](/concepts/traces.md) are automatically captured when executing CrewAI workflows such as `crew.kickoff()`. The example workflow defines trip planning agents that use web search tools, knowledge sources, and memory — all of which are traced by [MLflow](/concepts/mlflow.md). ^[tracing-crewai-databricks-on-aws.md]

## Disabling Auto-Tracing

Auto-tracing for CrewAI can be disabled globally by calling:

```python
[[mlflow|MLflow]].crewai.autolog(disable=True)
```

Or disabled for all frameworks with:

```python
[[mlflow|MLflow]].autolog(disable=True)
```

^[tracing-crewai-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- CrewAI
- LLM Tracing
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md)
- [Serverless Compute Clusters](/concepts/serverless-gpu-compute.md)
- [AI Gateway](/concepts/ai-gateway.md)
- Databricks Secrets

## Sources

- tracing-crewai-databricks-on-aws.md

# Citations

1. [tracing-crewai-databricks-on-aws.md](/references/tracing-crewai-databricks-on-aws-c9f44377.md)
