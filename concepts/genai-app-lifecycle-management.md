---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0de037cde1ce96b4556bf32bebadb75ecf6aa9ee42dd2e8ed61b53433c3a4e8c
  pageDirectory: concepts
  sources:
    - mlflow-3-for-genai-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genai-app-lifecycle-management
    - GALM
    - AI Lifecycle Management
    - Data Lifecycle Management
    - GenAI app lifecycle
    - GenAI apps & agents
  citations:
    - file: mlflow-3-for-genai-databricks-on-aws.md
title: GenAI App Lifecycle Management
description: Versioning, tracking, and governance for GenAI applications including prompts, apps, and traces across development and production
tags:
  - lifecycle
  - versioning
  - governance
timestamp: "2026-06-19T19:37:27.747Z"
---

# GenAI App Lifecycle Management

**GenAI App Lifecycle Management** refers to the end-to-end process of developing, evaluating, deploying, monitoring, and continuously improving generative AI applications and agents. MLflow 3 for GenAI provides an open platform that unifies tracking, evaluation, and observability throughout the development and production lifecycle. ^[mlflow-3-for-genai-databricks-on-aws.md]

## Overview

Evaluating GenAI applications is more complex than evaluating traditional software. Inputs and outputs are often free-form text, and many different outputs can be considered correct. Quality depends not only on correctness but also on factors like precision, length, completeness, appropriateness, and other criteria specific to the use case. Because LLMs are inherently non-deterministic, and GenAI agents include additional components such as retrievers and tools, their responses can vary from run to run. ^[mlflow-3-for-genai-databricks-on-aws.md]

Developers need concrete quality metrics, automated evaluation, and continuous monitoring to build and deploy robust AI apps. MLflow 3 for GenAI provides these key pieces for efficient development, deployment, and continuous improvement. ^[mlflow-3-for-genai-databricks-on-aws.md]

## Key Components

### Tracing

[MLflow Tracing](/concepts/mlflow-tracing.md) provides observability and logs the trace data required for evaluation and monitoring. It automatically logs inputs, intermediate steps, and outputs, providing the data foundation for evaluation and monitoring throughout the lifecycle. ^[mlflow-3-for-genai-databricks-on-aws.md]

### Evaluation and Monitoring

[MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) replaces manual testing with automated evaluation using built-in and custom LLM judges and scorers that match human expertise. These can be applied in both development and production. Every production interaction becomes an opportunity to improve with integrated feedback and evaluation workflows. ^[mlflow-3-for-genai-databricks-on-aws.md]

Key evaluation capabilities include:
- **Built-in and custom LLM judges and scorers** that let you define various aspects of quality and customize metrics to your use case. ^[mlflow-3-for-genai-databricks-on-aws.md]
- **Review apps for expert feedback** that allow you to collect and label datasets for evaluation and to align automated judges and scorers with expert judgement. ^[mlflow-3-for-genai-databricks-on-aws.md]
- **Automated evaluation and monitoring** that leverage the same judges and scorers during development and production. ^[mlflow-3-for-genai-databricks-on-aws.md]

### Versioning and Lifecycle Management

[MLflow Model Registry](/concepts/mlflow-model-registry.md) enables app and prompt versioning, allowing you to compare versions and track improvements over iterations. Managed MLflow on Databricks extends open source MLflow with capabilities designed for production GenAI applications, including enterprise-ready governance, fully managed hosting, production-level scaling, and integration with your data in the Databricks lakehouse and [Unity Catalog](/concepts/unity-catalog.md). ^[mlflow-3-for-genai-databricks-on-aws.md]

## Managed MLflow on Databricks

Managed MLflow on Databricks extends open source MLflow with capabilities designed for production GenAI applications, including:
- Enterprise-ready governance
- Fully managed hosting
- Production-level scaling
- Integration with your data in the Databricks lakehouse and Unity Catalog

Using MLflow 3 on Databricks, you can bring AI to your data to help you deeply understand and improve quality. Unity Catalog provides consistent governance for prompts, apps, and traces. Using any model or framework, MLflow supports you throughout the development loop all the way to and in production. ^[mlflow-3-for-genai-databricks-on-aws.md]

## Related Concepts

- [MLflow 3 for GenAI](/concepts/mlflow-3-for-genai.md) — The open platform for GenAI lifecycle management
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Observability and trace logging
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Automated evaluation with LLM judges
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation specifically for GenAI agents
- [Unity Catalog](/concepts/unity-catalog.md) — Governance for prompts, apps, and traces
- [LLM Judges](/concepts/llm-judges.md) — Automated quality assessment using LLMs
- [Prompt Versioning](/concepts/prompt-versioning.md) — Tracking prompt iterations over time

## Sources

- mlflow-3-for-genai-databricks-on-aws.md

# Citations

1. [mlflow-3-for-genai-databricks-on-aws.md](/references/mlflow-3-for-genai-databricks-on-aws-ac0de02b.md)
