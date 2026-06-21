---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d5bfe038bebbb3c7daf86a4bca4ec3c9b9d062952e7e55f959aba840d49747dd
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
    - tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-model-logging-for-serving
    - MMLFS
  citations:
    - file: custom-models-overview-databricks-on-aws.md
    - file: tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md
title: MLflow Model Logging for Serving
description: "Methods for logging ML models in MLflow format for deployment: autologging, built-in flavors, pyfunc custom logging, with required signatures and input examples for Unity Catalog."
tags:
  - mlflow
  - model-logging
  - databricks
timestamp: "2026-06-18T11:26:50.515Z"
---

# MLflow Model Logging for Serving

**MLflow Model Logging for Serving** refers to the process of recording trained machine learning models — along with their dependencies, metadata, and inference logic — in the MLflow format so they can be deployed as production-grade API endpoints using [Model Serving on Databricks](/concepts/model-serving-on-databricks.md). Proper logging is the first critical step in the custom model serving workflow. ^[custom-models-overview-databricks-on-aws.md]

## Overview

Before a model can be served as an API endpoint on Databricks, it must be logged in the MLflow format and registered in either [Unity Catalog](/concepts/unity-catalog.md) (recommended) or the workspace [MLflow Model Registry](/concepts/mlflow-model-registry.md). After registration, you can create a model serving endpoint to deploy and query the model. ^[custom-models-overview-databricks-on-aws.md, tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md]

## Logging Methods

MLflow provides several approaches for logging models, each suited to different use cases. ^[custom-models-overview-databricks-on-aws.md]

### Autologging

Autologging is automatically enabled when using [Databricks Runtime for ML](/concepts/databricks-runtime-for-ml.md). It captures models, parameters, metrics, and artifacts without requiring explicit logging calls. ^[custom-models-overview-databricks-on-aws.md]

```python
import mlflow
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_iris

iris = load_iris()
model = RandomForestRegressor()
model.fit(iris.data, iris.target)
```

^[custom-models-overview-databricks-on-aws.md]

### Logging with Built-in Flavors

MLflow provides built-in flavors for popular ML libraries including scikit-learn, [XGBoost](/concepts/xgboostspark-module.md), PyTorch, and [HuggingFace Transformers](/concepts/hugging-face-transformers-trainer.md). Manual logging offers more detailed control over what is captured. ^[custom-models-overview-databricks-on-aws.md]

```python
import mlflow
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

iris = load_iris()
model = RandomForestClassifier()
model.fit(iris.data, iris.target)

with mlflow.start_run():
    mlflow.sklearn.log_model(model, "random_forest_classifier")
```

^[custom-models-overview-databricks-on-aws.md]

### Custom Logging with pyfunc

The MLflow pyfunc flavor allows deployment of arbitrary Python code or additional logic alongside a model. This is useful when you need custom preprocessing, postprocessing, or inference logic. ^[custom-models-overview-databricks-on-aws.md]

```python
import mlflow
import mlflow.pyfunc

class Model(mlflow.pyfunc.PythonModel):
    def predict(self, context, model_input):
        return model_input * 2

with mlflow.start_run():
    mlflow.pyfunc.log_model("custom_model", python_model=Model())
```

^[custom-models-overview-databricks-on-aws.md]

### Logging Transformer Models

For generative AI and NLP models, you can log using the transformer flavor and specify inference configuration parameters: ^[tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md]

```python
with mlflow.start_run():
    model_info = mlflow.transformers.log_model(
        transformers_model=text_generation_pipeline,
        artifact_path="my_sentence_generator",
        inference_config=inference_config,
        registered_model_name='gpt2',
        input_example=input_example,
        signature=signature
    )
```

^[tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md]

## Signatures and Input Examples

Adding a model signature and input example to logged models is recommended. Signatures are required for logging models to Unity Catalog and help ensure that input data matches the expected format at inference time. ^[custom-models-overview-databricks-on-aws.md]

The following demonstrates inferring a signature from training data: ^[custom-models-overview-databricks-on-aws.md]

```python
from mlflow.models.signature import infer_signature

signature = infer_signature(training_data, model.predict(training_data))
mlflow.sklearn.log_model(model, "model", signature=signature)
```

Input examples provide sample data that can be used to test the endpoint after deployment: ^[custom-models-overview-databricks-on-aws.md]

```python
input_example = {"feature1": 0.5, "feature2": 3}
mlflow.sklearn.log_model(model, "model", input_example=input_example)
```

## Dependencies and Packaging

During deployment, a production-grade container is built that includes libraries automatically captured or explicitly specified in the MLflow model. The base image includes some system-level dependencies, but application-level dependencies must be explicitly included. ^[custom-models-overview-databricks-on-aws.md]

### Package Dependencies

For MLflow native flavor models, necessary package dependencies are automatically captured. For custom `pyfunc` models, dependencies can be explicitly added using several parameters: ^[custom-models-overview-databricks-on-aws.md]

**Using `pip_requirements`:**
```python
mlflow.sklearn.log_model(model, "sklearn-model",
    pip_requirements=["scikit-learn", "numpy"])
```

**Using `conda_env`:**
```python
conda_env = {
    'channels': ['defaults'],
    'dependencies': [
        'python=3.7.0',
        'scikit-learn=0.21.3'
    ],
    'name': 'mlflow-env'
}
mlflow.sklearn.log_model(model, "sklearn-model", conda_env=conda_env)
```

**Using `extra_pip_requirements`:**
```python
mlflow.sklearn.log_model(model, "sklearn-model",
    extra_pip_requirements=["sklearn_req"])
```

^[custom-models-overview-databricks-on-aws.md]

### Code Dependencies

Custom or private libraries and helper functions can be included using the `code_path` parameter: ^[custom-models-overview-databricks-on-aws.md]

```python
mlflow.sklearn.log_model(model, "sklearn-model",
    code_path=["path/to/helper_functions.py"])
```

See [Use custom Python libraries with Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md) for details on private library support.

## Post-Logging Validation

Before deploying a model, validate that all required dependencies are properly captured. If dependencies are missing, you may encounter errors during deployment. Databricks recommends testing the model locally when facing deployment issues. ^[custom-models-overview-databricks-on-aws.md]

See [Pre-deployment Validation for Model Serving](/concepts/pre-deployment-validation-for-model-serving.md) for validation and dependency update guidance.

## Registration

After logging, the model should be registered in either Unity Catalog or the workspace MLflow Model Registry. Unity Catalog is the recommended approach for production workloads as it provides centralized governance, auditing, and access control. ^[custom-models-overview-databricks-on-aws.md, tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md]

## Next Steps

After logging and registering the model, you can: ^[tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md]

- [Create custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md) — Deploy the model as an API endpoint
- [Query serving endpoints for custom models](/concepts/model-serving-endpoint-custom-models.md) — Send scoring requests
- Debugging guide for Model Serving — Troubleshoot deployment issues

## Related Concepts

- [MLflow Built-in Model Flavors](/concepts/mlflow-model-flavors.md) — Standardized model formats for popular libraries
- MLflow pyfunc — Custom Python model flavor for arbitrary code
- [Unity Catalog](/concepts/unity-catalog.md) — Centralized governance and model registry
- [Model Registry](/concepts/mlflow-model-registry.md) — Workspace-level model management
- [Model Signature](/concepts/model-signatures-in-unity-catalog.md) — Schema definition for model inputs and outputs
- [Compute Types for Model Serving](/concepts/compute-types-for-databricks-model-serving.md) — CPU and GPU options for deployment
- [Deployment Container and Dependencies](/concepts/deployment-container-and-dependencies.md) — How containers are built for serving

## Sources

- custom-models-overview-databricks-on-aws.md
- tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
2. [tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md](/references/tutorial-deploy-and-query-a-custom-model-databricks-on-aws-16c7ace5.md)
