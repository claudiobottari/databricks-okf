---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6cffbb397b81590df49ce77aa9d934d985cf93176aa4d93b6efcbfa4ba8e36b1
  pageDirectory: concepts
  sources:
    - example-use-features-with-structured-rag-applications-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - online-tables-in-unity-catalog
    - OTIUC
  citations:
    - file: example-use-features-with-structured-rag-applications-databricks-on-aws.md
title: Online Tables in Unity Catalog
description: Real-time synchronised tables in Databricks Unity Catalog that enable low-latency lookups of structured data for serving in applications.
tags:
  - unity-catalog
  - databricks
  - real-time
timestamp: "2026-06-19T10:25:26.785Z"
---

# Online Tables in Unity Catalog

**Online Tables in Unity Catalog** are a feature that enables low-latency access to structured data for real-time applications, particularly for [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) workloads. They are managed within Unity Catalog and can be hosted on feature serving endpoints for serving data to generative AI applications. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Overview

Online tables store structured data that a RAG application needs to retrieve at inference time. They are created as part of feature engineering in Unity Catalog and are the foundation for building structured RAG pipelines that combine unstructured text retrieval with structured data lookups. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Creating an Online Table

An online table is created from a source Delta table in Unity Catalog. The table is automatically synchronized to a low-latency online store that can be queried via a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md). The online table is the serving-side representation of the data, optimized for fast key-based lookups. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Integration with RAG Applications

The primary use case for online tables in Unity Catalog is supporting structured RAG applications. The typical workflow involves:

1. **Create a feature serving endpoint** that hosts the online table.
2. **Create a LangChainTool** that uses the endpoint to look up relevant data from the online table.
3. **Use the tool in a LangChain agent** so that during the RAG pipeline, the agent can fetch structured data from the online table when needed.
4. **Create a model serving endpoint** to host the complete LangChain application, making it available for real-time inference. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

This integration allows RAG applications to combine semantic search over documents with precise lookups of structured, often tabular, data (e.g., customer records, product catalogs, or metadata). ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Demo Notebook

The Databricks documentation includes a notebook titled "Online tables with RAG applications demo notebook" that illustrates how to use online tables and feature serving endpoints for RAG applications. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Related Concepts

- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) – The serving infrastructure that hosts online tables.
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) – The broader feature store framework.
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) – The pattern that benefits from online tables.
- LangChain – The framework used to build the agent that consumes online table data.
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) – The endpoint that serves the final application.

## Sources

- example-use-features-with-structured-rag-applications-databricks-on-aws.md

# Citations

1. [example-use-features-with-structured-rag-applications-databricks-on-aws.md](/references/example-use-features-with-structured-rag-applications-databricks-on-aws-38c29ed7.md)
