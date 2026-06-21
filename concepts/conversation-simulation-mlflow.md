---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf3ead1d837b820d660e7c5130ff509dbfe7af36fe61ca3eaf20ef5e711bbef5
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - conversation-simulation-mlflow
    - CS(
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: Conversation Simulation (MLflow)
description: A technique in MLflow for programmatically generating synthetic multi-turn conversations to test conversational AI agents without manual creation or production data.
tags:
  - mlflow
  - testing
  - evaluation
  - conversational-ai
timestamp: "2026-06-18T14:44:40.052Z"
---

# Conversation Simulation (MLflow)

**Conversation simulation** is a feature in MLflow that enables you to programmatically generate synthetic multi-turn conversations for testing conversational AI agents. Instead of manually crafting test conversations or waiting for production data, you define test scenarios—with goals, personas, and context—and let MLflow simulate realistic user interactions using an LLM.^[conversation-simulation-databricks-on-aws.md]

> **Note**: Conversation simulation is [experimental](https://docs.databricks.com/aws/en/release-notes/release-types). The API and behavior might change in future releases.^[conversation-simulation-databricks-on-aws.md]

## Why simulate conversations?

Simulated conversations address key challenges in agent evaluation by programmatically generating dialogues based on defined goals and personas. This approach enables:

- **Systematic evaluation**: Test different agent versions with consistent goals and personas.
- **Red-teaming**: Stress-test agents with diverse user behaviors at scale.
- **Rapid iteration**: Generate new test conversations instantly when requirements change.^[conversation-simulation-databricks-on-aws.md]

## Prerequisites

Install MLflow 3.10.0 or later:

```bash
pip install --upgrade 'mlflow[databricks]>=3.10'
```

^[conversation-simulation-databricks-on-aws.md]

## Workflow

1. **Define test cases or extract from existing conversations** — Specify goals, personas, and context for each simulated conversation, or generate them from production sessions.
2. **Create simulator** — Initialize [ConversationSimulator](/concepts/conversationsimulator.md) with your test cases and configuration.
3. **Define your agent** — Implement your agent in a function that accepts conversation history.
4. **Run evaluation** — Pass the simulator to `mlflow.genai.evaluate()` with your scorers.^[conversation-simulation-databricks-on-aws.md]

## Quick start

The following example simulates conversations and evaluates them with multi-turn and single-turn scorers:

```python
import mlflow
from mlflow.genai.simulators import ConversationSimulator
from mlflow.genai.scorers import ConversationCompleteness, Safety
from openai import OpenAI

client = OpenAI()

# 1. Define test cases with goals (required) and optional persona/context
test_cases = [
    {"goal": "Successfully configure experiment tracking"},
    {
        "goal": "Identify and fix a model deployment error",
        "persona": "You are a frustrated data scientist who has been stuck on this issue for hours",
    },
    {
        "goal": "Set up model versioning for a production pipeline",
        "persona": "You are a beginner who needs step-by-step guidance",
        "context": {"user_id": "beginner_123"},
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
        Safety(),                    # Single-turn scorer (applied to each turn)
    ],
)
```

^[conversation-simulation-databricks-on-aws.md]

## Defining test cases

Each test case represents a conversation scenario. Three fields are supported:

### Goal (required)

The goal describes what the simulated user wants to achieve. It should be specific enough to guide the conversation but open-ended enough to allow natural dialogue. Good goals describe the expected outcome so the simulator knows when the user's intent has been accomplished.

```python
# Good goals - specific, actionable, and describe expected outcome
{"goal": "Successfully configure MLflow tracking for a distributed training job"}
{"goal": "Understand when to use experiments vs. runs in MLflow"}
{"goal": "Identify and fix why model artifacts aren't being logged"}

# Less effective goals - too vague, no expected outcome
{"goal": "Learn about MLflow"}
{"goal": "Get help"}
```

^[conversation-simulation-databricks-on-aws.md]

### Persona (optional)

The persona shapes how the simulated user communicates. If not specified, a default helpful user persona is used.

```python
# Technical expert who asks detailed questions
{"goal": "Reduce model serving latency below 100ms", "persona": "You are a senior ML engineer who asks precise technical questions"}

# Beginner who needs more guidance
{"goal": "Successfully set up experiment tracking", "persona": "You are new to MLflow and need step-by-step explanations"}

# Frustrated user testing agent resilience
{"goal": "Fix a deployment blocking production", "persona": "You are impatient because this is blocking a release"}
```

^[conversation-simulation-databricks-on-aws.md]

### Context (optional)

The context field passes additional parameters to your predict function. This is useful for passing user identifiers for personalization, providing session state or configuration, or including metadata your agent needs.

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

Values in `context` are passed to `predict_fn` via `**kwargs`.^[conversation-simulation-databricks-on-aws.md]

### Define test cases as a list or DataFrame

Test cases can be supplied as a list of dictionaries or a pandas DataFrame:

```python
test_cases = [
    {"goal": "Successfully configure experiment tracking"},
    {"goal": "Debug a deployment error", "persona": "Senior engineer"},
    {"goal": "Set up a CI/CD pipeline for ML", "context": {"team": "platform"}},
]
simulator = ConversationSimulator(test_cases=test_cases)

# Or from a DataFrame
import pandas as pd
df = pd.DataFrame([
    {"goal": "Successfully configure experiment tracking"},
    {"goal": "Debug a deployment error", "persona": "Senior engineer"},
    {"goal": "Set up a CI/CD pipeline for ML"},
])
simulator = ConversationSimulator(test_cases=df)
```

^[conversation-simulation-databricks-on-aws.md]

## Generate test cases from existing conversations

Use `mlflow.genai.simulators.generate_test_cases` to extract goals and personas from existing conversation sessions (e.g., production data). This creates test cases that reflect real user behavior:

```python
import mlflow
from mlflow.genai.simulators import generate_test_cases, ConversationSimulator

# Get existing sessions from your experiments
sessions = mlflow.search_sessions(
    locations=["<experiment-id>"],
    max_results=50,
)

# Generate test cases by extracting goals and personas
test_cases = generate_test_cases(sessions)

# Optionally, save generated test cases as a dataset for reproducibility
from mlflow.genai.datasets import create_dataset
dataset = create_dataset(name="generated_scenarios")
dataset.merge_records([{"inputs": tc} for tc in test_cases])

# Use generated test cases with the simulator
simulator = ConversationSimulator(test_cases=test_cases)
```

^[conversation-simulation-databricks-on-aws.md]

## Track test cases as MLflow dataset

For reproducible testing, persist test cases as an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md):

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

^[conversation-simulation-databricks-on-aws.md]

## Agent function interface

Your agent function receives conversation history and returns a response. Two parameter names are supported: `input` or `messages`. The conversation history is a list of message dicts following the Chat Completions format (each with `role` and `content`). Additional arguments are passed via `**kwargs`, including `mlflow_session_id` (unique ID for this conversation session) and any fields from the test case's `context`.

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

### Basic example

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

## Configuration options

### ConversationSimulator parameters

- `test_cases` — List of dicts, DataFrame, or MLflow dataset with goal, persona, and context.
- `max_turns` — Maximum number of turns before the conversation stops (unless the goal is achieved earlier).
- `user_model` — LLM to use for simulating user responses (see model selection below).
- `temperature` — Temperature parameter passed to the user simulation LLM.

### Model selection

The simulator uses an LLM to generate realistic user messages. You can specify a different model using the `user_model` parameter:

```python
simulator = ConversationSimulator(
    test_cases=test_cases,
    user_model="anthropic:/claude-sonnet-4-20250514",
    temperature=0.7,  # Passed to the user simulation LLM
)
```

Supported model formats follow the pattern `"<provider>:/<model>"`. See the [MLflow documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/custom-judges/supported-models) for the full list of supported providers.^[conversation-simulation-databricks-on-aws.md]

#### Information about the models powering conversation simulation

LLM-based conversation simulation might use third-party services to simulate user interactions, including Azure OpenAI operated by Microsoft. For Azure OpenAI, Databricks has opted out of Abuse Monitoring so no prompts or responses are stored with Azure OpenAI. For European Union (EU) workspaces, conversation simulation uses models hosted in the EU; all other regions use models hosted in the US. Disabling Partner-powered AI features prevents conversation simulation from calling partner-powered models. You can still use conversation simulation by providing your own model.^[conversation-simulation-databricks-on-aws.md]

### Conversation stopping

Conversations stop when any of these conditions are met:

- **Max turns reached**: The `max_turns` limit is hit.
- **Goal achieved**: The simulator detects the user's goal has been accomplished.^[conversation-simulation-databricks-on-aws.md]

## Viewing results

Simulated conversations appear in the MLflow UI with special metadata:

- **Session ID**: Each conversation has a unique session ID (prefixed with `sim-`).
- **Simulation metadata**: Goal, persona, and turn number are stored on each trace.

Navigate to the **Sessions** tab in your experiment to view conversations grouped by session. Select a session to see individual turns and their assessments.^[conversation-simulation-databricks-on-aws.md]

## Related concepts

- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment
- [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) — Persisting test cases for reproducibility
- [Production Monitoring](/concepts/production-monitoring.md) — Using registered scorers in the inference table pipeline
- [Code-based Scorers](/concepts/code-based-scorers.md) — Custom evaluation functions for MLflow GenAI

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
