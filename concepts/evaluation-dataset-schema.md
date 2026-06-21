---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2777f6af2e65606fe525bcb7aa7c4c7752e3aa10a54e103ca894aa00f287087
  pageDirectory: concepts
  sources:
    - evaluation-dataset-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-dataset-schema
    - EDS
    - Evaluation data schema
  citations:
    - file: evaluation-dataset-reference-databricks-on-aws.md
title: Evaluation Dataset Schema
description: The structured schema for MLflow evaluation datasets, defining core fields like inputs, expectations, and lineage metadata for GenAI app evaluation.
tags:
  - mlflow
  - evaluation
  - dataset-schema
timestamp: "2026-06-19T18:42:52.539Z"
---

# Evaluation Dataset Schema

The **Evaluation Dataset Schema** defines the required structure for test data used to evaluate GenAI applications with [MLflow GenAI](/concepts/mlflow-3-for-genai.md). It specifies the format for `inputs`, ground-truth `expectations`, and lineage fields such as source and tags. This schema applies both when passing data directly to evaluation functions and when using the evaluation dataset abstraction. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Core Fields

All evaluation datasets must include the following core fields, whether passing data directly or using the dataset abstraction. ^[evaluation-dataset-reference-databricks-on-aws.md]

| Field | Type | Description |
|-------|------|-------------|
| `inputs` | JSON object or array | The input data to be evaluated by the GenAI app. |
| `expectations` | JSON object (optional) | Ground-truth answers or expected behaviors used by judges. |

### `expectations` Reserved Keys

The `expectations` field has several reserved keys that are used by built-in LLM judges: `guidelines`, `expected_facts`, and `expected_response`. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Additional Fields

The evaluation dataset abstraction supports additional fields for tracking lineage and version history. ^[evaluation-dataset-reference-databricks-on-aws.md]

### Source Field

The `source` field tracks where a dataset record originated. Each record can have **only one** source type. ^[evaluation-dataset-reference-databricks-on-aws.md]

**Human source** — Record created manually by a person:

```json
{
    "source": {
        "human": {
            "user_name": "jane.doe@company.com"
        }
    }
}
```

**Document source** — Record synthesized from a document:

```json
{
    "source": {
        "document": {
            "doc_uri": "s3://bucket/docs/product-manual.pdf",
            "content": "The first 500 chars of the document..."
        }
    }
}
```

**Trace source** — Record created from a production trace:

```json
{
    "source": {
        "trace": {
            "trace_id": "tr-abc123def456"
        }
    }
}
```

### Tags

Tags can be added to individual records for organization and filtering. The [MLflow Evaluation Dataset UI](/concepts/evaluation-dataset-ui.md) allows adding and editing tags directly. ^[evaluation-dataset-reference-databricks-on-aws.md]

## MLflow Evaluation Dataset UI

The **Datasets** tab in the MLflow experiment page provides a split-pane interface for managing evaluation datasets. The left pane lists all datasets associated with the experiment, while the right pane shows the records for the selected dataset. From the UI, you can search, sort, create, edit, and delete datasets and records without writing code. ^[evaluation-dataset-reference-databricks-on-aws.md]

### Creating a Dataset

Click **Create dataset**, select a [Unity Catalog](/concepts/unity-catalog.md) schema where you have `CREATE TABLE` permissions, enter a table name, and click **Create Dataset**. ^[evaluation-dataset-reference-databricks-on-aws.md]

### Editing Records

Inputs and expectations can be edited inline in the table. These fields accept JSON and validate input as you type. To add a new row, click **Add record**. To save all pending edits, click **Save changes**. ^[evaluation-dataset-reference-databricks-on-aws.md]

### Running an Evaluation

Click **Run an evaluation** to open a dialog with a Python code template that loads the dataset and runs `mlflow.genai.evaluate()` with a default set of scorers. The snippet can be copied to your clipboard for use in notebooks or scripts. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Key SDK Methods

The evaluation datasets SDK provides programmatic access to create, manage, and use datasets. Frequently used methods and classes include: ^[evaluation-dataset-reference-databricks-on-aws.md]

- `mlflow.genai.datasets.create_dataset()`
- `mlflow.genai.datasets.get_dataset()`
- `mlflow.genai.datasets.delete_dataset()`
- `EvaluationDataset` — class providing methods to interact with and modify evaluation datasets

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The MLflow subsystem for GenAI evaluation and monitoring
- [LLM Judges](/concepts/llm-judges.md) — Built-in judges that use reserved `expectations` keys
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Evaluating multiple agent variants against the same dataset
- [Custom Judges](/concepts/custom-judges.md) — Creating judges that evaluate against defined `expectations`
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Monitoring deployed GenAI apps with evaluation datasets
- [Evaluation Dataset SDK Reference](/concepts/evaluation-dataset-sdk.md) — Programmatic API for dataset management

## Sources

- evaluation-dataset-reference-databricks-on-aws.md

# Citations

1. [evaluation-dataset-reference-databricks-on-aws.md](/references/evaluation-dataset-reference-databricks-on-aws-b8093309.md)
