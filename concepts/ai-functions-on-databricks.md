---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0e3abab79d3725e4c3a67a26ef32c1e93bf790c1edf15d77c6ad9bdd675990b2
  pageDirectory: concepts
  sources:
    - deploy-models-using-model-serving-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-functions-on-databricks
    - AFOD
    - Transactions on Databricks
  citations:
    - file: deploy-models-using-model-serving-databricks-on-aws.md
title: AI Functions on Databricks
description: SQL-callable functions tightly integrated with Model Serving for batch inference, allowing users to enrich data using pre-provisioned or custom models directly from analytics workflows.
tags:
  - sql
  - batch-inference
  - analytics
timestamp: "2026-06-19T15:10:40.324Z"
---

Here is the wiki page for "AI Functions on Databricks".

---

## AI Functions on Databricks

**AI Functions** on Databricks are SQL functions that integrate large language model (LLM) capabilities directly into SQL analytics workflows. They allow users to perform [batch inference](/concepts/batch-inference-on-databricks.md) and enrich data with the output of generative AI models without needing to set up or manage a separate model serving infrastructure. ^[deploy-models-using-model-serving-databricks-on-aws.md]

### Overview

AI Functions provide a unified SQL interface for querying both [Databricks-hosted foundation models](/concepts/databricks-hosted-foundation-models.md) and [External Models](/concepts/external-models.md) (such as those from OpenAI or Anthropic). They are exposed through the `ai_query()` function and a set of task-specific AI Functions. ^[deploy-models-using-model-serving-databricks-on-aws.md]

These functions are tightly integrated with [Model Serving](/concepts/model-serving.md), which is the Databricks solution for deploying AI and ML models for real-time serving and batch inference. ^[deploy-models-using-model-serving-databricks-on-aws.md]

### Key Benefits

- **No endpoint configuration required** – When using pre-provisioned models that are hosted and managed by Databricks, you do not need to configure a model serving endpoint yourself. ^[deploy-models-using-model-serving-databricks-on-aws.md]
- **Unified interface** – Model Serving provides a single REST API for CRUD and querying tasks, and a single UI to manage all models and serving endpoints. ^[deploy-models-using-model-serving-databricks-on-aws.md]
- **Analytics integration** – You can access models directly from SQL using AI Functions, enabling easy integration into analytics workflows. ^[deploy-models-using-model-serving-databricks-on-aws.md]

### Use Cases

The primary use case for AI Functions is enriching data with AI in batch inference pipelines. This includes tasks such as:

- Generating summaries or embeddings for large datasets.
- Applying classification or extraction logic from LLMs to tabular data.
- Running inference across millions of rows in parallel within a single SQL query.

### How to Get Started

- For performing batch inference, see Enrich data using AI Functions.
- For an introductory tutorial on how to serve custom models on Databricks for real-time inference, see Tutorial: Deploy and query a custom model.
- For a getting-started tutorial on how to query a foundation model on Databricks for real-time inference, see Get started querying LLMs on Databricks.

### Related Concepts

- [Model Serving](/concepts/model-serving.md) – The underlying infrastructure that serves models for both real-time and batch inference.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The API pathway for querying Databricks-hosted foundation models.
- [External Models](/concepts/external-models.md) – Models hosted outside of Databricks that are accessible through AI Functions.
- SQL Analytics – The analytics workspace where AI Functions are executed.
- MLflow Deployment API – The deployment API that supports CRUD operations for serving endpoints.
- AI Functions API Reference – Reference documentation for the `ai_query()` function and all task-specific AI Functions.

### Sources

- deploy-models-using-model-serving-databricks-on-aws.md

# Citations

1. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
