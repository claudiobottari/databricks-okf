---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d8bad59ab0c9ff886408b2078f982f7f2a5f241fd664e78795118707020e9d1
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-analysis
    - MTA
    - Trace Data Analysis
    - Trace-based analysis
  citations:
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
title: MLflow Trace Analysis
description: Capability to investigate failing traces, examine span trees, pinpoint root causes, analyze latency, and identify bottlenecks in GenAI agent execution
tags:
  - tracing
  - debugging
  - mlflow
  - genai
timestamp: "2026-06-19T18:58:37.017Z"
---

# MLflow Trace Analysis

**MLflow Trace Analysis** is the process of investigating and debugging the execution traces of AI agents and applications instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md). It encompasses examining the full span hierarchy of a trace—including inputs, outputs, metadata, and token usage at every step—to identify root causes of failures, performance bottlenecks, and other issues in an agent's execution flow. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Overview

When an AI application is instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md), every invocation generates a **trace** — a record of the complete execution path. A trace is composed of one or more **spans**, where each span represents a discrete unit of work (such as an LLM call, a tool invocation, or a retrieval step). Analysing these traces allows developers to see exactly what happened during each step of an agent's reasoning and tool-calling process. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Key Capabilities

Trace analysis enables several categories of investigation:

- **Failure analysis**: Find failing traces, examine the span tree, pinpoint the exact span where an error occurred, and understand its root cause. This is essential for debugging agentic applications where errors may propagate through multiple tool calls. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- **Latency and performance analysis**: Inspect individual span durations, identify bottlenecks in the execution flow, and compute aggregate latency percentiles (P50/P95/P99) across traces. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- **Token and cost analysis**: Examine token usage at every step of a trace, including per-span consumption patterns, to understand which parts of the pipeline are most expensive or consume the most context window. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- **End-to-end observability**: Deep-dive into any trace to inspect its full span hierarchy, including all inputs and outputs at each step. This allows you to see not just the final answer, but the intermediate reasoning, tool call results, and retrieved context that led to it. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Common Analysis Patterns

Common questions that trace analysis helps answer include:

- "Which spans consume the most tokens across all my traces?" ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- "Find traces where the retriever returned no results but the agent still tried to answer." ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- "Identify cases where users get frustrated in the conversations with my agent." ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- "What are the most common failure patterns in my traces this past week?" ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Natural Language Interface: Genie Code

Within the [MLflow](/concepts/mlflow.md) experiment context, [Genie Code](/concepts/genie-code.md) provides a natural language interface for trace analysis. Instead of writing queries or navigating multiple UI pages, you can ask questions in plain language about your traces and get answers grounded in the experiment's observability data. This includes access to traces, prompts, datasets, evaluation runs, scorers, and labeling sessions. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

### Example Trace Analysis Queries

Genie Code can answer questions like:
- "Help me discover issues with my agent's tool calling in the traces for this experiment over the last 3 hours." ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- "Which sessions have the lowest user feedback scores, and what went wrong in those conversations?" ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The foundation for capturing traces in AI applications.
- Spans — The building blocks of a trace; each span is a unit of work.
- Span tree — The hierarchical structure of spans within a trace, showing parent-child relationships.
- [Token usage](/concepts/mlflow-token-usage-tracking.md) — A key metric tracked at the span level.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The broader framework for AI agent observability and evaluation.
- Evaluation and monitoring — The practice of assessing agent quality, which relies on trace data.
- [Root cause analysis](/concepts/inference-tables-for-root-cause-analysis.md) — A primary goal of trace analysis.
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluating agents using traces and scorers.

## Sources

- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md

# Citations

1. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
