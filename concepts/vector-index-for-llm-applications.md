---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f20d5cc9102805a253032f28500de7cb5accff6cba918d68c90b57b92d54753a
  pageDirectory: concepts
  sources:
    - llmops-workflows-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - vector-index-for-llm-applications
    - VIFLA
    - Vector Indexes
  citations:
    - file: llmops-workflows-on-databricks-databricks-on-aws.md
title: Vector Index for LLM Applications
description: Using vector indexes and Databricks AI Search for fast similarity searches to provide context and domain knowledge in LLM queries
tags:
  - vector-index
  - ai-search
  - rag
timestamp: "2026-06-19T19:12:54.943Z"
---

# Vector Index for LLM Applications

A **vector index** for LLM applications is a data structure that enables fast similarity searches over high-dimensional embeddings, allowing an application to retrieve relevant context or domain knowledge to augment an LLM query. This retrieval-augmented generation (RAG) pattern is a common architectural component in production LLM systems. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Use in Retrieval-Augmented Generation

RAG applications combine an LLM with an external knowledge source. The vector index stores embeddings of documents or data points; when a user query arrives, the index is searched for the most semantically similar items. Those items are then provided as context to the LLM, improving the factual accuracy and relevance of the generated response. In a Databricks environment, the vector index can replace or complement direct querying of the LLM through a [Model Serving](/concepts/model-serving.md) endpoint. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Databricks AI Search

Databricks provides an integrated **AI Search** functionality that allows you to use any [Delta table](/concepts/delta-lake-table.md) in [Unity Catalog](/concepts/unity-catalog.md) as a vector index. The AI Search index automatically syncs with the underlying Delta table, ensuring that updates to the source data are reflected in the index without manual re-indexing. This tight integration simplifies the operational overhead of maintaining a separate vector database. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Model Artifact and MLflow Logging

You can create a model artifact that encapsulates the logic to retrieve information from an AI Search index and provide the returned data as context to the LLM. This artifact can then be logged using either the MLflow LangChain model flavor or the PyFunc model flavor, enabling standardized model management and deployment through the [MLflow](/concepts/mlflow.md) lifecycle. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — The architectural pattern that commonly relies on vector indexes.
- AI Search — Databricks’ integrated service for building and managing vector indexes on Delta tables.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that stores the Delta tables used as AI Search indexes.
- [Delta table](/concepts/delta-lake-table.md) — The storage format for the underlying data that the vector index syncs with.
- [Model Serving](/concepts/model-serving.md) — The endpoint through which LLM queries can be made directly or supplemented with indexed context.
- [MLflow](/concepts/mlflow.md) — The platform used to log and manage the retrieval model artifact.
- LangChain — A framework for building LLM applications, supported as a model flavor in MLflow.
- PyFunc — A generic Python function model flavor in MLflow.

## Sources

- llmops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [llmops-workflows-on-databricks-databricks-on-aws.md](/references/llmops-workflows-on-databricks-databricks-on-aws-6b1b2e6a.md)
