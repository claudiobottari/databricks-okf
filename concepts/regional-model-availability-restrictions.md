---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e98e53d09714270fb9689f9fcb95e4ebd39bee60731641cbd360faf62a26037
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - regional-model-availability-restrictions
    - RMAR
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Regional Model Availability Restrictions
description: Certain foundation models (e.g., Anthropic Claude Opus 4.1, Meta Llama 3.1 405B, BGE Large) are restricted to US regions only, while others are available in both EU and US regions.
tags:
  - model-availability
  - regions
  - foundation-model-apis
timestamp: "2026-06-19T18:54:06.825Z"
---

# Regional Model Availability Restrictions

**Regional Model Availability Restrictions** refer to the geographic limitations placed on certain [Foundation Model APIs](/concepts/foundation-model-apis.md) models within Databricks. These restrictions depend on the model itself, the deployment mode ([Pay-per-token](/concepts/pay-per-token-serving-mode.md) or [Provisioned Throughput](/concepts/provisioned-throughput.md)), and the workspace region. Compliance and infrastructure requirements determine which models are accessible in which regions. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Overview

Databricks Foundation Model APIs support a range of models that are not uniformly available in all supported regions. Two main categories of regional restrictions apply: models that are available **only in US regions** and models that are available in **both US and EU regions** (when the workspace is in a supported US or EU region). For workspaces in other supported Model Serving regions, cross‑geo data processing must be enabled to access EU/US models. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## US‑Only Models

The following models are supported only in Foundation Model APIs pay‑per‑token supported **US regions**:

- Anthropic Claude Opus 4.1
- Meta Llama 3.1 405B Instruct
- BGE Large (En)

Starting February 15, 2026, Meta‑Llama‑3.1‑405B‑Instruct will be retired. See [Retired Models Policy](/concepts/partner-model-retirement-policy.md) for the recommended replacement model and migration guidance. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## EU and US Models

The following models are available in [Pay-per-token](/concepts/pay-per-token-serving-mode.md) EU and US supported regions (see the official region support list for detailed coverage):

- OpenAI GPT‑5.5 Pro
- OpenAI GPT‑5.5
- OpenAI GPT‑5.4
- OpenAI GPT‑5.4 mini
- OpenAI GPT‑5.4 nano
- OpenAI GPT‑5.3 Codex
- OpenAI GPT‑5.2 Codex
- OpenAI GPT‑5.2
- OpenAI GPT‑5.1
- OpenAI GPT‑5.1 Codex Max
- OpenAI GPT‑5.1 Codex Mini
- OpenAI GPT‑5
- OpenAI GPT‑5 mini
- OpenAI GPT‑5 nano
- Anthropic Claude Fable 5
- Anthropic Claude Opus 4.8
- Anthropic Claude Opus 4.7
- Anthropic Claude Opus 4.6
- Anthropic Claude Opus 4.5
- Anthropic Claude Sonnet 4.6
- Anthropic Claude Sonnet 4.5
- Anthropic Claude Haiku 4.5
- Anthropic Claude Sonnet 4

If the workspace is not located in an EU or US region but is in a supported Model Serving region, you can enable [Cross‑Geo Data Processing](/concepts/cross-geo-data-processing.md) to access these models. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Cross‑Geo Data Processing

As part of providing Foundation Model APIs, Databricks might process your data outside of the region and cloud provider where your data originated. For workspaces in a Model Serving region that is *not* in the US or EU, cross‑geo data processing must be enabled before EU/US models can be invoked. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Pay-per-token](/concepts/pay-per-token-serving-mode.md)
- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md)
- [Cross-Geo Data Processing](/concepts/cross-geo-data-processing.md)
- [Model Serving](/concepts/model-serving.md)
- [Retired Models Policy](/concepts/partner-model-retirement-policy.md)
- Data Residency and Processing

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
