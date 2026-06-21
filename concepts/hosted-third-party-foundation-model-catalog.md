---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 19279e2042597f4f912152d935b87862836f87962d2e55299a7a3a672f52d1ec
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hosted-third-party-foundation-model-catalog
    - HTFMC
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Hosted Third-Party Foundation Model Catalog
description: A curated catalog of state-of-the-art foundation models from OpenAI, Google, Anthropic, Meta, and Alibaba Cloud, hosted within the Databricks security perimeter and accessible via named endpoints.
tags:
  - databricks
  - model-catalog
  - llm
timestamp: "2026-06-19T09:52:47.794Z"
---

# Hosted Third-Party Foundation Model Catalog

The **Hosted Third-Party Foundation Model Catalog** is a collection of state-of-the-art open and proprietary models that Databricks makes available through its [Foundation Model APIs](/concepts/foundation-model-apis.md). These models include large language models, multimodal models, code‑specialised models, reasoning models, and text embedding models from leading AI providers. All models are hosted by Databricks within the Databricks security perimeter, allowing customers to use them without managing their own infrastructure. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## How to Access the Models

Models in the catalog can be accessed in two modes:

- **Pay‑per‑token** – customers send query requests and are billed per token consumed. The specific endpoint names (e.g., `databricks-gpt-5-5-pro`) are listed in the catalog documentation. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Provisioned throughput** – recommended for production workloads, this mode supports all models of a given architecture family, including fine‑tuned and custom pre‑trained models. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

Customers can also interact with these models using the [AI Playground](/concepts/ai-playground.md) for experimentation and prompt testing. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Model Families

The catalog includes the following third‑party model families:

| Provider | Model Family | Key Details |
|----------|--------------|-------------|
| **OpenAI** | GPT‑5.5 Pro, GPT‑5.5, GPT‑5.4, GPT‑5.4 mini, GPT‑5.4 nano, GPT‑5.3 Codex, GPT‑5.2 Codex, GPT‑5.2, GPT‑5.1, GPT‑5.1 Codex Max, GPT‑5.1 Codex Mini, GPT‑5, GPT‑5 mini, GPT‑5 nano, GPT OSS 120B, GPT OSS 20B | Text and image inputs; context windows up to 400K tokens; some models are code‑specialised or reasoning‑focused. Some models have ongoing or upcoming retirements. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| **Google** | Gemini 3.1 Flash Lite, Gemini 3.5 Flash, Gemini 3 Flash, Gemini 3.1 Pro Preview, Gemini 3 Pro Preview, Gemini 2.5 Pro, Gemini 2.5 Flash | Multimodal (text, image, video, audio); context windows up to 1M tokens; the Flash series emphasises speed and cost‑efficiency. Gemini 3 Pro Preview is on a global endpoint requiring cross‑geography routing and has a retirement date. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| **Alibaba Cloud** | Qwen3.5 122B A10B, Qwen3‑Embedding‑0.6B, Qwen3‑Next 80B A3B Instruct | Text inputs; MoE architecture; Qwen3.5 122B A10B is reasoning‑only (cannot disable reasoning). The embedding model supports 100+ languages and up to 32K tokens. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| **Meta** | Llama 4 Maverick, Meta‑Llama‑3.3‑70B‑Instruct, Meta‑Llama‑3.1‑405B‑Instruct, Meta‑Llama‑3.1‑8B‑Instruct | Text and image (Llama 4 Maverick), text‑only (others); context up to 128K tokens; Llama 3.1‑405B (pay‑per‑token) and 3.1 Codex Max/Mini are retired or retiring. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| **Anthropic** | Claude Haiku 4.5, Claude Sonnet 4.6, Claude Sonnet 4.5, Claude Fable 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Opus 4.5, Claude Sonnet 4, Claude Opus 4.1 | Text and image (most models); hybrid reasoning; some models have 1M token context windows (Opus 4.7, 4.6). Claude Fable 5 has special data retention for trust and safety. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |
| **Embedding models** | GTE Large (En), BGE Large (En), Qwen3‑Embedding‑0.6B | Text embeddings for semantic search, retrieval, clustering; GTE and BGE have 1024‑dimension vectors; Qwen3‑Embedding supports up to 32K context. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md] |

## Usage Notes

- **Accuracy caveats** – All LLMs may omit facts or produce false information. Databricks recommends using [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) in scenarios where accuracy is critical. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Model terms** – Customers are responsible for ensuring compliance with each model’s applicable terms (e.g., Anthropic’s usage policy, Llama Community License). ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Geographic routing** – Some models (Gemini 3 Pro Preview, GPT‑5.1 Codex Max/Mini) require [cross‑geography routing](/concepts/cross-geography-routing-for-global-endpoints.md) to be enabled. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]
- **Retirements** – Several models have scheduled retirement dates. Databricks provides replacement recommendations and migration guidance in the [Retired Models Policy](/concepts/partner-model-retirement-policy.md). ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Additional Resources

- [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models)
- [Foundation model REST API reference](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/api-reference)
- [Applicable model terms](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models)

## Related Wiki Pages

- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Pay-per-Token Endpoints](/concepts/pay-per-token-endpoints.md)
- [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md)
- [AI Playground](/concepts/ai-playground.md)
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)
- [Retired Models Policy](/concepts/partner-model-retirement-policy.md)

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
