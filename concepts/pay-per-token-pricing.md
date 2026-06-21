---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c994a990233b9a386662dcad18df6cd3165e709272feaee483e4dea06ab45ab6
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pay-per-token-pricing
    - Token-Based Pricing
    - Token-based pricing
    - pay-per-token
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: Pay-per-Token Pricing
description: Usage-based pricing model for Databricks Foundation Model APIs where users pay per token consumed for inference on curated model architectures.
tags:
  - model-serving
  - pricing
  - inference
timestamp: "2026-06-19T18:01:53.245Z"
---

# Pay-per-Token Pricing

**Pay-per-Token Pricing** is a consumption-based pricing model for foundation model serving, where costs are incurred based on the number of tokens processed by the model. On Databricks, this pricing option is available for select base models through Foundation Model APIs, with endpoints automatically provisioned in the workspace for immediate use.^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## How It Works on Databricks

Databricks provides pre-built endpoints for pay-per-token models. These endpoints appear automatically in the **Serving** tab of the workspace, listed under Foundation Model APIs at the top of the Endpoints list view. Users can query these endpoints without creating a custom endpoint.^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

Pay-per-token pricing is optimized for development, experimentation, and lower-volume inference workloads. For production workloads that require performance guarantees, Databricks offers an alternative pricing model called **provisioned throughput**, which reserves dedicated compute capacity for higher and more predictable throughput.^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Available Models

The following base models are available with pay-per-token pricing (non-exhaustive list from the source):

- **Meta-Llama-3.3-70B-Instruct** – a large instruction-tuned language model.
- **GTE-Large** – a text embedding model.^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

Databricks curates these architectures as part of its Foundation Model APIs, supporting optimized inference out of the box.

## Related Concepts

- [Provisioned Throughput](/concepts/provisioned-throughput.md) – the alternative pricing model for production workloads with reserved capacity.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – the service through which pay-per-token models are offered.
- [Model Serving](/concepts/model-serving.md) – the platform that hosts both pay-per-token and provisioned throughput endpoints.
- [External Models](/concepts/external-models.md) – foundation models hosted outside Databricks, which use a different pricing and governance model.

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
