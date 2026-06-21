---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7e5e3ba8fd7114fd3582298a4f2c0df706e082972bba1a2142e5be42d43783d2
  pageDirectory: concepts
  sources:
    - automl-python-api-reference-databricks-on-aws.md
    - machine-learning-on-databricks-databricks-on-aws.md
    - model-training-examples-databricks-on-aws.md
    - what-is-automl-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-automl
  citations:
    - file: what-is-automl-databricks-on-aws.md
title: Databricks AutoML
description: Automated machine learning system on Databricks that trains models and generates trial notebooks for classification, regression, and forecasting tasks.
tags:
  - machine-learning
  - automl
  - databricks
timestamp: "2026-06-19T22:12:16.760Z"
---

---
title: Databricks AutoML
summary: Automated machine learning on Databricks that prepares datasets, runs trials using open-source libraries (scikit-learn, XGBoost), and generates reproducible Python notebooks.
sources:
  - model-training-examples-databricks-on-aws.md
  - what-is-automl-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T19:45:31.887Z"
updatedAt: "2026-06-19T19:45:31.887Z"
tags:
  - machine-learning
  - automl
  - databricks
aliases:
  - databricks-automl
confidence: 0.95
provenanceState: merged
inferredParagraphs: 1
---

# Databricks AutoML

**Databricks AutoML** simplifies the process of applying machine learning to datasets by automatically finding the best algorithm and hyperparameter configuration. It is designed for data scientists and analysts who want to quickly build high-quality models without manually iterating through algorithms and tuning parameters. ^[what-is-automl-databricks-on-aws.md]

## How Does AutoML Work?

When you provide a dataset and specify the type of machine learning problem, Databricks AutoML performs the following steps:

1. **Cleans and prepares** your data for training.
2. **Orchestrates distributed model training** and hyperparameter tuning across multiple algorithms.
3. **Finds the best model** using open-source evaluation algorithms from scikit-learn, [XGBoost](/concepts/xgboostspark-module.md), LightGBM, Prophet, and ARIMA.
4. **Presents the results**, including generated source code notebooks for each trial, allowing you to review, reproduce, and modify the code as needed. ^[what-is-automl-databricks-on-aws.md]

You can start AutoML experiments through a low-code UI for regression, classification, or [forecasting](/concepts/forecast.md), or via the [Python API](https://docs.databricks.com/aws/en/machine-learning/automl/regression-train-api). ^[what-is-automl-databricks-on-aws.md]

## Machine Learning Problem Types

AutoML supports three main categories of machine learning problems:

- **Regression**: Predicting continuous numeric values. ^[what-is-automl-databricks-on-aws.md]
- **Classification**: Predicting categorical labels. ^[what-is-automl-databricks-on-aws.md]
- **Forecasting**: Predicting future values based on time series data. ^[what-is-automl-databricks-on-aws.md]

Each problem type has dedicated documentation and UI workflows for getting started. ^[what-is-automl-databricks-on-aws.md]

## Algorithms

AutoML trains and evaluates models based on several open-source libraries. For classification and regression models, the decision tree, random forests, logistic regression, and linear regression with stochastic gradient descent algorithms are based on scikit-learn. ^[what-is-automl-databricks-on-aws.md]

The full set of algorithms includes:

- scikit-learn (decision trees, random forests, logistic regression, linear regression with SGD)
- [XGBoost](/concepts/xgboostspark-module.md)
- LightGBM
- Prophet (for forecasting)
- ARIMA (for forecasting) ^[what-is-automl-databricks-on-aws.md]

## Notebook Generation

Classic compute AutoML generates notebooks containing the source code behind each trial so you can review, reproduce, and modify the code as needed. ^[what-is-automl-databricks-on-aws.md]

- **Forecasting experiments**: AutoML-generated notebooks are automatically imported to your workspace for all trials. ^[what-is-automl-databricks-on-aws.md]
- **Classification and regression experiments**: Notebooks for data exploration and the best trial are automatically imported. Notebooks for other trials are saved as MLflow artifacts on DBFS instead of being auto-imported. For these trials, the `notebook_path` and `notebook_url` in the `TrialInfo` Python API are not set. You can manually import them using the AutoML experiment UI or the `databricks.automl.import_notebook` Python API. ^[what-is-automl-databricks-on-aws.md]

If you only use the data exploration notebook or best trial notebook, the **Source** column in the AutoML experiment UI contains a link to the generated notebook for the best trial. ^[what-is-automl-databricks-on-aws.md]

## Model Explainability with SHAP Values

The notebooks produced by AutoML regression and classification runs include code to calculate Shapley values using the [SHAP package](https://shap.readthedocs.io/en/latest/overviews.html). Shapley values are based in game theory and estimate the importance of each feature to a model's predictions. ^[what-is-automl-databricks-on-aws.md]

Because SHAP calculations are highly memory-intensive, they are not performed by default. To enable them:

1. Go to the **Feature importance** section in an AutoML-generated trial notebook.
2. Set `shap_enabled = True`.
3. Re-run the notebook. ^[what-is-automl-databricks-on-aws.md]

Note: For MLR 11.1 and below, SHAP plots are not generated if the dataset contains a `datetime` column. ^[what-is-automl-databricks-on-aws.md]

## Requirements

- AutoML depends on the `databricks-automl-runtime` package, available on [PyPI](https://pypi.org/project/databricks-automl-runtime/). ^[what-is-automl-databricks-on-aws.md]
- No additional libraries other than those preinstalled in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) should be installed on the cluster. Any modification to existing library versions results in run failures due to incompatibility. ^[what-is-automl-databricks-on-aws.md]
- To access files in your workspace, network ports 1017 and 1021 must be open for AutoML experiments. ^[what-is-automl-databricks-on-aws.md]
- Use a compute resource with a supported compute access mode. Not all compute access modes have access to [Unity Catalog](/concepts/unity-catalog.md). ^[what-is-automl-databricks-on-aws.md]

## Availability Notes

In Databricks Runtime 18.0 ML or above, AutoML is not included as a built-in library. ^[what-is-automl-databricks-on-aws.md]

## Related Concepts

- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) — Automated optimization of model parameters using tools like Optuna and RayTune.
- [MLflow](/concepts/mlflow.md) — Tracks experiments, models, and artifacts generated by AutoML trials.
- [Feature Store](/concepts/feature-store.md) — Integration for reusing pre-computed features across models.
- [Unity Catalog](/concepts/unity-catalog.md) — Governs data access and lineage for AutoML experiments.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre-configured environment for ML workloads.

## Sources

- what-is-automl-databricks-on-aws.md
- model-training-examples-databricks-on-aws.md

# Citations

1. [what-is-automl-databricks-on-aws.md](/references/what-is-automl-databricks-on-aws-3a597bbd.md)
