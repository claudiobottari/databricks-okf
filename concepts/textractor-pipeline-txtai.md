---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6215e0634c52989976fc3094e37061eaaa91c7cbff69e4411797252660bbb512
  pageDirectory: concepts
  sources:
    - tracing-txtai-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - textractor-pipeline-txtai
    - TP(
    - Textractor pipeline
  citations:
    - file: tracing-txtai-databricks-on-aws.md
title: Textractor Pipeline (txtai)
description: A txtai pipeline component for extracting text from documents and data sources, traceable via MLflow autolog
tags:
  - txtai
  - pipeline
  - text-extraction
timestamp: "2026-06-19T23:13:32.269Z"
---

# Textractor Pipeline ([txtai](/concepts/txtai.md))

The **Textractor Pipeline** is a component of the [txtai](/concepts/txtai.md)](https://github.com/neuml/[txtai](/concepts/txtai.md)) library, an all-in-one embeddings database for semantic search, LLM orchestration, and language model workflows. The Textractor pipeline is specifically designed for extracting text from documents, such as scraping content from a URL. ^[tracing-txtai-databricks-on-aws.md]

## [MLflow Tracing](/concepts/mlflow-tracing.md) Integration

[MLflow Tracing](/concepts/mlflow-tracing.md) provides [Automatic Tracing](/concepts/automatic-tracing.md) capability for [txtai](/concepts/txtai.md) pipelines, including the Textractor pipeline. When auto-tracing is enabled via `mlflow.[txtai](/concepts/txtai.md).autolog()`, [MLflow](/concepts/mlflow.md) captures [Traces](/concepts/traces.md) for LLM invocations, embeddings, AI Search, and logs them to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-txtai-databricks-on-aws.md]

### Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with the Textractor pipeline, install [MLflow](/concepts/mlflow.md), the `txtai` library, and the `mlflow-txtai` extension. For development environments, install the full [MLflow](/concepts/mlflow.md) package with Databricks extras:

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" [[txtai|txtai]] mlflow-txtai
```

^[tracing-txtai-databricks-on-aws.md]

[MLflow 3](/concepts/mlflow-3.md) is highly recommended for the best tracing experience with [txtai](/concepts/txtai.md). When running outside Databricks notebooks, set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables. Inside Databricks notebooks, these credentials are automatically set. Additionally, ensure your LLM provider API keys are set if the Textractor pipeline internally uses an LLM. ^[tracing-txtai-databricks-on-aws.md]

> **Note for serverless compute clusters**: [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks is not automatically enabled. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function. ^[tracing-txtai-databricks-on-aws.md]

### Basic Example

The following example enables [MLflow](/concepts/mlflow.md) auto-tracing for [txtai](/concepts/txtai.md), sets up an [MLflow Experiment](/concepts/mlflow-experiment.md), and runs a simple Textractor pipeline on a GitHub repository URL:

```python
import [[mlflow|MLflow]]
from [[txtai|txtai]].pipeline import Textractor

# Enable [[mlflow|MLflow]] auto-tracing for [[txtai|txtai]]
[[mlflow|MLflow]].[[txtai|txtai]].autolog()

# Set up [[mlflow-tracking|MLflow Tracking]] to Databricks
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/txtai-demo")

# Define and run a simple Textractor pipeline.
textractor = Textractor()
textractor("https://github.com/neuml/[[txtai|txtai]]")
```

^[tracing-txtai-databricks-on-aws.md]

After execution, [Traces](/concepts/traces.md) for the Textractor pipeline invocation are captured and can be viewed in the [MLflow Experiment](/concepts/mlflow-experiment.md) UI.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Framework for capturing [Traces](/concepts/traces.md) of GenAI workflows.
- [txtai](/concepts/txtai.md) – Embeddings database and LLM orchestration library.
- [RAG Pipeline (txtai)](/concepts/rag-pipeline-txtai.md) – Another [txtai](/concepts/txtai.md) pipeline for retrieval-augmented generation.
- Agent (txtai) – A [txtai](/concepts/txtai.md) component for autonomous research tasks.
- [Autolog](/concepts/mlflow-autologging.md) – Mechanism for automatic [MLflow Tracking](/concepts/mlflow-tracking.md).

## Sources

- tracing-txtai-databricks-on-aws.md

# Citations

1. [tracing-txtai-databricks-on-aws.md](/references/tracing-txtai-databricks-on-aws-a07dafba.md)
