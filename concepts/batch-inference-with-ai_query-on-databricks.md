---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad7330f1b142c190b60a1482602a612d9ce2e2d900b4c423d8c656c9300471ff
  pageDirectory: concepts
  sources:
    - model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - batch-inference-with-ai_query-on-databricks
    - BIWAOD
  citations:
    - file: model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md
title: Batch Inference with ai_query on Databricks
description: Databricks recommends using the ai_query AI function as the modern replacement for legacy Hugging Face batch inference patterns
tags:
  - ai-query
  - batch-inference
  - databricks
timestamp: "2026-06-19T19:43:14.864Z"
---

# Batch Inference with ai_query on Databricks

**Batch inference with `ai_query` on Databricks** refers to the practice of using Databricks' AI Functions — specifically the `ai_query()` SQL function — to perform model inference on large volumes of data in a batch processing manner. This approach replaces older methods of batch inference, such as wrapping models with Pandas UDFs for distributed computation on Spark clusters. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Overview

Databricks provides the `ai_query` function as part of its AI Functions, enabling users to enrich data by querying AI models directly from SQL. This function can be used for batch inference by applying it to columns in a DataFrame or table, allowing for efficient processing of large datasets without the need to manually manage model serving infrastructure or distributed computation logic. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Recommended Approach

Databricks recommends using `ai_query` for batch inference as the preferred method over legacy approaches. The older documentation for Hugging Face Transformers inference using Pandas UDFs has been retired in favor of this newer, more streamlined approach. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

Key advantages include:

- **Simplified syntax**: Inference can be performed using standard SQL queries.
- **No manual UDF management**: Eliminates the need to write and maintain Pandas UDFs for model wrapping.
- **Integrated with Databricks SQL**: Works directly within Databricks SQL environments.
- **Scalable**: Leverages Databricks' infrastructure for distributed processing.

## Comparison with Legacy Methods

| Aspect | Pandas UDF Approach (Legacy) | ai_query Approach (Recommended) |
|---|---|---|
| Syntax | Python UDF with decorators | SQL function call |
| Model hosting | Loaded on cluster workers | Managed model serving |
| Resource management | Manual GPU/CPU tuning | Automatic |
| Maintenance | Higher code complexity | Lower code complexity |

^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Use Cases

Batch inference with `ai_query` is suitable for:

- Natural Language Processing (NLP) tasks such as translation, summarization, and named entity recognition
- [Large Language Model (LLM)](/concepts/large-language-models-llms-on-databricks.md) inference on tabular data
- [Model Serving](/concepts/model-serving.md) for offline scoring and enrichment pipelines
- Data enrichment workflows where each row requires model prediction

## Related Concepts

- [AI Functions on Databricks](/concepts/ai-functions.md) — The broader framework for AI-powered SQL functions
- Data Enrichment — The process of augmenting datasets with model predictions
- [Model Serving](/concepts/model-serving.md) — Deploying models for inference requests
- Batch Inference — Processing large volumes of data through a model in batches
- [Pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md) — Legacy approach for distributed model inference on Spark

## Sources

- model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md

# Citations

1. [model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md](/references/model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws-b5ae44ca.md)
