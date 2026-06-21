---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a35087247764adadee55aeef6b68388c3f30158c04e48ea25e4f30ea2391e3d6
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-trial-notebooks
    - ATN
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: AutoML Trial Notebooks
description: Generated notebooks per model trial during an AutoML run, importable via import_notebook from MLflow artifact URIs
tags:
  - automl
  - notebooks
  - mlflow
timestamp: "2026-06-19T09:07:56.717Z"
---

```yaml
---
title: AutoML trial notebooks
summary: Each AutoML run call trains a set of models and generates a trial notebook for each model.
sources:
  - automl-python-api-reference-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:31:24.477Z"
updatedAt: "2026-06-18T14:31:24.477Z"
tags:
  - AutoML
  - notebook
  - Databricks
aliases:
  - automl-trial-notebooks
  - ATN
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# AutoML Trial Notebooks

**AutoML trial notebooks** are generated notebooks that Databricks AutoML creates for each model trained during an automatic machine learning run. When you call `databricks.automl.classify`, `databricks.automl.regress`, or `databricks.automl.forecast`, AutoML trains a set of candidate models and, for each model, produces a trial notebook that documents the data preparation, feature engineering, algorithm selection, and hyperparameter tuning steps that were performed. ^[automl-python-api-reference-databricks-on-aws.md]

## Overview

Trial notebooks serve as a reproducible record of each model’s training process. They are stored as MLflow artifacts, which means they can be inspected, modified, and re‑run to reproduce the model or to extend the analysis. The AutoML Python API returns an `AutoMLSummary` object that contains a list of `TrialInfo` objects, one per trial. Each `TrialInfo` exposes the `artifact_uri` that points to the trial notebook saved as an MLflow artifact. ^[automl-python-api-reference-databricks-on-aws.md]

## Accessing Trial Notebooks

After an AutoML run completes, the `AutoMLSummary` object provides access to each trial through its `trials` attribute. Each element in that list is a `TrialInfo` object with properties such as:

- `artifact_uri` – the MLflow artifact URI for the trial notebook.
- `model` – a method to load the trained model from that trial.
- Additional metrics, parameters, and details about the trial.

You can retrieve the artifact URI of a specific trial and use it to import the notebook into your workspace. ^[automl-python-api-reference-databricks-on-aws.md]

## Importing Trial Notebooks

The `databricks.automl.import_notebook` method lets you take a trial notebook that has been saved as an MLflow artifact and import it into a workspace directory. This gives you a fully editable notebook that you can customize and run.

```python
databricks.automl.import_notebook(
    artifact_uri: str,
    path: str,
    overwrite: bool = False
) -> ImportNotebookResult
```

**Parameters:**

- `artifact_uri` – the URI of the trial notebook artifact (obtained from `TrialInfo.artifact_uri`).
- `path` – the workspace destination path for the imported notebook.
- `overwrite` – if `True`, overwrites any existing notebook at the target path.

The method returns an `ImportNotebookResult` object containing `path` and `url` of the imported notebook. ^[automl-python-api-reference-databricks-on-aws.md]

### Example

```python
summary = databricks.automl.classify(...)
result = databricks.automl.import_notebook(
    summary.trials[5].artifact_uri,
    "/Users/you@yourcompany.com/path/to/directory"
)
print(result.path)
print(result.url)
```

^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- AutoML – The broader automated machine learning service on Databricks.
- MLflow Artifacts – The storage mechanism that holds trial notebooks.
- [[AutoMLSummary]] – The object returned by AutoML methods that enumerates all trials.
- [[TrialInfo]] – Per‑trial summary containing metrics and artifact location.

## Sources

- automl-python-api-reference-databricks-on-aws.md
```

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
