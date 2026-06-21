---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8e307da4265b44ec195d4b092ec021a70adf5c4f01e5261eef1d394d5779b8df
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - test-cases-for-conversation-simulation
    - TCFCS
    - Test Cases for Simulation
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: Test Cases for Conversation Simulation
description: Structured specifications (goal, persona, context) defining each simulated conversation scenario, where goal describes the user's intent, persona shapes communication style, and context provides additional parameters to the agent function.
tags:
  - mlflow
  - testing
  - conversational-ai
timestamp: "2026-06-19T14:25:28.093Z"
---

```markdown
---
title: Test Cases for Conversation Simulation
summary: Definitions of conversation scenarios using three fields — goal (required), persona (optional), and context (optional) — that guide the simulator in generating realistic user interactions with an AI agent.
sources:
  - conversation-simulation-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:09:33.795Z"
updatedAt: "2026-06-18T11:09:33.795Z"
tags:
  - mlflow
  - testing
  - test-cases
  - conversational-ai
aliases:
  - test-cases-for-conversation-simulation
  - TCFCS
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 0
---

# Test Cases for Conversation Simulation

**Test cases for conversation simulation** define the scenarios that an [[MLflow 3 for GenAI|MLflow GenAI]] `ConversationSimulator` uses to generate synthetic multi-turn conversations for testing conversational AI agents. Each test case represents a specific user interaction scenario, enabling systematic evaluation without requiring manually created conversations or production data.^[conversation-simulation-databricks-on-aws.md]

## Overview

Test cases allow you to define goals, personas, and context for simulated conversations. Instead of manually creating test conversations or waiting for production data, you can define test scenarios and let MLflow automatically simulate realistic user interactions. This enables systematic evaluation, red-teaming, and rapid iteration.^[conversation-simulation-databricks-on-aws.md]

## Test Case Structure

Each test case is defined as a dictionary with three optional fields. The `goal` field is required; `persona` and `context` are optional.^[conversation-simulation-databricks-on-aws.md]

### Goal

The goal describes what the simulated user wants to achieve. It should be specific enough to guide the conversation but open-ended enough to allow natural dialogue. Good goals describe the expected outcome so the simulator knows when the user's intent has been accomplished.^[conversation-simulation-databricks-on-aws.md]

**Good goals** — specific, actionable, and describe expected outcomes:^[conversation-simulation-databricks-on-aws.md]

```python
{"goal": "Successfully configure MLflow tracking for a distributed training job"}
{"goal": "Understand when to use experiments vs. runs in MLflow"}
{"goal": "Identify and fix why model artifacts aren't being logged"}
```

**Less effective goals** — too vague, no expected outcome:^[conversation-simulation-databricks-on-aws.md]

```python
{"goal": "Learn about MLflow"}
{"goal": "Get help"}
```

### Persona

The persona shapes how the simulated user communicates. If not specified, a default helpful user persona is used.^[conversation-simulation-databricks-on-aws.md]

**Technical expert example**:^[conversation-simulation-databricks-on-aws.md]

```python
{
    "goal": "Reduce model serving latency below 100ms",
    "persona": "You are a senior ML engineer who asks precise technical questions",
}
```

**Beginner example**:^[conversation-simulation-databricks-on-aws.md]

```python
{
    "goal": "Successfully set up experiment tracking",
    "persona": "You are new to MLflow and need step-by-step explanations",
}
```

**Frustrated user example** for testing agent resilience:^[conversation-simulation-databricks-on-aws.md]

```python
{
    "goal": "Fix a deployment blocking production",
    "persona": "You are impatient because this is blocking a release",
}
```

### Context

The context field passes additional parameters to your [[Agent Function Interface|agent function]], received via `**kwargs`. This is useful for:^[conversation-simulation-databricks-on-aws.md]

- Passing user identifiers for personalization
- Providing session state or configuration
- Including metadata your agent needs

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

## Defining Test Cases

Test cases can be defined as a list of dictionaries or a pandas DataFrame:^[conversation-simulation-databricks-on-aws.md]

```python
test_cases = [
    {"goal": "Successfully configure experiment tracking"},
    {"goal": "Debug a deployment error", "persona": "Senior engineer"},
    {"goal": "Set up a CI/CD pipeline for ML", "context": {"team": "platform"}},
]
simulator = ConversationSimulator(test_cases=test_cases)
```

Using a DataFrame:^[conversation-simulation-databricks-on-aws.md]

```python
import pandas as pd
df = pd.DataFrame(
    [
        {"goal": "Successfully configure experiment tracking"},
        {"goal": "Debug a deployment error", "persona": "Senior engineer"},
        {"goal": "Set up a CI/CD pipeline for ML"},
    ]
)
simulator = ConversationSimulator(test_cases=df)
```

## Generating Test Cases from Existing Conversations

Use `generate_test_cases` to extract goals and personas from existing conversation sessions, creating test cases that reflect real user behavior:^[conversation-simulation-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.simulators import generate_test_cases, ConversationSimulator

sessions = mlflow.search_sessions(
    locations=["<experiment-id>"],
    max_results=50,
)

test_cases = generate_test_cases(sessions)

simulator = ConversationSimulator(test_cases=test_cases)
```

## Persisting Test Cases as MLflow Datasets

For reproducible testing, persist test cases as an [[MLflow Evaluation Dataset]]:^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.datasets import create_dataset, get_dataset

dataset = create_dataset(name="conversation_test_cases")
dataset.merge_records(
    [
        {"inputs": {"goal": "Successfully configure experiment tracking"}},
        {"inputs": {"goal": "Debug a deployment error", "persona": "Senior engineer"}},
    ]
)

dataset = get_dataset(name="conversation_test_cases")
simulator = ConversationSimulator(test_cases=dataset)
```

## Quick Start Example

A complete example that defines test cases, creates a simulator, and runs evaluation:^[conversation-simulation-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.simulators import ConversationSimulator
from mlflow.genai.scorers import ConversationCompleteness, Safety
from openai import OpenAI

client = OpenAI()

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

simulator = ConversationSimulator(
    test_cases=test_cases,
    max_turns=5,
)

def predict_fn(input: list[dict], **kwargs):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=input,
    )
    return response.choices[0].message.content

results = mlflow.genai.evaluate(
    data=simulator,
    predict_fn=predict_fn,
    scorers=[
        ConversationCompleteness(),
        Safety(),
    ],
)
```

## Conversation Stopping Conditions

When using test cases with the simulator, conversations stop when either:^[conversation-simulation-databricks-on-aws.md]

- **Max turns reached**: The `max_turns` limit is hit
- **Goal achieved**: The simulator detects the user's goal has been accomplished

## Related Concepts

- [[ConversationSimulator]] — The class that consumes test cases to generate synthetic conversations
- [[MLflow 3 for GenAI|MLflow GenAI]] — The MLflow subsystem for generative AI evaluation
- [[MLflow Evaluation Dataset]] — For persisting test cases for reproducibility
- [[Agent Function Interface|Agent Function]] — The predict function that receives test case context via kwargs
- Conversation Completeness Scorer — Multi-turn scorer for evaluating conversation quality
- [[Safety Scorer in MLflow|Safety Scorer]] — Single-turn scorer applied to each conversation turn

## Sources

- conversation-simulation-databricks-on-aws.md
```

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
