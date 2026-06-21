---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 244939847cf5a6ba989f5500377448c8055575441d745bdb2c94bec2871fbdca
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-skinny-vs-mlflow-serving-compatibility
    - MVMSC
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: mlflow-skinny vs mlflow Serving Compatibility
description: Databricks Runtime ML ships with mlflow-skinny by default; custom pyfunc models must explicitly specify the full mlflow package in pip_requirements to be deployable on Model Serving.
tags:
  - databricks
  - mlflow
  - model-serving
  - compatibility
timestamp: "2026-06-18T15:27:05.579Z"
---

# mlflow-skinny vs mlflow Serving Compatibility

**mlflow-skinny vs mlflow Serving Compatibility** describes a critical deployment requirement when using Databricks: custom MLflow Python function (`pyfunc`) models logged on Databricks Runtime ML must explicitly depend on the full `mlflow` package, not the default `mlflow-skinny` package, to be deployable via Model Serving.

## The Compatibility Issue

Databricks Runtime ML includes `mlflow-skinny` by default rather than the full `mlflow` package. When you log a `pyfunc` model on one of these runtimes without specifying `pip_requirements`, MLflow automatically captures `mlflow-skinny` in the model's `conda.yaml` environment specification. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

Model Serving requires the full `mlflow` package (not `mlflow-skinny`) in `conda.yaml` and cannot build the container image otherwise. This results in a deployment failure. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Solution

Always specify `mlflow==<version>` in `pip_requirements` when you call `mlflow.pyfunc.log_model()` on a Databricks Runtime ML runtime. This overrides the default dependency capture and ensures the full `mlflow` package is included for serving compatibility. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
# DBR ML ships with mlflow-skinny by default, so specify mlflow explicitly
# to ensure Model Serving compatibility.
mlflow.pyfunc.log_model(
    name="model",
    python_model=your_model,
    pip_requirements=["mlflow==3.8.1"],  # use mlflow, not mlflow-skinny
    registered_model_name="catalog.schema.model_name",
)
```

## Best Practices

- **Always set `pip_requirements` explicitly** when logging `pyfunc` models from Databricks Runtime ML environments.
- **Match the MLflow version** in `pip_requirements` to the version that your model code was developed against.
- **Test serving locally** before deploying to production to catch dependency issues early. See the MLflow documentation on [validating models before deployment](https://www.mlflow.org/docs/latest/models.html#validate-models-before-deployment).

## Related Concepts

- [Custom MLflow Python Function Models](/concepts/custom-mlflow-pythonmodel.md) — The `pyfunc` framework for deploying arbitrary Python code
- [Model Serving](/concepts/model-serving.md) — The deployment infrastructure for serving models
- Custom pyfunc model deployment — General guide for deploying custom Python models
- MLflow conda.yaml — The environment specification file for model dependencies
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The runtime that ships with `mlflow-skinny` by default

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
