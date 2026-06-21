---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 98d093ceb62701cc3eb771d303a8010b989503b26e7a753d692778277f7387a1
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - regress
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: Regress
description: The databricks.automl.regress method configures an AutoML run to train a regression model.
tags:
  - auto-ml
  - regression
  - python-api
timestamp: "2026-06-19T17:39:25.389Z"
---

Here is the wiki page for "Regress", written based solely on the provided source material.

---

## Regress

The `databricks.automl.regress` method is part of the [Databricks AutoML Python API](/concepts/databricks-automl-python-api.md). It configures an AutoML run to train a regression model. The method returns an `AutoMLSummary` object, which describes the metrics, parameters, and other details for each of the trials generated during the run. ^[automl-python-api-reference-databricks-on-aws.md]

### Parameters

The `regress` method accepts the following parameters:

- `dataset` (required): The input data. Can be a `pyspark.sql.DataFrame`, `pandas.DataFrame`, `pyspark.pandas.DataFrame`, or a string representing a path to data.
- `target_col` (required): A string specifying the name of the target column to predict.
- `primary_metric` (optional): The primary metric for evaluating the model. The default value is `"r2"`.
- `data_dir` (optional): A string path for the data directory.
- `experiment_dir` (optional, Databricks Runtime 10.4 LTS ML and above): A string path for the experiment directory.
- `experiment_name` (optional, Databricks Runtime 12.1 ML and above): A string for the experiment name.
- `exclude_cols` (optional, Databricks Runtime 10.3 ML and above): A list of column names to exclude from training.
- `exclude_frameworks` (optional, Databricks Runtime 10.3 ML and above): A list of framework names to exclude.
- `feature_store_lookups` (optional, Databricks Runtime 11.3 LTS ML and above): A list of dictionaries for feature store lookups.
- `imputers` (optional, Databricks Runtime 10.4 LTS ML and above): A dictionary specifying imputation strategies for missing values.
- `time_col` (optional): A string specifying the name of the time column.
- `split_col` (optional, Databricks Runtime 15.3 ML and above): A string specifying the name of the column used for data splitting.
- `sample_weight_col` (optional, Databricks Runtime 15.3 ML and above): A string specifying the name of the column containing sample weights.
- `max_trials` (optional, deprecated in Databricks Runtime 10.4 ML, not supported in 11.0 ML and above): An integer for the maximum number of trials. Use `timeout_minutes` instead.
- `timeout_minutes` (optional): An integer for the maximum duration of the AutoML run in minutes.

^[automl-python-api-reference-databricks-on-aws.md]

### Related Concepts

- [databricks.automl.classify](/concepts/databricksautomlclassify.md) – The equivalent method for training classification models.
- [databricks.automl.forecast](/concepts/databricksautomlforecast.md) – The equivalent method for training forecasting models.
- [AutoMLSummary](/concepts/automlsummary.md) – The object returned by the `regress` method.
- [Databricks AutoML](/concepts/databricks-automl.md) – Overview of the automated machine learning capabilities on Databricks.

### Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
