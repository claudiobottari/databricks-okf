---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6118498d657a2136abdd6982fa46275ac2cd592c894a4a51bf5ea3f93ec27af4
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
    - log-model-dependencies-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-skinny-vs-full-mlflow-in-databricks-runtime-ml
    - MVFMIDRM
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
    - file: log-model-dependencies-databricks-on-aws.md
title: Mlflow-Skinny vs Full Mlflow in Databricks Runtime ML
description: DBR ML ships with mlflow-skinny by default, but Model Serving requires the full mlflow package in conda.yaml; pip_requirements must specify mlflow explicitly.
tags:
  - databricks
  - mlflow
  - dependency-management
  - troubleshooting
timestamp: "2026-06-19T15:11:01.428Z"
---

# Mlflow-Skinny vs Full Mlflow in Databricks Runtime ML

**Mlflow-Skinny vs Full Mlflow in Databricks Runtime ML** describes the difference between the two MLflow package variants available in the Databricks ecosystem and the implications of using `mlflow-skinny` (the default on Databricks Runtime ML) when logging and serving models.

## Overview

Databricks Runtime ML (DBR ML) ships with `mlflow-skinny` by default rather than the full `mlflow` package. `mlflow-skinny` is a lightweight version that omits certain dependencies (such as `pandas`, `scikit-learn`, and others) to reduce the runtime footprint. While `mlflow-skinny` is sufficient for basic tracking and logging operations, it lacks some components that are required for model serving. ^[deploy-python-code-with-model-serving-databricks-on-aws.md, log-model-dependencies-databricks-on-aws.md]

## Problem: Model Serving Compatibility

When you log a `pyfunc` model on a DBR ML runtime **without explicitly specifying `pip_requirements`**, MLflow automatically infers the dependencies and captures `mlflow-skinny` in the model’s `conda.yaml`. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]  

Model Serving (the [Model Serving](/concepts/model-serving.md) endpoint) requires the full `mlflow` package in the environment to build the container image. If `conda.yaml` contains only `mlflow-skinny`, the serving infrastructure cannot resolve the required `mlflow` module and fails to create the endpoint. ^[deploy-python-code-with-model-serving-databricks-on-aws.md, log-model-dependencies-databricks-on-aws.md]

## Solution: Explicitly Specify `mlflow` in `pip_requirements`

To ensure compatibility with Model Serving, always specify the full `mlflow` package in the `pip_requirements` parameter when calling `mlflow.pyfunc.log_model()` on a Databricks Runtime ML runtime. ^[deploy-python-code-with-model-serving-databricks-on-aws.md, log-model-dependencies-databricks-on-aws.md]

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

The same guidance applies when using `log_model` with built-in flavors (e.g., `mlflow.sklearn.log_model`) if the model will be served via Model Serving. For `mlflow.sklearn` and other built-in flavors that do not use the `pyfunc` format, the dependency inference may still pick up `mlflow-skinny`; best practice is to override `pip_requirements` or use `conda_env` to explicitly include the full `mlflow` package. ^[log-model-dependencies-databricks-on-aws.md]

## How the Dependency Is Captured

When `pip_requirements` is not provided, MLflow’s automatic dependency inference ([`mlflow.models.infer_pip_requirements`](https://www.mlflow.org/docs/latest/python_api/mlflow.models.html#mlflow.models.infer_pip_requirements)) scans the environment and logs the detected packages. On DBR ML the detected environment includes `mlflow-skinny` rather than `mlflow`. The resulting `requirements.txt` and `conda.yaml` therefore reference `mlflow-skinny`, which is insufficient for serving. ^[log-model-dependencies-databricks-on-aws.md]

## Runtimes Affected

The issue applies to all [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) versions. Databricks recommends using the same runtime version for serving as was used during training, but the key point is that `mlflow-skinny` is always the default. Always explicitly include `mlflow` in dependencies when logging models that will be served. ^[deploy-python-code-with-model-serving-databricks-on-aws.md, log-model-dependencies-databricks-on-aws.md]

## Other Considerations for Custom Models

- **Additional dependencies**: For libraries not automatically detected, use `extra_pip_requirements` instead of overriding all requirements. See [Log Model Dependencies](/concepts/mlflow-model-dependency-logging.md).
- **Custom code**: If your model uses custom `.py` files or Python wheels, you can include them with `code_paths` (or `code_path` in MLflow 2.x). Those dependencies are handled separately and do not affect the `mlflow-skinny` issue. ^[log-model-dependencies-databricks-on-aws.md]

## Related Concepts

- MLflow pyfunc
- [Model Serving](/concepts/model-serving.md)
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md)
- [Log Model Dependencies](/concepts/mlflow-model-dependency-logging.md)
- [Deploy Python Code with Model Serving](/concepts/mlflow-model-serving-and-deployment.md)

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md
- log-model-dependencies-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
2. [log-model-dependencies-databricks-on-aws.md](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
