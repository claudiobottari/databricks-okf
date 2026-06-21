---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf525e52b9d36bbd172e1432eb1e032d59f119c0425afc62d5abba4c39238a25
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - regional-model-availability-databricks-foundation-model-apis
    - RMA(FMA
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Regional Model Availability (Databricks Foundation Model APIs)
description: Restrictions on which foundation models are available in US-only vs. EU-and-US regions, with cross-Geo processing as an option for non-EU/non-US workspaces.
tags:
  - databricks
  - regions
  - model-serving
timestamp: "2026-06-18T12:24:40.208Z"
---

# Regional Model Availability (Databricks Foundation Model APIs)

**Regional Model Availability** refers to the geographic restrictions that apply to specific foundation models served through Databricks Foundation Model APIs. These restrictions are based on compliance requirements, infrastructure deployment, and data residency policies. Availability differs between pay-per-token and provisioned throughput deployment modes. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Overview

Certain models hosted by Databricks Foundation Model APIs are only available in limited geographic regions. The availability is defined by whether a model can be served in US data regions, EU data regions, or both. Workspaces located outside US or EU regions may need to enable cross-geo data processing to access models that are only supported in US or EU. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

For pay-per-token workloads, the following regional categories apply:

| Category | Description |
|----------|-------------|
| **US-only models** | Supported only in Foundation Model APIs pay-per-token supported US regions |
| **EU and US models** | Available in both pay-per-token EU and US supported regions |

Provisioned throughput workloads may have different region availability; see Model Serving Limits and Regions for details.

## US-Only Models

The following models are supported **only** in Foundation Model APIs pay-per-token supported US regions: ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

- **Anthropic Claude Opus 4.1**
- **Meta Llama 3.1 405B Instruct** – Starting February 15, 2026, this model will be retired. See [Retired Models Policy](/concepts/partner-model-retirement-policy.md) for replacement recommendations and migration guidance.
- **BGE Large (En)**

Workspaces in non-US regions cannot serve these models unless cross-geo data processing is enabled, and then only if the workspace resides in a supported Model Serving region.

## EU and US Models

The following models are available in **both pay-per-token EU and US supported regions** (see Feature Region Support – Model Serving):

| Provider | Models |
|----------|--------|
| **OpenAI** | GPT-5.5 Pro, GPT-5.5, GPT-5.4, GPT-5.4 mini, GPT-5.4 nano, GPT-5.3 Codex, GPT-5.2 Codex, GPT-5.2, GPT-5.1, GPT-5.1 Codex Max, GPT-5.1 Codex Mini, GPT-5, GPT-5 mini, GPT-5 nano |
| **Anthropic Claude** | Fable 5, Opus 4.8, Opus 4.7, Opus 4.6, Opus 4.5, Sonnet 4.6, Sonnet 4.5, Haiku 4.5, Sonnet 4 |

If your workspace is not located in an EU or US region but is in a supported Model Serving region, you can enable [Cross-Geo Data Processing](/concepts/cross-geo-data-processing.md) to access these models. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Implications for Provisioned Throughput

Provisioned throughput workloads may support the same or additional regions depending on the compliance profile selected (e.g., HIPAA, PCI-DSS, FedRAMP). Refer to [Compliance Standards for Foundation Model APIs](/concepts/foundation-model-apis-limits-and-compliance.md) and Model Serving Limits for region-specific availability of provisioned throughput deployments.

## Related Concepts

- Foundation Model APIs Overview
- [Pay-per-Token vs Provisioned Throughput](/concepts/pay-per-token-vs-provisioned-throughput-modes.md)
- [Cross-Geo Data Processing](/concepts/cross-geo-data-processing.md)
- Feature Region Support
- [Retired Models Policy](/concepts/partner-model-retirement-policy.md)
- [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md)

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
