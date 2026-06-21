---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 103f600d8aa22588cb6ed5965a23d3f7a55cb264f8f1a2f957019a87e4d17a79
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - conversation-simulation
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: Conversation Simulation
description: Generating synthetic multi-turn conversations programmatically for testing conversational AI agents using defined goals, personas, and context, without relying on manual test creation or production data.
tags:
  - mlflow
  - testing
  - generative-ai
  - conversational-ai
timestamp: "2026-06-19T14:26:32.803Z"
---

# Conversation Simulation

**Conversation Simulation** is a feature in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that generates synthetic multi-turn conversations by simulating user interactions with an agent. Unlike [evaluate-conversations|evaluating pre-generated conversations](/concepts/conversation-evaluation-multi-turn-evaluation.md) (which uses existing traced data), conversation simulation creates new dialogue sessions on the fly, enabling systematic testing of agent behavior under controlled conditions. ^[conversation-simulation-databricks-on-aws.md]

## Use Cases

Conversation simulation addresses several key challenges in conversational AI development: ^[conversation-simulation-databricks-on-aws.md]

- **Systematic evaluation**: Test different agent versions with consistent goals and personas.
- **Red-teaming**: Stress-test agents with diverse user behaviors at scale.
- **Rapid iteration**: Generate new test conversations instantly when requirements change.

## How It Works

Simulation is driven by the `ConversationSimulator` class. You define a list of `test_cases`, each containing a `goal` (the objective the simulated user tries to achieve) and optionally a `persona` (a description of the user's background or tone) and `context` (additional parameters passed to your agent function). The simulator runs these cases against your agent, producing full conversation traces. The `max_turns` parameter controls the maximum number of dialogue exchanges per scenario. ^[conversation-simulation-databricks-on-aws.md]

### Quick Start Example

```python
import mlflow
from mlflow.genai.simulators import ConversationSimulator
from mlflow.genai.scorers import ConversationCompleteness, Safety
from openai import OpenAI

client = OpenAI()

# 1. Define test cases with goals (required) and optional persona/context
test_cases = [
    {
        "goal": "Successfully configure experiment tracking",
    },
    {
        "goal": "Identify and fix a model deployment error",
        "persona": "You are a frustrated data scientist who has been stuck on this issue for hours",
    },
    {
        "goal": "Set up model versioning for a production pipeline",
        "persona": "You are a beginner who needs step-by-step guidance",
        "context": {
            "user_id": "beginner_123"
        },
    },
]

# 2. Create the simulator
simulator = ConversationSimulator(
    test_cases=test_cases,
    max_turns=5,
)

# 3. Define your agent function
def predict_fn(input: list[dict], **kwargs):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=input,
    )
    return response.choices[0].message.content

# 4. Run evaluation with conversation and single-turn scorers
results = mlflow.genai.evaluate(
    data=simulator,
    predict_fn=predict_fn,
    scorers=[
        ConversationCompleteness(),  # Multi-turn scorer
        Safety(),  # Single-turn scorer (applied to each turn)
    ],
)
```

^[conversation-simulation-databricks-on-aws.md]

## Defining Test Cases

Each test case represents a conversation scenario with three supported fields: ^[conversation-simulation-databricks-on-aws.md]

### Goal

The goal describes what the simulated user wants to achieve. It should be specific enough to guide the conversation but open-ended enough to allow natural dialogue. Good goals describe the expected outcome so the simulator knows when the user's intent has been accomplished: ^[conversation-simulation-databricks-on-aws.md]

```python
# Good goals - specific, actionable, and describe expected outcomes
{"goal": "Successfully configure MLflow tracking for a distributed training job"}
{"goal": "Understand when to use experiments vs. runs in MLflow"}
{"goal": "Identify and fix why model artifacts aren't being logged"}

# Less effective goals - too vague, no expected outcome
{"goal": "Learn about MLflow"}
{"goal": "Get help"}
```

### Persona

The persona shapes how the simulated user communicates. If not specified, a default helpful user persona is used: ^[conversation-simulation-databricks-on-aws.md]

```python
# Technical expert who asks detailed questions
{
    "goal": "Reduce model serving latency below 100ms",
    "persona": "You are a senior ML engineer who asks precise technical questions",
}

# Beginner who needs more guidance
{
    "goal": "Successfully set up experiment tracking",
    "persona": "You are new to MLflow and need step-by-step explanations",
}

# Frustrated user testing agent resilience
{
    "goal": "Fix a deployment blocking production",
    "persona": "You are impatient because this is blocking a release",
}
```

### Context

The context field passes additional parameters to your predict function. This is useful for passing user identifiers, providing session state or configuration, or including metadata your agent needs: ^[conversation-simulation-databricks-on-aws.md]

```python
{
    "goal": "Get personalized model recommendations",
    "context": {
        "user_id": "enterprise_user_42",
        "subscription_tier": "premium",
        "preferred_framework": "pytorch",
    },
}
```

## Agent Function Interface

Your agent function receives the conversation history and returns a response. Two parameter names are supported: `input` (conversation history as a list of message dicts in Chat Completions response format) and `messages` (equivalent alternative in Chat Completions request format): ^[conversation-simulation-databricks-on-aws.md]

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

## Generating Test Cases from Existing Conversations

You can generate test cases from existing conversation sessions using `generate_test_cases`. This is useful for creating test cases that reflect real user behavior from production conversations: ^[conversation-simulation-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.simulators import generate_test_cases, ConversationSimulator

# Get existing sessions from your experiments
sessions = mlflow.search_sessions(
    locations=["<experiment-id>"],
    max_results=50,
)

# Generate test cases by extracting goals and personas from sessions
test_cases = generate_test_cases(sessions)

# Use generated test cases with the simulator
simulator = ConversationSimulator(test_cases=test_cases)
```

## Configuration Options

### ConversationSimulator Parameters ^[conversation-simulation-databricks-on-aws.md]

| Parameter | Description |
|-----------|-------------|
| `test_cases` | A list of scenario dictionaries. Each can contain `goal` (required), `persona` (optional), and `context` (optional). |
| `max_turns` | Maximum number of user‑agent exchanges per simulation. |

### Model Selection

The simulator uses an LLM to generate realistic user messages. You can specify a different model using the `user_model` parameter: ^[conversation-simulation-databricks-on-aws.md]

```python
simulator = ConversationSimulator(
    test_cases=test_cases,
    user_model="anthropic:/claude-sonnet-4-20250514",
    temperature=0.7,  # Passed to the user simulation LLM
)
```

Supported model formats follow the pattern `"<provider>:/<model>"`. ^[conversation-simulation-databricks-on-aws.md]

### Conversation Stopping

Conversations stop when any of these conditions are met: ^[conversation-simulation-databricks-on-aws.md]

- **Max turns reached**: The `max_turns` limit is hit.
- **Goal achieved**: The simulator detects the user's goal has been accomplished.

## Integration with Evaluation

Simulated conversations integrate directly with [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md). After simulation, the generated traces are automatically scored by the supplied [LLM Judges](/concepts/llm-judges.md). This makes it possible to compare different agent configurations (e.g., system prompt changes, tool sets) by running the same simulator against each variant and comparing the judge ratings. ^[conversation-simulation-databricks-on-aws.md]

## Viewing Results

Simulated conversations appear in the MLflow UI with special metadata: ^[conversation-simulation-databricks-on-aws.md]

- **Session ID**: Each conversation has a unique session ID (prefixed with `sim-`).
- **Simulation metadata**: Goal, persona, and turn number are stored on each trace.

Navigate to the **Sessions** tab in your experiment to view conversations grouped by session. Select a session to see individual turns and their assessments. ^[conversation-simulation-databricks-on-aws.md]

## Tracking Test Cases as MLflow Dataset

For reproducible testing, persist your test cases as an [MLflow Evaluation Dataset](/concepts/evaluation-datasets.md): ^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.datasets import create_dataset, get_dataset

# Create and populate a dataset
dataset = create_dataset(name="conversation_test_cases")
dataset.merge_records(
    [
        {"inputs": {"goal": "Successfully configure experiment tracking"}},
        {"inputs": {"goal": "Debug a deployment error", "persona": "Senior engineer"}},
    ]
)

# Use the dataset with the simulator
dataset = get_dataset(name="conversation_test_cases")
simulator = ConversationSimulator(test_cases=dataset)
```

## Related Concepts

- [Evaluate Conversations](/concepts/multi-turn-conversation-judges.md) – The two approaches to conversation evaluation (pre‑generated vs. simulated).
- [Multi-turn Judges](/concepts/multi-turn-judges.md) – LLM‑based scorers that assess whole conversations (e.g., `ConversationCompleteness`, `UserFrustration`).
- [ConversationSimulator](/concepts/conversationsimulator.md) – The class that drives simulation; part of `mlflow.genai.simulators`.
- [LLM Judges](/concepts/llm-judges.md) – General concept of using language models to score outputs.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The `mlflow.genai.evaluate()` API used for both single‑turn and multi‑turn evaluation.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – Persisting test cases for reproducible testing.
- [Production Monitoring](/concepts/production-monitoring.md) – How multi‑turn judges can be deployed for continuous monitoring of live conversations.

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
