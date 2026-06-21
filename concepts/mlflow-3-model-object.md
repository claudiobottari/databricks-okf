---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 83d1232b545db116dfeca86c154ba36d5b80482248c593c051a370802f1cb9a2
  pageDirectory: concepts
  sources:
    - view-training-results-with-mlflow-runs-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-model-object
    - M3MO
  citations:
    - file: view-training-results-with-mlflow-runs-databricks-on-aws.md
title: MLflow 3 Model Object
description: In MLflow 3, models are first-class objects distinct from run artifacts, with code snippets for loading and using them for predictions on Spark and Pandas DataFrames.
tags:
  - mlflow
  - models
  - mlflow-3
timestamp: "2026-06-19T23:25:47.787Z"
---

---
title: [MLflow 3](/concepts/mlflow-3.md) Model Object
summary: In [MLflow 3](/concepts/mlflow-3.md), models are promoted to first-class objects, separate from run artifacts, enabling independent lifecycle management and simplified tracking.
sources:
  - view-training-results-with-mlflow-runs-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T08:00:00.000Z"
updatedAt: "2026-06-20T08:00:00.000Z"
tags:
  - [MLflow](/concepts/mlflow.md)
  - mlflow-3
  - model-management
aliases:
  - mlflow-3-model-object
  - first-class-model
confidence: 0.9
provenanceState: inferred
inferredParagraphs: 2
---

# [MLflow 3](/concepts/mlflow-3.md) Model Object

The **MLflow 3 Model Object** refers to the representation of a trained machine learning model as a distinct first-class entity within the [MLflow Tracking](/concepts/mlflow-tracking.md) and model registry system, introduced in [MLflow 3](/concepts/mlflow-3.md). Unlike earlier versions where a model was stored as an artifact attached to a training run, in [MLflow 3](/concepts/mlflow-3.md) the model itself is an independent object that can be created, registered, versioned, and managed separately from the run that produced it. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Overview

In previous [MLflow](/concepts/mlflow.md) versions, when you logged a model as part of a run, the model files appeared under the **Artifacts** tab of the run page, and the run was the primary container for the model. [MLflow 3](/concepts/mlflow-3.md) changes this paradigm: the model becomes a first-class object, meaning it has its own identity, metadata, and lifecycle. This shift simplifies workflows where models need to be promoted, deployed, or compared across multiple runs without being tightly coupled to a single training execution. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

The exact API and schema changes for the [MLflow 3](/concepts/mlflow-3.md) Model Object are described in the separate "Get started with [MLflow 3 for Models](/concepts/mlflow-3-for-models.md)" guide, but the conceptual change is that users can now interact with models directly rather than going through run artifacts.

## Implications

Treating models as first-class objects enables:

- Independent versioning and registration of models without requiring the originating run to be present.
- Clearer lineage tracking, as models can be linked to multiple runs (e.g., fine-tuning iterations) while retaining their own identity.
- Simplified deployment pipelines that reference a model object rather than a run ID and artifact path.

Because models are no longer just artifacts, the [MLflow Runs](/concepts/mlflow-run.md) page now shows model objects separately, and code snippets for loading and predicting reflect the new model‑centric API. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) – The open‑source platform for [ML Lifecycle](/concepts/ml-lifecycle.md) management.
- [MLflow 3](/concepts/mlflow-3.md) – The version of [MLflow](/concepts/mlflow.md) that introduced the first‑class model object.
- [MLflow Runs](/concepts/mlflow-run.md) – The execution record; models are now distinct from runs.
- MLflow Artifacts – Output files from a run; models are no longer stored solely as artifacts.
- [Model Registry](/concepts/mlflow-model-registry.md) – A centralized model store; the first‑class object aligns with registry concepts.

## Sources

- view-training-results-with-mlflow-runs-databricks-on-aws.md

# Citations

1. [view-training-results-with-mlflow-runs-databricks-on-aws.md](/references/view-training-results-with-mlflow-runs-databricks-on-aws-c299681f.md)
