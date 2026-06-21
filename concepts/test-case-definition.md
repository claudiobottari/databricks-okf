---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cfc88d271b11247eb1bb0ba9cede57ecdfd661c028b8fcb05a5ba9b3ecaaf81e
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - test-case-definition
    - TCD
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: Test Case Definition
description: Scenarios for simulated conversations defined by a required goal and optional persona and context fields that guide the simulated user's behavior.
tags:
  - testing
  - conversational-ai
  - mlflow
timestamp: "2026-06-18T14:44:08.672Z"
---

# Test Case Definition

**Test Case Definition** refers to the structured specification of scenarios used to evaluate the performance and behavior of GenAI agents or other AI systems. In the context of [MLflow GenAI](/concepts/mlflow-3-for-genai.md), test cases define the inputs, expected outcomes, and contextual parameters that drive automated evaluation, including [Conversation Simulation](/concepts/conversation-simulation.md) and offline assessment.

## Overview

A test case represents a single evaluation scenario that describes what an agent should accomplish and under what conditions. Test cases are the fundamental building blocks for systematic evaluation, enabling consistent testing across different agent versions, configurations, and iterations. ^[conversation-simulation-databricks-on-aws.md]

Test cases can be defined manually by developers or generated automatically from existing production conversations, allowing evaluation scenarios to reflect real user behavior. ^[conversation-simulation-databricks-on-aws.md]

## Test Case Fields

Test cases typically support three primary fields that together define a complete evaluation scenario. ^[conversation-simulation-databricks-on-aws.md]

### Goal

The **goal** describes what the simulated user wants to achieve. It should be specific enough to guide the conversation but open-ended enough to allow natural dialogue. Good goals describe the expected outcome so the evaluation system knows when the user's intent has been accomplished. ^[conversation-simulation-databricks-on-aws.md]

- **Effective goals**: "Successfully configure MLflow tracking for a distributed training job" or "Understand when to use experiments vs. runs in MLflow"
- **Less effective goals**: "Learn about MLflow" or "Get help" — these are too vague to guide meaningful evaluation

### Persona

The **persona** shapes how the simulated user communicates. If not specified, a default helpful user persona is used. Personas are useful for testing agent behavior across different user types and scenarios. ^[conversation-simulation-databricks-on-aws.md]

Common persona examples include:
- A senior ML engineer who asks precise technical questions
- A beginner who needs step-by-step explanations
- A frustrated user testing agent resilience under pressure
- A beginner who needs step-by-step guidance

### Context

The **context** field passes additional parameters to the agent's prediction function. This is useful for providing user identifiers for personalization, session state or configuration, or metadata the agent needs to function properly. ^[conversation-simulation-databricks-on-aws.md]

Context fields are passed to the agent function via keyword arguments (`**kwargs`), allowing the agent to access values such as `user_id`, `subscription_tier`, or `preferred_framework`. ^[conversation-simulation-databricks-on-aws.md]

## Defining Test Cases

Test cases can be defined as a list of dictionaries or a pandas DataFrame. The simplest form requires only a goal field: ^[conversation-simulation-databricks-on-aws.md]

```python
test_cases = [
    {"goal": "Successfully configure experiment tracking"},
    {"goal": "Debug a deployment error", "persona": "Senior engineer"},
    {"goal": "Set up a CI/CD pipeline for ML", "context": {"team": "platform"}},
]
```

## Generating Test Cases from Existing Conversations

Test cases can be generated from existing conversation sessions using `generate_test_cases`. This approach creates test cases that reflect real user behavior from production conversations, extracted from stored sessions in MLflow experiments. ^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.simulators import generate_test_cases, ConversationSimulator

sessions = mlflow.search_sessions(
    locations=["<experiment-id>"],
    max_results=50,
)

test_cases = generate_test_cases(sessions)
```

Generated test cases can be saved as datasets for reproducibility using the [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) API. ^[conversation-simulation-databricks-on-aws.md]

## Test Cases in Conversation Simulation

When used with `ConversationSimulator`, test cases drive multi-turn conversations between simulated users and the agent. The simulator uses an LLM to generate realistic user messages based on the defined test cases, continuing until the goal is achieved or the maximum number of turns is reached. ^[conversation-simulation-databricks-on-aws.md]

## Persistence and Reproducibility

For reproducible testing, test cases can be persisted as [MLflow Evaluation Datasets](/concepts/mlflow-evaluation-datasets.md) using the `create_dataset` and `get_dataset` functions. This allows test cases to be versioned, shared, and reused across evaluation runs. ^[conversation-simulation-databricks-on-aws.md]

## Related Concepts

- [Conversation Simulation](/concepts/conversation-simulation.md) — The process of generating synthetic multi-turn conversations from test cases
- [Evaluation Dataset](/concepts/evaluation-dataset.md) — Persisted test cases for reproducible evaluation
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The broader evaluation framework for GenAI agents
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and evaluations
- [Multi-Turn Evaluation](/concepts/multi-turn-conversation-evaluation.md) — Evaluation that considers entire conversation histories rather than individual turns

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
