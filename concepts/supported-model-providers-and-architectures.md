---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bfbcad2fe22bdd8e4d6391dcc545ac8fe2cfcebcde20e70e782a782be02c530a
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-model-providers-and-architectures
    - Architectures and Supported Model Providers
    - SMPAA
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Supported Model Providers and Architectures
description: The range of third-party model providers available through Databricks Foundation Model APIs including OpenAI, Google (Gemini), Anthropic (Claude), Meta (Llama), Alibaba Cloud (Qwen), and specialized embedding model providers.
tags:
  - databricks
  - model-providers
  - openai
  - anthropic
  - google
  - meta
  - alibaba
timestamp: "2026-06-19T18:13:50.960Z"
---

# Supported Model Providers and Architectures

Databricks Foundation Model APIs offer a wide range of state-of-the-art open models from multiple providers. These models are available through pay-per-token endpoints and provisioned throughput mode, and can be queried via REST APIs or the AI Playground. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Overview

The Foundation Model APIs support both **pay-per-token** and **provisioned throughput** modes. Provisioned throughput is recommended for production workloads and supports all models of a model architecture family, including fine-tuned and custom pre-trained models that are also available in pay-per-token mode. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

For all listed models, Databricks recommends using [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) in scenarios where accuracy is especially important, as large language model outputs can omit facts or produce false information. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## OpenAI Models

OpenAI provides several GPT models hosted within the Databricks security perimeter. Available architectures include:

- **GPT-5.5 Pro** (`databricks-gpt-5-5-pro`) – Higher-accuracy variant for deep research and advanced math. Supports text and image inputs with a 400K total token context window and 128K max output tokens.
- **GPT-5.5** (`databricks-gpt-5-5`) – Frontier model for enterprise agent workflows and complex document reasoning.
- **GPT-5.4** (`databricks-gpt-5-4`) – General purpose model with improved accuracy and scaffolded reasoning.
- **GPT-5.4 mini** (`databricks-gpt-5-4-mini`) – Cost-optimized version of GPT-5.4.
- **GPT-5.4 nano** (`databricks-gpt-5-4-nano`) – Lightweight model for high-throughput tasks.
- **GPT-5.3 Codex** (`databricks-gpt-5-3-codex`) – Advanced agentic coding model combining reasoning and professional knowledge.
- **GPT-5.2 Codex** (`databricks-gpt-5-2-codex`) – Code-specialized model (retiring July 16, 2026).
- **GPT-5.2** (`databricks-gpt-5-2`) – General reasoning model with enhanced token efficiency.
- **GPT-5.1** (`databricks-gpt-5-1`) – General purpose model with Instant and Thinking modes.
- **GPT-5.1 Codex Max** (`databricks-gpt-5-1-codex-max`) – High-performance code model (retiring July 16, 2026, hosted on global endpoint).
- **GPT-5.1 Codex Mini** (`databricks-gpt-5-1-codex-mini`) – Cost-optimized code model (retiring July 16, 2026, hosted on global endpoint).
- **GPT-5** (`databricks-gpt-5`) – State-of-the-art reasoning model.
- **GPT-5 mini** (`databricks-gpt-5-mini`) – Cost-optimized reasoning model.
- **GPT-5 nano** (`databricks-gpt-5-nano`) – High-throughput reasoning model.
- **GPT OSS 120B** (`databricks-gpt-oss-120b`) – Flagship open-weight reasoning model with 128K context.
- **GPT OSS 20B** (`databricks-gpt-oss-20b`) – Lightweight reasoning model for real-time copilots.

All OpenAI models support text and image inputs (except GPT OSS models which are text-only) and are hosted within the Databricks security perimeter unless noted otherwise. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Google Models

Google provides Gemini family models:

- **Gemini 3.1 Flash Lite** (`databricks-gemini-3-1-flash-lite`) – Fastest, most cost-efficient Gemini 3 model. Supports text, image, video, audio.
- **Gemini 3.5 Flash** (`databricks-gemini-3-5-flash`) – High-speed, cost-efficient model with stronger reasoning. Multimodal.
- **Gemini 3 Flash** (`databricks-gemini-3-flash`) – High-speed model for near real-time analysis.
- **Gemini 3.1 Pro Preview** (`databricks-gemini-3-1-pro`) – Hybrid reasoning model with 1M token context.
- **Gemini 3 Pro Preview** (`databricks-gemini-3-pro`) – Hybrid reasoning model (retiring March 26, 2026; redirected to 3.1 Pro after). Hosted on global endpoint.
- **Gemini 2.5 Pro** (`databricks-gemini-2-5-pro`) – Hybrid reasoning model with Deep Think Mode and audio output.
- **Gemini 2.5 Flash** (`databricks-gemini-2-5-flash`) – First fully hybrid reasoning model, up to 1M tokens.
- **Gemma 3 12B** (`databricks-gemma-3-12b`) – 12B parameter multimodal model supporting 140+ languages.

All Gemini models support text, image, video, and audio inputs (Gemma supports text and image). Except where noted, endpoints are hosted within the Databricks security perimeter. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Alibaba Cloud Models

Alibaba Cloud provides Qwen family models:

- **Qwen3.5 122B A10B** (`databricks-qwen35-122b-a10b`) – Hybrid MoE reasoning model with 122B total parameters, 10B active. 256K context window. Text-only.
- **Qwen3-Embedding-0.6B** (`databricks-qwen3-embedding-0-6b`) – Text embedding model (~600M parameters) supporting 100+ languages, 32K token context, configurable dimensionality up to 1024.
- **Qwen3-Next 80B A3B Instruct** (`databricks-qwen3-next-80b-a3b-instruct`) – Efficient instruction-following model optimized for long contexts and multi-step workflows. Text-only.

These models are hosted on Databricks infrastructure. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Meta (Llama) Models

Meta provides Llama family models:

- **Llama 4 Maverick** (`databricks-llama-4-maverick`) – Mixture-of-experts architecture for compute efficiency. Supports text and image inputs.
- **Meta-Llama-3.3-70B-Instruct** (`databricks-meta-llama-3-3-70b-instruct`) – State-of-the-art model with 128K context. Text-only.
- **Meta-Llama-3.1-405B-Instruct** (`databricks-meta-llama-3-1-405b-instruct`) – Largest openly available model, competitive with GPT-4-Turbo. Retiring: Feb 15, 2026 (pay-per-token), May 15, 2026 (provisioned throughput).
- **Meta-Llama-3.1-8B-Instruct** (`databricks-meta-llama-3-1-8b-instruct`) – Lightweight model with 128K context.

Llama models are text-only (except Llama 4 Maverick which also processes images). ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Anthropic Models

Anthropic provides Claude family models:

- **Claude Haiku 4.5** (`databricks-claude-haiku-4-5`) – Fastest, most cost-effective model. Text and image.
- **Claude Sonnet 4.6** (`databricks-claude-sonnet-4-6`) – Most advanced hybrid reasoning model with instant and extended thinking modes.
- **Claude Sonnet 4.5** (`databricks-claude-sonnet-4-5`) – Hybrid reasoning model.
- **Claude Fable 5** (`databricks-claude-fable-5`) – Mythos-class model for autonomous knowledge work. Text-only. Prompts and responses retained for 30 days for safety.
- **Claude Opus 4.8** (`databricks-claude-opus-4-8`) – Most capable hybrid reasoning model. Text and image.
- **Claude Opus 4.7** (`databricks-claude-opus-4-7`) – Improved accuracy and efficiency, 1M token context.
- **Claude Opus 4.6** (`databricks-claude-opus-4-6`) – Hybrid reasoning with adaptive thinking.
- **Claude Opus 4.5** (`databricks-claude-opus-4-5`) – Built for complex tasks, 200K context.
- **Claude Sonnet 4** (`databricks-claude-sonnet-4`) – Hybrid reasoning model.
- **Claude Opus 4.1** (`databricks-claude-opus-4-1`) – Enterprise-scale hybrid reasoning model, 200K context.

All Claude models are hosted within the Databricks security perimeter. Customers must comply with Anthropic's usage policy. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Embedding Models

In addition to large language models, the Foundation Model APIs support embedding models for semantic retrieval, classification, and clustering:

- **GTE Large (En)** (`databricks-gte-large-en`) – General Text Embedding model from Alibaba, 1024-dimension vectors, 8192 token embedding window. Text-only.
- **BGE Large (En)** (`databricks-bge-large-en`) – BAAI General Embedding, 1024-dimension, 512 token window. Generates normalized embeddings. Text-only.
- **Qwen3-Embedding-0.6B** – 600M parameter model supporting 100+ languages, 32K token context, configurable up to 1024 dimensions.

Embedding models are especially effective when used with LLMs for [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) use cases. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Provisioned Throughput

Provisioned throughput mode supports all models of a model architecture family, including fine-tuned and custom pre-trained models. Databricks recommends provisioned throughput for production workloads. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The API layer for querying supported models.
- [Pay-per-token](/concepts/pay-per-token-serving-mode.md) – Usage-based pricing model for endpoint consumption.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – Reserved capacity for production deployments.
- [AI Playground](/concepts/ai-playground.md) – Interactive interface for testing models.
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) – Technique to improve factual accuracy.
- Embedding Models – Models for generating text vector representations.
- [Retired Models Policy](/concepts/partner-model-retirement-policy.md) – Deprecation timelines and migration guidance.

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
