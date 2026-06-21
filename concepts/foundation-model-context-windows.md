---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 705b4e46b232bd948c7ab99b1dfcfa85c85fc4b923823e2c67c0df5fcae5481b
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - foundation-model-context-windows
    - FMCW
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Foundation Model Context Windows
description: The maximum token limits for model inputs and outputs across supported models, ranging from 128K to 1M tokens, with common configurations like 400K input / 128K output for OpenAI GPT models.
tags:
  - llm
  - architecture
  - scaling
timestamp: "2026-06-19T14:51:15.981Z"
---

# Foundation Model Context Windows

**Foundation Model Context Windows** refer to the maximum number of tokens a large language model (LLM) can process in a single input, including both the user's prompt and any additional context such as retrieved documents, conversation history, or system instructions. The context window size is a key architectural characteristic that determines how much information a model can consider when generating a response.

## Overview

Different foundation models support different context window sizes, ranging from tens of thousands to over a million tokens. The context window directly impacts the model's ability to handle long documents, maintain coherent multi-turn conversations, and incorporate external knowledge through techniques like [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md). ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Context Window Sizes by Model Family

### OpenAI GPT Models

All OpenAI GPT models available through Databricks Foundation Model APIs feature a **400K total token context window** with **128K maximum output tokens**. This includes GPT-5.5 Pro, GPT-5.5, GPT-5.4, GPT-5.4 mini, GPT-5.4 nano, GPT-5.3 Codex, GPT-5.2 Codex, GPT-5.2, GPT-5.1, GPT-5.1 Codex Max, GPT-5.1 Codex Mini, GPT-5, GPT-5 mini, and GPT-5 nano. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### OpenAI GPT OSS Models

The open-weight models from OpenAI have a **128K token context window**. This applies to both GPT OSS 120B and GPT OSS 20B. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Google Gemini Models

Google's Gemini models offer the largest context windows among supported foundation models:

- **Gemini 3.1 Pro Preview**: 1-million-token context window ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Gemini 3 Pro Preview**: 1-million-token context window ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Gemini 2.5 Pro**: 1-million-token context window ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Gemini 2.5 Flash**: 1-million-token context window ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Gemini 3.5 Flash**: Context window size not explicitly specified in source ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Gemini 3 Flash**: Context window size not explicitly specified in source ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Gemini 3.1 Flash Lite**: Context window size not explicitly specified in source ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Anthropic Claude Models

Anthropic's Claude models offer varying context window sizes:

- **Claude Opus 4.7**: 1-million-token context window ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Opus 4.6**: 1-million-token context window ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Opus 4.5**: 200K token context window ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Opus 4.1**: 200K token context window ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Sonnet 4.6**: Context window size not explicitly specified in source ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Sonnet 4.5**: Context window size not explicitly specified in source ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Sonnet 4**: Context window size not explicitly specified in source ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Haiku 4.5**: Context window size not explicitly specified in source ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Fable 5**: Context window size not explicitly specified in source ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Opus 4.8**: Context window size not explicitly specified in source ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Meta Llama Models

Meta's Llama models available through Databricks Foundation Model APIs feature a **128K token context window**:

- **Meta-Llama-3.3-70B-Instruct**: 128,000 tokens ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Meta-Llama-3.1-405B-Instruct**: 128,000 tokens ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Meta-Llama-3.1-8B-Instruct**: 128,000 tokens ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Llama 4 Maverick**: Context window size not explicitly specified in source ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Alibaba Cloud Qwen Models

- **Qwen3.5 122B A10B**: 256K context window with up to 8,000 output tokens ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Qwen3-Next 80B A3B Instruct**: Designed for ultra-long contexts (exact size not specified) ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Google Gemma 3

- **Gemma 3 12B**: Up to 128K token context ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Embedding Models

Embedding models have smaller context windows suited for document chunking:

- **Qwen3-Embedding-0.6B**: Long contexts up to ~32K tokens ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **GTE Large (En)**: Embedding window of 8,192 tokens ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **BGE Large (En)**: Embedding window of 512 tokens ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Practical Implications

Larger context windows enable models to process entire documents, maintain extended conversation history, and incorporate more retrieved information from RAG systems. However, larger contexts also increase computational cost and latency. Databricks recommends using [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) in scenarios where accuracy is especially important, as foundation model outputs may omit facts or produce false information regardless of context window size. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The service through which these models are accessed
- Token — The basic unit of text processed by language models
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — Technique for providing relevant context within the window
- [Model Serving](/concepts/model-serving.md) — Infrastructure for deploying and querying foundation models
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Production-grade serving mode for foundation models

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
