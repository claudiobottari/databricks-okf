---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f7ac3d090884f63744f3a4b47380bbb144827ba25c2b3f2760ba2d3caa8def1
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - syncing-expectations-to-evaluation-datasets
    - SETED
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Syncing Expectations to Evaluation Datasets
description: A workflow that synchronizes collected Expectation labels from a labeling session to an Evaluation Dataset via an intelligent upsert, using trace inputs as unique keys.
tags:
  - mlflow
  - human-feedback
  - evaluation
  - datasets
timestamp: "2026-06-19T09:33:11.758Z"
---

# Syncing Expectations to Evaluation Datasets

**Syncing Expectations to Evaluation Datasets** is a feature of [Labeling Sessions](/concepts/labeling-sessions.md) in MLflow that allows you to transfer human-generated Expectations from a labeling session directly into an [Evaluation Dataset](/concepts/evaluation-dataset.md). This creates a feedback loop where expert labels become ground-truth test cases that can be reused for offline evaluation and automated judging.

## How dataset synchronization works

The synchronization is performed by the `sync()` method on a labeling session object. MLflow treats each trace’s input payload as a unique key to identify records in the target evaluation dataset. The sync performs an **intelligent upsert**:

- If a trace in the labeling session has the same input as an existing record in the dataset, the expectations from the labeling session **overwrite** the existing expectations **when the expectation names match**.  
- Traces whose inputs do not appear in any existing dataset record are **added as new records**.  
- Existing dataset records whose inputs do not correspond to any trace in the labeling session are **left unchanged**.

This design allows you to iteratively improve the evaluation dataset by adding new examples and updating ground truth for existing examples without duplicating records. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Using the sync method

To sync expectations from a completed labeling session to an evaluation dataset, call `session.sync(to_dataset="<dataset-name>")`. The method is available on the `LabelingSession` object obtained via `mlflow.genai.labeling.get_labeling_sessions()`.  

```python
import mlflow.genai.labeling as labeling

# Find the labeling session that has finished review
all_sessions = labeling.get_labeling_sessions()
session = None
for s in all_sessions:
    if s.name == "completed_review_session":
        session = s
        break

if session:
    # Sync expectations to the evaluation dataset
    session.sync(to_dataset="customer_service_eval_dataset")
    print("Synced expectations to evaluation dataset")
```

After the sync, the evaluation dataset contains the latest expert-labeled expectations, ready for use in later evaluation runs. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Prerequisites and notes

- Only **Expectations** (not general Feedback) are synced to evaluation datasets. Labeling sessions can collect either `Feedback` or `Expectation` data. For the sync to be meaningful, the labeling schema should capture expectations (e.g., `EXPECTED_FACTS`, `EXPECTED_RESPONSE`, `GUIDELINES` or custom schemas with type `expectation`).  
- The trace inputs must be consistent across the labeling session and the target dataset, because the sync uses them as the matching key.  
- The evaluation dataset must already exist before calling `sync()`.  

## Related concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) – The container for collecting expert labels.
- Expectations – Ground-truth annotations that can be synced to datasets.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – Reusable collections of test cases used for offline evaluation.
- [Custom Labeling Schemas](/concepts/custom-labeling-schema-creation.md) – Define what kind of expectation data is collected.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The evaluation workflow that consumes these datasets.

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
