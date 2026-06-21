---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3a485ab96949892ae183e545ee5bb1f973a210a9511f9ead7ba96c738a8ef6c8
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-turn-evaluation-with-simulated-conversations
    - MEWSC
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: Multi-turn Evaluation with Simulated Conversations
description: Using the ConversationSimulator as input to mlflow.genai.evaluate() alongside multi-turn scorers (ConversationCompleteness) and single-turn scorers (Safety) applied per turn.
tags:
  - mlflow
  - evaluation
  - conversational-ai
timestamp: "2026-06-19T17:52:19.733Z"
---

# Multi-turn Evaluation with Simulated Conversations

**Multi-turn Evaluation with Simulated Conversations** is an experimental feature in [MLflow](/concepts/mlflow.md) that enables synthetic generation of realistic multi-turn dialogues for testing conversational AI agents. Instead of manually crafting test conversations or waiting for production data, you define test scenarios—goals, personas, and optional context—and let MLflow programmatically simulate user interactions. ^[conversation-simulation-databricks-on-aws.md]

## Benefits

Simulating conversations addresses several challenges in evaluating conversational agents: ^[conversation-simulation-databricks-on-aws.md]

- **Systematic evaluation** – Test different agent versions with consistent goals and personas.
- **Red-teaming** – Stress-test agents with diverse user behaviors at scale.
- **Rapid iteration** – Generate new test conversations instantly when requirements change.

## Workflow

The typical workflow has four steps: ^[conversation-simulation-databricks-on-aws.md]

1. **Define test cases** – Specify goals, personas, and context for each simulated conversation, or extract them from existing production sessions.
2. **Create simulator** – Initialize a [ConversationSimulator](/concepts/conversationsimulator.md) with your test cases and configuration.
3. **Define your agent** – Implement your agent as a function that accepts conversation history.
4. **Run evaluation** – Pass the simulator to `mlflow.genai.evaluate()` with your scorers (both multi-turn and single-turn).

A complete example can be found in the [quick-start](#quick-start) section of the simulation guide.

## Defining Test Cases

Each test case represents a conversation scenario. Three fields are supported: ^[conversation-simulation-databricks-on-aws.md]

### Goal

The goal describes what the simulated user wants to achieve. It should be specific enough to guide the dialogue but open-ended enough to allow natural conversation. A well-formed goal describes the expected outcome so the simulator knows when the user’s intent has been accomplished. ^[conversation-simulation-databricks-on-aws.md]

```python
# Good goal
{"goal": "Successfully configure MLflow tracking for a distributed training job"}
# Less effective (too vague)
{"goal": "Learn about MLflow"}
```

### Persona

The persona shapes how the simulated user communicates. If not specified, a default helpful persona is used. Personas can range from technical experts to frustrated users or beginners. ^[conversation-simulation-databricks-on-aws.md]

```python
{"goal": "Fix a deployment blocking production", "persona": "You are impatient because this is blocking a release"}
```

### Context

The context field passes additional parameters to your agent’s predict function, such as user identifiers, session state, or configuration metadata. ^[conversation-simulation-databricks-on-aws.md]

```python
{"goal": "Get personalized recommendations", "context": {"user_id": "enterprise_user_42", "subscription_tier": "premium"}}
```

Test cases can be provided as a list of dictionaries or a pandas DataFrame. ^[conversation-simulation-databricks-on-aws.md]

## Generating Test Cases from Existing Conversations

Use `mlflow.genai.simulators.generate_test_cases()` to extract goals and personas from existing production sessions. This is useful for creating test cases that reflect real user behavior. The generated test cases can optionally be saved as an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) for reproducibility. ^[conversation-simulation-databricks-on-aws.md]

```python
sessions = mlflow.search_sessions(locations=["<experiment-id>"], max_results=50)
test_cases = generate_test_cases(sessions)
```

## Tracking Test Cases as an MLflow Dataset

For reproducible testing, persist your test cases using the [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) API. This allows you to create, populate, and later retrieve datasets for use with the simulator. ^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.datasets import create_dataset, get_dataset
dataset = create_dataset(name="conversation_test_cases")
dataset.merge_records([{"inputs": {"goal": "Successfully configure experiment tracking"}}])
simulator = ConversationSimulator(test_cases=dataset)
```

## Agent Function Interface

Your agent receives the conversation history and returns a response. The function must accept either `input` or `messages` as a parameter name, along with `**kwargs` for additional arguments such as `mlflow_session_id` or fields from the test case’s context. ^[conversation-simulation-databricks-on-aws.md]

```python
def predict_fn(input: list[dict], **kwargs) -> str:
    """Return the assistant's response as a string."""
```

## Configuration Options

### Model Selection

The simulator uses an LLM to generate realistic user messages. You can specify a different model using the `user_model` parameter with the format `"<provider>:/<model>"`. The `temperature` parameter is also passed to the user simulation LLM. ^[conversation-simulation-databricks-on-aws.md]

```python
simulator = ConversationSimulator(
    test_cases=test_cases,
    user_model="anthropic:/claude-sonnet-4-20250514",
    temperature=0.7
)
```

LLM-based conversation simulation for Azure OpenAI uses models hosted in the region corresponding to the workspace (EU or US). Data storage and abuse monitoring policies are noted in the documentation. Disabling Partner-powered AI features prevents the use of partner-provided models; you can still simulate by providing your own model. ^[conversation-simulation-databricks-on-aws.md]

### Conversation Stopping

Conversations stop when any of the following conditions are met: ^[conversation-simulation-databricks-on-aws.md]

- **Max turns reached** – The `max_turns` limit is hit.
- **Goal achieved** – The simulator detects that the user’s goal has been accomplished.

## Viewing Results

Simulated conversations appear in the MLflow UI with special metadata: ^[conversation-simulation-databricks-on-aws.md]

- **Session ID** – Each conversation has a unique session ID prefixed with `sim-`.
- **Simulation metadata** – Goal, persona, and turn number are stored on each trace.

Navigate to the **Sessions** tab in your experiment to view conversations grouped by session. Select a session to see individual turns and their assessments.

## Prerequisites

Install MLflow 3.10.0 or later with the Databricks extras: ^[conversation-simulation-databricks-on-aws.md]

```bash
pip install --upgrade 'mlflow[databricks]>=3.10'
```

## Related Concepts

- [ConversationSimulator](/concepts/conversationsimulator.md)
- [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md)
- [Multi-turn scorers](/concepts/multi-turn-scorers-in-mlflow.md) (e.g., ConversationCompleteness)
- Single-turn scorers (e.g., Safety)
- [Evaluate conversations](/concepts/multi-turn-conversation-judges.md) – static evaluation and multi-turn scoring
- Red-teaming

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
