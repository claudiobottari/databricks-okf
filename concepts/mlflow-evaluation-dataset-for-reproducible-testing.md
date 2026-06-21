---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b60d9523a539f765e6012e5fe272b3b20a089469589189be95e6c3c55c5edf61
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-evaluation-dataset-for-reproducible-testing
    - MEDFRT
    - Reproducible Testing
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: MLflow Evaluation Dataset for Reproducible Testing
description: A mechanism to persist test cases as MLflow Evaluation Datasets using create_dataset and get_dataset, enabling reproducible conversation simulation runs.
tags:
  - mlflow
  - reproducibility
  - testing
timestamp: "2026-06-18T14:44:26.175Z"
---

# MLflow Evaluation Dataset for Reproducible Testing

**MLflow Evaluation Dataset for Reproducible Testing** refers to a structured dataset mechanism within MLflow that persists test cases, scenarios, and evaluation inputs for consistent, repeatable testing of GenAI agents and ML models. By storing evaluation data as versioned datasets, teams can ensure that the same test cases are applied across different model or agent configurations, enabling reliable [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) and regression testing.

## Overview

An MLflow Evaluation Dataset provides a reproducible foundation for testing by capturing inputs, expected outputs, and metadata that evaluation workflows reference. Instead of defining test cases inline within scripts or relying on ad-hoc data generation, teams can create, version, and retrieve evaluation datasets programmatically. This approach supports systematic evaluation, collaborative testing, and auditability of quality assessments.^[conversation-simulation-databricks-on-aws.md]

## Creating and Populating a Dataset

Evaluation datasets are created using the `mlflow.genai.datasets` module. The `create_dataset()` function initializes a named dataset, and `merge_records()` populates it with evaluation records. Each record contains an `inputs` field that holds the test case data.^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.datasets import create_dataset

dataset = create_dataset(name="conversation_test_cases")
dataset.merge_records(
    [
        {"inputs": {"goal": "Successfully configure experiment tracking"}},
        {"inputs": {"goal": "Debug a deployment error", "persona": "Senior engineer"}},
    ]
)
```

Records can include custom fields beyond `inputs`, such as `persona` or `context`, depending on the evaluation scenario.^[conversation-simulation-databricks-on-aws.md]

## Retrieving a Stored Dataset

Previously created datasets can be retrieved by name for reuse across evaluation runs:

```python
from mlflow.genai.datasets import get_dataset

dataset = get_dataset(name="conversation_test_cases")
```

This allows teams to share standardized test datasets across experiments, ensuring consistency in evaluation criteria.^[conversation-simulation-databricks-on-aws.md]

## Use with Conversation Simulation

Evaluation datasets integrate with [ConversationSimulator](/concepts/conversationsimulator.md) for reproducible [Conversation Simulation](/concepts/conversation-simulation.md). Test cases stored in a dataset can be passed directly to the simulator, enabling systematic multi-turn conversation testing with consistent goals and personas:^[conversation-simulation-databricks-on-aws.md]

```python
from mlflow.genai.simulators import ConversationSimulator

dataset = get_dataset(name="conversation_test_cases")
simulator = ConversationSimulator(test_cases=dataset)
```

This pattern ensures that test scenarios remain stable across iterations, supporting reliable comparison of agent behavior changes.^[conversation-simulation-databricks-on-aws.md]

## Benefits for Reproducible Testing

- **Versioned test data**: Datasets can be versioned, enabling rollback to previous test suites for regression analysis.
- **Shared standards**: Teams can maintain centralized evaluation datasets that all members use, reducing inconsistency in testing practices.
- **Audit trail**: Persistent datasets provide a record of what inputs were used for specific evaluation runs, supporting compliance and debugging.
- **Integration with evaluation workflows**: Datasets feed directly into `mlflow.genai.evaluate()`, the [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) API, for automated scoring and quality assessment.^[conversation-simulation-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The core API for running evaluations against models and agents
- [Conversation Simulation](/concepts/conversation-simulation.md) — Generating synthetic multi-turn conversations for testing
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing agent behavior using consistent evaluation data
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers used with evaluation datasets
- Evaluation Dataset Persistence — Managing dataset lifecycle and versioning
- Reproducible ML — Broader principles of reproducibility in machine learning workflows

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
