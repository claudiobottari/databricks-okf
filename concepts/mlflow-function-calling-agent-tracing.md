---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9bcaf72b2861813dae3d7e54533ee25b69db228d42fbdd3e8e0fe36870806a4f
  pageDirectory: concepts
  sources:
    - tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-function-calling-agent-tracing
    - MFCAT
    - Function Calling Agent Tracing
  citations:
    - file: tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md
title: MLflow Function Calling Agent Tracing
description: Combining MLflow's @mlflow.trace decorator with mlflow.bedrock.autolog enables tracing of custom ReAct-style function-calling agents, capturing the full chain of LLM invocations and tool executions as a single trace.
tags:
  - mlflow
  - agents
  - tracing
  - function-calling
timestamp: "2026-06-19T23:08:48.394Z"
---

# [MLflow](/concepts/mlflow.md) Function Calling Agent Tracing

**MLflow Function Calling Agent Tracing** refers to the combined use of [MLflow](/concepts/mlflow.md)'s [Automatic Tracing](/concepts/automatic-tracing.md) for Amazon Bedrock and [Manual Tracing](/concepts/manual-tracing.md) decorators to capture end-to-end execution [Traces](/concepts/traces.md) of function-calling (ReAct) agents. This capability enables developers to observe and debug agent workflows that involve multiple LLM invocations and tool executions within a single trace.

## Overview

When building a function-calling agent that interacts with Amazon Bedrock, [MLflow Tracing](/concepts/mlflow-tracing.md) automatically captures function calling metadata, including tool definitions and invocation instructions. These details are highlighted in the **Chat** tab of the trace UI. By combining automatic Bedrock tracing with [Manual Tracing](/concepts/manual-tracing.md) via the `@mlflow.trace` decorator, developers can create comprehensive [Traces](/concepts/traces.md) that capture the entire agent execution chain, including LLM calls and tool function executions. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Setup

To enable function calling agent tracing, two components are required:

1. **Automatic Bedrock tracing**: Call `mlflow.bedrock.autolog()` to enable automatic trace capture for all Amazon Bedrock API invocations. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]
2. **Manual function tracing**: Decorate tool functions with `@mlflow.trace(span_type=SpanType.TOOL)` and the agent orchestrator with `@mlflow.trace(span_type=SpanType.AGENT)`. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

[MLflow](/concepts/mlflow.md) automatically resolves call chains and records execution metadata, so the tracing implementation remains straightforward even for complex agent logic. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Trace Structure

A function calling agent trace captures the following components:

- **LLM invocations**: Each call to Bedrock APIs (e.g., `converse`) is automatically traced, including prompts, completion responses, latencies, model name, and configuration parameters such as `temperature` and `maxTokens`. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]
- **Tool calls**: Functions decorated with `@mlflow.trace(span_type=SpanType.TOOL)` create dedicated spans showing the tool name, input arguments, and return values. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]
- **Agent orchestration**: The main agent function decorated with `@mlflow.trace(span_type=SpanType.AGENT)` serves as the parent span, encompassing all child spans for LLM calls and tool executions. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]
- **Function calling metadata**: Tool definitions and invocation instructions are highlighted in the **Chat** tab of the trace UI. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Supported Bedrock APIs

[MLflow](/concepts/mlflow.md) supports [Automatic Tracing](/concepts/automatic-tracing.md) for the following Amazon Bedrock APIs used in function calling agents:

- `converse`
- `converse_stream`
- `invoke_model`
- `invoke_model_with_response_stream`

The **Chat** tab UI is only supported for `converse` and `converse_stream`. For the other APIs, [MLflow](/concepts/mlflow.md) displays only the **Inputs / Outputs** tab. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Example: Tool Calling Agent

A typical function calling agent implementation involves:

1. Defining a tool function and decorating it with `@mlflow.trace(span_type=SpanType.TOOL)`.
2. Defining the agent orchestrator function with `@mlflow.trace(span_type=SpanType.AGENT)`.
3. Enabling automatic Bedrock tracing via `mlflow.bedrock.autolog()`.
4. Implementing the agent logic to handle tool use requests from the model response.

The resulting trace captures all LLM invocations and tool calls in a single, coherent trace displayed in the [MLflow](/concepts/mlflow.md) UI. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Prerequisites

- [MLflow 3](/concepts/mlflow-3.md) or later (recommended)
- AWS SDK for Python (Boto3)
- Configured AWS credentials for Bedrock access
- Databricks workspace credentials (automatic inside Databricks notebooks)

Installation command: `pip install --upgrade "[MLflow](/concepts/mlflow.md)[databricks]>=3.1" boto3` ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Disabling Auto-Tracing

Auto tracing for Amazon Bedrock can be disabled globally by calling `mlflow.bedrock.autolog(disable=True)` or `mlflow.autolog(disable=True)`. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The general tracing framework for capturing LLM execution metadata.
- Amazon Bedrock Integration — [MLflow](/concepts/mlflow.md)'s [Automatic Tracing](/concepts/automatic-tracing.md) for Bedrock API calls.
- Span Types — Classification of traced operations (AGENT, TOOL, LLM, etc.).
- ReAct Agent Pattern — The function-calling agent pattern used in the tracing example.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for logged [Traces](/concepts/traces.md).

## Sources

- tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md

# Citations

1. [tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md](/references/tracing-amazon-bedrock-with-mlflow-databricks-on-aws-2f3942c6.md)
