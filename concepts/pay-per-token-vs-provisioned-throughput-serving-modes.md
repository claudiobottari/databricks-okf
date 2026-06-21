---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8eaf38ec077711941b8296dd65ec539b9d695fbdc1d931b6fe6e447aa32da9c8
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - pay-per-token-vs-provisioned-throughput-serving-modes
    - PVPTSM
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Pay-per-token vs Provisioned Throughput Serving Modes
description: "Two distinct serving models in Databricks Foundation Model APIs: pay-per-token for consumption-based billing and provisioned throughput for production workloads with guaranteed capacity across model architecture families."
tags:
  - databricks
  - pricing
  - model-serving
  - production
timestamp: "2026-06-18T15:07:28.062Z"
---

# Pay-per-token vs Provisioned Throughput Serving Modes

**Pay-per-token** and **Provisioned Throughput** are two serving modes offered by [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) for deploying and querying large language models. The choice between them depends on workload characteristics, cost considerations, and performance requirements.

## Overview

Foundation Model APIs support both pay-per-token and provisioned throughput modes for serving models. Pay-per-token is a consumption-based pricing model where you are charged for each token processed, while provisioned throughput provides dedicated capacity for production workloads with predictable performance. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Pay-per-token Mode

In pay-per-token mode, you send query requests to model endpoints and are billed based on the number of input and output tokens processed. This mode is suitable for development, experimentation, and low-to-moderate volume workloads where cost predictability is less critical than flexibility. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Supported Models

Pay-per-token endpoints support a curated set of state-of-the-art open models. The specific model endpoint names available in pay-per-token mode are documented in the [pay-per-token supported models table](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/#token-foundation-apis). ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Provisioned Throughput Mode

Provisioned throughput mode provides dedicated serving capacity for production workloads. Databricks recommends provisioned throughput for production workloads because it offers predictable latency and throughput, which is essential for customer-facing applications and mission-critical systems. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Supported Architectures

Provisioned throughput supports all models of a model architecture family, including the fine-tuned and custom pre-trained models that are also supported in pay-per-token mode. The list of supported architectures is documented in the [Provisioned throughput Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/#throughput) documentation. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Comparison

| Aspect | Pay-per-token | Provisioned Throughput |
|--------|---------------|----------------------|
| Pricing model | Per-token consumption | Reserved capacity |
| Recommended use case | Development, experimentation, low-to-moderate volume | Production workloads |
| Performance | Shared, variable | Dedicated, predictable |
| Model support | Curated set of models | All models in supported architecture families, including fine-tuned and custom models |

## Choosing Between Modes

- **Use pay-per-token** when you are prototyping, running occasional inference, or have unpredictable or low-volume workloads where cost flexibility is important.
- **Use provisioned throughput** when you have production workloads that require consistent latency, high throughput, or guaranteed capacity. This is the recommended mode for production deployments. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The underlying API infrastructure for serving models
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) — General guidance for deploying models
- [AI Playground](/concepts/ai-playground.md) — Interactive interface for testing supported models
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — Common use case for foundation models

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
