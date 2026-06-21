---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8871aea631ceb72515abea49f251e32b2ff275777f2d5dfd0b5f662788c7d871
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
    - regression-with-automl-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - automl-model-registration-and-deployment
    - Deployment and AutoML Model Registration
    - AMRAD
    - Model Registration and Deployment
  citations:
    - file: classification-with-automl-databricks-on-aws.md
    - file: regression-with-automl-databricks-on-aws.md
    - file: train-regression-models-with-automl-python-api-databricks-on-aws.md
title: AutoML Model Registration and Deployment
description: Process for registering AutoML-generated models to Unity Catalog or Model Registry and deploying to model serving endpoints
tags:
  - databricks
  - automl
  - mlflow
  - model-serving
timestamp: "2026-06-19T17:43:44.876Z"
---

# AutoML Model Registration and Deployment

**AutoML Model Registration and Deployment** refers to the workflow of taking the best-performing model produced by an AutoML experiment (classification, regression, or forecasting) and making it available for production use via [Unity Catalog](/concepts/unity-catalog.md) or the [Model Registry](/concepts/mlflow-model-registry.md), followed by deployment to a [Model Serving](/concepts/model-serving.md) endpoint. ^[classification-with-automl-databricks-on-aws.md, regression-with-automl-databricks-on-aws.md]

## Registering a Model from the AutoML UI

After an AutoML experiment completes, the top row of the runs table shows the best model based on the primary evaluation metric. To register it:

1. Select the link in the **Models** column for the model you want to register.
2. Click the **register model** button to open a dialog where you can register the model to either **Unity Catalog** or the **Model Registry**. ^[classification-with-automl-databricks-on-aws.md, regression-with-automl-databricks-on-aws.md]

Databricks recommends registering models to Unity Catalog for the latest features. ^[classification-with-automl-databricks-on-aws.md, regression-with-automl-databricks-on-aws.md] Registration to Unity Catalog makes the model discoverable and governable under Unity Catalog's data governance framework, including access control and lineage tracking. Registration to the legacy Model Registry is also supported but not recommended for new projects.

## Deploying a Model

Once a model is registered, you can deploy it to a custom model serving endpoint. In the AutoML UI, after registration, you are given a link to create a serving endpoint for that model. Alternatively, you can navigate to the [Model Serving](/concepts/model-serving.md) page in the workspace and create an endpoint using the registered model version. ^[classification-with-automl-databricks-on-aws.md, regression-with-automl-databricks-on-aws.md]

## Registering and Deploying via the Python API

When using the AutoML Python API (e.g., `automl.classify()` or `automl.regress()`), the best model is returned as part of the `summary` object. The best trial's model path is accessible via `summary.best_trial.model_path`. You can register and deploy this model using standard [MLflow](/concepts/mlflow.md) Model Registry workflows. See Log, load, and register MLflow models for detailed instructions. ^[train-regression-models-with-automl-python-api-databricks-on-aws.md]

## Known Issue: `pandas.core.indexes.numeric` Error

When serving a model built using AutoML with [Model Serving](/concepts/model-serving.md), you may encounter the error `No module named 'pandas.core.indexes.numeric'`. This is caused by an incompatible `pandas` version between the AutoML training environment and the model serving endpoint environment. ^[classification-with-automl-databricks-on-aws.md, regression-with-automl-databricks-on-aws.md, train-regression-models-with-automl-python-api-databricks-on-aws.md]

To resolve the issue:

1. Download and run the [add-pandas-dependency.py script](https://docs.databricks.com/aws/en/assets/files/add-pandas-dependency-4808dc9dcdfb035bdca6ebce6b86d719.py). The script edits the `requirements.txt` and `conda.yaml` files of the logged MLflow model to include `pandas==1.5.3`. ^[classification-with-automl-databricks-on-aws.md, regression-with-automl-databricks-on-aws.md, train-regression-models-with-automl-python-api-databricks-on-aws.md]
2. Modify the script to include the `run_id` of the [MLflow Run](/concepts/mlflow-run.md) where your model was logged. ^[classification-with-automl-databricks-on-aws.md, regression-with-automl-databricks-on-aws.md, train-regression-models-with-automl-python-api-databricks-on-aws.md]
3. Re-register the model to Unity Catalog or the Model Registry. ^[classification-with-automl-databricks-on-aws.md, regression-with-automl-databricks-on-aws.md, train-regression-models-with-automl-python-api-databricks-on-aws.md]
4. Deploy the new version. ^[classification-with-automl-databricks-on-aws.md, regression-with-automl-databricks-on-aws.md, train-regression-models-with-automl-python-api-databricks-on-aws.md]

## Related Concepts

- AutoML — Automated machine learning for classification, regression, and forecasting.
- [Unity Catalog](/concepts/unity-catalog.md) — The recommended model registry for governance and discoverability.
- [Model Registry](/concepts/mlflow-model-registry.md) — Legacy model versioning and stage management.
- [Model Serving](/concepts/model-serving.md) — Deployment platform for serving models as REST endpoints.
- [MLflow](/concepts/mlflow.md) — Framework used by AutoML for experiment tracking and model packaging.
- Classification with AutoML
- Regression with AutoML
- Forecasting with AutoML

## Sources

- classification-with-automl-databricks-on-aws.md
- regression-with-automl-databricks-on-aws.md
- train-regression-models-with-automl-python-api-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
2. [regression-with-automl-databricks-on-aws.md](/references/regression-with-automl-databricks-on-aws-cc5aa3d0.md)
3. [train-regression-models-with-automl-python-api-databricks-on-aws.md](/references/train-regression-models-with-automl-python-api-databricks-on-aws-b83f8bc4.md)
