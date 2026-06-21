---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f545ec860ef1843657abb98a57c7840bb714aca1b0c8fcc7e98849be1cb36d8d
  pageDirectory: concepts
  sources:
    - conversation-simulation-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - generate_test_cases-from-production-sessions
    - GFPS
  citations:
    - file: conversation-simulation-databricks-on-aws.md
title: generate_test_cases from Production Sessions
description: A utility function that extracts test case goals and personas from existing production conversation sessions to reflect real user behavior.
tags:
  - mlflow
  - testing
  - production
timestamp: "2026-06-18T14:44:23.563Z"
---

# generate_test_cases from Production Sessions

**`generate_test_cases`** is a function in the [`mlflow.genai.simulators`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/conversation-simulation) module that extracts goals and personas from existing production conversation sessions and returns a list of test cases suitable for use with [ConversationSimulator](/concepts/conversationsimulator.md). This enables teams to create realistic, data‑driven evaluation scenarios directly from real user interactions. ^[conversation-simulation-databricks-on-aws.md]

## Overview

Manually writing test cases for conversational AI agents can miss edge cases and may not reflect actual user behavior. `generate_test_cases` addresses this by programmatically deriving test scenarios from historical session data. The function takes a set of previously logged sessions (obtained via `mlflow.search_sessions()`) and distills each session into a structured test case containing a `goal` and optionally a `persona`. These test cases can then be fed directly into a `ConversationSimulator` to drive simulated conversations that mirror real‑world usage patterns. ^[conversation-simulation-databricks-on-aws.md]

## Usage

The typical workflow is:

1. **Fetch production sessions** using `mlflow.search_sessions()` with appropriate filters (e.g., experiment location, time range, max results).
2. **Generate test cases** by calling `generate_test_cases(sessions)`.
3. (Optional) **Persist** the generated test cases as an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) for reproducibility.
4. **Create a `ConversationSimulator`** with the generated test cases.
5. **Run evaluation** with `mlflow.genai.evaluate()`.

```python
import mlflow
from mlflow.genai.simulators import generate_test_cases, ConversationSimulator

# Get existing sessions from a production experiment
sessions = mlflow.search_sessions(
    locations=["<experiment-id>"],
    max_results=50,
)

# Generate test cases by extracting goals and personas from sessions
test_cases = generate_test_cases(sessions)

# Optional: save generated test cases as a dataset for reproducibility
from mlflow.genai.datasets import create_dataset
dataset = create_dataset(name="generated_scenarios")
dataset.merge_records([{"inputs": tc} for tc in test_cases])

# Use generated test cases with the simulator
simulator = ConversationSimulator(test_cases=test_cases)
```

^[conversation-simulation-databricks-on-aws.md]

## Best Practices

- **Select a representative sample.** When fetching sessions, choose a diverse set that covers common user intents, edge cases, and different user personas. The quality of the generated test cases depends on the input sessions. ^[conversation-simulation-databricks-on-aws.md]
- **Review and refine.** Automatically extracted goals and personas may need manual tweaking to ensure they are specific enough and free of bias. Consider editing the generated list before using it in production evaluation. ^[conversation-simulation-databricks-on-aws.md]
- **Version your test cases.** Persisting the generated test cases as an MLflow dataset allows you to reproduce evaluations exactly and track changes over time. ^[conversation-simulation-databricks-on-aws.md]

## Related Concepts

- [ConversationSimulator](/concepts/conversationsimulator.md) – The simulator that uses the generated test cases to produce multi‑turn conversations.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` function that orchestrates simulation and scoring.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Collecting and analyzing production sessions that serve as input to `generate_test_cases`.
- [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) – A mechanism to save and reuse test cases.
- [Custom Judges](/concepts/custom-judges.md) – LLM‑based scorers used to evaluate simulated conversations.

## Sources

- conversation-simulation-databricks-on-aws.md

# Citations

1. [conversation-simulation-databricks-on-aws.md](/references/conversation-simulation-databricks-on-aws-dcc14b07.md)
