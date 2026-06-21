---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 05fe87eea05e6e6f3d1b82d6a80c79e1b81d410eb501e2043a883f709ac8b620
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cross-geo-data-processing-databricks
    - CDP(
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Cross-Geo Data Processing (Databricks)
description: A mechanism allowing Foundation Model API requests to be processed outside the workspace's home region and cloud provider, required for workspaces in non-US/non-EU Model Serving regions.
tags:
  - databricks
  - data-residency
  - compliance
timestamp: "2026-06-18T12:24:45.514Z"
---



# Cross-Geo Data Processing (Databricks)

**Cross-Geo Data Processing** refers to the scenario where Databricks processes data from a user's workspace outside of the region and cloud provider where the data originated. This can occur when using [Foundational Model APIs](/concepts/foundation-model-apis.md) or other designated Databricks services, and is subject to specific compliance and availability requirements.

## Overview

As part of providing [Foundation Model APIs](/concepts/foundation-model-apis.md) and other cloud services, Databricks may process your data outside of the region and cloud provider where your data originated. This cross-geo processing is a standard operational characteristic of certain Databricks services and is documented in the Databricks Geos reference. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Geographic Considerations

The region and geography where your Foundation Model API requests are processed depends on your workspace region and the specific model being used. If your workspace is in a supported [Model Serving](/concepts/model-serving.md) region but not in a US or EU region, it must be enabled for cross-Geo data processing to access certain models. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Enabling Cross-Geo Data Processing

Cross-geo data processing must be explicitly enabled for workspaces that are located in supported [Model Serving](/concepts/model-serving.md) regions outside of the US or EU. Without this enablement, users in such regions cannot access pay-per-token models that are only available in US or EU regions. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### When Cross-Geo Processing Is Required

Cross-geo data processing is required when:

- Your workspace is in a supported [Model Serving](/concepts/model-serving.md) region but not in a US or EU region.
- You need to access models that are restricted to specific geographic regions (e.g., US-only models like Anthropic Claude Opus 4.1 or Meta Llama 3.1 405B Instruct).
- You need to access models that are available in pay-per-token EU and US supported regions (e.g., various OpenAI GPT models, Anthropic Claude models).

## Designated Services

For geographic areas that process pay-per-token and provisioned throughput workloads, see the [Designated Services](/concepts/databricks-designated-service-with-geos.md) documentation. This provides detailed information about which geographic regions process specific types of workloads. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Model Availability by Region

Certain models have regional restrictions based on compliance and infrastructure requirements. The following model categories are relevant to cross-geo data processing:

| Category | Region | Models |
|----------|--------|--------|
| US-only models | Only Foundation Model APIs pay-per-token supported US regions | Anthropic Claude Opus 4.1, Meta Llama 3.1 405B Instruct, BGE Large |
| EU and US models | Both pay-per-token EU and US supported regions | Various OpenAI GPT models (GPT-5 series), Anthropic Claude models (Opus 4.x, Sonnet, Haiku) |

If your workspace is not in an EU or US region but is in a supported Model Serving region, you can enable cross-Geo data processing to access these models. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Compliance and Security Considerations

- **Compliance Security Profile**: Cross-geo processing is subject to the same compliance standards as the underlying service. For pay-per-token workloads, only certain compliance standards (e.g., HIPAA) are supported.
- **Data Residency**: Cross-geo processing means your data may be processed in a different geographic region than where it was originally stored or generated.
- **Security**: Cross-geo processing respects existing workspace security configurations, including IP allowlists and PrivateLink configurations.

## Related Concepts

- Databricks Geos — Geographic regions where Databricks operates
- [Designated Services](/concepts/databricks-designated-service-with-geos.md) — Services subject to specific geographic processing
- [Foundational Model APIs](/concepts/foundation-model-apis.md) — The primary service requiring cross-geo processing
- [Model Serving](/concepts/model-serving.md) — The infrastructure that processes model requests
- Data Residency — Requirements for keeping data within specific geographic boundaries
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md) — The compliance standards applicable to cross-geo workloads

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
