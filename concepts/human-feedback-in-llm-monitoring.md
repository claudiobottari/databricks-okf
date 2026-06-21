---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d9fb5f84da337329b57f175dc8b526d3f7d9634f24ba9b6fcdbd3780b65a438
  pageDirectory: concepts
  sources:
    - llmops-workflows-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - human-feedback-in-llm-monitoring
    - HFILM
    - LLM Monitoring
  citations:
    - file: llmops-workflows-on-databricks-databricks-on-aws.md
title: Human Feedback in LLM Monitoring
description: Incorporating human feedback loops into LLM application monitoring and evaluation, managed as data with near real-time streaming
tags:
  - human-feedback
  - monitoring
  - evaluation
  - llmops
timestamp: "2026-06-19T19:13:08.408Z"
---

# Human Feedback in LLM Monitoring

**Human Feedback in LLM Monitoring** refers to the practice of incorporating human evaluations and ratings into the monitoring infrastructure of large language model (LLM) applications. Unlike traditional ML models where automated metrics may suffice, LLM-generated outputs often require human judgment to assess quality, safety, and relevance. Human feedback loops are essential in most LLM applications and should be managed like other data, ideally incorporated into monitoring based on near real-time streaming. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Overview

Human feedback is a critical component of [LLMOps](/concepts/large-language-models-llms-on-databricks.md) workflows because LLM outputs—such as open-ended answers, summaries, and instructions—cannot be fully evaluated by automated metrics alone. Human reviewers assess model outputs against criteria like factual accuracy, helpfulness, safety, and alignment with user intent. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Integration into Monitoring

Human feedback should be treated as first-class data within the monitoring infrastructure. The recommended approach is to stream human feedback into a lakehouse architecture—for example, using [Delta Tables](/concepts/delta-lake-table.md)—and then incorporate it into monitoring dashboards and alerting pipelines in near real-time. This allows teams to detect degradation in model quality promptly and trigger Model Retraining or fine-tuning as needed. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## MLflow Review App

The [MLflow](/concepts/mlflow.md) review app helps you gather feedback from human reviewers. It provides a structured interface for raters to evaluate model outputs and record their assessments. The collected feedback can then be logged back into MLflow for analysis and used to drive downstream decisions such as model selection, fine-tuning, or alerting. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

### Key Features

- **Structured evaluation**: Reviewers can rate outputs on defined criteria (e.g., relevance, safety, coherence).
- **Feedback logging**: Ratings and comments are stored as part of the MLflow experiment or run metadata.
- **Integration with monitoring**: Feedback data can be piped into [Model Serving](/concepts/model-serving.md) monitoring dashboards for real-time quality tracking.

For details, see [Human feedback in MLflow](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/). ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Role in the LLMOps Workflow

In the LLMOps reference architecture, human feedback appears in the monitoring and evaluation phase. This is particularly important for:

- **[Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications**: Human reviewers assess whether retrieved context is used correctly and whether responses are grounded.
- **Fine-tuned models**: Feedback helps validate that fine-tuning improved performance for specific scenarios without introducing regressions.
- **Third-party API models**: When using [External Models](/concepts/external-models.md) (e.g., OpenAI API), human feedback provides quality control that the external service may not offer.

^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Best Practices

- **Treat feedback as data**: Log human feedback into the same data platform (e.g., [Unity Catalog](/concepts/unity-catalog.md)) used for other monitoring data.
- **Stream near real-time**: Use streaming infrastructure (e.g., Auto Loader or structured streaming) to minimize latency between user interaction and monitoring dashboards.
- **Combine with automated metrics**: Use human feedback to complement—not replace—automated quality, drift, and performance metrics.
- **Define clear rating rubrics**: Provide reviewers with explicit criteria to ensure consistent evaluations.

## Related Concepts

- [LLMOps](/concepts/large-language-models-llms-on-databricks.md) — The operational workflow for deploying and managing LLMs.
- [MLflow](/concepts/mlflow.md) — Platform for experiment tracking, model management, and human feedback collection.
- [Model Serving](/concepts/model-serving.md) — Unified interface for deploying and querying models, including monitoring.
- RAG Evaluation — Evaluating retrieval-augmented generation outputs.
- [LLM Evaluation Metrics](/concepts/llm-as-a-judge-evaluation-metrics.md) — Automated and human-in-the-loop metrics for LLM performance.
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md) — Customizing pre-trained models with human feedback data.

## Sources

- llmops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [llmops-workflows-on-databricks-databricks-on-aws.md](/references/llmops-workflows-on-databricks-databricks-on-aws-6b1b2e6a.md)
