---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ec6aa89582674c6af4c218e8184b0c312d6c3b09ee5948dbcd84a453ec3551e3
  pageDirectory: concepts
  sources:
    - example-use-features-with-structured-rag-applications-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - langchain-tool-for-feature-serving
    - LTFFS
  citations:
    - file: example-use-features-with-structured-rag-applications-databricks-on-aws.md
title: LangChain Tool for Feature Serving
description: A LangChain tool wrapper that calls a Databricks feature serving endpoint to retrieve structured data augmenting the context passed to an LLM.
tags:
  - langchain
  - rag
  - databricks
timestamp: "2026-06-19T10:25:17.344Z"
---

# LangChain Tool for Feature Serving

The **LangChain Tool for Feature Serving** is a component that connects a LangChain agent to a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) in Unity Catalog, enabling the agent to look up structured data from [Online Tables](/concepts/online-tables.md) at inference time. This tool is a key building block for structured [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications on Databricks.

## Overview

In a structured RAG workflow, the agent needs to retrieve relevant, up-to-date data (for example, customer profiles, product inventories, or transaction histories) from an online feature store. The LangChain Tool wraps a feature serving endpoint so that the agent can call it as one of its available actions during a chain of reasoning. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Typical Workflow

The lifecycle of a LangChain Tool for Feature Serving follows these high-level steps:

1. **Create a Feature Serving Endpoint** — Host the structured data (backed by an online table) on a scalable endpoint that supports low-latency lookups.
2. **Create the LangChain Tool** — Instantiate a LangChain tool that points to the feature serving endpoint and defines how the agent should use it (e.g., input schema, description).
3. **Integrate into a LangChain Agent** — Add the tool to the agent’s toolkit so the agent can decide when to query the online feature store.
4. **Deploy as a Model Serving Endpoint** — Package the entire LangChain application (including the agent and the tool) behind a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) for production serving.

^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Benefits

- **Low-latency lookups**: Feature serving endpoints are optimized for real-time inference, keeping the RAG pipeline fast.
- **Separation of concerns**: Structured data lives in Unity Catalog as online tables, while the LangChain agent orchestrates retrieval and generation.
- **Reusability**: The same tool can be used across multiple agent configurations or experiments.

## Related Concepts

- [Online Tables](/concepts/online-tables.md) – The source of structured data in Unity Catalog that powers the feature serving endpoint.
- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) – The serving infrastructure that exposes online features via REST API.
- LangChain Agent – The orchestrator that selects and invokes tools based on user input.
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) – The deployment target for the full RAG application.
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) – The overall pattern of combining retrieval with generation.

## Sources

- example-use-features-with-structured-rag-applications-databricks-on-aws.md

# Citations

1. [example-use-features-with-structured-rag-applications-databricks-on-aws.md](/references/example-use-features-with-structured-rag-applications-databricks-on-aws-38c29ed7.md)
