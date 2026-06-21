---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a51eb4a066f80b6ed89f6fccb6bfad8ec180891dec4604164974932aa1d5569e
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metrics-and-performance-analysis-for-genai-agents
    - Performance Analysis for GenAI Agents and Metrics
    - MAPAFGA
  citations:
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Metrics and Performance Analysis for GenAI Agents
description: The ability to compute latency percentiles (P50/P95/P99), track error rates and throughput over time, analyze token usage patterns and costs, and compare performance across different time periods or filters.
tags:
  - mlflow
  - monitoring
  - performance
  - genai
timestamp: "2026-06-19T10:43:43.071Z"
---

# Metrics and Performance Analysis for GenAI Agents

**Metrics and Performance Analysis for GenAI Agents** is the practice of measuring, tracking, and diagnosing the quality, efficiency, and operational behavior of generative AI agents. It combines quantitative metrics (latency, throughput, token usage, cost) with qualitative assessments (judge scores, human feedback) to enable continuous improvement and production monitoring.

## Overview

Performance analysis for GenAI agents spans two complementary dimensions: **operational metrics** (how fast, how costly, how often errors occur) and **quality metrics** (how well the agent meets user expectations, behaves correctly, and uses tools appropriately). MLflow provides a unified platform for collecting both types of data through traces, evaluation runs, and scoring sessions. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Key Metrics

### Operational Metrics

- **Latency**: Measured as percentiles (P50, P95, P99) to understand typical and worst-case response times. Genie Code can compute these percentiles across any time period or filter. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Error Rate**: The proportion of traces that contain failures or exceptions. Tracking error rates over time helps detect regressions. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Throughput**: The number of agent invocations per unit time. Throughput trends reveal capacity and demand patterns. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Token Usage**: The number of input and output tokens consumed across all spans (LLM calls, embeddings, etc.). Token usage is a primary driver of cost. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
- **Cost**: Derived from token usage and per-model pricing. Cost analysis can be broken down by agent configuration, time period, or user segment. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

### Quality Metrics

Quality is evaluated using [Custom Judges](/concepts/custom-judges.md) (LLM‑as‑a‑judge), human feedback, and [programmatic checks](/concepts/programmatic-and-batch-evaluation-patterns.md). Common dimensions include: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- **Issue resolution**: Whether the agent fully resolves, partially resolves, or needs follow‑up.
- **Expected behaviors**: Whether the agent meets, partially meets, or does not meet defined expectations.
- **Tool call correctness**: Whether the agent invoked the appropriate tools for the user’s request.
- **User satisfaction**: Expressed through ratings, comments, and labeling session scores.

## Tools and Methods

### [MLflow Tracing](/concepts/mlflow-tracing.md)

[MLflow Tracing](/concepts/mlflow-tracing.md) captures the full span tree of every agent invocation, including inputs, outputs, metadata, and token usage at each step. Traces are the foundation for computing all operational metrics and for root‑cause analysis. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

### Genie Code

[Genie Code](/concepts/genie-code.md) provides a natural‑language interface to explore traces, metrics, evaluation runs, and scorers. It can answer questions like: ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

- *“What are the most common failure patterns in my traces this past week, and what scorers should I add to catch them?”*
- *“Which spans consume the most tokens across all my traces?”*
- *“Find traces where the retriever returned no results but the agent still tried to answer.”*
- *“Identify cases where users get frustrated in the conversations with my agent.”*

Genie Code can also help set up `mlflow.genai.evaluate()` with the right scorers, inspect evaluation datasets, and review labeling schemas. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

### Custom Judges

[Custom Judges](/concepts/custom-judges.md) are LLM‑based scorers that evaluate agent outputs against specific criteria. Two types are used: ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

- **Input/Output judges**: Evaluate the conversation history and agent response (e.g., did the agent attempt to resolve the issue?).
- **Trace‑based judges**: Analyze the full execution trace, including tool calls, intermediate reasoning, and results. They can validate whether appropriate tools were invoked.

Custom judges are deployed consistently across configurations to enable objective [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md). ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### A/B Comparison

[A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) uses the same evaluation dataset and the same set of judges to compare two or more agent variants. For example, toggling a behavior flag (`RESOLVE_ISSUES = True` vs `False`) and scoring both with the same judges reveals which variant better satisfies quality criteria. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Labeling and Review

Labeling sessions allow human reviewers to provide feedback on agent traces. Reviewers can assign ratings, comments, and expectations according to a defined labeling schema. These annotations can be used to fine‑tune custom judges or to compute ground‑truth quality metrics. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Best Practices

1. **Instrument comprehensively**: Use `autolog()` or manual spans to capture all LLM calls, tool invocations, and retrieval steps. Without full tracing, latency and token attribution will be incomplete. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
2. **Define quality criteria upfront**: Create custom judges or labeling schemas that reflect the behaviors most important to your users (e.g., issue resolution, safety, helpfulness). ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
3. **Measure both operational and quality metrics**: Low latency alone is useless if responses are wrong; perfect answers are useless if the agent takes 30 seconds. Track both dimensions on the same traces. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]
4. **Compare variants systematically**: Use A/B comparison with consistent judges before promoting any configuration to production. Change only one variable at a time. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
5. **Align judges with human feedback**: Periodically compare judge scores against human annotations and update judge instructions to reduce drift. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
6. **Monitor for regressions**: Set up scheduled scorers or dashboards to track latency, error rate, and quality scores over time. Genie Code can alert on anomalies. ^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Custom Judges](/concepts/custom-judges.md)
- [Genie Code](/concepts/genie-code.md)
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md)
- [Evaluation Dataset](/concepts/evaluation-dataset.md)
- Human Feedback Alignment
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)
- [Prompt Registry](/concepts/prompt-registry.md)

## Sources

- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
