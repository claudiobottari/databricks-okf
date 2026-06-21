---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d65da7f914329a642826659d9b8968e2933898fa9d0681d8afc51806c938890b
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - agent-function-interface
    - AFI
    - Agent Function
    - agent function
    - agent-function-interface-for-mlflow-evaluation
    - AFIFME
    - agent-function-interface-for-simulation
    - AFIFS
  citations:
    - file: conversation-simulation-databricks-on-aws.md
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Agent Function Interface
description: The predict_fn contract for conversational agents being evaluated, accepting conversation history as a list of message dicts and returning a string response.
tags:
  - mlflow
  - API
  - agents
timestamp: "2026-06-18T14:44:08.448Z"
---

# Agent Function Interface

The **Agent Function Interface** defines the contract that a conversational AI agent must implement when used with [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) tools such as [ConversationSimulator](/concepts/conversationsimulator.md), [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md), or [Production Monitoring](/concepts/production-monitoring.md) with [Code-based Scorers](/concepts/code-based-scorers.md). It specifies how conversation history is passed to the agent and what the agent must return. ^[conversation-simulation-databricks-on-aws.md, code-based-scorer-reference-databricks-on-aws.md]

## Function Signature

The agent is defined as a Python function that accepts conversation history and returns a response string. Two parameter names are supported for receiving the conversation: ^[conversation-simulation-databricks-on-aws.md]

- **`input`** — Conversation history as a list of message dicts in the Chat Completions response format.
- **`messages`** — Equivalent alternative parameter name in the Chat Completions request format.

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

## Parameters

### `input` (or `messages`)

A list of message dictionaries representing the full conversation history up to the current turn. Each dictionary contains: ^[conversation-simulation-databricks-on-aws.md]

- **`role`**: Either `"user"` or `"assistant"`, indicating who sent the message.
- **`content`**: The text content of the message.

### `**kwargs`

Additional keyword arguments passed to the agent function. These include: ^[conversation-simulation-databricks-on-aws.md]

- **`mlflow_session_id`**: A unique identifier for the current conversation session, automatically assigned by MLflow. During simulation, session IDs are prefixed with `sim-`.
- **Context fields**: Any fields from the test case's `context` dictionary, such as `user_id`, `subscription_tier`, or custom metadata.

## Return Value

The function must return the assistant's response as a string. ^[conversation-simulation-databricks-on-aws.md]

```python
return response.choices[0].message.content
```

## Usage with ConversationSimulator

When used with [ConversationSimulator](/concepts/conversationsimulator.md), the agent function receives the conversation history that has accumulated so far and must append its response to the ongoing dialogue. The simulator handles generating user messages between agent responses. ^[conversation-simulation-databricks-on-aws.md]

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

### Passing Context from Test Cases

When test cases include a `context` field, those values are passed to the agent function via `**kwargs`. This allows agents to personalize responses based on user identity, subscription tier, or other metadata: ^[conversation-simulation-databricks-on-aws.md]

```python
def predict_fn(input: list[dict], **kwargs):
    user_id = kwargs.get("user_id")  # From test case context
    # ... agent logic using user_id ...
    return response
```

## Stateful Agents

Agents that maintain internal state across turns can use the `mlflow_session_id` from `kwargs` to track conversation state in an external store. The agent function itself should remain stateless — all necessary context must be derivable from the conversation history and keyword arguments. ^[conversation-simulation-databricks-on-aws.md]

## Usage with Evaluation

The agent function is passed as the `predict_fn` parameter to `mlflow.genai.evaluate()`. MLflow calls this function for each evaluation data point, passing the conversation history and any associated context. ^[conversation-simulation-databricks-on-aws.md]

```python
results = mlflow.genai.evaluate(
    data=simulator,
    predict_fn=predict_fn,
    scorers=[...],
)
```

## Best Practices

- **Handle both `input` and `messages` parameters**: Your function signature should accept either name to maximize compatibility with different MLflow APIs. ^[conversation-simulation-databricks-on-aws.md]
- **Keep the function stateless**: Use the conversation history and `kwargs` as the sole sources of state. External state management (e.g., a database) should be keyed by `mlflow_session_id`. ^[conversation-simulation-databricks-on-aws.md]
- **Return a plain string**: The interface expects a string response, not a structured object. Format any structured data (e.g., JSON, markdown) as string content. ^[conversation-simulation-databricks-on-aws.md]

## Related Concepts

- [ConversationSimulator](/concepts/conversationsimulator.md) — Generates synthetic multi-turn conversations that call this agent interface
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation framework that invokes the agent function
- [Code-based Scorers](/concepts/code-based-scorers.md) — Custom evaluation functions that can access the same runtime environment
- [Accessing Databricks secrets in scorers](/concepts/accessing-secrets-in-scorers.md) — How to securely access credentials within the evaluation runtime
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for storing evaluation results

## Sources

- conversation-simulation-databricks-on-aws.md
- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
2. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
