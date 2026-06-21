---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9e0b811d9ff8ff9d40c8a99cc7f7432bd737f6852e335a14b912fcc6ed530992
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - importnotebookresult
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: ImportNotebookResult
description: Result object returned by import_notebook containing the path and URL of the imported notebook.
tags:
  - machine-learning
  - automl
  - notebooks
  - databricks
timestamp: "2026-06-19T22:12:17.580Z"
---

# ImportNotebookResult

**ImportNotebookResult** is the return type of the `databricks.automl.import_notebook` method. This method imports a notebook that has been saved as an MLflow artifact and returns an `ImportNotebookResult` object containing metadata about the imported notebook. ^[automl-python-api-reference-databricks-on-aws.md]

## Attributes

The `ImportNotebookResult` object exposes at least the following attributes, as demonstrated in the API example: ^[automl-python-api-reference-databricks-on-aws.md]

- `path` – A string representing the file system path of the imported notebook in the Databricks workspace.
- `url` – A string representing the URL of the imported notebook in the Databricks workspace.

## Method Signature

The `import_notebook` method accepts the following parameters and returns an `ImportNotebookResult`: ^[automl-python-api-reference-databricks-on-aws.md]

```python
databricks.automl.import_notebook(
    artifact_uri: str,
    path: str,
    overwrite: bool = False
) -> ImportNotebookResult
```

- `artifact_uri` – The URI of the MLflow artifact containing the notebook.
- `path` – The target workspace path where the notebook should be imported.
- `overwrite` (optional) – If `True`, overwrites an existing notebook at the target path; defaults to `False`.

## Usage

Typically, you obtain an artifact URI from an [AutoMLSummary](/concepts/automlsummary.md) object (for example, from a specific trial) and call `import_notebook` to create a workspace notebook from that artifact. The returned `ImportNotebookResult` can then be used to navigate to the notebook via its `path` or `url`. ^[automl-python-api-reference-databricks-on-aws.md]

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

- [AutoMLSummary](/concepts/automlsummary.md) – The parent object that holds trial information and artifact URIs.
- MLflow Artifacts – The storage mechanism for trial notebooks generated during AutoML runs.
- Databricks Notebooks – The workspace object type created by importing an artifact.
- [TrialInfo](/concepts/trialinfo.md) – Contains individual trial details, including the artifact URI used for import.

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
