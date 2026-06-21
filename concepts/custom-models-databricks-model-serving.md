---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 272f42ef2bbfa20bb6925eaa191c2e9bfdc163bcc7ef5288e8af11f64faf4297
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-models-databricks-model-serving
    - CM(MS
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Custom Models (Databricks Model Serving)
description: Any Python ML model or custom code deployed as a production-grade API on Databricks using CPU or GPU compute resources, logged in MLflow format and registered in Unity Catalog or workspace registry.
tags:
  - machine-learning
  - model-serving
  - databricks
  - deployment
timestamp: "2026-06-19T14:40:06.725Z"
---

# Custom Models (Databricks Model Serving)

**Custom models** are any Python machine learning model or arbitrary Python code that can be deployed as a production-grade API using Databricks [Model Serving](/concepts/model-serving.md). These models can be trained with standard ML libraries (scikit‑learn, XGBoost, PyTorch, HuggingFace Transformers) and can include any Python logic beyond simple prediction. Databricks supports serving custom models on both CPU and GPU compute resources. ^[custom-models-overview-databricks-on-aws.md]

## Deploying a Custom Model

To deploy a custom model:

1. **Log the model or code** in MLflow format, using either a native [MLflow built‑in flavor](https://mlflow.org/docs/latest/models.html#built-in-model-flavors) (e.g., `mlflow.sklearn`) or the generic pyfunc interface (`mlflow.pyfunc.PythonModel`).
2. **Register the model** in [Unity Catalog](/concepts/unity-catalog.md) (recommended) or the workspace model registry.
3. **Create a model serving endpoint** to deploy and query the model. See [Create custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints) and [Query serving endpoints for custom models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-custom-model-endpoints).

For a complete walkthrough, see the [Model serving tutorial](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-intro). Databricks also offers [Foundation Model APIs](/concepts/foundation-model-apis.md) for generative AI and [External Models](/concepts/external-models.md) for models hosted outside of Databricks. ^[custom-models-overview-databricks-on-aws.md]

### Logging Methods

| Method | Description | Example |
|--------|-------------|---------|
| **Autologging** | Automatically enabled in Databricks Runtime for ML. Logs models implicitly during training. | `model.fit(...)` |
| **Built‑in flavor logging** | Manual logging with explicit control over the model artifact. | `mlflow.sklearn.log_model(model, "name")` |
| **Custom pyfunc logging** | Deploy arbitrary Python code or wrap additional logic around a model. | `mlflow.pyfunc.log_model("custom", python_model=Model())` |

Adding an MLflow **signature** and **input example** is recommended. Signatures are required when logging models to Unity Catalog. ^[custom-models-overview-databricks-on-aws.md]

## Compute Type

Model Serving provides a variety of CPU and GPU workload types. When deploying with a GPU, ensure that your code runs predictions on the GPU using framework‑specific methods; MLflow handles this automatically for PyTorch and Transformers flavors. The `CPU_MEDIUM` and `CPU_LARGE` workload types let you trade concurrency for more memory per worker on the same CPU hardware. ^[custom-models-overview-databricks-on-aws.md]

## Deployment Container and Dependencies

During deployment, a production‑grade container is built. It includes libraries captured from the MLflow model. Application‑level dependencies must be explicitly specified. If dependencies are missing, deployment errors can occur; Databricks recommends testing the model locally before deployment. ^[custom-models-overview-databricks-on-aws.md]

### Package and Code Dependencies

- **Package dependencies**: For native MLflow flavors, dependencies are auto‑captured. For pyfunc models, add dependencies via:
  - `pip_requirements` parameter (list of packages)
  - `conda_env` parameter (dictionary defining conda environment)
  - `extra_pip_requirements` parameter (additional packages beyond auto‑captured ones)
- **Code dependencies**: Use `code_path` parameter to point to helper Python files.
- **Custom or private libraries**: Can be added using the [custom Python libraries feature](https://docs.databricks.com/aws/en/machine-learning/model-serving/private-libraries-model-serving).

^[custom-models-overview-databricks-on-aws.md]

## Expectations and Limitations

The following apply specifically to custom model endpoints (not foundation or external models).

### Endpoint Creation and Updates

- **Deployment time**: Typically ~10 minutes, but longer for complex models.
- **Zero‑downtime updates**: Databricks keeps the existing endpoint running until the new one is ready. During this transition you are billed for both configurations.
- **Request timeout**: Requests that exceed **597 seconds** will time out.

> Databricks performs occasional zero‑downtime system maintenance. If a model fails to reload during maintenance, the update is marked as failed and the existing configuration continues serving. Ensure your models are robust and can reload at any time.

^[custom-models-overview-databricks-on-aws.md]

### Scaling Behavior

- **Provisioned concurrency**: The maximum parallel requests the system can handle. Estimate using: `provisioned concurrency = QPS × model execution time (s)`.
- **Scaling up**: Almost immediate with increased traffic.
- **Scaling down**: Every five minutes to match reduced traffic.
- **Scale to zero** (optional): After 30 minutes of inactivity, the endpoint can scale to zero. The first request after a cold start has higher latency (typically 10–20 seconds, but can be minutes). No SLA applies to scale‑from‑zero latency. **Not recommended for production workloads** that require consistent uptime or guaranteed response times.
- **Route optimization**: Recommended for high QPS and low‑latency use cases (see Route Optimization).
- **Express deployments**: Available for faster endpoint deployment (see [Express Deployments](/concepts/express-deployments-databricks.md)).

^[custom-models-overview-databricks-on-aws.md]

### GPU Workload Limitations

- Container image creation for GPU serving takes longer than for CPU.
- Very large models may time out (container build + deployment > 60 minutes) or fail with "No space left on device" error. For large language models, use [Foundation Model APIs](/concepts/foundation-model-apis.md) instead.
- Autoscaling for GPU is slower than for CPU.
- GPU capacity is not guaranteed when scaling to zero; the first request after a cold start may have extra high latency.

^[custom-models-overview-databricks-on-aws.md]

## Anaconda Licensing Notice (Legacy Models)

This section applies only to models logged with MLflow v1.17 or earlier (Databricks Runtime 8.3 ML or earlier). Anaconda Inc. updated its terms of service; commercial licenses may be required for using Anaconda channels. MLflow models logged before v1.18 defaulted to the `defaults` channel. Later versions default to `conda‑forge`. If your model has an unintended `defaults` dependency, you can re‑register the model with a new `conda.yaml` specifying a different channel via the `conda_env` parameter of `log_model()`. ^[custom-models-overview-databricks-on-aws.md]

## Additional Resources

- [Create custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints)
- [Query serving endpoints for custom models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-custom-model-endpoints)
- [Debugging guide for Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-debug)
- [Use custom Python libraries with Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/private-libraries-model-serving)
- [Package custom artifacts for Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-custom-artifacts)
- [Deploy Python code with Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/deploy-custom-python-code)
- [Route optimization on serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/route-optimization)
- [Express deployments for model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/express-deployments)
- [Configure access to resources from model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving)
- [Pre‑deployment validation for Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-pre-deployment-validation)

## Related Concepts

- MLflow Models
- [Model Serving](/concepts/model-serving.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Pyfunc
- Route Optimization
- [Express Deployments](/concepts/express-deployments-databricks.md)
- [External Models](/concepts/external-models.md)

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
