---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c93c69cfbbe12fffcf8d1bb4de22ad74d790b6118307c8cb8e81e8e93d0209cb
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - conversationsimulator-api
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: ConversationSimulator API
description: The MLflow class (mlflow.genai.simulators.ConversationSimulator) that orchestrates multi-turn conversation simulation, accepting test cases and configuration parameters like max_turns, temperature, and user_model.
tags:
  - mlflow
  - api
  - testing
  - conversational-ai
timestamp: "2026-06-19T14:25:10.040Z"
---

# ConversationSimulator API

The **ConversationSimulator API** is an experimental MLflow GenAI feature that enables programmatic generation of synthetic multi-turn conversations for testing conversational AI agents. Instead of manually creating test conversations or waiting for production data, you define test scenarios and let MLflow automatically simulate realistic user interactions. ^[conversation-simulation-databricks-on-aws.md]

## Overview

Conversation simulation addresses several key challenges in testing conversational agents. It enables systematic evaluation by letting teams test different agent versions with consistent goals and personas. It supports red-teaming by stress-testing agents with diverse user behaviors at scale. It also enables rapid iteration by generating new test conversations instantly when requirements change. ^[conversation-simulation-databricks-on-aws.md]

## Prerequisites

To use the ConversationSimulator API, you must install MLflow 3.10.0 or later:

```bash
pip install --upgrade 'mlflow[databricks]>=3.10'
```

^[conversation-simulation-databricks-on-aws.md]

## Workflow

The typical workflow consists of four steps:

1. **Define test cases** or extract them from existing conversations – specify goals, personas, and context for each simulated scenario.
2. **Create a simulator** – initialize `ConversationSimulator` with your test cases and configuration.
3. **Define your agent** – implement your agent in a function that accepts conversation history.
4. **Run evaluation** – pass the simulator to `mlflow.genai.evaluate()` with your scorers.

^[conversation-simulation-databricks-on-aws.md]

## Defining Test Cases

Each test case represents a conversation scenario and supports three optional fields. The **goal** describes what the simulated user wants to achieve. It should be specific enough to guide the conversation but open-ended enough to allow natural dialogue. Good goals describe the expected outcome so the simulator knows when the user’s intent has been accomplished. The **persona** shapes how the simulated user communicates; if not specified, a default helpful user persona is used. The **context** field passes additional parameters (such as user identifiers or session state) to your predict function. ^[conversation-simulation-databricks-on-aws.md]

### Example Test Cases

```python
# Good goals – specific, actionable, describe expected outcomes
{"goal": "Successfully configure MLflow tracking for a distributed training job"}
{"goal": "Identify and fix why model artifacts aren't being logged"}

# With persona
{
    "goal": "Reduce model serving latency below 100ms",
    "persona": "You are a senior ML engineer who asks precise technical questions"
}

# With context
{
    "goal": "Get personalized model recommendations",
    "context": {
        "user_id": "enterprise_user_42",
        "subscription_tier": "premium"
    }
}
```

Test cases can be provided as a list of dictionaries or a Pandas DataFrame:

```python
from mlflow.genai.simulators import ConversationSimulator

test_cases = [
    {"goal": "Successfully configure experiment tracking"},
    {"goal": "Debug a deployment error", "persona": "Senior engineer"},
    {"goal": "Set up a CI/CD pipeline for ML", "context": {"team": "platform"}},
]

simulator = ConversationSimulator(test_cases=test_cases)
```

## Generating Test Cases from Existing Conversations

You can generate test cases from existing conversation sessions using `generate_test_cases`. This is useful for creating test cases that reflect real user behavior from production conversations: ^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.simulators import generate_test_cases, ConversationSimulator

sessions = mlflow.search_sessions(
    locations=["<experiment-id>"],
    max_results=50,
)

test_cases = generate_test_cases(sessions)
simulator = ConversationSimulator(test_cases=test_cases)
```

## Agent Function Interface

Your agent function receives the conversation history and returns a response. Two parameter names are supported: `input` and `messages`. Both receive the conversation history as a list of message dicts in Chat Completions format. ^[conversation-simulation-databricks-on-aws.md]

```python
def predict_fn(input: list[dict], **kwargs) -> str:
    """
    Args:
        input: Conversation history as a list of message dicts.
               Each message has "role" ("user" or "assistant") and "content".
        **kwargs: Additional arguments including:
            - mlflow_session_id: Unique ID for this conversation session
            - Any fields from your test case's "context"
    Returns:
        The assistant's response as a string.
    """
```

The `**kwargs` parameter receives any fields from your test case’s `context` dictionary, which allows passing user identifiers, session state, configuration, or metadata your agent needs. ^[conversation-simulation-databricks-on-aws.md]

## Configuration Options

### ConversationSimulator Parameters

The `ConversationSimulator` accepts the following parameters:

- `test_cases`: Your test scenarios (list of dicts, DataFrame, or [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md))
- `max_turns`: Maximum number of conversation turns before stopping (default: system-defined)
- `user_model`: The LLM used to generate realistic user messages (default is system-defined)
- `temperature`: Controls randomness in the user simulation LLM

### Model Selection

The simulator uses an LLM to generate realistic user messages. You can specify a different model using the `user_model` parameter: ^[conversation-simulation-databricks-on-aws.md]

```python
simulator = ConversationSimulator(
    test_cases=test_cases,
    user_model="anthropic:/claude-sonnet-4-20250514",
    temperature=0.7,
)
```

Supported model formats follow the pattern `"<provider>:/<model>"`. ^[conversation-simulation-databricks-on-aws.md]

LLM-based conversation simulation may use third-party services to simulate user interactions, including Azure OpenAI operated by Microsoft. For European Union (EU) workspaces, conversation simulation uses models hosted in the EU. All other regions use models hosted in the US. Disabling Partner-powered AI features prevents conversation simulation from calling partner-powered models; you can still use conversation simulation by providing your own model. ^[conversation-simulation-databricks-on-aws.md]

## Conversation Stopping

Conversations stop when any of the following conditions are met: ^[conversation-simulation-databricks-on-aws.md]

- **Max turns reached**: The `max_turns` limit is hit
- **Goal achieved**: The simulator detects the user’s goal has been accomplished

## Running Evaluation

Pass the simulator to `mlflow.genai.evaluate()` with your agent function and scorers:

```python
results = mlflow.genai.evaluate(
    data=simulator,
    predict_fn=predict_fn,
    scorers=[
        ConversationCompleteness(),  # Multi-turn scorer
        Safety(),  # Single-turn scorer (applied to each turn)
    ],
)
```

## Viewing Results

Simulated conversations appear in the [MLflow UI](/concepts/mlflow.md) with special metadata: ^[conversation-simulation-databricks-on-aws.md]

- **Session ID**: Each conversation has a unique session ID prefixed with `sim-`
- **Simulation metadata**: Goal, persona, and turn number are stored on each trace

Navigate to the **Sessions** tab in your experiment to view conversations grouped by session. Select a session to see individual turns and their assessments. ^[conversation-simulation-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The framework for evaluating and monitoring generative AI applications
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – Persisting test cases for reproducible testing
- [Multi-turn Scorers](/concepts/multi-turn-scorers-in-mlflow.md) – Scorers designed for evaluating conversation quality
- [Conversation Evaluation](/concepts/conversation-evaluation.md) – Static evaluation of pre-existing conversations
- [Predefined Scorers](/concepts/mlflow-genai-predefined-scorers.md) – Built-in scorers for conversation completeness, safety, and more

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
