---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c58bfd4f733e71c21aa4c381bb6ce5fce27c268cf060df37ae1e1620a87b4ec6
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-evaluation-dataset-integration-for-conversation-simulation
    - MEDIFCS
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: MLflow Evaluation Dataset Integration for Conversation Simulation
description: Mechanism to persist conversation test cases as MLflow Evaluation Datasets for reproducible testing, using create_dataset and get_dataset APIs.
tags:
  - mlflow
  - reproducibility
  - data-management
timestamp: "2026-06-19T17:51:56.419Z"
---

# MLflow Evaluation Dataset Integration for Conversation Simulation

**MLflow Evaluation Dataset Integration** for [Conversation Simulation](/concepts/conversation-simulation.md) allows you to persist and reuse test case definitions as first-class [MLflow Evaluation Datasets](/concepts/mlflow-evaluation-datasets.md). This integration ensures reproducibility and versionability of the scenarios used to test conversational AI agents.

## Overview

When running multi-turn conversation simulations with `ConversationSimulator`, test cases (goals, personas, context) can be stored as an MLflow Evaluation Dataset instead of being defined inline. This makes it possible to track, share, and reproduce simulation scenarios across experiments. ^[conversation-simulation-databricks-on-aws.md]

## Prerequisites

- MLflow 3.10.0 or later (`pip install --upgrade 'mlflow[databricks]>=3.10'`). ^[conversation-simulation-databricks-on-aws.md]

## Creating an Evaluation Dataset for Test Cases

Use the `mlflow.genai.datasets.create_dataset` function to create a named dataset and populate it with the test case definitions. Each record’s `inputs` field should contain the test case dictionary (goal, persona, context).

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
```

^[conversation-simulation-databricks-on-aws.md]

## Using Datasets with ConversationSimulator

Once a dataset is created and persisted, you can retrieve it by name and pass it directly as the `test_cases` argument to `ConversationSimulator`. This eliminates the need to redefine test cases each time a simulation is run.

```python
dataset = get_dataset(name="conversation_test_cases")
simulator = ConversationSimulator(test_cases=dataset)
```

^[conversation-simulation-databricks-on-aws.md]

## Generating Test Cases from Existing Conversations

Test cases can also be **generated** from production conversation sessions using `generate_test_cases`. After generation, you can optionally save the resulting test cases as an evaluation dataset for future use, ensuring that scenarios derived from real user behavior are persisted and versioned.

```python
import mlflow
from mlflow.genai.simulators import generate_test_cases, ConversationSimulator
from mlflow.genai.datasets import create_dataset

# Get existing sessions
sessions = mlflow.search_sessions(
    locations=["<experiment-id>"],
    max_results=50,
)

# Generate test cases
test_cases = generate_test_cases(sessions)

# Save as a dataset
dataset = create_dataset(name="generated_scenarios")
dataset.merge_records([{"inputs": tc} for tc in test_cases])

# Use in simulator
simulator = ConversationSimulator(test_cases=dataset)
```

^[conversation-simulation-databricks-on-aws.md]

## Benefits

- **Reproducibility**: Test cases are tied to a dataset version, enabling consistent evaluations over time.
- **Sharing**: Datasets can be discovered and reused across teams and experiments.
- **Versioning**: Changes to test scenarios are tracked as new dataset versions.

## Related Concepts

- [Conversation Simulation](/concepts/conversation-simulation.md) – The core workflow for generating synthetic multi-turn conversations.
- [MLflow Evaluation Datasets](/concepts/mlflow-evaluation-datasets.md) – The data abstraction that stores and version evaluation inputs.
- [ConversationSimulator](/concepts/conversationsimulator.md) – The API that drives simulation using test cases.
- Evaluation with MLflow – General evaluation framework for LLM-based agents.
- Red-teaming – Security testing scenario supported by conversation simulation.

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
