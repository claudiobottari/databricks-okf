---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c817b9b55c2bf268c30a5706052efede15e270cd06187f6ef6abd8ced3642ad3
  pageDirectory: concepts
  sources:
    - function-calling-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tool-choice-parameter
    - TCP
    - Tool Choice
  citations:
    - file: function-calling-on-databricks-databricks-on-aws.md
    - file: function-calling-on-databricks-databricks-on-aws.md
      start: 68
      end: 83
    - file: function-calling-on-databricks-databricks-on-aws.md
      start: 85
      end: 105
title: Tool Choice Parameter
description: A configuration option ('auto', 'required', 'none', or a specific function name) that controls whether and which functions an LLM will invoke during a chat completion.
tags:
  - function-calling
  - llm-configuration
  - api-parameters
timestamp: "2026-06-19T18:56:11.245Z"
---

```markdown
---
title: Tool Choice Parameter
summary: A configurable parameter ('auto', 'required', 'none', or a specific function name) that controls whether and which functions an LLM calls. Also supports Computer Use (beta) for Claude models.
sources:
  - function-calling-on-databricks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:27:01.826Z"
updatedAt: "2026-06-19T10:40:53.438Z"
tags:
  - configuration
  - function-calling
  - API
aliases:
  - tool-choice-parameter
  - TCP
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

## Tool Choice Parameter

The **Tool Choice Parameter** (specified as `tool_choice` in the API) controls whether and how a large language model (LLM) uses the functions defined in the `tools` parameter of a Chat Completions API call. It governs the model's behavior when deciding to generate a structured function call versus a plain user-facing message. ^[function-calling-on-databricks-databricks-on-aws.md]

### Values

The `tool_choice` parameter accepts the following values: ^[function-calling-on-databricks-databricks-on-aws.md:68-83]

| Value | Behavior |
|-------|----------|
| `"auto"` (default) | The model decides which functions to call and whether to call any function. |
| `"required"` | The model always calls one or more functions. The model selects which function or functions to call. |
| `{"type": "function", "function": {"name": "my_function"}}` | The model calls only the specific function named in the parameter. |
| `"none"` | Disables function calling entirely — the model only generates a user-facing message. |

The `tool_choice` parameter also supports [Computer Use (beta)](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) for Claude models. ^[function-calling-on-databricks-databricks-on-aws.md]

### Usage

The parameter is passed as part of the request to a model serving endpoint. In the OpenAI SDK, it appears as the `tool_choice` argument in `client.chat.completions.create()`. The following example demonstrates single‑turn function calling with `tool_choice="auto"`: ^[function-calling-on-databricks-databricks-on-aws.md:85-105]

```python
import os, json
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DATABRICKS_TOKEN'),
    base_url=os.environ.get('DATABRICKS_BASE_URL')
)

tools = [{
    "type": "function",
    "function": {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            }
        }
    }
}]

messages = [{"role": "user", "content": "What is the current temperature of Chicago?"}]

response = client.chat.completions.create(
    model="databricks-meta-llama-3-3-70b-instruct",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)
```

### Related Concepts

- [[Supported Models for Function Calling on Databricks|Function Calling on Databricks]] – The feature that enables LLMs to generate structured function call outputs.
- [[Foundation Model APIs]] – The serving infrastructure where function calling and the `tool_choice` parameter are available.
- [[Chat Completions API]] – The API endpoint that accepts the `tool_choice` parameter.
- [[Structured Outputs in Foundation Model APIs|Structured Outputs]] – An alternative for batch inference or data processing tasks.

### Sources

- function-calling-on-databricks-databricks-on-aws.md
```

# Citations

1. [function-calling-on-databricks-databricks-on-aws.md](/references/function-calling-on-databricks-databricks-on-aws-52bb813f.md)
2. [function-calling-on-databricks-databricks-on-aws.md:68-83](/references/function-calling-on-databricks-databricks-on-aws-52bb813f.md)
3. [function-calling-on-databricks-databricks-on-aws.md:85-105](/references/function-calling-on-databricks-databricks-on-aws-52bb813f.md)
