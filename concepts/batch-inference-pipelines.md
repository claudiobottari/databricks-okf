---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9cdae17163c1bb9585e199c460c553041dfe0f18310e953bc789353c54221406
  pageDirectory: concepts
  sources:
    - deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - batch-inference-pipelines
    - BIP
    - Deploy batch inference pipelines
    - Batch inference
    - Deploy models for batch inference
    - Deploy models for batch inference and prediction
    - Model Inference Pipeline
  citations:
    - file: deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
title: Batch Inference Pipelines
description: A Databricks pattern for deploying and orchestrating batch inference workloads as pipelines, enabling scalable processing of large datasets.
tags:
  - databricks
  - batch-inference
  - pipelines
  - machine-learning
timestamp: "2026-06-19T15:10:49.586Z"
---

# Batch Inference Pipelines

**Batch Inference Pipelines** are workflows that apply machine learning models to large datasets in a batch (non-real-time) mode. Unlike real-time model serving, which responds to individual requests with low latency, batch inference processes many records simultaneously, making it suitable for periodic scoring, offline predictions, and large-scale data transformations. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Overview

Batch inference enables organizations to generate predictions, classifications, translations, or other model outputs across entire tables or datasets at scheduled intervals or on demand. On Databricks, batch inference can be performed using AI Functions—built-in SQL functions that apply AI models directly to data stored in the platform. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## AI Functions for Batch Inference

Databricks provides two primary approaches for running batch inference using AI Functions:

### Task-Specific AI Functions

Task-specific AI Functions are built-in functions designed for particular AI tasks. These functions can be called directly in SQL queries to process data in bulk. Example functions include text translation, summarization, and other specialized operations. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

The following example shows batch inference using the `ai_translate` function on a table of news summaries:

```sql
SELECT
    writer_summary,
    ai_translate(writer_summary, "cn") as cn_translation
FROM user.batch.news_summaries
LIMIT 500;
```

To perform batch inference on an entire table, omit the `LIMIT` clause. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

### General-Purpose AI Function (`ai_query`)

The `ai_query` function is a general-purpose AI function that supports multiple model types. It can be used for batch inference when the task-specific functions are not sufficient. See the documentation on supported models for ai_query for a complete list of compatible model types. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Comparison with Real-Time Model Serving

Batch inference pipelines differ from [Model Serving](/concepts/model-serving.md) for real-time inference:

| Aspect | Batch Inference | Real-Time Model Serving |
|--------|-----------------|------------------------|
| Timing | Scheduled or on-demand | Continuous, low-latency |
| Data volume | Large datasets (entire tables) | Individual requests |
| Latency | Minutes to hours | Milliseconds to seconds |
| Compute | Spark or SQL compute resources | Model Serving endpoints |

For real-time model serving, see [Deploy models using Model Serving](/concepts/mlflow-model-serving-and-deployment.md). ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Use Cases

Common use cases for batch inference pipelines include:

- **Periodic scoring** – Running predictions on new data daily or weekly
- **Large-scale transformations** – Translating or summarizing entire text corpora
- **Offline analysis** – Generating predictions for historical data analysis
- **Data enrichment** – Adding AI-generated features to existing datasets

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – Real-time inference endpoints for individual requests
- [AI Functions](/concepts/ai-functions.md) – Built-in SQL functions for applying AI models
- ai_query – General-purpose AI function for model inference
- [Deploy models for batch inference and prediction](/concepts/batch-inference-pipelines.md) – Official Databricks documentation
- [MLflow](/concepts/mlflow.md) – Lifecycle management for machine learning models
- [Feature Store](/concepts/feature-store.md) – Centralized repository for machine learning features

## Sources

- deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md

# Citations

1. [deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md](/references/deploy-models-for-batch-inference-and-prediction-databricks-on-aws-5481092c.md)
