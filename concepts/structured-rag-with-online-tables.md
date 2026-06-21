---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d3df8c04b103c3ed6ab583f22c2384f4b50b6a5e7b89180f7f281f387b2f9677
  pageDirectory: concepts
  sources:
    - example-use-features-with-structured-rag-applications-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - structured-rag-with-online-tables
    - SRWOT
  citations:
    - file: example-use-features-with-structured-rag-applications-databricks-on-aws.md
title: Structured RAG with Online Tables
description: Using Databricks online tables to serve structured data (e.g., customer metadata, product catalogs) as real-time context for retrieval-augmented generation applications.
tags:
  - rag
  - feature-store
  - databricks
timestamp: "2026-06-19T10:25:55.524Z"
---

```markdown
---
title: Structured RAG with Online Tables
summary: Using Databricks online tables to serve structured data in retrieval-augmented generation (RAG) applications
sources:
  - example-use-features-with-structured-rag-applications-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:14:08.167Z"
updatedAt: "2026-06-18T12:14:08.167Z"
tags:
  - RAG
  - feature-engineering
  - databricks
aliases:
  - structured-rag-with-online-tables
  - SRWOT
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Structured RAG with Online Tables

**Structured RAG with Online Tables** is a pattern that combines [[Retrieval Augmented Generation (RAG)|retrieval-augmented generation]] (RAG) applications with structured data served from [[Online Tables]] in Databricks. By using [[Feature Engineering in Unity Catalog]], developers can create an online table for the structured data that a RAG application requires and host it on a [[Feature Serving Endpoint]]. The RAG application then uses that endpoint to look up relevant data from the online table during inference. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Typical Steps

The typical implementation follows these steps:

1. **Create a feature serving endpoint** – An online table is published and exposed via a REST API endpoint that supports low-latency lookups. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]
2. **Create a [[LangChainTool for Feature Lookup|LangChainTool]]** – The tool wraps the feature serving endpoint so that a LangChain agent can call it to retrieve structured data. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]
3. **Use the tool in a LangChain agent** – The agent is configured with the tool, enabling it to query structured data when responding to user prompts. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]
4. **Create a [[Model Serving Endpoint]]** – The complete LangChain application is deployed to a model serving endpoint for production use. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Demo Notebook

Databricks provides a notebook titled *Online tables with RAG applications demo* that illustrates how to use online tables and feature serving endpoints for RAG applications. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Related Concepts

- [[Retrieval Augmented Generation (RAG)|Retrieval-Augmented Generation]]
- [[Online Tables]]
- [[Feature Serving Endpoint|Feature Serving Endpoints]]
- [[Feature Engineering in Unity Catalog]]
- LangChain
- [[LangChainTool for Feature Lookup|LangChainTool]]
- [[Model Serving Endpoint]]

## Sources

- example-use-features-with-structured-rag-applications-databricks-on-aws.md
```

# Citations

1. [example-use-features-with-structured-rag-applications-databricks-on-aws.md](/references/example-use-features-with-structured-rag-applications-databricks-on-aws-38c29ed7.md)
