---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e280953cb54c7a222fa6e04b1ce84a535da52740d3ac79aa2bc7408a566e331
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - active-mlflow-run-management-with-fit
    - AMRMWF
    - mlflow-active-run-management-with-fit
    - MARMWF
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: Active MLflow Run Management with fit()
description: The recommended practice of wrapping CrossValidator/TrainValidationSplit fit() calls inside a 'with mlflow.start_run():' statement to ensure proper logging under a dedicated MLflow main run and enable additional custom logging.
tags:
  - mlflow
  - best-practices
  - spark-mllib
timestamp: "2026-06-19T22:07:13.542Z"
---

# Active [MLflow Run](/concepts/mlflow-run.md) Management with fit()

**Active [MLflow Run](/concepts/mlflow-run.md) Management with `fit()`** refers to the recommended practice of wrapping calls to `fit()` — specifically when using `CrossValidator` or `TrainValidationSplit` in [Apache Spark MLlib](/concepts/apache-spark-mllib.md) — inside an MLflow active run context using `mlflow.start_run()`. This ensures that hyperparameter tuning results are logged under their own dedicated MLflow main run, making it easier to organize and tag experiments. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Overview

When [MLlib Automated MLflow Tracking](/concepts/mllib-automated-mlflow-tracking.md) is enabled, `CrossValidator` or `TrainValidationSplit` log tuning results as nested MLflow runs:

- **Main (parent) run**: The information for the `CrossValidator` or `TrainValidationSplit` is logged to the main run. If there is already an active run, information is logged to that active run without stopping it. If no active run exists, MLflow creates a new run, logs to it, and ends the run before returning. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]
- **Child runs**: Each hyperparameter setting tested and the corresponding evaluation metric are logged to a child run under the main run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Recommended Practice

Databricks recommends wrapping the call to `fit()` inside a `with mlflow.start_run():` statement. This practice ensures that:

1. The information is logged under its own MLflow main run, distinct from any other active runs.
2. It becomes easier to log additional tags, parameters, or metrics to that specific run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

### Example

```python
import mlflow

with mlflow.start_run():
    # fit() will log tuning results as child runs under this main run
    model = cv.fit(training_data)
```

### Important Note

When `fit()` is called multiple times within the same active [MLflow Run](/concepts/mlflow-run.md), those multiple calls are logged to the same main run. To resolve name conflicts for MLflow parameters and tags, MLflow appends a UUID to names with conflicts. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## MLlib Automated MLflow Tracking Context

MLlib automated MLflow tracking automatically logs hyperparameters and evaluation metrics from `CrossValidator` or `TrainValidationSplit` tuning code without requiring explicit API calls. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

**Deprecation note**: MLlib automated MLflow tracking is deprecated on clusters running Databricks Runtime 10.1 ML and above, and is disabled by default on clusters running Databricks Runtime 10.2 ML and above. Instead, use [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md) by calling `mlflow.pyspark.ml.autolog()`, which is enabled by default with [Databricks Autologging](/concepts/databricks-autologging.md). To use the old MLlib automated MLflow tracking in Databricks Runtime 10.2 ML or above, enable it by setting the Spark configurations `spark.databricks.mlflow.trackMLlib.enabled true` and `spark.databricks.mlflow.autologging.enabled false`. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — The core tracking API for logging experiments
- [MLlib Automated MLflow Tracking](/concepts/mllib-automated-mlflow-tracking.md) — The automated logging feature for Spark MLlib tuning
- [Nested MLflow Runs](/concepts/nested-mlflow-runs-for-tuning.md) — The structure used by `CrossValidator` and `TrainValidationSplit` for organizing tuning results
- [Databricks Autologging](/concepts/databricks-autologging.md) — The modern default approach for automatic MLflow logging
- [CrossValidator](/concepts/crossvalidator.md) — Spark MLlib model selection tool that benefits from active run management
- [TrainValidationSplit](/concepts/trainvalidationsplit.md) — Alternative model selection tool that logs results as nested runs

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
