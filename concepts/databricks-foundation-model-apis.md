---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 085f4b7c0a1fd2e7a1437e834fbcd1ea25daa461d2b96e44ce512f3654716611
  pageDirectory: concepts
  sources:
    - ai-governance-databricks-on-aws.md
    - databricks-foundation-model-apis-databricks-on-aws.md
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
    - foundation-model-rest-api-reference-databricks-on-aws.md
    - optimize-prompts-tutorial-databricks-on-aws.md
    - provider-native-apis-databricks-on-aws.md
    - query-a-chat-model-databricks-on-aws.md
    - query-with-the-anthropic-messages-api-databricks-on-aws.md
    - use-foundation-models-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-foundation-model-apis
    - DFMA
    - Databricks Foundation Model API
    - Databricks Foundation Models
  citations:
    - file: databricks-foundation-model-apis-databricks-on-aws.md
    - file: foundation-model-rest-api-reference-databricks-on-aws.md
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
    - file: provider-native-apis-databricks-on-aws.md
    - file: ai-governance-databricks-on-aws.md
    - file: query-a-chat-model-databricks-on-aws.md
    - file: optimize-prompts-tutorial-databricks-on-aws.md
title: Databricks Foundation Model APIs
description: Databricks-hosted foundation models made available through APIs that can be governed via Unity Catalog permissions as securable AI objects.
tags:
  - databricks
  - foundation-models
  - API
  - governance
timestamp: "2026-06-19T17:29:23.347Z"
---

---

title: Databricks Foundation Model APIs
summary: Databricks-hosted foundation models available through Foundation Model APIs with Unity Catalog permissions for access control.
sources:
  - ai-governance-databricks-on-aws.md
  - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  - foundation-model-rest-api-reference-databricks-on-aws.md
  - optimize-prompts-tutorial-databricks-on-aws.md
  - provider-native-apis-databricks-on-aws.md
  - query-a-chat-model-databricks-on-aws.md
  - databricks-foundation-model-apis-databricks-on-aws.md
  - use-foundation-models-databricks-on-aws.md
  - query-with-the-anthropic-messages-api-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:38:13.161Z"
updatedAt: "2026-06-19T13:56:17.515Z"
tags:
  - foundation-models
  - databricks
  - api-permissions
aliases:
  - databricks-foundation-model-apis
  - DFMA
confidence: 0.95
provenanceState: merged
inferredParagraphs: 1
---

# Databricks Foundation Model APIs

**Databricks Foundation Model APIs** provide access to state-of-the-art open and proprietary models through serving endpoints hosted and managed by Databricks. They allow you to query large language models (LLMs) and embedding models without deploying or managing your own model infrastructure. The APIs are designed to be compatible with OpenAI's REST API, making migration of existing applications straightforward. Foundation Model APIs are a Databricks Designated Service and use Databricks Geos to manage data residency when processing customer content. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Modes of use

Foundation Model APIs are offered in three modes to suit different workloads. ^[databricks-foundation-model-apis-databricks-on-aws.md]

### Pay-per-token

This is the easiest way to get started. Preconfigured endpoints for supported models are available in your Databricks workspace under the **Serving** tab. Pay-per-token is recommended for beginning your journey with Foundation Model APIs and can be used for production workloads, though it is not designed for high‑throughput applications. ^[databricks-foundation-model-apis-databricks-on-aws.md]

### Provisioned throughput

Provisioned throughput endpoints provide optimized inference with performance guarantees and are recommended for all production workloads, especially those requiring high throughput, fine‑tuned models, or compliance certifications such as HIPAA. Provisioned throughput supports all models of a given architecture family, including base models, fine‑tuned variants, and custom pre‑trained models. Endpoints can be created using the API or the **Serving** UI and can serve multiple models for A/B testing. ^[databricks-foundation-model-apis-databricks-on-aws.md, foundation-model-rest-api-reference-databricks-on-aws.md]

### AI Functions for batch inference

For batch inference workloads, you can use AI Functions to run inference on any generative AI or ML model. Batch inference pipelines can be created using AI Functions. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Supported models

A wide range of models is available through Foundation Model APIs, including models from OpenAI, Anthropic, Google, Alibaba Cloud, Meta, and others. Each model has a designated endpoint name (for example, `databricks-gpt-5-4-mini`, `databricks-claude-sonnet-4-6`, `databricks-gemini-2-5-flash`) and supports text inputs; many also support image, video, or audio inputs. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

Representative categories include:

- **OpenAI GPT‑5 series** (e.g., GPT‑5.5 Pro, GPT‑5.4 mini, GPT‑5) – general‑purpose reasoning and coding models with multimodal support.
- **Anthropic Claude** (e.g., Claude Opus 4.8, Claude Sonnet 4.6, Claude Haiku 4.5) – hybrid reasoning models with extended thinking capabilities.
- **Google Gemini** (e.g., Gemini 2.5 Pro, Gemini 3.5 Flash, Gemini 3.1 Flash Lite) – multimodal models supporting text, image, video, and audio.
- **Meta Llama** (e.g., Llama 4 Maverick, Meta‑Llama‑3.3‑70B‑Instruct) – open‑weight models optimized for dialogue and reasoning.
- **Alibaba Cloud Qwen** (e.g., Qwen3.5 122B A10B, Qwen3‑Embedding‑0.6B) – MoE reasoning models and embedding models.
- **OpenAI open‑weight models** (e.g., GPT OSS 120B, GPT OSS 20B) – reasoning models with adjustable effort.
- **Embedding models** (e.g., GTE Large, BGE Large, Qwen3‑Embedding) – generate dense vector representations for retrieval and semantic search.

For the complete list, model endpoint names, and retirement schedules, see [Databricks‑hosted foundation models available in Foundation Model APIs](/concepts/databricks-model-serving-foundation-model-apis-fmapi.md). ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## API compatibility

### OpenAI‑compatible APIs

The Chat Completions API, Completions API, and Embeddings API follow OpenAI's request format. Both pay‑per‑token and provisioned throughput endpoints accept the same JSON structure. The Responses API (compatible only with OpenAI models) enables multi‑turn conversations using an `input` field instead of `messages`. Detailed parameter schemas are available in the Foundation model REST API reference. ^[foundation-model-rest-api-reference-databricks-on-aws.md]

### Provider native APIs

When features beyond the unified OpenAI‑compatible API are needed, you can use provider‑specific APIs directly. Databricks supports:

- **OpenAI Responses API** – for GPT‑5 series and GPT‑4o models.
- **Anthropic Messages API** – for Claude models.
- **Google Gemini API** – for Gemini models (text, image, video, audio).

See the dedicated how‑to pages: [Query with the Anthropic Messages API](/concepts/anthropic-messages-api-on-databricks.md), [Query with the OpenAI Responses API](/concepts/openai-responses-api-on-databricks.md). ^[provider-native-apis-databricks-on-aws.md]

## AI governance

Foundation Model APIs integrate with [Unity Catalog](/concepts/unity-catalog.md) for AI governance. Models served through the APIs are securable objects in Unity Catalog, allowing you to grant and revoke access using standard Unity Catalog privileges. [Unity AI Gateway](/concepts/unity-ai-gateway.md) provides centralized control for governing AI traffic, including rate limiting, usage tracking, and cost monitoring across hosted and external LLM endpoints. ^[ai-governance-databricks-on-aws.md]

## Usage examples

You can interact with Foundation Model APIs using the OpenAI Python SDK, the Databricks SDK, or the REST API directly. The following is a minimal chat completion call using the OpenAI SDK:

```python
from openai import OpenAI

client = OpenAI(
    api_key="<databricks-token>",
    base_url="https://<workspace-url>/serving-endpoints"
)
response = client.chat.completions.create(
    model="databricks-meta-llama-3-3-70b-instruct",
    messages=[{"role": "user", "content": "What is the capital of France?"}]
)
print(response.choices[0].message.content)
```

For embedding and completion tasks, see the Foundation model REST API reference. ^[foundation-model-rest-api-reference-databricks-on-aws.md, query-a-chat-model-databricks-on-aws.md]

Foundation Model APIs can also be used from MLflow GenAI for tasks such as prompt optimization, as shown in the MLflow genai optimize_prompts|Optimize prompts tutorial. ^[optimize-prompts-tutorial-databricks-on-aws.md]

For queries using provider-specific SDKs, see:

- [Query with the Anthropic Messages API](/concepts/anthropic-messages-api-on-databricks.md)
- [Query with the OpenAI Responses API](/concepts/openai-responses-api-on-databricks.md)

## Requirements

- A Databricks API token for authentication.
- Serverless compute enabled for provisioned throughput endpoints.
- A workspace in a supported region. See Feature region support for pay‑per‑token and provisioned throughput regions. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Limitations

Foundation Model APIs have rate limits and constraints that vary by model and mode. For detailed limits, see [Foundation Model APIs limits](/concepts/foundation-model-apis-rate-limits.md). Notable limitations include:

- Parallel [function calling](/concepts/llm-function-calling.md) is not supported in the current public preview.
- The maximum number of functions in `tools` is 32.
- Some models have retirement dates (e.g., Meta‑Llama‑3.1‑405B-Instruct, Gemini 3 Pro). ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Related concepts

- [Model Serving](/concepts/model-serving.md) – the underlying infrastructure for serving models on Databricks.
- [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md) – deploying models with performance guarantees.
- [External Models](/concepts/external-models.md) – using third‑party model providers via Databricks.
- Function calling – structured output generation from LLMs.
- [Structured outputs](/concepts/structured-outputs-in-foundation-model-apis.md) – generating JSON‑formatted responses.
- [Foundation Model APIs limits](/concepts/foundation-model-apis-rate-limits.md) – rate and usage limits.
- [Databricks‑hosted foundation models](/concepts/databricks-hosted-foundation-models.md) – the complete list of available models.
- [AI Playground](/concepts/ai-playground.md) – interactive interface for testing supported models.

## Sources

- databricks-foundation-model-apis-databricks-on-aws.md
- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
- foundation-model-rest-api-reference-databricks-on-aws.md
- optimize-prompts-tutorial-databricks-on-aws.md
- provider-native-apis-databricks-on-aws.md
- ai-governance-databricks-on-aws.md
- query-a-chat-model-databricks-on-aws.md
- use-foundation-models-databricks-on-aws.md
- query-with-the-anthropic-messages-api-databricks-on-aws.md

# Citations

1. [databricks-foundation-model-apis-databricks-on-aws.md](/references/databricks-foundation-model-apis-databricks-on-aws-f789bf37.md)
2. [foundation-model-rest-api-reference-databricks-on-aws.md](/references/foundation-model-rest-api-reference-databricks-on-aws-26351d38.md)
3. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
4. [provider-native-apis-databricks-on-aws.md](/references/provider-native-apis-databricks-on-aws-188451d9.md)
5. [ai-governance-databricks-on-aws.md](/references/ai-governance-databricks-on-aws-e6fd4910.md)
6. [query-a-chat-model-databricks-on-aws.md](/references/query-a-chat-model-databricks-on-aws-0a958863.md)
7. [optimize-prompts-tutorial-databricks-on-aws.md](/references/optimize-prompts-tutorial-databricks-on-aws-b91f2148.md)
