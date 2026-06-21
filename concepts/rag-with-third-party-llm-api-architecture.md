---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9232dd240f62f2d194b260199e5898bb2e41625e36539c3eedd80c275ead80c1
  pageDirectory: concepts
  sources:
    - llmops-workflows-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rag-with-third-party-llm-api-architecture
    - RWTLAA
  citations:
    - file: llmops-workflows-on-databricks-databricks-on-aws.md
title: RAG with Third-Party LLM API Architecture
description: Production architecture for retrieval-augmented generation applications that connect to third-party LLM APIs via Databricks External Models
tags:
  - rag
  - llm-api
  - architecture
timestamp: "2026-06-19T19:12:49.121Z"
---

# RAG with Third-Party LLM API Architecture

**RAG with Third-Party LLM API Architecture** refers to a production deployment pattern for a [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) application that connects to a large language model (LLM) hosted externally, rather than self-hosting the model. The architecture uses [Databricks External Models](/concepts/external-models.md) to manage the connection to the external LLM API, and [Model Serving](/concepts/model-serving.md) to expose the application logic.

## Overview

In this architecture, the RAG pipeline is deployed as a model serving endpoint that makes external API calls to one or more internal or third-party LLM APIs. This design is appropriate when the LLM is accessed as a service (e.g., OpenAI, Anthropic, or an internal hosted API) rather than being fine‑tuned and served from Databricks. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Reference Architecture

The production architecture for a RAG application using a third-party LLM API is illustrated in the official Databricks documentation:

![third-party LLM using external model](https://docs.databricks.com/aws/en/assets/images/llmops-rag-3p-fe920f2390a4eb5a216dd39d389d61d4.png)

^[llmops-workflows-on-databricks-databricks-on-aws.md]

The diagram shows the following major components:

| Component | Description |
|-----------|-------------|
| **External Models** | Databricks External Models provide a unified interface for calling third-party LLM APIs, handling credential management and request routing. |
| **Model Serving** | The RAG application logic (including retrieval and prompt construction) is deployed on [Model Serving](/concepts/model-serving.md), which routes requests to the external LLM. |
| **Optional Vector Database** | A vector store (e.g., Databricks AI Search) is used to index documents and perform similarity search. It can be replaced by directly querying the LLM through the Model Serving endpoint. |
| **Human Feedback** | Human review and feedback loops are integrated into monitoring and evaluation, often using the MLflow review app. |

^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Key Architectural Differences from Traditional MLOps

Compared to self-hosted LLM or traditional ML deployments, this architecture introduces several new considerations:

- **External API calls** : The Model Serving endpoint makes outbound API calls to third‑party LLM endpoints, adding network latency and potential reliability concerns. Credentials for these APIs must be managed securely, typically via [Secret Scopes](/concepts/databricks-secret-scopes.md) or External Models credentials. ^[llmops-workflows-on-databricks-databricks-on-aws.md]
- **Complexity and governance** : The decoupling of the LLM from the serving infrastructure adds operational complexity and requires careful monitoring of API usage, cost, and data privacy. The Databricks External Models feature helps unify governance across multiple providers. ^[llmops-workflows-on-databricks-databricks-on-aws.md]
- **Vector database integration** : The optional vector index is often a [Delta Table](/concepts/delta-lake-table.md) synced with Databricks AI Search. The retrieval logic is packaged as a model artifact (e.g., LangChain or PyFunc) and logged with MLflow. ^[llmops-workflows-on-databricks-databricks-on-aws.md]
- **Human feedback** : Human evaluation loops are essential for monitoring LLM quality. Feedback is managed as data (often streaming) and incorporated into monitoring dashboards. The MLflow review app facilitates this collection. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Use Cases

This architecture is suitable when:
- The development team wants to leverage a powerful LLM without the expense of hosting it.
- The application requires fast iteration using a model provided as a service.
- A fine‑tuned or self‑hosted model is not necessary or feasible.

In contrast, for scenarios where the LLM is fine‑tuned on custom data and self‑hosted, the [RAG with Fine-tuned Open Source Model Architecture](/concepts/rag-with-fine-tuned-open-source-model-architecture.md) (also described in the same source) may be more appropriate.

## Related Concepts

- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)
- [Databricks External Models](/concepts/external-models.md)
- [Model Serving](/concepts/model-serving.md)
- Databricks AI Search
- Vector Database
- [LLMOps](/concepts/large-language-models-llms-on-databricks.md)
- [MLflow](/concepts/mlflow.md)
- Human Feedback in MLflow
- [External Model Credentials](/concepts/external-model-configuration.md)

## Sources

- llmops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [llmops-workflows-on-databricks-databricks-on-aws.md](/references/llmops-workflows-on-databricks-databricks-on-aws-6b1b2e6a.md)
