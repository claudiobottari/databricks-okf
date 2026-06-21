---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 53a48aa86a29b6c16e21a842215d80a8cb8cdc31aa2e3a4ffbe4cc5658458f9f
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - model-retirement-policy-on-databricks
    - MRPOD
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Model Retirement Policy on Databricks
description: A lifecycle management policy for Databricks-hosted foundation models that includes scheduled retirement dates, recommended replacement models, and migration guidance for deprecated endpoints.
tags:
  - databricks
  - model-lifecycle
  - deprecation
  - migration
timestamp: "2026-06-18T15:07:58.180Z"
---



# Model Retirement Policy on Databricks

**Model Retirement Policy on Databricks** describes the process, timelines, and migration guidance when a model hosted via [Foundation Model APIs](/concepts/foundation-model-apis.md) or [Provisioned Throughput](/concepts/provisioned-throughput.md) is scheduled for retirement. Databricks publishes retirement schedules to give customers advance notice and recommends alternative models to transition to.

## Policy

Databricks sets and communicates a retirement date for each model. When a model is retired, API calls to its endpoint stop working. The policy also identifies the recommended replacement model and provides migration guidance for customers to transition their workloads during the deprecation period. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Retired Models

The following models have announced retirement dates. See the individual model entries for details.

### OpenAI GPT-5.1 Codex Max (retiring July 16, 2026)

- **Endpoint name**: `databricks-gpt-5-1-codex-max`
- **Supported inputs**: text, image
- **Retirement date**: July 16, 2026
- **Replacement**: See Retired models for the recommended replacement model and migration guidance.

This model is hosted on a global endpoint and requires [cross geography routing](/concepts/cross-geography-routing-for-global-endpoints.md) to be enabled. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### OpenAI GPT-5.1 Codex Mini (retiring July 16, 2026)

- **Endpoint name**: `databricks-gpt-5-1-codex-mini`
- **Supported inputs**: text, image
- **Retirement date**: July 16, 2026
- **Replacement**: See Retired models for the recommended replacement model and migration guidance.

This model is hosted on a global endpoint and requires [cross geography routing](/concepts/cross-geography-routing-for-global-endpoints.md) to be enabled. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Google Gemini 3 Pro Preview (retiring March 26, 2026)

- **Endpoint name**: `databricks-gemini-3-pro`
- **Supported inputs**: text, image, video, audio
- **Retirement date**: March 26, 2026
- **Migration window**: Between March 26, 2026 and June 7, 2026, API calls to Gemini 3 Pro will be temporarily redirected to Gemini 3.1 Pro. The pricing for both models is identical.
- **Replacement**: See Retired models for the recommended replacement model and migration guidance.

This model is hosted on a global endpoint and requires [cross geography routing](/concepts/cross-geography-routing-for-global-endpoints.md) to be enabled. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### OpenAI GPT-5.2 Codex (retiring July 16, 2026)

- **Endpoint name**: `databricks-gpt-5-2-codex`
- **Supported inputs**: text, image
- **Retirement date**: July 16, 2026
- **Replacement**: See Retired models for the recommended replacement model and migration guidance. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Meta-Llama-3.1-405B-Instruct (retiring)

- **Endpoint name**: `databricks-meta-llama-3-1-405b-instruct`
- **Retirement dates**:
  - **Pay-per-token workloads**: Starting February 15, 2026
  - **Provisioned throughput workloads**: Starting May 15, 2026
- **Replacement**: See Retired models for the recommended replacement model and migration guidance. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Meta-Llama-3.1-70B-Instruct (replaced)

- **Endpoint name**: `databricks-meta-llama-3-1-70b-instruct`
- **Replacement**: Starting December 11, 2024, `Meta-Llama-3.3-70B-Instruct` replaces support for `Meta-Llama-3.1-70B-Instruct` in Foundation Model APIs pay-per-token endpoints. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The service through which these models are served.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – A serving mode that supports additional model architectures.
- [Pay-per-Token Pricing](/concepts/pay-per-token-pricing.md) – The pricing model for querying foundation models.
- Supported model architectures – The complete set of model families available through Foundation Model APIs.
- Retired models – The Databricks page listing all retired and deprecated models.

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
