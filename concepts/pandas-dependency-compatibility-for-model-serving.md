---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3706158d7d7b6f7e13677f01f74e2c11360d5d9a5f4faab9d0c4ed4cc1f1cdfa
  pageDirectory: concepts
  sources:
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pandas-dependency-compatibility-for-model-serving
    - PDCFMS
  citations:
    - file: forecasting-with-automl-classic-compute-databricks-on-aws.md
title: Pandas Dependency Compatibility for Model Serving
description: Known issue where AutoML-built models can fail in Model Serving due to incompatible pandas versions, resolved by adding pandas==1.5.3 dependency via a provided script
tags:
  - troubleshooting
  - model-serving
  - pandas
  - compatibility
timestamp: "2026-06-18T12:24:15.940Z"
---

# Pandas Dependency Compatibility for Model Serving

**Pandas Dependency Compatibility for Model Serving** refers to the version mismatch between the `pandas` library used during model training (particularly with AutoML) and the `pandas` version available in the [Model Serving](/concepts/model-serving.md) endpoint environment. This incompatibility can cause runtime errors when serving models, most commonly the `No module named 'pandas.core.indexes.numeric'` error. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Error

When serving a model built using AutoML with Model Serving, you may encounter the following error:

```
No module named 'pandas.core.indexes.numeric'
```

^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Cause

This error occurs because of an incompatible `pandas` version between the AutoML training environment and the model serving endpoint environment. The model was trained with a version of `pandas` that includes the `pandas.core.indexes.numeric` module, but the serving environment has a different version that does not include this module or has a different module structure. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Solution

Resolve the error by editing the logged model's dependencies to include the appropriate `pandas` version: `pandas==1.5.3`. This can be done using the [add-pandas-dependency.py script](https://docs.databricks.com/aws/en/assets/files/add-pandas-dependency-4808dc9dcdfb035bdca6ebce6b86d719.py), which modifies the `requirements.txt` and `conda.yaml` files for the logged model. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Steps

1. Modify the script to include the `run_id` of the [MLflow Run](/concepts/mlflow-run.md) where your model was logged.
2. Re-register the model to [Unity Catalog](/concepts/unity-catalog.md) or the [Model Registry](/concepts/mlflow-model-registry.md).
3. Try serving the new version of the MLflow model.

^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Related Concepts

- AutoML — The automated machine learning tool that can produce models with pandas dependency issues
- [Model Serving](/concepts/model-serving.md) — The deployment environment where the pandas version mismatch manifests
- MLflow Models — The model format that stores dependency specifications in `requirements.txt` and `conda.yaml`
- [Model Registry](/concepts/mlflow-model-registry.md) — Where models are registered before deployment
- [Unity Catalog](/concepts/unity-catalog.md) — Recommended destination for model registration

## Sources

- forecasting-with-automl-classic-compute-databricks-on-aws.md

# Citations

1. [forecasting-with-automl-classic-compute-databricks-on-aws.md](/references/forecasting-with-automl-classic-compute-databricks-on-aws-20de86d0.md)
