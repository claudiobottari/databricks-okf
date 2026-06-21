---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bdb914664ed93b9ca22232678ecee5df69a5e03e7014268af7075f194ade8a64
  pageDirectory: concepts
  sources:
    - arize-phoenix-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-gpt-5-mini-model
  citations:
    - file: arize-phoenix-scorers-databricks-on-aws.md
title: databricks-gpt-5-mini Model
description: A Databricks-hosted GPT model used as the judge/grader for Arize Phoenix scorers in MLflow evaluations
tags:
  - databricks
  - model
  - llm-as-judge
timestamp: "2026-06-19T22:08:21.379Z"
---

# databricks-gpt-5-mini Model

The **databricks-gpt-5-mini Model** is a large language model (LLM) served on Databricks and accessible via the `databricks:/` model endpoint scheme. It is referenced in the context of [MLflow](/concepts/mlflow.md)’s generative AI evaluation framework, specifically as the scoring model used with [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md).

## Usage in MLflow Evaluation

In the `mlflow.genai.evaluate` API, the model is specified as `model="databricks:/databricks-gpt-5-mini"` when instantiating `Hallucination` and `Relevance` scorers from `mlflow.genai.scorers.phoenix`. This allows the evaluation pipeline to use the hosted model to compute hallucination and relevance scores for a given evaluation dataset. ^[arize-phoenix-scorers-databricks-on-aws.md]

## Model Endpoint Pattern

The `databricks:/` prefix indicates that the model is deployed on [Databricks Model Serving](/concepts/databricks-model-serving.md), enabling authenticated access from within a Databricks workspace. The model name `databricks-gpt-5-mini` suggests a smaller, cost-optimized variant of a GPT‑5 class model, suitable for evaluation tasks such as scoring and monitoring.

## Related Concepts

- [MLflow](/concepts/mlflow.md)
- [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md)
- [Hallucination Scorer](/concepts/hallucination-scorer.md)
- [Relevance Scorer](/concepts/relevance-scorer.md)
- [Databricks Model Serving](/concepts/databricks-model-serving.md)
- Generative AI evaluation
- Model monitoring

## Sources

- arize-phoenix-scorers-databricks-on-aws.md

# Citations

1. [arize-phoenix-scorers-databricks-on-aws.md](/references/arize-phoenix-scorers-databricks-on-aws-53f4b817.md)
