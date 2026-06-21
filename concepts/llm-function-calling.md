---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7bb055dd2223779cb0391613087523ace0ed45ac9d332b3dcbff3b9671aa5ce5
  pageDirectory: concepts
  sources:
    - function-calling-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-function-calling
    - LFC
    - Function Calling
    - Function calling
    - function calling
    - LLM Tool Calling
    - Tool Calling
    - Tool Calling (Function Calling)
    - Tool calling
    - tool calling
  citations:
    - file: function-calling-on-databricks-databricks-on-aws.md
title: LLM Function Calling
description: A technique that lets LLMs generate structured JSON output describing function arguments, enabling reliable integration with external APIs and code.
tags:
  - llm
  - function-calling
  - structured-output
timestamp: "2026-06-18T12:27:13.455Z"
---

# LLM Function Calling

**LLM Function Calling** is a technique that enables large language models to generate structured, machine-readable output by providing descriptions of functions in the API request. The model does not execute the functions; instead, it produces a JSON object containing the function name and arguments, which the calling application can use to invoke the actual function in code. This approach improves the reliability of structured responses compared to free-form text generation. ^[function-calling-on-databricks-databricks-on-aws.md]

On Databricks, function calling is OpenAI-compatible and is available only through model serving, as part of [Foundation Model APIs](/concepts/foundation-model-apis.md) and serving endpoints that serve [External Models](/concepts/external-models.md). ^[function-calling-on-databricks-databricks-on-aws.md]

## Basic Sequence

The typical workflow for function calling consists of the following steps: ^[function-calling-on-databricks-databricks-on-aws.md]

1. Call the model with the user query and a set of function definitions provided in the `tools` parameter. Each function is described by a name, description, and a JSON schema for its parameters.
2. The model decides whether to call one or more of the defined functions. If it does, the response contains a JSON object with strings that conform to the schema.
3. Parse the JSON in your application code and call the actual function with the provided arguments.
4. Append the function result as a new message and call the model again, allowing the model to summarize the results for the user.

## When to Use Function Calling

Common use cases for function calling include: ^[function-calling-on-databricks-databricks-on-aws.md]

- Creating assistants that answer questions by calling external APIs, for example `send_email(to: string, body: string)` or `current_weather(location: string, unit: 'celsius' | 'fahrenheit')`.
- Generating API calls from natural language, such as converting “Who are my top customers?” into a call to `get_customers(min_revenue: int, created_before: string, limit: int)`.

For batch inference or data processing tasks that convert unstructured data into structured data, [structured outputs](/concepts/structured-outputs-in-foundation-model-apis.md) are recommended instead of function calling. ^[function-calling-on-databricks-databricks-on-aws.md]

## Supported Models

The following models support function calling on Databricks. Availability depends on the model serving feature ([Foundation Model APIs](/concepts/foundation-model-apis.md) or [External Models](/concepts/external-models.md)) and region. ^[function-calling-on-databricks-databricks-on-aws.md]

| Model | Serving Feature |
|-------|-----------------|
| Meta-Llama-3.1-405B-Instruct | Foundation Model APIs |
| Meta-Llama-3.3-70B-Instruct | Foundation Model APIs |
| Meta-Llama-4 Maverick | Foundation Model APIs |
| Google Gemini 3 Pro | External models |
| Various Claude models | External models (multi-turn optimized) |

Note that some models have retirement dates. See Applicable model terms and Retired models policy for details. ^[function-calling-on-databricks-databricks-on-aws.md]

## How to Use Function Calling

To use function calling, provide the function `parameters` and a `description` in the `tools` parameter of the [Chat Completions API](/concepts/chat-completions-api.md). The `tool_choice` parameter controls the model's behavior: ^[function-calling-on-databricks-databricks-on-aws.md]

- `"auto"` (default): The model decides whether to call functions and which ones.
- `"required"`: The model always calls one or more functions, selecting which ones.
- `{"type": "function", "function": {"name": "my_function"}}`: The model calls only the specified function.
- `"none"`: Function calling is disabled; the model generates a plain text response.

The following example uses the [OpenAI SDK](/concepts/openai-api-compatibility-in-databricks.md) to call a weather function: ^[function-calling-on-databricks-databricks-on-aws.md]

```python
import os, json
from openai import OpenAI

client = OpenAI(
  api_key=os.environ.get('YOUR_DATABRICKS_TOKEN'),
  base_url=os.environ.get('YOUR_DATABRICKS_BASE_URL')
)

tools = [{
  "type": "function",
  "function": {
    "name": "get_current_weather",
    "description": "Get the current weather in a given location",
    "parameters": {
      "type": "object",
      "properties": {
        "location": { "type": "string", "description": "The city and state" },
        "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] }
      }
    }
  }
}]

messages = [{"role": "user", "content": "What is the current temperature of Chicago?"}]

response = client.chat.completions.create(
    model="databricks-meta-llama-3-3-70b-instruct",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

print(json.dumps(response.choices[0].message.model_dump()['tool_calls'], indent=2))
```

This parameter also supports Computer Use (beta) for Claude models. ^[function-calling-on-databricks-databricks-on-aws.md]

### JSON Schema Considerations

Foundation Model APIs support a simplified subset of the JSON schema specification. To achieve higher quality function call generation, avoid complex schemas. The following are not supported: ^[function-calling-on-databricks-databricks-on-aws.md]

- `pattern` (regular expressions)
- `anyOf`, `oneOf`, `allOf`, `prefixItems`, or `$ref`
- Lists of types except for the special case `[type, "null"]`

Additional limitations: ^[function-calling-on-databricks-databricks-on-aws.md]

- Maximum number of keys in the JSON schema is 16.
- Length or size constraints for objects and arrays (`maxProperties`, `minProperties`, `maxLength`) are not enforced.
- Heavily nested schemas result in lower quality generation. Flattening the schema is recommended.

## Token Usage

Function calling uses prompt injection and other techniques to improve tool call quality, which increases input and output token consumption. The more tools defined, the higher the input token count, leading to corresponding billing implications. ^[function-calling-on-databricks-databricks-on-aws.md]

## Limitations (Public Preview)

The following limitations apply during the public preview: ^[function-calling-on-databricks-databricks-on-aws.md]

- For multi-turn function calling, Claude models are recommended.
- Llama 4 Maverick is optimized for single-turn calls; multi-turn support is under development.
- Parallel function calling is not supported.
- Maximum of 32 functions in the `tools` parameter.
- Provisioned throughput support is available only on new endpoints; existing endpoints cannot be retrofitted.
- For Google Gemini endpoints, the `id` field on `function_call` and `function_response` is not supported.

## Notebook Example

A detailed notebook demonstrating function calling on Databricks is available in the Databricks documentation (refer to the "Function calling example notebook" in the source). ^[function-calling-on-databricks-databricks-on-aws.md]

## Sources

- function-calling-on-databricks-databricks-on-aws.md

# Citations

1. [function-calling-on-databricks-databricks-on-aws.md](/references/function-calling-on-databricks-databricks-on-aws-52bb813f.md)
