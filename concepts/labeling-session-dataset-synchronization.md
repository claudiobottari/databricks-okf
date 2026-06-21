---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 67b9b3ea0e364f2b2bbd4be8b266dee86e26d1db0e0310863e0d72577dd1770f
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-session-dataset-synchronization
    - LSDS
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Labeling Session Dataset Synchronization
description: The mechanism to sync Expectation data from labeling sessions to Evaluation Datasets via an intelligent upsert operation, using trace inputs as unique keys.
tags:
  - mlflow
  - datasets
  - synchronization
  - evaluation
timestamp: "2026-06-19T17:59:20.563Z"
---

```yaml
---
title: Labeling Session Dataset Synchronization
summary: An upsert operation (sync method) that pushes Expectations collected in a labeling session to an Evaluation Dataset, using trace inputs as unique keys to merge new and updated ground-truth records.
sources:
  - create-and-manage-labeling-sessions-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:19:01.050Z"
updatedAt: "2026-06-18T11:19:01.050Z"
tags:
  - mlflow
  - evaluation
  - datasets
  - sync
aliases:
  - labeling-session-dataset-synchronization
  - LSDS
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 1
---

# Labeling Session Dataset Synchronization

**Labeling Session Dataset Synchronization** is the process of transferring human-generated assessments — specifically `Expectations` — from a [[labeling session]] to an [[evaluation dataset]] using the `sync()` method of the MLflow `LabelingSession` API. This capability enables teams to iteratively build and refine test datasets by incorporating expert labels collected during review. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## How Synchronization Works

The `sync()` method performs an intelligent upsert operation using trace inputs as unique keys. The behavior follows these rules: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

1. **Matching by trace inputs** – Each trace’s input values act as the unique identifier when comparing against records in the evaluation dataset.
2. **Overwriting matching expectations** – If a trace in the labeling session has inputs that match an existing dataset record and the expectation names are identical, the expectations from the labeling session replace the existing expectations in the dataset.
3. **Adding new records** – Traces whose inputs do **not** match any existing dataset record are appended as new entries.
4. **Preserving unchanged records** – Dataset records whose inputs do not correspond to any trace in the labeling session remain unmodified.

This approach allows iterative improvement: new examples can be added and ground truth for existing examples can be updated without rebuilding the entire evaluation dataset. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Usage

The `sync()` method is available on a `LabelingSession` object. It requires the name of an existing evaluation dataset. The method is documented in the MLflow API reference as [`mlflow.genai.LabelingSession.sync`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.LabelingSession.sync). ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Example

```python
import mlflow.genai.labeling as labeling

# Find a labeling session that has completed labels
all_sessions = labeling.get_labeling_sessions()
session = None
for s in all_sessions:
    if s.name == "completed_review_session":
        session = s
        break

if session:
    # Sync expectations to an existing evaluation dataset
    session.sync(to_dataset="customer_service_eval_dataset")
    print("Synced expectations to evaluation dataset")
else:
    print("Session not found")
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Best Practices

Use the `Expectations` schema type (such as `EXPECTED_FACTS` or `EXPECTED_RESPONSE`) to collect ground‑truth data that can be synced. Structure trace inputs consistently across sessions, because inputs serve as the unique key for upsert matching. Call `sync()` after each round of labeling to keep the evaluation dataset current. After syncing, consider snapshotting the dataset or recording its version alongside the labeling session’s run ID to maintain reproducibility.

## Related Concepts

- [Labeling Session](/concepts/labeling-session.md) – The container for traces and collected assessments.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – The target dataset that receives synchronized Expectations.
- [Labeling Schema](/concepts/labeling-schema.md) – Defines the structure of Expectations and Feedback collected in a session.
- Expectations – Ground‑truth assessments that can be synced to evaluation datasets.
- [[MLflow Trace|MLflow Traces]] – The individual invocations that are reviewed and labeled.
- MLflow API – Programmatic interface for creating sessions, adding traces, and syncing data.

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
