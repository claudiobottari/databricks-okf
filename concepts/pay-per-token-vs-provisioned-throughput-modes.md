---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: adb9582b70c7aa600ded94d047e6745446f61634fb5a6b3d17f0304bed6b4a8a
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pay-per-token-vs-provisioned-throughput-modes
    - PVPTM
    - Pay-per-Token vs Provisioned Throughput
    - Pay-per-token vs Provisioned Throughput
    - Supported Models for Provisioned Throughput
    - pay-per-token-vs-provisioned-throughput-serving-modes
    - PVPTSM
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Pay-per-Token vs Provisioned Throughput Modes
description: "Two pricing and deployment modes for Foundation Model APIs: pay-per-token for variable usage and provisioned throughput for production workloads, with the latter supporting all models in a model architecture family."
tags:
  - databricks
  - pricing
  - model-serving
timestamp: "2026-06-19T09:52:17.893Z"
---

--- SOURCE: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md ---

# Pay-per-Token vs Provisioned Throughput Modes

**Pay-per-Token** and **Provisioned Throughput** are two pricing and serving modes available through Databricks [Foundation Model APIs](/concepts/foundation-model-apis.md) for hosted models. The choice between them depends on workload predictability, latency requirements, cost tolerance, and whether you need custom or fine-tuned model support.

## Pay-per-Token Mode

Pay-per-Token mode charges per inference request based on the number of input and output tokens processed. It is the default mode for most supported models and is accessible directly from your Databricks workspace via the endpoint names listed in the [Databricks-hosted foundation models](/concepts/databricks-hosted-foundation-models.md) documentation.^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

This mode is well-suited for development, experimentation, variable workloads, and scenarios where traffic patterns are unpredictable. No capacity reservation is required, and you only pay for what you use.

## Provisioned Throughput Mode

Provisioned Throughput mode reserves a fixed amount of model serving capacity for your workloads. Databricks recommends this mode for production workloads because it provides predictable performance and throughput.^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

Unlike pay-per-token, provisioned throughput supports all models within a given model architecture family — not just the specific pre-trained models offered in pay-per-token mode. This includes fine-tuned and custom pre-trained models built on those architectures.^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Comparison

| Aspect | Pay-per-Token | Provisioned Throughput |
|--------|---------------|------------------------|
| Pricing | Per token consumed | Reserved capacity (fixed cost) |
| Recommended use case | Development, experimentation, variable traffic | Production, predictable traffic, custom models |
| Model support | Specific pre-trained models as listed in supported models table | All models in a supported architecture family, including fine-tuned and custom pre-trained models |
| Performance | Shared capacity; may have variable latency | Dedicated capacity; predictable latency |
| Capacity planning | None required | Must reserve capacity in advance |

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The serving infrastructure behind both modes.
- [Databricks-hosted foundation models](/concepts/databricks-hosted-foundation-models.md) — The list of models available in pay-per-token mode.
- [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md) — Details on supported architectures for provisioned throughput.
- [AI Playground](/concepts/ai-playground.md) — Interactive environment for testing supported models.
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) — General serving concepts.

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
