---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 554d8560751bf0e80a13a0f50d6b2c65f43bb80de800193c8613216a0cfdaa8a
  pageDirectory: concepts
  sources:
    - databricks-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-serving-mode
    - PTSM
  citations:
    - file: databricks-foundation-model-apis-databricks-on-aws.md
title: Provisioned throughput serving mode
description: Dedicated endpoints with performance guarantees, HIPAA compliance, fine-tuned model support, and optimized inference for production workloads on Databricks.
tags:
  - model-serving
  - production
  - performance
  - compliance
timestamp: "2026-06-19T14:50:32.037Z"
---

Here is the updated wiki page for "Provisioned throughput serving mode".

---

**Provisioned throughput** is a serving mode of [Foundation Model APIs](/concepts/foundation-model-apis.md) that provides endpoints with optimized inference for foundation model workloads requiring performance guarantees. Databricks recommends this mode for all production workloads. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Overview

Provisioned throughput addresses the needs of workloads that demand high throughput, low latency, or fine-tuned models, and it supports additional security requirements such as HIPAA compliance. Provisioned throughput endpoints are hosted by Databricks as part of the [Databricks Designated Services](https://docs.databricks.com/aws/en/resources/designated-services) tier, meaning they use [Databricks Geos](https://docs.databricks.com/aws/en/resources/databricks-geos) to manage data residency when processing customer content. ^[databricks-foundation-model-apis-databricks-on-aws.md]

Provisioned throughput also supports:

- **Base models of all sizes** – accessible via the Databricks Marketplace or downloaded from Hugging Face or other external sources and registered in [Unity Catalog](/concepts/unity-catalog.md).
- **Fine-tuned variants** of supported base models, including those trained on proprietary data.
- **Fully custom weights and tokenizers** – for models trained from scratch, continued pre‑trained, or other architectural variations (for example, CodeLlama variants).

This flexibility allows teams to bring their own model artifacts while still benefiting from Databricks-managed inference infrastructure. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Requirements

To use provisioned throughput endpoints, the following prerequisites must be met:

- A Databricks API token for authenticating endpoint requests.
- [Serverless compute](/concepts/serverless-gpu-compute.md) enabled in the workspace.
- A workspace located in a [supported provisioned throughput region](https://docs.databricks.com/aws/en/resources/feature-region-support#model-serving-aws).

^[databricks-foundation-model-apis-databricks-on-aws.md]

## Comparison with other serving modes

Provisioned throughput stands alongside two other Foundation Model API modes:

| Mode | Recommended use case |
|------|----------------------|
| **Pay-per-token** | Getting started, low-throughput or development workloads, quick proof-of-concepts. |
| **Provisioned throughput** | Production workloads requiring performance guarantees, high throughput, fine-tuned models, or HIPAA compliance. |
| **AI Functions** | Batch inference workloads using any generative AI or ML model. |

Each mode serves distinct workload profiles, and provisioned throughput is the only mode that offers SLA-backed performance guarantees for production traffic spikes. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Deploying a provisioned throughput endpoint

Provisioned throughput Foundation Model APIs are deployed through a step-by-step process documented in [Provisioned throughput Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis). The endpoint can be queried using the OpenAI-compatible API, the Foundation Model APIs Python SDK, the MLflow Deployments SDK, or the REST API. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The overarching API service that offers provisioned throughput as one of its modes.
- [Model Serving](/concepts/model-serving.md) – The Databricks platform for deploying and serving ML models.
- [Pay-per-token serving mode](/concepts/pay-per-token-serving-mode.md) – The consumption-based alternative for lower-volume use cases.
- [AI Functions](/concepts/ai-functions.md) – A separate mode optimized for batch inference workloads.
- [Unity Catalog](/concepts/unity-catalog.md) – Required for registering custom models used with provisioned throughput.
- [Serverless compute](/concepts/serverless-gpu-compute.md) – The underlying compute model required for provisioned throughput endpoints.

## Sources

- databricks-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-foundation-model-apis-databricks-on-aws.md](/references/databricks-foundation-model-apis-databricks-on-aws-f789bf37.md)
