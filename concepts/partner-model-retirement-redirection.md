---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9ee19e777d83720bdbac4bf7ca6b9f12153fd2e62f1a1015bfb57aef33a87927
  pageDirectory: concepts
  sources:
    - generative-ai-models-maintenance-policy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partner-model-retirement-redirection
    - PMRR
  citations:
    - file: generative-ai-models-maintenance-policy-databricks-on-aws.md
title: Partner Model Retirement Redirection
description: A Databricks policy that temporarily redirects deprecated third-party models (OpenAI, Anthropic, Google) to similar versions when partners provide shorter notice than Databricks' standard transition period.
tags:
  - databricks
  - machine-learning
  - partner-models
  - api-redirection
timestamp: "2026-06-19T18:57:45.770Z"
---

# Partner Model Retirement Redirection

**Partner Model Retirement Redirection** is a Databricks mechanism that temporarily redirects requests from a retiring third‑party partner model to a similar version when the partner’s retirement timeline is shorter than Databricks’ standard deprecation period. This ensures that customers receive the full transition time promised by Databricks, even when the partner announces a shorter lead time. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Context

Partner models are those provided by third‑party partners — specifically OpenAI, Anthropic, and Google — that are available through Databricks’ [Foundation Model APIs](/concepts/foundation-model-apis.md). For these models, Databricks generally follows the same deprecation timelines and policies as for provisioned throughput and pay‑per‑token models. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

However, the retirement dates published by partners may be shorter than the transition periods that Databricks advertises. For example, if a pay‑per‑token model deprecation is announced with only one month’s lead time instead of the standard three months, Databricks redirects the model for an additional two months to prevent immediate breakage and allow time for migration. Queries fail at the end of the full three‑month period. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Conditions for Redirection

The redirection can occur only if both of the following conditions are met: ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

1. **Same price** – The replacement model must have the same price as the retiring model.
2. **Backwards compatible** – The replacement model must be backwards compatible with the retiring model’s input/output format and behaviour.

The replacement model is usually an incremental model version, such as version 3.0 versus 3.1. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Impact and Usage

Under redirection, API calls to the original model continue to succeed until the Databricks‑guaranteed transition period ends. Customers are expected to migrate their applications to the recommended replacement model before that final date. The redirection is transparent to the caller; the endpoint URL remains the same, but the model ID in the response object may change to reflect the updated version. ^[generative-ai-models-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [Model retirement policy](/concepts/model-retirement-policy-databricks.md) – The overarching policy for retiring models on Databricks.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The serving infrastructure through which partner models are provided.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – A serving option with dedicated throughput that may have different retirement policies.
- [Pay‑per‑token serving](/concepts/pay-per-token-serving-mode.md) – A consumption‑based serving option subject to the same retirement timelines.
- Retired models – List of models that have been or are scheduled for retirement.

## Sources

- generative-ai-models-maintenance-policy-databricks-on-aws.md

# Citations

1. [generative-ai-models-maintenance-policy-databricks-on-aws.md](/references/generative-ai-models-maintenance-policy-databricks-on-aws-d0d09539.md)
