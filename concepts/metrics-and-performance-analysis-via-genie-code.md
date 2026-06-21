---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4da10af9c2457b9856354f092c282a9bfcf0d3d4ee1c6c32b6a894ff9907cba3
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metrics-and-performance-analysis-via-genie-code
    - Performance Analysis via Genie Code and Metrics
    - MAPAVGC
  citations:
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
title: Metrics and Performance Analysis via Genie Code
description: Genie Code capability to compute latency percentiles (P50/P95/P99), track error rates and throughput over time, analyze token usage patterns and costs, and compare performance across time periods or filters.
tags:
  - observability
  - metrics
  - performance
  - genai
timestamp: "2026-06-18T12:28:59.411Z"
---

Here is the wiki page for "Metrics and Performance Analysis via Genie Code".

---

# Metrics and Performance Analysis via Genie Code

**Metrics and Performance Analysis via Genie Code** refers to the ability to compute, analyze, and compare performance metrics for GenAI applications using a natural language interface within MLflow. Instead of writing custom queries or navigating multiple UI pages, you can ask Genie Code to calculate latency percentiles, error rates, throughput, token usage, and costs for your agent's execution traces. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Overview

Genie Code is a conversational tool that sits inside the MLflow experiment viewer. It has read access to everything in an experiment — traces, prompts, datasets, evaluation runs, scorers, and labeling sessions. For metrics and performance analysis, Genie Code offers the following capabilities: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- **Compute latency percentiles**: Ask for P50, P95, and P99 latencies across all traces or a filtered subset.
- **Track error rates and throughput**: Monitor how often agents fail and how many requests they handle over time.
- **Analyze token usage patterns and costs**: Identify which spans consume the most tokens and estimate associated costs.
- **Compare performance across different time periods or filters**: Slice performance metrics by date range, agent configuration, or other criteria.

## Benefits

Using natural language for metrics analysis eliminates the need to manually query tables or build dashboards for common observability tasks. You can answer questions like "What are the most common failure patterns in my traces this past week?" or "Which spans consume the most tokens across all my traces?" directly in the experiment UI. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Example Questions

- "Compute latency percentiles (P50/P95/P99) for my agent over the last 24 hours"
- "Track error rates and throughput over time for this experiment"
- "Analyze token usage patterns and costs across all traces"
- "Compare performance between yesterday and today"
- "Which spans consume the most tokens across all my traces?"

## Requirements

To use Genie Code for metrics and performance analysis, your workspace must have: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- Partner-powered AI features enabled for both the account and workspace.
- Your workspace in a supported region (Genie Code is a Designated Service that uses Geos to manage data residency).

## Accessing Genie Code

Click the **Genie Code** icon in the top-right of your workspace while viewing an experiment. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Related Concepts

- Genie Code for Agent Observability and Evaluation — The broader tool that encompasses metrics, trace analysis, quality evaluation, and more
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The observability layer that captures the trace data used for metrics analysis
- [Trace Analysis and Debugging](/concepts/genai-trace-analysis-and-debugging.md) — Using Genie Code to examine spans and root causes
- [Quality and Evaluations](/concepts/genai-evaluation-and-quality-assessment.md) — Reviewing assessment scores from judges and human feedback
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for ongoing quality monitoring in production

## Sources

- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md

# Citations

1. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
