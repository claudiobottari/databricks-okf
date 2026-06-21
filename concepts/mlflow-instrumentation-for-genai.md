---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 97a6531cc345594285c74f559a11b88b9d78406b8e0b1a6378f3cf058abb223d
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-instrumentation-for-genai
    - MIFG
  citations:
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
title: MLflow Instrumentation for GenAI
description: Methods for adding tracing to GenAI code using autolog(), @mlflow.trace decorator, or manual span creation with runnable code snippets
tags:
  - instrumentation
  - tracing
  - mlflow
  - genai
timestamp: "2026-06-19T18:58:45.339Z"
---

# MLflow Instrumentation for GenAI

**MLflow Instrumentation for GenAI** refers to the set of tools and practices that enable observability, debugging, and improvement of GenAI applications within [MLflow](/concepts/mlflow.md). Instrumentation covers adding tracing to code, collecting performance metrics, logging evaluation results, and managing prompts. A natural‑language interface called [Genie Code](/concepts/genie-code.md) assists users in performing these tasks conversationally. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Genie Code Overview

Genie Code provides a natural‑language interface for understanding, debugging, and improving GenAI applications within MLflow. It has read access to everything in an experiment — from traces, prompts, and datasets to evaluation runs, scorers, and labeling sessions — allowing users to explore observability and evaluation data without writing queries or navigating multiple UI pages. To access it, click the Genie Code icon in the top‑right of a workspace while viewing an experiment. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Instrumentation Capabilities

Genie Code helps with a wide range of instrumentation and evaluation tasks: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- **Trace analysis and debugging**: Investigate failing traces, find errors, examine span trees, pinpoint root causes, analyze latency, and identify bottlenecks. Users can deep‑dive into any trace to inspect its full span hierarchy, including inputs, outputs, metadata, and token usage at every step. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Metrics and performance**: Compute latency percentiles (P50/P95/P99), track error rates and throughput over time, analyze token usage patterns and costs, and compare performance across different time periods or filters. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Quality and evaluations**: Review assessment scores from human feedback, LLM judges, and programmatic checks. Inspect evaluation datasets, check registered scorers and their configurations, and get help setting up `mlflow.genai.evaluate()` with the right scorers. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Labeling and review**: View labeling sessions and who is assigned to review traces; inspect labeling schemas to understand feedback criteria such as ratings, comments, and expectations. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Prompt registry**: Browse prompts in [Unity Catalog](/concepts/unity-catalog.md), view templates, versions, and aliases. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Instrumentation guidance**: Get help adding tracing to code with `autolog()`, `@mlflow.trace`, or manual spans, with runnable code snippets that can be pasted directly into Databricks notebooks. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Example Questions

Users can ask Genie Code questions such as: "Help me set up evaluation for my RAG agent with the right scorers", "Which spans consume the most tokens across all my traces?", or "Find traces where the retriever returned no results but the agent still tried to answer." These questions illustrate how Genie Code supports both instrumentation setup and ongoing observability. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Requirements

To use Genie Code for agent observability and evaluation, the workspace must have partner‑powered AI features enabled for both the account and the workspace. Additionally, the workspace must be in a supported region; Genie Code is a Designated Service that uses Geos to manage data residency. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – End‑to‑end observability for GenAI applications.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – Setting up evaluation and monitoring for AI agents.
- [autolog](/concepts/mlflow-autologging.md) – Automatic tracing and logging in MLflow.
- @mlflow.trace – Decorator for adding custom tracing to functions.
- [Genie Code](/concepts/genie-code.md) – The natural‑language interface described above.
- [Prompt Registry](/concepts/prompt-registry.md) – Storage and versioning of prompts in Unity Catalog.

## Sources

- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md

# Citations

1. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
