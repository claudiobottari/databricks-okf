---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b49f0639182f6d8551fbf539b0aff360adec1ed714ac8a35ebee4576c75d6a06
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - test-case-generation-from-production-conversations
    - TCGFPC
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: Test Case Generation from Production Conversations
description: Process of extracting test scenarios (goals and personas) from existing production conversation sessions using mlflow.search_sessions and generate_test_cases.
tags:
  - mlflow
  - testing
  - synthetic-data
  - production
timestamp: "2026-06-19T09:23:38.424Z"
---

# Test Case Generation from Production Conversations

**Test Case Generation from Production Conversations** is a technique in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that automatically extracts structured test scenarios from real user conversations. This approach enables teams to create evaluation datasets that reflect actual user behavior, improving the relevance and coverage of agent testing.

## Overview

Instead of manually defining test cases or relying solely on synthetic data, you can generate test cases from existing production conversation sessions. This ensures that your evaluation dataset captures real user intents, behaviors, and edge cases that occur in production.^[conversation-simulation-databricks-on-aws.md]

## Workflow

The process involves three main steps:

1. **Retrieve existing sessions** from your MLflow experiments
2. **Generate test cases** by extracting goals and personas from those sessions
3. **Use the generated test cases** with a [ConversationSimulator](/concepts/conversationsimulator.md) for evaluation

## Implementation

### Retrieving Sessions

Use `mlflow.search_sessions()` to fetch existing conversation sessions from your experiments:^[conversation-simulation-databricks-on-aws.md]

```python
import mlflow

sessions = mlflow.search_sessions(
    locations=["<experiment-id>"],
    max_results=50,
)
```

### Generating Test Cases

Pass the retrieved sessions to `generate_test_cases()` to automatically extract goals and personas:^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.simulators import generate_test_cases, ConversationSimulator

test_cases = generate_test_cases(sessions)
```

The function analyzes each conversation session and produces test case objects containing the extracted goal and persona information.

### Using Generated Test Cases

The generated test cases can be used directly with a `ConversationSimulator`:^[conversation-simulation-databricks-on-aws.md]

```python
simulator = ConversationSimulator(test_cases=test_cases)
```

## Persisting Test Cases as Datasets

For reproducible testing, you can save generated test cases as an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md):^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.datasets import create_dataset

dataset = create_dataset(name="generated_scenarios")
dataset.merge_records([{"inputs": tc} for tc in test_cases])

# Later, retrieve and use the dataset
simulator = ConversationSimulator(test_cases=dataset)
```

## Benefits

- **Real-world relevance**: Test cases reflect actual user behavior and intents rather than synthetic scenarios^[conversation-simulation-databricks-on-aws.md]
- **Systematic evaluation**: Enables testing different agent versions with consistent goals and personas derived from production data^[conversation-simulation-databricks-on-aws.md]
- **Rapid iteration**: Generate new test conversations instantly when requirements change, without waiting for new production data^[conversation-simulation-databricks-on-aws.md]
- **Red-teaming**: Stress-test agents with diverse user behaviors at scale, based on real interaction patterns^[conversation-simulation-databricks-on-aws.md]

## Related Concepts

- [Conversation Simulation](/concepts/conversation-simulation.md) — Generating synthetic multi-turn conversations for testing
- [ConversationSimulator](/concepts/conversationsimulator.md) — The simulator that uses test cases to generate conversations
- [MLflow Evaluation Datasets](/concepts/mlflow-evaluation-datasets.md) — Persisting test cases for reproducible evaluation
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Monitoring real agent performance in production
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing agent versions using consistent test cases

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
