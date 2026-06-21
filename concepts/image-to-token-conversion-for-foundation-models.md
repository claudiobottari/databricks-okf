---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5ec9cb31c4694bcc3f41e9655c9fab85f0330c45236b89bd68afcb3fe791dbf7
  pageDirectory: concepts
  sources:
    - query-vision-models-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - image-to-token-conversion-for-foundation-models
    - ICFFM
  citations:
    - file: query-vision-models-databricks-on-aws.md
title: Image-to-Token Conversion for Foundation Models
description: The mechanism by which each image in a request to a Databricks-hosted foundation model is converted to token usage for billing and pricing purposes.
tags:
  - databricks
  - billing
  - tokens
  - vision
timestamp: "2026-06-19T20:05:02.921Z"
---

# Image-to-Token Conversion for Foundation Models

**Image-to-Token Conversion** is the process by which images submitted to foundation model serving endpoints are converted into tokens for processing and billing purposes. When querying vision-capable foundation models through Databricks Model Serving, each image in a request contributes to the total token usage, which affects both model processing and cost calculation. ^[query-vision-models-databricks-on-aws.md]

## Overview

Foundation models optimized for vision tasks accept images as input through the Chat Completions API. Before the model can process an image, the serving infrastructure converts the image data into tokens — the fundamental units that the model operates on. This conversion happens automatically when an image is included in a request to a supported foundation model endpoint. ^[query-vision-models-databricks-on-aws.md]

## Token Usage and Billing

Each image in a request to a foundation model adds to your token usage. The number of tokens consumed by an image depends on the image dimensions, resolution, and the specific model being used. Databricks provides a [pricing calculator](https://www.databricks.com/product/pricing/genai-pricing-calculator) to estimate image pricing based on the token usage and model you are using. ^[query-vision-models-databricks-on-aws.md]

## Scope and Applicability

Image-to-token conversion applies only to **Foundation Model APIs** — Databricks-hosted models served through the platform's managed infrastructure. For [External Models](/concepts/external-models.md) served through Databricks, users should refer to the provider's documentation for image processing and billing details. ^[query-vision-models-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The service that provides access to Databricks-hosted foundation models.
- [Model Serving](/concepts/model-serving.md) — The infrastructure that hosts and serves models for inference.
- Vision Models — Foundation models optimized for image understanding tasks.
- [Chat Completions API](/concepts/chat-completions-api.md) — The API used to send image and text prompts to vision models.
- Tokenization — The general process of converting input data into tokens for model processing.
- Query Vision Models — How to write query requests for vision-capable foundation models.

## Sources

- query-vision-models-databricks-on-aws.md

# Citations

1. [query-vision-models-databricks-on-aws.md](/references/query-vision-models-databricks-on-aws-afa9c021.md)
