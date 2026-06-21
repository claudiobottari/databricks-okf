---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3ec2c269e254b0be94e01132d9195ed29fd77c9856c2e0fa5f6c3a3cb4d47e33
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - classify
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: Classify
description: The databricks.automl.classify method configures an AutoML run to train a classification model.
tags:
  - auto-ml
  - classification
  - python-api
timestamp: "2026-06-19T17:39:12.662Z"
---

---
title: Classify
summary: The `databricks.automl.classify` method configures an AutoML run to train a classification model.
sources:
  - automl-python-api-reference-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:09:21.819Z"
updatedAt: "2026-06-18T08:09:21.819Z"
tags:
  - databricks
  - automl
  - api
  - classification
aliases:
  - classify-method
  - automl-classify
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Classify

**Classify** (lowercase `classify` in code) is a method in the `databricks.automl` Python API that initiates an AutoML run for training a [Classification](/concepts/data-classification.md) model. It accepts a dataset and a target column, then automatically trains multiple models and generates a trial notebook for each model. The method returns an `AutoMLSummary` object containing metrics and details for each trial. ^[automl-python-api-reference-databricks-on-aws.md]

## Parameters

The function signature is:

```python
databricks.automl.classify(
    dataset,
    *,
    target_col,
    primary_metric="f1",
    data_dir=None,
    experiment_dir=None,
    experiment_name=None,
    exclude_cols=None,
    exclude_frameworks=None,
    feature_store_lookups=None,
    imputers=None,
    pos_label=None,
    time_col=None,
    split_col=None,
    sample_weight_col=None,
    max_trials=None,
    timeout_minutes=None,
) -> AutoMLSummary
```

^[automl-python-api-reference-databricks-on-aws.md]

Key parameters include:

- **`dataset`** – A PySpark DataFrame, pandas DataFrame, pandas-on-Spark DataFrame, or a path to a Delta table.
- **`target_col`** (required) – The name of the column containing the target labels.
- **`primary_metric`** – The metric to optimize. Default is `"f1"`.
- **`timeout_minutes`** – Controls the maximum duration of the AutoML run. In Databricks Runtime 11.0 ML and above, this replaces the deprecated `max_trials` parameter.
- **`pos_label`** (Databricks Runtime 11.1 ML+) – Specifies the positive label for binary classification.
- **`split_col`** (Databricks Runtime 15.3 ML+) – Optional column name to define train/test splits.
- **`sample_weight_col`** (Databricks Runtime 15.4 ML+) – Optional column for sample weights.

See the full parameter list in the source documentation for version-specific availability. ^[automl-python-api-reference-databricks-on-aws.md]

## Return Value

Returns an `AutoMLSummary` object, which includes:

- Trial information accessible via `summary.trials` (list of `TrialInfo` objects).
- Methods to load the model trained by a specific trial.
- An `artifact_uri` for each trial that can be used with `databricks.automl.import_notebook()` to import the generated notebook. ^[automl-python-api-reference-databricks-on-aws.md]

## Example

```python
summary = databricks.automl.classify(
    dataset=train_df,
    target_col="label",
    timeout_minutes=30,
)
# Load the best model
best_trial = summary.trials[0]
model = best_trial.load_model()
```

^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- AutoML – Overview of automated machine learning on Databricks.
- [AutoMLSummary](/concepts/automlsummary.md) – The summary object returned by all AutoML run methods.
- [TrialInfo](/concepts/trialinfo.md) – Object describing each trial’s metrics, parameters, and artifact URI.
- [Regress](/concepts/regress.md) – The analogous method for regression tasks.
- [Forecast](/concepts/forecast.md) – The analogous method for time series forecasting.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The runtime that includes the AutoML API.

## Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
