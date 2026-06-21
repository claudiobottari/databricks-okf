---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1ace17b04520c165e6a1d864f51e8f0d9a95e7ac07ce49256d8d71dbe1945be1
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-import-notebook
    - AIN
    - automl-import_notebook
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: AutoML Import Notebook
description: Method to import a notebook saved as an MLflow artifact
tags:
  - automl
  - notebooks
  - mlflow
  - databricks
timestamp: "2026-06-18T10:51:38.081Z"
---

# AutoML Import Notebook

**AutoML Import Notebook** is a method in the Databricks AutoML Python API that imports a notebook saved as an MLflow artifact into a specified workspace path. This allows you to programmatically retrieve and reuse trial notebooks generated during an AutoML run.^[automl-python-api-reference-databricks-on-aws.md]

## API Reference

The `databricks.automl.import_notebook` method accepts three parameters and returns an `ImportNotebookResult` object.^[automl-python-api-reference-databricks-on-aws.md]

### Syntax

```python
databricks.automl.import_notebook(
  artifact_uri: str,
  path: str,
  overwrite: bool = False
) -> ImportNotebookResult
```

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `artifact_uri` | `str` | The MLflow artifact URI of the notebook to import. This is typically obtained from a trial's `artifact_uri` attribute in an [AutoMLSummary](/concepts/automlsummary.md) object. |
| `path` | `str` | The destination workspace path where the notebook should be imported (e.g., `/Users/you@yourcompany.com/path/to/directory`). |
| `overwrite` | `bool` | Whether to overwrite an existing notebook at the destination path. Defaults to `False`. |

^[automl-python-api-reference-databricks-on-aws.md]

### Return Value

The method returns an `ImportNotebookResult` object containing the following fields:

| Field | Type | Description |
|---|---|---|
| `path` | `str` | The workspace path where the notebook was imported. |
| `url` | `str` | The URL to access the imported notebook in the workspace. |

^[automl-python-api-reference-databricks-on-aws.md]

## Usage Example

The following example demonstrates how to import a trial notebook after running an AutoML classification experiment:^[automl-python-api-reference-databricks-on-aws.md]

```python
summary = databricks.automl.classify(...)
result = databricks.automl.import_notebook(
    summary.trials[5].artifact_uri,
    "/Users/you@yourcompany.com/path/to/directory"
)
print(result.path)
print(result.url)
```

In this example, the notebook from the sixth trial (index 5) of the AutoML run is imported to the specified workspace directory. The `artifact_uri` is accessed from the `TrialInfo` object within the `AutoMLSummary`.^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- [AutoML Python API Reference](/concepts/automl-python-api.md) — The complete API for starting classification, regression, and forecasting AutoML runs
- [AutoMLSummary](/concepts/automlsummary.md) — The summary object returned by AutoML run methods, containing trial information including artifact URIs
- [TrialInfo](/concepts/trialinfo.md) — The summary object for each individual trial, which provides access to the artifact URI and trained model
- [ImportNotebookResult](/concepts/importnotebookresult.md) — The result object containing the imported notebook's path and URL
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The underlying system that stores trial notebooks as MLflow artifacts
- [Databricks AutoML](/concepts/databricks-automl.md) — The broader AutoML platform for automated model training

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
