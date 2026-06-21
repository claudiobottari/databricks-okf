---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3ebb8d2021c0734411e5042c2d87a65df65e5f2d50e348977b44a4c55b2247a3
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-api-service-offerings
    - FMASO
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Foundation Model API Service Offerings
description: Three tiers of Databricks generative AI model access — pay-per-token, provisioned throughput, and fine-tuning — each with distinct retirement timelines and policies.
tags:
  - databricks
  - foundation-model-apis
  - service-tiers
timestamp: "2026-06-18T12:29:08.268Z"
---

# Foundation Model API Service Offerings

**Foundation Model API Service Offerings** are Databricks-managed services that provide access to state-of-the-art generative AI models through three distinct serving and training options: pay-per-token endpoints, provisioned throughput endpoints, and foundation model fine-tuning. Databricks maintains a model maintenance policy to update and retire models across these offerings, ensuring customers have access to the most capable and performant models. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Service Offerings

The three offerings are collectively referred to as Foundation Model APIs (for serving) and Foundation Model Fine-tuning (for training). They cover both Databricks-hosted models and partner models from OpenAI, Anthropic, and Google. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

- **Foundation Model APIs pay-per-token** – Serve models on a usage‑based pricing model, charging per input and output token. Supported chat and completion models are subject to retirement policies. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]
- **Foundation Model APIs provisioned throughput** – Reserve dedicated throughput for a model with guaranteed capacity and predictable pricing. This offering is recommended when long‑term support for a specific model version is required. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]
- **Foundation Model Fine-tuning** – Fine‑tune supported base models using your own data. The fine‑tuning offering is subject to its own retirement policy for base model families. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Model Retirement Policy

Databricks announces planned retirements for models served or fine‑tuned through these offerings. The retirement timelines differ by offering and model category. For partner models (OpenAI, Anthropic, Google), Databricks follows the partner’s deprecation timeline but may temporarily redirect traffic to a similar, backward‑compatible model to provide a longer transition window if the partner’s lead time is shorter than Databricks’ standard policy. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Pay‑per‑token Retirement Policy

The pay‑per‑token offering follows a specific retirement schedule (see the policy tables in the source document). After the retirement date, queries to the deprecated model fail. Databricks recommends migrating applications to the replacement model before that date. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Provisioned Throughput Retirement Policy

Retirement for provisioned throughput is handled at the model family level. Customers are given advance notice and a transition period. The provisioned throughput offering is the recommended choice if you require long‑term support for a specific model version. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Partner Model Retirement Policy

For third‑party partner models, Databricks generally applies the same deprecation timelines as for its own models. However, if a partner announces a retirement with less lead time than Databricks’ standard transition period, Databricks may redirect the model to a similar, backward‑compatible version (for example, version 3.0 → 3.1) at the same price. This redirection prevents immediate breakage and allows the full transition period to elapse before queries fail. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

### Fine‑tuning Retirement Policy

The Foundation Model Fine‑tuning offering has a separate retirement schedule for base model families. Customers must migrate to a recommended replacement base model family before the retirement date. After retirement, fine‑tuning is no longer available for that family. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Model Updates

Databricks may ship incremental model updates to deliver optimizations. When an update occurs, the endpoint URL remains the same, but the model ID in the response object changes to reflect the date of the update. For example, an update to `meta-llama/Meta-Llama-3.3-70B` shipped on 3/4/2024 results in the model name `meta-llama/Meta-Llama-3.3-70B-030424`. A version history of updates is maintained for reference. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Retired Models

The source document provides tables of current and upcoming model retirements for each offering, including retirement dates and recommended replacement models. Databricks strongly advises migrating to the replacement model before the indicated retirement date. For pay‑per‑token serving, if you require long‑term support for a specific model version, use provisioned throughput instead. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Finding Workloads Using Retired Models

To identify workloads that are still using deprecated models, Databricks provides a SQL query against the `system.serving` system tables. The query joins `endpoint_usage` with `served_entities` to return request counts, token consumption, and request timing grouped by requester and endpoint, filtered by a retired model name pattern. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs Pay-per-Token](/concepts/foundation-model-apis-pay-per-token.md)
- [Foundation Model APIs Provisioned Throughput](/concepts/foundation-model-apis-provisioned-throughput.md)
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md)
- [Model Maintenance Policy](/concepts/model-retirement-and-deprecation-policy.md)
- Generative AI serving
- [Provisioned Throughput](/concepts/provisioned-throughput.md)

## Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
