---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 33234ccc51259cbcd49422221af010467022b4fe4bb646839ac82cf8632b6bfb
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-mode
    - PTM
    - Provisioned Throughput Models
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Provisioned Throughput Mode
description: A reserved-capacity deployment mode for foundation models, recommended by Databricks for production workloads, supporting all models of a given architecture family.
tags:
  - pricing
  - model-serving
  - production
timestamp: "2026-06-19T14:50:33.319Z"
---

# Provisioned Throughput Mode

**Provisioned Throughput Mode** is a dedicated capacity deployment option within Databricks [Foundation Model APIs](/concepts/foundation-model-apis.md) that provides reserved inference throughput for large language models. Databricks recommends this mode for production workloads that require consistent, predictable performance. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Overview

In Provisioned Throughput Mode, the API supports all models belonging to a given model architecture family, including fine-tuned and custom pre-trained models that are also available in [Pay-per-token mode](/concepts/pay-per-token-serving-mode.md). This enables organizations to deploy custom variants of supported architectures with guaranteed throughput, making it suitable for mission-critical applications. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Supported Architectures

The list of supported model architectures for provisioned throughput is documented separately in the Provisioned throughput Foundation Model APIs reference. Users should consult that reference to determine which model families are eligible for reserved capacity deployment. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Comparison with Pay-per-Token Mode

While [Pay-per-token mode](/concepts/pay-per-token-serving-mode.md) offers on-demand, usage-based pricing suitable for development, experimentation, and low-volume workloads, Provisioned Throughput Mode provides dedicated capacity for production deployments. The provisioned mode guarantees throughput and eliminates contention with other users, making it the recommended choice for applications with consistent or predictable traffic patterns. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The overarching service that includes both pay-per-token and provisioned throughput modes.
- [Pay-per-token mode](/concepts/pay-per-token-serving-mode.md) — The on-demand pricing alternative, suitable for development and low-volume usage.
- Model architecture family — A group of models sharing the same underlying architecture, all supported under provisioned throughput.
- Production workloads — The recommended use case for provisioned throughput mode.
- [Model Serving](/concepts/model-serving.md) — The broader infrastructure for deploying and serving models on Databricks.

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
