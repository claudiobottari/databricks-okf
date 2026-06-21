---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5aeb1294fd456380c07c89f1d0e4ade7fdaa5d8af289162e02a0a3350876064c
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - agent-function-interface-for-mlflow-evaluation
    - AFIFME
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: Agent Function Interface for MLflow Evaluation
description: The predict_fn contract that wraps a conversational agent for use with MLflow evaluation, accepting conversation history and returning responses.
tags:
  - mlflow
  - conversational-ai
  - api-design
timestamp: "2026-06-19T09:24:06.862Z"
---

Here is the wiki page for "Agent Function Interface for MLflow Evaluation".

---

## Agent Function Interface for MLflow Evaluation

The **Agent Function Interface** defines how your conversational AI agent communicates with [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md). When using [Conversation Simulation](/concepts/conversation-simulation.md) or other multi-turn evaluation workflows, your agent must implement a specific function signature so that MLflow can pass conversation history to it and receive a response. ^[conversation-simulation-databricks-on-aws.md]

## Function Signature

Your agent function receives the conversation history and returns a response. Two parameter names are supported:

- **`input`**: Conversation history as a list of message dicts (Chat Completions response format).
- **`messages`**: Equivalent alternative parameter name (Chat Completions request format). ^[conversation-simulation-databricks-on-aws.md]

### Python Signature

```python
def predict_fn(input: list[dict], **kwargs) -> str:
```

**Parameters:**

- `input` (or `messages`): A list of dictionaries representing the conversation history. Each message has a `"role"` (either `"user"` or `"assistant"`) and `"content"` (the text of the message). ^[conversation-simulation-databricks-on-aws.md]
- `**kwargs`: Additional keyword arguments passed to the function. These can include:
  - `mlflow_session_id`: A unique identifier for the conversation session.
  - Any fields specified in the test case's `"context"` field. ^[conversation-simulation-databricks-on-aws.md]

**Returns:**

- The function must return a string — the assistant's response for the current turn. ^[conversation-simulation-databricks-on-aws.md]

## Usage in Evaluation

When using [Conversation Simulator](/concepts/conversationsimulator.md) (or any MLflow evaluation that invokes the agent), you define your agent with this function signature. MLflow passes the conversation history (as a list of message dictionaries) and the `**kwargs` to your function for each turn of the conversation. ^[conversation-simulation-databricks-on-aws.md]

### Basic Example

```python
from openai import OpenAI

client = OpenAI()

def predict_fn(input: list[dict], **kwargs):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=input,
    )
    return response.choices[0].message.content
```

This example receives the conversation history as `input`, passes it to the OpenAI API as `messages`, and returns the assistant's response as a string. ^[conversation-simulation-databricks-on-aws.md]

### With Context Support

If your test case includes a `"context"` field, those values are passed to your function via `**kwargs`. For example:

```python
def predict_fn(input: list[dict], **kwargs):
    user_id = kwargs.get("user_id")
    # Use user_id for personalization or logging
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=input,
    )
    return response.choices[0].message.content
```

The `user_id` from the test case's `context` is available as a keyword argument. ^[conversation-simulation-databricks-on-aws.md]

## Best Practices

- **Use `input` or `messages`**: Parameter name is flexible, but use `input` for clarity with MLflow's documentation, or `messages` if your API expects the [Chat Completions](/concepts/chat-completions-api.md) request format. ^[conversation-simulation-databricks-on-aws.md]
- **Handle `**kwargs` gracefully**: Your function should accept and ignore additional keyword arguments if it doesn't need them. ^[conversation-simulation-databricks-on-aws.md]
- **Return a string**: The return value must be a string, not a dictionary or other object. ^[conversation-simulation-databricks-on-aws.md]

## Related Concepts

- [Conversation Simulator](/concepts/conversationsimulator.md) — The tool that uses this interface to generate multi-turn conversations.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation framework that invokes the agent function.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) — Test cases that provide context and inputs for the agent function.
- [Chat Completions](/concepts/chat-completions-api.md) — The format of the `messages` list expected by OpenAI-compatible APIs.

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
