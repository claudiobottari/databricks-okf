---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e781925f675eddc50faedda3bd22d28c5117297e4ee0223d6dd32e6e489d8616
  pageDirectory: concepts
  sources:
    - databricks-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-functions-for-batch-inference
    - AFFBI
  citations:
    - file: databricks-foundation-model-apis-databricks-on-aws.md
title: AI Functions for Batch Inference
description: Batch inference mode using AI Functions within Databricks, recommended for running inference on large datasets using generative AI or ML models.
tags:
  - batch-inference
  - ai-functions
  - databricks
timestamp: "2026-06-19T18:12:56.607Z"
---

# AI Functions for Batch Inference

**AI Functions for Batch Inference** is a serving mode in [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) designed for running batch inference workloads using generative AI or ML models through AI Functions. This mode enables processing large datasets efficiently without maintaining individual model deployments.^[databricks-foundation-model-apis-databricks-on-aws.md]

## Overview

AI Functions for batch inference allow you to run batch inference using any generative AI or ML model through the AI Functions feature of Databricks Foundation Model APIs.^[databricks-foundation-model-apis-databricks-on-aws.md] This mode is specifically optimized for batch inference workloads, making it suitable for production-scale batch processing tasks where you need to apply models to large datasets.

## Usage

To use AI Functions for batch inference, refer to the official Databricks documentation:

- [Enrich data using AI Functions](https://docs.databricks.com/aws/en/large-language-models/ai-functions) — Guides on using AI Functions to enrich your data.
- [Deploy batch inference pipelines](https://docs.databricks.com/aws/en/large-language-models/batch-inference-pipelines) — Instructions for creating batch inference pipelines using AI Functions.

^[databricks-foundation-model-apis-databricks-on-aws.md]

## Comparison with Other Serving Modes

The Foundation Model APIs provide three serving modes, each recommended for different use cases:^[databricks-foundation-model-apis-databricks-on-aws.md]

| Mode | Recommended Use Case |
|------|---------------------|
| Pay-per-token | Getting started, low-throughput applications, production workloads |
| Provisioned throughput | Production workloads requiring high throughput, performance guarantees, fine-tuned models, or compliance certifications like HIPAA |
| AI Functions optimized models | Batch inference workloads |

## Key Differentiators

Unlike pay-per-token and provisioned throughput modes, AI Functions for batch inference are designed specifically for processing large volumes of data in batch. This mode eliminates the need to set up and manage individual model deployments, as the infrastructure is managed by Databricks.^[databricks-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) — The underlying APIs providing access to foundation models through multiple serving modes.
- [Batch Inference Pipelines](/concepts/batch-inference-pipelines.md) — The infrastructure for deploying and managing batch inference workflows on Databricks.
- [AI Functions](/concepts/ai-functions.md) — SQL-based functions that enable calling models directly from data pipelines.
- [Model Serving](/concepts/model-serving.md) — The broader Databricks platform for serving models in real-time and batch inference contexts.
- [Unity Catalog](/concepts/unity-catalog.md) — Manages model artifacts, permissions, and governance for foundation models.
- [Pay-per-token Foundation Model APIs](/concepts/pay-per-token-foundation-model-apis.md) — Mode for getting started with foundation models.
- [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md) — Mode for production workloads with performance guarantees.

## Sources

- databricks-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-foundation-model-apis-databricks-on-aws.md](/references/databricks-foundation-model-apis-databricks-on-aws-f789bf37.md)
