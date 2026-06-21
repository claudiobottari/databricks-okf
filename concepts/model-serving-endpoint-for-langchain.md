---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1c19fcbf555a252b94c78efc15555734ed38324e335fcbf2b20b72bfad483c75
  pageDirectory: concepts
  sources:
    - example-use-features-with-structured-rag-applications-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-for-langchain
    - MSEFL
  citations:
    - file: example-use-features-with-structured-rag-applications-databricks-on-aws.md
title: Model Serving Endpoint for LangChain
description: A Databricks model serving endpoint used to deploy a LangChain application that uses feature lookups for RAG
tags:
  - databricks
  - model-serving
  - deployment
timestamp: "2026-06-18T12:14:08.499Z"
---

# Model Serving Endpoint for LangChain

A **Model Serving Endpoint for LangChain** is a [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoint that hosts a LangChain application, enabling real-time inference for generative AI workflows such as [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md). This endpoint is the final deployment target after building a LangChain agent that incorporates tools for feature lookup, retrieval, and reasoning. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Overview

In structured RAG applications, the typical pipeline is:

1. Create a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) backed by an [Online Table](/concepts/online-tables.md) that stores structured data.
2. Build a LangChain tool that queries the feature serving endpoint to look up relevant data at inference time.
3. Use the tool within a LangChain agent (e.g., a conversational agent) to retrieve and incorporate structured knowledge into the response.
4. Create a model serving endpoint to host the full LangChain application. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

The model serving endpoint serves the LangChain application as a REST API, handling requests from downstream applications while the agent internally invokes the feature serving endpoint for dynamic retrieval.

## Relationship to Feature Serving Endpoints

The model serving endpoint is distinct from a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md). The feature serving endpoint serves raw feature values (e.g., from online tables) to the LangChain tool; the model serving endpoint serves the complete LangChain application, including its agent logic, prompt templates, and model calls. Both are used together in a structured RAG architecture.

## Workflow Example

The typical steps for deploying a LangChain application on Databricks are:

1. **Create an online table** for the structured data required by the RAG application.
2. **Create a feature serving endpoint** that makes the online table queryable via an API.
3. **Create a LangChain tool** that uses the feature serving endpoint to look up relevant data.
4. **Build a LangChain agent** that uses the tool (and possibly other components) to generate responses.
5. **Create a model serving endpoint** to host the LangChain agent as a production-grade inference service. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

The resulting model serving endpoint can be integrated into any application that needs structured, up-to-date information combined with generative AI capabilities.

## Related Concepts

- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) – Endpoint that serves feature values from online tables
- [Online Tables](/concepts/online-tables.md) – Synchronized tables that provide low-latency access to structured data
- LangChain – The framework for building LLM-powered applications
- LangChain Tool – A reusable function that an agent can invoke
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) – A pattern combining retrieval with generation
- [Databricks Model Serving](/concepts/databricks-model-serving.md) – The infrastructure for deploying and serving ML models

## Sources

- example-use-features-with-structured-rag-applications-databricks-on-aws.md

# Citations

1. [example-use-features-with-structured-rag-applications-databricks-on-aws.md](/references/example-use-features-with-structured-rag-applications-databricks-on-aws-38c29ed7.md)
