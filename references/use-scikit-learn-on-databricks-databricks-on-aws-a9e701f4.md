---
title: Use scikit-learn on Databricks | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/scikit-learn
ingestedAt: "2026-06-18T08:13:34.841Z"
---

This page provides examples of how you can use the `scikit-learn` package to train machine learning models in Databricks. [scikit-learn](https://scikit-learn.org/stable/index.html) is one of the most popular Python libraries for single-node machine learning and is included in Databricks Runtime and Databricks Runtime ML. See [Databricks Runtime release notes](https://docs.databricks.com/aws/en/release-notes/runtime/) for the scikit-learn library version included with your cluster's runtime.

You can [import these notebooks](https://docs.databricks.com/aws/en/notebooks/notebook-export-import#import-notebook) and run them in your Databricks workspace.

## Basic example using scikit-learn[​](#basic-example-using-scikit-learn "Direct link to basic-example-using-scikit-learn")

This notebook provides a quick overview of machine learning model training on Databricks. It uses the `scikit-learn` package to train a simple classification model. It also illustrates the use of [MLflow](https://docs.databricks.com/aws/en/mlflow/) to track the model development process, and [Optuna](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/#optuna-overview) to automate hyperparameter tuning.

prompt

Tell Genie Code (Agent mode) to do this for you:

    Create tables in Unity Catalog for these datasets and then use those tables to train a classification model to predict wine quality./databricks-datasets/wine-quality/winequality-white.csv and /databricks-datasets/wine-quality/winequality-red.csv

If your workspace is enabled for Unity Catalog, use this version of the notebook:

#### scikit-learn classification notebook (Unity Catalog)

If your workspace is not enabled for Unity Catalog, use this version of the notebook:

#### scikit-learn classification notebook

## End-to-end example using scikit-learn on Databricks[​](#end-to-end-example-using-scikit-learn-on-databricks "Direct link to end-to-end-example-using-scikit-learn-on-databricks")

This notebook uses scikit-learn to illustrate a complete end-to-end example of loading data, model training, distributed hyperparameter tuning, and model inference. It also illustrates model lifecycle management using MLflow Model Registry to log and register your model.

If your workspace is enabled for Unity Catalog, use this version of the notebook:

#### Use scikit-learn with MLflow integration on Databricks (Unity Catalog)

If your workspace is not enabled for Unity Catalog, use this version of the notebook:

#### Use scikit-learn with MLflow integration on Databricks
