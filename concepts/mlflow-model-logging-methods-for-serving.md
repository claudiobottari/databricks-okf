---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bfe73868bc68fd951748ba9cdb67d6640f80377e6039c41790a5ef4aaf3d6069
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-model-logging-methods-for-serving
    - MMLMFS
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: MLflow model logging methods for serving
description: "Three approaches to log ML models for Databricks Model Serving: autologging, MLflow built-in flavors, and custom pyfunc logging — each with different trade-offs for manual control and flexibility."
tags:
  - mlflow
  - model-logging
  - machine-learning
timestamp: "2026-06-19T18:03:47.943Z"
---

```markdown
---
title: MLflow Model Logging Methods for Serving
summary: Three supported methods for logging ML models for serving — autologging, MLflow built-in flavors, and custom pyfunc logging — along with signature and input example recommendations for Unity Catalog compatibility.
sources:
  - custom-models-overview-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:57:56.074Z"
updatedAt: "2026-06-19T14:40:00.606Z"
tags:
  - mlflow
  - model-logging
  - machine-learning
aliases:
  - mlflow-model-logging-methods-for-serving
  - MMLMFS
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow Model Logging Methods for Serving

**MLflow Model Logging Methods for Serving** describes the three supported approaches for saving machine learning models in MLflow format so they can be deployed as production-grade APIs using Databricks Model Serving. The method chosen determines how dependencies are captured, how custom logic is packaged, and the level of control available to the developer.

## What Are Custom Models?

Model Serving can deploy any Python model or custom code as a production-grade API using CPU or GPU compute resources. Databricks refers to such models as **custom models**. These ML models can be trained using standard ML libraries like scikit-learn, XGBoost, PyTorch, and HuggingFace transformers and can include any Python code. ^[custom-models-overview-databricks-on-aws.md]

To deploy a custom model, you must first log the model or code in the MLflow format. After the model is logged, register it in the [[Unity Catalog]] (recommended) or the workspace registry. From there, you can create a model serving endpoint to deploy and query your model. ^[custom-models-overview-databricks-on-aws.md]

## Supported Logging Methods

### Autologging

Autologging is automatically enabled when using [[Databricks Runtime for Machine Learning]]. This method automatically logs models, parameters, metrics, and artifacts without requiring explicit `log_model` calls in your training code. ^[custom-models-overview-databricks-on-aws.md]

```python
import mlflow
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_iris

iris = load_iris()
model = RandomForestRegressor()
model.fit(iris.data, iris.target)
```

### Log Using MLflow's Built-in Flavors

This method provides more detailed control over what is logged. You manually call the `log_model` method specific to your model's framework (e.g., `mlflow.sklearn.log_model()`). MLflow automatically captures the model artifact and its package dependencies. ^[custom-models-overview-databricks-on-aws.md]

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

### Custom Logging with `pyfunc`

The PyFunc (Python Function) flavor is used for deploying arbitrary Python code or for adding custom logic alongside your model. This is the most flexible approach, as it allows you to define a custom `predict` method that can include preprocessing, postprocessing, or calls to external services. ^[custom-models-overview-databricks-on-aws.md]

```python
import mlflow
import mlflow.pyfunc

class Model(mlflow.pyfunc.PythonModel):
    def predict(self, context, model_input):
        return model_input * 2

with mlflow.start_run():
    mlflow.pyfunc.log_model("custom_model", python_model=Model())
```

## Signature and Input Examples

Adding a MLflow Model Signature and input example to the model is recommended. Signatures are **required** for logging models to the Unity Catalog. ^[custom-models-overview-databricks-on-aws.md]

```python
from mlflow.models.signature import infer_signature

signature = infer_signature(training_data, model.predict(training_data))
mlflow.sklearn.log_model(model, "model", signature=signature)
```

Input examples help document the expected input format for the model endpoint:

```python
input_example = {"feature1": 0.5, "feature2": 3}
mlflow.sklearn.log_model(model, "model", input_example=input_example)
```

## Compute Type

Model Serving provides a variety of CPU and GPU options for deploying your model. When deploying with a GPU, you must make sure that your code is set up so that predictions are run on the GPU, using the methods provided by your framework. MLflow does this automatically for models logged with the PyTorch or Transformers flavors. ^[custom-models-overview-databricks-on-aws.md]

The `CPU_MEDIUM` and `CPU_LARGE` workload types let you trade concurrency for more memory per worker on the same CPU hardware. Use them when your model needs more memory than standard `CPU` provides. ^[custom-models-overview-databricks-on-aws.md]

## Package and Code Dependencies

For MLflow native flavor models, the necessary package dependencies are automatically captured. For custom `pyfunc` models, dependencies must be explicitly added. ^[custom-models-overview-databricks-on-aws.md]

### Specifying Dependencies

**Using `pip_requirements`:**

```python
mlflow.sklearn.log_model(
    model,
    "sklearn-model",
    pip_requirements=["scikit-learn", "numpy"]
)
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

**Using `extra_pip_requirements`** to add requirements beyond what is automatically captured:

```python
mlflow.sklearn.log_model(
    model,
    "sklearn-model",
    extra_pip_requirements=["sklearn_req"]
)
```

### Code Dependencies

If you have code dependencies, these can be specified using the `code_path` parameter:

```python
mlflow.sklearn.log_model(
    model,
    "sklearn-model",
    code_path=["path/to/helper_functions.py"]
)
```

## Deployment Container

During deployment, a production-grade container is built and deployed as the endpoint. This container includes libraries automatically captured or specified in the MLflow model. The base image includes some system-level dependencies, but application-level dependencies must be explicitly specified in your MLflow model. ^[custom-models-overview-databricks-on-aws.md]

If not all required dependencies are included in the model, you might encounter dependency errors during deployment. When running into model deployment issues, Databricks recommends testing the model locally. ^[custom-models-overview-databricks-on-aws.md]

## GPU Workload Limitations

The following are limitations for serving endpoints with GPU workloads: ^[custom-models-overview-databricks-on-aws.md]

- Container image creation for GPU serving takes longer than for CPU serving due to model size and increased installation requirements.
- When deploying very large models, the deployment process might timeout if the container build and model deployment exceed 60 minutes, or the container build might fail with "No space left on device" error. For large language models, use [[Foundation Model APIs]] instead.
- Autoscaling for GPU serving takes longer than for CPU serving.
- GPU capacity is not guaranteed when scaling to zero. GPU endpoints might experience extra high latency for the first request after scaling to zero.

## Best Practices

- **Always add a signature** when logging models, especially for Unity Catalog registration.
- **Include an input example** to document the expected input format for the model endpoint.
- **Explicitly specify dependencies** for `pyfunc` models to avoid deployment failures.
- **Use [[Pre-deployment Validation for Model Serving|Pre-deployment validation]]** to verify dependencies and model compatibility before creating an endpoint.

## Related Concepts

- [[Model Serving on Databricks]] — Deploying and querying custom model endpoints
- [[Unity Catalog Model Registry]] — Registering models for deployment
- PyFunc — MLflow's Python function flavor for custom model logic
- MLflow Model Signature — Defining input and output schemas
- [[Foundation Model APIs]] — Alternative for serving large language models
- [[Express Deployments (Databricks)|Express Deployments]] — Faster endpoint deployment for custom models
- Route Optimization — Improving latency for high-throughput use cases

## Sources

- custom-models-overview-databricks-on-aws.md
```

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
