---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f5c54d13a956a093ea378e319adcfa33cc92f56676632d4abbf4ee094c25dbd
  pageDirectory: concepts
  sources:
    - deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-functions-databricks
    - AF(
    - Function Calling (Databricks)
  citations:
    - file: deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
title: AI Functions (Databricks)
description: Built-in SQL functions on Databricks that enable applying AI models directly to data using task-specific or general-purpose functions like ai_query
tags:
  - databricks
  - sql
  - ai-functions
  - machine-learning
timestamp: "2026-06-19T18:30:23.807Z"
---

Here is the updated wiki page for "AI Functions (Databricks)".

---

# AI Functions (Databricks)

**AI Functions** are built-in SQL functions in Databricks that allow you to apply AI capabilities directly to data stored in the lakehouse without manually deploying models or writing custom inference code. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Overview

AI Functions provide a convenient way to run batch inference on your Databricks data using either task-specific functions or a general-purpose function. They eliminate the need to set up separate serving infrastructure for many common AI workloads, making it easy to incorporate AI processing into standard SQL pipelines. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Types of AI Functions

### Task-Specific AI Functions

These are functions designed for particular AI tasks. For example, `ai_translate` performs language translation. Databricks offers a set of task-specific AI functions that cover common use cases such as translation, summarization, and classification. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

### General-Purpose Function: `ai_query`

The `ai_query` function is a general-purpose AI function that can query a wide range of supported models. It can be used for any inference task where a compatible model is available, including custom models registered in Unity Catalog or Databricks-hosted foundation models. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Batch Inference with AI Functions

You can use AI Functions to perform batch inference on entire tables or subsets of data without leaving SQL. The following example applies the task-specific `ai_translate` function to translate a column of text summaries into Chinese:

```sql
SELECT
  writer_summary,
  ai_translate(writer_summary, "cn") AS cn_translation
FROM user.batch.news_summaries
LIMIT 500;
```

If you want to process the entire table, remove the `LIMIT 500` clause. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

Alternatively, `ai_query` can be used for the same purpose. For example:

```sql
SELECT
  writer_summary,
  ai_query('databricks-llama-3-70b', writer_summary) AS ai_response
FROM user.batch.news_summaries
LIMIT 500;
```

See the ai_query documentation for supported model types and the [batch inference](/concepts/batch-inference-on-databricks.md) guide for building production pipelines. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Related Concepts

- Batch Inference — Running AI predictions on large datasets at once
- ai_query — The general-purpose AI function
- [Model Serving](/concepts/model-serving.md) — Real-time inference for deployed models
- [Deploy models for batch inference](/concepts/batch-inference-pipelines.md) — End-to-end pipeline guidance

## Sources

- deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md

# Citations

1. [deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md](/references/deploy-models-for-batch-inference-and-prediction-databricks-on-aws-5481092c.md)
