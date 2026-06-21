---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 109c0e8c1deadace18ca274c63f2a8fb348fbf71f6974b4fd0a997c5eba8767b
  pageDirectory: concepts
  sources:
    - tracing-anthropic-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - anthropic-tool-calling-trace-with-mlflow
    - ATCTWM
  citations:
    - file: tracing-anthropic-databricks-on-aws.md
title: Anthropic Tool Calling Trace with MLflow
description: Capturing and annotating Anthropic function/tool calling responses in MLflow Traces, including decorating tool functions with @mlflow.trace to create spans
tags:
  - mlflow
  - tracing
  - anthropic
  - tool-calling
  - agents
timestamp: "2026-06-19T23:09:20.097Z"
---

Here is the wiki page for "Anthropic Tool Calling Trace with [MLflow](/concepts/mlflow.md)".

---

## Anthropic Tool Calling Trace with [MLflow](/concepts/mlflow.md)

**Anthropic Tool Calling Trace with MLflow** refers to the capability of [MLflow Tracing](/concepts/mlflow-tracing.md) to automatically capture and log tool calling interactions when using Anthropic's language models. When enabled via the `mlflow.anthropic.autolog()` function, [MLflow](/concepts/mlflow.md) automatically [Traces](/concepts/traces.md) Anthropic SDK invocations, including any tool (function calling) responses returned by the model, and logs them as nested [Traces](/concepts/traces.md) to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-anthropic-databricks-on-aws.md]

### Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) provides [Automatic Tracing](/concepts/automatic-tracing.md) for Anthropic LLMs. By enabling auto tracing through `mlflow.anthropic.autolog()`, [MLflow](/concepts/mlflow.md) captures the full lifecycle of an Anthropic API call, including prompts, completion responses, model name, latency, metadata (such as `temperature` and `max_tokens`), and any exceptions raised. When tool calling is used, the function instructions in the response are highlighted in the trace UI. ^[tracing-anthropic-databricks-on-aws.md]

On [Serverless Compute Clusters](/concepts/serverless-gpu-compute.md), autologging is not automatically enabled — users must explicitly call `mlflow.anthropic.autolog()` to enable tracing. Currently, the [MLflow](/concepts/mlflow.md) Anthropic integration supports tracing only for synchronous calls for text interactions; async APIs were added in [MLflow](/concepts/mlflow.md) 2.21.0. ^[tracing-anthropic-databricks-on-aws.md]

### Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with Anthropic, install the required packages:

- **For development environments:** Install `"[MLflow](/concepts/mlflow.md)[databricks]>=3.1"` and `anthropic`.
- [MLflow 3](/concepts/mlflow-3.md) is highly recommended for the best tracing experience. ^[tracing-anthropic-databricks-on-aws.md]

Users must also configure their environment with an Anthropic API Key. For production use, the recommended approach is to use [AI Gateway](/concepts/ai-gateway.md) or Databricks Secrets instead of environment variables. ^[tracing-anthropic-databricks-on-aws.md]

### Tool Calling Agent Example

The tool calling trace is particularly useful for building agentic applications. Developers can decorate custom tool functions with the `@mlflow.trace(span_type=SpanType.TOOL)` decorator to create a span for tool execution. The agent function itself can be decorated with `@mlflow.trace(span_type=SpanType.AGENT)` to capture the overall agent orchestration. ^[tracing-anthropic-databricks-on-aws.md]

Below is an example of a simple function-calling agent that uses Anthropic's Tool Calling with [MLflow Tracing](/concepts/mlflow-tracing.md) and the asynchronous Anthropic SDK: ^[tracing-anthropic-databricks-on-aws.md]

```python
import json
import anthropic
import [[mlflow|MLflow]]
import asyncio
from [[mlflow|MLflow]].entities import SpanType

# Enable auto-tracing
[[mlflow|MLflow]].anthropic.autolog()
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/anthropic-tool-agent-demo")

client = anthropic.AsyncAnthropic()
model_name = "claude-3-5-sonnet-20241022"

# Define the tool function with [[mlflow-tracing|MLflow Tracing]]
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

# Define the agent with [[mlflow-tracing|MLflow Tracing]]
@mlflow.trace(span_type=SpanType.AGENT)
async def run_tool_agent(question: str):
    messages = [{"role": "user", "content": question}]
    ai_msg = await client.messages.create(
        model=model_name, messages=messages, tools=tools, max_tokens=2048,
    )
    messages.append({"role": "assistant", "content": ai_msg.content})
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
                    {"type": "tool_result", "tool_use_id": tool_call.id, "content": tool_result}
                ],
            }
        )
    response = await client.messages.create(
        model=model_name, messages=messages, max_tokens=2048,
    )
    return response.content[-1].text

# Run the tool calling agent for multiple cities
cities = ["Tokyo", "Paris", "Sydney"]
questions = [f"What's the weather like in {city} today?" for city in cities]
answers = await asyncio.gather(*(run_tool_agent(q) for q in questions))
for city, answer in zip(cities, answers):
    print(f"{city}: {answer}")
```

The resulting trace in the [MLflow](/concepts/mlflow.md) UI highlights the tool call instructions returned by the model, and the `@mlflow.trace`-decorated tool functions appear as separate spans under the agent span. ^[tracing-anthropic-databricks-on-aws.md]

### Supported APIs

[MLflow](/concepts/mlflow.md) supports [Automatic Tracing](/concepts/automatic-tracing.md) for the following Anthropic APIs (async support was added in [MLflow](/concepts/mlflow.md) 2.21.0):

- `anthropic.Anthropic().messages.create()` (synchronous)
- `anthropic.AsyncAnthropic().messages.create()` (async, supported from [MLflow](/concepts/mlflow.md) 2.21.0)

To request support for additional APIs, users can file a feature request on the [MLflow GitHub repository](/concepts/databricks-connect-github-repository.md). ^[tracing-anthropic-databricks-on-aws.md]

### Disabling Auto-Tracing

Auto tracing for Anthropic can be disabled globally by calling either:

- `mlflow.anthropic.autolog(disable=True)`
- `mlflow.autolog(disable=True)`

^[tracing-anthropic-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Anthropic API](/concepts/mlflow-anthropic-autolog.md)
- [Tool Calling (Function Calling)](/concepts/llm-function-calling.md)
- Agent Tracing with MLflow
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [AI Gateway](/concepts/ai-gateway.md)

### Sources

- tracing-anthropic-databricks-on-aws.md

# Citations

1. [tracing-anthropic-databricks-on-aws.md](/references/tracing-anthropic-databricks-on-aws-085cde5b.md)
