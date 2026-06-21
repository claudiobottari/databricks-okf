---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d24bccaaeb289fdae84923778d10f5972d5a54d58c40d3c3e95f0ef6996e9dae
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cross-geo-data-processing-for-foundation-model-apis
    - CDPFFMA
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Cross-Geo Data Processing for Foundation Model APIs
description: Databricks may process Foundation Model API request data outside the region and cloud provider where it originated; workspaces outside US/EU regions must enable cross-Geo data processing to access certain models.
tags:
  - data-residency
  - compliance
  - foundation-model-apis
timestamp: "2026-06-19T10:37:50.185Z"
---

# Cross-Geo Data Processing for Foundation Model APIs

**Cross-Geo Data Processing for Foundation Model APIs** refers to the scenario where [Foundation Model API](/concepts/foundation-model-apis.md) requests submitted from a workspace in one geographic region are processed by inference infrastructure located in a different region or cloud provider. Databricks may process your data outside of the region and cloud provider where your data originated as part of delivering the Foundation Model APIs. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## When Cross-Geo Processing Is Required

Cross-geo processing is necessary when your workspace resides in a [Model Serving region](/concepts/model-serving.md) that is **not** in an EU or US geography. Workspaces in such regions must be explicitly enabled for cross-Geo data processing to use the pay-per-tier Foundation Model APIs. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

If your workspace is in a supported Model Serving region but is not an EU or US region, you cannot access many models (e.g., OpenAI GPT-5, Anthropic Claude Opus, Meta Llama) unless you enable cross-Geo processing. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Regional Model Availability

Certain models are restricted to specific geographies for compliance and infrastructure reasons. The following table summarizes the regional restrictions for pay-per-tier workloads:

| Region | Models |
|--------|--------|
| US-only | Anthropic Claude Opus 4.1, Meta Llama 3.1 405B Instruct, BGE Large (En) |
| EU and US | All other models listed (OpenAI GPT-5.x, Anthropic Claude Opus/Sonnet/Haiku, etc.) |

Workspaces outside the US or EU that want to use models classified as “EU and US” must enable cross-Geo processing. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Data Residency Implications

Because cross-geo processing sends request data to a different region, customers with strict data residency requirements should review the [Designated Services](/concepts/databricks-designated-service-with-geos.md) documentation to understand which geographic areas process pay-per-tier and provisioned throughput workloads. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The managed service for invoking hosted LLMs and embeddings.
- [Model Serving](/concepts/model-serving.md) – The underlying infrastructure for serving models.
- Databricks Geos – Geographic availability and data storage regions.
- [Designated Services](/concepts/databricks-designated-service-with-geos.md) – Geographic processing locations for specific workloads.
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md) – Security and compliance controls for Foundation Model APIs.
- Workspace Regions – Configuring and enabling cross-Geo processing at the workspace level.

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
