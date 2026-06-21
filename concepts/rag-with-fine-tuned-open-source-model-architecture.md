---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7de941f85a05dcbe501f07705f5a094f0eba512f6155a2dff5d444d8277b0da9
  pageDirectory: concepts
  sources:
    - llmops-workflows-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rag-with-fine-tuned-open-source-model-architecture
    - RWFOSMA
  citations:
    - file: llmops-workflows-on-databricks-databricks-on-aws.md
title: RAG with Fine-tuned Open Source Model Architecture
description: Production architecture for retrieval-augmented generation applications that fine-tune an open source model on custom data
tags:
  - rag
  - fine-tuning
  - open-source
timestamp: "2026-06-19T19:12:48.111Z"
---

# RAG with Fine-tuned Open Source Model Architecture

**RAG with Fine-tuned Open Source Model Architecture** refers to a production architecture for [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications that fine-tune an open source [Large Language Model (LLM)](/concepts/large-language-models-llms-on-databricks.md) rather than relying on a third-party API. This approach combines the benefits of Fine-tuning with the retrieval capabilities of RAG to create domain-specific, self-hosted AI applications. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Architecture Overview

The architecture for a RAG application using a fine-tuned open source model follows the general [LLMOps](/concepts/large-language-models-llms-on-databricks.md) production architecture but with several key modifications compared to traditional MLOps workflows. The system integrates a fine-tuned model with a Vector Index for similarity search, all deployed through [Model Serving](/concepts/model-serving.md) endpoints. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

### Key Components

- **Fine-tuned Open Source Model**: A pretrained foundation model that has been customized using domain-specific data through [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md) on Databricks. This replaces the third-party API used in other RAG architectures. ^[llmops-workflows-on-databricks-databricks-on-aws.md]
- **Vector Index**: An optional component that enables fast similarity searches to provide context or domain knowledge in LLM queries. Databricks provides integrated AI Search functionality that uses any [Delta table](/concepts/delta-lake-table.md) in [Unity Catalog](/concepts/unity-catalog.md) as an index, automatically syncing with the source table. ^[llmops-workflows-on-databricks-databricks-on-aws.md]
- **Model Artifact**: Encapsulates the logic to retrieve information from the AI Search index and provide the returned data as context to the LLM. This artifact is logged using the [MLflow](/concepts/mlflow.md) LangChain or PyFunc model flavor. ^[llmops-workflows-on-databricks-databricks-on-aws.md]
- **Model Serving Endpoint**: Provides a unified interface to deploy, govern, and query the fine-tuned model. Unlike third-party API architectures, this endpoint does not make external API calls, reducing latency and credential management complexity. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Workflow

The production workflow consists of two distinct pipelines represented as separate [Lakeflow Jobs](/concepts/lakeflow-jobs.md):

1. **Fine-tuning Pipeline**: Takes a pretrained foundation model from a [Model Hub](/concepts/model-hub-in-llmops.md) (available in Unity Catalog or Databricks Marketplace) and fine-tunes it using custom data to optimize performance for the specific application. ^[llmops-workflows-on-databricks-databricks-on-aws.md]
2. **Deployment Pipeline**: Validates and deploys the fine-tuned model to a Model Serving endpoint. Validating a fine-tuned model before deployment is often a manual process. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Comparison with Third-Party API Architecture

| Aspect | Fine-tuned Open Source Model | Third-Party API |
|--------|------------------------------|-----------------|
| Model source | Self-hosted, fine-tuned from open source | External API via [Databricks External Models](/concepts/external-models.md) |
| Latency | Lower (no external calls) | Higher (external API calls) |
| Credential management | Simpler | More complex |
| Data privacy | Data stays within environment | Data sent to third-party |
| Customization | High (via fine-tuning) | Limited to prompt engineering |

^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Human Feedback Integration

Human feedback loops are essential in most LLM applications and should be managed like other data, ideally incorporated into monitoring based on near real-time streaming. The [MLflow Review App](/concepts/mlflow-review-app.md) helps gather feedback from human reviewers for continuous improvement. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Related Concepts

- LLMOps workflows on Databricks
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md)
- [Model Serving](/concepts/model-serving.md)
- AI Search
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow](/concepts/mlflow.md)
- [Model Hub](/concepts/model-hub-in-llmops.md)
- Databricks Marketplace

## Sources

- llmops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [llmops-workflows-on-databricks-databricks-on-aws.md](/references/llmops-workflows-on-databricks-databricks-on-aws-6b1b2e6a.md)
