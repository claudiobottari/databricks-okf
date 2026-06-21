---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8f5b7eb363983b14b97bcb46b02ab45235e57cf904dec8ee27b5c58b5e72abb
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - agent-function-interface-for-simulated-conversations
    - AFIFSC
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: Agent Function Interface for Simulated Conversations
description: The predict_fn interface that receives conversation history and context (including mlflow_session_id and custom context fields) and returns assistant responses.
tags:
  - mlflow
  - API
  - conversational-ai
timestamp: "2026-06-19T17:52:00.283Z"
---

```markdown
---
title: Agent Function Interface for Simulated Conversations
summary: The interface that an agent function must implement to work with MLflow conversation simulation, accepting conversation history and returning a response.
sources:
  - conversation-simulation-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:15:09.839Z"
updatedAt: "2026-06-18T08:15:09.839Z"
tags:
  - mlflow
  - conversation-simulation
  - agent
  - interface
aliases:
  - agent-function-interface
  - predict_fn-interface
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Agent Function Interface for Simulated Conversations

## Overview

The **agent function interface** is the contract that your conversational agent must satisfy when used with [[MLflow]] conversation simulation. The function receives the conversation history (as a list of messages) and returns the agent’s response as a string. It is passed as the `predict_fn` argument to `mlflow.genai.evaluate()`. ^[conversation-simulation-databricks-on-aws.md]

## Function Signature

Two parameter names are supported for the conversation history: `input` and `messages`. At least one of these must be present in the function signature. ^[conversation-simulation-databricks-on-aws.md]

```python
def predict_fn(input: list[dict], **kwargs) -> str:
    ...
```

or equivalently:

```python
def predict_fn(messages: list[dict], **kwargs) -> str:
    ...
```

## Parameters

### `input` (or `messages`)
- **Type**: `list[dict]`
- **Description**: The conversation history as a list of message dictionaries. Each dictionary has a `"role"` field (either `"user"` or `"assistant"`) and a `"content"` field containing the message text. When using the `messages` parameter name, the format follows the Chat Completions request format. ^[conversation-simulation-databricks-on-aws.md]

### `**kwargs`
Additional keyword arguments that are passed to the function:
- **`mlflow_session_id`**: A unique identifier for the current conversation session.
- **Any fields from the test case’s `context`**: If a test case includes a `context` dictionary, its keys (e.g., `user_id`, `subscription_tier`) are forwarded as keyword arguments. ^[conversation-simulation-databricks-on-aws.md]

## Return Value

The function must return a **string** containing the assistant’s response. This response becomes the next assistant message in the conversation history. ^[conversation-simulation-databricks-on-aws.md]

## Examples

### Basic agent (using `input` parameter)

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

This example passes the conversation history directly to an OpenAI model and returns its response. ^[conversation-simulation-databricks-on-aws.md]

### Agent using context

Context fields from the test case are available in `kwargs`. For example, if a test case specifies `"context": {"user_id": "beginner_123"}`, then `user_id` is passed as a keyword argument and can be used to personalize the response. ^[conversation-simulation-databricks-on-aws.md]

### Stateful agent

For agents that need to maintain state across turns, the `mlflow_session_id` can be used as a key to store and retrieve session‑specific data. ^[conversation-simulation-databricks-on-aws.md]

## Usage with `mlflow.genai.evaluate`

The agent function is provided as the `predict_fn` argument when calling `mlflow.genai.evaluate()` together with a [[ConversationSimulator]] and one or more [[scorers]]. The simulator generates user messages, and the agent function supplies the assistant replies. ^[conversation-simulation-databricks-on-aws.md]

## Related Concepts

- [[ConversationSimulator]] – The component that generates synthetic user turns.
- [[MLflow]] – The platform under which conversation simulation runs.
- [[mlflow.genai.evaluate]] – The function that orchestrates the evaluation loop.
- [[Scorers]] – Metrics applied to each turn or the full conversation.
- [[Evaluation datasets]] – Persisting test cases for reproducible testing.

## Sources

- conversation-simulation-databricks-on-aws.md
```

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
