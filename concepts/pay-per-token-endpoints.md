---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: af7d67834a9dd7fb10a2fc6cd2047f56a0b03897898f79a9916329a6d4879e00
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pay-per-token-endpoints
    - Pay-per-token Endpoint
    - Pay-per-token endpoint
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Pay-per-Token Endpoints
description: A consumption-based pricing model for foundation model inference where users are charged per token processed, suitable for exploration and variable workloads.
tags:
  - pricing
  - model-serving
  - inference
timestamp: "2026-06-19T14:50:39.578Z"
---

# Pay-per-Token Endpoints

**Pay-per-Token Endpoints** are preconfigured endpoints available in each Databricks workspace for supported foundation models. They bill usage based on the number of tokens processed in requests and responses, requiring no advance capacity planning or endpoint configuration. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Overview

Pay-per-token endpoints are a component of the [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md). A preconfigured endpoint exists in the workspace for each supported pay-per-token model. Users interact with these endpoints using HTTP POST requests. No endpoint configuration or provisioning is needed. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

Requests and responses use JSON; the exact JSON structure depends on the endpoint's task type. Supported task types include Chat Completions, Completions, Embeddings, and Responses API. Chat and Completions endpoints support streaming responses. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

The Foundation Model APIs are designed to be similar to OpenAI's REST API, making migration easier. Both pay-per-token and [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) accept the same REST API request format. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Available Models

Pay-per-token endpoints support a wide range of models from multiple providers, including:

- **OpenAI models**: GPT-5.5 Pro, GPT-5.5, GPT-5.4, GPT-5.4 mini, GPT-5.4 nano, GPT-5.3 Codex, GPT-5.2 Codex, GPT-5.2, GPT-5.1, GPT-5.1 Codex Max, GPT-5.1 Codex Mini, GPT-5, GPT-5 mini, GPT-5 nano, GPT OSS 120B, GPT OSS 20B ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Google models**: Gemini 3.1 Flash Lite, Gemini 3.5 Flash, Gemini 3 Flash, Gemini 3.1 Pro Preview, Gemini 3 Pro Preview, Gemini 2.5 Pro, Gemini 2.5 Flash, Gemma 3 12B ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Anthropic models**: Claude Haiku 4.5, Claude Sonnet 4.6, Claude Sonnet 4.5, Claude Fable 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Opus 4.5, Claude Sonnet 4, Claude Opus 4.1 ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Alibaba Cloud models**: Qwen3.5 122B A10B, Qwen3-Embedding-0.6B, Qwen3-Next 80B A3B Instruct ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Meta models**: Llama 4 Maverick, Meta-Llama-3.3-70B-Instruct, Meta-Llama-3.1-405B-Instruct, Meta-Llama-3.1-8B-Instruct ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Embedding models**: GTE Large (En), BGE Large (En) ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

Models support various input types including text, image, video, and audio depending on the specific model. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Usage Tracking

Responses include a `usage` sub-message that reports the number of tokens consumed in the request and response. The format of this sub-message is consistent across all task types. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

For models such as `databricks-meta-llama-3-3-70b-instruct`, user prompts are transformed using a prompt template before being passed to the model. For pay-per-token endpoints, a system prompt might also be added. The `prompt_tokens` count in the usage response includes all text added by the server. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Supported APIs

Pay-per-token endpoints support the following API formats:

- **Chat Completions API** — Multi-turn conversation with a model.
- **Completions API** — Single-prompt text generation with support for batched inputs.
- **Embeddings API** — Map input strings into embedding vectors, with batched input support.
- **Responses API** — Multi-turn conversation with OpenAI models; uses `input` instead of `messages`.

All pay-per-token endpoints use HTTP POST requests and accept JSON request/response bodies. Chat and completion endpoints additionally support streaming responses. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## API Compatibility

The Databricks Foundation Model APIs are designed to be similar to OpenAI's REST API. Both pay-per-token and provisioned throughput endpoints accept the same REST API request format, facilitating migration of existing projects. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) — Dedicated endpoints with reserved capacity for production workloads.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The overarching API framework for accessing foundation models on Databricks.
- [Databricks Model Serving](/concepts/databricks-model-serving.md) — The serving infrastructure that hosts foundation models.
- Streaming Responses — Supported for chat and completion task types.
- [AI Playground](/concepts/ai-playground.md) — An interactive interface for experimenting with supported models.

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
