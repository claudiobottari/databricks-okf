---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44664fc559d7273119d25f3b30b58397f5694ecb723dab5eb4ef6775fd0b7fb4
  pageDirectory: concepts
  sources:
    - classic-machine-learning-databricks-on-aws.md
    - tutorial-end-to-end-classic-ml-models-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - end-to-end-ml-workflow-on-databricks
    - EMWOD
    - MLOps workflow recommended by Databricks
  citations:
    - file: tutorial-end-to-end-classic-ml-models-on-databricks-databricks-on-aws.md
    - file: classic-machine-learning-databricks-on-aws.md
title: End-to-End ML Workflow on Databricks
description: A complete machine learning pipeline pattern covering data ingestion, preprocessing, model training, prediction, visualization, and evaluation within the Databricks environment.
tags:
  - workflow
  - machine-learning
  - databricks
  - pipeline
timestamp: "2026-06-19T09:12:47.066Z"
---

# End-to-End ML Workflow on Databricks

An **End-to-End ML Workflow on Databricks** refers to the complete lifecycle of building, training, evaluating, deploying, and serving a machine learning model entirely within the Databricks platform. This integrated workflow leverages Databricks’ collaborative notebooks, managed compute (including GPU clusters), and [MLflow](/concepts/mlflow.md) for experiment tracking, model registry, and inference, allowing data scientists and engineers to move from raw data to production predictions without leaving the environment. ^[tutorial-end-to-end-classic-ml-models-on-databricks-databricks-on-aws.md, classic-machine-learning-databricks-on-aws.md]

## Typical Stages of an End-to-End ML Workflow

While workflows vary by problem domain, a complete end-to-end ML project on Databricks commonly includes the following stages, as illustrated in the official classic ML tutorial: ^[tutorial-end-to-end-classic-ml-models-on-databricks-databricks-on-aws.md]

1. **Data Loading and Exploration** – Ingest raw data from files, tables, or external sources and perform visualisation to understand distributions and relationships.
2. **Preprocessing and Feature Engineering** – Clean, transform, and create features suitable for modeling.
3. **Model Training with Hyperparameter Optimisation** – Run parallel training experiments, often using distributed hyperparameter tuning to find the best model configuration.
4. **Experiment Tracking with MLflow** – Automatically log parameters, metrics, artifacts, and models during each run, enabling comparison and reproducibility.
5. **Model Registration** – Promote the chosen model to the [MLflow Model Registry](/concepts/mlflow-model-registry.md), where it can be versioned, staged, and governed.
6. **Inference on New Data** – Deploy the registered model for batch scoring or real-time serving. In the classic tutorial, inference is demonstrated by applying the registered model to new data using a Spark UDF.

## Example: Classic ML (XGBoost) Tutorial

The official tutorial notebook presents a complete end-to-end example for a traditional ML task using XGBoost. It walks through loading the dataset, performing visual data analysis, setting up parallel hyperparameter optimisation with tools like [Hyperopt](/concepts/hyperopt.md) or Spark’s built-in cross-validation, and then using MLflow to review results, register the best model, and perform inference on unseen data via a Spark UDF. The notebook is available in both MLflow 3 (Unity Catalog) and MLflow 2.x variants. ^[tutorial-end-to-end-classic-ml-models-on-databricks-databricks-on-aws.md]

## Example: Time Series Forecasting with GluonTS

For deep learning use cases, Databricks also provides an end-to-end workflow for probabilistic time-series forecasting. A notebook demonstrates how to use GluonTS’s DeepAR model on a serverless GPU cluster, covering data ingestion, resampling, model training, prediction generation, visualisation of forecasts, and quantitative evaluation. This example highlights the platform’s ability to support GPU-accelerated training and specialised libraries within an end-to-end pipeline. ^[classic-machine-learning-databricks-on-aws.md]

## Benefits of an Integrated Workflow

By keeping the entire workflow within Databricks, teams gain:
- **Unified environment** – No context switching between data engineering, experimentation, and deployment tools.
- **Built-in collaboration** – Notebooks and [Unity Catalog](/concepts/unity-catalog.md) facilitate sharing and governance across roles.
- **Scalable compute** – Clusters can be dynamically adjusted for data processing, training, and serving.
- **Reproducibility** – MLflow captures the full lineage of runs, models, and parameters.

These advantages reduce friction and accelerate the time from data to deployment.

## Related Concepts

- Classic Machine Learning on Databricks
- [Deep Learning on Databricks (GPU)](/concepts/deep-learning-on-databricks.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Model Registry](/concepts/mlflow-model-registry.md)
- Spark UDF for Inference
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md)
- Time Series Forecasting with GluonTS

## Sources

- tutorial-end-to-end-classic-ml-models-on-databricks-databricks-on-aws.md
- classic-machine-learning-databricks-on-aws.md

# Citations

1. [tutorial-end-to-end-classic-ml-models-on-databricks-databricks-on-aws.md](/references/tutorial-end-to-end-classic-ml-models-on-databricks-databricks-on-aws-c4680c06.md)
2. [classic-machine-learning-databricks-on-aws.md](/references/classic-machine-learning-databricks-on-aws-838aa327.md)
