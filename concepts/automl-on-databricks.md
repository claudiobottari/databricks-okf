---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0908abb1a4ef39e3bda1e559a3cf3ec817a20b5fe5d72547a6d112b365129a93
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
    - machine-learning-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - automl-on-databricks
    - AOD
    - AutoML (Databricks)
    - AutoML in Databricks
    - AutoML Regression on Databricks
    - AutoML Training on Databricks
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
    - file: machine-learning-on-databricks-databricks-on-aws.md
    - file: model-training-examples-databricks-on-aws.md
title: AutoML on Databricks
description: A no-code UI and Python API feature that automatically finds the best algorithm and hyperparameter configuration for machine learning datasets.
tags:
  - databricks
  - automl
  - machine-learning
timestamp: "2026-06-19T18:14:58.849Z"
---

# AutoML on Databricks

**AutoML on Databricks** is a managed service that automates the process of building high-quality machine learning models. It handles dataset preparation, algorithm selection, and hyperparameter tuning with minimal manual intervention, offering both a no-code UI and a Python API. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md, machine-learning-on-databricks-databricks-on-aws.md]

## Overview

AutoML simplifies the end-to-end ML workflow by automatically finding the best algorithm and hyperparameter configuration for a given dataset. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md] It is designed to help users quickly build models without deep expertise in algorithm selection or tuning, while still providing full transparency and reproducibility.

## Capabilities

AutoML performs the following tasks automatically:

- **Data preparation**: Prepares the dataset for model training, including feature engineering and preprocessing. ^[model-training-examples-databricks-on-aws.md]
- **Algorithm search**: Runs a series of trials using popular open-source libraries such as scikit-learn and XGBoost to evaluate different algorithms. ^[model-training-examples-databricks-on-aws.md]
- **Hyperparameter tuning**: Performs automated hyperparameter optimization to improve model performance. ^[machine-learning-on-databricks-databricks-on-aws.md]

AutoML offers both a **no-code UI** for point-and-click model building and a **Python API** for programmatic access and integration into workflows. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## How It Works

When you run AutoML, it evaluates multiple combinations of algorithms and hyperparameters over the provided dataset. Each trial is executed using the compute resources of the [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md), which includes pre-built ML and deep learning libraries. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

After the trials complete, AutoML creates a Python notebook for each trial run. These notebooks contain the source code used to produce the model, allowing you to review, reproduce, and modify the code. ^[model-training-examples-databricks-on-aws.md]

## Access and Usage

- **UI**: Available from the Databricks workspace under the Machine Learning section. Users can upload data, select the target column, and start an AutoML experiment with a few clicks.
- **API**: Use the `databricks.automl` Python package to start experiments programmatically, enabling integration with [Lakeflow Jobs](/concepts/lakeflow-jobs.md) and other automated workflows.

## Outputs

AutoML produces:

- A set of trained models with associated metrics.
- Python notebooks for every trial, providing full code transparency.
- An MLflow experiment that tracks all runs, parameters, and metrics, making it easy to compare models and promote the best one.

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The pre-configured runtime that powers AutoML trials.
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – The underlying optimization process used by AutoML.
- [Feature Engineering](/concepts/featureengineeringclient-api.md) – Automated feature preprocessing part of the AutoML pipeline.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Used to log and compare AutoML experiment runs.
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) – Can orchestrate AutoML workflows in production.
- Machine Learning on Databricks – The broader ML platform that includes AutoML.

## Sources

- databricks-runtime-for-machine-learning-databricks-on-aws.md
- machine-learning-on-databricks-databricks-on-aws.md
- model-training-examples-databricks-on-aws.md

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
2. [machine-learning-on-databricks-databricks-on-aws.md](/references/machine-learning-on-databricks-databricks-on-aws-34650b43.md)
3. [model-training-examples-databricks-on-aws.md](/references/model-training-examples-databricks-on-aws-47a05943.md)
