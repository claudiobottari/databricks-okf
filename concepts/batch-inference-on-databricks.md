---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c1d13d4d30e7d0a348fd67f097c809ef1d8663e40893ccf76c58d30c5c97caae
  pageDirectory: concepts
  sources:
    - deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - batch-inference-on-databricks
    - BIOD
    - Batch Inference Notebooks
    - Batch Inference on Spark DataFrames
    - batch inference
  citations:
    - file: deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
title: Batch Inference on Databricks
description: Databricks' recommended approach for running batch predictions on large datasets using AI Functions and SQL queries
tags:
  - machine-learning
  - batch-inference
  - databricks
timestamp: "2026-06-19T18:29:31.343Z"
---

```markdown
# Batch Inference on Databricks

**Batch inference** on Databricks is the process of applying a pre‑trained machine learning model to a large dataset all at once, rather than serving predictions in real‑time. Databricks recommends using [[AI Functions]] for most batch inference workloads because they are built directly into SQL and require no additional infrastructure. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

For real‑time model serving, see [[Model Serving]]. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## AI Functions for Batch Inference

[[AI Functions]] are built-in SQL functions that apply AI capabilities to data stored in Databricks. They support two styles of batch inference: task‑specific functions and the general‑purpose `ai_query` function. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

### Task‑Specific AI Functions

Task‑specific functions handle common operations such as translation, summarization, or classification. The following example uses `ai_translate` to translate a text column into Chinese: ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

```sql
SELECT
  writer_summary,
  ai_translate(writer_summary, "cn") AS cn_translation
FROM user.batch.news_summaries
LIMIT 500;
```

To run inference on an entire table, remove the `LIMIT` clause. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

### General‑Purpose AI Function

The `ai_query` function works with a wide range of model types and supported models. It is the recommended choice when no task‑specific function exists for the required operation. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

See the list of supported models for `ai_query` in the official documentation. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Batch Inference Pipelines

For workflows that require custom preprocessing, postprocessing, or orchestration logic, Databricks offers [[batch inference pipelines]]. These pipelines can be built using frameworks such as Delta Live Tables or Databricks Workflows and provide full control over the inference process. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md] *(Note: The source only references the existence of batch inference pipelines; specific tools are common extensions.)*

## Choosing an Approach

| Approach | Best For |
|----------|----------|
| AI Functions (task‑specific or `ai_query`) | Simple SQL‑based inference, quick ad‑hoc analysis, integration with existing SQL workflows |
| Batch Inference Pipelines | Complex preprocessing, multi‑step workflows, scheduled production jobs |

## Related Concepts

- [[AI Functions]] – Built‑in SQL functions for applying AI to data
- ai_query function|ai_query Function – General‑purpose AI inference function
- [[Model Serving]] – Real‑time model serving (alternative to batch inference)
- [[Batch Inference Pipelines]] – Full‑featured pipeline approach for complex batch inference

## Sources

- deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
```

# Citations

1. [deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md](/references/deploy-models-for-batch-inference-and-prediction-databricks-on-aws-5481092c.md)
