---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 15535bb3cb3275b8199e1c51a172159bf24d6115d4b259ab2a46e1f6655924ec
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-classify
    - AutoML Python API reference|classify
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: AutoML classify()
description: Python API method to start an AutoML classification run, supporting parameters such as target_col, primary_metric, imputers, pos_label, and more.
tags:
  - machine-learning
  - classification
  - api
  - databricks
timestamp: "2026-06-19T22:12:05.717Z"
---

## AutoML classify()

**AutoML classify()** is a method in the `databricks.automl` Python API that starts an AutoML run for training a classification model. The method trains a set of models and generates a trial notebook for each trained model. ^[automl-python-api-reference-databricks-on-aws.md]

### Function signature

```python
databricks.automl.classify(
  dataset: Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str],
  *,
  target_col: str,
  primary_metric: str = "f1",
  data_dir: Optional[str] = None,
  experiment_dir: Optional[str] = None,                             # DBR 10.4 LTS ML and above
  experiment_name: Optional[str] = None,                            # DBR 12.1 ML and above
  exclude_cols: Optional[List[str]] = None,                         # DBR 10.3 ML and above
  exclude_frameworks: Optional[List[str]] = None,                   # DBR 10.3 ML and above
  feature_store_lookups: Optional[List[Dict]] = None,               # DBR 11.3 LTS ML and above
  imputers: Optional[Dict[str, Union[str, Dict[str, Any]]]] = None, # DBR 10.4 LTS ML and above
  pos_label: Optional[Union[int, bool, str]] = None,                # DBR 11.1 ML and above
  time_col: Optional[str] = None,
  split_col: Optional[str] = None,                                  # DBR 15.3 ML and above
  sample_weight_col: Optional[str] = None,                          # DBR 15.4 ML and above
  max_trials: Optional[int] = None,                                 # DBR 10.5 ML and below
  timeout_minutes: Optional[int] = None,
) -> AutoMLSummary
```

^[automl-python-api-reference-databricks-on-aws.md]

### Parameters

- **dataset** – The training data. Acceptable types: [PySpark DataFrame](/concepts/pysparklyr-package.md), pandas DataFrame, pandas-on-Spark DataFrame, or a string path to a registered Delta table. ^[automl-python-api-reference-databricks-on-aws.md]
- **target_col** – The name of the column containing the label (target) to predict. ^[automl-python-api-reference-databricks-on-aws.md]
- **primary_metric** – The primary evaluation metric to optimize during model selection. Default is `"f1"`. ^[automl-python-api-reference-databricks-on-aws.md]
- **data_dir**, **experiment_dir**, **experiment_name** – Directories or experiment names for storing output data and [MLflow experiments](/concepts/mlflow-experiment.md). Availability depends on the [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) version. ^[automl-python-api-reference-databricks-on-aws.md]
- **exclude_cols** – List of column names to exclude from training (available from DBR 10.3 ML). ^[automl-python-api-reference-databricks-on-aws.md]
- **exclude_frameworks** – List of machine learning frameworks to exclude (available from DBR 10.3 ML). ^[automl-python-api-reference-databricks-on-aws.md]
- **feature_store_lookups** – Configuration for [Feature Store](/concepts/feature-store.md) lookups (available from DBR 11.3 LTS ML). ^[automl-python-api-reference-databricks-on-aws.md]
- **imputers** – Custom imputation strategies for missing values (available from DBR 10.4 LTS ML). ^[automl-python-api-reference-databricks-on-aws.md]
- **pos_label** – The positive class label for binary classification (available from DBR 11.1 ML). ^[automl-python-api-reference-databricks-on-aws.md]
- **time_col** – Name of a timestamp column, used when the data is time‑ordered. ^[automl-python-api-reference-databricks-on-aws.md]
- **split_col** – Column used to define train/validation splits (available from DBR 15.3 ML). ^[automl-python-api-reference-databricks-on-aws.md]
- **sample_weight_col** – Column containing sample weights (available from DBR 15.4 ML). ^[automl-python-api-reference-databricks-on-aws.md]
- **max_trials** (deprecated) – Maximum number of trials. Deprecated in DBR 10.4 ML and not supported in DBR 11.0 ML and above. Use **timeout_minutes** instead. ^[automl-python-api-reference-databricks-on-aws.md]
- **timeout_minutes** – Maximum run duration in minutes. ^[automl-python-api-reference-databricks-on-aws.md]

### Return value

Returns an [AutoMLSummary](/concepts/automlsummary.md) object describing the metrics, parameters, and other details for each trial. The summary also provides methods to load models trained by a specific trial. The individual trial results are represented by [TrialInfo](/concepts/trialinfo.md). ^[automl-python-api-reference-databricks-on-aws.md]

### Related concepts

- AutoML – Overview of automated machine learning on Databricks.
- [Classification](/concepts/data-classification.md) – The task of predicting a categorical label.
- [MLflow](/concepts/mlflow.md) – Used to log experiments and models.
- [AutoMLSummary](/concepts/automlsummary.md) – Container for all trial results.
- [TrialInfo](/concepts/trialinfo.md) – Details for a single trial, including model loading.
- [ImportNotebookResult](/concepts/importnotebookresult.md) – Result from importing a notebook saved as an MLflow artifact.

### Sources

- automl-python-api-reference-databricks-on-aws.md

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
