---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef7c4df4ee757ab72e98940e00bb54033741f57c1d42b17794eb3237cd7ac0ea
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-models-on-databricks-model-serving
    - CMODMS
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Custom models on Databricks Model Serving
description: Any Python ML model or custom code deployable as a production-grade API on Databricks using CPU or GPU compute, logged in MLflow format and registered in Unity Catalog or workspace registry.
tags:
  - machine-learning
  - model-serving
  - databricks
timestamp: "2026-06-19T18:03:40.868Z"
---

```markdown
---
title: Custom Models on Databricks Model Serving
summary: Any Python ML model or custom code deployable as a production-grade API on Databricks using CPU or GPU compute, logged in MLflow format and registered in Unity Catalog or workspace registry.
sources:
  - custom-models-overview-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:57:29.225Z"
updatedAt: "2026-06-18T14:57:29.225Z"
tags:
  - machine-learning
  - databricks
  - model-serving
aliases:
  - custom-models-on-databricks-model-serving
  - CMODMS
confidence: 0.99
provenanceState: extracted
inferredParagraphs: 0
---

# Custom Models on Databricks Model Serving

**Custom Models on Databricks Model Serving** refers to the capability to deploy any Python-based machine learning model or custom Python code as a production-grade API endpoint using Databricks Model Serving. This feature supports both CPU and GPU compute resources and works with models trained using standard ML libraries such as scikit-learn, XGBoost, PyTorch, and HuggingFace Transformers. ^[custom-models-overview-databricks-on-aws.md]

## Overview

Model Serving can deploy any Python model or custom code as a scalable API. Databricks refers to these as **custom models**, distinguishing them from [[Foundation Model APIs]] and [[External Models]] which serve pre-built or third-party models. Custom models can include any Python code and are logged in the MLflow format before deployment. ^[custom-models-overview-databricks-on-aws.md]

## Deployment Workflow

Deploying a custom model follows a three-step process:

1. **Log the model** in MLflow format using either native [[MLflow Model Flavors|MLflow built-in flavors]] or the pyfunc interface for arbitrary Python code.
2. **Register the model** in the [[Unity Catalog]] (recommended) or the workspace model registry.
3. **Create a serving endpoint** to deploy and query the model. ^[custom-models-overview-databricks-on-aws.md]

For a complete tutorial, see Model Serving Tutorial.

## Logging ML Models

### Autologging

When using [[Databricks Runtime for ML]], autologging is automatically enabled. Models are logged without explicit `log_model` calls. ^[custom-models-overview-databricks-on-aws.md]

### Built-in Flavors

Manual logging with MLflow's built-in flavors provides more detailed control:

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

### Custom pyfunc Models

For deploying arbitrary Python code or additional code alongside a model, use the `pyfunc` interface:

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

### Signatures and Input Examples

Adding a model signature and input example is recommended. Signatures are required for logging models to Unity Catalog. ^[custom-models-overview-databricks-on-aws.md]

```python
from mlflow.models.signature import infer_signature

signature = infer_signature(training_data, model.predict(training_data))
mlflow.sklearn.log_model(model, "model", signature=signature)

input_example = {"feature1": 0.5, "feature2": 3}
mlflow.sklearn.log_model(model, "model", input_example=input_example)
```

^[custom-models-overview-databricks-on-aws.md]

## Compute Types

Model Serving provides a variety of CPU and GPU options. When deploying with a GPU, code must be configured to run predictions on the GPU using framework-specific methods. MLflow handles this automatically for models logged with PyTorch or Transformers flavors. ^[custom-models-overview-databricks-on-aws.md]

The `CPU_MEDIUM` and `CPU_LARGE` workload types allow trading concurrency for more memory per worker on the same CPU hardware, useful when models need more memory than standard `CPU` provides. ^[custom-models-overview-databricks-on-aws.md]

## Deployment Container and Dependencies

During deployment, a production-grade container is built that includes libraries automatically captured or specified in the MLflow model. The base image includes some system-level dependencies, but application-level dependencies must be explicitly specified. ^[custom-models-overview-databricks-on-aws.md]

### Package Dependencies

For MLflow native flavor models, package dependencies are automatically captured. For custom `pyfunc` models, dependencies can be added explicitly using:

- **`pip_requirements` parameter**: `mlflow.sklearn.log_model(model, "sklearn-model", pip_requirements=["scikit-learn", "numpy"])`
- **`conda_env` parameter**: Specify a conda environment dictionary
- **`extra_pip_requirements`**: Add requirements beyond what is automatically captured

^[custom-models-overview-databricks-on-aws.md]

### Code Dependencies

Code dependencies can be specified using `code_path`:

```python
mlflow.sklearn.log_model(model, "sklearn-model", code_path=["path/to/helper_functions.py"])
```

^[custom-models-overview-databricks-on-aws.md]

For custom or private libraries, see [[Custom Libraries for Databricks Model Serving|Use Custom Python Libraries with Model Serving]]. For validation before deployment, see [[Pre-deployment Validation for Model Serving]]. ^[custom-models-overview-databricks-on-aws.md]

## Expectations and Limitations

### Endpoint Creation and Updates

- **Deployment time**: Approximately 10 minutes, but may take longer depending on model complexity, size, and dependencies. ^[custom-models-overview-databricks-on-aws.md]
- **Zero-downtime updates**: Databricks keeps the existing endpoint configuration active until the new one is ready. During this transition, you are billed for both configurations. ^[custom-models-overview-databricks-on-aws.md]
- **Request timeout**: Requests time out if model computation exceeds 597 seconds. ^[custom-models-overview-databricks-on-aws.md]
- **System maintenance**: Databricks performs occasional zero-downtime system updates. Models must be robust enough to reload at any time. ^[custom-models-overview-databricks-on-aws.md]

### Endpoint Scaling

- **Provisioned concurrency**: Maximum number of parallel requests. Estimate using: provisioned concurrency = queries per second (QPS) × model execution time (s). ^[custom-models-overview-databricks-on-aws.md]
- **Scaling behavior**: Endpoints scale up almost immediately with increased traffic and scale down every five minutes to match reduced traffic. ^[custom-models-overview-databricks-on-aws.md]
- **Scale to zero**: Optional feature that scales endpoints down to zero after 30 minutes of inactivity. The first request after scaling experiences a "cold start" with higher latency (usually 10‑20 seconds, but can be minutes). No SLA applies. ^[custom-models-overview-databricks-on-aws.md]
- **Route optimization**: Recommended for high QPS and low latency use cases. See [[Route Optimization for Serving Endpoints|Route Optimization on Serving Endpoints]]. ^[custom-models-overview-databricks-on-aws.md]
- **Express deployments**: Available for faster endpoint deployment. See [[Express Deployments for Model Serving|Express Deployments for Model Serving Endpoints]]. ^[custom-models-overview-databricks-on-aws.md]

> **Warning**: Scale to zero should not be used for production workloads requiring consistent uptime or guaranteed response times. ^[custom-models-overview-databricks-on-aws.md]

### GPU Workload Limitations

- Container image creation for GPU serving takes longer than CPU serving due to model size and increased installation requirements. ^[custom-models-overview-databricks-on-aws.md]
- Very large model deployments may timeout if container build and deployment exceed 60 minutes, or may fail with "No space left on device" errors. For large language models, use [[Foundation Model APIs]] instead. ^[custom-models-overview-databricks-on-aws.md]
- Autoscaling for GPU serving takes longer than for CPU serving. ^[custom-models-overview-databricks-on-aws.md]
- GPU capacity is not guaranteed when scaling to zero, and endpoints may experience extra high latency for the first request after scaling. ^[custom-models-overview-databricks-on-aws.md]

## Anaconda Licensing for Legacy Models

This section applies only to models logged with MLflow v1.17 or earlier (Databricks Runtime 8.3 ML or earlier). Models logged before MLflow v1.18 used the conda `defaults` channel by default. Due to Anaconda Inc.'s updated terms of service, Databricks now uses `conda-forge` as the default channel for models logged with MLflow v1.18 and above. ^[custom-models-overview-databricks-on-aws.md]

To check if a legacy model has a `defaults` channel dependency, examine the `channel` value in the model's `conda.yaml` file. To change the channel, re-register the model with a new `conda.yaml` using the `conda_env` parameter of `log_model()`. ^[custom-models-overview-databricks-on-aws.md]

## Related Concepts

- [[Custom Model Serving Endpoint Support|Create Custom Model Serving Endpoints]]
- Query Serving Endpoints for Custom Models
- Debugging Guide for Model Serving
- [[Custom Libraries for Databricks Model Serving|Use Custom Python Libraries with Model Serving]]
- Package Custom Artifacts for Model Serving
- [[MLflow Model Serving and Deployment|Deploy Python Code with Model Serving]]
- [[Route Optimization for Serving Endpoints|Route Optimization on Serving Endpoints]]
- [[Express Deployments for Model Serving|Express Deployments for Model Serving Endpoints]]
- Configure Access to Resources from Model Serving Endpoints
- [[Instance Profile for Model Serving Endpoints|Add an Instance Profile to a Model Serving Endpoint]]
- [[Foundation Model APIs]]
- [[External Models]]
- MLflow Built-in Flavors
- Pyfunc
- [[Unity Catalog]]

## Sources

- custom-models-overview-databricks-on-aws.md
```

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
