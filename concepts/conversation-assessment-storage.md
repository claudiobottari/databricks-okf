---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 92a5accad3518e8ccbc68d136a6c4a3d7e34f7c7c13e7afbbebe98cbef285590
  pageDirectory: concepts
  sources:
    - evaluate-conversations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - conversation-assessment-storage
    - CAS
  citations:
    - file: evaluate-conversations-databricks-on-aws.md
title: Conversation Assessment Storage
description: The design principle of storing multi-turn assessment results on the first trace of each session to ensure stability when new turns are added.
tags:
  - mlflow
  - data-storage
  - evaluation
timestamp: "2026-06-19T10:23:25.462Z"
---

# Conversation Assessment Storage

**Conversation Assessment Storage** refers to how [MLflow](/concepts/mlflow.md) stores evaluation results from [Multi-turn Judges](/concepts/multi-turn-judges.md) that assess entire conversation sessions rather than individual turns. This storage design ensures that conversation-level metrics remain stable, discoverable, and efficiently displayable in the Sessions UI. ^[evaluate-conversations-databricks-on-aws.md]

## Storage Location

Multi-turn assessments are stored on the **first trace** (chronologically) in each session. This means all conversation-level scores and feedback from multi-turn judges are attached to the earliest trace of a session. ^[evaluate-conversations-databricks-on-aws.md]

## Design Benefits

Storing assessments on the first trace provides several advantages:

- **Stability**: Assessments remain unchanged even as new turns are added to a conversation, because the first trace is never replaced. ^[evaluate-conversations-databricks-on-aws.md]
- **Discoverability**: Users can easily find conversation-level assessments by looking at the traces that begin each session. ^[evaluate-conversations-databricks-on-aws.md]
- **UI efficiency**: The Sessions UI can quickly retrieve and display conversation metrics without aggregating across multiple traces. ^[evaluate-conversations-databricks-on-aws.md]

## Metadata

Each multi-turn assessment includes metadata that identifies it as conversation-level:

- `session_id`: The session ID that links the assessment to the full conversation. ^[evaluate-conversations-databricks-on-aws.md]

This metadata allows the system to associate the stored assessment with the correct session and to distinguish conversation-level evaluations from per-turn evaluations. ^[evaluate-conversations-databricks-on-aws.md]

## Related Concepts

- [Multi-turn evaluation](/concepts/multi-turn-conversation-evaluation.md) – The process of assessing entire conversation sessions.
- [Multi-turn Judges](/concepts/multi-turn-judges.md) – LLM-based scorers that evaluate across multiple turns.
- Session ID – The trace tag used to group individual turns into a conversation.
- [[MLflow Trace|MLflow Traces]] – The tracing system that captures individual agent calls.
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Using multi-turn judges in continuous production monitoring.

## Sources

- evaluate-conversations-databricks-on-aws.md

# Citations

1. [evaluate-conversations-databricks-on-aws.md](/references/evaluate-conversations-databricks-on-aws-f530405b.md)
