---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 054d51bedb13fd206a01908616f09189bbf9f74076b6e4784b4c61c266aeb641
  pageDirectory: concepts
  sources:
    - tracing-txtai-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-txtai-extension
  citations:
    - file: tracing-txtai-databricks-on-aws.md
title: mlflow-txtai extension
description: A Python package (mlflow-txtai) that provides the integration bridge between MLflow tracing and txtai workflows
tags:
  - mlflow
  - txtai
  - integration
  - package
timestamp: "2026-06-19T23:13:37.350Z"
---

## mlflow-txtai extension

The **mlflow-txtai extension** is a Python package that enables [MLflow Tracing](/concepts/mlflow-tracing.md) for the [txtai](/concepts/txtai.md) library, an all-in-one embeddings database for semantic search, LLM orchestration, and language model workflows. When installed and activated, the extension automatically captures [Traces](/concepts/traces.md) for [txtai](/concepts/txtai.md) components such as LLM invocations, embeddings, AI Search operations, and agent actions, and logs them to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-txtai-databricks-on-aws.md]

### Prerequisites

To use the mlflow-txtai extension, you need `mlflow`, `txtai`, and the `mlflow-txtai` package itself. For development environments, the recommended installation includes the full [MLflow](/concepts/mlflow.md) package with Databricks extras: ^[tracing-txtai-databricks-on-aws.md]

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" [[txtai|txtai]] mlflow-txtai
```

[MLflow 3](/concepts/mlflow-3.md) is recommended for the best tracing experience. Environment configuration requires setting `DATABRICKS_HOST` and `DATABRICKS_TOKEN` (for users outside Databricks notebooks) and any LLM provider API keys (e.g., `OPENAI_API_KEY`) that your [txtai](/concepts/txtai.md) pipeline uses. Inside Databricks notebooks, credentials are automatically set. ^[tracing-txtai-databricks-on-aws.md]

### Enabling Tracing

Tracing for [txtai](/concepts/txtai.md) is enabled by calling `mlflow.[txtai](/concepts/txtai.md).autolog()`. This function sets auto‑tracing for all supported [txtai](/concepts/txtai.md) components. On serverless compute clusters, [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks is **not** automatically enabled — you must explicitly call the appropriate `mlflow.<library>.autolog()` function. ^[tracing-txtai-databricks-on-aws.md]

### Supported Workflows and Examples

The mlflow-txtai extension supports tracing for the following [txtai](/concepts/txtai.md) workflows:

- **Textractor pipeline**: A simple data extraction pipeline. Tracing captures the extraction steps. ^[tracing-txtai-databricks-on-aws.md]
- **Retrieval Augmented Generation (RAG) pipeline**: Combines an embeddings database (e.g., `Embeddings.load()` from Hugging Face Hub) with a language model (e.g., `hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4`) and a custom prompt template. Tracing records the retrieval and generation steps. ^[tracing-txtai-databricks-on-aws.md]
- **Agent**: A [txtai Agent](/concepts/txtai-agent.md) that can use tools (such as a search tool over an astronomy embeddings database) and iteratively research a topic. Tracing captures each tool call, iteration, and the final output. ^[tracing-txtai-databricks-on-aws.md]

Example code for each of these workflows is provided in the official Databricks documentation. In each case, the pattern is:

1. Call `mlflow.[txtai](/concepts/txtai.md).autolog()`.
2. (Optionally) set the tracking URI and experiment.
3. Create and run the [txtai](/concepts/txtai.md) pipeline/agent.

### More Information

For additional examples and usage guidance, refer to the [mlflow-txtai extension repository](https://github.com/neuml/mlflow-txtai/tree/master). ^[tracing-txtai-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [txtai](/concepts/txtai.md)
- Semantic Search
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)
- LLM Orchestration
- [MLflow Experiment](/concepts/mlflow-experiment.md)
- [Autologging](/concepts/mlflow-autologging.md)
- Serverless Compute

### Sources

- tracing-txtai-databricks-on-aws.md

# Citations

1. [tracing-txtai-databricks-on-aws.md](/references/tracing-txtai-databricks-on-aws-a07dafba.md)
