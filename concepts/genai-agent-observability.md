---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3261ea04defb3b3efa401af88b57e2d46731a5e6967678f0a940add71d63e38d
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genai-agent-observability
    - GAO
    - Agent Observability
    - GenAI Agents
  citations:
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
title: GenAI Agent Observability
description: The practice of monitoring, tracing, debugging, and evaluating GenAI agent behavior using MLflow tools
tags:
  - observability
  - genai
  - mlflow
  - monitoring
timestamp: "2026-06-19T18:58:15.714Z"
---

# GenAI Agent Observability

**GenAI Agent Observability** refers to the practice of monitoring, debugging, and improving the behavior of GenAI applications — such as conversational agents, RAG pipelines, and tool‑using systems — by examining traces, metrics, evaluations, and user feedback. On the Databricks platform, this capability is surfaced through [MLflow 3 for GenAI](/concepts/mlflow-3-for-genai.md) and is specifically powered by the [Genie Code](/concepts/genie-code.md) natural language interface. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

GenAI Agent Observability gives practitioners conversational read access to everything stored in an [MLflow Experiment](/concepts/mlflow-experiment.md): traces, prompts, datasets, evaluation runs, scorers, and labeling sessions. Instead of writing queries or navigating multiple UI pages, users can interact with their observability data using plain English. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Capabilities

The observability platform supports a wide range of tasks: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- **Trace analysis and debugging** – Investigate failing traces, find errors, examine span trees, pinpoint root causes, analyze latency, and identify bottlenecks in the agent’s execution flow. Deep‑dive into any trace to inspect its full span hierarchy, including inputs, outputs, metadata, and token usage at every step.
- **Metrics and performance** – Compute latency percentiles (P50/P95/P99), track error rates and throughput over time, analyze token usage patterns and costs, and compare performance across different time periods or filters.
- **Quality and evaluations** – Review assessment scores from human feedback, [LLM Judges](/concepts/llm-judges.md), and programmatic checks. Inspect evaluation datasets, check registered scorers and their configurations, and get help setting up `mlflow.genai.evaluate()` with the right scorers.
- **Labeling and review** – View labeling sessions and who is assigned to review traces; inspect labeling schemas to understand feedback criteria such as ratings, comments, and expectations.
- **Prompt registry** – Browse prompts in [Unity Catalog](/concepts/unity-catalog.md), view templates, versions, and aliases.
- **Instrumentation guidance** – Get help adding tracing to code with `autolog()`, `@mlflow.trace`, or manual spans, with runnable code snippets that can be pasted directly into Databricks notebooks.

## Example questions

Users can ask natural language questions such as: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- “Help me discover issues with my agent’s tool calling in the traces for this experiment over the last 3 hours”
- “Identify cases where users get frustrated in the conversations with my agent”
- “Which sessions have the lowest user feedback scores, and what went wrong in those conversations?”
- “What are the most common failure patterns in my traces this past week, and what scorers should I add to catch them?”
- “Which spans consume the most tokens across all my traces?”
- “Find traces where the retriever returned no results but the agent still tried to answer”
- “Help me set up evaluation for my RAG agent with the right scorers”

## Requirements

To use GenAI Agent Observability (via Genie Code), the workspace must meet the following conditions: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- Partner-powered AI features enabled for both the account and workspace.
- The workspace must be in a supported region; Genie Code is a Designated Service that uses Geos to manage data residency.

## Related concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying mechanism for end‑to‑end observability of GenAI applications.
- GenAI Evaluation and Monitoring – Setting up evaluation and monitoring for AI agents.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit that stores traces, metrics, and evaluation data.
- [LLM Judges](/concepts/llm-judges.md) – Automated evaluators used in quality assessments.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) for prompts and other governance objects.

## Sources

- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md

# Citations

1. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
