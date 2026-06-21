---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c1cb132a81c6fdd2a20e0726b62a23820a41414c14e66e4b07834c1260e56b2
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-vs-pay-per-token
    - PTVP
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: Provisioned Throughput vs Pay-per-Token
description: "Two pricing models for Foundation Model APIs: pay-per-token for immediate use of base models, and provisioned throughput for production workloads with performance guarantees."
tags:
  - pricing
  - model-serving
  - performance
timestamp: "2026-06-19T09:37:24.157Z"
---

# Provisioned Throughput vs Pay-per-Token

**Provisioned Throughput** and **Pay-per-Token** are two pricing and capacity models offered by Databricks [Foundation Model APIs](/concepts/foundation-model-apis.md) for serving large language models. The choice between them depends on workload requirements, performance guarantees, and whether the model is a base model or a fine-tuned variant.

## Overview

Pay-per-token is the simpler, consumption-based model. Base models such as Meta-Llama-3.3-70B-Instruct and GTE-Large are available immediately with pay-per-token pricing. Databricks automatically creates dedicated endpoints for these models in your workspace, so you can start querying them without any manual endpoint setup. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

Provisioned throughput is designed for production workloads that need guaranteed performance. It allows you to deploy both base models and fine‑tuned models with committed throughput capacity. Endpoints must be explicitly created, typically via the REST API, and they provide performance guarantees that pay-per-token endpoints do not. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Key Differences

| Feature | Pay-per-Token | Provisioned Throughput |
|---------|---------------|------------------------|
| **Pricing** | Pay per token consumed | Pay for reserved throughput capacity |
| **Model support** | Base models only (e.g., Meta‑Llama‑3.3‑70B‑Instruct, GTE‑Large) | Base models and fine‑tuned models |
| **Performance guarantees** | None (best‑effort) | Yes – guaranteed throughput |
| **Endpoint setup** | Automatic – endpoints are pre‑created in the workspace | Manual – must create endpoint via UI, REST API, or MLflow Deployments SDK |
| **Use cases** | Experimentation, prototyping, low‑volume inference | Production workloads, high‑volume inference, latency‑sensitive applications |

Both models are served through [Model Serving](/concepts/model-serving.md) and can be queried using the same scoring APIs. For instructions on creating a provisioned throughput endpoint, see [Create provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md). ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## When to Use Each Model

- **Pay‑per‑token** is ideal for development, testing, and applications where traffic is low or unpredictable. Because no provisioning is required, you can start using the model immediately and only pay for what you consume.
- **Provisioned throughput** is suited for production applications that demand consistent latency and throughput. It is also the only option when you need to serve a fine‑tuned version of a foundation model.

## Related Resources

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Overview of available models and pricing.
- [Create provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) – Step‑by‑step guide for REST API creation.
- Score foundation models – How to query both types of endpoints.
- Model Serving limits – Regional availability and capacity constraints.

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
