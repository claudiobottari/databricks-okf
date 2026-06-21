---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4c27325c55f9f377aac366a4cae5455cf1233e16ebe707f31dfc3a29cd81a11
  pageDirectory: concepts
  sources:
    - evaluate-and-monitor-ai-agents-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - review-app-for-human-feedback
    - RAFHF
  citations:
    - file: evaluate-and-monitor-ai-agents-databricks-on-aws.md
title: Review App for Human Feedback
description: Integrated application for collecting domain expert feedback on AI agent outputs, producing evaluation data for further iteration.
tags:
  - mlflow
  - human-feedback
  - evaluation
timestamp: "2026-06-19T18:41:31.050Z"
---

# Review App for Human Feedback

The **Review App for Human Feedback** is an integrated component of the MLflow evaluation and monitoring ecosystem. It provides domain experts with a dedicated interface to review AI agent outputs and supply human feedback, which is then used to generate evaluation data for iterative improvement of the application. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Role in the Evaluation Lifecycle

MLflow supports the complete development lifecycle for GenAI applications, from testing through production monitoring. The Review App fits into this workflow by enabling domain experts to contribute human judgment alongside automated evaluation methods. Traces captured by [MLflow Tracing](/concepts/mlflow-tracing.md) can be evaluated offline using [LLM Judges and Scorers](/concepts/llm-judges-and-scorers.md), and the same scorers can be reused for [Production Monitoring](/concepts/production-monitoring.md). Between these stages, the Review App collects human feedback, producing evaluation data that feeds back into further iteration. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Purpose and Capabilities

The primary purpose of the Review App is to collect human feedback on AI agent behavior. Domain experts—subject-matter experts who understand the desired quality criteria—use the app to review agent responses and provide annotations. This human-generated evaluation data complements automated scoring and captures nuances that automated metrics might miss. The collected feedback is used to refine the agent, update prompts or tooling, and improve overall application quality. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Integration with MLflow Components

The Review App is part of the broader evaluation and monitoring framework in MLflow 3. It integrates with:

- **[MLflow Tracing](/concepts/mlflow-tracing.md)** – Logs every trace of agent calls, which can be reviewed in the Review App.
- **[LLM Judges and Scorers](/concepts/llm-judges-and-scorers.md)** – Automated scoring that can be validated or calibrated against human feedback.
- **[Production Monitoring](/concepts/production-monitoring.md)** – Enables auditing of production traces with human judgment.

## Related Concepts

- Human Feedback Alignment – Improving judge accuracy with expert annotations.
- [Evaluation Harness](/concepts/evaluation-harness.md) – The offline evaluation framework that can incorporate human-annotated data.

## Sources

- evaluate-and-monitor-ai-agents-databricks-on-aws.md

# Citations

1. [evaluate-and-monitor-ai-agents-databricks-on-aws.md](/references/evaluate-and-monitor-ai-agents-databricks-on-aws-edcafd11.md)
