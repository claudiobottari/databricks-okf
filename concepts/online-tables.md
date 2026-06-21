---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3e5b95b2dd0a81835efcf6b0919272248c205c175d32948195a28f166a890761
  pageDirectory: concepts
  sources:
    - example-use-features-with-structured-rag-applications-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-tables
    - Online Table
    - online table
  citations:
    - file: example-use-features-with-structured-rag-applications-databricks-on-aws.md
title: Online Tables
description: Unity Catalog tables optimized for low-latency serving of feature data, used to host structured data that RAG applications need to query in real time.
tags:
  - databricks
  - unity-catalog
  - feature-store
timestamp: "2026-06-19T18:44:09.198Z"
---

I'll create the wiki page based solely on the provided source material.

---

# Online Tables

**Online tables** are a Unity Catalog feature that stores structured data in a low-latency, serving-optimized format. They are primarily used in [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications to provide real-time access to structured data during inference. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Use in RAG Applications

In a structured RAG application, an online table holds the structured data that the application needs at query time. The table is hosted on a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md), which exposes the data for fast lookup. The RAG application uses a LangChain Tool to query the endpoint and retrieve relevant rows, which are then incorporated into the prompt context for the GenAI model. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

### Typical Workflow

1. **Create an online table** from a Unity Catalog table containing the structured data required by the RAG application.
2. **Host the online table** on a feature serving endpoint, making it available for low-latency lookups.
3. **Build a LangChain Tool** that wraps the feature serving endpoint, allowing a LangChain agent to retrieve data from the online table.
4. **Use the tool** in a LangChain agent to fetch relevant structured information as part of the RAG retrieval step.
5. **Deploy the LangChain application** on a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) to serve the complete RAG pipeline.

## Related Concepts

- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) — The serving infrastructure that exposes online tables for low-latency access
- LangChain Tool — A LangChain abstraction that wraps external data sources for agent use
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — The application pattern that combines retrieval with generation
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — The serving infrastructure for deploying LangChain applications
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages online tables

## Sources

- example-use-features-with-structured-rag-applications-databricks-on-aws.md

# Citations

1. [example-use-features-with-structured-rag-applications-databricks-on-aws.md](/references/example-use-features-with-structured-rag-applications-databricks-on-aws-38c29ed7.md)
