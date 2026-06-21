---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 688e3a4c417e90a5b7c63318446d1422a10f0eae285efeedafb3d6c1256fb93a
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cross-geography-routing-for-global-endpoints
    - CRFGE
    - Cross Geography Routing
    - cross geography routing
    - cross‑geography routing
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Cross-Geography Routing for Global Endpoints
description: Some hosted models require enabling cross-geography routing to be accessible via global endpoints, as noted for OpenAI GPT-5.1 Codex models and Google Gemini 3 Pro Preview.
tags:
  - databricks
  - data-residency
  - networking
timestamp: "2026-06-19T09:52:50.166Z"
---

Here is the wiki page for "Cross-Geography Routing for Global Endpoints", written based solely on the provided source material.

---

## Cross-Geography Routing for Global Endpoints

**Cross-Geography Routing for Global Endpoints** is a configuration setting that controls whether a model endpoint hosted by Databricks can route inference requests across geographic boundaries. When enabled, certain model endpoints that are hosted on global infrastructure can process requests in regions outside the user's primary workspace geography.

This setting is required for specific Databricks-hosted foundation models that are served through global endpoints rather than region-specific endpoints. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Models Requiring Cross-Geography Routing

Several models offered through Databricks Foundation Model APIs are hosted on global endpoints and explicitly require cross-geography routing to be enabled. These include:

- **OpenAI GPT-5.1 Codex Max** (`databricks-gpt-5-1-codex-max`) ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **OpenAI GPT-5.1 Codex Mini** (`databricks-gpt-5-1-codex-mini`) ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Google Gemini 3 Pro Preview** (`databricks-gemini-3-pro`) ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

These models are noted as being "hosted on a global endpoint" in their documentation, and users must enable cross-geography routing to use them. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## How to Enable

To enable cross-geography routing for global endpoints, users must configure the appropriate setting in their Databricks workspace. The source material references the Databricks documentation on [cross-geography processing](https://docs.databricks.com/aws/en/resources/databricks-geos#cross-geo-processing) for the specific steps. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The service through which these models are accessed.
- [Databricks-hosted foundation models](/concepts/databricks-hosted-foundation-models.md) – The full list of supported models.
- [Supported Models for Provisioned Throughput](/concepts/pay-per-token-vs-provisioned-throughput-modes.md) – An alternative deployment mode for production workloads that may have different geographic restrictions.
- [Databricks Geos and Data Residency](/concepts/databricks-geos-and-data-residency.md) – The broader policy framework for data processing locations.

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
