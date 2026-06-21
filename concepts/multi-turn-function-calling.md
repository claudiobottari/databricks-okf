---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 346be77e4c6bdbb7c57b4586eef081a73931bf4fa23d5905246f6cdca85e6f33
  pageDirectory: concepts
  sources:
    - function-calling-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - multi-turn-function-calling
    - MFC
  citations:
    - file: function-calling-on-databricks-databricks-on-aws.md
title: Multi-turn Function Calling
description: Function calling across multiple conversational turns, recommended for Claude models on Databricks; Llama models currently optimized for single-turn only.
tags:
  - function-calling
  - multi-turn
  - llm
timestamp: "2026-06-18T12:27:48.962Z"
---

# Multi-turn Function Calling

**Multi-turn Function Calling** is a technique in which a large language model (LLM) participates in a conversational loop, making multiple function calls across several turns to accomplish a complex task. Unlike single-turn function calling — where the model makes one function call and returns the result — multi-turn calling allows the model to call an initial function, receive its structured response, then issue one or more additional function calls based on that response, iteratively refining its output.

## Overview

Multi-turn function calling is central to building agents that can chain together multiple API calls, maintain context across turns, and resolve ambiguous requests through follow-up questions. The model receives the full conversation history — including previous tool call arguments and tool responses — and uses that context to decide which function to call next and what arguments to supply. ^[function-calling-on-databricks-databricks-on-aws.md]

## When to Use Multi-Turn Function Calling

Use multi-turn function calling when a single function call is insufficient to answer the user's request. Common scenarios include:

- **Multi-step workflows** – e.g., first calling `search_flights(departure, destination, date)`, then calling `book_flight(flight_id, passenger_details)` with the result, then calling `send_confirmation_email(booking_reference)`.
- **Ambiguity resolution** – when the model asks for clarification (e.g., "Did you mean the 'Alliance' credit card or the 'Ally' bank?"), receives the answer, then proceeds with the correct function.
- **Data enrichment pipelines** – calling an initial API to get an identifier, then using that identifier in a subsequent function call to fetch detailed records.

## Multi-Turn vs. Single-Turn on Databricks

During the Public Preview of function calling on Databricks, the feature is **optimized for single-turn function calling**. Multi-turn function calling is supported but is under development, and Databricks recommends using specific models for the best multi-turn experience. ^[function-calling-on-databricks-databricks-on-aws.md]

### Supported Models for Multi-Turn

- For multi-turn function calling, Databricks **recommends** the [supported Claude models](https://docs.databricks.com/aws/en/machine-learning/model-serving/function-calling#function-calling-models). ^[function-calling-on-databricks-databricks-on-aws.md]
- If using **Llama 4 Maverick**, the current function calling solution is optimized for single-turn function calls. Multi-turn function calling is supported during preview but is under development. ^[function-calling-on-databricks-databricks-on-aws.md]

### Limitations

The following limitations apply for multi-turn function calling during Public Preview:

| Limitation | Detail |
|---|---|
| Parallel function calls | Not supported |
| Max functions in `tools` | 32 |
| `tool_choice` behavior | Default is `"auto"`; can be set to `"required"`, a specific function name, or `"none"` |

^[function-calling-on-databricks-databricks-on-aws.md]

## How Multi-Turn Function Calling Works

The fundamental pattern for multi-turn function calling is:

1. **First call**: Submit the user query and a set of function definitions in the `tools` parameter. The model returns a `tool_calls` object containing a JSON schema-compliant argument for one or more of the defined functions.
2. **Execute the function**: Your code parses the JSON, calls the actual API or backend function, and obtains a structured result.
3. **Append the result**: Add the function response to the messages array as a new `role: "tool"` message. This message contains the function's output.
4. **Second call**: Call the model again, this time with the conversation history that includes the original query, the first `tool_calls`, and the `tool` response. The model may issue another `tool_calls` or generate a final summary for the user.
5. **Repeat**: Continue the loop until the model signals it is done (by producing a `role: "assistant"` message with no `tool_calls`) or until a maximum turn limit is reached.

### Required Structure of Tool Responses

Each tool response message must follow this structure:

```json
{
  "role": "tool",
  "content": "The function output as a string",
  "tool_call_id": "call_Abc123..."
}
```

The `tool_call_id` must match the `id` field from the corresponding `tool_calls` object in the model's response. If the IDs do not match, the model may fail to associate the result with the correct function call. ^[function-calling-on-databricks-databricks-on-aws.md]

## Example: Multi-Turn with Ambiguity Resolution

The following example demonstrates a multi-turn scenario where the model first asks for clarification, then proceeds with the correct function call.

### Initial Call (First Turn)

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
      "name": "send_email",
      "description": "Send an email to a recipient",
      "parameters": {
        "type": "object",
        "properties": {
          "to": {
            "type": "string",
            "description": "Email address of the recipient"
          },
          "body": {
            "type": "string",
            "description": "Body of the email"
          }
        }
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "get_weather",
      "description": "Get the current weather for a location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string"
          }
        }
      }
    }
  }
]

messages = [
  {"role": "user", "content": "Please send the weather report to alice@example.com."}
]

response = client.chat.completions.create(
    model="databricks-meta-llama-3-3-70b-instruct",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)
```

### Model Response (First Turn)

The model may respond with a `tool_calls` object:

```json
[
  {
    "id": "call_xyz",
    "type": "function",
    "function": {
      "name": "send_email",
      "arguments": "{\"to\": \"alice@example.com\", \"body\": \"\"}"
    }
  }
]
```

Notice that the `body` argument is empty. The model has identified a required parameter but did not have enough context to fill it. This is a case where multi-turn is needed.

### Append Tool Result

```python
tool_result = "Weather report for today: Sunny, 72°F"
tool_call_id = "call_xyz"

messages.append({
  "role": "tool",
  "content": tool_result,
  "tool_call_id": tool_call_id
})
```

### Second Call

```python
response = client.chat.completions.create(
    model="databricks-meta-llama-3-3-70b-instruct",
    messages=messages,  # Now includes the tool result
    tools=tools,
    tool_choice="auto",
)
```

The model now has the weather data and can either stop (returning a summary) or make another call if needed.

## Best Practices for Multi-Turn Function Calling

- **Keep conversation history clean.** Only include messages that are relevant to the current turn. Avoid injecting historical tool results that are no longer applicable.
- **Use `tool_call_id` consistently.** Ensure every `role: "tool"` message has a `tool_call_id` that matches the `id` from the model's previous `tool_calls`.
- **Set a maximum turn limit.** Prevent infinite loops by configuring a max number of turns (e.g., 5 or 10) beyond which the agent stops and returns a fallback response.
- **Use `tool_choice: "auto"` for multi-turn by default.** Let the model decide when to stop. Only use `tool_choice: "required"` when you are certain every turn should produce a function call.
- **Monitor token usage.** Each tool definition and each turn of conversation consumes input tokens. The more tools you define and the more turns you take, the higher the token cost.

## Related Concepts

- Single-turn function calling
- [Tool calling](/concepts/llm-function-calling.md)
- [Structured outputs](/concepts/structured-outputs-in-foundation-model-apis.md)
- JSON schema validation
- [Foundation Model APIs](/concepts/foundation-model-apis.md)

## Sources

- function-calling-on-databricks-databricks-on-aws.md

# Citations

1. [function-calling-on-databricks-databricks-on-aws.md](/references/function-calling-on-databricks-databricks-on-aws-52bb813f.md)
