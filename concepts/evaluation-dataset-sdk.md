---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cfc32f46eab6d6c79687013ebabb030dca4f546f5b584883cec3efd8c6fa8883
  pageDirectory: concepts
  sources:
    - evaluation-dataset-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-dataset-sdk
    - EDS
    - Evaluation Dataset SDK Reference
  citations:
    - file: evaluation-dataset-reference-databricks-on-aws.md
title: Evaluation Dataset SDK
description: The programmatic Python API (mlflow.genai.datasets) for creating, retrieving, and deleting evaluation datasets, including the EvaluationDataset class.
tags:
  - mlflow
  - sdk
  - api-reference
  - python
timestamp: "2026-06-19T18:43:27.066Z"
---

--- title: Evaluation Dataset SDK summary: The programmatic API (mlflow.genai.datasets) for creating, retrieving, and deleting evaluation datasets, including the EvaluationDataset class. sources: - evaluation-dataset-reference-databricks-on-aws.md kind: concept createdAt: "2026-06-18T12:13:30.180Z" updatedAt: "2026-06-18T12:13:30.180Z" tags: - mlflow - sdk - api - python - evaluation aliases: - evaluation-dataset-sdk - EDS confidence: 1 provenanceState: extracted inferredParagraphs: 0 ---

# Evaluation Dataset SDK

The **Evaluation Dataset SDK** is the programmatic interface to the `mlflow.genai.datasets` module, providing methods to create, retrieve, delete, and manage structured test datasets used for evaluating GenAI applications. It works alongside the [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) framework and integrates with `mlflow.genai.evaluate()` to supply inputs, expectations, and lineage metadata for evaluation runs. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Dataset Schema

Evaluation datasets follow a defined schema that includes core evaluation fields and optional lineage fields. The SDK respects this schema when creating and interacting with datasets. ^[evaluation-dataset-reference-databricks-on-aws.md]

### Core Fields

- **`inputs`**: The primary input data passed to the GenAI app during evaluation.
- **`expectations`** (optional): Ground‑truth reference data for LLM judges. The `expectations` dictionary has reserved keys recognised by built‑in judges:
  - `guidelines` – Rules or constraints the response should follow.
  - `expected_facts` – Facts that should appear in the output.
  - `expected_response` – A canonical expected answer.

^[evaluation-dataset-reference-databricks-on-aws.md]

### Additional Fields

The dataset abstraction also supports lineage fields:

- **`source`**: Describes the origin of each record. Each record can have only one source type:
  - `human` – Record created manually by a person. Requires a `user_name`.
  - `document` – Record synthesised from a document. Includes a `doc_uri` and an optional `content` excerpt.
  - `trace` – Record derived from a production trace. Includes a `trace_id`.
- **Tags** (optional): Key‑value pairs attached to individual records for filtering or categorisation.

^[evaluation-dataset-reference-databricks-on-aws.md]

## SDK Methods and Classes

The SDK is available under `mlflow.genai.datasets`. Below are the most frequently used methods and the `EvaluationDataset` class. For the complete API reference, see the official [MLflow documentation](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#module-mlflow.genai.datasets). ^[evaluation-dataset-reference-databricks-on-aws.md]

### `create_dataset`

Creates a new evaluation dataset as a Delta table in Unity Catalog. You must specify a Unity Catalog schema (with `CREATE TABLE` permissions) and a table name.

```python
mlflow.genai.datasets.create_dataset(
    name="catalog.schema.table_name",
    description="Optional description"
)
```

^[evaluation-dataset-reference-databricks-on-aws.md]

### `get_dataset`

Retrieves an existing evaluation dataset by its full name. Returns an `EvaluationDataset` object that can be used to read records or load the dataset into an evaluation run.

```python
dataset = mlflow.genai.datasets.get_dataset("catalog.schema.table_name")
```

^[evaluation-dataset-reference-databricks-on-aws.md]

### `delete_dataset`

Deletes an evaluation dataset and all its records from Unity Catalog.

```python
mlflow.genai.datasets.delete_dataset("catalog.schema.table_name")
```

^[evaluation-dataset-reference-databricks-on-aws.md]

### `EvaluationDataset` Class

The `EvaluationDataset` class represents a loaded dataset and provides methods to:

- Read records and their fields (`inputs`, `expectations`, `source`, `tags`).
- Modify records (edit inputs or expectations, add or remove tags).
- Add or delete individual records.
- Save changes back to Unity Catalog.
- Load the dataset into an evaluation context (e.g., as the `data` argument to `mlflow.genai.evaluate()`).

```python
dataset = mlflow.genai.datasets.get_dataset("catalog.schema.table_name")
# Add a new record
dataset.add_record(
    inputs={"question": "What is MLflow?"},
    expectations={"guidelines": "Answer in one sentence."}
)
dataset.save()
```

^[evaluation-dataset-reference-databricks-on-aws.md]

## Typical Workflow

1. **Create a dataset** using `create_dataset` in a Unity Catalog schema.
2. **Populate records** – either manually via the SDK or by importing from production traces.
3. **Edit and curate** records using `EvaluationDataset` methods or the [MLflow Evaluation Dataset UI](/concepts/mlflow-evaluation-dataset-ui.md).
4. **Run evaluation** by passing the dataset to `mlflow.genai.evaluate()`.
5. **Iterate** – refine the dataset as needed and re‑evaluate.

The SDK and UI are complementary: the UI provides a visual editor for managing datasets, while the SDK supports automation and scripted workflows.

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The overall evaluation framework.
- [LLM Judges](/concepts/llm-judges.md) – Built‑in and custom scorers that use the dataset.
- [Evaluation Dataset UI](/concepts/evaluation-dataset-ui.md) – The visual interface for managing datasets.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer where datasets are stored.
- [GenAI App Development](/concepts/databricks-genai-notebook-development.md) – End‑to‑end workflow from dataset creation to production monitoring.

## Sources

- evaluation-dataset-reference-databricks-on-aws.md

# Citations

1. [evaluation-dataset-reference-databricks-on-aws.md](/references/evaluation-dataset-reference-databricks-on-aws-b8093309.md)
