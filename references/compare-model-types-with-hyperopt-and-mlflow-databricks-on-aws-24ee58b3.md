---
title: Compare model types with Hyperopt and MLflow | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/hyperopt-model-selection
ingestedAt: "2026-06-18T08:09:49.494Z"
---

*   [](https://docs.databricks.com/aws/en/)
*   [Machine learning](https://docs.databricks.com/aws/en/machine-learning/)
*   [Train models](https://docs.databricks.com/aws/en/machine-learning/train-model/)
*   [Databricks Runtime ML](https://docs.databricks.com/aws/en/machine-learning/databricks-runtime-ml)
*   [Model training examples](https://docs.databricks.com/aws/en/machine-learning/train-model/training-examples)
*   [Hyperparameter tuning](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/)
*   Compare model types with Hyperopt and MLflow

Last updated on **May 6, 2026**

note

The open-source version of [Hyperopt](https://github.com/hyperopt/hyperopt) is no longer being maintained.

Hyperopt is not included in Databricks Runtime for Machine Learning after 16.4 LTS ML. Databricks recommends using either [Optuna](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/optuna) for single-node optimization or [RayTune](https://docs.ray.io/en/latest/tune/index.html) for a similar experience to the deprecated Hyperopt distributed hyperparameter tuning functionality. Learn more about using [RayTune](https://docs.databricks.com/aws/en/machine-learning/ray/ray-mlflow) on Databricks.

This notebook demonstrates how to tune the hyperparameters for multiple models and arrive at a best model overall. It uses Hyperopt with `SparkTrials` to compare three model types, evaluating model performance with a different set of hyperparameters appropriate for each model type.

#### Compare models using scikit-learn, Hyperopt, and MLflow notebook
