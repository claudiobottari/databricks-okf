---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f61fe3796bc07b5fc77d949519467ec3780bf083c849be8e2f0a33eada688777
  pageDirectory: concepts
  sources:
    - query-vision-models-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - external-models-vs-foundation-model-apis-on-databricks
    - EMVFMAOD
  citations:
    - file: query-vision-models-databricks-on-aws.md
title: External Models vs Foundation Model APIs on Databricks
description: The distinction between Databricks-hosted foundation models (with specific image handling and token billing) and externally hosted models (where provider documentation governs behavior).
tags:
  - databricks
  - model-serving
  - external-models
  - architecture
timestamp: "2026-06-19T20:05:14.596Z"
---

# External Models vs Foundation Model APIs on Databricks

**External Models** and **Foundation Model APIs** are two distinct approaches for serving machine learning models on Databricks. Both provide access to powerful AI models, but they differ in deployment, management, and usage patterns.

## Foundation Model APIs

Foundation Model APIs provide access to Databricks-hosted foundation models through a unified serving endpoint. These models are managed and maintained by Databricks, offering a fully managed experience for querying models optimized for various tasks, including vision, chat, reasoning, and embeddings. ^[query-vision-models-databricks-on-aws.md]

Key characteristics of Foundation Model APIs include:

- **Managed infrastructure**: Databricks handles model hosting, scaling, and maintenance.
- **Unified API**: A consistent interface for querying different model types.
- **Token-based pricing**: Image inputs and other features contribute to token usage, with pricing available through the Databricks pricing calculator. ^[query-vision-models-databricks-on-aws.md]
- **Built-in limitations**: Databricks documents specific limitations for image understanding and other capabilities for supported foundation models. ^[query-vision-models-databricks-on-aws.md]

## External Models

External Models refer to models served through Databricks Model Serving endpoints that are not hosted by Databricks. These are typically models deployed from external providers or custom models that users bring to the platform. ^[query-vision-models-databricks-on-aws.md]

Key characteristics of External Models include:

- **User-managed deployment**: Users are responsible for deploying and managing the model infrastructure.
- **Provider-specific documentation**: For features like image-to-token conversion and limitations, users must refer to the external provider's documentation rather than Databricks documentation. ^[query-vision-models-databricks-on-aws.md]
- **Flexible configuration**: Users have more control over model selection, configuration, and scaling.

## Comparison

| Aspect | Foundation Model APIs | External Models |
|--------|----------------------|-----------------|
| Hosting | Databricks-managed | User-managed or third-party |
| API consistency | Unified across models | Provider-specific |
| Documentation | Databricks provides model-specific docs | Refer to provider's documentation |
| Image-to-token conversion | Documented by Databricks | Refer to provider's documentation |
| Limitations | Documented by Databricks | Refer to provider's documentation |
| Management overhead | Low | Higher |

## Querying Vision Models

Both approaches support querying vision models through the Chat Completions API. The OpenAI client can be used to send requests to either type of endpoint by specifying the model serving endpoint name as the `model` input. ^[query-vision-models-databricks-on-aws.md]

For Foundation Model APIs, image inputs are automatically converted to tokens, and Databricks provides documentation on token usage and pricing. For External Models, users must consult the provider's documentation for image handling details. ^[query-vision-models-databricks-on-aws.md]

## Choosing Between the Two

Consider Foundation Model APIs when:
- You want a fully managed experience with minimal operational overhead.
- You need access to Databricks-hosted models with documented capabilities and limitations.
- You prefer unified API interfaces across different model types.

Consider External Models when:
- You need models not available through Foundation Model APIs.
- You require more control over model deployment and configuration.
- You have custom or fine-tuned models to serve.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The infrastructure for deploying and querying models on Databricks.
- Foundation Models — Large pre-trained models available through Databricks.
- [Chat Completions API](/concepts/chat-completions-api.md) — The API used for querying chat and vision models.
- Query Vision Models — Specific guidance for image-based model queries.
- [Query Embedding Models](/concepts/text-embedding-models.md) — Querying models for text embeddings.
- [Query Reasoning Models](/concepts/hybrid-reasoning-models.md) — Querying models optimized for reasoning tasks.
- Query Chat Models — Querying models for conversational AI.

## Sources

- query-vision-models-databricks-on-aws.md

# Citations

1. [query-vision-models-databricks-on-aws.md](/references/query-vision-models-databricks-on-aws-afa9c021.md)
