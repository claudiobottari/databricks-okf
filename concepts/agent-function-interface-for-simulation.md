---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ec01e743e92280a78a96af51e99afeb376e65a12352ff1aa5badc0bd02fdf2f9
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - agent-function-interface-for-simulation
    - AFIFS
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: Agent Function Interface for Simulation
description: The predict_fn interface that conversational AI agents must implement to participate in simulation, accepting conversation history as a list of message dicts (supports 'input' or 'messages' parameter names) and returning a string response.
tags:
  - mlflow
  - api
  - conversational-ai
timestamp: "2026-06-19T14:25:23.109Z"
---

# Agent Function Interface for Simulation

The **Agent Function Interface for Simulation** defines the contract that a conversational AI agent must satisfy when used with [Conversation Simulation](/concepts/conversation-simulation.md) in [MLflow GenAI](/concepts/mlflow-3-for-genai.md). It specifies the function signature, expected parameter names, return type, and additional keyword arguments available for passing context and session metadata.

## Function Signature

The agent function receives the conversation history and returns a response string. Two parameter names are supported for the conversation history: `input` and `messages`. The function can accept additional keyword arguments (`**kwargs`). ^[conversation-simulation-databricks-on-aws.md]

```python
def predict_fn(input: list[dict], **kwargs) -> str:
    """
    Args:
        input: Conversation history as a list of message dicts.
               Each message has "role" ("user" or "assistant") and "content".
               Alternatively, use "messages" as the parameter name.
        **kwargs: Additional arguments including:
            - mlflow_session_id: Unique ID for this conversation session
            - Any fields from your test case's "context"
    Returns:
        The assistant's response as a string.
    """
```

^[conversation-simulation-databricks-on-aws.md]

## Parameter Details

### `input` (or `messages`)

The conversation history is provided as a list of dictionaries, each containing at minimum `"role"` and `"content"` keys.

- `input` uses the Chat Completions **response** format (for the `messages` parameter of the OpenAI API).
- `messages` is an equivalent alternative parameter name using the Chat Completions **request** format.
- Either name can be used interchangeably. The simulation passes the history in both forms, so the agent can choose whichever signature is more convenient. ^[conversation-simulation-databricks-on-aws.md]

### `**kwargs`

Additional keyword arguments passed to the agent function include:

- **`mlflow_session_id`**: A unique identifier for the current conversation session, prefixed with `sim-` for simulated conversations. ^[conversation-simulation-databricks-on-aws.md]
- **Context fields**: Any fields defined in the test case's `context` dictionary are passed as separate keyword arguments. For example, if a test case includes `"context": {"user_id": "beginner_123"}`, the agent function receives `user_id="beginner_123"`. ^[conversation-simulation-databricks-on-aws.md]

## Return Value

The function must return a **string** representing the assistant's response. This response is added to the conversation history as a message with `role: "assistant"`. ^[conversation-simulation-databricks-on-aws.md]

## Examples

### Basic Usage

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

^[conversation-simulation-databricks-on-aws.md]

### With Context

When test cases include a `context` dictionary, the field values are passed as keyword arguments:

```python
def predict_fn(input: list[dict], **kwargs):
    user_id = kwargs.get("user_id", "unknown")
    # Use user_id for personalization
    # ...
    return response
```

^[conversation-simulation-databricks-on-aws.md]

### Stateful Agent

For agents that maintain state across turns, the `mlflow_session_id` can be used to retrieve or store session state:

```python
def predict_fn(input: list[dict], **kwargs):
    session_id = kwargs.get("mlflow_session_id")
    # Retrieve session state from external store
    # ...
    return response
```

^[conversation-simulation-databricks-on-aws.md]

## Design Considerations

- The function should be **stateless** or use external storage for session state because multiple conversations may run concurrently.
- The conversation history grows with each turn; agents should handle increasing message list lengths appropriately.
- For agents that require additional configuration (e.g., system prompts), those should be set outside the predict function or passed via context.

## Related Concepts

- [Conversation Simulation](/concepts/conversation-simulation.md) — The framework that invokes this agent function.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The evaluation and monitoring toolkit.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) — How test cases are defined and persisted.
- Simulation Session — How simulated conversations are tracked in the MLflow UI.
- Conversation History Format — The structure of message dictionaries.

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
