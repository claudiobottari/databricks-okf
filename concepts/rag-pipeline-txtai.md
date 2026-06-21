---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a2bf1005029af5bf1779586149cb4ddcd41201a0ad4d17b88e6242d27dd8d281
  pageDirectory: concepts
  sources:
    - tracing-txtai-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rag-pipeline-txtai
    - RP(
    - RAG Pipeline
    - RAG pipeline
    - txtai RAG pipeline
  citations:
    - file: tracing-txtai-databricks-on-aws.md
title: RAG Pipeline (txtai)
description: Retrieval Augmented Generation pipeline in txtai that combines embeddings retrieval with LLM generation, supporting custom prompt templates and traceable via MLflow
tags:
  - txtai
  - rag
  - retrieval
  - generation
timestamp: "2026-06-19T23:13:38.831Z"
---

## RAG Pipeline ([txtai](/concepts/txtai.md))

A **RAG Pipeline ([txtai](/concepts/txtai.md))** refers to the retrieval-augmented generation workflow built with the [txtai](/concepts/txtai.md)](https://github.com/neuml/[txtai](/concepts/txtai.md)) library, which combines an embeddings database (for semantic search) with a large language model (LLM) to answer questions grounded in retrieved context. The [txtai](/concepts/txtai.md) library provides a dedicated `RAG` class that orchestrates the retrieval and generation steps. ^[tracing-txtai-databricks-on-aws.md]

### Overview

In a [txtai](/concepts/txtai.md) RAG pipeline, a user question is first used to query an `Embeddings` index (the retriever) for relevant passages. The retrieved context is then inserted into a prompt template, and the completed prompt is passed to an LLM (the generator) to produce a final answer. The entire flow can be automatically traced by [MLflow Tracing](/concepts/mlflow-tracing.md) when `mlflow.[txtai](/concepts/txtai.md).autolog()` is enabled. ^[tracing-txtai-databricks-on-aws.md]

### Key Components

- **Embeddings (Retriever):** A pre‑loaded `txtai.Embeddings` instance, typically loaded from a Hugging Face Hub container (e.g., `neuml/txtai-wikipedia-slim`). This provides the similarity search backbone. ^[tracing-txtai-databricks-on-aws.md]
- **LLM (Generator):** A language model specified by its Hugging Face model ID (e.g., `hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4`). The RAG pipeline passes the formatted prompt to this model. ^[tracing-txtai-databricks-on-aws.md]
- **Prompt Template:** A string template that embeds the user's `{question}` and the retrieved `{context}`. The template can also include a system message (via the `system` parameter) to set the assistant’s behavior. ^[tracing-txtai-databricks-on-aws.md]
- **`context` parameter:** Controls how many chunks are retrieved from the embeddings index (e.g., `context=10` retrieves the top 10 most relevant passages). ^[tracing-txtai-databricks-on-aws.md]

### Example: Tracing a [txtai](/concepts/txtai.md) RAG Pipeline with [MLflow](/concepts/mlflow.md)

The following code demonstrates a complete [txtai](/concepts/txtai.md) RAG pipeline with automatic [MLflow Tracing](/concepts/mlflow-tracing.md) enabled: ^[tracing-txtai-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]
from [[txtai|txtai]] import Embeddings, RAG

# Enable [[mlflow|MLflow]] auto-tracing for [[txtai|txtai]]
[[mlflow|MLflow]].[[txtai|txtai]].autolog()

# Load a prebuilt Wikipedia embeddings index
wiki = Embeddings()
wiki.load(provider="huggingface-hub", container="neuml/txtai-wikipedia-slim")

# Define the prompt template
template = """Answer the following question using only the context below. Only include information
specifically discussed.
question: {question}
context: {context} """

# Create the RAG pipeline
rag = RAG(
    wiki,
    "hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4",
    system="You are a friendly assistant. You answer questions from users.",
    template=template,
    context=10,
)

# Run a query
rag("Tell me about the Roman Empire", maxlength=2048)
```

When executed, [MLflow](/concepts/mlflow.md) captures [Traces](/concepts/traces.md) for the retrieval step (the embeddings search), the prompt construction, and the LLM invocation. The [Traces](/concepts/traces.md) are logged to the active [MLflow Experiment](/concepts/mlflow-experiment.md) and can be viewed in the Databricks Trace UI. ^[tracing-txtai-databricks-on-aws.md]

### Prerequisites

- Install required packages: `pip install --upgrade "[MLflow](/concepts/mlflow.md)[databricks]>=3.1" [txtai](/concepts/txtai.md) mlflow-txtai`. The `mlflow-txtai` extension is necessary for autologging support. ^[tracing-txtai-databricks-on-aws.md]
- Set environment variables for Databricks tracking (if outside a Databricks notebook): `DATABRICKS_HOST` and `DATABRICKS_TOKEN`. ^[tracing-txtai-databricks-on-aws.md]
- Provide the appropriate LLM provider API key (e.g., `OPENAI_API_KEY` or `HUGGING_FACE_HUB_TOKEN`) if the LLM model requires one. ^[tracing-txtai-databricks-on-aws.md]
- On serverless compute clusters, [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks must be explicitly enabled by calling `mlflow.[txtai](/concepts/txtai.md).autolog()`. ^[tracing-txtai-databricks-on-aws.md]

### Related Concepts

- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- txtai embeddings database
- Prompt template
- Semantic search

### Sources

- tracing-txtai-databricks-on-aws.md

# Citations

1. [tracing-txtai-databricks-on-aws.md](/references/tracing-txtai-databricks-on-aws-a07dafba.md)
