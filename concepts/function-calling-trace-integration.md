---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6421344da1e5ea51e2c9cf03a1e227c8d149a8eaec9bc1ec6faef2956b97705d
  pageDirectory: concepts
  sources:
    - tracing-databricks-foundation-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - function-calling-trace-integration
    - FCTI
    - Function Calling Trace Support
  citations:
    - file: tracing-databricks-foundation-models-databricks-on-aws.md
title: Function Calling Trace Integration
description: MLflow auto-traces function calling responses from Databricks Foundation Models, highlights function instructions in the trace UI, and supports decorating tool functions with @mlflow.trace to create spans for tool execution.
tags:
  - mlflow
  - tracing
  - function-calling
  - agents
timestamp: "2026-06-19T23:11:21.454Z"
---

# Function Calling Trace Integration

**Function Calling Trace Integration** refers to [MLflow Tracing](/concepts/mlflow-tracing.md)](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/)'s ability to automatically capture and visualize function calling workflows when invoking Databricks Foundation Models. Since Databricks Foundation Models expose an OpenAI-compatible API, [MLflow](/concepts/mlflow.md)'s OpenAI autologging automatically [Traces](/concepts/traces.md) function call requests, responses, and tool execution paths. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Overview

When using Databricks Foundation Models with function calling, [MLflow](/concepts/mlflow.md) automatically captures the function instruction returned in the model response and highlights it in the trace UI. Beyond capturing the model's function call request, developers can further annotate their custom tool functions with the `@mlflow.trace` decorator to create dedicated spans for tool execution, providing end-to-end visibility of the agent workflow. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## How It Works

The integration works by calling `mlflow.openai.autolog()` to enable [Automatic Tracing](/concepts/automatic-tracing.md) for all OpenAI-compatible API calls, including those directed at Databricks [Foundation Model Serving Endpoints](/concepts/foundation-model-serving-endpoints.md). When a function calling request is made—where the `tools` parameter is provided—MLflow [Traces](/concepts/traces.md): ^[tracing-databricks-foundation-models-databricks-on-aws.md]

- The original prompt and the model's response containing function call instructions
- Any tool function execution wrapped with `@mlflow.trace(span_type=SpanType.TOOL)`
- The subsequent model response after tool results are returned
- Latencies for each step of the agent loop

A simple tool-calling agent decorated with `@mlflow.trace(span_type=SpanType.AGENT)` can wrap the entire agent orchestration, providing a parent span that contains sub-spans for the model calls and tool executions. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Example: Function Calling Agent with Tracing

The following example demonstrates a weather lookup agent that uses function calling with full trace instrumentation: ^[tracing-databricks-foundation-models-databricks-on-aws.md]

```python
import json
import os
from openai import OpenAI
import [[mlflow|MLflow]]
from [[mlflow|MLflow]].entities import SpanType

# Enable auto-tracing for OpenAI (which will trace Databricks Foundation Model API calls)
[[mlflow|MLflow]].openai.autolog()

# Create OpenAI client configured for Databricks
client = OpenAI(
    api_key=os.environ.get("DATABRICKS_TOKEN"),
    base_url=f"{os.environ.get('DATABRICKS_HOST')}/serving-endpoints"
)

# Define the tool function with @mlflow.trace to create a span for its execution
@mlflow.trace(span_type=SpanType.TOOL)
def get_weather(city: str) -> str:
    if city == "Tokyo":
        return "sunny"
    elif city == "Paris":
        return "rainy"
    return "unknown"

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
            },
        },
    }
]

_tool_functions = {"get_weather": get_weather}

# Define a simple tool calling agent with @mlflow.trace
@mlflow.trace(span_type=SpanType.AGENT)
def run_tool_agent(question: str):
    messages = [{"role": "user", "content": question}]

    # Invoke the model with the given question and available tools
    response = client.chat.completions.create(
        model="databricks-llama-4-maverick",
        messages=messages,
        tools=tools,
    )
    ai_msg = response.choices[0].message

    # If the model requests tool call(s), invoke the function
    if tool_calls := ai_msg.tool_calls:
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            if tool_func := _tool_functions.get(function_name):
                args = json.loads(tool_call.function.arguments)
                tool_result = tool_func(**args)
            else:
                raise RuntimeError("An invalid tool is returned from the assistant!")
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": tool_result,
                }
            )
        # Send the tool results to the model and get a new response
        response = client.chat.completions.create(
            model="databricks-llama-4-maverick", messages=messages
        )
    return response.choices[0].message.content

# Run the tool calling agent
question = "What's the weather like in Paris today?"
answer = run_tool_agent(question)
```

## Trace Visualization

In the [[mlflow-trace|MLflow Trace]] UI, the [Function Calling Workflow](/concepts/function-calling-workflow.md) is visualized with:

1. An **AGENT** span wrapping the entire `run_tool_agent` orchestration
2. Child spans for each model call (`client.chat.completions.create`), showing the function call request and response
3. **TOOL** spans for each tool function execution (e.g., `get_weather`)
4. The final model response after incorporating tool results

The function instruction returned by the model is highlighted in the span UI, making it easy to inspect which function was requested and with what arguments. ^[tracing-databricks-foundation-models-databricks-on-aws.md]

## Prerequisites

To use function calling trace integration, install [MLflow 3](/concepts/mlflow-3.md) or later with Databricks extras and the OpenAI SDK: ^[tracing-databricks-foundation-models-databricks-on-aws.md]

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" openai
```

For users outside Databricks notebooks, set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables. Inside Databricks notebooks, these credentials are automatically configured.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing framework underlying this integration
- Databricks Foundation Models — The [Model Serving](/concepts/model-serving.md) endpoints being traced
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Where [Traces](/concepts/traces.md) are logged
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation workflows that benefit from function calling [Traces](/concepts/traces.md)
- [OpenAI Autologging](/concepts/mlflow-openai-autolog.md) — The mechanism used to capture [Traces](/concepts/traces.md) automatically

## Sources

- tracing-databricks-foundation-models-databricks-on-aws.md

# Citations

1. [tracing-databricks-foundation-models-databricks-on-aws.md](/references/tracing-databricks-foundation-models-databricks-on-aws-5051d97b.md)
