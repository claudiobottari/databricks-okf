---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 52e1f215b871e7cb93caa11dba7b84a9012e77c302fff8b30af5b89cd26cdd0c
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - foundation-model-api-multimodal-support
    - FMAMS
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Foundation Model API Multimodal Support
description: The capability of Databricks-hosted foundation models to accept diverse input types including text, image, video, and audio across multiple model providers.
tags:
  - multimodal
  - databricks
  - llm
  - foundation-models
timestamp: "2026-06-18T15:08:46.612Z"
---

# Foundation Model API Multimodal Support

**Foundation Model API Multimodal Support** refers to the capability of Databricks-hosted foundation models to process and generate outputs from multiple input types, including text, images, video, and audio. This enables applications that combine different data modalities, such as analyzing images with text prompts or processing video with audio, within a single model invocation. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Supported Models

Several foundation models available through the [Foundation Model APIs](/concepts/foundation-model-apis.md) support multimodal inputs. These include:

### OpenAI Models

All OpenAI models in the Foundation Model APIs support multimodal inputs, including text and image. The following models are part of the GPT-5 and GPT-5.5 model families:

- **GPT-5** (`databricks-gpt-5`) – State-of-the-art general purpose reasoning model with a 400K total token context window and 128K maximum output tokens. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **GPT-5 mini** (`databricks-gpt-5-mini`) – Cost-optimized for reasoning and chat workloads, supporting text and image inputs. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **GPT-5 nano** (`databricks-gpt-5-nano`) – Optimized for high-throughput tasks like simple instruction-following or classification. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **GPT-5.1** (`databricks-gpt-5-1`) – Features both Instant and Thinking modes for fast conversation or deep reasoning. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **GPT-5.2** (`databricks-gpt-5-2`) – Higher accuracy with improved token efficiency on medium-to-complex tasks. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **GPT-5.3 Codex** (`databricks-gpt-5-3-codex`) – Agentic coding model that can handle complex, long-running tasks involving research, tool use, and execution. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **GPT-5.4** (`databricks-gpt-5-4`) – General purpose large language model with improved performance on complex tasks and more deliberate scaffolded reasoning. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **GPT-5.4 mini** (`databricks-gpt-5-4-mini`) – Cost-optimized general purpose LLM built on the GPT-5.4 architecture. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **GPT-5.4 nano** (`databricks-gpt-5-4-nano`) – General purpose LLM excelling at high-throughput tasks. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **GPT-5.5** (`databricks-gpt-5-5`) – OpenAI's strongest frontier model for enterprise agent workflows, complex document reasoning, and long-horizon coding agents. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **GPT-5.5 Pro** (`databricks-gpt-5-5-pro`) – Higher-accuracy variant of GPT-5.5 aimed at the hardest problems, including deep research, advanced math, and high-stakes reasoning. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

All OpenAI models listed above support text and image inputs with a 400K total token context window and 128K maximum output tokens. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Google Models

Google models in the Foundation Model APIs support multimodal inputs including text, image, video, and audio:

- **Gemini 3.5 Flash** (`databricks-gemini-3-5-flash`) – High-speed, cost-efficient multimodal AI model with stronger reasoning and advanced multimodal capabilities. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Gemini 3.1 Pro Preview** (`databricks-gemini-3-1-pro`) – State-of-the-art hybrid reasoning model with a 1-million-token context window. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Gemini 2.5 Pro** (`databricks-gemini-2-5-pro`) – Hybrid reasoning model with "Deep Think Mode" and built-in audio output. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Gemini 2.5 Flash** (`databricks-gemini-2-5-flash`) – High-speed, cost-efficient multimodal AI model that can process up to 1 million tokens in a single context. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Gemini 3 Flash** (`databricks-gemini-3-flash`) – High-speed, cost-efficient multimodal AI model for complex video analysis, data extraction, and visual Q&As in near real-time. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Gemini 3.1 Flash Lite** (`databricks-gemini-3-1-flash-lite`) – The fastest and most cost-efficient model in the Gemini 3 series, optimized for high-throughput, cost-effective deployments. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Anthropic Models

All Anthropic models in the Foundation Model APIs support multimodal inputs including text and image:

- **Claude Opus 4.5** (`databricks-claude-opus-4-5`) – Most capable hybrid reasoning model with a 200K token context window. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Opus 4.6** (`databricks-claude-opus-4-6`) – Most capable hybrid reasoning model with adaptive thinking capabilities and a 1 million token context window. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Opus 4.7** (`databricks-claude-opus-4-7`) – Advanced Opus series with improved accuracy, efficiency, and enhanced vision capabilities, featuring a 1 million token context window. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Opus 4.8** (`databricks-claude-opus-4-8`) – Most capable hybrid reasoning model with further improvements to accuracy, efficiency, and reasoning capabilities, supporting complex extraction and agentic reasoning tasks with image support. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Sonnet 4** (`databricks-claude-sonnet-4`) – State-of-the-art hybrid reasoning model with near-instant responses and extended thinking. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Sonnet 4.5** (`databricks-claude-sonnet-4-5`) – Anthropic's most advanced hybrid reasoning model. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Sonnet 4.6** (`databricks-claude-sonnet-4-6`) – Anthropic's most advanced hybrid reasoning model. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Haiku 4.5** (`databricks-claude-haiku-4-5`) – Anthropic's fastest and most cost-effective model with near-frontier coding quality. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Claude Fable 5** (`databricks-claude-fable-5`) – Mythos-class model designed for autonomous knowledge work and coding. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Meta Models

Meta's Llama models in the Foundation Model APIs support multimodal inputs including text and image:

- **Llama 4 Maverick** (`databricks-llama-4-maverick`) – First of the Llama model family to use a mixture of experts architecture for compute efficiency, optimized for precise image and text understanding use cases. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Other Models

- **Gemma 3 12B** (`databricks-gemma-3-12b`) – 12-billion parameter multimodal and vision language model developed by Google. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Input Types

The supported input types vary by model:

| Model Family | Supported Inputs |
|-------------|-----------------|
| OpenAI GPT models | text, image |
| Google Gemini models | text, image, video, audio |
| Anthropic Claude models | text, image |
| Meta Llama models | text, image |
| Gemma models | text, image |

^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Multimodal Capabilities

Foundation models with multimodal support can process inputs that combine multiple modalities. For example, a model might receive:

- A text description and an image for analysis
- A video with audio for content understanding
- Text and image for document processing

These capabilities enable applications such as:

- **Image analysis** – Describing or analyzing images with text prompts. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Video understanding** – Processing video content for data extraction, classification, or question answering. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Document processing** – Extracting information from documents that combine text and images. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Visual Q&A** – Answering questions about visual content based on text prompts. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Complex video analysis** – Analyzing video content for data extraction and understanding. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Context Windows

Multimodal support is available across models with varying context window sizes:

| Model | Context Window (Total Tokens) |
|-------|------------------------------|
| OpenAI GPT models | 400K |
| Google Gemini 3.1 Pro | 1M |
| Google Gemini 2.5 Pro | 1M |
| Google Gemini 2.5 Flash | 1M |
| Anthropic Claude Opus 4.5 | 200K |
| Anthropic Claude Opus 4.6 | 1M |
| Anthropic Claude Opus 4.7 | 1M |

^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The API endpoints for accessing these models.
- [AI Playground](/concepts/ai-playground.md) – A tool for interacting with supported models.
- [Pay-per-Token Endpoints](/concepts/pay-per-token-endpoints.md) – Usage-based pricing for model queries.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – Recommended for production workloads.
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) – Technique for improving accuracy with external knowledge sources.

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
