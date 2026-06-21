---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 495daa792c5d28f4f6faf3bc2aa2525dd5f9d3853dbaa02e37166c20a08db05f
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dataset-synchronization
    - Data synchronization
    - data synchronization
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Dataset Synchronization
description: A mechanism to sync collected Expectations from labeling sessions to Evaluation Datasets via an intelligent upsert operation, using trace inputs as unique keys.
tags:
  - evaluation
  - dataset
  - labeling
  - sync
timestamp: "2026-06-19T14:33:46.070Z"
---

# Dataset Synchronization

**Dataset Synchronization** is a feature that synchronizes `Expectations` collected from [labeling sessions](/concepts/labeling-session.md) into an [Evaluation Dataset](/concepts/evaluation-dataset.md). It provides an intelligent upsert mechanism to iteratively improve evaluation datasets by adding new ground truth examples and updating existing ones based on human feedback.

## Overview

Human feedback collected during labeling sessions (for example, expert annotations on agent outputs) is stored as `Expectations` on the traces within the session. The `sync()` method on a `LabelingSession` object allows you to transfer these expectations to an evaluation dataset. This turns qualitative feedback into a structured test set that can be reused for offline evaluation.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## How Dataset Synchronization Works

The `sync()` method performs an intelligent upsert operation^[create-and-manage-labeling-sessions-databricks-on-aws.md]:

- Each trace's **inputs** serve as a unique key to identify records in the dataset.
- For traces with matching inputs, expectations from the labeling session **overwrite** existing expectations in the dataset when the expectation names are the same.
- Traces from the labeling session that do not match any existing trace inputs in the dataset are **added as new records**.
- Existing dataset records with different inputs remain **unchanged**.

This behavior supports an iterative workflow: you can run multiple labeling sessions, collect feedback on edge cases, and continuously refine your evaluation dataset without manual deduplication.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Usage

Call the `sync()` method on a labeling session object, specifying the target evaluation dataset name:

```python
import mlflow.genai.labeling as labeling

# Find session with completed labels by name
all_sessions = labeling.get_labeling_sessions()
session = None
for s in all_sessions:
    if s.name == "completed_review_session":
        session = s
        break

if session:
    # Sync expectations to dataset
    session.sync(to_dataset="customer_service_eval_dataset")
    print("Synced expectations to evaluation dataset")
else:
    print("Session not found")
```

After synchronization, the evaluation dataset contains updated expectations for existing records and new records for traces that were not previously included.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Best Practices

- **Use consistent expectation names** across labeling sessions so that the upsert logic correctly overwrites matching expectations.
- **Sync after each labeling session** to keep the evaluation dataset up to date as feedback accumulates.
- **Store the labeling session's [MLflow Run](/concepts/mlflow-run.md) ID** (`session.mlflow_run_id`) for reliable programmatic access, as session names may not be unique.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Session](/concepts/labeling-session.md) – The container that collects human feedback on traces.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – The structured dataset that feeds into offline evaluation pipelines.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The parent entity that groups labeling sessions and runs.
- [Expectation](/concepts/feedback-vs-expectation-labels.md) – The human-annotated ground truth stored on a trace and synced to datasets.

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
