---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ddaa75efbe908baea2b27c6c8f445c2c5a559ad33e2dbf6fdb0d0531616f203c
  pageDirectory: concepts
  sources:
    - function-calling-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - function-calling-workflow
    - FCW
  citations:
    - file: function-calling-on-databricks-databricks-on-aws.md
title: Function Calling Workflow
description: The four-step sequence of calling the model with tools, receiving JSON function arguments, executing the function in code, and returning results to the model for summarization.
tags:
  - workflow
  - function-calling
  - LLM
timestamp: "2026-06-19T10:40:47.440Z"
---

# Function Calling Workflow

**Function Calling Workflow** refers to the process of using large language models (LLMs) to generate structured JSON output that can be used to invoke external functions or APIs. On Databricks, function calling is OpenAI-compatible and available through [Foundation Model APIs](/concepts/foundation-model-apis.md) and serving endpoints for [External Models](/concepts/external-models.md). ^[function-calling-on-databricks-databricks-on-aws.md]

## Overview

Function calling provides a way to control LLM output so that it generates structured responses more reliably. The developer describes functions—including their names, descriptions, and argument schemas—in the API call using a JSON schema. The LLM does **not** execute these functions; instead, it produces a JSON object containing the arguments that the developer’s code can then use to call the actual functions. ^[function-calling-on-databricks-databricks-on-aws.md]

The basic sequence of steps is:

1. Call the model with the user query and a set of functions defined in the `tools` parameter.
2. The model decides whether to call one or more of the defined functions. If it does, the response includes a JSON object of strings adhering to the custom schema.
3. Parse the JSON in your code and invoke the function with the provided arguments.
4. Call the model again, appending the structured response as a new message. The model then summarizes the results and returns that summary to the user. ^[function-calling-on-databricks-databricks-on-aws.md]

## When to Use Function Calling

Common use cases include:

- Creating assistants that answer questions by calling other APIs (e.g., `send_email(to, body)` or `current_weather(location, unit)`).
- Turning natural language into API calls (e.g., “Who are my top customers?” becomes a `get_customers(min_revenue, created_before, limit)` call). ^[function-calling-on-databricks-databricks-on-aws.md]

For batch inference or data processing tasks (converting unstructured to structured data), Databricks recommends using [Structured Outputs](/concepts/structured-outputs-in-foundation-model-apis.md) instead. ^[function-calling-on-databricks-databricks-on-aws.md]

## Supported Models

The following table lists supported models and their availability through Databricks model serving features. See the source documentation for region availability and applicable terms.

| Model | Availability |
|---|---|
| Meta-Llama-3.3-70B-Instruct (replaces Meta-Llama-3.1-70B-Instruct) | Foundation Model APIs / External Models |
| Meta-Llama-3.1-405B-Instruct | Foundation Model APIs (pay-per-token until Feb 15, 2026; provisioned throughput until May 15, 2026) |
| Claude models (e.g., for multi-turn) | Foundation Model APIs / External Models |
| Google Gemini models (retirement planned) | External Models |

For the full list, refer to the [function calling documentation](https://docs.databricks.com/aws/en/machine-learning/model-serving/function-calling#function-calling-models). ^[function-calling-on-databricks-databricks-on-aws.md]

## Using Function Calling

### Defining Functions

You provide functions via the `tools` parameter. Each tool definition includes `type: "function"` and a `function` object with `name`, `description`, and `parameters` (a JSON schema). ^[function-calling-on-databricks-databricks-on-aws.md]

### Controlling Function Invocation (`tool_choice`)

The default `tool_choice` is `"auto"`, letting the model decide whether and which functions to call. You can customize this behavior:

- `"required"`: The model always calls one or more functions (chooses which).
- `{"type": "function", "function": {"name": "my_function"}}`: The model calls only that specific function.
- `"none"`: Disable function calling; the model generates a user-facing message only. ^[function-calling-on-databricks-databricks-on-aws.md]

### Example (Single Turn)

The following example uses the OpenAI SDK to define a `get_current_weather` function and ask for the current temperature in Chicago:

```python
import os
import json
from openai import OpenAI

DATABRICKS_TOKEN = os.environ.get('YOUR_DATABRICKS_TOKEN')
DATABRICKS_BASE_URL = os.environ.get('YOUR_DATABRICKS_BASE_URL')

client = OpenAI(
    api_key=DATABRICKS_TOKEN,
    base_url=DATABRICKS_BASE_URL
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"]
                    }
                }
            }
        }
    }
]

messages = [{"role": "user", "content": "What is the current temperature of Chicago?"}]

response = client.chat.completions.create(
    model="databricks-meta-llama-3-3-70b-instruct",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)

print(json.dumps(response.choices[0].message.model_dump()['tool_calls'], indent=2))
```

The `tools` parameter also supports Computer Use (beta) for Claude models. ^[function-calling-on-databricks-databricks-on-aws.md]

## JSON Schema

Foundation Model APIs support a subset of the JSON Schema specification to promote higher quality generation. The following are **not** supported:

- `pattern` (regular expressions)
- Complex nesting/composition: `anyOf`, `oneOf`, `allOf`, `prefixItems`, `$ref`
- Lists of types except when one is a valid type and the other is `"null"` (e.g., `["string", "null"]`)
- `maxProperties`, `minProperties`, `maxLength` are not enforced (no length/size constraints for objects/arrays).

Additional limitations:
- Maximum 16 keys in the JSON schema.
- Heavily nested schemas degrade generation quality; flattening the schema is recommended. ^[function-calling-on-databricks-databricks-on-aws.md]

## Token Usage

Function calling uses prompt injection and other techniques to improve tool call quality, which increases input and output token consumption. The more tools you define, the more input tokens are consumed, affecting billing. ^[function-calling-on-databricks-databricks-on-aws.md]

## Limitations (Public Preview)

- **Multi-turn function calling**: Databricks recommends using supported Claude models for multi-turn workflows. For Llama 4 Maverick, multi-turn is supported but under development.
- **Parallel function calling** is not supported.
- Maximum of **32 functions** can be defined in `tools`.
- Provisioned throughput support for function calling is only available on **new endpoints**; previously created endpoints cannot be updated.
- For Google Gemini endpoints, the `id` field in `function_call` and `function_response` is not supported. ^[function-calling-on-databricks-databricks-on-aws.md]

## Notebook Example

A detailed notebook example is available in the Databricks documentation:

[Function calling example notebook](https://docs.databricks.com/aws/en/machine-learning/model-serving/function-calling#notebook-example) ^[function-calling-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Tool Choice](/concepts/tool-choice-parameter.md) — How to control function invocation
- [Structured Outputs](/concepts/structured-outputs-in-foundation-model-apis.md) — Alternative for batch/unstructured-to-structured tasks
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Model serving feature
- [External Models](/concepts/external-models.md) — Serving models from providers other than Databricks
- JSON Schema — Definition format for function parameters
- Computer Use (beta) — Supported for Claude models

## Sources

- function-calling-on-databricks-databricks-on-aws.md

# Citations

1. [function-calling-on-databricks-databricks-on-aws.md](/references/function-calling-on-databricks-databricks-on-aws-52bb813f.md)
