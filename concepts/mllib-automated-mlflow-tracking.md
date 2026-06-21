---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 57e9ff1aaddc619955a2eb6b8cb5068fb6b2a5e221c052a32b167c9c5f119f25
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
    - hyperparameter-tuning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mllib-automated-mlflow-tracking
    - MAMT
    - Automated MLflow Tracking
    - Apache Spark MLlib and MLflow Tracking
    - Apache Spark MLlib automated MLflow tracking
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
    - file: hyperparameter-tuning-databricks-on-aws.md
title: MLlib Automated MLflow Tracking
description: A deprecated Databricks feature that automatically logs hyperparameters and evaluation metrics to MLflow when tuning Apache Spark MLlib models using CrossValidator or TrainValidationSplit, without requiring explicit API calls.
tags:
  - machine-learning
  - mlflow
  - databricks
  - spark-mllib
timestamp: "2026-06-19T22:06:57.175Z"
---

```markdown
# MLlib Automated MLflow Tracking

**MLlib Automated MLflow Tracking** is a Databricks feature that automatically logs hyperparameters and evaluation metrics to [[MLflow]] when tuning [[apache-spark-mllib|Apache Spark MLlib]] models using `CrossValidator` or `TrainValidationSplit`, without requiring explicit API calls. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md] ^[hyperparameter-tuning-databricks-on-aws.md]

## Overview

MLlib Automated MLflow Tracking is supported for Python notebooks on [[Databricks Runtime for Machine Learning]] and certain Databricks Runtime versions. When you run tuning code that uses `CrossValidator` or `TrainValidationSplit`, hyperparameters and evaluation metrics are automatically logged to MLflow without requiring explicit API calls. The feature supports tracking for machine learning model tuning in Python, R, and Scala, though automated tracking is only available for Python notebooks. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## How It Works

When tuning code runs using `CrossValidator` or `TrainValidationSplit`, the results are logged as nested MLflow runs: ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

- **Main (parent) run**: Information for the `CrossValidator` or `TrainValidationSplit` is logged to the main run. If there is an already active run, information is logged to that active run and the active run is not stopped. If there is no active run, MLflow creates a new run, logs to it, and ends the run before returning. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]
- **Child runs**: Each hyperparameter setting tested and the corresponding evaluation metric are logged to a child run under the main run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Best Practices

When calling `fit()`, Databricks recommends active [[mlflow-run|MLflow Run]] management — wrapping the call to `fit()` inside a `with mlflow.start_run():` statement. This ensures that the information is logged under its own MLflow main run and makes it easier to log additional tags, parameters, or metrics to that run. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

When `fit()` is called multiple times within the same active [[mlflow-run|MLflow Run]], those multiple runs are logged to the same main run. To resolve name conflicts for MLflow parameters and tags, MLflow appends a UUID to names with conflicts. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Deprecation and Replacement

MLlib Automated MLflow Tracking is deprecated on clusters running Databricks Runtime 10.1 ML and above, and it is disabled by default on clusters running Databricks Runtime 10.2 ML and above. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md] The same deprecation is confirmed for clusters running Databricks Runtime 10.4 LTS ML and above. ^[hyperparameter-tuning-databricks-on-aws.md]

The recommended replacement is [[MLflow PySpark ML autologging]], which is enabled by default with [[Databricks Autologging]]. To use it, call `mlflow.pyspark.ml.autolog()`. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md] ^[hyperparameter-tuning-databricks-on-aws.md]

To re-enable the old MLlib Automated MLflow Tracking in Databricks Runtime 10.2 ML or above, set the following Spark Configurations: ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

```
spark.databricks.mlflow.trackMLlib.enabled true
spark.databricks.mlflow.autologging.enabled false
```

## Related Concepts

- [[MLflow]] — Open source platform for managing the machine learning lifecycle
- [[MLflow Tracking]] — Component for logging and querying ML experiments
- [[Databricks Autologging]] — Automatic MLflow logging for common ML frameworks
- [[MLflow PySpark ML autologging]] — The recommended replacement for MLlib automated tracking
- [[CrossValidator]] — Spark MLlib model tuning estimator
- [[TrainValidationSplit]] — Spark MLlib model tuning estimator
- [[Hyperparameter Tuning]] — Broader topic of optimizing model hyperparameters
- Spark Configurations — Settings for configuring Spark clusters

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
- hyperparameter-tuning-databricks-on-aws.md
```

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
2. [hyperparameter-tuning-databricks-on-aws.md](/references/hyperparameter-tuning-databricks-on-aws-6d74646d.md)
