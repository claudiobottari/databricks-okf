---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22281de0787aa9cc360fa6150fd08c285b9714f5de89f3a6d7641ed8cfae5cf0
  pageDirectory: concepts
  sources:
    - tracing-crewai-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-crewai-autolog
    - MCA
  citations:
    - file: tracing-crewai-databricks-on-aws.md
title: MLflow CrewAI Autolog
description: Automatic tracing for CrewAI multi-agent workflows via mlflow.crewai.autolog()
tags:
  - mlflow
  - tracing
  - crewai
  - observability
timestamp: "2026-06-19T23:10:17.486Z"
---

# [MLflow](/concepts/mlflow.md) CrewAI Autolog

**MLflow CrewAI Autolog** is an [Automatic Tracing](/concepts/automatic-tracing.md) capability provided by [MLflow Tracing](/concepts/mlflow-tracing.md) that captures nested [Traces](/concepts/traces.md) for CrewAI workflow execution. By enabling autologging via the [`mlflow.crewai.autolog`](https://[MLflow](/concepts/mlflow.md).org/docs/latest/api_reference/python_api/[MLflow](/concepts/mlflow.md).crewai.html#mlflow.crewai.autolog) function, [MLflow](/concepts/mlflow.md) records detailed trace data from CrewAI agents and logs them to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-crewai-databricks-on-aws.md]

## How to Enable

To enable [Automatic Tracing](/concepts/automatic-tracing.md) for CrewAI, call `mlflow.crewai.autolog()` before running any CrewAI workflows:

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].crewai.autolog()
```

On serverless compute clusters, autologging for generative AI tracing frameworks is not automatically enabled. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace. ^[tracing-crewai-databricks-on-aws.md]

## Information Captured

[MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md) automatically capture the following information about CrewAI agents: ^[tracing-crewai-databricks-on-aws.md]

- Tasks and the agent who executes each task
- Every LLM call with input prompts, completion responses, and various metadata
- Memory load and write operations
- Latency of each operation
- Any exception if raised

## Limitations

Currently, MLflow’s CrewAI integration only supports tracing for synchronous task execution. Asynchronous tasks and `kickoff` are not supported. ^[tracing-crewai-databricks-on-aws.md]

## Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with CrewAI, install the required packages:

- **Development environments**: Install the full [MLflow](/concepts/mlflow.md) package with Databricks extras and `crewai`:
  ```bash
  pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" crewai
  ```

[MLflow 3](/concepts/mlflow-3.md) is highly recommended for the best tracing experience with CrewAI. ^[tracing-crewai-databricks-on-aws.md]

Additionally, configure your environment:

- **Outside Databricks notebooks**: Set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables.
- **Inside Databricks notebooks**: Credentials are automatically set.
- **API Keys**: Ensure necessary LLM provider API keys are configured. For production, use [AI Gateway](/concepts/ai-gateway.md) or Databricks secrets instead of hardcoded values. ^[tracing-crewai-databricks-on-aws.md]

## Example Usage

The following example demonstrates enabling autologging and running a multi-agent trip planning workflow: ^[tracing-crewai-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]
import os

# Set API keys (example: OpenAI and Serper)
# os.environ["OPENAI_API_KEY"] = "your-openai-key"
# os.environ["SERPER_API_KEY"] = "your-serper-key"

# Enable auto-tracing
[[mlflow|MLflow]].crewai.autolog()

# Set [[mlflow-tracking|MLflow Tracking]] to Databricks
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/crewai-demo")

# Define agents, tasks, and crew (see full example in source)
# ...
```

After enabling autologging, every call to `crew.kickoff()` generates a nested trace that is logged to the specified experiment.

## Disabling Autologging

Auto-tracing for CrewAI can be disabled globally by calling:
- `mlflow.crewai.autolog(disable=True)`, or
- `mlflow.autolog(disable=True)`.

^[tracing-crewai-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The core tracing infrastructure that powers autologging.
- CrewAI – The open-source multi-agent framework that is traced.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The organizational unit for storing [Traces](/concepts/traces.md).
- [Autologging](/concepts/mlflow-autologging.md) – MLflow’s general mechanism for automatic instrumentation.
- [Serverless Compute Databricks](/concepts/serverless-gpu-compute-databricks.md) – Compute environment where explicit autolog calls are needed.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – Another [MLflow](/concepts/mlflow.md) feature that may involve tracing.
- [LLM Monitoring](/concepts/human-feedback-in-llm-monitoring.md) – Monitoring large language model calls, which autolog captures.

## Sources

- tracing-crewai-databricks-on-aws.md

# Citations

1. [tracing-crewai-databricks-on-aws.md](/references/tracing-crewai-databricks-on-aws-c9f44377.md)
