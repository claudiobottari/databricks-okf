---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 836e9af818c37f256fa14f189cb129ec4c8c0878c5b7a08ae26b1484124b85b0
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-pandas-compatibility-issue
    - APCI
  citations:
    - file: classification-with-automl-databricks-on-aws.md
title: AutoML Pandas Compatibility Issue
description: Known pandas version incompatibility error when serving AutoML models, with resolution via a dependency-fix script
tags:
  - databricks
  - automl
  - troubleshooting
  - pandas
timestamp: "2026-06-19T17:43:45.896Z"
---

# AutoML Pandas Compatibility Issue

The **AutoML Pandas Compatibility Issue** is an error that occurs when serving a model built using AutoML with [Model Serving](/concepts/model-serving.md) on Databricks. The error arises from an incompatible version of the `pandas` library between the AutoML training environment and the model serving endpoint environment.^[classification-with-automl-databricks-on-aws.md]

## Error Message

When this issue occurs, the model serving endpoint returns the following error:

```
No module named 'pandas.core.indexes.numeric'
```

^[classification-with-automl-databricks-on-aws.md]

## Cause

The error is caused by a version mismatch in the `pandas` dependency. The AutoML training process logs the model with a certain version of pandas, but the model serving endpoint environment uses a different version that lacks the `pandas.core.indexes.numeric` module.^[classification-with-automl-databricks-on-aws.md]

## Resolution

You can resolve this error by running the [add-pandas-dependency.py script](https://docs.databricks.com/aws/en/assets/files/add-pandas-dependency-4808dc9dcdfb035bdca6ebce6b86d719.py). This script edits the `requirements.txt` and `conda.yaml` files for your logged model to include the appropriate pandas dependency version: `pandas==1.5.3`.^[classification-with-automl-databricks-on-aws.md]

### Steps

1. **Modify the script** to include the `run_id` of the [MLflow Run](/concepts/mlflow-run.md) where your model was logged.^[classification-with-automl-databricks-on-aws.md]
2. **Re-register the model** to [Unity Catalog](/concepts/unity-catalog.md) or the [Model Registry](/concepts/mlflow-model-registry.md). Databricks recommends registering models to Unity Catalog for the latest features.^[classification-with-automl-databricks-on-aws.md]
3. **Try serving the new version** of the MLflow model.^[classification-with-automl-databricks-on-aws.md]

## Related Concepts

- AutoML — Automated machine learning tool for classification, regression, and forecasting
- [Model Serving](/concepts/model-serving.md) — Infrastructure for deploying MLflow models to production endpoints
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Repository for managing model versions and lifecycle
- [Unity Catalog](/concepts/unity-catalog.md) — Databricks' unified governance solution for data and AI assets
- Classification with AutoML — Specific AutoML workflow for classification problems

## Sources

- classification-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
