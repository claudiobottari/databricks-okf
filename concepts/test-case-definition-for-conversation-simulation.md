---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 626f2bdf1f90bc6c343206b41f3bb413b6ac9d6acaeb6a027ea97a0ff5348c45
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - test-case-definition-for-conversation-simulation
    - TCDFCS
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: Test Case Definition for Conversation Simulation
description: Structured specification of a conversation scenario using goal, persona, and context fields to guide the simulator in generating realistic dialogues.
tags:
  - testing
  - conversational-ai
  - workflow
timestamp: "2026-06-19T17:52:23.550Z"
---

# Test Case Definition for Conversation Simulation

**Test Case Definition for Conversation Simulation** is the process of specifying structured scenarios that drive synthetic multi-turn conversation generation for evaluating conversational AI agents. Each test case defines what a simulated user should accomplish, how they should behave, and what metadata the agent may need to produce a realistic response. ^[conversation-simulation-databricks-on-aws.md]

## Overview

A test case is the fundamental unit of input to a [ConversationSimulator](/concepts/conversationsimulator.md). It encodes a conversation scenario that the simulator's underlying LLM uses to generate a sequence of user messages. Properly defined test cases enable systematic evaluation, red-teaming, and rapid iteration without relying on manually crafted dialogues or production data. ^[conversation-simulation-databricks-on-aws.md]

## Test Case Fields

Each test case is a dictionary (or a row in a DataFrame) supporting three optional fields and one required field:

### Goal (Required)

The **goal** describes what the simulated user wants to achieve. It must be specific enough to guide the conversation but open-ended enough to allow natural dialogue. Effective goals state the expected outcome so the simulator can detect when the user's intent has been accomplished. ^[conversation-simulation-databricks-on-aws.md]

**Good examples** – specific, actionable, with a clear outcome: ^[conversation-simulation-databricks-on-aws.md]

```python
{"goal": "Successfully configure MLflow tracking for a distributed training job"}
{"goal": "Understand when to use experiments vs. runs in MLflow"}
{"goal": "Identify and fix why model artifacts aren't being logged"}
```

**Less effective examples** – too vague, no expected outcome: ^[conversation-simulation-databricks-on-aws.md]

```python
{"goal": "Learn about MLflow"}
{"goal": "Get help"}
```

### Persona (Optional)

The **persona** shapes how the simulated user communicates. If omitted, a default helpful user persona is used. Personas can range from a senior ML engineer asking precise questions to a frustrated user testing the agent's resilience. ^[conversation-simulation-databricks-on-aws.md]

**Examples:** ^[conversation-simulation-databricks-on-aws.md]

```python
# Technical expert who asks detailed questions
{"goal": "Reduce model serving latency below 100ms", "persona": "You are a senior ML engineer who asks precise technical questions"}

# Beginner who needs more guidance
{"goal": "Successfully set up experiment tracking", "persona": "You are new to MLflow and need step-by-step explanations"}

# Frustrated user testing agent resilience
{"goal": "Fix a deployment blocking production", "persona": "You are impatient because this is blocking a release"}
```

### Context (Optional)

The **context** field passes additional parameters (via `**kwargs`) to the agent's `predict_fn`. This is useful for personalizing responses, injecting session state, or providing configuration metadata. ^[conversation-simulation-databricks-on-aws.md]

**Example:** ^[conversation-simulation-databricks-on-aws.md]

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

## Test Case Formats

Test cases can be provided as:
- A **list of dictionaries** (the simplest approach) ^[conversation-simulation-databricks-on-aws.md]
- A **pandas DataFrame** with columns `goal`, `persona`, and `context` ^[conversation-simulation-databricks-on-aws.md]
- An **MLflow Evaluation Dataset** for reproducible testing ^[conversation-simulation-databricks-on-aws.md]

## Generating Test Cases from Existing Sessions

Test cases can be extracted from production conversation sessions using `generate_test_cases`. This creates scenarios that reflect real user behavior and is useful for building a representative evaluation suite. ^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.simulators import generate_test_cases, ConversationSimulator

sessions = mlflow.search_sessions(
    locations=["<experiment-id>"],
    max_results=50,
)

test_cases = generate_test_cases(sessions)
simulator = ConversationSimulator(test_cases=test_cases)
```

Generated test cases can be persisted as an MLflow dataset for reproducibility. ^[conversation-simulation-databricks-on-aws.md]

## Relation to Agent Function

The agent function (`predict_fn`) receives the conversation history generated from a test case. It accepts either `input` or `messages` as the parameter name for the conversation history, and receives `context` fields through `**kwargs`. The simulator uses the goal to determine when a conversation is complete. ^[conversation-simulation-databricks-on-aws.md]

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
