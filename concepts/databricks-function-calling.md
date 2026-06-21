---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aac4d0ed387d6566476aa5f31764d9544d15eeacdf2b55a6b00c39448aa41649
  pageDirectory: concepts
  sources:
    - function-calling-on-databricks-databricks-on-aws.md
    - use-foundation-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-function-calling
    - DFC
  citations:
    - file: function-calling-on-databricks-databricks-on-aws.md
    - file: use-foundation-models-databricks-on-aws.md
title: Databricks Function Calling
description: An OpenAI-compatible mechanism on Databricks that lets LLMs generate structured JSON function-call outputs based on user-defined tool schemas, without the model executing the functions itself.
tags:
  - function-calling
  - llm
  - databricks
  - structured-outputs
timestamp: "2026-06-19T18:56:13.114Z"
---

# Databricks Function Calling

**Databricks Function Calling** is an OpenAI-compatible feature available during model serving that enables LLMs to generate structured JSON outputs based on user-defined function schemas. Instead of the model executing functions directly, it returns a JSON object with the function name and arguments that your application can use to call those functions in code. ^[function-calling-on-databricks-databricks-on-aws.md]

## Overview

Function calling gives developers a way to control LLM output more reliably by describing functions—including their parameters and descriptions—in the API call using a JSON schema. The model analyzes the user's query and decides whether to call one of the defined functions. If it does, the response contains a JSON object structured according to your custom schema. ^[function-calling-on-databricks-databricks-on-aws.md]

The basic sequence of steps is:

1. Call the model with a user query and a set of functions defined in the `tools` parameter. ^[function-calling-on-databricks-databricks-on-aws.md]
2. The model decides whether to call any functions. If it does, the content is a JSON object of strings that adheres to your custom schema. ^[function-calling-on-databricks-databricks-on-aws.md]
3. Parse the JSON strings in your code and call your function with the provided arguments. ^[function-calling-on-databricks-databricks-on-aws.md]
4. Call the model again, appending the structured response as a new message. The model then summarizes the results and sends that summary to the user. ^[function-calling-on-databricks-databricks-on-aws.md]

## When to Use Function Calling

Common use cases include:

- **Creating assistants that answer questions by calling other APIs.** For example, defining functions like `send_email(to: string, body: string)` or `current_weather(location: string, unit: 'celsius' | 'fahrenheit')`. ^[function-calling-on-databricks-databricks-on-aws.md]
- **Defining API calls based on natural language.** For instance, taking the statement "Who are my top customers?" and turning it into an API call `get_customers(min_revenue: int, created_before: string, limit: int)`. ^[function-calling-on-databricks-databricks-on-aws.md]

For batch inference or data processing tasks (like converting unstructured data into structured data), Databricks recommends using [structured outputs](/concepts/structured-outputs-in-foundation-model-apis.md) instead. ^[function-calling-on-databricks-databricks-on-aws.md]

## Availability

Function calling is only available during model serving as part of [Foundation Model APIs](/concepts/foundation-model-apis.md) and serving endpoints that serve [External Models](/concepts/external-models.md). ^[function-calling-on-databricks-databricks-on-aws.md, use-foundation-models-databricks-on-aws.md]

## Using Function Calling

### Tool Choice

The default behavior for `tool_choice` is `"auto"`, which lets the model decide which functions to call and whether to call them. You can customize this behavior: ^[function-calling-on-databricks-databricks-on-aws.md]

- Set `tool_choice: "required"` to force the model to always call one or more functions (the model selects which ones).
- Set `tool_choice: {"type": "function", "function": {"name": "my_function"}}` to force the model to call only a specific function.
- Set `tool_choice: "none"` to disable function calling and have the model generate only a user-facing message.

### Example

The following example uses the OpenAI SDK to call a weather function:

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

^[function-calling-on-databricks-databricks-on-aws.md]

## JSON Schema Support

Foundation Model APIs broadly support function definitions accepted by OpenAI. However, using a simpler JSON schema for function definitions results in higher quality JSON generation. ^[function-calling-on-databricks-databricks-on-aws.md]

### Unsupported Schema Keys

The following JSON schema features are **not** supported in function call definitions: ^[function-calling-on-databricks-databricks-on-aws.md]

- Regular expressions using `pattern`.
- Complex nested or schema composition using `anyOf`, `oneOf`, `allOf`, `prefixItems`, or `$ref`.
- Lists of types, except for the special case of `[type, "null"]` where one type is a valid JSON type and the other is `"null"`.

### Other Limitations

- Maximum number of keys specified in the JSON schema: **16**. ^[function-calling-on-databricks-databricks-on-aws.md]
- Foundation Model APIs do not enforce length or size constraints for objects and arrays (including `maxProperties`, `minProperties`, and `maxLength`). ^[function-calling-on-databricks-databricks-on-aws.md]
- Heavily nested JSON schemas result in lower quality generation. Flattening the schema is recommended. ^[function-calling-on-databricks-databricks-on-aws.md]

## Token Usage

Prompt injection and other techniques are used to enhance the quality of tool calls. This impacts the number of input and output tokens consumed by the model, which has billing implications. The more tools you use, the more your input tokens increase. ^[function-calling-on-databricks-databricks-on-aws.md]

## Limitations (Public Preview)

- **Multi-turn function calling:** Databricks recommends supported Claude models for multi-turn scenarios. For Llama 4 Maverick, multi-turn support is under development. ^[function-calling-on-databricks-databricks-on-aws.md]
- **Parallel function calling** is not supported. ^[function-calling-on-databricks-databricks-on-aws.md]
- Maximum number of functions in `tools`: **32**. ^[function-calling-on-databricks-databricks-on-aws.md]
- For provisioned throughput, function calling is only supported on **new** endpoints (cannot be added to previously created endpoints). ^[function-calling-on-databricks-databricks-on-aws.md]
- For Google Gemini endpoints, the `id` field on `function_call` and `function_response` is not supported. ^[function-calling-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The service that hosts and serves foundation models on Databricks
- [Structured Outputs](/concepts/structured-outputs-in-foundation-model-apis.md) — Alternative for batch inference and data processing tasks
- [External Models](/concepts/external-models.md) — Foundation models hosted outside of Databricks
- [Model Serving](/concepts/model-serving.md) — The infrastructure for serving models
- [Chat Completions API](/concepts/chat-completions-api.md) — The API used for querying foundation models

## Sources

- function-calling-on-databricks-databricks-on-aws.md
- use-foundation-models-databricks-on-aws.md

# Citations

1. [function-calling-on-databricks-databricks-on-aws.md](/references/function-calling-on-databricks-databricks-on-aws-52bb813f.md)
2. [use-foundation-models-databricks-on-aws.md](/references/use-foundation-models-databricks-on-aws-8c2af434.md)
