---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3419ac9d2820f81ed63f26473339a759b5b7d2d7f39f9b66e772c8e1f5b04f39
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-dataset-sync
    - EDS
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Evaluation Dataset Sync
description: A process that synchronizes Expectations collected in a labeling session to an Evaluation Dataset using an intelligent upsert operation keyed on trace inputs.
tags:
  - mlflow
  - evaluation
  - datasets
  - sync
timestamp: "2026-06-18T14:51:50.690Z"
---

# Evaluation Dataset Sync

**Evaluation Dataset Sync** is the process of transferring human-generated expectations from [Labeling Sessions](/concepts/labeling-sessions.md) to [Evaluation Datasets](/concepts/evaluation-datasets.md) in [MLflow GenAI](/concepts/mlflow-3-for-genai.md). This synchronization enables teams to iteratively improve their test datasets by incorporating expert annotations obtained during review workflows. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## How It Works

The sync is performed by calling the `sync()` method on a labeling session object. The operation is an intelligent upsert: it uses each trace’s inputs as a unique key to identify records in the target evaluation dataset. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

When expectations from the labeling session are synced:

- For traces whose inputs match an existing record in the dataset, expectations with the same name **overwrite** the existing expectations in that record. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- Traces from the labeling session that do **not** match any existing trace inputs are **added as new records** to the dataset. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- Existing dataset records with different inputs remain unchanged. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

This design allows teams to incrementally grow and refine evaluation datasets without manually reconstructing entries.

## Benefits

- **Iterative improvement**: As domain experts label more traces, the evaluation dataset can be updated to reflect ground truth for new scenarios and correct existing expectations. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **No data duplication**: Because inputs act as keys, repeated syncs from the same or different sessions do not create duplicate records for the same trace. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Traceability**: The synced expectations retain the structure defined in the labeling schemas used during the labeling session. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Using the API

The `sync()` method is called on a `LabelingSession` object. It is available through the [`mlflow.genai.LabelingSession.sync`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.LabelingSession.sync) API. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
# Pseudocode – see source for full example
session.sync(to_dataset="customer_service_eval_dataset")
```

The `to_dataset` argument specifies the name of the target evaluation dataset. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Prerequisites

- The labeling session must contain traces that have been reviewed and labeled with the **Expectation** schema (as opposed to Feedback-only schemas). Only expectations are synced; feedback data is not transferred. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- The target evaluation dataset should already exist. If it does not, the sync operation may fail or create a new dataset depending on the implementation (the source material does not specify behavior for non-existent datasets; consult the API documentation). ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Best Practices

- **Use Expectation schemas** in labeling sessions when the goal is to build ground truth for evaluation. Feedback schemas are better suited for qualitative assessment that does not feed directly into datasets. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Sync regularly** after each round of labeling to keep evaluation datasets aligned with the latest expert judgments. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) — The containers that collect expert feedback on traces.
- [Labeling Schemas](/concepts/labeling-schemas.md) — Define the questions and format for feedback (built-in types include `EXPECTED_FACTS`, `EXPECTED_RESPONSE`, `GUIDELINES`).
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Structured test data used in `mlflow.genai.evaluate()`.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The overall evaluation workflow that consumes these datasets.
- Human Feedback Alignment — Broader practice of incorporating human annotations into evaluation.

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
