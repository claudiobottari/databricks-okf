---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f8680eb17d7915dd61bfdb37bd07b0b5b724f9264c6cf35f021d35d386ddadd
  pageDirectory: concepts
  sources:
    - deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - task-specific-ai-functions-vs-general-purpose-ai-functions
    - TAFVGAF
  citations:
    - file: deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
title: Task-Specific AI Functions vs General-Purpose AI Functions
description: Databricks distinguishes between task-specific AI functions (e.g., ai_translate for translation) and the general-purpose ai_query function for applying AI models in SQL.
tags:
  - databricks
  - sql
  - ai-functions
  - architecture
timestamp: "2026-06-19T15:10:18.930Z"
---

# Task-Specific AI Functions vs General-Purpose AI Functions

**Task-Specific AI Functions** and **General-Purpose AI Functions** are two categories of built-in functions in Databricks that enable applying AI to data stored on the platform. Both are used for [batch inference](/concepts/batch-inference-on-databricks.md) and prediction workflows, but they differ in scope and flexibility.

## Overview

AI Functions are built-in functions that you can use to apply AI on your data stored on Databricks. You can run batch inference using task-specific AI functions or the general purpose function, `ai_query`. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Task-Specific AI Functions

Task-specific AI functions are designed for particular AI tasks, such as translation, summarization, or classification. These functions provide a focused interface for common AI operations without requiring users to specify a model or configure complex parameters.

For example, `ai_translate` is a task-specific AI function that translates text from one language to another. The following query uses `ai_translate` to perform batch inference on a table of news summaries, translating the `writer_summary` column to Chinese: ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

```sql
SELECT
  writer_summary,
  ai_translate(writer_summary, "cn") as cn_translation
FROM user.batch.news_summaries
LIMIT 500;
```

To perform batch inference on an entire table, you can remove the `LIMIT 500` clause from the query. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## General-Purpose AI Function (`ai_query`)

The general-purpose function `ai_query` provides a more flexible interface for batch inference. Unlike task-specific functions, `ai_query` allows users to specify which model to use and can support a wider range of AI tasks. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

`ai_query` supports various model types and associated models. For details on which models are supported, see the documentation on supported models for `ai_query`. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Comparison

| Aspect | Task-Specific AI Functions | General-Purpose AI Function (`ai_query`) |
|--------|---------------------------|----------------------------------------|
| Purpose | Specific AI tasks (e.g., translation, summarization) | General AI inference across multiple tasks |
| Interface | Pre-defined function with task-specific parameters | Flexible query interface with model selection |
| Model Selection | Implicit (function determines the model) | Explicit (user specifies the model) |
| Use Case | Simple, common AI operations | Custom or varied AI workloads |

## When to Use Each

- **Task-specific AI functions** are ideal when you need to perform a common, well-defined AI task like translation or summarization with minimal configuration.
- **`ai_query`** is better suited for scenarios where you need flexibility in model selection or want to perform custom AI tasks not covered by task-specific functions.

## Related Concepts

- Batch Inference — Running AI predictions on large datasets stored in Databricks.
- [Batch Inference Pipelines](/concepts/batch-inference-pipelines.md) — Structured pipelines for deploying batch inference workflows.
- [Model Serving](/concepts/model-serving.md) — Real-time model serving for production applications.
- [AI Functions](/concepts/ai-functions.md) — The broader category of built-in AI functions in Databricks.

## Sources

- deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md

# Citations

1. [deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md](/references/deploy-models-for-batch-inference-and-prediction-databricks-on-aws-5481092c.md)
