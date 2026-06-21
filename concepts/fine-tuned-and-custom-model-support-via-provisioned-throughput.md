---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b63d725f2a26cc12187d3f52cdc8bc5170ff479af7d6084fc58c4c22c5abc83
  pageDirectory: concepts
  sources:
    - databricks-foundation-model-apis-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fine-tuned-and-custom-model-support-via-provisioned-throughput
    - custom model support via Provisioned Throughput and Fine-tuned
    - FACMSVPT
  citations:
    - file: databricks-foundation-model-apis-databricks-on-aws.md
title: Fine-tuned and custom model support via Provisioned Throughput
description: Provisioned throughput endpoints support base models of all sizes, fine-tuned variants, fully custom weights and tokenizers, and architectural variations like CodeLlama.
tags:
  - fine-tuning
  - custom-models
  - model-serving
  - databricks
timestamp: "2026-06-18T11:38:34.315Z"
---

# Fine-tuned and Custom Model Support via Provisioned Throughput

**Fine-tuned and custom model support via Provisioned Throughput** refers to the ability to deploy models with custom weights, tokenizers, or fine-tuned variants on [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) using provisioned throughput endpoints. This capability is designed for production workloads that require high throughput, performance guarantees, and additional security requirements such as HIPAA compliance.^[databricks-foundation-model-apis-databricks-on-aws.md]

## Supported Model Types

Provisioned throughput endpoints support the following categories of models:^[databricks-foundation-model-apis-databricks-on-aws.md]

- **Base models of all sizes** – Standard foundation models that can be accessed via the Databricks Marketplace, or downloaded from [Hugging Face](/concepts/hugging-face-trainer.md) or another external source and registered in [Unity Catalog](/concepts/unity-catalog.md).
- **Fine-tuned variants of base models** – Any fine-tuned version of a supported base model, including models fine-tuned on proprietary data.
- **Fully custom weights and tokenizers** – Models trained from scratch, those that have undergone continued pre-training, or other variations using the base model architecture (for example, CodeLlama).

## How to Deploy

To deploy a fine-tuned or custom model using provisioned throughput:^[databricks-foundation-model-apis-databricks-on-aws.md]

1. **Register the model** – Register the model weights in Unity Catalog. Models can be obtained from the Databricks Marketplace, Hugging Face, or any external source.
2. **Create a serving endpoint** – Use the Databricks UI, REST API, or SDK to create a provisioned throughput endpoint that points to the registered model.
3. **Configure performance** – Select the appropriate throughput tier based on your expected workload. Provisioned throughput provides performance guarantees suitable for production traffic.

## Benefits

Provisioned throughput for fine-tuned and custom models offers:^[databricks-foundation-model-apis-databricks-on-aws.md]

- **Performance guarantees** – Suitable for high-throughput production workloads with predictable latency.
- **Security and compliance** – Available with compliance certifications like HIPAA (requires serverless compute in a supported region).
- **Flexibility** – Supports both publicly available base models and fully custom fine-tuned models without vendor lock-in.
- **Simplified operations** – No need to manage underlying infrastructure; Databricks hosts the model and handles scaling.

## Requirements

- A workspace in a supported AWS region for provisioned throughput. See [feature region support](https://docs.databricks.com/aws/en/resources/feature-region-support#model-serving-aws).^[databricks-foundation-model-apis-databricks-on-aws.md]
- Serverless compute enabled for the workspace.
- A Databricks API token for authentication when using REST APIs or SDKs.

## Limitations

Overall Foundation Model API limits apply. See the dedicated [Foundation Model APIs limits](/concepts/foundation-model-apis-rate-limits.md) page for details on rate limits, concurrency, and quota restrictions.^[databricks-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md) – Step-by-step deployment guide.
- [Model Serving](/concepts/model-serving.md) – The underlying serving infrastructure.
- [Unity Catalog](/concepts/unity-catalog.md) – Used for registering custom model weights.
- Databricks Marketplace – Source for base models.
- [Pay-per-token Foundation Model APIs](/concepts/pay-per-token-foundation-model-apis.md) – Alternative pricing mode for lower-throughput workloads.
- [AI Functions for Batch Inference](/concepts/ai-functions-for-batch-inference.md) – Batch inference option using the same models.

## Sources

- databricks-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-foundation-model-apis-databricks-on-aws.md](/references/databricks-foundation-model-apis-databricks-on-aws-f789bf37.md)
