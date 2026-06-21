---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f1989c53e308757babb7d36011b46c1df313dac49feb81fa3c673fc091c86560
  pageDirectory: concepts
  sources:
    - function-calling-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-function-calling-workflow
    - DFCW
  citations:
    - file: function-calling-on-databricks-databricks-on-aws.md
title: Databricks Function Calling Workflow
description: "The four-step sequence for using function calling on Databricks: submit query with tools, model returns JSON arguments, parse and execute function, append results for final summary."
tags:
  - databricks
  - function-calling
  - workflow
timestamp: "2026-06-18T12:27:21.141Z"
---

---
title: Databricks Function Calling Workflow
summary: An OpenAI-compatible workflow that enables LLMs to generate structured JSON output for function invocation, following a call–respond–summarize pattern during model serving.
source: function-calling-on-databricks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:08:33.206Z"
updatedAt: "2026-06-18T11:08:33.206Z"
tags:
  - databricks
  - function-calling
  - llm
  - generative-ai
aliases:
  - function-calling-on-databricks
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks Function Calling Workflow

**Databricks Function Calling Workflow** is an OpenAI-compatible mechanism that allows large language models (LLMs) to generate structured JSON output representing function invocations. The LLM itself does not execute the functions — instead, it produces a JSON object that your application code can parse and use to call the corresponding functions. The workflow is available only during model serving via [Foundation Model APIs](/concepts/foundation-model-apis.md) and serving endpoints that serve [External Models](/concepts/external-models.md). ^[function-calling-on-databricks-databricks-on-aws.md]

## How It Works

The basic sequence of steps in the function calling workflow is as follows: ^[function-calling-on-databricks-databricks-on-aws.md]

1. **Call the model** with the user's query and a set of function definitions provided in the `tools` parameter.
2. **The model decides** whether to call any of the defined functions. If a function is called, the response content is a JSON object of strings that conforms to your custom schema.
3. **Parse and execute** the JSON in your code, calling your function with the provided arguments if they exist.
4. **Call the model again** by appending the structured response as a new message. The model then summarizes the results and sends that summary to the user.

## When to Use Function Calling

Typical use cases include: ^[function-calling-on-databricks-databricks-on-aws.md]

- **Assistants** that answer questions by calling external APIs, for example defining functions like `send_email(to: string, body: string)` or `current_weather(location: string, unit: 'celsius' | 'fahrenheit')`.
- **Natural language to API** workflows, where a statement like "Who are my top customers?" generates an API call to `get_customers(min_revenue: int, created_before: string, limit: int)`.

For batch inference or data processing tasks that convert unstructured data into structured data, Databricks recommends using [structured outputs](/concepts/structured-outputs-in-foundation-model-apis.md) instead. ^[function-calling-on-databricks-databricks-on-aws.md]

## Supported Models

Function calling is supported on a specific set of models available through Foundation Model APIs and external model serving endpoints. See [Foundation Model APIs](/concepts/foundation-model-apis.md) for region availability of pay-per-token models. See [External Models](/concepts/external-models.md) for region availability of externally hosted models. ^[function-calling-on-databricks-databricks-on-aws.md]

> **Note:** Meta-Llama-3.1-405B-Instruct is being retired. See [Retired Models Policy](/concepts/partner-model-retirement-policy.md) for migration guidance.

## Using Function Calling

To use function calling, provide two key elements in your API request: ^[function-calling-on-databricks-databricks-on-aws.md]

- `parameters` — A JSON schema describing the function's expected arguments.
- `description` — A natural language explanation of what the function does.

### Controlling Function Choice

The default behavior for `tool_choice` is `"auto"`, which lets the model decide which functions to call and whether to call them. You can customize this behavior: ^[function-calling-on-databricks-databricks-on-aws.md]

| `tool_choice` Value | Behavior |
|---------------------|----------|
| `"auto"` | Model decides whether and which function to call (default) |
| `"required"` | Model always calls one or more functions, choosing which |
| `{"type": "function", "function": {"name": "my_function"}}` | Model calls only the specified function |
| `"none"` | Disables function calling; model generates a user-facing message only |

### Example: Single Turn Function Call

The following example uses the OpenAI SDK to request the current weather in Chicago: ^[function-calling-on-databricks-databricks-on-aws.md]

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

> **Note:** During Public Preview, function calling on Databricks is optimized for single turn function calling. Multi-turn function calling is supported for Claude models and is under development for Llama 4 Maverick. ^[function-calling-on-databricks-databricks-on-aws.md]

The `tools` parameter also supports Computer Use (beta) for Claude models. ^[function-calling-on-databricks-databricks-on-aws.md]

### JSON Schema Support

Foundation Model APIs support a subset of the [JSON Schema specification](/concepts/json-schema-subset-for-function-calling.md) to promote higher quality function call generation. The following are not supported: ^[function-calling-on-databricks-databricks-on-aws.md]

- Regular expressions using `pattern`.
- Complex schema composition using `anyOf`, `oneOf`, `allOf`, `prefixItems`, or `$ref`.
- Lists of types, except for the special case of `[type, "null"]` where one type is a valid JSON type and the other is `"null"`.

Additional limitations: ^[function-calling-on-databricks-databricks-on-aws.md]

- Maximum of 16 keys in the JSON schema.
- No enforcement of length or size constraints (`maxProperties`, `minProperties`, `maxLength`).
- Heavily nested JSON schemas produce lower quality generation. Flattening the schema is recommended.

## Token Usage

Prompt injection and other techniques are used to enhance the quality of tool calls, which increases the number of input and output tokens consumed by the model. Using more tools further increases input tokens and affects billing. ^[function-calling-on-databricks-databricks-on-aws.md]

## Limitations (Public Preview)

- **Parallel function calling** is not supported. ^[function-calling-on-databricks-databricks-on-aws.md]
- Maximum of **32 functions** can be defined in the `tools` parameter. ^[function-calling-on-databricks-databricks-on-aws.md]
- For [Provisioned Throughput](/concepts/provisioned-throughput.md) support, function calling is only available on **new endpoints** — you cannot add it to previously created endpoints. ^[function-calling-on-databricks-databricks-on-aws.md]
- For Google Gemini endpoints, the `id` field on `function_call` and `function_response` is not supported. ^[function-calling-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The serving layer that provides function calling
- [External Models](/concepts/external-models.md) — Serving externally hosted models with function calling
- [Structured Outputs](/concepts/structured-outputs-in-foundation-model-apis.md) — Recommended for batch inference and data processing
- [Chat Completions API](/concepts/chat-completions-api.md) — The API endpoint used for function calling
- JSON Schema — The schema format used to define function parameters
- Claude Models — Models that support multi-turn function calling
- [Retired Models Policy](/concepts/partner-model-retirement-policy.md) — Migration guidance for deprecated models

## Sources

- function-calling-on-databricks-databricks-on-aws.md

# Citations

1. [function-calling-on-databricks-databricks-on-aws.md](/references/function-calling-on-databricks-databricks-on-aws-52bb813f.md)
