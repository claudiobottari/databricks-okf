---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7fa48e90faedc64a84b9be41b6d8dddcfe9ad9f43af2de83670def13a7481ffd
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-skinny-vs-mlflow-compatibility-on-databricks
    - MVMCOD
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: mlflow-skinny vs mlflow Compatibility on Databricks
description: The critical requirement that Databricks Model Serving needs the full mlflow package (not mlflow-skinny) in conda.yaml when deploying custom pyfunc models from Databricks Runtime ML
tags:
  - databricks
  - mlflow
  - troubleshooting
timestamp: "2026-06-19T10:11:57.623Z"
---

Here is the wiki page for "mlflow-skinny vs mlflow Compatibility on Databricks".

---

## mlflow-skinny vs mlflow Compatibility on Databricks

**mlflow-skinny vs mlflow Compatibility on Databricks** refers to the critical distinction between the lightweight `mlflow-skinny` package (which ships by default in Databricks Runtime ML) and the full `mlflow` package required by [Model Serving](/concepts/model-serving.md) for container image builds. Using the wrong package when logging a model can cause deployment failures.

## Overview

Databricks Runtime ML runtimes include `mlflow-skinny` by default rather than the full `mlflow` package. `mlflow-skinny` is a minimal installation that omits many dependencies (such as server-side components and certain model flavors) to reduce the runtime footprint. However, [Model Serving](/concepts/model-serving.md) requires the full `mlflow` package to build the container image for serving. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## The Compatibility Problem

When you log a custom MLflow PyFunc model using `mlflow.pyfunc.log_model()` on a Databricks Runtime ML runtime without explicitly specifying `pip_requirements`, MLflow automatically captures the packages from the current environment. Because the environment contains `mlflow-skinny` (not `mlflow`), the model's `conda.yaml` will list `mlflow-skinny` as a dependency. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

Model Serving cannot build the container image when `conda.yaml` specifies `mlflow-skinny` instead of `mlflow`. This results in a deployment failure. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Solution

Always specify `mlflow==<version>` in the `pip_requirements` parameter when calling `mlflow.pyfunc.log_model()` on a Databricks Runtime ML runtime. This overrides the automatic capture of `mlflow-skinny` and ensures the full `mlflow` package is included in the model's environment. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Example

```python
import mlflow

mlflow.pyfunc.log_model(
    name="model",
    python_model=your_model,
    pip_requirements=["mlflow==3.8.1"],  # use mlflow, not mlflow-skinny
    registered_model_name="catalog.schema.model_name",
)
```

^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Best Practices

- **Always specify `pip_requirements` explicitly** when logging `pyfunc` models on Databricks Runtime ML. This avoids the automatic capture of `mlflow-skinny`.
- **Use the same MLflow version** that is available in the Databricks Runtime ML version you are using. Check the Databricks documentation for the specific MLflow version bundled with your runtime.
- **Test locally before deploying** to Model Serving. Use `mlflow.models.predict()` to validate that the model loads and predicts correctly with the specified dependencies. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Related Concepts

- MLflow PyFunc Model — The custom Python function model format used for deployment.
- [Model Serving](/concepts/model-serving.md) — The Databricks service that requires the full `mlflow` package.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The runtime that ships `mlflow-skinny` by default.
- Custom Model Deployment — General guidance for deploying custom Python code.
- MLflow Model Logging — The process of packaging and logging models with MLflow.

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
