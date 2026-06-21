---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 84cb9691333ff1ddb11f781e61b1529fe687b500b3deb37ddf5110a9d02f2f4a
  pageDirectory: concepts
  sources:
    - deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai_query-function
    - ai_query Function
  citations:
    - file: deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
title: ai_query function
description: A general-purpose AI function in Databricks SQL for running batch inference against supported foundation models
tags:
  - databricks
  - sql
  - ai-functions
  - llm
timestamp: "2026-06-19T18:29:44.931Z"
---

Here is the wiki page for `ai_query function`.

---

## ai_query Function

The **`ai_query` function** is a built-in, general-purpose [AI function](/concepts/ai-functions.md) in Databricks SQL for applying AI models to data stored on Databricks. It provides a flexible interface for batch inference without being tied to a specific task, making it useful when no task-specific AI function exists or when full control over the prompt is required. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Usage

`ai_query` is called inside a `SELECT` statement, typically with a table reference and optional filtering (such as `LIMIT`). It accepts a model specification and input text, and returns the model’s response for each row. Because it is general-purpose, it can be used for a wide variety of LLM-based tasks, including summarization, classification, and custom generation. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

For example, batch inference can be performed on a table using `ai_query` in place of a task-specific function like `ai_translate`. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Supported Models

For a complete list of model types and the associated models that `ai_query` supports, see the official Databricks documentation on ai_query supported models. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Batch Inference Context

`ai_query` is one of the options Databricks recommends for batch inference, alongside task-specific AI functions. When you need a model that does not have a dedicated task function, or when you want full control over the prompt sent to the model, `ai_query` serves as the general-purpose alternative. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

For guidance on building and scheduling batch inference pipelines, see [Deploy batch inference pipelines](/concepts/batch-inference-pipelines.md). ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

For real-time serving rather than batch processing, see [Model Serving](/concepts/model-serving.md).

## Related Concepts

- [AI Functions](/concepts/ai-functions.md) — The family of built-in SQL functions for applying AI on Databricks.
- Batch Inference — The practice of running a model on many records at once.
- ai_translate — A task-specific AI function for translation.
- [Deploy batch inference pipelines](/concepts/batch-inference-pipelines.md) — How to operationalize batch inference with `ai_query`.
- [Model Serving](/concepts/model-serving.md) — Real-time deployment of models.
- SQL Functions — General Databricks SQL function reference.

## Sources

- deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md

# Citations

1. [deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md](/references/deploy-models-for-batch-inference-and-prediction-databricks-on-aws-5481092c.md)
