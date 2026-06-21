---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 963ba494aedc1cd8c31bf0418cdd85ad3b43debe707c656512d0113871fc690b
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-skinny-vs-mlflow-on-databricks
    - MVMOD
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: mlflow-skinny vs mlflow on Databricks
description: Databricks Runtime ML includes mlflow-skinny by default, but Model Serving requires the full mlflow package; custom pyfunc models must explicitly specify mlflow in pip_requirements
tags:
  - mlflow
  - databricks
  - deployment
timestamp: "2026-06-18T11:59:49.733Z"
---

# mlflow-skinny vs mlflow on Databricks

**mlflow-skinny** is a lightweight version of the full **mlflow** package that ships by default in Databricks Runtime ML. The critical difference between the two is that `mlflow-skinny` lacks certain dependencies required by Model Serving, which can cause deployment failures if not handled properly.

## Key Differences

| Feature | mlflow-skinny | mlflow |
|---------|---------------|--------|
| Included in DBR ML by default | Yes | No |
| Full MLflow functionality | Limited | Yes |
| Model Serving compatibility | No | Yes |
| Dependency footprint | Smaller | Full |

^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## The Problem: Model Serving Requires Full mlflow

Databricks Runtime ML runtimes include `mlflow-skinny` by default rather than the full `mlflow` package. When you log a pyfunc model on one of these runtimes without specifying `pip_requirements`, MLflow captures `mlflow-skinny` in the model's `conda.yaml`. Model Serving requires `mlflow` (not `mlflow-skinny`) in `conda.yaml` and cannot build the container image otherwise. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Solution: Always Specify mlflow in pip_requirements

When calling `mlflow.pyfunc.log_model()` on a Databricks Runtime ML runtime, always specify `mlflow==<version>` in `pip_requirements`:

```python
mlflow.pyfunc.log_model(
    name="model",
    python_model=your_model,
    pip_requirements=["mlflow==3.8.1"],  # use mlflow, not mlflow-skinny
    registered_model_name="catalog.schema.model_name",
)
```

^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Related Concepts

- [Custom MLflow Python Function Models](/concepts/custom-mlflow-pythonmodel.md) — Creating custom pyfunc models for deployment
- [Model Serving](/concepts/model-serving.md) — Deploying models to serving endpoints
- MLflow pyfunc — The Python function model flavor in MLflow
- MLflow Models — The MLflow model format and its requirements

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
