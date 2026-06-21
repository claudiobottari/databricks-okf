---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c573ebc5248f0eb6de30a3c352a93742f8414f030e84d53c1df7e7261473bf1
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - regional-model-availability-us-vs-eu
    - RMA(VE
    - Regional Model Availability
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Regional Model Availability (US vs EU)
description: "Certain foundation models have geographic restrictions: some models are US-only (e.g., Anthropic Claude Opus 4.1, Meta Llama 3.1 405B), while others are available in both EU and US regions (e.g., OpenAI GPT-5.x series, Anthropic Claude models)."
tags:
  - regional-availability
  - foundation-model-apis
  - geographic-restrictions
timestamp: "2026-06-19T10:38:01.964Z"
---

# Regional Model Availability (US vs EU)

**Regional Model Availability (US vs EU)** refers to the geographic restrictions on which foundation models can be accessed through [Foundation Model APIs](/concepts/foundation-model-apis.md) in different workspace regions. Certain models are only available in US regions for pay-per-token workloads, while others are supported in both US and EU regions. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## US-Only Models

The following models are supported **only** in Foundation Model APIs pay-per-token supported US regions: ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

- Anthropic Claude Opus 4.1
- Meta Llama 3.1 405B Instruct
- BGE Large (En)

## EU and US Models

The following models are available in **both EU and US** pay-per-token supported regions: ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

**OpenAI Models:**
- OpenAI GPT-5.5 Pro
- OpenAI GPT-5.5
- OpenAI GPT-5.4
- OpenAI GPT-5.4 mini
- OpenAI GPT-5.4 nano
- OpenAI GPT-5.3 Codex
- OpenAI GPT-5.2 Codex
- OpenAI GPT-5.2
- OpenAI GPT-5.1
- OpenAI GPT-5.1 Codex Max
- OpenAI GPT-5.1 Codex Mini
- OpenAI GPT-5
- OpenAI GPT-5 mini
- OpenAI GPT-5 nano

**Anthropic Models:**
- Anthropic Claude Fable 5
- Anthropic Claude Opus 4.8
- Anthropic Claude Opus 4.7
- Anthropic Claude Opus 4.6
- Anthropic Claude Opus 4.5
- Anthropic Claude Sonnet 4.6
- Anthropic Claude Sonnet 4.5
- Anthropic Claude Haiku 4.5
- Anthropic Claude Sonnet 4

## Accessing Models from Non-EU/US Regions

If your workspace is not in an EU or US region but is in a supported Model Serving region, you can enable [Cross-Geo Data Processing](/concepts/cross-geo-data-processing.md) to access the models listed in the EU and US category. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Compliance Considerations

Regional model availability interacts with compliance standards. Pay-per-token workloads are HIPAA compliant, but other compliance standards (PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus) are not currently supported for pay-per-token workloads. [Provisioned Throughput](/concepts/provisioned-throughput.md) workloads support the full range of compliance standards and are recommended for workloads requiring certifications beyond HIPAA. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The service through which these models are accessed
- [Pay-per-token vs Provisioned Throughput](/concepts/pay-per-token-vs-provisioned-throughput-modes.md) — Deployment modes with different compliance support
- [Cross-Geo Data Processing](/concepts/cross-geo-data-processing.md) — Enabling access from non-EU/US regions
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md) — Security standards for model serving
- Model Serving Regions — Complete list of supported regions

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
