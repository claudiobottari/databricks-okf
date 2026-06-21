---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 14ff1a5a1dd691d28d96b13ed8ade810233bea856d018b45e5185169beaff6a2
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - hybrid-reasoning-models
    - HRM
    - Query Reasoning Models
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Hybrid Reasoning Models
description: A class of AI models (e.g., Claude Opus 4.x, Gemini 2.5/3 Pro) that offer both near-instant responses and extended/deep thinking modes depending on task complexity, blending fast inference with deliberate reasoning.
tags:
  - reasoning
  - llm
  - architecture
  - model-capabilities
timestamp: "2026-06-19T18:13:47.973Z"
---

# Hybrid Reasoning Models

**Hybrid reasoning models** are a class of large language models that combine two inference modes within a single architecture: near-instant responses for straightforward tasks and extended, chain-of-thought reasoning for complex problems that require deep analysis or multi-step problem solving. The model automatically adjusts its reasoning depth based on the complexity of the input. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## How Hybrid Reasoning Works

Hybrid reasoning models offer two distinct modes of operation. For simple prompts—such as routine classification, basic instruction-following, or straightforward Q&A—the model responds nearly instantly without visible internal deliberation. For hard problems—such as advanced mathematics, complex code generation, or multi-step agentic workflows—the model engages extended thinking, producing intermediate reasoning traces before arriving at a final answer. The choice between modes is determined automatically by the task complexity. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

This architecture is described for several models available through Databricks Foundation Model APIs, including the Anthropic Claude Sonnet series (Claude Sonnet 4, 4.5, 4.6) and the Claude Opus series (Opus 4.5, 4.6, 4.7, 4.8), as well as Google Gemini models (Gemini 2.5 Flash, 2.5 Pro, 3 Pro Preview, 3.1 Pro Preview). ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Available Hybrid Reasoning Models

Databricks Foundation Model APIs provide hybrid reasoning models from multiple providers. All listed endpoints are hosted by Databricks within the Databricks security perimeter. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Anthropic Claude Sonnet Series

| Model | Endpoint Name | Context Window | Description |
|-------|---------------|----------------|-------------|
| Claude Sonnet 4 | `databricks-claude-sonnet-4` | 200K tokens | Near-instant responses and extended thinking for code development, content analysis, and agent applications. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| Claude Sonnet 4.5 | `databricks-claude-sonnet-4-5` | 200K tokens | Advanced hybrid reasoning balancing throughput and deep thinking for customer-facing agents and production coding. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| Claude Sonnet 4.6 | `databricks-claude-sonnet-4-6` | 200K tokens | Most advanced Sonnet hybrid reasoning model; two modes based on task complexity. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |

### Anthropic Claude Opus Series

| Model | Endpoint Name | Context Window | Description |
|-------|---------------|----------------|-------------|
| Claude Opus 4.5 | `databricks-claude-opus-4-5` | 200K tokens | Most capable hybrid reasoning model for complex tasks requiring deep analysis and extended thinking. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| Claude Opus 4.6 | `databricks-claude-opus-4-6` | 1M tokens | Adaptive thinking with max effort level for demanding tasks; excels at research and multi-step workflows. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| Claude Opus 4.7 | `databricks-claude-opus-4-7` | 1M tokens | Improved accuracy and efficiency with enhanced vision; strong on extraction and agentic reasoning. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| Claude Opus 4.8 | `databricks-claude-opus-4-8` | 1M tokens | Most capable Opus hybrid model; further improved accuracy, efficiency, and reasoning. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |

### Google Gemini Pro Series

| Model | Endpoint Name | Context Window | Description |
|-------|---------------|----------------|-------------|
| Gemini 2.5 Flash | `databricks-gemini-2-5-flash` | 1M tokens | Google's first fully hybrid reasoning model; optimized for real-time and high-volume applications. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| Gemini 2.5 Pro | `databricks-gemini-2-5-pro` | 1M tokens | Hybrid reasoning with "Deep Think Mode" and built-in audio output; excels at complex analysis. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| Gemini 3 Pro Preview | `databricks-gemini-3-pro` | 1M tokens | State-of-the-art hybrid reasoning with built-in multimodal capabilities. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| Gemini 3.1 Pro Preview | `databricks-gemini-3-1-pro` | 1M tokens | Stronger reasoning and document intelligence; excels at deep analysis and multimodal understanding. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |

## Comparison with Reasoning-Only Models

Hybrid reasoning models are distinct from reasoning-only models such as Alibaba Cloud Qwen3.5 122B A10B. As a reasoning-only model, Qwen3.5 122B A10B always reasons before responding, and its reasoning cannot be disabled. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] In contrast, hybrid models dynamically decide whether to reason deeply or respond instantly based on the task.

## Accuracy Considerations

As with other large language models, hybrid reasoning model output might omit some facts and occasionally produce false information. Databricks recommends using [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) in scenarios where accuracy is especially important. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The service that hosts these models in Databricks workspaces
- Chain-of-Thought Reasoning — The deep reasoning mode used for complex tasks
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — Recommended for accuracy-critical applications
- [AI Playground](/concepts/ai-playground.md) — Interactive interface for experimenting with supported models
- [Pay-per-Token Endpoints](/concepts/pay-per-token-endpoints.md) — Usage-based pricing for foundation model access
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Recommended deployment mode for production workloads
- Hybrid MoE Models — Mixture-of-Experts architectures combining inference modes
- Reasoning-Only Models — Models that always perform chain-of-thought reasoning

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
