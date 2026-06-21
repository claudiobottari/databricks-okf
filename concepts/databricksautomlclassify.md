---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f484872b62006d74694357ead5a71ccfb6cc463d7a8b08298c91d1878cea924
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricksautomlclassify
  citations:
    - file: automl-python-api-reference-databricks-on-aws.md
title: databricks.automl.classify
description: AutoML method that trains classification models, returning an AutoMLSummary with trial notebooks and model metrics.
tags:
  - AutoML
  - classification
  - Databricks
  - API
timestamp: "2026-06-19T14:07:31.397Z"
---

```markdown
---
title: databricks.automl.classify
summary: AutoML method for training classification models, returning an AutoMLSummary with trial notebooks per model.
sources:
  - automl-python-api-reference-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:31:07.970Z"
updatedAt: "2026-06-18T14:31:07.970Z"
tags:
  - AutoML
  - classification
  - machine-learning
  - Databricks
aliases:
  - databricksautomlclassify
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# databricks.automl.classify

The `databricks.automl.classify` method configures an AutoML run to train a classification model. It is one of three primary AutoML tasks in Databricks, alongside `databricks.automl.regress` for regression and `databricks.automl.forecast` for forecasting. ^[automl-python-api-reference-databricks-on-aws.md]

## Signature

```python
databricks.automl.classify(
    dataset: Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str],
    *,
    target_col: str,
    primary_metric: str = "f1",
    data_dir: Optional[str] = None,
    experiment_dir: Optional[str] = None,        # :re[DBR] 10.4 LTS ML and above
    experiment_name: Optional[str] = None,       # :re[DBR] 12.1 ML and above
    exclude_cols: Optional[List[str]] = None,    # :re[DBR] 10.3 ML and above
    exclude_frameworks: Optional[List[str]] = None,  # :re[DBR] 10.3 ML and above
    feature_store_lookups: Optional[List[Dict]] = None,  # :re[DBR] 11.3 LTS ML and above
    imputers: Optional[Dict[str, Union[str, Dict[str, Any]]]] = None,  # :re[DBR] 10.4 LTS ML and above
    pos_label: Optional[Union[int, bool, str]] = None,  # :re[DBR] 11.1 ML and above
    time_col: Optional[str] = None,
    split_col: Optional[str] = None,            # :re[DBR] 15.3 ML and above
    sample_weight_col: Optional[str] = None,    # :re[DBR] 15.4 ML and above
    max_trials: Optional[int] = None,           # :re[DBR] 10.5 ML and below (deprecated)
    timeout_minutes: Optional[int] = None,
) -> AutoMLSummary
```

^[automl-python-api-reference-databricks-on-aws.md]

## Parameters

- **dataset** – The input data for training. Can be a PySpark DataFrame, pandas DataFrame, pandas-on-Spark DataFrame, or a path (string) to a table. ^[automl-python-api-reference-databricks-on-aws.md]
- **target_col** – The name of the column that contains the labels (target variable) for classification. ^[automl-python-api-reference-databricks-on-aws.md]
- **primary_metric** – The metric used to select the best model; defaults to `"f1"`. ^[automl-python-api-reference-databricks-on-aws.md]
- **data_dir** – Path to a directory where AutoML stores intermediate data. ^[automl-python-api-reference-databricks-on-aws.md]
- **experiment_dir** – (Available in Databricks Runtime 10.4 LTS ML and above) Path to an MLflow experiment directory for tracking runs. ^[automl-python-api-reference-databricks-on-aws.md]
- **experiment_name** – (Available in DBR 12.1 ML and above) Name of an MLflow experiment. ^[automl-python-api-reference-databricks-on-aws.md]
- **exclude_cols** – (Available in DBR 10.3 ML and above) List of column names to exclude from training. ^[automl-python-api-reference-databricks-on-aws.md]
- **exclude_frameworks** – (Available in DBR 10.3 ML and above) List of ML frameworks (e.g., `["lightgbm"]`) to exclude from the search. ^[automl-python-api-reference-databricks-on-aws.md]
- **feature_store_lookups** – (Available in DBR 11.3 LTS ML and above) List of dictionaries describing feature store lookups. ^[automl-python-api-reference-databricks-on-aws.md]
- **imputers** – (Available in DBR 10.4 LTS ML and above) Dictionary specifying imputation strategies for missing values. ^[automl-python-api-reference-databricks-on-aws.md]
- **pos_label** – (Available in DBR 11.1 ML and above) The positive class label for binary classification. ^[automl-python-api-reference-databricks-on-aws.md]
- **time_col** – Optional column that identifies time ordering (used for time-aware splitting). ^[automl-python-api-reference-databricks-on-aws.md]
- **split_col** – (Available in DBR 15.3 ML and above) Column used to define custom train/validation splits. ^[automl-python-api-reference-databricks-on-aws.md]
- **sample_weight_col** – (Available in DBR 15.4 ML and above) Column containing sample weights for training. ^[automl-python-api-reference-databricks-on-aws.md]
- **max_trials** – Deprecated in Databricks Runtime 10.4 ML and unsupported in DBR 11.0 ML and above. Use `timeout_minutes` instead. ^[automl-python-api-reference-databricks-on-aws.md]
- **timeout_minutes** – Maximum duration (in minutes) allowed for the AutoML run. Controls run length instead of a fixed trial count. ^[automl-python-api-reference-databricks-on-aws.md]

## Return Value

Returns an [[AutoMLSummary]] object containing metrics, parameters, and details for each trial. You can use this object to load the best model or any specific trial model. ^[automl-python-api-reference-databricks-on-aws.md]

## Usage Notes

- Each `classify` run trains a set of models and generates a trial notebook for each model. ^[automl-python-api-reference-databricks-on-aws.md]
- The `max_trials` parameter is deprecated; use `timeout_minutes` to control the duration of an AutoML run. ^[automl-python-api-reference-databricks-on-aws.md]

## Related Concepts

- [[databricks.automl.regress]] – Regression AutoML runs.
- [[databricks.automl.forecast]] – Forecasting AutoML runs.
- [[AutoMLSummary]] – The summary object returned by all AutoML task methods.
- [[TrialInfo]] – Summary of an individual trial.
- [[ImportNotebookResult]] – Result of importing a trial notebook.

## Sources

- automl-python-api-reference-databricks-on-aws.md
```

# Citations

1. [automl-python-api-reference-databricks-on-aws.md](/references/automl-python-api-reference-databricks-on-aws-bc754c3a.md)
