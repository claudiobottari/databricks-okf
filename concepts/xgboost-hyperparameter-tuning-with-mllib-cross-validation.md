---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: afb6d8fe88c72e4d5cc179fb0a81491020108ae6f777198d96d2dae839beb485
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - xgboost-hyperparameter-tuning-with-mllib-cross-validation
    - XHTWMC
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
    - file: xgboost-gpu-gpu.md
    - file: previous-section
    - file: hyperparameter-tuning-with-hyperopt-on-databricks-databricks-on-aws.md
    - file: automated-ml-on-databricks-databricks-on-aws.md
title: XGBoost hyperparameter tuning with MLlib cross-validation
description: Using MLlib's CrossValidator to tune XGBoost model hyperparameters (e.g., n_estimators, max_depth) in a distributed Scala environment.
tags:
  - xgboost
  - cross-validation
  - hyperparameter-tuning
  - mllib
timestamp: "2026-06-18T15:32:09.533Z"
---

# XGBoost Hyperparameter Tuning with MLlib Cross-Validation

**XGBoost hyperparameter tuning with MLlib cross-validation** refers to the process of using Apache Spark's MLlib cross-validation framework to systematically search for optimal hyperparameters for an [XGBoost](/concepts/xgboostspark-module.md) model. This approach integrates the gradient boosting algorithm with Spark's distributed computing infrastructure, enabling parallel evaluation of multiple parameter configurations across a cluster.^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Overview

Cross-validation is a standard technique for model selection that evaluates the performance of different hyperparameter configurations by splitting the training data into folds and computing average validation metrics. MLlib provides a `CrossValidator` class that automates this process, and it can be directly applied to XGBoost models embedded in an ML pipeline.^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Workflow

### Embedding XGBoost in an ML Pipeline

The first step is to wrap an XGBoost estimator inside an MLlib ML pipeline. This allows the cross-validation process to treat the XGBoost model as a standard PipelineStage, enabling seamless integration with Spark's [feature engineering](/concepts/featureengineeringclient-api.md) and model evaluation components.^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

### Specifying a Parameter Grid

A grid of candidate hyperparameters is defined by the user. Common XGBoost parameters to tune include:

- **`maxDepth`** – Maximum tree depth, controlling model complexity and overfitting risk.
- **`eta`** (learning rate) – Step size shrinkage to prevent overfitting.
- **`subsample`** – Fraction of training data sampled per tree, enabling stochastic gradient boosting.
- **`colsample_bytree`** – Fraction of features sampled for each tree, reducing correlation between trees.
- **`min_child_weight`** – Minimum sum of instance weight in a child node, controlling node splitting.
- **`gamma`** – Minimum loss reduction required for a partition, acting as a regularization parameter.
- **`lambda`** and **`alpha`** – L2 and L1 regularization terms on weights.
- **`numRound`** – Number of boosting rounds, controlling ensemble size.^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md, xgboost-gpu-gpu.md]

### Executing Cross-Validation

The `CrossValidator` evaluates each combination of parameters using `k`-fold cross-validation (typically `k=3` or `k=5`). For each fold, it trains an XGBoost model on the training partition and evaluates it on the validation partition using a user-specified evaluation metric (e.g., AUC, RMSE, log loss). The metric scores are averaged across folds to produce a stable estimate of out-of-sample performance.^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

### Selecting the Best Model

After evaluating all combinations in the parameter grid, the `CrossValidator` selects the configuration that achieved the best average metric score. A new XGBoost model is then retrained on the entire dataset using that optimal set of hyperparameters. The resulting model can be saved, deployed, or used for [batch inference](/concepts/batch-inference-on-databricks.md) or streaming inference.^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Example: XGBoost Regression with Cross-Validation

The example notebook "XGBoost regression with cross-validation" demonstrates this workflow end-to-end using a regression dataset. The key steps are:^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

1. **Load and prepare data** into a Spark DataFrame with feature columns and a label column.
2. **Define an XGBoostRegressor** with configurable hyperparameters.
3. **Build an MLlib pipeline** that applies feature transformers (e.g., VectorAssembler) and the XGBoost estimator.
4. **Create a ParamGridBuilder** with a set of candidate values for tunable parameters.
5. **Configure a [CrossValidator](/concepts/crossvalidator.md)** with the pipeline, parameter grid, and an evaluator (e.g., RegressionEvaluator with `metricName = "rmse"`).
6. **Fit the cross-validator** to the training data. The fitting process distributes the training of all fold models across the cluster.
7. **Extract the best model** from the fitted cross-validator using `bestModel`, and inspect its summary (e.g., feature importance, training metrics).
8. **Make predictions** on test data with the tuned model.

## Best Practices

- **Start with a coarse grid**, then refine around promising regions to reduce compute cost.^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]
- **Use [GPU acceleration](/concepts/gpu-accelerated-xgboost-training.md)** when available by setting the `gpu_id` parameter and ensuring the cluster has GPU-enabled instances.^[xgboost-gpu-gpu.md]
- **Monitor training metrics** with [MLflow](/concepts/mlflow.md) to track experiments, compare runs, and visualize learning curves.^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]
- **Set `num_workers`** to match the number of executors in the Spark cluster for optimal parallelism.^[xgboost-gpu-gpu.md]
- **Consider early stopping** via the `maximizeEvaluationOn` parameter in the XGBoostTrainer to automatically stop unpromising runs, reducing wasted compute.^[previous-section]

## Scalability Considerations

When tuning on very large datasets or wide parameter grids, consider:
- **[Hyperopt](/concepts/hyperopt.md) integration** – Databricks supports [Hyperopt](/concepts/hyperopt.md) for Bayesian optimization over larger search spaces, which can be more efficient than grid search.^[hyperparameter-tuning-with-hyperopt-on-databricks-databricks-on-aws.md]
- **Manual tuning for small datasets** – Grid search with cross-validation may be overkill for small datasets; manual exploration often suffices.^[previous-section]
- **Automated Machine Learning (AutoML)** – Databricks AutoML can automatically explore XGBoost configurations and return a tuned model with minimal user input.^[automated-ml-on-databricks-databricks-on-aws.md]

## Related Concepts

- XGBoost model training
- [MLlib pipeline](/concepts/mllib-pipelines-api.md)
- [CrossValidator](/concepts/crossvalidator.md)
- ParamGridBuilder
- Hyperparameter optimization
- [Model selection](/concepts/custom-judge-model-selection.md)
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md)
- [GPU acceleration for XGBoost](/concepts/gpu-accelerated-xgboost-training.md)

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
2. xgboost-gpu-gpu.md
3. previous-section
4. hyperparameter-tuning-with-hyperopt-on-databricks-databricks-on-aws.md
5. automated-ml-on-databricks-databricks-on-aws.md
