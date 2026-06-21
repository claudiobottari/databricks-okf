---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a74b85b162f29c2b84220dbf85bc18d8f64af95acf6fe342e8b2660371b9046a
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - xgboost-classification-on-databricks
    - XCOD
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
title: XGBoost Classification on Databricks
description: Example notebook showing XGBoost classification embedded in an MLlib ML pipeline on Databricks
tags:
  - machine-learning
  - classification
  - xgboost
  - databricks
timestamp: "2026-06-18T12:05:03.483Z"
---

# XGBoost Classification on Databricks

**XGBoost Classification on Databricks** refers to the practice of training and deploying XGBoost classification models within the Databricks platform, leveraging Apache Spark and MLlib for distributed computation. XGBoost is a gradient-boosted decision tree (GBDT) algorithm that performs well on structured and tabular data, and integrates with Databricks's unified analytics environment for scalable model development.

## Overview

XGBoost (Extreme Gradient Boosting) is a popular machine learning algorithm that builds an ensemble of decision trees sequentially, correcting errors from previous trees with each new tree. On Databricks, you can distribute XGBoost training across a cluster of worker nodes using the XGBoost4J-Spark library, which is bundled in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) (Databricks Runtime ML). ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

Classification with XGBoost on Databricks typically involves:

- **Binary classification**: Predicting one of two outcomes (e.g., customer churn vs. not churn).
- **Multiclass classification**: Predicting among three or more categories (e.g., product categorization).
- **Distributed training**: Using [Spark MLlib pipeline](/concepts/mllib-pipelines-api.md) stages to parallelize training across a cluster, reducing training time on large datasets. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Workflow

1. **Prepare data**: Convert a Spark DataFrame into an XGBoost-compatible format — usually a sparse or dense feature vector plus a label column. A VectorAssembler or custom UDF can combine raw columns into a feature vector. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]
2. **Define the model**: Instantiate an `XGBoostClassifier` (for binary/multiclass) or `XGBoostRegressor` (for regression). Set hyperparameters such as `max_depth`, `learning_rate`, `n_estimators`, and the number of worker nodes (`n_workers`). ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]
3. **Train**: Call `.fit()` on the training DataFrame. XGBoost automatically partitions the feature matrix across the cluster and builds trees in parallel.
4. **Evaluate**: Use MLlib evaluators (e.g., `BinaryClassificationEvaluator` or `MulticlassClassificationEvaluator`) to compute AUC, accuracy, or other metrics.
5. **Tune**: Use [CrossValidator](/concepts/crossvalidator.md) or [TrainValidationSplit](/concepts/trainvalidationsplit.md) with ParamGridBuilder to search over hyperparameter grids. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]
6. **Deploy**: Save the trained model as an MLflow model or a Spark ML pipeline. Then serve it on a [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoint.

## Integration with Spark MLlib

You can embed an XGBoost classifier as the last stage of a Spark ML pipeline. This enables feature transformations (scaling, one-hot encoding, text vectorization) to happen before the XGBoost model sees the data. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

```python
# Pseudocode — the Scala example uses the same conceptual pipeline.
from pyspark.ml.feature import VectorAssembler
from pyspark.ml import Pipeline
from xgboost.spark import SparkXGBClassifier

assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
xgb = SparkXGBClassifier(
    featuresCol="features",
    labelCol="target",
    numRound=100,
    maxDepth=6,
    objective="binary:logistic",
)
pipeline = Pipeline(stages=[assembler, xgb])
model = pipeline.fit(train_df)
```

## Cross-Validation with XGBoost

MLlib's cross-validation can tune XGBoost hyperparameters without manual grid search. The example notebook shows how to wrap an XGBoost model in an [MLlib cross-validation pipeline](/concepts/crossvalidator.md) and evaluate each fold's performance. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Notebook examples

Databricks provides two reference notebooks for XGBoost classification:

- **XGBoost classification with ML pipeline**: Demonstrates embedding an XGBoost classifier in a Spark ML pipeline, fitting, prediction, and evaluation.
- **XGBoost regression with cross-validation**: Shows how to use MLlib cross-validation to tune an XGBoost regressor (the same pattern applies to classifiers). ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Requirements

- Databricks Runtime for Machine Learning (any version that includes XGBoost and XGBoost4J-Spark) — usually Databricks Runtime ML 10.x or higher. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]
- A cluster with at least two worker nodes to benefit from distributed training. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]
- Scala or Python code — both are supported. PySpark users can call `sparkxgb` from the `xgboost.spark` package. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Related concepts

- [Feature Engineering on Databricks](/concepts/feature-engineering-on-databricks.md)
- Model Evaluation with MLflow
- Hyperparameter Tuning with Hyperopt
- [Spark ML Pipelines](/concepts/mllib-pipelines-api.md)
- [XGBoost](/concepts/xgboostspark-module.md)
- [Gradient Boosted Trees](/concepts/gradient-boosted-trees-regression-with-mllib.md)

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
