---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e93ffd16380f92b7f9e3fe3acdcbf4256b38b0c7fb41c1c50c9be77abf23e9cf
  pageDirectory: concepts
  sources:
    - example-use-features-with-structured-rag-applications-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - langchaintool-with-feature-serving
    - LWFS
  citations:
    - file: example-use-features-with-structured-rag-applications-databricks-on-aws.md
title: LangChainTool with Feature Serving
description: A LangChain tool that wraps a Databricks feature serving endpoint to enable an agent to look up structured data during a RAG workflow.
tags:
  - langchain
  - feature-store
  - rag
  - agent-tools
timestamp: "2026-06-19T18:44:13.458Z"
---

# LangChainTool with Feature Serving

**LangChainTool with Feature Serving** is a pattern for integrating structured data from Databricks [Online Tables](/concepts/online-tables.md) into [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications using the LangChain framework. A LangChainTool wraps a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) so that the LangChain agent can query structured data — such as customer profiles, product inventories, or real-time metrics — and pass the retrieved information as context to a language model. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## How It Works

The workflow combines [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) with LangChain’s tool-use abstraction. An online table stores the structured data that the RAG application needs. That table is hosted on a feature serving endpoint, which exposes a low-latency lookup API. A LangChainTool is created that calls this endpoint; the LangChain agent uses the tool to fetch relevant rows at query time, and the returned data becomes part of the prompt sent to the LLM. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Typical Steps

The process for setting up a LangChainTool with feature serving involves four steps:

1. **Create a feature serving endpoint** that serves an online table containing the structured data.
2. **Create a LangChainTool** that uses the endpoint to look up relevant data. The tool encapsulates the API call and returns the results in a format LangChain can consume.
3. **Use the tool in the LangChain agent** to retrieve relevant data during the RAG workflow. The agent decides when to invoke the tool based on the user query.
4. **Create a [Model Serving Endpoint](/concepts/model-serving-endpoint.md)** to host the complete LangChain application, including the agent and the tool, as a production API. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

A demo notebook is provided that illustrates the full integration, from online table creation to endpoint deployment. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Related Concepts

- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) – The serving infrastructure that exposes online table data via REST APIs.
- [Online Table](/concepts/online-tables.md) – A Unity Catalog table synchronized to a low-latency store for real-time lookups.
- LangChain – The framework used to build agentic RAG applications with tool integration.
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) – Hosts the final LangChain application as a scalable API.
- [RAG (Retrieval-Augmented Generation)](/concepts/retrieval-augmented-generation-rag.md) – The overarching pattern that combines retrieval with generation.

## Sources

- example-use-features-with-structured-rag-applications-databricks-on-aws.md

# Citations

1. [example-use-features-with-structured-rag-applications-databricks-on-aws.md](/references/example-use-features-with-structured-rag-applications-databricks-on-aws-38c29ed7.md)
