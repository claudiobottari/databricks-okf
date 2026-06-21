---
title: Model training examples | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/training-examples
ingestedAt: "2026-06-18T08:13:43.129Z"
---

This section includes examples showing how to train machine learning models on Databricks using many popular open-source libraries.

You can also use [AutoML](https://docs.databricks.com/aws/en/machine-learning/automl/), which automatically prepares a dataset for model training, performs a set of trials using open-source libraries such as scikit-learn and XGBoost, and creates a Python notebook with the source code for each trial run so you can review, reproduce, and modify the code.

## Machine learning examples[​](#machine-learning-examples "Direct link to Machine learning examples")

Package

Notebook(s)

Features

scikit-learn

[Machine learning tutorial](https://docs.databricks.com/aws/en/machine-learning/train-model/scikit-learn#basic-example)

Unity Catalog, classification model, MLflow, automated hyperparameter tuning with Hyperopt and MLflow

scikit-learn

[End-to-end example](https://docs.databricks.com/aws/en/machine-learning/train-model/scikit-learn#e2e-example)

Unity Catalog, classification model, MLflow, automated hyperparameter tuning with Hyperopt and MLflow, XGBoost

MLlib

[MLlib examples](https://docs.databricks.com/aws/en/machine-learning/train-model/mllib)

Binary classification, decision trees, GBT regression, Structured Streaming, custom transformer

xgboost

[XGBoost examples](https://docs.databricks.com/aws/en/machine-learning/train-model/xgboost)

Python, PySpark, and Scala, single node workloads and distributed training

## Hyperparameter tuning examples[​](#hyperparameter-tuning-examples "Direct link to Hyperparameter tuning examples")

For general information about hyperparameter tuning in Databricks, see [Hyperparameter tuning](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/).

note

The open-source version of [Hyperopt](https://github.com/hyperopt/hyperopt) is no longer being maintained.

Hyperopt is not included in Databricks Runtime for Machine Learning after 16.4 LTS ML. Databricks recommends using either [Optuna](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/optuna) for single-node optimization or [RayTune](https://docs.ray.io/en/latest/tune/index.html) for a similar experience to the deprecated Hyperopt distributed hyperparameter tuning functionality. Learn more about using [RayTune](https://docs.databricks.com/aws/en/machine-learning/ray/ray-mlflow) on Databricks.
