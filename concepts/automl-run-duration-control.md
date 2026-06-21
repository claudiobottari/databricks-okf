---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2b4f412e784270472ae93045ca66afa2b1995eef195e69f05726a93779f0020a
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-run-duration-control
    - ARDC
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
    - file: automl-python-api-reference-databricks-on-aws.md
      start: 7
      end: 9
title: AutoML Run Duration Control
description: Controlling AutoML run duration via timeout_minutes, with max_trials deprecated
tags:
  - automl
  - best-practice
  - databricks
timestamp: "2026-06-18T10:51:56.883Z"
---

# AutoML Run Duration Control

**AutoML run duration control** refers to the mechanism for limiting the execution time of an automated machine learning run in Databricks AutoML. The primary way to control run duration is the `timeout_minutes` parameter; the older `max_trials` parameter is deprecated. ^[automl-python-api-reference-databricks-on-aws.md]

## The `max_trials` Parameter (Deprecated)

The `max_trials` parameter was used in earlier versions of Databricks Runtime to limit an AutoML run by specifying the maximum number of model trials. It is deprecated in Databricks Runtime 10.4 ML and is **not supported** in Databricks Runtime 11.0 ML and above. ^[automl-python-api-reference-databricks-on-aws.md:7-9]

Databricks recommends replacing `max_trials` with `timeout_minutes` to control run duration. In the Python API, `max_trials` appears only in the signatures of the `classify` and `regress` methods, and only for Databricks Runtime 10.5 ML and below. ^[automl-python-api-reference-databricks-on-aws.md:7-9]

## The `timeout_minutes` Parameter

The `timeout_minutes` parameter is the recommended, cross-version approach for controlling the duration of an AutoML run. It is accepted by all three main AutoML methods—[AutoML Python API reference|classify](/concepts/automl-classify.md), [AutoML Python API reference|regress](/concepts/automl-regress.md), and [AutoML Python API reference|forecast](/concepts/automl-forecast.md)—as an optional integer. The run stops when the specified number of minutes is reached, regardless of how many trials have completed. ^[automl-python-api-reference-databricks-on-aws.md]

Using `timeout_minutes` gives predictable wall-clock time limits and adapts naturally to varying workload sizes, which `max_trials` could not guarantee.

## Usage in the Python API

The following example shows how to start a classification AutoML run with a 60‑minute timeout:

```python
import databricks.automl

summary = databricks.automl.classify(
    dataset=my_dataframe,
    target_col="label",
    timeout_minutes=60
)
```

The same pattern applies to `regress` and `forecast`. The method returns an `AutoMLSummary` object that contains the metrics and trial information for the run. ^[automl-python-api-reference-databricks-on-aws.md]

## Run Duration and Trial Notebooks

Each AutoML run trains a set of models and generates a trial notebook for every model. The `timeout_minutes` limit covers the overall run, including training, evaluation, and notebook generation. If the timeout is reached, any ongoing trial is stopped and results from completed trials are preserved. ^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- [AutoML Python API reference](/concepts/automl-python-api.md) — Complete API details for `classify`, `regress`, and `forecast`
- [AutoML Summary](/concepts/automlsummary.md) — The object returned by an AutoML run, containing trial information
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The runtime versions that affect parameter support
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Used by AutoML to log trial results

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
2. [automl-python-api-reference-databricks-on-aws.md:7-9](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
