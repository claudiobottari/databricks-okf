---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 106595e3a4265d53445fe3e8478cb9c3503bae7f0663cac5423688aaae725e3b
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-security-perimeter
    - DSP
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Databricks Security Perimeter
description: A security boundary within which Databricks hosts third-party foundation model endpoints, ensuring data does not leave the Databricks-controlled environment.
tags:
  - security
  - databricks
  - model-serving
  - compliance
timestamp: "2026-06-18T15:07:39.002Z"
---

# Databricks Security Perimeter

The **Databricks security perimeter** is a secure hosting environment within Databricks infrastructure where certain foundation model endpoints are deployed. Models hosted inside this perimeter are served directly by Databricks, ensuring that inference requests and data processing remain within Databricks' controlled boundary. The term is used in the Databricks documentation to distinguish these endpoints from models hosted externally or on global endpoints that may require cross-geography routing. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Models Hosted Within the Security Perimeter

The following models are explicitly documented as being hosted by Databricks within the Databricks security perimeter. All of these endpoints use the `databricks-` prefix in their endpoint names.

### OpenAI Models (GPT series)
- `databricks-gpt-5-5-pro`
- `databricks-gpt-5-5`
- `databricks-gpt-5-4`
- `databricks-gpt-5-4-mini`
- `databricks-gpt-5-4-nano`
- `databricks-gpt-5-3-codex`
- `databricks-gpt-5-2-codex`
- `databricks-gpt-5-2`
- `databricks-gpt-5-1`
- `databricks-gpt-5-1-codex-max`
- `databricks-gpt-5-1-codex-mini`
- `databricks-gpt-5`
- `databricks-gpt-5-mini`
- `databricks-gpt-5-nano`

### Google Gemini Models
- `databricks-gemini-3-1-flash-lite`
- `databricks-gemini-3-5-flash`
- `databricks-gemini-3-flash`
- `databricks-gemini-3-1-pro`
- `databricks-gemini-3-pro`
- `databricks-gemini-2-5-pro`
- `databricks-gemini-2-5-flash`

### Anthropic Claude Models
- `databricks-claude-haiku-4-5`
- `databricks-claude-sonnet-4-6`
- `databricks-claude-sonnet-4-5`
- `databricks-claude-fable-5`
- `databricks-claude-opus-4-8`
- `databricks-claude-opus-4-7`
- `databricks-claude-opus-4-6`
- `databricks-claude-opus-4-5`
- `databricks-claude-sonnet-4`
- `databricks-claude-opus-4-1`

^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Models Not Explicitly Listed Within the Security Perimeter

Several other foundation models offered through Databricks Foundation Model APIs are not documented as being hosted within the Databricks security perimeter. These include open-weight models such as Llama 4 Maverick, Meta-Llama variants, Qwen models, GPT OSS models, Gemma 3 12B, and embedding models (GTE Large, BGE Large). The absence of the security perimeter statement may indicate different hosting arrangements (e.g., global endpoints or external providers). ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Implications

Hosting within the Databricks security perimeter provides customers with assurance that model inference occurs entirely on Databricks-managed infrastructure, without data leaving the Databricks environment. This is particularly relevant for customers with strict data residency or compliance requirements. For models not hosted within the perimeter, additional considerations such as cross-geography routing requirements may apply (e.g., global endpoints must have [cross geography routing](/concepts/cross-geography-routing-for-global-endpoints.md) enabled). ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The service hosting these models.
- [Pay-per-Token Endpoints](/concepts/pay-per-token-endpoints.md) — Usage mode for the listed models.
- [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md) — Alternative deployment mode.
- Global endpoints — Endpoints that require cross-geography routing.
- [Model Serving](/concepts/model-serving.md) — General model deployment on Databricks.

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
