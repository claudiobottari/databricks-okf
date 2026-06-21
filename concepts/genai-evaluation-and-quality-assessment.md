---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b887c7fabb907ac37bb0e5322f68f2dfb7065d0b0f82db821e6545c8204af619
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genai-evaluation-and-quality-assessment
    - Quality Assessment and GenAI Evaluation
    - GEAQA
    - Quality and Evaluations
  citations:
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
title: GenAI Evaluation and Quality Assessment
description: Reviewing assessment scores from human feedback, LLM judges, and programmatic checks; inspecting evaluation datasets and scorers for GenAI agents
tags:
  - evaluation
  - quality
  - genai
  - mlflow
timestamp: "2026-06-19T18:58:30.812Z"
---

# GenAI Evaluation and Quality Assessment

**GenAI Evaluation and Quality Assessment** refers to the systematic process of measuring, testing, and monitoring the performance, safety, and reliability of generative AI applications. Within MLflow, this capability is primarily supported by **Genie Code**, a natural language interface that provides read access to traces, prompts, datasets, evaluation runs, scorers, and labeling sessions – enabling exploration of observability and evaluation data conversationally. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Overview

Genie Code allows developers to review assessment scores from human feedback, [LLM Judges](/concepts/llm-judges.md), and [programmatic checks](/concepts/programmatic-and-batch-evaluation-patterns.md), inspect evaluation datasets, check registered scorers and their configurations, and get help setting up `mlflow.genai.evaluate()` with the right scorers. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Capabilities

Genie Code assists with a wide range of observability and evaluation tasks: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- **Trace analysis and debugging** — Investigate failing traces, find errors, examine span trees, pinpoint root causes, analyze latency, and identify bottlenecks. Deep‑dive into any trace to inspect the full span hierarchy, including inputs, outputs, metadata, and token usage at every step.
- **Metrics and performance** — Compute latency percentiles (P50/P95/P99), track error rates and throughput over time, analyze token usage patterns and costs, and compare performance across different time periods or filters.
- **Quality and evaluations** — Review assessment scores from human feedback, LLM judges, and programmatic checks. Inspect evaluation datasets, check registered scorers and their configurations, and get help setting up `mlflow.genai.evaluate()` with the right scorers.
- **Labeling and review** — View labeling sessions and who is assigned to review traces, and inspect labeling schemas to understand feedback criteria such as ratings, comments, and expectations.
- **Prompt registry** — Browse prompts in Unity Catalog, view templates, versions, and aliases.
- **Instrumentation guidance** — Get help adding tracing to code with `autolog()`, `@mlflow.trace`, or manual spans, with runnable code snippets.

## Example Questions

Developers can ask Genie Code questions such as: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- "Help me discover issues with my agent's tool calling in the traces for this experiment over the last 3 hours"
- "Identify cases where users get frustrated in the conversations with my agent"
- "Which sessions have the lowest user feedback scores, and what went wrong in those conversations?"
- "What are the most common failure patterns in my traces this past week, and what scorers should I add to catch them?"
- "Which spans consume the most tokens across all my traces?"
- "Find traces where the retriever returned no results but the agent still tried to answer"
- "Help me set up evaluation for my RAG agent with the right scorers"

## Requirements

To use Genie Code for agent observability and evaluation, the workspace needs: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- Partner-powered AI features enabled for both the account and workspace.
- The workspace must be in a supported region. Genie Code is a Designated Service that uses Geos to manage data residency.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — GenAI observability and end-to-end trace collection
- Evaluate and Monitor AI Agents — Setting up evaluation and monitoring for GenAI agents
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers for quality assessment
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying scorers for continuous quality monitoring
- Human Feedback Alignment — Improving judge accuracy with expert annotations

## Sources

- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md

# Citations

1. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
