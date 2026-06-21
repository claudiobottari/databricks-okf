---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 657b7df9645b72917515de741edafb89b269caebff9b5856430a3fc926cdbae3
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multimodal-foundation-models
    - MFM
    - Query audio and video models
    - multimodal capabilities
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Multimodal Foundation Models
description: Foundation models that accept multiple input types (text, image, video, audio) alongside text, enabling cross-modal reasoning tasks like image understanding, video analysis, and visual Q&A.
tags:
  - multimodal
  - llm
  - vision
timestamp: "2026-06-19T14:51:35.341Z"
---

# Multimodal Foundation Models

**Multimodal Foundation Models** are a class of Foundation Models|large-scale machine learning models that can process and generate information across multiple data modalities, such as text, images, and audio. They represent a significant advancement beyond single-modal models in enabling more comprehensive AI systems that can reason about and generate across diverse input types. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Overview

Multimodal foundation models integrate processing capabilities for multiple input types within a single model architecture. These models accept a variety of input formats—including text, image, video, and audio—and generate text outputs. They are designed for tasks that require understanding across different data types, such as complex reasoning, visual question answering, document analysis, and content generation. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Supported Input Modalities

The specific input modalities supported vary by model, but commonly include:

- **Text**: All listed models accept text as primary input for prompting and instruction.
- **Image**: Many models support image input for tasks such as visual Q&A and document understanding.
- **Video**: Several models—particularly from the Gemini and Qwen series—support video input.
- **Audio**: Some models, including select Gemini variants, are capable of processing audio inputs.

^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Available Multimodal Models

Databricks Foundation Model APIs host a range of multimodal foundation models from multiple providers. The following models support multimodal inputs:

### OpenAI Models

- **`databricks-gpt-5-5-pro`** — GPT-5.5 Pro, a higher-accuracy variant for deep research, advanced math, and high-stakes reasoning. Supports text and image inputs with a 400K token context window.
- **`databricks-gpt-5-5`** — GPT-5.5, OpenAI's strongest frontier model for enterprise agent workflows and complex document reasoning. Supports text and image inputs.
- **`databricks-gpt-5-4`** — GPT-5.4, a general-purpose model with improved deliberate scaffolded reasoning. Supports text and image inputs.
- **`databricks-gpt-5-4-mini`** — GPT-5.4 mini, a cost-optimized variant for reliable reasoning and precise language. Supports text and image inputs.
- **`databricks-gpt-5-4-nano`** — GPT-5.4 nano, for high-throughput tasks like instruction-following or classification. Supports text and image inputs.
- **`databricks-gpt-5-3-codex`** — GPT-5.3 Codex, OpenAI's most advanced agentic coding model, combining coding performance with reasoning capabilities. Supports text and image inputs.
- **`databricks-gpt-5-2-codex`** — GPT-5.2 Codex, a code-specialized model. Supports text and image inputs.
- **`databricks-gpt-5-2`** — GPT-5.2, a general-purpose model with improved token efficiency. Supports text and image inputs.
- **`databricks-gpt-5-1`** — GPT-5.1, a model with Instant and Thinking modes for fast conversation or deep reasoning. Supports text and image inputs.

^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Google Gemini Models

- **`databricks-gemini-3-1-flash-lite`** — Gemini 3.1 Flash Lite, the fastest and most cost-efficient model in the Gemini 3 series. Supports text, image, video, and audio inputs.
- **`databricks-gemini-3-5-flash`** — Gemini 3.5 Flash, a high-speed, cost-efficient model with stronger reasoning and advanced multimodal capabilities. Supports text, image, video, and audio inputs.
- **`databricks-gemini-3-flash`** — Gemini 3 Flash, a high-speed model for complex video analysis, data extraction, and visual Q&As. Supports text, image, video, and audio inputs.
- **`databricks-gemini-3-1-pro`** — Gemini 3.1 Pro Preview, a state-of-the-art hybrid reasoning model with a 1-million-token context window. Supports text, image, video, and audio inputs.
- **`databricks-gemini-3-pro`** — Gemini 3 Pro Preview, a hybrid reasoning model with a 1-million-token context window. Supports text, image, video, and audio inputs.
- **`databricks-gemini-2-5-pro`** — Gemini 2.5 Pro, a hybrid reasoning model with "Deep Think Mode" and built-in audio output. Supports text, image, video, and audio inputs.
- **`databricks-gemini-2-5-flash`** — Gemini 2.5 Flash, a high-speed, cost-efficient multimodal model and the first fully hybrid reasoning model from Google. Supports text, image, video, and audio inputs.

^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Model Characteristics

Multimodal foundation models share several common architectural characteristics:

- **Context windows**: Many models offer large context windows, with some supporting up to 400K or 1 million tokens for extended document and conversation processing.
- **Output tokens**: Most models support up to 128K maximum output tokens, enabling extensive text generation. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Hybrid reasoning**: Several models combine near-instant responses with extended thinking capabilities, automatically adjusting for simple or complex tasks. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Recommendations for Use

As with other large language models, multimodal foundation model output may occasionally omit facts or produce false information. Databricks recommends using [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) in scenarios where accuracy is especially important. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The serving infrastructure for accessing multimodal models.
- [Large Language Models](/concepts/large-language-models-llms-on-databricks.md) — The broader class of models to which multimodal models belong.
- [AI Playground](/concepts/ai-playground.md) — A tool for interactive model experimentation.
- [Retrieval Augmented Generation](/concepts/retrieval-augmented-generation-rag.md) — A technique for improving model accuracy by grounding responses in retrieved context.
- Fine-tuning — Customization of foundation models for specific tasks.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — A deployment mode for production workloads.

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
