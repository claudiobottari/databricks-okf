---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d2a83ad261db279bd08b7fd4f43fd99f0c5db9830b1b6309f12896f1ce09ee3
  pageDirectory: concepts
  sources:
    - evaluation-dataset-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-datasets-sdk
    - MGDS
    - MLflow GenAI Datasets
  citations:
    - file: evaluation-dataset-reference-databricks-on-aws.md
title: MLflow GenAI Datasets SDK
description: Programmatic API (mlflow.genai.datasets) for creating, retrieving, deleting, and interacting with evaluation datasets via Python.
tags:
  - mlflow
  - sdk
  - api
  - python
timestamp: "2026-06-19T10:25:12.954Z"
---

# MLflow GenAI Datasets SDK

The **MLflow GenAI Datasets SDK** provides a programmatic Python interface for creating, managing, and using structured evaluation datasets within the [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluation framework. The SDK enables developers to define test data with `inputs`, optional ground-truth `expectations`, and lineage fields such as source and tags, then use them with `mlflow.genai.evaluate()` to assess GenAI application quality. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Key Classes and Methods

The SDK is available through the `mlflow.genai.datasets` module. The most frequently used methods and classes include: ^[evaluation-dataset-reference-databricks-on-aws.md]

- **`mlflow.genai.datasets.create_dataset`** – Creates a new evaluation dataset backed by a [Unity Catalog](/concepts/unity-catalog.md) table.
- **`mlflow.genai.datasets.get_dataset`** – Retrieves an existing evaluation dataset by its identifier.
- **`mlflow.genai.datasets.delete_dataset`** – Deletes an evaluation dataset.
- **`EvaluationDataset`** – The core class that provides methods to interact with and modify evaluation datasets programmatically.

For the complete API reference, see the official [MLflow Python API reference for `mlflow.genai.datasets`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#module-mlflow.genai.datasets). ^[evaluation-dataset-reference-databricks-on-aws.md]

## Dataset Schema

Evaluation datasets created with the SDK must follow a defined schema with both core fields and optional lineage fields. ^[evaluation-dataset-reference-databricks-on-aws.md]

### Core Fields

- **`inputs`** – The primary input data for the GenAI application under evaluation.
- **`expectations`** – Optional ground-truth data used by built-in LLM judges. This field has several reserved keys: `guidelines`, `expected_facts`, and `expected_response`. ^[evaluation-dataset-reference-databricks-on-aws.md]

### Additional Fields

The SDK also supports lineage tracking fields for dataset records: ^[evaluation-dataset-reference-databricks-on-aws.md]

- **`source`** – Tracks where a dataset record originated. Each record can have only one source type. Supported source types include:
  - **Human source** – Records created manually by a person, identified by username.
  - **Document source** – Records synthesized from a document, with a document URI and optional content excerpt.
  - **Trace source** – Records created from a production trace, identified by a trace ID.

## Record-Level Tags

The SDK supports adding tags to individual dataset records, enabling flexible metadata and categorization for evaluation data. Tags can be managed programmatically or through the [MLflow Evaluation Dataset UI](/concepts/mlflow-evaluation-dataset-ui.md). ^[evaluation-dataset-reference-databricks-on-aws.md]

## Usage with Evaluation

Evaluation datasets created with the SDK are designed to be used with `mlflow.genai.evaluate()`, which loads the dataset and runs evaluation with a specified set of scorers. The SDK also provides a ready-to-use Python code snippet from the dataset UI that loads the dataset and configures evaluation with default scorers. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Related Concepts

- [Evaluation Dataset Schema](/concepts/evaluation-dataset-schema.md) – The full schema specification for dataset fields and reserved keys.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The evaluation harness that consumes datasets from the SDK.
- [MLflow Evaluation Dataset UI](/concepts/mlflow-evaluation-dataset-ui.md) – The visual interface for managing datasets without writing code.
- MLflow GenAI Datasets – General concepts and examples for using evaluation datasets.

## Sources

- evaluation-dataset-reference-databricks-on-aws.md

# Citations

1. [evaluation-dataset-reference-databricks-on-aws.md](/references/evaluation-dataset-reference-databricks-on-aws-b8093309.md)
