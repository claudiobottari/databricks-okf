---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d7e12239d820bc30593a4137f88538c81df9a5bf8a0a41f4c67e9619a52491ab
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automlsummary
    - AutoML Summary
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: AutoMLSummary
description: Summary object returned by AutoML runs that describes metrics, parameters, and trial details, and provides methods to load trained models.
tags:
  - machine-learning
  - automl
  - api
  - databricks
timestamp: "2026-06-19T22:12:29.645Z"
---

```markdown
---
title: AutoMLSummary
summary: Summary object for an AutoML run describing metrics, parameters, and trial details, used to load trained models.
sources:
  - automl-python-api-reference-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:51:59.849Z"
updatedAt: "2026-06-19T17:39:18.478Z"
tags:
  - auto-ml
  - api-object
  - databricks
aliases:
  - automlsummary
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# AutoMLSummary

**AutoMLSummary** is a summary object returned by the Databricks AutoML Python API methods `classify`, `regress`, and `forecast`. It describes the metrics, parameters, and other details for each trial in an AutoML run, and provides a way to load the model trained by a specific trial. ^[automl-python-api-reference-databricks-on-aws.md]

## Obtaining an AutoMLSummary

Every AutoML run returns an `AutoMLSummary` instance. The three entry-point methods are:

- `databricks.automl.classify(...)` — for [[AutoML Classification (classify)|auto-ml-classification|classification]] problems
- `databricks.automl.regress(...)` — for regression problems
- `databricks.automl.forecast(...)` — for [[AutoML Forecasting (forecast)|auto-ml-forecasting|forecasting]] problems

Each method accepts a dataset, a target column, and various optional parameters (e.g., `timeout_minutes`, `primary_metric`, `exclude_cols`, `exclude_frameworks`, `feature_store_lookups`, `imputers`, `sample_weight_col`, and others that vary by task). The returned `AutoMLSummary` contains the complete results of the run. ^[automl-python-api-reference-databricks-on-aws.md]

> **Note:** The `max_trials` parameter is deprecated in Databricks Runtime 10.4 ML and is not supported in Databricks Runtime 11.0 ML and above. Use `timeout_minutes` to control the duration of an AutoML run. ^[automl-python-api-reference-databricks-on-aws.md]

## Key Properties

The summary object exposes a `trials` attribute, which is a list of [[TrialInfo]] objects. Each `TrialInfo` represents a single trial (model) trained during the AutoML run and carries the trial's metrics, parameters, and an `artifact_uri` pointing to the logged MLflow artifacts. ^[automl-python-api-reference-databricks-on-aws.md]

## Using AutoMLSummary

To inspect the results of a specific trial, index into the `trials` list:

```python
summary = databricks.automl.classify(...)
trial = summary.trials[5]
print(trial.artifact_uri)
```

The `TrialInfo` object also has a method to load the model generated for that trial. ^[automl-python-api-reference-databricks-on-aws.md]

### Importing a trial notebook

The `databricks.automl.import_notebook` method imports a notebook that was saved as an MLflow artifact in a trial. It takes the `artifact_uri` (typically obtained from a `TrialInfo`), a destination path, and an `overwrite` flag. It returns an [[ImportNotebookResult]] object containing the path and URL of the imported notebook. ^[automl-python-api-reference-databricks-on-aws.md]

Example:

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

## Related concepts

- AutoML — The low-code and API-based automated machine learning framework
- [[MLflow]] — Tracking and artifact logging used by AutoML runs
- [[TrialInfo]] — Summary object for an individual trial within an AutoML run
- [[ImportNotebookResult]] — Result of importing a trial notebook from an artifact URI
- PySpark — Common data source type for AutoML datasets

## Sources

- automl-python-api-reference-databricks-on-aws.md
```

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
