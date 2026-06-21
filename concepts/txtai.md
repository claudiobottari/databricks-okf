---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ffeeecf86cc68acf23e88f62d8b389decb148c1ded0e0beb61928af14627eb5b
  pageDirectory: concepts
  sources:
    - tracing-txtai-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  citations:
    - file: tracing-txtai-databricks-on-aws.md
title: txtai
description: An all-in-one embeddings database for semantic search, LLM orchestration, and language model workflows
tags:
  - embeddings
  - semantic-search
  - llm-orchestration
timestamp: "2026-06-19T23:13:28.486Z"
---

# txtai

**txtai** is an all-in-one embeddings database for semantic search, large language model (LLM) orchestration, and language model workflows. It provides a unified framework for building [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) pipelines, semantic search applications, and AI agents that can retrieve and reason over structured and unstructured data. ^[tracing-txtai-databricks-on-aws.md]

## Overview

txtai combines vector embeddings with traditional search and LLM capabilities. It supports a variety of workflows including text extraction, embedding generation, semantic search, RAG, and autonomous agent execution. The library is designed to be modular, allowing users to compose different pipelines such as the Textractor pipeline, the RAG pipeline, and the Agent pipeline. ^[tracing-txtai-databricks-on-aws.md]

## [MLflow Tracing](/concepts/mlflow-tracing.md) Integration

[MLflow Tracing](/concepts/mlflow-tracing.md) provides [Automatic Tracing](/concepts/automatic-tracing.md) capability for txtai. When auto tracing is enabled by calling `mlflow.txtai.autolog()`, [MLflow](/concepts/mlflow.md) captures [Traces](/concepts/traces.md) for LLM invocations, embeddings, AI Search operations, and logs them to the active [MLflow Experiment](/concepts/mlflow-experiment.md). This enables debugging and observability of txtai applications through the [[mlflow-trace|MLflow Trace]] UI. ^[tracing-txtai-databricks-on-aws.md]

### Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with txtai, the following packages must be installed:

- `mlflow[databricks]>=3.1` ([MLflow 3](/concepts/mlflow-3.md) is recommended)
- `txtai`
- `mlflow-txtai` (extension package)

For development environments, install with pip:

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" txtai mlflow-txtai
```

Additionally, users must configure Databricks environment variables (`DATABRICKS_HOST` and `DATABRICKS_TOKEN`) when running outside of Databricks notebooks. Inside Databricks notebooks, these credentials are automatically set. LLM provider API keys (e.g., `OPENAI_API_KEY`) must also be configured if the txtai pipeline uses an external LLM. ^[tracing-txtai-databricks-on-aws.md]

### Serverless Compute Note

On serverless compute clusters, [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks is not automatically enabled. Users must explicitly call the appropriate `mlflow.<library>.autolog()` function for the specific integration they want to trace. ^[tracing-txtai-databricks-on-aws.md]

## Example Workflows

### Textractor Pipeline

The [Textractor pipeline](/concepts/textractor-pipeline-txtai.md) extracts text from data sources. After enabling `mlflow.txtai.autolog()`, a textractor instance can be run and its [Traces](/concepts/traces.md) will be captured:

```python
import [[mlflow|MLflow]]
from txtai.pipeline import Textractor

[[mlflow|MLflow]].txtai.autolog()
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/txtai-demo")

textractor = Textractor()
textractor("https://github.com/neuml/txtai")
```

^[tracing-txtai-databricks-on-aws.md]

### [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)

The [txtai RAG pipeline](/concepts/rag-pipeline-txtai.md) combines an embeddings index with an LLM to answer questions using retrieved context. The following example loads a Wikipedia embeddings index and creates a RAG pipeline:

```python
import [[mlflow|MLflow]]
from txtai import Embeddings, RAG

[[mlflow|MLflow]].txtai.autolog()

wiki = Embeddings()
wiki.load(provider="huggingface-hub", container="neuml/txtai-wikipedia-slim")

template = """Answer the following question using only the context below…"""
rag = RAG(
    wiki,
    "hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4",
    system="You are a friendly assistant…",
    template=template,
    context=10,
)
rag("Tell me about the Roman Empire", maxlength=2048)
```

^[tracing-txtai-databricks-on-aws.md]

### Agent

The [txtai Agent](/concepts/txtai-agent.md) can autonomously perform multi-step research. The example below creates an astronomy research agent that searches an embeddings database and produces a Markdown report:

```python
import [[mlflow|MLflow]]
from txtai import Agent, Embeddings

[[mlflow|MLflow]].txtai.autolog()

def search(query):
    return embeddings.search(
        "SELECT id, text, distance FROM txtai WHERE similar(:query)", 10,
        parameters={"query": query},
    )

embeddings = Embeddings()
embeddings.load(provider="huggingface-hub", container="neuml/txtai-astronomy")

agent = Agent(tools=[search], llm="hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4", max_iterations=10)

agent(
    "Write a detailed list with explanations of 10 candidate stars…",
    maxlength=16000,
)
```

^[tracing-txtai-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — Captures and organizes trace data for RAG and agent workflows
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — A pattern that combines retrieval and generation
- Semantic Search — Search based on meaning rather than keywords
- Embeddings — Vector representations of data used for similarity search
- AI Agents — Autonomous systems that combine tools and LLMs
- LLM Orchestration — Coordinating LLM calls with other components

## Sources

- tracing-txtai-databricks-on-aws.md

# Citations

1. [tracing-txtai-databricks-on-aws.md](/references/tracing-txtai-databricks-on-aws-a07dafba.md)
