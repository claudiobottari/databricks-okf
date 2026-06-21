---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 367d2fd0e98bd26df84dca59f361c33e80627363ed98fe9541cf969e9cc62d1b
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-serving-modes
    - FMSM
    - Foundation Model Serving
    - Foundation model serving
    - Foundational Model Serving
    - Cold Start in Model Serving
    - Supported foundation models on Model Serving
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Foundation Model Serving Modes
description: "Two modes for accessing models via Databricks Foundation Model APIs: pay-per-token (usage-based pricing) and provisioned throughput (dedicated capacity recommended for production workloads)."
tags:
  - databricks
  - pricing
  - model-serving
timestamp: "2026-06-19T18:13:11.711Z"
---

# Foundation Model Serving Modes

**Foundation Model Serving Modes** refer to the two pricing and deployment options provided by [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) for running inference on state-of-the-art open and proprietary models. These modes determine how you pay for model usage and how throughput is allocated. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Pay‑per‑Token Mode

In pay‑per‑token mode, you send query requests to pre‑defined model endpoints and are charged based on the number of input and output tokens consumed. Databricks provides a list of supported model endpoints that operate on this pricing model. Pay‑per‑token is suitable for experimentation, prototyping, and low‑volume workloads. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

The endpoint names follow a consistent naming convention (e.g., `databricks-gpt-5-4-mini`, `databricks-claude-sonnet-4`, `databricks-meta-llama-3-3-70b-instruct`). You can find the complete list of pay‑per‑token supported models in the "pay‑per‑token supported models table" referenced in the official documentation. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Provisioned Throughput Mode

Provisioned throughput mode reserves a fixed amount of inference capacity for your workloads. Databricks recommends this mode for production workloads because it provides predictable performance and dedicated throughput. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

A key advantage of provisioned throughput is that it supports **all models of a model architecture family**, including fine‑tuned and custom pre‑trained models that are also available in pay‑per‑token mode. This makes it possible to deploy customised variants alongside the base models from the same architecture family. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Choosing a Serving Mode

| Criterion | Pay‑per‑Token | Provisioned Throughput |
|-----------|---------------|------------------------|
| Use case | Experimentation, development, low‑volume | Production, high‑volume, latency‑sensitive |
| Pricing | Per‑token consumption | Reserved capacity |
| Model support | Pre‑defined list of endpoints | All models of a supported architecture family, including custom variants |
| Recommendation | Not recommended for production | Recommended for production workloads |

## Related Concepts

- [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) – The overarching API layer that exposes these serving modes.
- [AI Playground](/concepts/ai-playground.md) – A UI for interacting with supported models in a chat interface.
- [Model Serving](/concepts/model-serving.md) – General Databricks model serving concepts.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – Capacity reservation for production inference.
- [Pay‑per‑Token](/concepts/pay-per-token-serving-mode.md) – Consumption‑based pricing for model inference.

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
