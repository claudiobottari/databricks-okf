---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 962ea911a78908314e5f8fe79e9573aa7878026ee090624d143c2980c8a57841
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - conversationsimulator
    - Conversation Simulator
    - conversation-simulation-mlflow
    - CS(
    - conversation-simulation
    - conversationsimulator-api
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: ConversationSimulator
description: MLflow API class that generates synthetic multi-turn conversations for testing conversational AI agents by defining test scenarios and simulating realistic user interactions.
tags:
  - mlflow
  - testing
  - conversational-ai
timestamp: "2026-06-19T17:51:46.631Z"
---

# ConversationSimulator

**ConversationSimulator** is an experimental feature in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that generates synthetic multi-turn conversations for testing conversational AI agents. Instead of manually creating test conversations or waiting for production data, you define test scenarios and let MLflow automatically simulate realistic user interactions. ^[conversation-simulation-databricks-on-aws.md]

## Prerequisites

ConversationSimulator requires MLflow 3.10.0 or later. Install it with:

```bash
pip install --upgrade 'mlflow[databricks]>=3.10'
```

^[conversation-simulation-databricks-on-aws.md]

## Why simulate conversations?

Conversation simulation addresses common challenges in evaluating conversational agents by programmatically generating conversations based on defined goals and personas. It enables: ^[conversation-simulation-databricks-on-aws.md]

- **Systematic evaluation**: Test different agent versions with consistent goals and personas.
- **Red-teaming**: Stress-test agents with diverse user behaviors at scale.
- **Rapid iteration**: Generate new test conversations instantly when requirements change.

## Workflow

1. **Define test cases** – Specify goals, personas, and context for each simulated conversation, or extract them from production sessions. ^[conversation-simulation-databricks-on-aws.md]
2. **Create simulator** – Initialize `ConversationSimulator` with your test cases and configuration. ^[conversation-simulation-databricks-on-aws.md]
3. **Define your agent** – Implement your agent in a function that accepts conversation history. ^[conversation-simulation-databricks-on-aws.md]
4. **Run evaluation** – Pass the simulator to `mlflow.genai.evaluate()` with your scorers. ^[conversation-simulation-databricks-on-aws.md]

## Quick start

Here is a complete example that simulates conversations and evaluates them:

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

simulator = ConversationSimulator(test_cases=test_cases, max_turns=5)

def predict_fn(input: list[dict], **kwargs):
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=input,
    )
    return response.choices[0].message.content

results = mlflow.genai.evaluate(
    data=simulator,
    predict_fn=predict_fn,
    scorers=[ConversationCompleteness(), Safety()],
)
```

^[conversation-simulation-databricks-on-aws.md]

## Defining test cases

Each test case represents a conversation scenario and supports three fields: ^[conversation-simulation-databricks-on-aws.md]

- **`goal`** (required) – Describes what the simulated user wants to achieve. It should be specific and describe the expected outcome so the simulator knows when the user's intent is accomplished. ^[conversation-simulation-databricks-on-aws.md]
- **`persona`** (optional) – Shapes how the simulated user communicates. If not specified, a default helpful user persona is used. ^[conversation-simulation-databricks-on-aws.md]
- **`context`** (optional) – Passes additional parameters (e.g., user ID, session state) to your agent function via `**kwargs`. ^[conversation-simulation-databricks-on-aws.md]

Test cases can be provided as a list of dictionaries or a pandas DataFrame. ^[conversation-simulation-databricks-on-aws.md]

## Generating test cases from existing conversations

Use `generate_test_cases` to extract goals and personas from production sessions stored in MLflow experiments. This creates test cases that reflect real user behavior: ^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.simulators import generate_test_cases, ConversationSimulator

sessions = mlflow.search_sessions(locations=["<experiment-id>"], max_results=50)
test_cases = generate_test_cases(sessions)
simulator = ConversationSimulator(test_cases=test_cases)
```

Generated test cases can optionally be saved as an [Evaluation Dataset](/concepts/evaluation-dataset.md) for reproducibility. ^[conversation-simulation-databricks-on-aws.md]

## Tracking test cases as MLflow Dataset

For reproducible testing, persist test cases as an MLflow Evaluation Dataset using `create_dataset`: ^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.datasets import create_dataset, get_dataset

dataset = create_dataset(name="conversation_test_cases")
dataset.merge_records([{"inputs": {"goal": "Successfully configure experiment tracking"}}])

simulator = ConversationSimulator(test_cases=dataset)
```

## Agent function interface

Your agent function receives the conversation history and returns a response. Two parameter names are supported: `input` (list of message dicts, as in the Chat Completions response format) or `messages` (equivalent alternative). ^[conversation-simulation-databricks-on-aws.md]

Additional arguments passed via `**kwargs` include `mlflow_session_id` (a unique ID for the session) and any fields from the test case's `context`. ^[conversation-simulation-databricks-on-aws.md]

A basic example:

```python
from openai import OpenAI

client = OpenAI()

def predict_fn(input: list[dict], **kwargs):
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=input,
    )
    return response.choices[0].message.content
```

^[conversation-simulation-databricks-on-aws.md]

## Configuration options

The `ConversationSimulator` accepts several parameters: ^[conversation-simulation-databricks-on-aws.md]

- `user_model` – Specify the LLM used to generate simulated user messages. Format: `"<provider>:/<model>"`. Defaults to a Databricks hosted model. ^[conversation-simulation-databricks-on-aws.md]
- `temperature` – Controls randomness of the user simulation LLM. ^[conversation-simulation-databricks-on-aws.md]
- `max_turns` – Maximum number of turns per conversation before stopping. ^[conversation-simulation-databricks-on-aws.md]

Conversations also stop when the simulator detects that the user's goal has been achieved. ^[conversation-simulation-databricks-on-aws.md]

### Model provider information

LLM-based conversation simulation may use third-party services, including Azure OpenAI operated by Microsoft. Databricks has opted out of Abuse Monitoring for Azure OpenAI, so no prompts or responses are stored with Azure OpenAI. For European Union (EU) workspaces, models hosted in the EU are used; all other regions use US-hosted models. Disabling Partner-powered AI features prevents conversation simulation from calling partner-powered models, but you can still use the feature by providing your own model. ^[conversation-simulation-databricks-on-aws.md]

## Viewing results

Simulated conversations appear in the MLflow UI with special metadata: ^[conversation-simulation-databricks-on-aws.md]

- Each conversation has a unique session ID prefixed with `sim-`.
- Goal, persona, and turn number are stored on each trace.

Navigate to the **Sessions** tab in your experiment to view conversations grouped by session. Select a session to see individual turns and their assessments. ^[conversation-simulation-databricks-on-aws.md]

## Related concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md)
- [Evaluation Dataset](/concepts/evaluation-dataset.md)
- ConversationCompleteness
- Safety
- generate_test_cases
- create_dataset
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
