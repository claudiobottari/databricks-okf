---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7326aaff102e84a03c61ca8ab95087968a3e72e3a836e43d1f204ac0e966f2a3
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-analysis-and-debugging-with-genie-code
    - Debugging with Genie Code and Trace Analysis
    - TAADWGC
  citations:
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
title: Trace Analysis and Debugging with Genie Code
description: Genie Code capability to investigate failing traces, find errors, examine span trees, pinpoint root causes, analyze latency, and identify bottlenecks in an agent's execution flow.
tags:
  - observability
  - debugging
  - tracing
  - genai
timestamp: "2026-06-18T12:29:03.591Z"
---

# Trace Analysis and Debugging with Genie Code

**Trace Analysis and Debugging with Genie Code** refers to using the natural-language interface of Genie Code within MLflow to investigate, diagnose, and understand the behavior of GenAI agents at the level of individual execution traces. Instead of writing queries or manually navigating UI tabs, you can ask conversational questions about traces, span hierarchies, errors, latency, token usage, and root causes. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Overview

Genie Code has read access to everything in an [MLflow Experiment](/concepts/mlflow-experiment.md), including traces, prompts, datasets, evaluation runs, scorers, and labeling sessions. For trace analysis specifically, you can explore the full span tree of any trace — inspecting inputs, outputs, metadata, and token usage at every step — all through a chat interface. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Capabilities for Trace Analysis

Genie Code supports the following trace-related tasks:

- **Investigate failing traces** – Find traces that contain errors, examine their span trees, and pinpoint the exact step where a failure occurred.
- **Analyze latency and bottlenecks** – Compute latency percentiles (P50, P95, P99) across traces, identify slow spans, and understand where time is spent in the agent's execution flow.
- **Examine span hierarchies** – Deep-dive into any trace to inspect its full span hierarchy, including inputs, outputs, metadata, and token usage at every level.
- **Pattern discovery** – Identify common failure patterns, such as when the retriever returns no results but the agent still attempts to answer, or when users express frustration in conversations.
- **Token consumption analysis** – Determine which spans consume the most tokens across all traces.

These capabilities are part of the broader observability and evaluation feature set, which also includes metrics and performance tracking, quality evaluation with LLM judges, labeling review, prompt registry browsing, and instrumentation guidance. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Example Questions

Genie Code can process natural-language questions such as:

- “Help me discover issues with my agent's tool calling in the traces for this experiment over the last 3 hours”
- “Which spans consume the most tokens across all my traces?”
- “Find traces where the retriever returned no results but the agent still tried to answer”
- “Identify cases where users get frustrated in the conversations with my agent”
- “Which sessions have the lowest user feedback scores, and what went wrong in those conversations?”
- “What are the most common failure patterns in my traces this past week, and what scorers should I add to catch them?”

These questions demonstrate how Genie Code translates high-level debugging needs into actionable insights without requiring manual query construction. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## How to Access

While viewing an experiment in the MLflow UI, click the Genie Code icon in the top‑right corner of your workspace to open the chat interface. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Requirements

To use Genie Code for trace analysis and debugging, your workspace must have:

- Partner‑powered AI features enabled for both the account and workspace.
- The workspace located in a supported region (Genie Code is a Designated Service that uses Geos to manage data residency). ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying observability system that captures and stores traces.
- GenAI Agent Evaluation – Evaluating agent quality using judges and human feedback.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for traces, runs, and evaluation data.
- Observability and Debugging – Broader practices for monitoring and improving GenAI agents.
- [Instrumentation Guidance](/concepts/mlflow-instrumentation-guidance.md) – Genie Code can help set up tracing with `autolog()`, `@mlflow.trace`, or manual spans.

## Sources

- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md

# Citations

1. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
