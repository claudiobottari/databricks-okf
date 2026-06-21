---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3d67c80e6ff7c0a22ce9e6db003b031b0a016b1fefbba5ba5b96eab7c2e57a19
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-code
    - Genie
  citations:
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
    - file: concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
    - file: model-serving-observability-with-genie-code-databricks-on-aws.md
title: Genie Code
description: A natural language interface within Databricks/MLflow for conversational exploration of GenAI observability and evaluation data
tags:
  - databricks
  - genai
  - observability
  - mlflow
timestamp: "2026-06-19T18:59:11.850Z"
---

---
title: Genie Code
summary: An AI assistant integrated across Databricks notebooks and workspace, used for development, debugging, and operations with specialized knowledge of enterprise context.
sources:
  - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
  - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  - model-serving-observability-with-genie-code-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:28:56.703Z"
updatedAt: "2026-06-19T09:21:36.970Z"
tags:
  - ai-assistant
  - databricks
  - development
aliases:
  - genie-code
confidence: 0.9
provenanceState: merged
inferredParagraphs: 2
---

**Genie Code** is an AI assistant integrated throughout the Databricks workspace that provides a natural language interface for understanding, debugging, and improving GenAI applications within [MLflow](/concepts/mlflow.md). It has read access to everything in an experiment — including traces, prompts, datasets, evaluation runs, scorers, and labeling sessions — so users can explore observability and evaluation data conversationally instead of writing queries or navigating multiple UI pages.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md] [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Overview

Genie Code serves as an AI-assisted development and operations companion for data science and machine learning workflows. It can be used at every step of the workflow: starting with Genie chat to discover relevant models, data, and features in the workspace and Unity Catalog; to prototype pipelines for featurization, model training, tuning, evaluation, and deployment; to analyzing [model serving endpoints](/concepts/model-serving-endpoint.md) to diagnose and investigate production issues.^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Getting Started

To get started, click the Genie Code icon in the top-right of your workspace while viewing an experiment or a model serving endpoint page.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md] [model-serving-observability-with-genie-code-databricks-on-aws.md]

## Capabilities

Genie Code supports a wide range of observability and evaluation tasks, including:

- **Trace analysis and debugging**: Investigate failing traces, find errors, examine span trees, pinpoint root causes, analyze latency, and identify bottlenecks in an agent's execution flow. Users can deep-dive into any trace to inspect its full span hierarchy, including inputs, outputs, metadata, and token usage at every step.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Metrics and performance**: Compute latency percentiles (P50/P95/P99), track error rates and throughput over time, analyze token usage patterns and costs, and compare performance across different time periods or filters.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Quality and evaluations**: Review assessment scores from human feedback, LLM judges, and programmatic checks. Inspect evaluation datasets, check registered scorers and their configurations, and get help setting up `mlflow.genai.evaluate()` with the right scorers.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Labeling and review**: View labeling sessions and see who is assigned to review traces, and inspect labeling schemas to understand feedback criteria such as ratings, comments, and expectations.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Prompt registry**: Browse prompts in [Unity Catalog](/concepts/unity-catalog.md), view templates, versions, and aliases.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Instrumentation guidance**: Get help adding tracing to code with `autolog()`, `@mlflow.trace`, or manual spans, with runnable code snippets that can be pasted directly into Databricks notebooks.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Model serving observability**: In agent mode, Genie Code can analyze endpoint health and deployment states, review configurations against best practices, diagnose deployment failures using build logs and events, investigate high latency or timeout issues, assess scaling and resource utilization, and recommend optimal scaling configurations.^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Example Questions

Here are some typical queries users can ask Genie Code:

- "Help me discover issues with my agent's tool calling in the traces for this experiment over the last 3 hours"^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- "Identify cases where users get frustrated in the conversations with my agent"^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- "Which sessions have the lowest user feedback scores, and what went wrong in those conversations?"^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- "What are the most common failure patterns in my traces this past week, and what scorers should I add to catch them?"^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- "Which spans consume the most tokens across all my traces?"^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- "Find traces where the retriever returned no results but the agent still tried to answer"^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- "Help me set up evaluation for my RAG agent with the right scorers"^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- "Check the health of this endpoint"^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- "Why is my latency so high?"^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- "/diagnose" or "Why did my deployment fail?"^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- "Analyze error patterns from the last week"^[model-serving-observability-with-genie-code-databricks-on-aws.md]
- "Show me recent requests to this endpoint"^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Requirements

To use Genie Code for agent observability and evaluation, the workspace needs the following:

- Partner-powered AI features enabled for both the account and workspace.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- The workspace must be in a supported region. Genie Code is a Designated Service that uses Geos to manage data residency.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

For model serving, Genie Code currently only supports custom model serving endpoints.^[model-serving-observability-with-genie-code-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — End-to-end observability for GenAI applications
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Automated evaluation and monitoring for AI agents
- [MLflow 3 for GenAI](/concepts/mlflow-3-for-genai.md) — Getting started with MLflow's GenAI capabilities
- [Prompt Registry](/concepts/prompt-registry.md) — Managing prompts in Unity Catalog
- [Model Serving](/concepts/model-serving.md) — Deploying and serving models for inference
- Model Serving Observability — Monitoring and diagnosing model serving endpoints

## Sources

- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
- concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
- model-serving-observability-with-genie-code-databricks-on-aws.md

# Citations

1. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
2. [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md](/references/concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws-6175a64a.md)
3. [model-serving-observability-with-genie-code-databricks-on-aws.md](/references/model-serving-observability-with-genie-code-databricks-on-aws-64add48f.md)
