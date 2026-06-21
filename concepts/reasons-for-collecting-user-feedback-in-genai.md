---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8e5c53b647e4e94edea724630ccaf83a0b3438552622a89a1f01baa9fb1b0928
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reasons-for-collecting-user-feedback-in-genai
    - RFCUFIG
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: Reasons for Collecting User Feedback in GenAI
description: "Five key motivations: real-world quality signals, continuous improvement, training data creation, quality monitoring, and model fine-tuning."
tags:
  - mlflow
  - genai
  - feedback
  - motivation
timestamp: "2026-06-19T09:17:12.517Z"
---

# Reasons for Collecting User Feedback in GenAI

**User feedback** is a critical component for understanding and improving the real-world quality of a GenAI application. MLflow provides a structured feedback mechanism through assessments attached to traces, enabling teams to capture, analyze, and act on user responses. ^[collect-user-feedback-databricks-on-aws.md]

Collecting user feedback directly from production or development environments gives teams ground-truth data about how their application actually performs. The following reasons, drawn from MLflow’s guidance on tracing and feedback, explain why feedback collection is essential. ^[collect-user-feedback-databricks-on-aws.md]

## Real‑world Quality Signals

User feedback reveals how actual users perceive your application’s outputs. Unlike offline evaluation metrics, this feedback reflects genuine use cases, edge cases, and user expectations — providing a signal that cannot be replicated with synthetic data alone. ^[collect-user-feedback-databricks-on-aws.md]

## Continuous Improvement

Negative or critical feedback highlights patterns of failure or dissatisfaction. By systematically analyzing these patterns, teams can prioritize development efforts, fix recurring issues, and iteratively improve the application. ^[collect-user-feedback-databricks-on-aws.md]

## Training Data Creation

Feedback from production interactions can be used to build high‑quality evaluation datasets. These datasets are invaluable for offline testing, regression detection, and benchmarking future versions of the GenAI system. ^[collect-user-feedback-databricks-on-aws.md]

## Quality Monitoring

Tracking satisfaction metrics over time — and across different user segments — provides a dashboard of application health. With feedback stored as assessments on traces, teams can compute positive/negative ratios, feedback rates, and per‑segment scores, enabling continuous quality monitoring. ^[collect-user-feedback-databricks-on-aws.md]

## Model Fine‑tuning

Feedback data can be leveraged to fine‑tune the underlying models. By collecting examples where users expressed approval or disapproval, teams can curate training examples that directly reflect desired behaviors, improving model alignment with user needs. ^[collect-user-feedback-databricks-on-aws.md]

## Related Concepts

- [Trace Assessments](/concepts/trace-assessments.md) – How feedback is stored as assessments on MLflow traces.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – Using feedback to create datasets for offline evaluation.
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying feedback collection for ongoing quality metrics.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The platform that enables feedback logging and trace management.
- [Collecting user feedback (implementation)](/concepts/end-user-feedback-collection-via-sdk.md) – Practical code patterns for feedback collection.

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
