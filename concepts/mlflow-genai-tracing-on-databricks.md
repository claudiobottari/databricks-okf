---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e37f66487845ce11b9a72e1e9db8324395a402bd945932c47493ea130ecbd11d
  pageDirectory: concepts
  sources:
    - tracing-ag2-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-tracing-on-databricks
    - MGTOD
  citations:
    - file: tracing-ag2-databricks-on-aws.md
title: MLflow GenAI Tracing on Databricks
description: The integration that captures full traces of GenAI agent workflows—LLM calls, tool invocations, and multi-agent message passing—and records them to a Databricks experiment.
tags:
  - mlflow
  - tracing
  - databricks
  - genai
timestamp: "2026-06-19T23:08:24.114Z"
---

# [MLflow GenAI Tracing](/concepts/mlflow-genai-tracing.md) on Databricks

**MLflow GenAI Tracing on Databricks** is a set of capabilities within the [MLflow](/concepts/mlflow.md) platform that enables automatic instrumentation, monitoring, and debugging of [Large Language Model (LLM)](/concepts/large-language-models-llms-on-databricks.md) applications and AI agent workflows running on Databricks. By capturing detailed [Traces](/concepts/traces.md) of calls between LLMs, tools, and other components, GenAI Tracing helps developers understand, optimize, and troubleshoot their generative AI applications.

## Overview

[MLflow GenAI Tracing](/concepts/mlflow-genai-tracing.md) provides automatic instrumentation for popular AI frameworks, recording the sequence of operations—including LLM calls, tool invocations, and intermediate outputs—during the execution of an application. These [Traces](/concepts/traces.md) are stored as part of an [MLflow Experiment](/concepts/mlflow-experiment.md) and can be viewed in the Databricks workspace UI. ^[tracing-ag2-databricks-on-aws.md]

Tracing is enabled on a per-framework basis using framework-specific autologging functions. Once enabled, every call to the framework's agent or conversational components is automatically traced without requiring manual instrumentation of individual function calls. ^[tracing-ag2-databricks-on-aws.md]

## Supported Frameworks

[MLflow GenAI Tracing](/concepts/mlflow-genai-tracing.md) supports multiple agent and LLM orchestration frameworks, including:

- AG2 (formerly AutoGen 0.2)
- LangChain
- LlamaIndex
- [AutoGen](/concepts/autogen-auto-tracing.md) (newer versions)
- OpenAI Python SDK
- Other frameworks as they are added to the [MLflow](/concepts/mlflow.md) integration ecosystem

## How Tracing Works

When autologging is enabled for a supported framework, [MLflow](/concepts/mlflow.md) intercepts the framework's internal communication flows. For example, in an AG2-based multi-agent workflow, [MLflow](/concepts/mlflow.md) captures:

- Messages exchanged between agents (e.g., user proxy and assistant agents)
- Function/tool invocation details (e.g., a calculator function call with its arguments)
- LLM requests and responses (e.g., model name, prompt, completion)
- Termination messages and final outputs ^[tracing-ag2-databricks-on-aws.md]

Each trace is recorded as an [MLflow Run](/concepts/mlflow-run.md), providing a complete audit trail of the application's execution path.

## Enabling Tracing

### Prerequisites

- A Databricks workspace with [MLflow](/concepts/mlflow.md) enabled
- The [MLflow](/concepts/mlflow.md) Python client installed and configured

### Basic Setup

To enable tracing for a specific framework, import [MLflow](/concepts/mlflow.md) and call the framework's autolog function before any application code runs. The following example demonstrates enabling auto-tracing for AG2: ^[tracing-ag2-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]

# Enable auto-tracing for AG2
[[mlflow|MLflow]].ag2.autolog()

# (Optional) Set tracking URI and experiment
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/ag2-tracing-demo")
```

After calling `autolog()`, all subsequent AG2 agent interactions within the same session are automatically traced. ^[tracing-ag2-databricks-on-aws.md]

### Configuration Options

- **Tracking URI**: Set to `"databricks"` to store [Traces](/concepts/traces.md) in the Databricks workspace's [MLflow Tracking](/concepts/mlflow-tracking.md) server.
- **Experiment**: Specify an [MLflow Experiment](/concepts/mlflow-experiment.md) path to organize [Traces](/concepts/traces.md). If not set, [Traces](/concepts/traces.md) are recorded under the default experiment. ^[tracing-ag2-databricks-on-aws.md]

## Viewing [Traces](/concepts/traces.md)

[Traces](/concepts/traces.md) are accessible through:

1. The **MLflow experiment** page in the Databricks workspace UI
2. The **Runs** tab, where each trace appears as a separate run
3. The **Traces** view within an experiment, which provides a dedicated visualization for trace data

Users can inspect individual spans within a trace to see details such as input parameters, output values, execution duration, and error messages.

## Use Cases

- **Debugging multi-agent workflows**: Identify where an agent made an incorrect tool selection or received unexpected input.
- **Performance optimization**: Analyze latency contributions from LLM calls versus tool executions.
- **Auditing and compliance**: Maintain a record of all LLM interactions for governance purposes.
- **Evaluation and testing**: Compare [Traces](/concepts/traces.md) across different model versions or prompt configurations.

## Best Practices

- Enable autologging at the beginning of your notebook or script before any agent code runs.
- Use descriptive experiment names to organize [Traces](/concepts/traces.md) by project or workflow type.
- Set the tracking URI to `"databricks"` to leverage workspace-level trace storage and sharing capabilities. ^[tracing-ag2-databricks-on-aws.md]
- For [Production Monitoring](/concepts/production-monitoring.md), combine tracing with [MLflow Model Evaluation](/concepts/mlflow-evaluation-ui.md) and [MLflow Production Monitoring](/concepts/mlflow-production-monitoring.md).

## Limitations

- Tracing captures only the interactions within the instrumented framework; direct LLM API calls outside the framework may not be traced automatically.
- Trace data volume can grow quickly for long-running agent workflows; consider setting appropriate retention policies.
- Framework-specific autologging may not cover all custom extensions or wrappers built by users.

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — The underlying system for logging parameters, metrics, and artifacts.
- [MLflow Autologging](/concepts/mlflow-autologging.md) — Automatic instrumentation for ML frameworks (including GenAI).
- [LLM Monitoring](/concepts/human-feedback-in-llm-monitoring.md) — Broader monitoring practices for generative AI applications.
- AI Agent Debugging — Techniques and tools for diagnosing issues in agent-based systems.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational units for grouping trace runs.
- Distributed Tracing — General concept applied to AI workloads.

## Sources

- tracing-ag2-databricks-on-aws.md

# Citations

1. [tracing-ag2-databricks-on-aws.md](/references/tracing-ag2-databricks-on-aws-417b54da.md)
