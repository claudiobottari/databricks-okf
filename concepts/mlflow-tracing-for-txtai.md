---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ff9c873c89dd2770570483655f44a3d81d8101bf759b98bced5f320f489b62ec
  pageDirectory: concepts
  sources:
    - tracing-txtai-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-for-txtai
    - MTFT
  citations:
    - file: tracing-txtai-databricks-on-aws.md
    - file: tracing-trace-txtai-databricks-on-aws.md
title: MLflow Tracing for txtai
description: Automatic tracing capability for txtai workflows via MLflow's autolog function, capturing traces for LLM invocations, embeddings, and AI Search
tags:
  - mlflow
  - tracing
  - txtai
  - observability
timestamp: "2026-06-19T23:13:28.913Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) for [txtai](/concepts/txtai.md)

**MLflow Tracing for txtai** enables automatic capture and logging of [Traces](/concepts/traces.md) from [txtai](/concepts/txtai.md)](https://github.com/neuml/[txtai](/concepts/txtai.md)) workflows, including LLM invocations, embeddings operations, AI Search queries, and agent interactions. When enabled, [MLflow](/concepts/mlflow.md) records trace data to the active [MLflow Experiment](/concepts/mlflow-experiment.md), allowing developers to debug, observe, and analyze the behavior of [txtai](/concepts/txtai.md) applications such as semantic search, [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md), and agent-based systems. ^[tracing-txtai-databricks-on-aws.md]

## Overview

[txtai](/concepts/txtai.md)](https://github.com/neuml/[txtai](/concepts/txtai.md)) is an all-in-one embeddings database for semantic search, LLM orchestration, and language model workflows. [MLflow](/concepts/mlflow.md) provides [Automatic Tracing](/concepts/automatic-tracing.md) capability for [txtai](/concepts/txtai.md) via the `mlflow.[txtai](/concepts/txtai.md).autolog()` function. Once enabled, [MLflow](/concepts/mlflow.md) captures [Traces](/concepts/traces.md) for LLM invocation, embeddings, AI Search, and logs them to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-txtai-databricks-on-aws.md]

## Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with [txtai](/concepts/txtai.md), you need to install [MLflow](/concepts/mlflow.md), the `txtai` library, and the `mlflow-txtai` extension. For development environments, install the full [MLflow](/concepts/mlflow.md) package with Databricks extras:

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" [[txtai|txtai]] mlflow-txtai
```

[MLflow 3](/concepts/mlflow-3.md) is highly recommended for the best tracing experience with [txtai](/concepts/txtai.md). ^[tracing-txtai-databricks-on-aws.md]

### Environment Configuration

**For users outside Databricks notebooks**: Set Databricks environment variables:

```bash
export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
export DATABRICKS_TOKEN="your-personal-access-token"
```

**For users inside Databricks notebooks**: These credentials are automatically set.

**API Keys**: Ensure your LLM provider API keys are set:

```bash
export OPENAI_API_KEY="your-openai-api-key"
```

^[tracing-txtai-databricks-on-aws.md]

## Enabling Tracing

On serverless compute clusters, [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks is not automatically enabled. You must explicitly call `mlflow.[txtai](/concepts/txtai.md).autolog()` to enable tracing for [txtai](/concepts/txtai.md) pipelines. ^[tracing-txtai-databricks-on-aws.md]

### Basic Example: Textractor Pipeline

The following example [Traces](/concepts/traces.md) a [Textractor pipeline](https://neuml.github.io/[txtai](/concepts/txtai.md)/pipeline/data/textractor/):

```python
import [[mlflow|MLflow]]
from [[txtai|txtai]].pipeline import Textractor

# Enable [[mlflow|MLflow]] auto-tracing for [[txtai|txtai]]
[[mlflow|MLflow]].[[txtai|txtai]].autolog()

# Set up [[mlflow-tracking|MLflow Tracking]] to Databricks
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/txtai-demo")

# Define and run a simple Textractor pipeline
textractor = Textractor()
textractor("https://github.com/neuml/[[txtai|txtai]]")
```

^[tracing-txtai-databricks-on-aws.md]

### Example: RAG Pipeline

The following example [Traces](/concepts/traces.md) a [RAG pipeline](https://neuml.github.io/[txtai](/concepts/txtai.md)/pipeline/text/rag/):

```python
import [[mlflow|MLflow]]
from [[txtai|txtai]] import Embeddings, RAG

# Enable [[mlflow|MLflow]] auto-tracing for [[txtai|txtai]]
[[mlflow|MLflow]].[[txtai|txtai]].autolog()

# Set up [[mlflow-tracking|MLflow Tracking]] to Databricks
# [[mlflow|MLflow]].set_tracking_uri("databricks")
# [[mlflow|MLflow]].set_experiment("/Shared/txtai-rag-demo")

wiki = Embeddings()
wiki.load(provider="huggingface-hub", container="neuml/txtai-wikipedia-slim")

template = """Answer the following question using only the context below. Only include information
specifically discussed.
question: {question}
context: {context} """

rag = RAG(
    wiki,
    "hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4",
    system="You are a friendly assistant. You answer questions from users.",
    template=template,
    context=10,
)
rag("Tell me about the Roman Empire", maxlength=2048)
```

^[tracing-txtai-databricks-on-aws.md]

### Example: Agent Pipeline

The following example [Traces](/concepts/traces.md) a [txtai Agent](/concepts/txtai-agent.md)](https://neuml.github.io/[txtai](/concepts/txtai.md)/agent/) designed to research astronomy questions:

```python
import [[mlflow|MLflow]]
from [[txtai|txtai]] import Agent, Embeddings

# Enable [[mlflow|MLflow]] auto-tracing for [[txtai|txtai]]
[[mlflow|MLflow]].[[txtai|txtai]].autolog()

def search(query):
    """Searches a database of astronomy data."""
    return embeddings.search(
        "SELECT id, text, distance FROM [[txtai|txtai]] WHERE similar(:query)", 
        10, 
        parameters={"query": query},
    )

embeddings = Embeddings()
embeddings.load(provider="huggingface-hub", container="neuml/txtai-astronomy")

agent = Agent(
    tools=[search],
    llm="hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4",
    max_iterations=10,
)

researcher = """{command}
Do the following:
- Search for results related to the topic.
- Analyze the results
- Continue querying until conclusive answers are found
- Write a Markdown report"""

agent(
    researcher.format(
        command="Write a detailed list with explanations of 10 candidate stars that could potentially be habitable to life."
    ),
    maxlength=16000,
)
```

^[tracing-trace-txtai-databricks-on-aws.md]

## Traced Components

[MLflow Tracing](/concepts/mlflow-tracing.md) for [txtai](/concepts/txtai.md) automatically captures [Traces](/concepts/traces.md) for the following components:

- **LLM invocation** — Model inference calls made by [txtai](/concepts/txtai.md) workflows
- **Embeddings** — Vector embedding operations for semantic search
- **AI Search** — Similarity search queries against the embeddings database
- **Agent interactions** — Tool calls and iterations within [txtai](/concepts/txtai.md) agents

^[tracing-txtai-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The general tracing framework that captures [Traces](/concepts/traces.md) for genAI applications
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — A pattern combining retrieval with LLM generation
- LLM Orchestration — Managing multi-step workflows involving language models
- Semantic Search — Search based on meaning rather than keyword matching
- Agent Workflows — Autonomous systems that use tools and iterate toward a goal

## Sources

- tracing-txtai-databricks-on-aws.md

# Citations

1. [tracing-txtai-databricks-on-aws.md](/references/tracing-txtai-databricks-on-aws-a07dafba.md)
2. tracing-trace-txtai-databricks-on-aws.md
