---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ff467f3de2dd932dcd6c1e01a398e9cc6e1efa25d97dba1ca31976141fffc8e6
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricksautomlimport_notebook
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: databricks.automl.import_notebook
description: Method to import a notebook saved as an MLflow artifact, returning an ImportNotebookResult with path and URL.
tags:
  - AutoML
  - notebooks
  - MLflow
  - Databricks
timestamp: "2026-06-19T14:07:37.946Z"
---

---
title: databricks.automl.import_notebook
summary: Method to import a notebook saved as an MLflow artifact into a Databricks workspace path.
sources:
  - automl-python-api-reference-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:31:13.494Z"
updatedAt: "2026-06-18T14:31:13.494Z"
tags:
  - AutoML
  - notebook
  - MLflow
  - Databricks
aliases:
  - databricksautomlimport_notebook
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# databricks.automl.import_notebook

The `databricks.automl.import_notebook` method imports a notebook that has been saved as an MLflow artifact and returns an [ImportNotebookResult](/concepts/importnotebookresult.md) object. It is part of the [AutoML Python API](/concepts/automl-python-api.md) and is typically used after an AutoML run to bring one of the generated trial notebooks into the Databricks workspace. ^[automl-python-api-reference-databricks-on-aws.md]

## Signature

```python
databricks.automl.import_notebook(
    artifact_uri: str,
    path: str,
    overwrite: bool = False
) -> ImportNotebookResult
```

## Parameters

- **`artifact_uri`** (str) – The URI of the MLflow artifact containing the notebook. This is usually obtained from a trial’s `artifact_uri` attribute in an [AutoMLSummary](/concepts/automlsummary.md) object.
- **`path`** (str) – The target workspace path where the notebook should be imported.
- **`overwrite`** (bool, default `False`) – If `True`, overwrites an existing notebook at the target path.

## Return value

The method returns an [ImportNotebookResult](/concepts/importnotebookresult.md), which contains at least the fields `path` and `url` that describe the location of the imported notebook in the workspace. ^[automl-python-api-reference-databricks-on-aws.md]

## Example

The following example runs a classification AutoML run and then imports one of the generated trial notebooks into the user’s workspace directory.

```python
summary = databricks.automl.classify(...)
result = databricks.automl.import_notebook(
    summary.trials[5].artifact_uri,
    "/Users/you@yourcompany.com/path/to/directory"
)
print(result.path)
print(result.url)
```

## Related Concepts

- [AutoML Python API](/concepts/automl-python-api.md) – The module that contains this method.
- [AutoMLSummary](/concepts/automlsummary.md) – The summary object providing artifact URIs for each trial.
- [TrialInfo](/concepts/trialinfo.md) – The summary object for an individual trial.
- [ImportNotebookResult](/concepts/importnotebookresult.md) – The result object returned by this method.
- MLflow artifact – The artifact store that holds the saved notebook.

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
