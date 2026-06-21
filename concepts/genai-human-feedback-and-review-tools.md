---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d11ee6b28af68a22aa17a00d09a591697d2c05fb81288b42319c8802c2177d73
  pageDirectory: concepts
  sources:
    - open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genai-human-feedback-and-review-tools
    - review tools and GenAI human feedback
    - GHFART
  citations:
    - file: open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md
title: GenAI human feedback and review tools
description: Databricks provides a Review App for human feedback on GenAI outputs, including a Chat UI for vibe checks and an expert feedback UI for labeling traces, enabling structured human evaluation of generative AI.
tags:
  - genai
  - human-feedback
  - evaluation
timestamp: "2026-06-19T19:50:00.423Z"
---

# GenAI Human Feedback and Review Tools

**GenAI human feedback and review tools** are managed capabilities provided by Databricks for evaluating generative AI applications through human input. These tools are part of the broader [MLflow 3 for GenAI](/concepts/mlflow-3-for-genai.md) ecosystem and are available exclusively through Databricks-managed MLflow, building on the open source MLflow data model and APIs. ^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

## Overview

Human feedback tools enable developers and domain experts to assess the quality of GenAI applications by providing direct human evaluation. This complements automated evaluation methods such as [LLM Judges](/concepts/llm-judges.md) and [[scorers]], offering a qualitative dimension to the evaluation process. ^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

## Review App for Human Feedback

The primary interface for human evaluation is the **Review App**, which provides two main capabilities for assessing GenAI outputs: ^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

### Chat UI for Vibe Checks

The Review App includes a Chat UI that allows evaluators to perform informal "vibe checks" on GenAI applications. This interface enables interactive testing of model responses in a conversational format, helping evaluators quickly assess overall quality and behavior before more formal evaluation. ^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

### Expert Feedback UI for Labeling Traces

The Review App also provides an [expert feedback UI](/concepts/review-apps-for-expert-feedback.md) for labeling existing traces. This allows domain experts to review and annotate specific model interactions, providing structured feedback that can be used for further analysis, model improvement, or as training data for [reinforcement learning from human feedback (RLHF)](/concepts/trl-transformer-reinforcement-learning.md). ^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

## Integration with the Databricks Platform

Human feedback tools are integrated with the broader Databricks platform, providing: ^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

- **Enterprise governance**: Feedback data is governed under [Unity Catalog](/concepts/unity-catalog.md), ensuring consistent access control and auditability alongside other AI assets.
- **Lakehouse data integration**: Feedback logs and traces can be analyzed using AI/BI Genie Spaces, dashboards, and Databricks SQL.
- **Production monitoring**: Human feedback can complement automated [Production Monitoring](/concepts/production-monitoring.md) services that continuously evaluate production traffic using LLM judges and scorers.

## Relationship to Open Source MLflow

The human feedback and review tools are an additional capability of managed MLflow on Databricks, not available in open source MLflow. The core MLflow data model and APIs remain open source, ensuring portability of data and workloads. ^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

## Related Concepts

- [MLflow 3 for GenAI](/concepts/mlflow-3-for-genai.md) — The overarching framework for GenAI development on Databricks
- [Production Monitoring](/concepts/production-monitoring.md) — Automated evaluation of production GenAI traffic
- [Tracing](/concepts/mlflow-tracing.md) — Recording and storing GenAI model interactions for analysis
- Expert feedback — Structured human evaluation of model outputs
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for AI assets including feedback data
- [LLM evaluation](/concepts/llm-as-a-judge-evaluation.md) — Broader topic of assessing LLM quality

## Sources

- open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md

# Citations

1. [open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md](/references/open-source-vs-managed-mlflow-on-databricks-databricks-on-aws-ce848b0f.md)
