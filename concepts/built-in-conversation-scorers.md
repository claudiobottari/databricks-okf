---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0d03d0900849a9ee40d819d710ef02a02552b42380fd888e3522341213994c3c
  pageDirectory: concepts
  sources:
    - evaluate-conversations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - built-in-conversation-scorers
    - BCS
  citations:
    - file: evaluate-conversations-databricks-on-aws.md
title: Built-in Conversation Scorers
description: Predefined multi-turn judges like ConversationCompleteness, UserFrustration, and Safety provided by MLflow for evaluating conversation quality without custom development.
tags:
  - mlflow
  - scorers
  - evaluation
  - llm-judges
timestamp: "2026-06-19T18:42:00.535Z"
---

# Built-in Conversation Scorers

**Built-in Conversation Scorers** are pre-defined [Multi-turn Judges](/concepts/multi-turn-judge.md) provided by [MLflow](/concepts/mlflow.md) for evaluating entire conversation sessions rather than individual turns. They are designed to assess conversational AI systems on session-level quality dimensions such as user frustration, conversation completeness, and safety, which emerge only over multiple interactions. ^[evaluate-conversations-databricks-on-aws.md]

## Overview

Traditional single-turn evaluation evaluates each agent response independently, but conversational agents require session-level evaluation to capture phenomena like user frustration patterns, whether all questions were answered, knowledge retention across turns, and dialogue coherence. Built-in conversation scorers address these needs by analyzing the complete conversation history grouped by session ID. ^[evaluate-conversations-databricks-on-aws.md]

Multi-turn judges (scorers) can be used in two contexts:

- **Offline evaluation** during development, as described in the evaluation documentation.
- **Continuous monitoring** in production by attaching judges to [Production Monitoring](/concepts/production-monitoring.md) pipelines. ^[evaluate-conversations-databricks-on-aws.md]

> **Note**: Multi-turn evaluation is an experimental feature. The API and behavior may change in future releases. ^[evaluate-conversations-databricks-on-aws.md]

## Available Built-in Scorers

MLflow provides several built-in multi-turn judges. Examples mentioned in the documentation include:

- **`ConversationCompleteness`** – Assesses whether the agent answered all user questions by the end of the conversation.
- **`UserFrustration`** – Detects whether the user became frustrated and whether the frustration was resolved.
- **`Safety`** – Evaluates the conversation for harmful or unsafe content.

For the complete list of available built-in multi-turn judges and detailed documentation, see the [MLflow predefined scorers documentation](/concepts/mlflow-genai-predefined-scorers.md) (linked in the source). ^[evaluate-conversations-databricks-on-aws.md]

## Prerequisites

To use built-in conversation scorers, you must:

- Install MLflow 3.10.0 or later: `pip install --upgrade 'mlflow[databricks]>=3.10'`.
- Instrument your agent to tag traces with session IDs under the tag `mlflow.trace.session`. This groups individual traces into conversation sessions. ^[evaluate-conversations-databricks-on-aws.md]

## Usage Example

The following example evaluates pre-generated conversations by retrieving traces from an experiment and passing them to `mlflow.genai.evaluate` with built-in scorers. MLflow automatically groups traces by session ID.

```python
from mlflow.genai.scorers import ConversationCompleteness, UserFrustration

# Get traces from your experiment
traces = mlflow.search_traces(
    filter_string="attributes.status = 'OK'",
    return_type="list",
)

# Evaluate conversations using built-in scorers
results = mlflow.genai.evaluate(
    data=traces,
    scorers=[
        ConversationCompleteness(),
        UserFrustration(),
    ],
)
```

^[evaluate-conversations-databricks-on-aws.md]

You can also retrieve complete sessions directly with `mlflow.search_sessions` and flatten them for evaluation. ^[evaluate-conversations-databricks-on-aws.md]

## How Assessments Are Stored

Multi-turn assessments are stored on the **first trace** (chronologically) in each session. This ensures that assessments remain stable as new turns are added, and conversation-level metrics can be efficiently displayed in the Sessions UI. Assessments include metadata such as the `session_id` to link them to the full conversation. ^[evaluate-conversations-databricks-on-aws.md]

## Related Concepts

- [Multi-turn Judges](/concepts/multi-turn-judge.md) – The underlying LLM judge mechanism for conversation evaluation.
- [ConversationSimulator](/concepts/conversationsimulator.md) – Generates synthetic conversations for evaluation.
- [Custom Judges](/concepts/custom-judges.md) – Create your own multi-turn judges using `make_judge` and the `{{ conversation }}` template variable.
- [Production Monitoring](/concepts/production-monitoring.md) – Use multi-turn judges for continuous evaluation in production.
- [Track users and sessions](/concepts/mlflow-user-and-session-tracking.md) – How to instrument agents with session IDs.

## Sources

- evaluate-conversations-databricks-on-aws.md

# Citations

1. [evaluate-conversations-databricks-on-aws.md](/references/evaluate-conversations-databricks-on-aws-f530405b.md)
