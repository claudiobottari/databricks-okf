---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c179f4207f036b001f7c7b57e3975958b4ffe868580a7006c382008d83b0d9a3
  pageDirectory: concepts
  sources:
    - evaluate-conversations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - conversation-assessment-storage-on-first-trace
    - CASOFT
  citations:
    - file: evaluate-conversations-databricks-on-aws.md
title: Conversation Assessment Storage on First Trace
description: Design pattern where multi-turn assessment results are stored on the first (chronologically earliest) trace in each session to ensure stability and efficient UI display.
tags:
  - mlflow
  - architecture
  - evaluation
  - storage
timestamp: "2026-06-19T18:41:49.770Z"
---

# Conversation Assessment Storage on First Trace

**Conversation Assessment Storage on First Trace** is a design principle in MLflow's multi-turn evaluation system where conversation-level assessments are stored on the chronologically first trace in each session. This storage strategy ensures stability, discoverability, and efficient display of conversation metrics in the MLflow Sessions UI.

## Overview

When evaluating multi-turn conversations using [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md), the system produces conversation-level assessments through multi-turn judges. Instead of duplicating assessment data across every turn in a conversation, MLflow stores these assessments exclusively on the first trace (chronologically) of each session. ^[evaluate-conversations-databricks-on-aws.md]

This approach applies to both pre-generated conversation evaluation and simulated conversation evaluation workflows.

## Design Rationale

The storage design ensures three key outcomes:

- **Stability**: Assessments remain stable even as new turns are added to a conversation. Because the assessment is stored on the first trace, adding subsequent turns does not alter where the conversation-level metrics are recorded. ^[evaluate-conversations-databricks-on-aws.md]
- **Discoverability**: You can easily find conversation-level assessments by looking at session start traces. All conversation-level metrics are concentrated on a single trace per session. ^[evaluate-conversations-databricks-on-aws.md]
- **Efficient UI display**: The Sessions UI can efficiently display conversation metrics because it only needs to examine the first trace per session to retrieve aggregated assessment data. ^[evaluate-conversations-databricks-on-aws.md]

## Assessment Metadata

Assessments stored on the first trace include metadata that identifies them as conversation-level:

- `session_id`: The session ID linking the assessment to the full conversation. This allows the system and users to associate the stored assessment with the entire multi-turn session. ^[evaluate-conversations-databricks-on-aws.md]

## Related Concepts

- [Multi-turn Conversation Evaluation](/concepts/multi-turn-conversation-evaluation.md) – The overarching workflow for assessing entire conversation sessions.
- Session ID Tagging – The mechanism for grouping individual traces into conversation sessions using the `mlflow.trace.session` tag.
- Trace Storage – General architecture for storing individual AI agent traces in MLflow.
- [LLM Judges](/concepts/llm-judges.md) – The evaluation components that produce conversation-level assessments.
- [Conversation Simulation](/concepts/conversation-simulation.md) – A workflow that generates synthetic conversations for evaluation.

## Sources

- evaluate-conversations-databricks-on-aws.md

# Citations

1. [evaluate-conversations-databricks-on-aws.md](/references/evaluate-conversations-databricks-on-aws-f530405b.md)
