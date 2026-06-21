---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9521d348ce28e819401608c8492cedbbca53bf2f08a645008682056be0ec0c3f
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-apis-pay-per-token
    - FMAP
    - FMAPI
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Foundation Model APIs Pay-per-Token
description: A Databricks offering that provides access to generative AI models with pay-per-token pricing, governed by a specific model retirement policy with defined transition periods.
tags:
  - databricks
  - foundation-model-apis
  - pricing
timestamp: "2026-06-19T10:43:28.953Z"
---

Here is the wiki page for "Foundation Model APIs Pay-per-Token", written based solely on the provided source material.

---

## Foundation Model APIs Pay-per-Token

**Foundation Model APIs Pay-per-Token** is a Databricks offering that provides access to generative AI models through an API where you are charged based on the number of input and output tokens processed. This offering is part of the [Foundation Model APIs](/concepts/foundation-model-apis.md) family, which also includes [Foundation Model APIs Provisioned Throughput](/concepts/foundation-model-apis-provisioned-throughput.md) and [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md). ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Overview

The pay-per-token model allows users to access supported chat and completion models without reserving dedicated capacity, paying only for the tokens consumed by each request. This model is suitable for variable or low-volume workloads where predictable throughput is not required. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Model Retirement Policy

Databricks maintains a model retirement policy for the Foundation Model APIs pay-per-token offering. This policy ensures that users receive advance notice when a model is scheduled for retirement, allowing time to migrate to replacement models. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

For partner models (those provided by OpenAI, Anthropic, and Google), Databricks generally follows the same deprecation timelines as for pay-per-token models. However, if a partner announces a deprecation with shorter notice than Databricks' standard transition period, Databricks may temporarily redirect the model to a similar, backwards-compatible version (typically an incremental model version) to bridge the gap. This redirection is only possible if the replacement model has the same price and is backwards compatible. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Model Updates

When Databricks ships incremental model updates, the endpoint URL remains the same. However, the model ID in the response object changes to reflect the date of the update. For example, if an update is shipped to `meta-llama/Meta-Llama-3.3-70B` on March 4, 2024, the model name in the response object updates to `meta-llama/Meta-Llama-3.3-70B-030424`. Databricks maintains a version history of these updates. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Migration Guidance

When a model is scheduled for retirement, Databricks recommends that you migrate your applications to use replacement models before the indicated retirement date. If you require long-term support for a specific model version, Databricks recommends using Foundation Model APIs [Provisioned Throughput](/concepts/provisioned-throughput.md) for your serving workloads. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Identifying Affected Workloads

Databricks provides a SQL query using the `system.serving` system tables to find workloads that use retired or deprecated models. The query joins `system.serving.endpoint_usage` with `system.serving.served_entities` to identify requesters, endpoint names, and usage statistics for models matching a given retired model name. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Related Concepts

- [Foundation Model APIs Provisioned Throughput](/concepts/foundation-model-apis-provisioned-throughput.md) — Reserved capacity offering for predictable workloads
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md) — Fine-tuning offering for customizing models
- Generative AI Models Maintenance Policy — The overarching policy covering all model offerings
- Model Retirement — Process and timelines for retiring models

### Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
