---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 08c0e57f0b375f3b4f0c7e815b15ed5869d5e99ab419bcaf7a8c021da1ebf2bf
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-retirement-and-deprecation-policy
    - Deprecation Policy and Model Retirement
    - MRADP
    - Model Maintenance Policy
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Model Retirement and Deprecation Policy
description: Databricks Foundation Model APIs have a formal retirement policy for models, with specific retirement dates and recommended replacement models for migrating workloads.
tags:
  - databricks
  - lifecycle
  - model-management
timestamp: "2026-06-19T18:13:37.892Z"
---

Here is the wiki page for "Model Retirement and Deprecation Policy", based solely on the provided source material.

---

## Model Retirement and Deprecation Policy

The **Model Retirement and Deprecation Policy** outlines the lifecycle for models served through [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md). When a model is scheduled for retirement, Databricks provides a deprecation period during which customers can migrate to a recommended replacement model. After the retirement date, API calls to the retired model may be temporarily redirected to an alternative model to allow additional migration time. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Deprecation and Retirement Process

When a model is announced for retirement, the relevant documentation includes the retirement date and a recommended replacement model. Customers are expected to migrate their workloads during the deprecation period. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

In some cases, after the official retirement date, API calls to the retired model are temporarily redirected to a newer or replacement model. For example, Google Gemini 3 Pro Preview was retired on March 26, 2026; between that date and June 7, 2026, API calls to Gemini 3 Pro were redirected to Gemini 3.1 Pro. The pricing for both models was identical during this period. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Retired Models

The following models have been announced for retirement with specific dates and replacement guidance:

| Model | Retirement Date | Replacement / Notes |
|-------|----------------|---------------------|
| OpenAI GPT-5.2 Codex | July 16, 2026 | Recommended replacement and migration guidance is available in the retired models documentation. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| OpenAI GPT-5.1 Codex Max | July 16, 2026 | Recommended replacement and migration guidance is available in the retired models documentation. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| OpenAI GPT-5.1 Codex Mini | July 16, 2026 | Recommended replacement and migration guidance is available in the retired models documentation. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| Meta-Llama-3.1-405B-Instruct | February 15, 2026 (pay-per-token); May 15, 2026 (provisioned throughput) | Recommended replacement and migration guidance is available in the retired models documentation. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| Google Gemini 3 Pro Preview | March 26, 2026 | API calls redirected to Gemini 3.1 Pro until June 7, 2026; pricing identical. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |

### Implementation for Provisioned Throughput

For provisioned throughput workloads, the retirement date may differ from pay-per-token endpoints. The documentation for each model specifies the retirement timeline for both modes. For example, Meta-Llama-3.1-405B-Instruct has a pay-per-token retirement date of February 15, 2026, and a provisioned throughput retirement date of May 15, 2026. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The serving infrastructure for these models.
- [Pay-per-token Foundation Model APIs](/concepts/pay-per-token-foundation-model-apis.md) — Modes of model access.
- [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md) — Modes of model access for production workloads.

### Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
