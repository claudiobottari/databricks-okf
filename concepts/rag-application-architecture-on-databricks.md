---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bb0d95de3b79d2603af73e158509a6c9635b137ec1cd34d7c935ab437f25dd04
  pageDirectory: concepts
  sources:
    - example-use-features-with-structured-rag-applications-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rag-application-architecture-on-databricks
    - RAAOD
  citations:
    - file: example-use-features-with-structured-rag-applications-databricks-on-aws.md
    - file: |-
        example-use-features-with-structured-rag-applications-databricks-on-aws.md

        ## Architecture Flow

        The structured data retrieval path follows a layered pipeline:

        - A user query reaches the **Model Serving Endpoint**.
        - The **LangChain Agent** receives the query and determines it needs structured context.
        - The agent calls the **LangChain Tool**
    - file: |-
        which queries the **Feature Serving Endpoint**.
        - The **Feature Serving Endpoint** looks up the relevant data from the **Online Table**.
        - The retrieved structured data is passed back through the tool to the agent
    - file: |-
        which incorporates it into the prompt for the language model.
        - The language model generates a final response
    - file: |-
        which is returned to the user.

        ## Related Concepts

        - [[Retrieval-Augmented Generation (RAG)
title: RAG Application Architecture on Databricks
description: "The four-step pipeline for building structured RAG apps on Databricks: create a feature serving endpoint, build a LangChain tool, use it in a LangChain agent, and host via Model Serving."
tags:
  - databricks
  - architecture
  - rag
  - pipeline
timestamp: "2026-06-19T18:44:26.836Z"
---

```markdown
---
title: RAG Application Architecture on Databricks
summary: "The end-to-end pipeline: create a feature serving endpoint, build a LangChain tool to query it, use the tool in a LangChain agent, and deploy the agent behind a model serving endpoint."
sources:
  - example-use-features-with-structured-rag-applications-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:25:30.056Z"
updatedAt: "2026-06-19T10:25:30.056Z"
tags:
  - rag
  - architecture
  - databricks
aliases:
  - rag-application-architecture-on-databricks
  - RAAOD
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 1
---

## RAG Application Architecture on Databricks

**RAG Application Architecture on Databricks** describes the recommended system design for building production [[Retrieval-Augmented Generation (RAG)]] applications on the Databricks platform. It integrates [[Unity Catalog]] for data governance, Feature Serving and [[Online Tables]] for structured data retrieval, and [[Model Serving]] for hosting the generative AI model, often orchestrated through a framework like LangChain.

## Overview

Retrieval-augmented generation (RAG) is one of the most common approaches to building generative AI applications. Feature engineering in Unity Catalog supports structured RAG applications using online tables. An online table is created for the structured data that the RAG application needs and hosted on a feature serving endpoint. The RAG application uses the feature serving endpoint to look up relevant data from the online table. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

## Core Components and Steps

The typical steps to implement this architecture are as follows: ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]

1. **Create a feature serving endpoint** to host the online table. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]
2. **Create a LangChain Tool** that uses the endpoint to look up relevant data. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]
3. **Use the tool in a LangChain Agent** to retrieve relevant data. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md]
4. **Create a [[Model Serving Endpoint]]** to host the LangChain application. ^[example-use-features-with-structured-rag-applications-databricks-on-aws.md

## Architecture Flow

The structured data retrieval path follows a layered pipeline:

- A user query reaches the **Model Serving Endpoint**.
- The **LangChain Agent** receives the query and determines it needs structured context.
- The agent calls the **LangChain Tool**, which queries the **Feature Serving Endpoint**.
- The **Feature Serving Endpoint** looks up the relevant data from the **Online Table**.
- The retrieved structured data is passed back through the tool to the agent, which incorporates it into the prompt for the language model.
- The language model generates a final response, which is returned to the user.

## Related Concepts

- [[Retrieval-Augmented Generation (RAG)]]
- [[Feature Engineering in Unity Catalog]]
- [[Online Tables]]
- Feature Serving
- [[Model Serving]]
- LangChain
- LangChain Agent
- [[Unity Catalog]]
- [[AI Runtime (AI v5) on Databricks|Generative AI on Databricks]]

## Sources

- example-use-features-with-structured-rag-applications-databricks-on-aws.md
```

# Citations

1. [example-use-features-with-structured-rag-applications-databricks-on-aws.md](/references/example-use-features-with-structured-rag-applications-databricks-on-aws-38c29ed7.md)
2. example-use-features-with-structured-rag-applications-databricks-on-aws.md

## Architecture Flow

The structured data retrieval path follows a layered pipeline:

- A user query reaches the **Model Serving Endpoint**.
- The **LangChain Agent** receives the query and determines it needs structured context.
- The agent calls the **LangChain Tool**
3. which queries the **Feature Serving Endpoint**.
- The **Feature Serving Endpoint** looks up the relevant data from the **Online Table**.
- The retrieved structured data is passed back through the tool to the agent
4. which incorporates it into the prompt for the language model.
- The language model generates a final response
5. which is returned to the user.

## Related Concepts

- [[Retrieval-Augmented Generation (RAG)
