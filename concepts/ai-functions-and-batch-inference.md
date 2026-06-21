---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 21c28019fc526188c60e8f1e002f0fb9edf0712db2631839913f18ce1167aeac
  pageDirectory: concepts
  sources:
    - deploy-models-using-model-serving-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-functions-and-batch-inference
    - Batch Inference and AI Functions
    - AFABI
    - Batch Inference (AI Functions)
    - Batch Inference AI Functions
    - Batch inference (AI Functions)
    - batch inference (AI Functions)
  citations:
    - file: deploy-models-using-model-serving-databricks-on-aws.md
title: AI Functions and Batch Inference
description: Databricks SQL functions (including ai-query) tightly integrated with Model Serving to perform batch inference using pre-provisioned or custom models directly within analytics workflows.
tags:
  - batch-inference
  - sql
  - databricks
timestamp: "2026-06-18T15:26:24.128Z"
---

# AI Functions and Batch Inference

**AI Functions and Batch Inference** refers to the tight integration between [AI Functions](/concepts/ai-functions.md) (SQL-callable functions that invoke machine learning models) and [Model Serving](/concepts/model-serving.md) on Databricks, enabling users to perform large-scale batch inference directly from SQL without manually configuring serving endpoints for pre-provisioned models. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Overview

AI Functions provide a SQL interface to invoke foundation models and custom models, making it easy to embed AI capabilities into analytics workflows. When combined with Model Serving, AI Functions become the primary mechanism for batch inference scenarios. ^[deploy-models-using-model-serving-databricks-on-aws.md]

Model Serving offers a unified REST API and MLflow Deployment API for CRUD and querying tasks, and provides a single UI to manage all models and their serving endpoints. Users can access models directly from SQL using AI Functions for easy integration into analytics workflows. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Batch Inference with AI Functions

For batch inference, you can use any of the task-specific AI Functions or the generic `ai-query` function in your batch inference pipelines. If you choose to use a pre‑provisioned model that is hosted and managed by Databricks, you do not need to configure a model serving endpoint yourself—the integration handles it automatically. ^[deploy-models-using-model-serving-databricks-on-aws.md]

### Typical Workflow

1. **Prepare your data** in a Delta table or SQL view.
2. **Write a SQL query** that uses AI Functions (e.g., `ai_classify()`, `ai_generate()`, or `ai_query()`) to apply the model to each row or batch of rows.
3. **Execute the query** on a Databricks cluster or SQL warehouse; the batch inference runs by calling the underlying Model Serving endpoint or the pre‑provisioned model directly.
4. **Store the results** back into a table for downstream analytics or application consumption.

## Use Cases

- **Enrichment**: Augment existing datasets with model predictions, summaries, or classifications at scale.
- **Data transformation**: Use LLMs to translate, rewrite, or extract structured information from text columns.
- **Scoring**: Apply custom regression, classification, or ranking models to large batches of records.
- **Analytics integration**: Combine AI outputs with SQL aggregations, joins, and window functions for business intelligence.

## Requirements

- A Databricks workspace with [Model Serving](/concepts/model-serving.md) enabled and the necessary serverless compute entitlements.
- Access to a model—either a pre‑provisioned foundation model (e.g., Meta Llama) or a custom model deployed via Model Serving—that can be called through AI Functions.
- Appropriate permissions on the model and on the underlying data.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – The infrastructure that serves models for real-time and batch inference.
- [AI Functions](/concepts/ai-functions.md) – SQL-callable functions that invoke models.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Pre‑provisioned LLMs available for immediate use.
- Custom Models – User-trained models packaged in MLflow format.
- SQL Analytics – Using SQL to perform analytics and now AI inference.
- Batch Inference – Applying a model to a large dataset at once, as opposed to real-time single-record scoring.

## Sources

- deploy-models-using-model-serving-databricks-on-aws.md

# Citations

1. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
