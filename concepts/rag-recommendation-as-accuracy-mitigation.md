---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5ef7ba9e82bb2925c24be4f0ddd423948f96a8c2ecee129c86877d7838755bd1
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rag-recommendation-as-accuracy-mitigation
    - RRAAM
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: RAG Recommendation as Accuracy Mitigation
description: A consistent recommendation across all documented models to use Retrieval Augmented Generation (RAG) when accuracy is critical, to mitigate the risk of hallucinations and factual omissions.
tags:
  - databricks
  - rag
  - best-practice
  - accuracy
timestamp: "2026-06-19T09:52:34.585Z"
---

# RAG Recommendation as Accuracy Mitigation

**RAG Recommendation as Accuracy Mitigation** refers to the practice of using [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) to address the inherent accuracy limitations of large language models (LLMs). Databricks recommends RAG in scenarios where factual accuracy is especially important, as a countermeasure against the tendency of LLMs to omit facts or produce false information.

## Overview

All large language models, regardless of provider or architecture, can produce outputs that omit some facts or occasionally generate false information — a phenomenon often referred to as hallucination. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important to mitigate this risk. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Scope of the Recommendation

The RAG recommendation applies uniformly across all foundation model families available through Databricks Foundation Model APIs. Every model description in the supported models documentation includes the same advisory language about accuracy limitations and the RAG recommendation. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Affected Model Families

The recommendation applies to models from all major providers, including:

- **OpenAI**: GPT-5.5 Pro, GPT-5.5, GPT-5.4, GPT-5.4 mini, GPT-5.4 nano, GPT-5.3 Codex, GPT-5.2 Codex, GPT-5.2, GPT-5.1, GPT-5.1 Codex Max, GPT-5.1 Codex Mini, GPT-5, GPT-5 mini, GPT-5 nano, GPT OSS 120B, GPT OSS 20B ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Google**: Gemini 3.1 Flash Lite, Gemini 3.5 Flash, Gemini 3 Flash, Gemini 3.1 Pro Preview, Gemini 3 Pro Preview, Gemini 2.5 Pro, Gemini 2.5 Flash, Gemma 3 12B ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Anthropic**: Claude Haiku 4.5, Claude Sonnet 4.6, Claude Sonnet 4.5, Claude Fable 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Opus 4.5, Claude Sonnet 4, Claude Opus 4.1 ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Alibaba Cloud**: Qwen3.5 122B A10B, Qwen3-Next 80B A3B Instruct ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Meta**: Llama 4 Maverick, Meta-Llama-3.3-70B-Instruct, Meta-Llama-3.1-405B-Instruct, Meta-Llama-3.1-8B-Instruct ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Embedding Models

The recommendation also extends to embedding models such as Qwen3-Embedding-0.6B, GTE Large (En), and BGE Large (En). These models are described as especially effective when used in tandem with LLMs for RAG use cases, as they can find relevant text snippets in large document collections to provide context to an LLM. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## How RAG Mitigates Accuracy Issues

RAG improves factual accuracy by grounding LLM responses in retrieved information from authoritative sources rather than relying solely on the model's parametric knowledge. The typical workflow involves:

1. **Retrieval**: An embedding model converts user queries and document chunks into vector representations, then retrieves the most relevant passages from a knowledge base.
2. **Augmentation**: The retrieved passages are inserted into the LLM's context window alongside the original query.
3. **Generation**: The LLM produces a response conditioned on both the query and the retrieved evidence, reducing reliance on potentially incomplete or incorrect internal knowledge.

## Related Concepts

- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — The core technique recommended for accuracy improvement
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The Databricks service through which these models are accessed
- Embedding Models — Models used for the retrieval step in RAG pipelines
- [LLM Hallucination](/concepts/hallucination-scorer.md) — The phenomenon RAG aims to mitigate
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Databricks' recommended mode for production RAG workloads

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
