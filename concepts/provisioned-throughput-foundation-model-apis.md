---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf825b5070464d74c186daf734c286ea915fcf0079ac81c0b518321ae499634a
  pageDirectory: concepts
  sources:
    - databricks-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-foundation-model-apis
    - PTFMA
    - Deploy Provisioned Throughput Foundation Model APIs
    - Provisioned Throughput Foundation Model API
    - Provisioned Throughput Foundation Model APIs Deployment
    - Provisioned Throughput for Foundation Model APIs
  citations:
    - file: databricks-foundation-model-apis-databricks-on-aws.md
title: Provisioned Throughput Foundation Model APIs
description: Optimized inference mode for foundation model workloads requiring performance guarantees, compliance certifications like HIPAA, and support for fine-tuned models.
tags:
  - model-serving
  - production
  - performance
  - compliance
timestamp: "2026-06-19T18:12:43.749Z"
---

# Provisioned Throughput Foundation Model APIs

**Provisioned throughput** is a serving mode for [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) that provides dedicated compute capacity with performance guarantees for production workloads. It is recommended for applications that require high throughput, consistent latency, or compliance certifications. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Overview

Provisioned throughput endpoints offer optimized inference for foundation model workloads that demand predictable performance. Unlike pay-per-token mode, which is suitable for experimentation and low-throughput use cases, provisioned throughput is designed for production deployments where reliability and performance SLAs are critical. ^[databricks-foundation-model-apis-databricks-on-aws.md]

Key characteristics of provisioned throughput include:

- Performance guarantees for production traffic spikes
- Support for fine-tuned models and custom weights
- Compliance certifications such as HIPAA
- Dedicated serverless compute infrastructure

## Requirements

To use provisioned throughput Foundation Model APIs, you need:

- A Databricks API token for authentication
- Serverless compute enabled in your workspace
- A workspace in a supported region (see [provisioned throughput regions](https://docs.databricks.com/aws/en/resources/feature-region-support#model-serving-aws))

## Supported Capabilities

Provisioned throughput supports the following model types: ^[databricks-foundation-model-apis-databricks-on-aws.md]

- **Base models of all sizes** – These can be accessed through the Databricks Marketplace, downloaded from Hugging Face, or obtained from other external sources and registered in Unity Catalog.
- **Fine-tuned variants** – Any fine-tuned version of supported base models, including those trained on proprietary data.
- **Custom weights and tokenizers** – Fully custom models trained from scratch, models with continued pre-training, or other variations using the base model architecture (for example, CodeLlama).

## When to Use Provisioned Throughput

Provisioned throughput is recommended for: ^[databricks-foundation-model-apis-databricks-on-aws.md]

- Production workloads requiring high throughput
- Applications with strict performance guarantees
- Deployments using fine-tuned or custom models
- Workloads with additional security or compliance requirements (such as HIPAA)
- Applications that need to handle production traffic spikes reliably

## Comparison with Other Modes

| Feature | Pay-per-token | Provisioned throughput | AI Functions |
|---------|---------------|----------------------|--------------|
| Recommended use | Getting started, experimentation | Production workloads | Batch inference |
| Performance guarantees | No | Yes | N/A |
| Fine-tuned model support | No | Yes | N/A |
| Compliance certifications | Limited | HIPAA and others | N/A |
| Throughput | Low | High | Batch |

## Deployment

For step-by-step guidance on deploying provisioned throughput endpoints, see Provisioned Throughput Foundation Model APIs Deployment. The deployment process involves creating a serving endpoint with provisioned throughput configuration and selecting the desired model from supported architectures. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Best Practices

- Reserve capacity in advance through your cloud provider for high-demand workloads
- Monitor endpoint performance using Databricks observability tools
- Start with pay-per-token for prototyping, then migrate to provisioned throughput for production
- Choose provisioned throughput when compliance certifications are required

## Limitations

Provisioned throughput endpoints are subject to regional availability and resource constraints. See [Foundation Model APIs limits](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#fmapi-limits) for detailed information on rate limits and quotas.

## Related Concepts

- [Pay-per-token Foundation Model APIs](/concepts/pay-per-token-foundation-model-apis.md)
- [AI Functions for Batch Inference](/concepts/ai-functions-for-batch-inference.md)
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md)
- Unity Catalog for Foundation Models
- [Foundation Model REST API Reference](/concepts/foundation-model-apis.md)

## Sources

- databricks-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-foundation-model-apis-databricks-on-aws.md](/references/databricks-foundation-model-apis-databricks-on-aws-f789bf37.md)
