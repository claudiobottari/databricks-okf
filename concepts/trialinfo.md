---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f31de2178344037c296a5bbeb5f5d8e90ae2f91c2a1a94e2ab11251d3f054a4
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trialinfo
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: TrialInfo
description: Summary object for each individual trial in an AutoML run, with a method to load the model generated for that trial.
tags:
  - machine-learning
  - automl
  - api
  - databricks
timestamp: "2026-06-19T22:12:13.285Z"
---

# TrialInfo

**TrialInfo** is a summary object for each individual trial in a Databricks AutoML run. It provides metadata about the trial, such as the URI to its MLflow artifacts, and a method to load the model generated during that trial. ^[automl-python-api-reference-databricks-on-aws.md]

## Overview

When an AutoML run completes, it returns an [AutoMLSummary](/concepts/automlsummary.md) object. The `trials` attribute of `AutoMLSummary` is a list of `TrialInfo` objects, one per trial. `AutoMLSummary` describes the metrics, parameters, and other details for each trial. ^[automl-python-api-reference-databricks-on-aws.md]

## Attributes

The source material demonstrates one attribute of `TrialInfo`:

- **`artifact_uri`** – A URI pointing to the trial’s MLflow artifacts, such as the generated notebook. This URI can be passed to `databricks.automl.import_notebook()` to import the trial notebook into a workspace directory. ^[automl-python-api-reference-databricks-on-aws.md]

## Methods

- **Load model** – `TrialInfo` provides a method to load the model trained during that trial. This allows you to programmatically retrieve and use the model. ^[automl-python-api-reference-databricks-on-aws.md]

## Usage Example

The following example uses `artifact_uri` to import a trial notebook:

```python
summary = databricks.automl.classify(...)
result = databricks.automl.import_notebook(
    summary.trials[5].artifact_uri,
    "/Users/you@yourcompany.com/path/to/directory"
)
```

^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- [AutoMLSummary](/concepts/automlsummary.md) — The parent summary object for an entire AutoML run.
- [ImportNotebookResult](/concepts/importnotebookresult.md) — The result object returned by `import_notebook()`.
- [Databricks AutoML](/concepts/databricks-automl.md) — The automated machine learning service.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The experiment tracking system used to log trial results.

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
