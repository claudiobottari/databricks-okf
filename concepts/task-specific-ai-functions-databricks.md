---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 529459bc9fa38d65ccecbe90338c3482a3c448cdab8cd3973818e59503d7bc5e
  pageDirectory: concepts
  sources:
    - deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - task-specific-ai-functions-databricks
    - TAF(
  citations:
    - file: deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
title: Task-Specific AI Functions (Databricks)
description: Specialized built-in AI functions such as ai_translate for targeted batch inference tasks without needing to specify a model.
tags:
  - databricks
  - ai
  - llm
  - nlp
timestamp: "2026-06-18T15:26:12.793Z"
---

# Task-Specific AI Functions (Databricks)

**Task-Specific AI Functions** are built-in SQL functions in Databricks that allow users to apply AI capabilities directly to data stored in Databricks without needing to manage models or infrastructure. These functions provide a simplified interface for common AI tasks such as translation, summarization, and classification.

## Overview

Task-specific AI functions are part of Databricks' AI Functions framework, which enables batch inference directly from SQL queries. Unlike the general-purpose `ai_query` function, task-specific functions are designed for particular use cases and provide a more intuitive, purpose-built interface for common AI operations. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Available Functions

The task-specific AI functions include:

- **`ai_translate()`** – Translates text from one language to another
- **`ai_summarize()`** – Generates summaries of text content
- **`ai_classify()`** – Classifies text into predefined categories
- **`ai_extract()`** – Extracts structured information from unstructured text
- **`ai_mask()`** – Masks sensitive information in text

For the complete list of available task-specific functions, see the Databricks documentation on [AI Functions](https://docs.databricks.com/aws/en/large-language-models/ai-functions). ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Batch Inference with Task-Specific Functions

Task-specific AI functions are designed for batch inference workflows. You can apply them to entire tables or subsets of data using standard SQL queries. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

### Example: Batch Translation

The following example uses `ai_translate` to translate a column of text summaries from English to Chinese:

```sql
SELECT
  writer_summary,
  ai_translate(writer_summary, "cn") AS cn_translation
FROM user.batch.news_summaries
LIMIT 500;
```

To perform batch inference on an entire table, remove the `LIMIT` clause from the query. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Comparison with `ai_query`

| Feature | Task-Specific Functions | `ai_query` |
|---------|------------------------|------------|
| Interface | Purpose-built for specific tasks | General-purpose |
| Use case | Translation, summarization, classification, etc. | Any model query |
| Syntax | `ai_translate(text, target_lang)` | `ai_query(model, prompt)` |
| Model selection | Automatic (pre-configured) | User-specified |

The general-purpose `ai_query` function supports a wider range of models and use cases. See the [supported models documentation](https://docs.databricks.com/aws/en/large-language-models/ai-query#supported-models) for details. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Best Practices

- **Use task-specific functions for common operations** – They provide a simpler interface and handle model selection automatically.
- **Use `ai_query` for custom or advanced use cases** – When you need to specify a particular model or craft custom prompts.
- **Limit batch sizes during development** – Use `LIMIT` clauses to test queries on small subsets before running on full tables.
- **Consider performance** – Batch inference on large tables may require significant compute resources.

## Related Concepts

- ai_query function|ai_query Function – The general-purpose AI function for custom model queries
- [Batch Inference Pipelines](/concepts/batch-inference-pipelines.md) – Structured workflows for production batch inference
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) – Real-time model serving for interactive applications
- Databricks SQL – The SQL environment where AI functions are executed
- [Large Language Models on Databricks](/concepts/large-language-models-llms-on-databricks.md) – Overview of LLM capabilities in the platform

## Sources

- deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md

# Citations

1. [deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md](/references/deploy-models-for-batch-inference-and-prediction-databricks-on-aws-5481092c.md)
