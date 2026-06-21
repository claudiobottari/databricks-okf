---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a8bec529bddf88ec8d5cd6530a01873892f51a9e97f38c799123b76f28f1e2af
  pageDirectory: concepts
  sources:
    - evaluate-conversations-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-turn-assessment-storage
    - MAS
  citations:
    - file: evaluate-conversations-databricks-on-aws.md
title: Multi-turn Assessment Storage
description: Design pattern where multi-turn assessments are stored on the first trace (chronologically) in each session to ensure stability and easy retrieval.
tags:
  - evaluation
  - data-storage
  - mlflow
timestamp: "2026-06-18T12:12:41.938Z"
---

# Multi-turn Assessment Storage

**Multi-turn Assessment Storage** refers to how conversation-level evaluation results are stored and organized in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) when assessing multi-turn conversations rather than individual turns. This storage design ensures stability, discoverability, and efficient display of conversation metrics in the MLflow UI.

## Storage Location

Multi-turn assessments are stored on the **first trace** (chronologically) in each conversation session. This design choice ensures that assessments remain stable even as new turns are added to a conversation, and allows users to easily find conversation-level assessments by looking at session start traces.^[evaluate-conversations-databricks-on-aws.md]

## Assessment Metadata

Each multi-turn assessment includes metadata identifying it as conversation-level, including:

- `session_id`: The session ID linking the assessment to the full conversation

This metadata enables the Sessions UI to efficiently display conversation metrics and allows users to trace back from an assessment to the complete conversation it evaluates.^[evaluate-conversations-databricks-on-aws.md]

## Rationale for Storage Design

The decision to store assessments on the first trace rather than the last trace or as a separate entity is driven by three key requirements:^[evaluate-conversations-databricks-on-aws.md]

1. **Stability**: Assessments remain consistent even as new turns are added to a conversation. Storing on the last trace would cause assessments to shift when new turns occur, potentially breaking references and comparisons.

2. **Discoverability**: Users can find conversation-level assessments by looking at session start traces, making it straightforward to locate and inspect evaluation results for any conversation.

3. **UI Efficiency**: The Sessions UI can efficiently query and display conversation metrics because assessments are predictably stored on the first trace of each session.

## Using Stored Assessments

### Retrieving Assessments

You can retrieve stored assessments using [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) APIs. To evaluate a specific session, use `mlflow.search_traces` with a filter string targeting the session ID:^[evaluate-conversations-databricks-on-aws.md]

```python
import mlflow

# Get traces for a specific session
traces = mlflow.search_traces(
    filter_string="tags.`mlflow.trace.session` = '<your-session-id>'",
    return_type="list",
)

# Evaluate the session
results = mlflow.genai.evaluate(
    data=traces,
    scorers=[ConversationCompleteness(), UserFrustration()],
)
```

### Retrieving Sessions

To retrieve complete sessions directly, use `mlflow.search_sessions`:^[evaluate-conversations-databricks-on-aws.md]

```python
# Get complete sessions (each session is a list of traces)
sessions = mlflow.search_sessions(
    locations=["<your-experiment-id>"],
    max_results=50,
)

# Flatten for evaluation
all_traces = [trace for session in sessions for trace in session]
```

## Related Concepts

- [Conversation Evaluation](/concepts/conversation-evaluation.md) — The broader practice of assessing multi-turn conversations
- [Multi-turn Judges](/concepts/multi-turn-judge.md) — LLM-based judges that evaluate conversation-level quality using the `{{ conversation }}` template variable
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The API used to run evaluations and store assessments
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Using multi-turn judges for continuous monitoring in production
- [Track Users and Sessions](/concepts/mlflow-user-and-session-tracking.md) — Instrumenting agents with session IDs for grouping traces
- [Conversation Simulation](/concepts/conversationsimulator.md) — Generating synthetic conversations for testing

## Sources

- evaluate-conversations-databricks-on-aws.md

# Citations

1. [evaluate-conversations-databricks-on-aws.md](/references/evaluate-conversations-databricks-on-aws-f530405b.md)
