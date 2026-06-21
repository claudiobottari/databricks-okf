---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c9d1fa6787a01de3c2380b90ebfe8b1f23f7553f48051c3be2522a66db5afd1
  pageDirectory: concepts
  sources:
    - example-use-features-with-structured-rag-applications-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - langchaintool-for-feature-lookup
    - LFFL
    - LangChainTool
  citations:
    - file: example-use-features-with-structured-rag-applications-databricks-on-aws.md
title: LangChainTool for Feature Lookup
description: A LangChain tool created to query a Databricks feature serving endpoint for relevant structured data in a RAG pipeline
tags:
  - langchain
  - RAG
  - databricks
timestamp: "2026-06-18T12:14:09.264Z"
---

# LangChainTool for Feature Lookup

The **LangChainTool for Feature Lookup** is a tool that enables a LangChain Agent to retrieve structured data from an online table via a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) during a retrieval-augmented generation (RAG) workflow. It bridges feature engineering in Unity Catalog with generative AI applications by providing a standard LangChain interface for real-time feature lookups. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Overview

In structured RAG applications, the agent needs access to up-to-date structured data (e.g., customer profiles, inventory levels) alongside unstructured text. Databricks supports this pattern using online tables hosted on feature serving endpoints. The LangChainTool wraps the endpoint call so the agent can query features as part of its reasoning loop. The typical workflow is:

1. Create a feature serving endpoint backed by an online table.
2. Create a LangChainTool that uses the endpoint to look up relevant data.
3. Include the tool in the LangChain agent's tool set.
4. Deploy the agent behind a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) for production. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Creating the Tool

The LangChainTool is built by instantiating a LangChain `Tool` class that calls the feature serving endpoint. The tool's `_run` method sends a request to the endpoint with the lookup key (e.g., a user ID or product ID) and returns the structured data as a string that the LLM can consume. The exact implementation depends on the LangChain version and the feature serving SDK, but the pattern is consistent:

- Define a function that takes a lookup query and returns the feature values from the endpoint.
- Wrap the function with `Tool(name="feature_lookup", func=my_lookup_function, description="...")`.
- Add the tool to the agent's tool list. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Usage in a LangChain Agent

Once registered, the agent can invoke the tool during its reasoning steps. For example, when answering a customer support question, the agent might call the feature lookup tool to retrieve the customer's recent orders, subscription status, or other context stored in the online table. This structured data is combined with the prompt to generate a more accurate, context-aware response. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Deployment

After the LangChain agent is configured with the feature lookup tool, it can be deployed to a model serving endpoint. Databricks provides a notebook (see the demo notebook linked in the source) that walks through the complete flow from creating the online table to serving the agent. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Related Concepts

- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) — The REST endpoint that serves online features from an online table.
- [Online Table](/concepts/online-tables.md) — A low-latency, continuously updated table used for real-time feature lookups.
- RAG Application — Retrieval-Augmented Generation, the overarching pattern.
- LangChain Agent — The LangChain framework for building agentic applications.
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — The endpoint that hosts the final agent for inference.

## Sources

- example-use-features-with-structured-rag-applications-databricks-on-aws.md

# Citations

1. [example-use-features-with-structured-rag-applications-databricks-on-aws.md](/references/example-use-features-with-structured-rag-applications-databricks-on-aws-38c29ed7.md)
