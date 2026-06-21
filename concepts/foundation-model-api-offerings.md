---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8a75da19d0f03a2952af2b23425a35e0cec72ac5bc548df74f7439935c34d914
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - foundation-model-api-offerings
    - FMAO
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Foundation Model API Offerings
description: The three Databricks Foundation Model API service tiers — pay-per-token, provisioned throughput, and fine-tuning — each with distinct model retirement timelines and policies.
tags:
  - databricks
  - machine-learning
  - api-offerings
  - foundation-models
timestamp: "2026-06-19T18:58:04.678Z"
---

Here is the wiki page for "Foundation Model API Offerings".

---

## Foundation Model API Offerings

**Foundation Model API Offerings** on Databricks provide access to state-of-the-art generative AI models through pay-per-token and provisioned throughput endpoints, along with fine-tuning capabilities. Databricks offers models from multiple providers, including Meta, OpenAI, Anthropic, and Google, through these APIs. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Offerings

The Foundation Model APIs are available in three main tiers:

- **Foundation Model APIs pay-per-token**: A consumption-based pricing model where you pay only for the tokens used in each request. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]
- **Foundation Model APIs provisioned throughput**: A reserved capacity model that provides guaranteed throughput for serving workloads, recommended for applications requiring long-term support for a specific model version. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]
- **Foundation Model Fine-tuning**: An offering that allows you to customize foundation models on your own data. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Model Maintenance Policy

Databricks may update supported models or retire older models to continue supporting the most state-of-the-art models. The retirement policy explains how Databricks notifies you when a model is set for retirement, what happens during the transition period, and what to expect on the retirement date. Timelines differ by offering and model category. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

Retirement policies only impact supported chat and completion models. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

#### Partner Model Retirement Policy

Partner models are models provided by third-party partners—specifically OpenAI, Anthropic, and Google. Databricks generally follows the same deprecation timelines as for other models. However, if a partner provides a shorter retirement notice, Databricks attempts to bridge the gap by temporarily redirecting models to a similar version so customers receive the full transition time. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

This redirection can only occur if the replacement model has the same price and is backwards compatible. The replacement model is usually an incremental model version, like 3.0 versus 3.1. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Model Updates

Databricks may ship incremental model updates to deliver optimizations. When a model is updated, the endpoint URL remains the same, but the model ID in the response object changes to reflect the date of the update. For example, if an update is shipped to `meta-llama/Meta-Llama-3.3-70B` on March 4, 2024, the model name in the response object updates to `meta-llama/Meta-Llama-3.3-70B-030424`. Databricks maintains a version history of the updates. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Retired Models

Databricks publishes tables of current and upcoming model retirements for each offering, including retirement dates and recommended replacement models. Databricks recommends migrating applications to replacement models before the indicated retirement date. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

For applications requiring long-term support for a specific model version, Databricks recommends using Foundation Model APIs provisioned throughput. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Finding Workloads Using Retired Models

You can query the `system.serving` tables in SQL to find workloads using deprecated models and identify their owners. The query joins `endpoint_usage` with `served_entities` to retrieve requester, endpoint name, model name, request count, token counts, and time ranges. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Related Concepts

- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md)
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md)
- [Pay-per-Token Serving](/concepts/pay-per-token-serving-mode.md)
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md)
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md)

### Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
