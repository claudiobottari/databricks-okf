---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7af5dc95569e76cc9e696b507c72fec9700688a680bbb436927155b11f83bf4c
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genai-trace-analysis-and-debugging
    - Debugging and GenAI Trace Analysis
    - GTAAD
    - Trace Analysis and Debugging
    - Debug and Observe with Traces
    - GenAI Application Debugging
    - GenAI Trace Analysis
    - Trace Analysis Examples
  citations:
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
title: GenAI Trace Analysis and Debugging
description: The capability to investigate failing traces, examine span trees, pinpoint root causes, analyze latency, and identify bottlenecks in GenAI agent execution flows within MLflow.
tags:
  - mlflow
  - debugging
  - tracing
  - genai
timestamp: "2026-06-19T10:43:36.500Z"
---

# GenAI Trace Analysis and Debugging

**GenAI Trace Analysis and Debugging** refers to the process of investigating, diagnosing, and improving the behavior of GenAI agents by examining their execution traces. Within [MLflow](/concepts/mlflow.md), this capability is provided through **Genie Code**, a natural language interface that gives read access to all trace data in an experiment — allowing developers to explore and debug agent performance conversationally rather than writing queries or navigating multiple UI pages. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Overview

Traces record the full execution flow of a GenAI agent, including inputs, outputs, intermediate reasoning steps, tool calls, metadata, and token usage at every span. Genie Code can deep-dive into any trace to inspect its span hierarchy and identify root causes of errors or performance issues. This enables developers to understand why an agent returned a particular response, which steps consumed the most tokens, or where a failure occurred in the chain. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Capabilities

With Genie Code, you can perform a wide range of trace analysis and debugging tasks, including: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- Investigating failing traces and finding errors across the experiment.
- Examining span trees to understand the call hierarchy and dependencies.
- Pinpointing root causes of agent failures or unexpected behavior.
- Analyzing latency distributions and identifying bottlenecks in the execution flow.
- Inspecting full span details — inputs, outputs, metadata, and token usage — at every step.
- Comparing performance across different time periods or filters.

## Example Queries

The following are examples of natural language questions you can ask Genie Code to perform trace analysis and debugging: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- *"Help me discover issues with my agent's tool calling in the traces for this experiment over the last 3 hours"*
- *"Which spans consume the most tokens across all my traces?"*
- *"Find traces where the retriever returned no results but the agent still tried to answer"*
- *"Identify cases where users get frustrated in the conversations with my agent"*
- *"Which sessions have the lowest user feedback scores, and what went wrong in those conversations?"*
- *"What are the most common failure patterns in my traces this past week, and what scorers should I add to catch them?"*

## Requirements

To use Genie Code for trace analysis and debugging, your workspace must meet the following prerequisites: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- Partner-powered AI features must be enabled for both the account and the workspace. See partner-powered AI features.
- The workspace must be in a supported region. Genie Code is a [Designated Service](https://docs.databricks.com/aws/en/resources/designated-services) that uses Geos to manage data residency. See [Geo availability of Genie Code features](https://docs.databricks.com/aws/en/genie-code/#geo-availability).

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — End-to-end observability for GenAI applications.
- [GenAI Observability](/concepts/genai-observability.md) — Monitoring and understanding agent behavior.
- Evaluation and Monitoring — Setting up quality checks and monitoring for agents.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Offline and online assessment of agent performance.
- [LLM Judges](/concepts/llm-judges.md) — Scorers that evaluate agent outputs.
- [Prompt Registry](/concepts/prompt-registry.md) — Managing prompt templates and versions in Unity Catalog.
- [Autolog](/concepts/mlflow-autologging.md) — Automated tracing instrumentation.

## Sources

- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md

# Citations

1. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
