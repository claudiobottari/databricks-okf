---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1dca42287de252e98afc80f3bd7f332cc4035248f62c46060f55777a1883a0b1
  pageDirectory: concepts
  sources:
    - foundation-model-apis-limits-and-quotas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-endpoints
    - PTE
    - Create provisioned throughput endpoints
  citations:
    - file: foundation-model-apis-limits-and-quotas-databricks-on-aws.md
    - file: foundation-model-rest-api-reference-databricks-on-aws.md
title: Provisioned throughput endpoints
description: Alternative to pay-per-token endpoints offering no TPM restrictions, higher rate limits (up to 200 QPS), and predictable performance for production workloads.
tags:
  - provisioned-throughput
  - production-workloads
  - databricks
timestamp: "2026-06-19T18:54:23.620Z"
---

# Provisioned Throughput Endpoints

**Provisioned Throughput Endpoints** are a deployment option for Databricks Foundation Model APIs that provide dedicated compute resources for serving models. They are designed for production workloads that require higher, predictable throughput and are not subject to the token-based rate limits that govern pay-per-token endpoints. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## How They Work

Unlike pay-per-token endpoints, which share resources across users and are throttled by input‑tokens‑per‑minute (ITPM), output‑tokens‑per‑minute (OTPM), and queries‑per‑hour (QPH) limits, provisioned throughput endpoints give you reserved capacity. There are **no token-per-minute restrictions**; processing capacity is determined solely by the amount of provisioned resources. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

Provisioned throughput endpoints support **higher rate limits – up to 200 queries per second per workspace** – and deliver **predictable performance** because dedicated resources isolate your workload from other tenants. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Creating and Configuring Endpoints

You can create a provisioned throughput endpoint using either the Serving UI or the [POST /api/2.0/serving-endpoints](https://docs.databricks.com/api/workspace/servingendpoints/create) API. These endpoints support **multiple models per endpoint** for A/B testing, as long as the served models expose the same API format (for example, both are chat models). ^[foundation-model-rest-api-reference-databricks-on-aws.md]

## Supported Models and Output Token Limits

Each supported model has a maximum output token limit when deployed on a provisioned throughput endpoint. The exact limits vary per model and are published in the [Foundation Model APIs limits documentation](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/limits). ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Additional Limitations for Specific Models

Some models have extra restrictions when used with provisioned throughput:

| Model | Limitation |
|-------|------------|
| **Llama 4 Maverick** | Support is in **Public Preview**. Autoscaling is not supported. Metrics panels are not supported. Traffic splitting (serving multiple models on the same endpoint) is not supported. |
| **Meta Llama models from `system.ai`** | Only the **Instruct** version can be deployed from Unity Catalog; base versions are not supported. |

^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Differences from Pay‑per‑Token Endpoints

| Feature | Pay‑per‑Token | Provisioned Throughput |
|---------|---------------|------------------------|
| Capacity model | Shared, rate‑limited | Reserved, dedicated |
| Rate limits | ITPM, OTPM, QPH enforced | No TPM limits; up to 200 QPS per workspace |
| Performance | Variable (shared resources) | Predictable (dedicated resources) |
| Usage cost | Per‑token pricing | Based on provisioned capacity |
| Best for | Development, low‑volume, variable usage | Production, sustained high‑volume workloads |

## Best Practices

- **Use provisioned throughput for production applications** with sustained usage patterns where rate limits on pay‑per‑token endpoints would be disruptive. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]
- **Plan capacity** to match your expected query volume, keeping in mind the model-specific output token limits and the 200 QPS workspace limit.
- **Monitor endpoint metrics** (latency, throughput, error rates) and scale provisioned resources as needed. Provisioned throughput endpoints are meant for predictable, high‑demand traffic.

## Related Concepts

- [Pay-per-token endpoint](/concepts/pay-per-token-endpoints.md) – The alternative deployment mode with token‑based rate limits.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The overarching service that provides both endpoint types.
- [Model Serving](/concepts/model-serving.md) – The platform that hosts provisioned throughput endpoints.
- [Rate limits](/concepts/rate-limits-and-timeouts-in-model-serving.md) – The enforcement mechanisms for pay‑per‑token endpoints (not applicable to provisioned throughput).
- A/B testing with multiple models – Using a single endpoint to serve multiple model versions.

## Sources

- foundation-model-apis-limits-and-quotas-databricks-on-aws.md
- foundation-model-rest-api-reference-databricks-on-aws.md

# Citations

1. [foundation-model-apis-limits-and-quotas-databricks-on-aws.md](/references/foundation-model-apis-limits-and-quotas-databricks-on-aws-f7287590.md)
2. [foundation-model-rest-api-reference-databricks-on-aws.md](/references/foundation-model-rest-api-reference-databricks-on-aws-26351d38.md)
