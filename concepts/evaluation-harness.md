---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 86ff3d070c68ebee749e1281e7e0b2be88874c03dc036e9a5c6e9db9d1b18ab4
  pageDirectory: concepts
  sources:
    - evaluate-and-monitor-ai-agents-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-harness
    - Automated evaluation (Eval Harness)
  citations:
    - file: evaluate-and-monitor-ai-agents-databricks-on-aws.md
title: Evaluation Harness
description: Testing framework for evaluating traces during the development phase of GenAI applications.
tags:
  - mlflow
  - testing
  - evaluation
timestamp: "2026-06-19T18:41:19.045Z"
---

# Evaluation Harness

The **Evaluation Harness** is a development-phase component of [MLflow 3](/concepts/mlflow-3.md) that allows developers to evaluate [traces](/concepts/mlflow-tracing.md) using built-in or custom [LLM Judges and Scorers](/concepts/llm-judges-and-scorers.md). It is part of the iterative workflow for optimizing the quality of GenAI applications, including agents, RAG systems, and other LLM-based applications. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Overview

Evaluation and monitoring in MLflow 3 build upon [MLflow Tracing](/concepts/mlflow-tracing.md), which provides real-time trace logging during development, testing, and production. The evaluation harness enables developers to assess traces generated during development by applying the same [[scorers]] and [LLM Judges](/concepts/llm-judges.md) that can later be reused in [Production Monitoring](/concepts/production-monitoring.md). This consistency ensures that quality criteria are measured uniformly throughout the application lifecycle. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Role in the Development Lifecycle

The evaluation harness is used during development to iteratively measure and improve the quality of AI agents and LLM applications. Domain experts can also provide feedback through an integrated [Review App](/concepts/mlflow-review-app.md), producing evaluation data that feeds back into further iteration. The workflow is depicted in the MLflow 3 evaluation and monitoring diagram, which shows the cycle of development, trace logging, evaluation, and monitoring. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [LLM Judges](/concepts/llm-judges.md)
- [[Scorers]]
- [Production Monitoring](/concepts/production-monitoring.md)
- [Review App](/concepts/mlflow-review-app.md)
- [MLflow 3](/concepts/mlflow-3.md)

## Sources

- evaluate-and-monitor-ai-agents-databricks-on-aws.md

# Citations

1. [evaluate-and-monitor-ai-agents-databricks-on-aws.md](/references/evaluate-and-monitor-ai-agents-databricks-on-aws-edcafd11.md)
