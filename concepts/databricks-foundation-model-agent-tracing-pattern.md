---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 72ca6288b3c24feceada988254853a46794440a80c02aa6d9c7dc01841410cda
  pageDirectory: concepts
  sources:
    - tracing-databricks-foundation-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-foundation-model-agent-tracing-pattern
    - DFMATP
  citations:
    - file: tracing-databricks-foundation-models-databricks-on-aws.md
title: Databricks Foundation Model Agent Tracing Pattern
description: A design pattern for building tool-calling agents with Databricks Foundation Models where MLflow Tracing automatically captures the full agent loop including model invocations, tool function execution (decorated with @mlflow.trace), and final responses.
tags:
  - mlflow
  - agents
  - tracing
  - pattern
timestamp: "2026-06-19T23:11:28.111Z"
---

# Databricks Foundation Model Agent Tracing Pattern

The **Databricks Foundation Model Agent Tracing Pattern** refers to the use of [MLflow Tracing](/concepts/mlflow-tracing.md) combined with Databricks Foundation Models to capture and visualize the full execution flow of an LLM-based agent. By enabling [Automatic Tracing](/concepts/automatic-tracing.md) via `mlflow.openai.autolog()`, every call to a Databricks Foundation Model endpoint — including prompts, responses, latencies, tool calls, and exceptions — is recorded as a trace in the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Overview

Databricks Foundation Models expose an OpenAI-compatible API. [MLflow](/concepts/mlflow.md) provides an [Automatic Tracing](/concepts/automatic-tracing.md) integration that builds on top of the OpenAI SDK: calling `mlflow.openai.autolog()` instruments the OpenAI client so that any subsequent request to a Databricks Foundation Model endpoint is transparently traced. This pattern is the recommended way to capture observability data for agents that use Databricks-hosted models. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

On serverless compute clusters, autologging is not automatically enabled; you must explicitly call `mlflow.openai.autolog()` to activate tracing for this integration. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Captured Information

A trace automatically captures the following data for each Databricks Foundation Model call: ^[tracing-databricks-foundation-models-databricks-on-aws.md]

- Prompts and completion responses
- Latencies
- Model name and endpoint
- Additional metadata such as `temperature` and `max_tokens` (if specified)
- Function calling arguments and results (if returned in the response)
- Any exception that is raised

## Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with Databricks Foundation Models, install [MLflow](/concepts/mlflow.md) and the OpenAI SDK. For development environments, the recommended command is: ^[tracing-databricks-foundation-models-databricks-on-aws.md]

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" openai
```

[MLflow 3](/concepts/mlflow-3.md) is highly recommended for the best tracing experience. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

Before running examples, configure your environment. Users outside Databricks notebooks must set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables. Inside Databricks notebooks, these credentials are automatically available. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Supported APIs

[MLflow](/concepts/mlflow.md) supports [Automatic Tracing](/concepts/automatic-tracing.md) for the following [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md):

- Chat Completions (`client.chat.completions.create`) – both non-streaming and streaming
- Function/Tool Calling (via the `tools` parameter in Chat Completions)

To request support for additional APIs, file a feature request on the [MLflow](/concepts/mlflow.md) GitHub repository](https://github.com/[MLflow](/concepts/mlflow.md)/[MLflow](/concepts/mlflow.md)/issues). ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Basic Example

The following example enables auto-tracing, configures the OpenAI client for a Databricks workspace, and sends a chat completion request. The trace is automatically logged to the specified experiment. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]
import os
from openai import OpenAI

[[mlflow|MLflow]].openai.autolog()
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/databricks-foundation-models-demo")

client = OpenAI(
    api_key=os.environ.get("DATABRICKS_TOKEN"),
    base_url=f"{os.environ.get('DATABRICKS_HOST')}/serving-endpoints"
)

response = client.chat.completions.create(
    model="databricks-llama-4-maverick",
    messages=[{"role": "user", "content": "What is the capital of France?"}],
    temperature=0.1,
    max_tokens=100,
)
```

## Streaming

[MLflow Tracing](/concepts/mlflow-tracing.md) also supports streaming responses. The same auto-tracing setup captures the streaming response and renders the concatenated output in the span UI. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

```python
stream = client.chat.completions.create(
    model="databricks-llama-4-maverick",
    messages=[{"role": "user", "content": "Explain the benefits of using Databricks Foundation Models"}],
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
```

## Function Calling (Agent Pattern)

The function calling feature enables agent-like behavior. [MLflow Tracing](/concepts/mlflow-tracing.md) automatically captures the function calling request and response from the model. To trace tool execution, decorate each tool function with the `@mlflow.trace` decorator, and optionally wrap the agent logic with another `@mlflow.trace` decorator to create a parent span. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

The following example implements a simple tool-calling agent that uses a weather function and [Traces](/concepts/traces.md) both the model interaction and the tool execution: ^[tracing-databricks-foundation-models-databricks-on-aws.md]

```python
import json
from openai import OpenAI
import [[mlflow|MLflow]]
from [[mlflow|MLflow]].entities import SpanType

[[mlflow|MLflow]].openai.autolog()
client = OpenAI(
    api_key=os.environ.get("DATABRICKS_TOKEN"),
    base_url=f"{os.environ.get('DATABRICKS_HOST')}/serving-endpoints"
)

@mlflow.trace(span_type=SpanType.TOOL)
def get_weather(city: str) -> str:
    if city == "Tokyo":
        return "sunny"
    elif city == "Paris":
        return "rainy"
    return "unknown"

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "parameters": {"type": "object", "properties": {"city": {"type": "string"}}}
    }
}]

_tool_functions = {"get_weather": get_weather}

@mlflow.trace(span_type=SpanType.AGENT)
def run_tool_agent(question: str):
    messages = [{"role": "user", "content": question}]
    response = client.chat.completions.create(
        model="databricks-llama-4-maverick", messages=messages, tools=tools
    )
    ai_msg = response.choices[0].message
    if tool_calls := ai_msg.tool_calls:
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            if tool_func := _tool_functions.get(function_name):
                args = json.loads(tool_call.function.arguments)
                tool_result = tool_func(**args)
            else:
                raise RuntimeError("An invalid tool is returned from the assistant!")
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": tool_result,
            })
        response = client.chat.completions.create(
            model="databricks-llama-4-maverick", messages=messages
        )
    return response.choices[0].message.content

answer = run_tool_agent("What's the weather like in Paris today?")
```

In this pattern, the `@mlflow.trace` decorator creates a Span for the tool function, and the outer `@mlflow.trace(span_type=SpanType.AGENT)` creates a higher-level span for the entire agent workflow. The trace UI highlights the function calling instructions and tool results. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Disabling Auto-Tracing

Auto tracing can be disabled globally by calling `mlflow.openai.autolog(disable=True)` or `mlflow.autolog(disable=True)`. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Available Models

Databricks Foundation Models provides access to models such as Llama, Anthropic, and other leading foundation models. For the complete list of model IDs, refer to the Databricks Foundation Models documentation. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [MLflow Experiment](/concepts/mlflow-experiment.md)
- Span
- [Autologging](/concepts/mlflow-autologging.md)
- [Function Calling](/concepts/llm-function-calling.md)
- LLM Agent
- Databricks Foundation Models
- OpenAI

## Sources

- tracing-databricks-foundation-models-databricks-on-aws.md

# Citations

1. [tracing-databricks-foundation-models-databricks-on-aws.md](/references/tracing-databricks-foundation-models-databricks-on-aws-5051d97b.md)
