---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 02eee387770f39257f0fc63c98c2faf036730270a0c0229ba3d03b8277cb47bc
  pageDirectory: concepts
  sources:
    - mlflow-3-for-genai-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automated-evaluation-and-monitoring
    - Monitoring and Automated Evaluation
    - AEAM
    - Automated Evaluation
    - Automated evaluation
  citations:
    - file: mlflow-3-for-genai-databricks-on-aws.md
title: Automated Evaluation and Monitoring
description: Using the same LLM judges and scorers during development and production to replace manual testing and continuously improve GenAI app quality
tags:
  - automation
  - evaluation
  - monitoring
  - production
timestamp: "2026-06-19T19:37:32.073Z"
---

# Automated Evaluation and Monitoring

**Automated Evaluation and Monitoring** refers to the practice of using consistent, programmatic quality assessment tools throughout the entire lifecycle of GenAI applications and agents—from development through production. Within the MLflow 3 for GenAI framework, automated evaluation and monitoring leverage the same judges and scorers across both development and production environments, enabling continuous quality assessment without manual intervention. ^[mlflow-3-for-genai-databricks-on-aws.md]

## Overview

Evaluating GenAI applications and agents is more complex than evaluating traditional software. Inputs and outputs are often free-form text, and many different outputs can be considered correct. Quality depends not only on correctness but also on factors like precision, length, completeness, appropriateness, and other criteria specific to the use case. Because LLMs are inherently non-deterministic, and GenAI agents include additional components such as retrievers and tools, their responses can vary from run to run. Automated evaluation addresses these challenges by providing systematic, repeatable quality measurement. ^[mlflow-3-for-genai-databricks-on-aws.md]

## Key Components

### Tracing as a Foundation

[MLflow Tracing](/concepts/mlflow-tracing.md) automatically logs inputs, intermediate steps, and outputs, providing the data foundation required for both evaluation and monitoring. This trace data enables comprehensive observability into GenAI application behavior. ^[mlflow-3-for-genai-databricks-on-aws.md]

### Built-in and Custom LLM Judges and Scorers

MLflow 3 provides Built-in and Custom LLM Judges and Scorers that allow developers to define various aspects of quality and customize metrics to their specific use case. These judges and scorers can be applied consistently during both development and production. ^[mlflow-3-for-genai-databricks-on-aws.md]

### Expert Feedback Integration

[Review Apps for Expert Feedback](/concepts/review-apps-for-expert-feedback.md) allow teams to collect and label datasets for evaluation, helping to align automated judges and scorers with expert judgment. This human-in-the-loop component ensures that automated metrics reflect real-world quality standards. ^[mlflow-3-for-genai-databricks-on-aws.md]

## Benefits

Developers need concrete quality metrics, automated evaluation, and continuous monitoring to build and deploy robust AI apps. MLflow 3 for GenAI provides these capabilities for efficient development, deployment, and continuous improvement. Every production interaction becomes an opportunity to improve quality with integrated feedback and evaluation workflows. ^[mlflow-3-for-genai-databricks-on-aws.md]

## Integration with Databricks

Managed MLflow on Databricks extends open source MLflow with capabilities designed for production GenAI applications, including enterprise-ready governance, fully managed hosting, production-level scaling, and integration with data in the Databricks Lakehouse and [Unity Catalog](/concepts/unity-catalog.md). This allows teams to bring AI to their data to deeply understand and improve quality. ^[mlflow-3-for-genai-databricks-on-aws.md]

## Related Concepts

- [MLflow 3 for GenAI](/concepts/mlflow-3-for-genai.md) — The overarching platform that unifies tracking, evaluation, and observability
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Provides the trace data foundation for evaluation and monitoring
- Built-in and Custom LLM Judges and Scorers — Define quality metrics for automated assessment
- [Review Apps for Expert Feedback](/concepts/review-apps-for-expert-feedback.md) — Human-in-the-loop evaluation alignment
- [App and Prompt Versioning](/concepts/prompt-versioning-and-immutability.md) — Enables comparison across iterations
- AI Lifecycle Management — Version, track, and govern GenAI applications
- [Unity Catalog](/concepts/unity-catalog.md) — Provides governance for prompts, apps, and traces

## Sources

- mlflow-3-for-genai-databricks-on-aws.md

# Citations

1. [mlflow-3-for-genai-databricks-on-aws.md](/references/mlflow-3-for-genai-databricks-on-aws-ac0de02b.md)
