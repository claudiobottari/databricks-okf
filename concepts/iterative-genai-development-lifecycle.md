---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2366a58f15921f9c60cbe2cccbb5c58aafad3302990dbf0059c633817c6950a3
  pageDirectory: concepts
  sources:
    - evaluate-and-monitor-ai-agents-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - iterative-genai-development-lifecycle
    - IGDL
  citations:
    - file: evaluate-and-monitor-ai-agents-databricks-on-aws.md
title: Iterative GenAI Development Lifecycle
description: The continuous optimization workflow of developing, testing, monitoring, and collecting human feedback for GenAI applications.
tags:
  - mlflow
  - lifecycle
  - genai
timestamp: "2026-06-18T12:11:59.878Z"
---

# Iterative GenAI Development Lifecycle

The **Iterative GenAI Development Lifecycle** is a continuous workflow for building, evaluating, and improving [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications — covering development testing, production monitoring, human feedback collection, and iterative refinement. [MLflow 3](/concepts/mlflow-3.md) provides an integrated evaluation and monitoring component that supports this lifecycle end-to-end, enabling teams to systematically measure and enhance the quality of LLM-based applications, agents, and RAG systems. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Overview

Evaluating AI agents and LLMs is more complex than traditional ML model evaluation because these applications involve multiple components, multi-turn conversations, and nuanced quality criteria. The MLflow evaluation and monitoring framework is designed to help you iteratively optimize quality by connecting offline development testing with online production monitoring. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

The lifecycle builds upon [MLflow Tracing](/concepts/mlflow-tracing.md), which provides real-time trace logging during development, testing, and production. These traces can be evaluated during development using built-in or custom [LLM Judges and Scorers](/concepts/llm-judges-and-scorers.md), and the same judges and scorers can be reused for production monitoring, ensuring consistent evaluation across all stages. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Key Phases

### Development and Testing

During development, you run offline evaluation using the [Evaluation Harness](/concepts/evaluation-harness.md) with LLM-based judges. Traces from your agent or GenAI application are scored against quality criteria such as correctness, safety, or adherence to instructions. Any issues discovered can be addressed by modifying prompts, tools, or model configurations and re-evaluating. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

### Production Monitoring

Once the application is deployed, production monitoring reuses the same judges and scorers to continuously assess live traffic. This provides ongoing visibility into quality metrics and helps detect regressions or drift. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

### Human Feedback and Review

Domain experts can provide feedback using the integrated [Review App](/concepts/mlflow-review-app.md), which supports [expert feedback](/concepts/review-apps-for-expert-feedback.md) collection. This human evaluation data can be used as ground truth for further iteration or to fine-tune judges. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

### Iteration

The feedback and evaluation results feed back into the development phase, enabling a closed loop of continuous improvement. New evaluation data can be used to retrain judges, adjust prompts, or retune models. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Diagram

The high-level iterative workflow is illustrated in the following diagram (not reproduced here in text):

> ![Overview diagram of MLflow 3 evaluation and monitoring](https://docs.databricks.com/aws/en/assets/images/flowchart-00c729ac75207b58d9c2243583a30d5a.png)

## Benefits

- **Consistent measurement** – The same judges and scorers are used across development and production, eliminating evaluation gap.
- **Traceability** – All evaluation results are linked to [Traces](/concepts/traces.md), making it easy to inspect individual examples.
- **Iterative optimization** – Human feedback and production metrics directly inform the next development cycle.
- **Component reuse** – Judges, datasets, and evaluation configurations are portable across environments.

## Requirements

The Agent Evaluation SDK methods are available using the `mlflow[databricks]>=3.1` SDK. See Migrate to MLflow 3 from Agent Evaluation for guidance on updating MLflow 2 Agent Evaluation code. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Real-time trace logging for GenAI applications
- [LLM Judges and Scorers](/concepts/llm-judges-and-scorers.md) – Built-in and custom evaluators for quality assessment
- [Evaluation Harness](/concepts/evaluation-harness.md) – Offline evaluation framework using traces
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Continuous quality monitoring in production
- [Review App](/concepts/mlflow-review-app.md) – Human feedback collection interface
- [Expert Feedback](/concepts/review-apps-for-expert-feedback.md) – Human annotations for improving evaluation

## Sources

- evaluate-and-monitor-ai-agents-databricks-on-aws.md

# Citations

1. [evaluate-and-monitor-ai-agents-databricks-on-aws.md](/references/evaluate-and-monitor-ai-agents-databricks-on-aws-edcafd11.md)
