---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: da5a7675085fa16a352d7386a3f370d1ba0594c50a3ae279fa24936d12370fc3
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-turn-scorers-in-mlflow
    - MSIM
    - Built-in Scorers in MLflow
    - Multi-turn Scorers
    - Multi-turn scorers
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: Multi-turn Scorers in MLflow
description: Evaluation scorers that assess conversational AI agents across multiple turns, such as ConversationCompleteness and Safety, applicable within the conversation simulation evaluation workflow.
tags:
  - mlflow
  - evaluation
  - scorers
  - conversational-ai
timestamp: "2026-06-18T11:10:06.501Z"
---

# Multi-turn Scorers in MLflow

**Multi-turn Scorers** are a category of [scorers (MLflow)](/concepts/scorers-mlflow-genai.md) in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that evaluate an entire multi-turn conversation as a single unit, rather than scoring each turn independently. They are designed for use with [Conversation Simulation](/concepts/conversationsimulator.md) and the `mlflow.genai.evaluate()` API.^[conversation-simulation-databricks-on-aws.md]

## Overview

When evaluating a conversational AI agent, you may want to assess properties that only make sense across the full dialogue — such as whether the user’s goal was achieved, whether the conversation remained coherent, or whether harmful content emerged over multiple turns. Multi-turn scorers accomplish this by receiving the complete conversation trace and returning a single [Feedback (MLflow)|Feedback](/concepts/mlflow-feedback-object.md) object.^[conversation-simulation-databricks-on-aws.md]

This contrasts with **single-turn scorers**, which are applied independently to each user-assistant exchange. In `mlflow.genai.evaluate()`, you can combine both types in the same evaluation run.^[conversation-simulation-databricks-on-aws.md]

## Example: ConversationCompleteness

The predefined `ConversationCompleteness` scorer is a built-in multi-turn scorer. The following example shows it used alongside the single-turn `Safety` scorer:^[conversation-simulation-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers import ConversationCompleteness, Safety

results = mlflow.genai.evaluate(
    data=simulator,
    predict_fn=predict_fn,
    scorers=[
        ConversationCompleteness(),  # Multi-turn scorer
        Safety(),                     # Single-turn scorer (applied to each turn)
    ],
)
```

When the evaluation runs, `ConversationCompleteness` examines the simulated conversation as a whole, while `Safety` evaluates each turn individually.^[conversation-simulation-databricks-on-aws.md]

## Usage with Conversation Simulation

Multi-turn scorers are particularly useful when paired with [ConversationSimulator](/concepts/conversationsimulator.md). After defining test cases and an agent function, you pass the simulator as the `data` argument and list multi-turn scorers in the `scorers` parameter. The simulation generates multiple turns, and the multi-turn scorer assesses the resulting session.^[conversation-simulation-databricks-on-aws.md]

For example, a multi-turn scorer like `ConversationCompleteness` can determine whether the simulated user’s goal was accomplished by the end of the conversation, a judgement that requires the full dialogue context.^[conversation-simulation-databricks-on-aws.md]

## Related Concepts

- [Conversation Simulation](/concepts/conversationsimulator.md) — Synthetic generation of multi-turn dialogues for testing
- Single-turn Scorers — Per-turn evaluation scorers
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The evaluation framework that supports multi-turn scorers
- [Predefined Scorers](/concepts/mlflow-genai-predefined-scorers.md) — Built-in scorers like `ConversationCompleteness`, `Safety`, and `User Frustration`
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Persisting test cases for reproducible evaluation

## Sources

- `conversation-simulation-databricks-on-aws.md`

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
