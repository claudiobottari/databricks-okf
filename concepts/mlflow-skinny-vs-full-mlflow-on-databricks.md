---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d38aca4aad11ea9d688ac31df7db613d918504f36eff1d7a02bf8bced193eae
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-skinny-vs-full-mlflow-on-databricks
    - MVFMOD
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: MLflow-Skinny vs Full MLflow on Databricks
description: Databricks Runtime ML includes mlflow-skinny by default, not full mlflow; custom pyfunc models must explicitly specify mlflow in pip_requirements to ensure Model Serving container compatibility.
tags:
  - databricks
  - mlflow
  - dependency-management
timestamp: "2026-06-19T18:30:59.622Z"
---

# MLflow-Skinny vs Full MLflow on Databricks

When deploying and serving models on Databricks, it is critical to understand the difference between **MLflow-Skinny** (the minimal MLflow package) and **Full MLflow** (the complete MLflow package), particularly regarding [Model Serving](/concepts/model-serving.md) compatibility.

## What is MLflow-Skinny?

**MLflow-Skinny** is a lightweight version of the MLflow package that ships by default with Databricks Runtime ML (Databricks Machine Learning Runtime). It contains only the core MLflow tracking and logging components, omitting several dependencies that are required for model deployment and serving. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## The Compatibility Problem

When you log a custom PyFunc model using `mlflow.pyfunc.log_model()` on a Databricks Runtime ML without explicitly specifying `pip_requirements`, MLflow automatically captures `mlflow-skinny` in the model's `conda.yaml`. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

**Model Serving requires `mlflow` (the full package) — not `mlflow-skinny` — in the model's `conda.yaml`.** If `conda.yaml` contains `mlflow-skinny`, the serving infrastructure cannot build the necessary container image for deployment. This results in deployment failures. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## The Solution

Always specify `mlflow==<version>` explicitly in the `pip_requirements` parameter when calling `mlflow.pyfunc.log_model()` on a Databricks Runtime ML runtime. This ensures that the full `mlflow` package (including all serving dependencies) is captured in the model's environment specification. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Correct Usage Example

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

^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## What Full MLflow Provides

The full `mlflow` package includes all the dependencies necessary for:
- Model serving container image creation
- Model deployment to [Model Serving endpoints](/concepts/model-serving-endpoint.md)
- Advanced inference capabilities
- Complete model registry functionality

## Impact on Custom PyFunc Models

This consideration is especially important when deploying [Custom Python Function Models](/concepts/custom-mlflow-pythonmodel.md) that include preprocessing logic, postprocessing logic, or custom branching behavior in the `predict` function. These custom models require the full MLflow environment to be properly served. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Related Concepts

- PyFunc model — The MLflow Python function model format for custom deployment
- [Model Serving](/concepts/model-serving.md) — The deployment infrastructure that requires full MLflow
- [Custom Python Function Models](/concepts/custom-mlflow-pythonmodel.md) — Advanced model deployment patterns
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The runtime environment that ships with mlflow-skinny
- Model Deployment Validation — Best practice to verify serving capability before deployment

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
