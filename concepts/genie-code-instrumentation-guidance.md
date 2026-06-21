---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a4b5ad69bdb1849e5688c574cf97f05289ef9a8ff7f6e493a66ceb30a1330afc
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-code-instrumentation-guidance
    - GCIG
  citations:
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
title: Genie Code Instrumentation Guidance
description: Genie Code provides help adding tracing to code with autolog(), @mlflow.trace, or manual spans, including runnable code snippets that can be pasted into Databricks notebooks.
tags:
  - instrumentation
  - tracing
  - mlflow
  - genai
timestamp: "2026-06-18T12:29:19.271Z"
---

Here is the wiki page for "Genie Code Instrumentation Guidance", written based solely on the provided source material.

---

## Genie Code Instrumentation Guidance

**Genie Code Instrumentation Guidance** is a feature within [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that provides a natural language interface for adding tracing, error handling, and debugging instrumentation to your code. It is part of the broader [Genie Code](/concepts/genie-code.md) assistant, which has read access to all observability data in an experiment, including traces, prompts, datasets, evaluation runs, scorers, and labeling sessions. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Overview

When you need help adding tracing to your GenAI application, Genie Code can provide runnable code snippets that you can paste directly into Databricks notebooks. The guidance covers instrumentation techniques such as `autolog()`, `@mlflow.trace`, and manual spans. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Capabilities

Specific instrumentation guidance tasks that Genie Code can assist with include:

- **Adding tracing to your code** with `autolog()`, `@mlflow.trace`, or manual spans, with runnable code snippets you can paste directly into Databricks notebooks. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Trace analysis and debugging**: Investigating failing traces, finding errors, examining span trees, pinpointing root causes, analyzing latency, and identifying bottlenecks in your agent's execution flow. Deep-dive into any trace to inspect its full span hierarchy, including inputs, outputs, metadata, and token usage at every step. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Getting help setting up `mlflow.genai.evaluate()`** with the right scorers for your use case. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Metrics and performance**: computing latency percentiles, tracking error rates and throughput, analyzing token usage patterns and costs. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Example Questions

Genie Code can answer questions like:

- "Help me discover issues with my agent's tool calling in the traces for this experiment over the last 3 hours"
- "Identify cases where users get frustrated in the conversations with my agent"
- "Which sessions have the lowest user feedback scores, and what went wrong in those conversations?"
- "What are the most common failure patterns in my traces this past week, and what scorers should I add to catch them?"
- "Which spans consume the most tokens across all my traces?"
- "Find traces where the retriever returned no results but the agent still tried to answer"
- "Help me set up evaluation for my RAG agent with the right scorers"

^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Requirements

To use Genie Code for agent observability and evaluation, your workspace needs the following:

- Partner-powered AI features enabled for both the account and workspace. See [Partner-Powered AI Features](/concepts/partner-powered-ai-features-on-databricks.md).
- Your workspace must be in a supported region. Genie Code is a Designated Service that uses Geos to manage data residency. See Geo Availability of Genie Code Features.

^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The core observability framework for GenAI applications
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The evaluation module for AI agents
- [Autolog](/concepts/mlflow-autologging.md) — Automatic instrumentation of MLflow runs
- [MLflow trace decorator](/concepts/mlflow-trace-decorator.md) — The `@mlflow.trace` decorator for manual span creation
- [GenAI Agent Observability](/concepts/genai-agent-observability.md) — The broader practice of monitoring and debugging AI agents
- [Genie Code](/concepts/genie-code.md) — The full Genie Code assistant

## Sources

- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md

# Citations

1. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
