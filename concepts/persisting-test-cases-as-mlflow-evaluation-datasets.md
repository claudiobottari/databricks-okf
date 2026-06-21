---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c5a77d0b9b356f98954f818efad2da3a19c103d4abd149f1d95a81e964bc98a2
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - persisting-test-cases-as-mlflow-evaluation-datasets
    - PTCAMED
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: Persisting Test Cases as MLflow Evaluation Datasets
description: Storing conversation test cases in reusable MLflow Evaluation Datasets via mlflow.genai.datasets for reproducible testing and versioning across simulation runs.
tags:
  - mlflow
  - testing
  - data-management
  - reproducibility
timestamp: "2026-06-19T14:25:37.980Z"
---

# Persisting Test Cases as MLflow Evaluation Datasets

**Persisting test cases as MLflow evaluation datasets** refers to the practice of saving structured test case records (goals, personas, context) in an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) to enable reproducible testing and evaluation of conversational AI agents. This approach decouples test case authoring from evaluation runs, allowing teams to version, share, and reuse test suites across experiments.

## Overview

When using [ConversationSimulator](/concepts/conversationsimulator.md) to generate synthetic multi-turn conversations, test cases are typically defined inline as a list of dictionaries or a DataFrame. However, for long-lived projects or collaborative workflows, it is beneficial to persist these test cases as a named dataset. MLflow provides a dataset API (`mlflow.genai.datasets`) to create, populate, and retrieve evaluation datasets that can be passed directly to the simulator or other evaluation functions. ^[conversation-simulation-databricks-on-aws.md]

## Creating a Dataset from Test Cases

The `create_dataset` function creates a new dataset object. You then populate it by merging records, each containing an `inputs` key whose value is the test case dictionary (including `goal`, `persona`, `context`, etc.). The dataset can be given a descriptive name for later retrieval. ^[conversation-simulation-databricks-on-aws.md]

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

## Benefits

- **Reproducibility**: The same test cases can be loaded across different evaluation runs, ensuring consistent comparisons between agent versions.
- **Versioning**: Datasets can be versioned and tracked alongside MLflow experiments, providing a complete audit trail.
- **Collaboration**: Team members can share named datasets, avoiding duplication and drift in test definitions.

## Use with Other Evaluations

Persisted test cases are not limited to conversation simulation. They can be used with any `mlflow.genai.evaluate()` call that accepts a dataset as the `data` parameter, enabling the same test suite to drive both single-turn and multi-turn evaluations. ^[conversation-simulation-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) — Core concept for structured test data.
- [ConversationSimulator](/concepts/conversationsimulator.md) — Uses test cases to simulate multi-turn dialogues.
- generate_test_cases — Extracts test cases from existing conversation sessions.
- [Reproducible Testing](/concepts/mlflow-evaluation-dataset-for-reproducible-testing.md) — General practice of persisting evaluation artifacts.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for runs, datasets, and evaluation results.

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
