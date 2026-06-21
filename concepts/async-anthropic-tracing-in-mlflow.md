---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1a73e3a46eb93fd394545e71d500f711b8174ed3f7ee6b0d4cbe60e49c80c67c
  pageDirectory: concepts
  sources:
    - tracing-anthropic-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - async-anthropic-tracing-in-mlflow
    - AATIM
    - Synchronous Anthropic Tracing in MLflow
    - Async tracing in MLflow
  citations:
    - file: tracing-anthropic-databricks-on-aws.md
title: Async Anthropic Tracing in MLflow
description: Support for tracing asynchronous Anthropic SDK calls (AsyncAnthropic) added in MLflow 2.21.0, enabling non-blocking concurrent invocation tracing
tags:
  - mlflow
  - tracing
  - anthropic
  - async
timestamp: "2026-06-19T23:09:21.283Z"
---

# Async Anthropic Tracing in [MLflow](/concepts/mlflow.md)

**Async Anthropic Tracing in MLflow** refers to the automatic capture of [Traces](/concepts/traces.md) from asynchronous calls to the Anthropic Python SDK, enabling observability into non-blocking LLM interactions. [MLflow](/concepts/mlflow.md) provides [Automatic Tracing](/concepts/automatic-tracing.md) for Anthropic's async APIs, allowing developers to monitor and debug concurrent AI agent workflows. ^[tracing-anthropic-databricks-on-aws.md]

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) provides [Automatic Tracing](/concepts/automatic-tracing.md) capability for Anthropic LLMs. By enabling auto tracing for Anthropic via the `mlflow.anthropic.autolog()` function, [MLflow](/concepts/mlflow.md) captures nested [Traces](/concepts/traces.md) and logs them to the active [MLflow Experiment](/concepts/mlflow-experiment.md) upon invocation of the Anthropic Python SDK. ^[tracing-anthropic-databricks-on-aws.md]

Async support for Anthropic was added in [MLflow](/concepts/mlflow.md) 2.21.0. ^[tracing-anthropic-databricks-on-aws.md]

## Supported APIs

[MLflow](/concepts/mlflow.md) supports [Automatic Tracing](/concepts/automatic-tracing.md) for the following Anthropic APIs:

- **Synchronous**: `client.messages.create()` — text interactions
- **Async**: `await client.messages.create()` — asynchronous text interactions (supported from [MLflow](/concepts/mlflow.md) 2.21.0+)

Currently, [MLflow](/concepts/mlflow.md) Anthropic integration only supports tracing for synchronous calls for text interactions. Async APIs are traced, but full inputs cannot be recorded for multi-modal inputs. ^[tracing-anthropic-databricks-on-aws.md]

## Captured Information

[[mlflow-trace|MLflow Trace]] automatically captures the following information about Anthropic calls:

- Prompts and completion responses
- Latencies
- Model name
- Additional metadata such as `temperature` and `max_tokens`, if specified
- Function calling if returned in the response
- Any exception if raised

^[tracing-anthropic-databricks-on-aws.md]

## Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with Anthropic, install [MLflow](/concepts/mlflow.md) and the Anthropic SDK:

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" anthropic
```

[MLflow 3](/concepts/mlflow-3.md) is highly recommended for the best tracing experience with Anthropic. ^[tracing-anthropic-databricks-on-aws.md]

### Environment Configuration

**For users outside Databricks notebooks**: Set your Databricks environment variables:

```bash
export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
export DATABRICKS_TOKEN="your-personal-access-token"
```

**For users inside Databricks notebooks**: These credentials are automatically set for you.

**API Keys**: Ensure your Anthropic API key is configured. For production use, Databricks recommends using [AI Gateway](/concepts/ai-gateway.md) or Databricks Secrets instead of environment variables:

```bash
export ANTHROPIC_API_KEY="your-anthropic-api-key"
```

^[tracing-anthropic-databricks-on-aws.md]

## Basic Async Example

```python
import anthropic
import [[mlflow|MLflow]]
import os

# Enable auto-tracing for Anthropic
[[mlflow|MLflow]].anthropic.autolog()

# Set up [[mlflow-tracking|MLflow Tracking]] to Databricks if not already configured
# [[mlflow|MLflow]].set_tracking_uri("databricks")
# [[mlflow|MLflow]].set_experiment("/Shared/anthropic-async-demo")

client = anthropic.AsyncAnthropic()

response = await client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"},
    ],
)
```

^[tracing-anthropic-databricks-on-aws.md]

## Tool Calling with Async Tracing

[MLflow Tracing](/concepts/mlflow-tracing.md) automatically captures tool calling responses from Anthropic models. The function instruction in the response is highlighted in the trace UI. You can annotate tool functions with the `@mlflow.trace` decorator to create a span for tool execution. ^[tracing-anthropic-databricks-on-aws.md]

The following example implements a simple function calling agent using Anthropic Tool Calling and [MLflow Tracing](/concepts/mlflow-tracing.md). It uses the asynchronous Anthropic SDK so the agent can handle concurrent invocations without blocking:

```python
import json
import anthropic
import [[mlflow|MLflow]]
import asyncio
from [[mlflow|MLflow]].entities import SpanType
import os

# Enable auto-tracing
[[mlflow|MLflow]].anthropic.autolog()

client = anthropic.AsyncAnthropic()
model_name = "claude-3-5-sonnet-20241022"

# Define the tool function. Decorate it with @mlflow.trace to create a span.
@mlflow.trace(span_type=SpanType.TOOL)
async def get_weather(city: str) -> str:
    if city == "Tokyo":
        return "sunny"
    elif city == "Paris":
        return "rainy"
    return "unknown"

tools = [
    {
        "name": "get_weather",
        "description": "Returns the weather condition of a given city.",
        "input_schema": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    }
]

_tool_functions = {"get_weather": get_weather}

# Define a simple tool calling agent
@mlflow.trace(span_type=SpanType.AGENT)
async def run_tool_agent(question: str):
    messages = [{"role": "user", "content": question}]
    
    # Invoke the model with the given question and available tools
    ai_msg = await client.messages.create(
        model=model_name,
        messages=messages,
        tools=tools,
        max_tokens=2048,
    )
    messages.append({"role": "assistant", "content": ai_msg.content})
    
    # If the model requests tool call(s), invoke the function
    tool_calls = [c for c in ai_msg.content if c.type == "tool_use"]
    for tool_call in tool_calls:
        if tool_func := _tool_functions.get(tool_call.name):
            tool_result = await tool_func(**tool_call.input)
        else:
            raise RuntimeError("An invalid tool is returned from the assistant!")
        messages.append(
            {
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": tool_call.id,
                        "content": tool_result,
                    }
                ],
            }
        )
    
    # Send the tool results to the model and get a new response
    response = await client.messages.create(
        model=model_name,
        messages=messages,
        max_tokens=2048,
    )
    return response.content[-1].text

# Run the tool calling agent with concurrent invocations
cities = ["Tokyo", "Paris", "Sydney"]
questions = [f"What's the weather like in {city} today?" for city in cities]
answers = await asyncio.gather(*(run_tool_agent(q) for q in questions))

for city, answer in zip(cities, answers):
    print(f"{city}: {answer}")
```

^[tracing-anthropic-databricks-on-aws.md]

## Important Notes

- **Serverless compute clusters**: Autologging is not automatically enabled. You must explicitly call `mlflow.anthropic.autolog()` to enable [Automatic Tracing](/concepts/automatic-tracing.md). ^[tracing-anthropic-databricks-on-aws.md]
- **Multi-modal inputs**: Full inputs cannot be recorded for multi-modal inputs in async mode. ^[tracing-anthropic-databricks-on-aws.md]
- **Disabling auto-tracing**: Auto tracing for Anthropic can be disabled globally by calling `mlflow.anthropic.autolog(disable=True)` or `mlflow.autolog(disable=True)`. ^[tracing-anthropic-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The underlying tracing framework for capturing LLM interactions
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit where [Traces](/concepts/traces.md) are logged
- [AI Gateway](/concepts/ai-gateway.md) — Recommended for secure API key management in production
- Databricks Secrets — Alternative secure credential storage
- Synchronous Anthropic Tracing in MLflow — The synchronous counterpart for non-async calls
- OpenAI Tracing in MLflow — Similar tracing capabilities for OpenAI models

## Sources

- tracing-anthropic-databricks-on-aws.md

# Citations

1. [tracing-anthropic-databricks-on-aws.md](/references/tracing-anthropic-databricks-on-aws-085cde5b.md)
