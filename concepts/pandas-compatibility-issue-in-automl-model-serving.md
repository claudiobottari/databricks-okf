---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 897ff9ee57f3be45c122d9da4ae96521d91738ea4c8ba391c66a0d48e14c4a5a
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pandas-compatibility-issue-in-automl-model-serving
    - PCIIAMS
  citations:
    - file: classification-with-automl-databricks-on-aws.md
title: Pandas Compatibility Issue in AutoML Model Serving
description: Known incompatibility between pandas version used by AutoML training and the model serving environment, resolved by editing the logged model's dependencies to include pandas==1.5.3.
tags:
  - automl
  - troubleshooting
  - pandas
  - databricks
timestamp: "2026-06-19T14:12:15.892Z"
---

# Pandas Compatibility Issue in AutoML Model Serving

The **Pandas Compatibility Issue in AutoML Model Serving** is a known error that occurs when serving a model built using AutoML with [Model Serving](/concepts/model-serving.md) on Databricks. The error manifests as `No module named 'pandas.core.indexes.numeric'` due to an incompatible `pandas` version between the AutoML training environment and the model serving endpoint environment.^[classification-with-automl-databricks-on-aws.md]

## Error Message

When serving a model built using AutoML, the following error may appear:

```
No module named 'pandas.core.indexes.numeric'
```

^[classification-with-automl-databricks-on-aws.md]

## Cause

AutoML models are trained in an environment that uses one version of `pandas`, while the model serving endpoint may use a different, incompatible version. This version mismatch causes the `No module named 'pandas.core.indexes.numeric'` error during model serving.^[classification-with-automl-databricks-on-aws.md]

## Resolution

The issue can be resolved by explicitly adding the correct `pandas` dependency to the logged model's environment files. The recommended approach is to run the `add-pandas-dependency.py` script, which edits the `requirements.txt` and `conda.yaml` files for the logged model to include the appropriate `pandas` dependency version: `pandas==1.5.3`.^[classification-with-automl-databricks-on-aws.md]

### Steps to Resolve

1. Download and run the [add-pandas-dependency.py script](https://docs.databricks.com/aws/en/assets/files/add-pandas-dependency-4808dc9dcdfb035bdca6ebce6b86d719.py).
2. Modify the script to include the `run_id` of the [MLflow](/concepts/mlflow.md) run where your model was logged.
3. Re-register the model to [Unity Catalog](/concepts/unity-catalog.md) or the [Model Registry](/concepts/mlflow-model-registry.md).
4. Attempt to serve the new version of the MLflow model.

^[classification-with-automl-databricks-on-aws.md]

## Prevention

To avoid this issue, it is recommended to ensure that the `pandas` version used during model training is compatible with the serving environment. Registering models to [Unity Catalog](/concepts/unity-catalog.md) is also recommended for the latest features and better compatibility management.^[classification-with-automl-databricks-on-aws.md]

## Related Concepts

- AutoML — Automated machine learning for model development
- [Model Serving](/concepts/model-serving.md) — Deploying models for inference
- [MLflow](/concepts/mlflow.md) — Model lifecycle management
- [Unity Catalog](/concepts/unity-catalog.md) — Recommended model registry for latest features
- [Model Registry](/concepts/mlflow-model-registry.md) — Alternative model management option
- Classification with AutoML — The primary AutoML use case affected by this issue

## Sources

- classification-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
